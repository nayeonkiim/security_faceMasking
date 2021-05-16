const express = require('express');
const router = express.Router();
const decrypt = require('./decrypt');

router.get('/', (req, res, next) => {
    res.render('input');
});

router.post('/dec', decrypt.dec);

router.get('/filter', (req, res, next) => {
    res.render('index');
})

module.exports = router;