const Enmap = require("enmap");
const passwordHash = require('password-hash');
const accounts = new Enmap({name: "accounts"});
const guilds = new Enmap({name: "guilds"})

module.exports = function(app) {
  app.get('/createGuild/:username/:password/:guildname', (req, res) => {
    const password = req.params.password
    const username = req.params.username
    const guildName = req.params.guildname

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
