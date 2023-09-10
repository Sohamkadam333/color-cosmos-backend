const express = require('express');
const palateController = require('../controllers/palateController');

const router = express.Router();

// GET ALL Palates
router.get('/get-all-palates', palateController.getAllPalates);

// GET SINGLE Palate
router.get('/get-palate/:id', palateController.getSinglePalate);

// POST SINGLE Palate
router.post('/post-palate', palateController.postPalate);

module.exports = router;
