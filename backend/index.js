const express = require("express");
const app = express();
const passwordHash = require('password-hash');
const Enmap = require("enmap");
const accounts = new Enmap({name: "accounts"});
const guilds = new Enmap({name: "guilds"})

app.get("/", (request, response) => {
  response.send("<b> The Xerty Meter </b>")
});

app.get('/declineInvite/:username/:password/:guild', (req, res) => {
  const password = req.params.password
  const username = req.params.username
  const guild = req.params.guild

  if(!accounts.get(username))
    return res.send({error: "Your name isn't correct."})

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

app.get('/acceptInvite/:username/:password/:guild', (req, res) => {
  console.log("reach")
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
app.get('/inviteUser/:username/:password/:otheruser', (req, res) => {
  const password = req.params.password
  const username = req.params.username
  const otherUser = req.params.otheruser

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

app.get('/addUser/:username/:password', (req, res) => {
  const username = req.params.username;
  const password = passwordHash.generate(req.params.password);

  if(!username || !password)
    return res.send({error: "Username or password empty."});

  if(accounts.get(username))
    return res.send({error: "User already exists."});

  if(username.length > 10)
    return res.send({error: "Username too long."});

  accounts.set(username, {name: username, password: password, proc: Math.floor(Math.random() * 100) + 1, invitations: []})
  res.send({sucess: "Account added."})
});

app.get('/getUser/:username/:password', (req, res) => {
  if(!accounts.get(req.params.username))
    return res.send({error: "This user doesn't exist."});

  if (!passwordHash.verify(req.params.password, accounts.get(req.params.username).password))
    return res.send({error: "Incorrect username or password."});

    res.send({sucess: accounts.get(req.params.username)})
});

const listener = app.listen(3000, () => {
  console.log("Your app is listening on port " + listener.address().port);
});
