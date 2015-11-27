var http = require("http");
var httpProxy = require("http-proxy");
var express = require("express");
var fs = require("fs");

var proxy = httpProxy.createProxyServer({
    ssl: {
      key: fs.readFileSync('certs/key.pem', 'utf8'),
      cert: fs.readFileSync('certs/cert.pem', 'utf8')
    }
  });

var app = express();

app.use(express.static("public"));

function proxyRequest(req,res) {
  console.log(req);
  //donothingurl = req["url"] + req[""]
  console.log(req["url"])
  if (req["url"].indexOf("reddit.com") != -1) {
    console.log("reddit!")
    proxy.web(req, res, {
      target: "http://localhost:8000",
      ws: true});
  }
  else {
    console.log("not reddit!")
    proxy.web(req, res, {
      target: req["url"],
      ws: true});
  }
}

var proxyserver = http.createServer(proxyRequest);
var messageserver = app.listen(8000);


proxyserver.listen(5000);
