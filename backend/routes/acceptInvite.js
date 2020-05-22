const Enmap = require("enmap");
const passwordHash = require('password-hash');
const accounts = new Enmap({name: "accounts"});
const guilds = new Enmap({name: "guilds"})

module.exports = function(app) {
  app.get('/acceptInvite/:username/:password/:guild', (req, res) => {
    const password = req.params.password
    const username = req.params.username
    const guild = req.params.guild

    if(!accounts.get(username))
      return res.send({error: "User doesn't exist."})

    if(!username || !password)
      return res.send({error: "Username or password empty."});

    if (!passwordHash.verify(password, accounts.get(username).password))
      return res.send({error: "Incorrect username or password."});

    if(!guilds.get(guild))
      return res.send({error: "This guild doesn't exist."});

    if(accounts.get(username).guilds)
      return res.send({error: "You already have a guild."})

    let player = accounts.get(username);

    var index = player.invitations.indexOf(guild);
    if (index !== -1) player.invitations.splice(index, 1);

    player.guild = guilds.get(guild);

    accounts.set(username, player);

    res.send({sucess: `Invite accepted.`})
  })
}
