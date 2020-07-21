const db = require("quick.db");
const passwordHash = require('password-hash');
const accounts = new db.table('accounts');
const guilds = new db.table('guilds');

module.exports = function(app) {
  app.post('/declineInvite', (req, res) => {
    const password = req.body.password
    const username = req.body.username
    const guild = req.body.guild

    if(!accounts.get(username))
      return res.send({error: "User doesn't exist"})

    if(!username || !password)
      return res.send({error: "Username or password empty."});

    if (!passwordHash.verify(password, accounts.get(username).password))
      return res.send({error: "Incorrect username or password."});

    let player = accounts.get(username);

    if(player.guild)
      return res.send({error: "You're already in a guild."});

    if(!guilds.get(guild))
      return res.send({erorr: "This guild doesn't exist."})

    if(!player.invitations.includes(guild))
      return res.send({error: "You aren't invited to this guild."})

    var index = player.invitations.indexOf(guild);
    if (index !== -1) player.invitations.splice(index, 1);

    accounts.set(username, player)
    res.send({sucess: "Invite declined."})
  })
}
