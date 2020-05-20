const express = require("express");
const app = express();
const Enmap = require("enmap");
const gay = new Enmap({name: "gay"});
const accounts = new Enmap({name: "accounts"});


app.get("/", (request, response) => {
  response.send("<b> The Gay Detector </b>")
});

app.get('/addUser/:username/:password', (req, res) => {
  var username = req.params.username;
  var password = req.params.password;
  
  if(username.length < 0 || password.length < 0)
    return res.send({error: "Username or password empty."});
  
  if(accounts.get(username))
    return res.send({error: "User already exists."});
  
  if(username.length > 10)
    return res.send({error: "Username too long."});
  
  accounts.set(username, password)
  gay.set(username, Math.floor(Math.random() * 100) + 1)
  res.send({sucess: "Account added."})
});

app.get('/getUser/:username/:password', (req, res) => {
  if (accounts.get(req.params.username) !== req.params.password)
    return res.send({error: "Incorrect username or password."});
  
    res.send({sucess: gay.get(req.params.username)})
});

const listener = app.listen(process.env.PORT, () => {
  console.log("Your app is listening on port " + listener.address().port);
});
