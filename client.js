/**
 * author       : dot.f <fangyanliang@yiban.cn>
 * createTime   : 2016/8/10 16:03
 * description  :
 */

// var http = require('http')
//     ,httpProxy = require('http-proxy')  //http-proxy
//     ,proxy = httpProxy.createProxyServer({})
//     ,fs = require('fs')
//     ,path = require('path');
//
// var server = http.createServer(function(req, res) {
//     console.log(req.url)
//     proxy.web(req, res, { target: 'http://service.js.10086.cn' });
//
// });
//
// console.log("listening on port 80")
// server.listen(80);
//
//     host:
//         127.0.0.1 service.js.10086.cn
//
//
var http = require('http'),
    httpProxy = require('http-proxy');
//// Create your proxy server and set the target in the options.//
httpProxy.createProxyServer({target:'http://221.178.251.154'}).listen(80);//// Create your target server//

// http.createServer(function (req, res) {
//     res.writeHead(200, { 'Content-Type': 'text/plain' });
//     res.write('request successfully proxied!' + '\n' + JSON.stringify(req.headers, true, 2));
//     res.end();
// }).listen(9000);