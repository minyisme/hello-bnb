var request = require("request");

request("http://www.youtube.com", function(error, response, body) {
  console.log(body);
});
