const mongoose = require('mongoose')
const Schema = mongoose.Schema;

const LogsSchema = new Schema({
    mail:{
        sender:{
            type:String,
        },
        object:{
            type:String,
        },
        content:{
            type: String,
        }
    },
    results:{
        total:{
            type: Number,
        },
        orthographe:{
            type: Number,
        },
        positivite:{
            type: Number,
        },
        alarmant:{
            type: Number,
        },
        engageant:{
            type: Number
        }
    }
},{timestamps:true});

LogsSchema.index({"sender":"text","object":"text","content":"text"})

module.exports = mongoose.model('Log',LogsSchema)
