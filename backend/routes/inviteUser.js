const db = require("quick.db");
const passwordHash = require('password-hash');
const accounts = new db.table('accounts');
const guilds = new db.table('guilds');

module.exports = function(app) {
  app.post('/inviteUser', (req, res) => {
    const password = req.body.password
    const username = req.body.username
    const otherUser = req.body.otheruser

    if(!accounts.get(username))
      return res.send({error: "Your name isn't correct."})

    if(!username || !password)
      return res.send({error: "Username or password empty."});

    if (!passwordHash.verify(password, accounts.get(username).password))
      return res.send({error: "Incorrect username or password."});

    const player = accounts.get(username);
    const invitee = accounts.get(otherUser)

    if(!player.guild)
      return res.send({error: "You aren't in a guild."});

    if(player.guild.owner !== username)
      return res.send({error: "You aren't a owner of your guild."});

    if(!invitee)
      return res.send({error: "OtherUser doesn't exist."})

    if(invitee.invitations.includes(player.guild.name))
      return res.send({error: "You can't invite to a user twice."})

    if(invitee.guild)
      return res.send({error: "Invitee already has a Guild."})


    invitee.invitations.push(player.guild.name)
    accounts.set(otherUser, invitee)
    res.send({sucess: "Player invited."})
  })
}
