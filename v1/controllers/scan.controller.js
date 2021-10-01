/**
 * Utils
 */
const validator = require('../utils/validators.utils');
const {spawn} = require('child_process');
const error = require('../utils/returns.utils').error;
const crypto = require('../utils/crypto.utils')
const success = require('../utils/returns.utils').success;
const Email = require('../models/email.model');
const Log = require('../models/logs.model')
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}
function roundDecimal(nombre, precision){
    var precision = precision || 2;
    var tmp = Math.pow(10, precision);
    return Math.round( nombre*tmp )/tmp;
}

//Routes
module.exports = {
    scan: function (req, res) {
        var body = req.body;
        var dataToSend;
        var sender = body.sender.substring(
            body.sender.indexOf("<") + 1,
            body.sender.lastIndexOf(">")
        );
        var email = {"objet":body.object,"text":body.content};
        //console.log(JSON.stringify(email))
        // spawn new child process to call the python script
        const python = spawn('python3', ['/home/ubuntu/workshop-api/v1/python/app.py', `${JSON.stringify(email).toString()}`]);
        // collect data from script
        python.stdout.on('data', function (data) {
            console.log('Pipe data from python script ...');
            dataToSend = data.toString();
        });
        python.stderr.on('data', function (data) {
            console.log(data.toString());
        });
        // in close event we are sure that stream from child process is closed
        python.on('close', (code) => {
            console.log(`child process close all stdio with code ${code}`);
            // send data to browser
            //var result = dataToSend.toString()
            //console.log(result)
            let result = JSON.parse(dataToSend.toString())
            var key = "F0isMOeIrU3QKY7qIesu9p2SguUC0Yvz";
            var positivite = Math.floor((100-result.positivite)/4);
            var alarmant = Math.floor((100-result.alarmant)/3);
            var orthographe = Math.floor((100-result.orthographe)/3);
            var engageant = Math.floor((100-result.engagement)/3);
            var total = engageant+orthographe+alarmant//+positivite
            var test = new Log({
                mail:{
                    sender:sender,
                    content:crypto.encrypt(body.content,key),
                    object: crypto.encrypt(body.object,key)
                },
                results:{
                    total:total,
                    //positivite: positivite,
                    orthographe: orthographe,
                    alarmant: alarmant,
                    engageant: engageant
                }
            })
            test.save((err,logSaved)=>{
                if(err)console.log(err);
                return res.status(200).json(success(logSaved._id));
            })
        });

    },
    retour: function(req,res){
        Log.findById(req.query.id,(err,logFound)=>{
            if(err)console.log(err);
            var logretour = {
                //{"title":"Positivité","value":logFound.results.positivite,"color":"#E38627"}
                result:[{"title":"Orthographe","value":logFound.results.orthographe,"color":"#C13C37"},{"title":"Engageant","value":logFound.results.engageant,"color":"#6A2135"},{"title":"Alarmant","value":logFound.results.alarmant,"color":"#E38627"}],
                total:logFound.results.total
            }
            return res.status(200).json(success(logretour))
        })
    }
};
