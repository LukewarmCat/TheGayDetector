const db = require("quick.db");
const passwordHash = require('password-hash');
const accounts = new db.table('accounts');
const guilds = new db.table('guilds');

module.exports = function(app) {
  app.post('/addUser', (req, res) => {
    const username = req.body.username;
    const password = passwordHash.generate(req.body.password);

    if(!username || !password)
      return res.send({error: "Username or password empty."});

    if(accounts.get(username))
      return res.send({error: "User already exists."});

    if(username.length > 10)
      return res.send({error: "Username too long."});

    accounts.set(username, {name: username, password: password, proc: Math.floor(Math.random() * 100) + 1, invitations: []})
    res.send({sucess: "Account added."})
  });
}
