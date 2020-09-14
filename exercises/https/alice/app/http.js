'use strict';
const express = require('express');
const fs = require('fs');

const HOST = '0.0.0.0';
const PORT = 5000;
const secret = fs.readFileSync('/run/secrets/secret1', 'utf8').trim();
const sharedSecret = fs.readFileSync('/run/secrets/sharedsecret', 'utf8').trim();


const app = express();
app.get('/', (req, res) => {
    res.send('[HTTP]: My Name is Alice: ' + secret + ' AND ' + sharedSecret + '\n');
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
