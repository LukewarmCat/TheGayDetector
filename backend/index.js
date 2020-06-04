const express = require("express");
const app = express();

app.use(express.json());
app.use(express.urlencoded())

require('./routes')(app);

app.get("/", (request, response) => {
  response.send(`<link href="https://fonts.googleapis.com/css2?family=Pacifico&display=swap" rel="stylesheet">

<p style="font-size: 30;font-family: 'Pacifico', cursive;text-align: center;">The Xerty Meter</p>
<p style="font-size: 20;text-align: center;white-space: pre-wrap;">
Source: https://github.com/LukewarmCat/xerty
Discord: https://discord.gg/Hg2uDPB



lukewarmcat &copy; 2020
</p>`)
});

const listener = app.listen(3000, () => {
  console.log("Xerty's Backend is up. Listening on: 3000.");
});
