'use strict';
const app = require('express')();
const https = require('https');
//const helmet = require('helmet');
const fs = require('fs');

const HOST = '0.0.0.0';
const PORT = 5001;
const secret = fs.readFileSync('/run/secrets/secret2', 'utf8').trim();
const sharedSecret = fs.readFileSync('/run/secrets/sharedsecret', 'utf8').trim();

app.get('/', (req, res) => {
    res.send('[HTTPS]: My Name is Alice: ' + secret + ' AND ' + sharedSecret + '\n');
});

https.createServer({
    key: fs.readFileSync('./alice.key'),
    cert: fs.readFileSync('./alice.crt')
}, app)
.listen(PORT, HOST);