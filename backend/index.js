const express = require("express");
const app = express();
require('./routes')(app);

app.get("/", (request, response) => {
  response.send("<b> The Xerty Meter </b>")
});

const listener = app.listen(3000, () => {
  console.log("Xerty's Backend is up. Listening on: 3000.");
});
