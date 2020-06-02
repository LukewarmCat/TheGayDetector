const db = require("quick.db");
const passwordHash = require('password-hash');
const accounts = new db.table('accounts');
const guilds = new db.table('guilds');

module.exports = function(app) {
  app.get('/getGuildRanking/:username/:password', (req, res) => {
    if(!accounts.get(req.params.username))
      return res.send({error: "This user doesn't exist."});

    if (!passwordHash.verify(req.params.password, accounts.get(req.params.username).password))
      return res.send({error: "Incorrect username or password."});

      let ranking = [];
      guilds.all().forEach((x)=>{
         x = JSON.parse(x.data)
         ranking.push([x.totalxerty, x.name])
      })

      ranking.sort((x, y)=>{return x[0] - y[0]})


      res.send({sucess: ranking})
  });
}
