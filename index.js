const express = require('express');
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
// const userRouter = require('./routes/userRoutes');
// const verifyToken = require('./middleware/checkAuth');
// const verifyToken = require('./middleware/checkAuth');

const app = express();

// MIDDLEWARES
app.use(express.json());
app.use(cors());
// app.use(logger);

// Home Page
app.get('/api/v1', async (req, res) => {
	res.send('Home Page Success');
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
