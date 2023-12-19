const express = require('express');
const fs = require('fs');
const path = require('path');
require('dotenv').config();
const cors = require('cors');
// const logger = require('./middleware/logger');
// const pageNotFound = require('./middleware/pageNotFound');
const mongoose = require('mongoose');
// const User = require('./models/userModel');
// const Blog = require('./models/blogModel');
// const bcrypt = require('bcrypt');
const palateRouter = require('./routes/palateRoutes');
const gradientRouter = require('./routes/gradientRoutes');
const myLogger = require('./middleware/reqCount');
// const userRouter = require('./routes/userRoutes');
// const verifyToken = require('./middleware/checkAuth');
// const verifyToken = require('./middleware/checkAuth');

const app = express();

// MIDDLEWARES
app.use(express.json());

// ALLOW ALL
app.use(cors());

// CORS ORIGIN
// List of allowed origins (add your extension ID and three additional origins)
// const allowedOrigins = [
// 	'chrome-extension://cjgholfdgchgianpgloflnmhpljbjaab/',
// 	'https://allowed-origin-1.com',
// 	'https://color-cosmos.onrender.com/',
// ];

// Configure CORS to allow requests only from specified origins
// const corsOptions = {
// 	origin: (origin, callback) => {
// 		if (allowedOrigins.includes(origin) || !origin) {
// 			// Allow requests from specified origins or non-browser clients (e.g., mobile apps)
// 			callback(null, true);
// 		} else {
// 			// Reject requests from other origins
// 			callback(new Error('Origin Not Allowed'));
// 		}
// 	},
// 	methods: 'GET,HEAD,PUT,PATCH,POST,DELETE',
// 	credentials: true,
// 	optionsSuccessStatus: 204,
// };

// app.use(cors(corsOptions));

app.use(myLogger);
// app.use(logger);

// Home Page
app.get('/api/v1', async (req, res) => {
	// local path
	// let jsonPath = path.join(__dirname, 'middleware', 'requestCount.log');

	// server path
	let jsonPath = path.join(__dirname, 'middleware', 'requestCount.log');
	console.log('Home dir path =', jsonPath);
	let reqCount;
	fs.readFile(jsonPath, 'utf8', (err, data) => {
		if (err) {
			console.log('error reading file', jsonPath);
		} else {
			console.log('request count below');
			console.log(data);
			reqCount = data;
		}
		res.status(200).json({
			response: 'Success',
			reqCount: reqCount,
			mainDir: __dirname,
			middlewarePath: jsonPath,
		});
	});

	// *********** local testing
	// res.status(200).json({
	// 	response: 'Success',
	// 	//reqCount: reqCount,
	// 	mainDir: __dirname,
	// });
});

// User Router
// app.use('/api/v1/user', userRouter);

// Verify token only for blogs
// app.use(verifyToken);

// Blogs Router
app.use('/api/v1/', palateRouter);
app.use('/api/v1/', gradientRouter);

// app.use(pageNotFound);

// CONNECT TO DB
const connectToDB = async (url) => {
	try {
		await mongoose.connect(url, {
			useNewUrlParser: true,
			useUnifiedTopology: true,
		});
		console.log('Connected to DB SUCCESS');

		app.listen(process.env.PORT, () => {
			console.log('server started');
		});
	} catch (error) {
		console.error({ msg: `Error connecting DB ${error}` });
	}
};

connectToDB(process.env.MONGO_URI);
