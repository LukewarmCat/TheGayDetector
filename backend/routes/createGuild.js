const db = require("quick.db");
const passwordHash = require('password-hash');
const accounts = new db.table('accounts');
const guilds = new db.table('guilds');

module.exports = function(app) {
  app.post('/createGuild', (req, res) => {
    const password = req.body.password
    const username = req.body.username
    const guildName = req.body.guildName

    if(guildName.length > 6 || guildName.length < 3)
      return res.send({error: "Guild name wrong. Max: 6, Min: 3 in length."})

    if(!accounts.get(username))
      return res.send({error: "User doesn't exist."})

    if(!username || !password)
      return res.send({error: "Username or password empty."});

    if (!passwordHash.verify(password, accounts.get(username).password))
      return res.send({error: "Incorrect username or password."});

    if(guilds.get(guildName))
      return res.send({error: "This guild already exists."});

    const guildTag = guildName.substring(0,3);
    let player = accounts.get(username);

    var newguild = {name: guildName, tag: guildTag, accounts: [player.name], owner: player.name}

    player.guild = newguild;

    guilds.set(guildName, newguild);

    accounts.set(username, player)
    res.send({sucess: `Guild ${guildName} made.`})
  })
}
