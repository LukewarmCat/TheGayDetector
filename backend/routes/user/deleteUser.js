const db = require("quick.db");
const passwordHash = require('password-hash');
const accounts = new db.table('accounts');
const guilds = new db.table('guilds');

module.exports = function(app) {
  app.post('/deleteUser', (req, res) => {
    const password = req.body.password
    const username = req.body.username

    if(!accounts.get(username))
      return res.send({error: "User doesn't exist."})

    if(!username || !password)
      return res.send({error: "Username or password empty."});

    if (!passwordHash.verify(password, accounts.get(username).password))
      return res.send({error: "Incorrect username or password."});

    let player = accounts.get(username);

    if(player.guild)
      return res.send({error: "You're in a guild. Please leave it."});

    accounts.delete(username)
    res.send({sucess: "Account has been removed."})
  })
}
