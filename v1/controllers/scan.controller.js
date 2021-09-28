/**
 * Utils
 */
const validator = require('../utils/validators.utils');
const {spawn} = require('child_process');
const error = require('../utils/returns.utils').error;
const success = require('../utils/returns.utils').success;
const Email = require('../models/email.model');
const Log = require('../models/logs.model')

function makeEmail() {
    var strValues="abcdefg12345";
    var strEmail = "";
    var strTmp;
    for (var i=0;i<10;i++) {
        strTmp = strValues.charAt(Math.round(strValues.length*Math.random()));
        strEmail = strEmail + strTmp;
    }
    strTmp = "";
    strEmail = strEmail + "@";
    for (var j=0;j<8;j++) {
        strTmp = strValues.charAt(Math.round(strValues.length*Math.random()));
        strEmail = strEmail + strTmp;
    }
    strEmail = strEmail + ".com"
    return strEmail;
}
function getRandomString(length) {
    var randomChars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var result = '';
    for ( var i = 0; i < length; i++ ) {
        result += randomChars.charAt(Math.floor(Math.random() * randomChars.length));
    }
    return result;
}
function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

//Routes
module.exports = {
    scan: function (req, res) {
        var dataToSend;
        // spawn new child process to call the python script
        const python = spawn('python3', ['/home/ubuntu/workshop-api/v1/python/app.py']);
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
            let result = JSON.parse(dataToSend)
            var test = new Log({
                mail:{
                    sender:makeEmail(),
                    content:getRandomString(300),
                    object: getRandomString(50)
                },
                results:{
                    total:getRandomInt(100),
                    sentiments:getRandomInt(33),
                    orthographe: getRandomInt(33),
                    imperatif: getRandomInt(33)
                }
            })
            test.save((err,logSaved)=>{
                if(err)console.log(err);
                console.log(logSaved)
                return res.status(200).json(success(result));
            })
        });

    },
};
