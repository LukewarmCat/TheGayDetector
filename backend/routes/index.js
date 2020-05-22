var fs = require('fs');
const blacklist = ["index.js"]
module.exports = function(app){
    fs.readdirSync(__dirname).forEach(function(file) {
        if (blacklist.includes(file)) return;
        var name = file.substr(0, file.indexOf('.'));
        require('./' + name)(app);
    });
}
