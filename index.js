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
app.use(cors());

// CORS ORIGIN
app.use((req, res, next) => {
	const allowedOrigins = [
		'http://example.com',
		'http://anotherexample.com',
		'http://192.168.1.100:5500',
		'https://chromewebstore.google.com/detail/color-cosmos/cjgholfdgchgianpgloflnmhpljbjaab',
	];
	const origin = req.headers.origin;

	if (allowedOrigins.includes(origin)) {
		res.setHeader('Access-Control-Allow-Origin', origin);
		res.header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE');
		res.header('Access-Control-Allow-Headers', 'Content-Type, Authorization');
		res.header('Access-Control-Allow-Credentials', true);

		if (req.method === 'OPTIONS') {
			res.sendStatus(200);
		} else {
			next();
		}
	} else {
		res.status(403).json({ error: 'Origin not allowed' });
	}
});

app.use(myLogger);
// app.use(logger);

// Home Page
app.get('/api/v1', async (req, res) => {
	let jsonPath = path.join(__dirname, 'models', 'requestCount.log');
	let reqCount;
	fs.readFile(jsonPath, 'utf8', (err, data) => {
		if (err) {
			console.log('error');
		} else {
			console.log('Request Count = ', data);
			reqCount = data;
		}
		res.status(200).json({
			response: 'Success',
			reqCount: reqCount,
		});
	});
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
