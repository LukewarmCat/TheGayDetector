const db = require("quick.db");
const passwordHash = require('password-hash');
const accounts = new db.table('accounts');
const guilds = new db.table('guilds');

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
    let temp = guilds.get(guild);

    var index = player.invitations.indexOf(guild);
    if (index !== -1) player.invitations.splice(index, 1);

    temp.accounts.push(username);

    player.guild = temp;

    accounts.set(username, player);
    guilds.set(guild, temp)
    res.send({sucess: `Invite accepted.`})
  })
}
