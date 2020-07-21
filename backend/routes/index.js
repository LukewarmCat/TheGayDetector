var fs = require('fs');

// https://stackoverflow.com/a/16684530
module.exports = function(app){
var walk = function(dir) {
    var results = [];
    var list = fs.readdirSync(dir);
    list.forEach(function(file) {
        file = dir + '/' + file;
        var stat = fs.statSync(file);
        if (stat && stat.isDirectory()) {
            results = results.concat(walk(file));
        } else {
            results.push(file);
        }
    });
    return results;
}

walk(__dirname).forEach((file) => {
  if(file.includes(["index.js"])) return;
  var name = file.substr(0, file.indexOf('.'));
  require(name)(app)
})
}
