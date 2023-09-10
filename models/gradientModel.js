const mongoose = require('mongoose');

const gradientSchema = mongoose.Schema(
	{
		id: {
			type: String,
			require: true,
		},
		name: {
			type: String,
			require: true,
		},
		colors: {
			type: Array,
			require: true,
		},
		css: {
			type: String,
			require: true,
		},
	},
	{
		timestamps: true,
	}
);

const Gradient = mongoose.model('Gradient', gradientSchema);
module.exports = Gradient;
