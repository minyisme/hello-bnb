// //Add express for simplified http server
// var express = require('express');
// //Initiate http server
// var app = express();


// //Include static HTML in the 'html' directory
// app.use(express.static('public'));

// //Start the http server on port 4005
// var server = app.listen(4005);
// server.listen(4005, function() {
//     console.log('Server listening at http://localhost:4005/');
// });

var http = require('http');
var fs = require('fs');

// var host = '127.0.0.1';
var host = '10.10.30.167';
// var port = 1337;
var port = 4005;

var express = require('express');
var app = express();

//Include static HTML in the 'html' directory
app.use(express.static('public'));


var server = http.createServer(function(request, response){

	console.log('read' + " http://www.youtube.com");

	//read and get //. = root
	fs.readFile('.' + request.url , function(error, data){ 

		if(error){
			response.writeHead(404, {'Content-type':'text/plain'});
			response.end('404 file not found');	
		}else{
			response.writeHead(200, {'Content-type':'text/html'});
			response.end(data);
		}

	});

});

//run server
server.listen(port, host, function(){

	console.log('server listening at ' + host + ':' + port );

});

