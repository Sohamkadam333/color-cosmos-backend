const Gradient = require('../models/gradientModel');

// GET ALL GRADIENTS
const getAllGradients = async (req, res) => {
	try {
		const gradients = await Gradient.find();

		res.status(200).json({ msg: 'Success', gradients });
	} catch (error) {
		res.status(400).json({ msg: 'gradientss do not exits', error: error.message });
	}
};

// GET SINGLE GRADIENT
const getSingleGradient = async (req, res) => {
	const { id } = req.params;

	try {
		const gradient = await Gradient.findById(id);

		res.status(200).json({ msg: 'Success', gradient });
	} catch (error) {
		res.status(400).json({ msg: 'gradient do not exits', error: error.message });
	}
	console.log(id);
	// res.send(`${id} Single blog`);
};

module.exports = {
	getAllGradients,
	getSingleGradient,
};
