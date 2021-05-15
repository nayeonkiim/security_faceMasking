const express = require('express');
const router = express.Router();
const decrypt = require('./decrypt');


router.get('/', decrypt.dec);
router.get('/filter', (req, res, next) => {
    res.render('index');
})

module.exports = router;