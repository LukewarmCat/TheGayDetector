const Enmap = require("enmap");
const passwordHash = require('password-hash');
const accounts = new Enmap({name: "accounts"});
const guilds = new Enmap({name: "guilds"})

module.exports = function(app) {
  app.get('/leaveGuild/:username/:password/:guild', (req, res) => {
    const password = req.params.password
    const username = req.params.username
    const guild = req.params.guild

    if(!accounts.get(username))
      return res.send({error: "User doesn't exist."})

    if(!username || !password)
      return res.send({error: "Username or password empty."});

    if (!passwordHash.verify(password, accounts.get(username).password))
      return res.send({error: "Incorrect username or password."});

    const player = accounts.get(username);

    if(!player.guild)
      return res.send({error: "You aren't in a guild."});

    if(player.guild.owner === username)
      return res.send({error: "You own this guild. Please delete it."});

    const playerGuild = guilds.get(player.guild.name);

    player.guild = undefined;

    var index = playerGuild.members.indexOf(username);
    if (index !== -1) player.members.splice(index, 1);

    guilds.set(playerGuild.name, playerGuild);
    accounts.set(username, player);
    res.send({sucess: "Guild left."})
  })
}
