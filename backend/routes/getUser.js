const db = require("quick.db");
const passwordHash = require('password-hash');
const accounts = new db.table('accounts');
const guilds = new db.table('guilds');

module.exports = function(app) {
  app.get('/getUser/:username/:password', (req, res) => {
    if(!accounts.get(req.params.username))
      return res.send({error: "This user doesn't exist."});

    if (!passwordHash.verify(req.params.password, accounts.get(req.params.username).password))
      return res.send({error: "Incorrect username or password."});

      let player = accounts.get(req.params.username)
      if(player.guild) {
        let temp = guilds.get(player.guild.name);
        totalxerty = 0;
        temp.accounts.forEach((x)=>{
          memplayer = accounts.get(x);
          totalxerty += memplayer.proc;
        })
        temp.totalxerty = totalxerty;
        player.guild = temp;
        guilds.set(temp.name, temp)
      }


      res.send({sucess: player})
  });
}
