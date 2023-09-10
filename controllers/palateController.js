const Palate = require('../models/palateModel');

// GET ALL BLOGS
const getAllPalates = async (req, res) => {
	try {
		const palate = await Palate.find();

		res.status(200).json({ msg: 'Success', palate });
	} catch (error) {
		res.status(400).json({ msg: 'palates do not exits', error: error.message });
	}
};

// GET SINGLE BLOG
const getSinglePalate = async (req, res) => {
	const { id } = req.params;

	try {
		const palate = await Palate.findById(id);

		res.status(200).json({ msg: 'Success', palate });
	} catch (error) {
		res.status(400).json({ msg: 'palate do not exits', error: error.message });
	}
	console.log(req.body);
};

// POST BLOG
const postPalate = async (req, res) => {
	console.log('try post palate');
	const { name, colors, id } = req.body;
	try {
		if (!name || !colors || !id) {
			res.status(400).json({ msg: 'All fields must be filled' });
			return;
		}
		const palate = await Palate.create({
			name,
			colors,
			id,
		});
		res.status(200).json({ msg: 'Posting Success', palate });
	} catch (error) {
		// console.log(err.message);
		res.status(400).json({ msg: 'Blog Post Error', error: error.message });
	}
};

module.exports = {
	getAllPalates,
	getSinglePalate,
	postPalate,
};
