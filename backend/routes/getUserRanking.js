const db = require("quick.db");
const passwordHash = require('password-hash');
const accounts = new db.table('accounts');
const guilds = new db.table('guilds');

function isObject (item) {
  return (typeof item === "object" && !Array.isArray(item) && item !== null);
}

module.exports = function(app) {
  app.post('/getUserRanking', (req, res) => {
    if(!accounts.get(req.body.username))
      return res.send({error: "This user doesn't exist."});

    if (!passwordHash.verify(req.body.password, accounts.get(req.body.username).password))
      return res.send({error: "Incorrect username or password."});

      let ranking = [];
      accounts.all().forEach((x)=>{
        if (isObject(x.data)) {
          ranking.push([x.data.proc, x.data.name])
        } else {
          y = JSON.parse(x.data)
          ranking.push([y.proc, y.name])
       }
      })

      ranking.sort((x, y)=>{return x[0] - y[0]})


      res.send({sucess: ranking})
  });
}
