const Enmap = require("enmap");
const passwordHash = require('password-hash');
const accounts = new Enmap({name: "accounts"});
const guilds = new Enmap({name: "guilds"})

module.exports = function(app) {
  app.get('/deleteGuild/:username/:password/:guild', (req, res) => {
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

    if(player.guild.owner !== username)
      return res.send({error: "You aren't a owner of your guild."});

    accounts.keyArray().forEach((x)=>{
      let pz = accounts.get(x)
      if(pz.guild) {
        if(pz.guild.name == guild) {
          pz.guild = undefined;
          accounts.set(x, pz)
        }
      }
    })

    guilds.set(guild, undefined);

    res.send({sucess: "Guild deleted."})
  })
}
