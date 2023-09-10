const mongoose = require('mongoose');

const palateSchema = mongoose.Schema(
	{
		name: {
			type: String,
			require: true,
		},
		colors: {
			type: Array,
			require: true,
		},
		id: {
			type: String,
			require: true,
		},
	},
	{
		timestamps: true,
	}
);

const Palate = mongoose.model('Palate', palateSchema);
module.exports = Palate;
