const express = require('express');
const gradientController = require('../controllers/gradientController');

const router = express.Router();

// GET ALL BLOGS
router.get('/get-all-gradients', gradientController.getAllGradients);

// GET SINGLE BLOGS
router.get('/get-gradient/:id', gradientController.getSingleGradient);

module.exports = router;
