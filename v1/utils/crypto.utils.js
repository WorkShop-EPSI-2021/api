//Modules
var crypto = require('crypto');
//Config
var SERVER_KEY = "rzIJbojc6I0blcT4qzvGGCYBpm7Tj3bx";
const IV_LENGTH = 16;

//Exported function
module.exports = {
    encrypt: function (text, key) {
        if(!text){
            return null;
        }
        try {
            var string = text.toString();
            var finalKey = crypto.createHash('sha256').update(String(SERVER_KEY + key)).digest('base64').substr(0, 32);
            let iv = crypto.randomBytes(IV_LENGTH);
            let cipher = crypto.createCipheriv('aes-256-cbc', Buffer.from(finalKey), iv);
            let encrypted = cipher.update(string);

            encrypted = Buffer.concat([encrypted, cipher.final()]);

            return iv.toString('hex') + ':' + encrypted.toString('hex');
        } catch (e) {
            return null;
        }
    },
    decrypt: function (text, key) {
        try {
            if(!text){
                return null;
            }
            var finalKey = crypto.createHash('sha256').update(String(SERVER_KEY + key)).digest('base64').substr(0, 32);
            let textParts = text.split(':');
            let iv = Buffer.from(textParts.shift(), 'hex');
            let encryptedText = Buffer.from(textParts.join(':'), 'hex');
            let decipher = crypto.createDecipheriv('aes-256-cbc', Buffer.from(finalKey), iv);
            let decrypted = decipher.update(encryptedText);

            decrypted = Buffer.concat([decrypted, decipher.final()]);

            return decrypted.toString();
        } catch (e) {
            return null;
        }
    },
    randomString: async function (length) {
        var randomChars = 'ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz123456789';
        var result = '';
        for ( var i = 0; i < length; i++ ) {
            result += randomChars.charAt(Math.floor(Math.random() * randomChars.length));
        }
        return await "MV-" + result;
    }
};