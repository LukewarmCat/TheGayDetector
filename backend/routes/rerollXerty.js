const db = require("quick.db");
const passwordHash = require('password-hash');
const accounts = new db.table('accounts');
const guilds = new db.table('guilds');

module.exports = function(app) {
  app.get('/rerollXerty/:username/:password', (req, res) => {
    if(!accounts.get(req.params.username))
      return res.send({error: "This user doesn't exist."});

    if (!passwordHash.verify(req.params.password, accounts.get(req.params.username).password))
      return res.send({error: "Incorrect username or password."});

      let player = accounts.get(req.params.username)

      if(player.rerollTimeout) {
        if(Date.now() < player.rerollTimeout + 86400) {
                return res.send({error: "You recently rerolled. Please try tommorow."});
        }
      } else {
        player.rerollTimeout = Date.now();
        player.proc = Math.floor(Math.random() * 100) + 1;
        accounts.set(player.name, player)
        return res.send({sucess: "Sucessfully rerolled!"});
      }
  });
}
