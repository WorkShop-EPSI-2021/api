const mongoose = require('mongoose')
const Schema = mongoose.Schema;
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
const EmailSchema = new Schema({
    email:{
        type: String,
        required:true,
    },
    status:{
        type: String,
        match:/^(verified|spam|neutral)$/,
        required:true,
        default:"neutral"
    }
},{timestamps:true});

EmailSchema.index({"email":"text","status":"text"})

module.exports = mongoose.model('Email',EmailSchema)