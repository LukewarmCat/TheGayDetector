const Enmap = require("enmap");
const passwordHash = require('password-hash');
const accounts = new Enmap({name: "accounts"});
const guilds = new Enmap({name: "guilds"})

module.exports = function(app) {
  app.get('/deleteUser/:username/:password', (req, res) => {
    const password = req.params.password
    const username = req.params.username

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
