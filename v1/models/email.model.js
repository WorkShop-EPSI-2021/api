const mongoose = require('mongoose')
const Schema = mongoose.Schema;
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