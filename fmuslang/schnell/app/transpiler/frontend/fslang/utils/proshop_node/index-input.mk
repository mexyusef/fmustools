--% index/fmus
proshopmern,d(/mk)
	%utama=__FILE__
	%__TEMPLATE_SERVER_PORT=__NILAI_SERVER_PORT__
	.gitignore,f(e=utama=/np/node-mongodb/.gitignore)
	package.json,f(e=utama=/np/node-mongodb/package.json)
	Procfile,f(e=utama=/np/node-mongodb/Procfile)
	README.md,f(e=utama=/np/node-mongodb/README.md)
	$*ln -s /mnt/c/node_modules/proshop_node/node_modules .
	docker-compose.yml,f(e=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_node/dcu.mk=/np/docker-compose.yml)
	.env,f(e=utama=/np/node-mongodb/.env)
	backend,d(/mk)
		apps,d(/mk)
__TEMPLATE_SERVER_APP_CONTENT
			#user,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_node/user.mk=index/fmus*)
		apps,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_node/modify.mk=index/fmus*)
		main,d(/mk)
			uploadRoutes.js,f(e=utama=/np/node-mongodb/backend/uploadRoutes.js)
		seeder.js,f(e=utama=/np/node-mongodb/backend/seeder.js)
		server.js,f(e=utama=/np/node-mongodb/backend/server.js)
		config,d(/mk)
			db.js,f(e=utama=/np/node-mongodb/backend/config/db.js)
		data,d(/mk)
			products.js,f(e=utama=/np/node-mongodb/backend/data/products.js)
			users.js,f(e=utama=/np/node-mongodb/backend/data/users.js)
		middleware,d(/mk)
			authMiddleware.js,f(e=utama=/np/node-mongodb/backend/middleware/authMiddleware.js)
			errorMiddleware.js,f(e=utama=/np/node-mongodb/backend/middleware/errorMiddleware.js)
		utils,d(/mk)
			generateToken.js,f(e=utama=/np/node-mongodb/backend/utils/generateToken.js)
	uploads,d(/mk)
		file.txt,f(e=utama=/np/node-mongodb/uploads/file.txt)
--#

--% /np/node-mongodb/.env
PAYPAL_CLIENT_ID=
MONGO_URI=mongodb://usef:rahasia@localhost/test?authSource=admin
--#

--% /np/node-mongodb/.gitignore
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
node_modules
node_modules/
/.pnp
.pnp.js

# testing
/coverage

# production
/frontend/build

# misc
.DS_Store
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

npm-debug.log*
yarn-debug.log*
yarn-error.log*
.vscode/settings.json

--#

--% /np/node-mongodb/package.json
{
	"name": "proshop",
	"version": "1.0.0",
	"description": "MERN shopping cart app",
	"main": "server.js",
	"type": "module",
	"scripts": {
		"start": "node backend/server",
		"server": "nodemon backend/server",
		"client": "npm start --prefix frontend",
		"dev": "concurrently \"npm run server\" \"npm run client\"",
		"data:import": "node backend/seeder",
		"data:destroy": "node backend/seeder -d",
		"heroku-postbuild": "NPM_CONFIG_PRODUCTION=false npm install --prefix frontend && npm run build --prefix frontend"
	},
	"author": "Brad Traversy",
	"license": "MIT",
	"dependencies": {
		"bcryptjs": "^2.4.3",
		"colors": "^1.4.0",
		"dotenv": "^8.2.0",
		"express": "^4.17.1",
		"express-async-handler": "^1.1.4",
		"jsonwebtoken": "^8.5.1",
		"mongoose": "^5.10.6",
		"morgan": "^1.10.0",
		"multer": "^1.4.2"
	},
	"devDependencies": {
		"concurrently": "^5.3.0",
		"nodemon": "^2.0.4"
	}
}

--#

--% /np/node-mongodb/Procfile
web: node backend/server.js
--#

--% /np/node-mongodb/README.md

## Features

- Full featured shopping cart
- Product reviews and ratings
- Top products carousel
- Product pagination
- Product search feature
- User profile with orders
- Admin product management
- Admin user management
- Admin Order details page
- Mark orders as delivered option
- Checkout process (shipping, payment method, etc)
- PayPal / credit card integration
- Database seeder (products & users)

## Usage

### ES Modules in Node

We use ECMAScript Modules in the backend in this project. Be sure to have at least Node v14.6+ or you will need to add the "--experimental-modules" flag.

Also, when importing a file (not a package), be sure to add .js at the end or you will get a "module not found" error

You can also install and setup Babel if you would like

### Env Variables

Create a .env file in then root and add the following

```
NODE_ENV = development
PORT = 5000
MONGO_URI = your mongodb uri
JWT_SECRET = 'abc123'
PAYPAL_CLIENT_ID = your paypal client id
```

### Install Dependencies (frontend & backend)

```
npm install
cd frontend
npm install
```

### Run

```
# Run frontend (:3000) & backend (:5000)
npm run dev

# Run backend only
npm run server
```

## Build & Deploy

```
# Create frontend prod build
cd frontend
npm run build
```

There is a Heroku postbuild script, so if you push to Heroku, no need to build manually for deployment to Heroku

### Seed Database

You can use the following commands to seed the database with some sample users and products as well as destroy all data

```
# Import data
npm run data:import

# Destroy data
npm run data:destroy
```

```
Sample User Logins

admin@example.com (Admin)
123456

john@example.com (Customer)
123456

jane@example.com (Customer)
123456
```
--#

--% /np/node-mongodb/backend/seeder.js
import mongoose from 'mongoose'
import dotenv from 'dotenv'
import colors from 'colors'

import users from './data/users.js'
import products from './data/products.js'

__TEMPLATE_SEEDER_IMPORTS

import connectDB from './config/db.js'

dotenv.config()

connectDB()

const importData = async () => {
	try {
__TEMPLATE_DELETE_NON_PRODUCT_USER
		//await Order.deleteMany()
		await Product.deleteMany()
		await User.deleteMany()

		const createdUsers = await User.insertMany(users)

		const adminUser = createdUsers[0]._id

		const sampleProducts = products.map((product) => {
			return { ...product, user: adminUser }
		})

		await Product.insertMany(sampleProducts)

		console.log('Data Imported!'.green.inverse)
		process.exit()
	} catch (error) {
		console.error(`${error}`.red.inverse)
		process.exit(1)
	}
}

const destroyData = async () => {
	try {
__TEMPLATE_DELETE_NON_PRODUCT_USER
		//await Order.deleteMany()
		await Product.deleteMany()
		await User.deleteMany()

		console.log('Data Destroyed!'.red.inverse)
		process.exit()
	} catch (error) {
		console.error(`${error}`.red.inverse)
		process.exit(1)
	}
}

if (process.argv[2] === '-d') {
	destroyData()
} else {
	importData()
}

--#

--% /np/node-mongodb/backend/server.js
import path from 'path'
import express from 'express'
import dotenv from 'dotenv'
import colors from 'colors'
import morgan from 'morgan'
import { notFound, errorHandler } from './middleware/errorMiddleware.js'
import connectDB from './config/db.js'

import uploadRoutes from './main/uploadRoutes.js'

__TEMPLATE_APP_SERVER_IMPORTS

dotenv.config()

connectDB()

const app = express()

if (process.env.NODE_ENV === 'development') {
	app.use(morgan('dev'))
}

app.use(express.json())

app.use('/api/upload', uploadRoutes)

__TEMPLATE_APP_SERVER_USES

app.get('/api/config/paypal', (req, res) =>
	res.send(process.env.PAYPAL_CLIENT_ID)
)

const __dirname = path.resolve()
app.use('/uploads', express.static(path.join(__dirname, '/uploads')))

if (process.env.NODE_ENV === 'production') {
	app.use(express.static(path.join(__dirname, '/frontend/build')))

	app.get('*', (req, res) =>
		res.sendFile(path.resolve(__dirname, 'frontend', 'build', 'index.html'))
	)
} else {
	app.get('/', (req, res) => {
		res.send('API is running....')
	})
}

app.use(notFound)
app.use(errorHandler)

const PORT = process.env.PORT || __TEMPLATE_SERVER_PORT

app.listen(
	PORT,
	console.log(
		`Server running in ${process.env.NODE_ENV} mode on port ${PORT}`.yellow.bold
	)
)

--#

--% /np/node-mongodb/backend/config/db.js
import mongoose from 'mongoose'

const connectDB = async () => {
	try {
		const conn = await mongoose.connect(process.env.MONGO_URI, {
			useUnifiedTopology: true,
			useNewUrlParser: true,
			useCreateIndex: true,
		})

		console.log(`MongoDB Connected: ${conn.connection.host}`.cyan.underline)
	} catch (error) {
		console.error(`Error: ${error.message}`.red.underline.bold)
		process.exit(1)
	}
}

export default connectDB

--#

--% /np/node-mongodb/backend/orderController.js
import asyncHandler from 'express-async-handler'
import Order from '../models/orderModel.js'

// @desc    Create new order
// @route   POST /api/orders
// @access  Private
const addOrderItems = asyncHandler(async (req, res) => {
	const {
		orderItems,
		shippingAddress,
		paymentMethod,
		itemsPrice,
		taxPrice,
		shippingPrice,
		totalPrice,
	} = req.body

	if (orderItems && orderItems.length === 0) {
		res.status(400)
		throw new Error('No order items')
		return
	} else {
		const order = new Order({
			orderItems,
			user: req.user._id,
			shippingAddress,
			paymentMethod,
			itemsPrice,
			taxPrice,
			shippingPrice,
			totalPrice,
		})

		const createdOrder = await order.save()

		res.status(201).json(createdOrder)
	}
})

// @desc    Get order by ID
// @route   GET /api/orders/:id
// @access  Private
const getOrderById = asyncHandler(async (req, res) => {
	const order = await Order.findById(req.params.id).populate(
		'user',
		'name email'
	)

	if (order) {
		res.json(order)
	} else {
		res.status(404)
		throw new Error('Order not found')
	}
})

// @desc    Update order to paid
// @route   GET /api/orders/:id/pay
// @access  Private
const updateOrderToPaid = asyncHandler(async (req, res) => {
	const order = await Order.findById(req.params.id)

	if (order) {
		order.isPaid = true
		order.paidAt = Date.now()
		order.paymentResult = {
			id: req.body.id,
			status: req.body.status,
			update_time: req.body.update_time,
			email_address: req.body.payer.email_address,
		}

		const updatedOrder = await order.save()

		res.json(updatedOrder)
	} else {
		res.status(404)
		throw new Error('Order not found')
	}
})

// @desc    Update order to delivered
// @route   GET /api/orders/:id/deliver
// @access  Private/Admin
const updateOrderToDelivered = asyncHandler(async (req, res) => {
	const order = await Order.findById(req.params.id)

	if (order) {
		order.isDelivered = true
		order.deliveredAt = Date.now()

		const updatedOrder = await order.save()

		res.json(updatedOrder)
	} else {
		res.status(404)
		throw new Error('Order not found')
	}
})

// @desc    Get logged in user orders
// @route   GET /api/orders/myorders
// @access  Private
const getMyOrders = asyncHandler(async (req, res) => {
	const orders = await Order.find({ user: req.user._id })
	res.json(orders)
})

// @desc    Get all orders
// @route   GET /api/orders
// @access  Private/Admin
const getOrders = asyncHandler(async (req, res) => {
	const orders = await Order.find({}).populate('user', 'id name')
	res.json(orders)
})

export {
	addOrderItems,
	getOrderById,
	updateOrderToPaid,
	updateOrderToDelivered,
	getMyOrders,
	getOrders,
}

--#

--% /np/node-mongodb/backend/productController.js
import asyncHandler from 'express-async-handler'
import Product from '../models/productModel.js'

// @desc    Fetch all products
// @route   GET /api/products
// @access  Public
const getProducts = asyncHandler(async (req, res) => {
	const pageSize = 10
	const page = Number(req.query.pageNumber) || 1

	const keyword = req.query.keyword
		? {
				name: {
					$regex: req.query.keyword,
					$options: 'i',
				},
			}
		: {}

	const count = await Product.countDocuments({ ...keyword })
	const products = await Product.find({ ...keyword })
		.limit(pageSize)
		.skip(pageSize * (page - 1))

	res.json({ products, page, pages: Math.ceil(count / pageSize) })
})

// @desc    Fetch single product
// @route   GET /api/products/:id
// @access  Public
const getProductById = asyncHandler(async (req, res) => {
	const product = await Product.findById(req.params.id)

	if (product) {
		res.json(product)
	} else {
		res.status(404)
		throw new Error('Product not found')
	}
})

// @desc    Delete a product
// @route   DELETE /api/products/:id
// @access  Private/Admin
const deleteProduct = asyncHandler(async (req, res) => {
	const product = await Product.findById(req.params.id)

	if (product) {
		await product.remove()
		res.json({ message: 'Product removed' })
	} else {
		res.status(404)
		throw new Error('Product not found')
	}
})

// @desc    Create a product
// @route   POST /api/products
// @access  Private/Admin
const createProduct = asyncHandler(async (req, res) => {
	const product = new Product({
		name: 'Sample name',
		price: 0,
		user: req.user._id,
		image: '/images/sample.jpg',
		brand: 'Sample brand',
		category: 'Sample category',
		countInStock: 0,
		numReviews: 0,
		description: 'Sample description',
	})

	const createdProduct = await product.save()
	res.status(201).json(createdProduct)
})

// @desc    Update a product
// @route   PUT /api/products/:id
// @access  Private/Admin
const updateProduct = asyncHandler(async (req, res) => {
	const {
		name,
		price,
		description,
		image,
		brand,
		category,
		countInStock,
	} = req.body

	const product = await Product.findById(req.params.id)

	if (product) {
		product.name = name
		product.price = price
		product.description = description
		product.image = image
		product.brand = brand
		product.category = category
		product.countInStock = countInStock

		const updatedProduct = await product.save()
		res.json(updatedProduct)
	} else {
		res.status(404)
		throw new Error('Product not found')
	}
})

// @desc    Create new review
// @route   POST /api/products/:id/reviews
// @access  Private
const createProductReview = asyncHandler(async (req, res) => {
	const { rating, comment } = req.body

	const product = await Product.findById(req.params.id)

	if (product) {
		const alreadyReviewed = product.reviews.find(
			(r) => r.user.toString() === req.user._id.toString()
		)

		if (alreadyReviewed) {
			res.status(400)
			throw new Error('Product already reviewed')
		}

		const review = {
			name: req.user.name,
			rating: Number(rating),
			comment,
			user: req.user._id,
		}

		product.reviews.push(review)

		product.numReviews = product.reviews.length

		product.rating =
			product.reviews.reduce((acc, item) => item.rating + acc, 0) /
			product.reviews.length

		await product.save()
		res.status(201).json({ message: 'Review added' })
	} else {
		res.status(404)
		throw new Error('Product not found')
	}
})

// @desc    Get top rated products
// @route   GET /api/products/top
// @access  Public
const getTopProducts = asyncHandler(async (req, res) => {
	const products = await Product.find({}).sort({ rating: -1 }).limit(3)

	res.json(products)
})

export {
	getProducts,
	getProductById,
	deleteProduct,
	createProduct,
	updateProduct,
	createProductReview,
	getTopProducts,
}

--#

--% /np/node-mongodb/backend/userController.js
import asyncHandler from 'express-async-handler'
import generateToken from '../utils/generateToken.js'
import User from '../models/userModel.js'

// @desc    Auth user & get token
// @route   POST /api/users/login
// @access  Public
const authUser = asyncHandler(async (req, res) => {
	const { email, password } = req.body

	const user = await User.findOne({ email })

	if (user && (await user.matchPassword(password))) {
		res.json({
			_id: user._id,
			name: user.name,
			email: user.email,
			isAdmin: user.isAdmin,
			token: generateToken(user._id),
		})
	} else {
		res.status(401)
		throw new Error('Invalid email or password')
	}
})

// @desc    Register a new user
// @route   POST /api/users
// @access  Public
const registerUser = asyncHandler(async (req, res) => {
	const { name, email, password } = req.body

	const userExists = await User.findOne({ email })

	if (userExists) {
		res.status(400)
		throw new Error('User already exists')
	}

	const user = await User.create({
		name,
		email,
		password,
	})

	if (user) {
		res.status(201).json({
			_id: user._id,
			name: user.name,
			email: user.email,
			isAdmin: user.isAdmin,
			token: generateToken(user._id),
		})
	} else {
		res.status(400)
		throw new Error('Invalid user data')
	}
})

// @desc    Get user profile
// @route   GET /api/users/profile
// @access  Private
const getUserProfile = asyncHandler(async (req, res) => {
	const user = await User.findById(req.user._id)

	if (user) {
		res.json({
			_id: user._id,
			name: user.name,
			email: user.email,
			isAdmin: user.isAdmin,
		})
	} else {
		res.status(404)
		throw new Error('User not found')
	}
})

// @desc    Update user profile
// @route   PUT /api/users/profile
// @access  Private
const updateUserProfile = asyncHandler(async (req, res) => {
	const user = await User.findById(req.user._id)

	if (user) {
		user.name = req.body.name || user.name
		user.email = req.body.email || user.email
		if (req.body.password) {
			user.password = req.body.password
		}

		const updatedUser = await user.save()

		res.json({
			_id: updatedUser._id,
			name: updatedUser.name,
			email: updatedUser.email,
			isAdmin: updatedUser.isAdmin,
			token: generateToken(updatedUser._id),
		})
	} else {
		res.status(404)
		throw new Error('User not found')
	}
})

// @desc    Get all users
// @route   GET /api/users
// @access  Private/Admin
const getUsers = asyncHandler(async (req, res) => {
	const users = await User.find({})
	res.json(users)
})

// @desc    Delete user
// @route   DELETE /api/users/:id
// @access  Private/Admin
const deleteUser = asyncHandler(async (req, res) => {
	const user = await User.findById(req.params.id)

	if (user) {
		await user.remove()
		res.json({ message: 'User removed' })
	} else {
		res.status(404)
		throw new Error('User not found')
	}
})

// @desc    Get user by ID
// @route   GET /api/users/:id
// @access  Private/Admin
const getUserById = asyncHandler(async (req, res) => {
	const user = await User.findById(req.params.id).select('-password')

	if (user) {
		res.json(user)
	} else {
		res.status(404)
		throw new Error('User not found')
	}
})

// @desc    Update user
// @route   PUT /api/users/:id
// @access  Private/Admin
const updateUser = asyncHandler(async (req, res) => {
	const user = await User.findById(req.params.id)

	if (user) {
		user.name = req.body.name || user.name
		user.email = req.body.email || user.email
		user.isAdmin = req.body.isAdmin

		const updatedUser = await user.save()

		res.json({
			_id: updatedUser._id,
			name: updatedUser.name,
			email: updatedUser.email,
			isAdmin: updatedUser.isAdmin,
		})
	} else {
		res.status(404)
		throw new Error('User not found')
	}
})

export {
	authUser,
	registerUser,
	getUserProfile,
	updateUserProfile,
	getUsers,
	deleteUser,
	getUserById,
	updateUser,
}

--#

--% /np/node-mongodb/backend/data/products.js
const products = [
	{
		name: 'Airpods Wireless Bluetooth Headphones',
		image: '/images/airpods.jpg',
		description:
			'Bluetooth technology lets you connect it with compatible devices wirelessly High-quality AAC audio offers immersive listening experience Built-in microphone allows you to take calls while working',
		brand: 'Apple',
		category: 'Electronics',
		price: 89.99,
		countInStock: 3,
		rating: 0,
		numReviews: 0,
	},
	{
		name: 'iPhone 11 Pro 256GB Memory',
		image: '/images/phone.jpg',
		description:
			'Introducing the iPhone 11 Pro. A transformative triple-camera system that adds tons of capability without complexity. An unprecedented leap in battery life',
		brand: 'Apple',
		category: 'Electronics',
		price: 599.99,
		countInStock: 10,
		rating: 0,
		numReviews: 0,
	},
	{
		name: 'Cannon EOS 80D DSLR Camera',
		image: '/images/camera.jpg',
		description:
			'Characterized by versatile imaging specs, the Canon EOS 80D further clarifies itself using a pair of robust focusing systems and an intuitive design',
		brand: 'Cannon',
		category: 'Electronics',
		price: 929.99,
		countInStock: 0,
		rating: 0,
		numReviews: 0,
	},
	{
		name: 'Sony Playstation 4 Pro White Version',
		image: '/images/playstation.jpg',
		description:
			'The ultimate home entertainment center starts with PlayStation. Whether you are into gaming, HD movies, television, music',
		brand: 'Sony',
		category: 'Electronics',
		price: 399.99,
		countInStock: 10,
		rating: 0,
		numReviews: 0,
	},
	{
		name: 'Logitech G-Series Gaming Mouse',
		image: '/images/mouse.jpg',
		description:
			'Get a better handle on your games with this Logitech LIGHTSYNC gaming mouse. The six programmable buttons allow customization for a smooth playing experience',
		brand: 'Logitech',
		category: 'Electronics',
		price: 49.99,
		countInStock: 7,
		rating: 0,
		numReviews: 0,
	},
	{
		name: 'Amazon Echo Dot 3rd Generation',
		image: '/images/alexa.jpg',
		description:
			'Meet Echo Dot - Our most popular smart speaker with a fabric design. It is our most compact smart speaker that fits perfectly into small space',
		brand: 'Amazon',
		category: 'Electronics',
		price: 29.99,
		countInStock: 0,
		rating: 0,
		numReviews: 0,
	},
]

export default products

--#

--% /np/node-mongodb/backend/data/users.js
import bcrypt from 'bcryptjs'

const users = [
	{
		name: 'Admin User',
		email: 'admin@example.com',
		password: bcrypt.hashSync('123456', 10),
		isAdmin: true,
	},
	{
		name: 'John Doe',
		email: 'john@example.com',
		password: bcrypt.hashSync('123456', 10),
	},
	{
		name: 'Jane Doe',
		email: 'jane@example.com',
		password: bcrypt.hashSync('123456', 10),
	},
]

export default users

--#

--% /np/node-mongodb/backend/middleware/authMiddleware.js
import jwt from 'jsonwebtoken'
import asyncHandler from 'express-async-handler'
import User from '../apps/user/model.js'

const protect = asyncHandler(async (req, res, next) => {
	let token

	if (
		req.headers.authorization &&
		req.headers.authorization.startsWith('Bearer')
	) {
		try {
			token = req.headers.authorization.split(' ')[1]

			const decoded = jwt.verify(token, process.env.JWT_SECRET)

			req.user = await User.findById(decoded.id).select('-password')

			next()
		} catch (error) {
			console.error(error)
			res.status(401)
			throw new Error('Not authorized, token failed')
		}
	}

	if (!token) {
		res.status(401)
		throw new Error('Not authorized, no token')
	}
})

const admin = (req, res, next) => {
	if (req.user && req.user.isAdmin) {
		next()
	} else {
		res.status(401)
		throw new Error('Not authorized as an admin')
	}
}

export { protect, admin }

--#

--% /np/node-mongodb/backend/middleware/errorMiddleware.js
const notFound = (req, res, next) => {
	const error = new Error(`Not Found - ${req.originalUrl}`)
	res.status(404)
	next(error)
}

const errorHandler = (err, req, res, next) => {
	const statusCode = res.statusCode === 200 ? 500 : res.statusCode
	res.status(statusCode)
	res.json({
		message: err.message,
		stack: process.env.NODE_ENV === 'production' ? null : err.stack,
	})
}

export { notFound, errorHandler }

--#

--% /np/node-mongodb/backend/orderModel.js
import mongoose from 'mongoose'

const orderSchema = mongoose.Schema(
	{
		user: {
			type: mongoose.Schema.Types.ObjectId,
			required: true,
			ref: 'User',
		},
		orderItems: [
			{
				name: { type: String, required: true },
				qty: { type: Number, required: true },
				image: { type: String, required: true },
				price: { type: Number, required: true },
				product: {
					type: mongoose.Schema.Types.ObjectId,
					required: true,
					ref: 'Product',
				},
			},
		],
		shippingAddress: {
			address: { type: String, required: true },
			city: { type: String, required: true },
			postalCode: { type: String, required: true },
			country: { type: String, required: true },
		},
		paymentMethod: {
			type: String,
			required: true,
		},
		paymentResult: {
			id: { type: String },
			status: { type: String },
			update_time: { type: String },
			email_address: { type: String },
		},
		taxPrice: {
			type: Number,
			required: true,
			default: 0.0,
		},
		shippingPrice: {
			type: Number,
			required: true,
			default: 0.0,
		},
		totalPrice: {
			type: Number,
			required: true,
			default: 0.0,
		},
		isPaid: {
			type: Boolean,
			required: true,
			default: false,
		},
		paidAt: {
			type: Date,
		},
		isDelivered: {
			type: Boolean,
			required: true,
			default: false,
		},
		deliveredAt: {
			type: Date,
		},
	},
	{
		timestamps: true,
	}
)

const Order = mongoose.model('Order', orderSchema)

export default Order

--#

--% /np/node-mongodb/backend/productModel.js
import mongoose from 'mongoose'

const reviewSchema = mongoose.Schema(
	{
		name: { type: String, required: true },
		rating: { type: Number, required: true },
		comment: { type: String, required: true },
		user: {
			type: mongoose.Schema.Types.ObjectId,
			required: true,
			ref: 'User',
		},
	},
	{
		timestamps: true,
	}
)

const productSchema = mongoose.Schema(
	{
		user: {
			type: mongoose.Schema.Types.ObjectId,
			required: true,
			ref: 'User',
		},
		name: {
			type: String,
			required: true,
		},
		image: {
			type: String,
			required: true,
		},
		brand: {
			type: String,
			required: true,
		},
		category: {
			type: String,
			required: true,
		},
		description: {
			type: String,
			required: true,
		},
		reviews: [reviewSchema],
		rating: {
			type: Number,
			required: true,
			default: 0,
		},
		numReviews: {
			type: Number,
			required: true,
			default: 0,
		},
		price: {
			type: Number,
			required: true,
			default: 0,
		},
		countInStock: {
			type: Number,
			required: true,
			default: 0,
		},
	},
	{
		timestamps: true,
	}
)

const Product = mongoose.model('Product', productSchema)

export default Product

--#

--% /np/node-mongodb/backend/userModel.js
import mongoose from 'mongoose'
import bcrypt from 'bcryptjs'

const userSchema = mongoose.Schema(
	{
		name: {
			type: String,
			required: true,
		},
		email: {
			type: String,
			required: true,
			unique: true,
		},
		password: {
			type: String,
			required: true,
		},
		isAdmin: {
			type: Boolean,
			required: true,
			default: false,
		},
	},
	{
		timestamps: true,
	}
)

userSchema.methods.matchPassword = async function (enteredPassword) {
	return await bcrypt.compare(enteredPassword, this.password)
}

userSchema.pre('save', async function (next) {
	if (!this.isModified('password')) {
		next()
	}

	const salt = await bcrypt.genSalt(10)
	this.password = await bcrypt.hash(this.password, salt)
})

const User = mongoose.model('User', userSchema)

export default User

--#

--% /np/node-mongodb/backend/orderRoutes.js
import express from 'express'
const router = express.Router()
import {
	addOrderItems,
	getOrderById,
	updateOrderToPaid,
	updateOrderToDelivered,
	getMyOrders,
	getOrders,
} from '../controllers/orderController.js'
import { protect, admin } from '../middleware/authMiddleware.js'

router.route('/').post(protect, addOrderItems).get(protect, admin, getOrders)
router.route('/myorders').get(protect, getMyOrders)
router.route('/:id').get(protect, getOrderById)
router.route('/:id/pay').put(protect, updateOrderToPaid)
router.route('/:id/deliver').put(protect, admin, updateOrderToDelivered)

export default router

--#

--% /np/node-mongodb/backend/productRoutes.js
import express from 'express'
const router = express.Router()
import {
	getProducts,
	getProductById,
	deleteProduct,
	createProduct,
	updateProduct,
	createProductReview,
	getTopProducts,
} from '../controllers/productController.js'
import { protect, admin } from '../middleware/authMiddleware.js'

router.route('/').get(getProducts).post(protect, admin, createProduct)
router.route('/:id/reviews').post(protect, createProductReview)
router.get('/top', getTopProducts)
router
	.route('/:id')
	.get(getProductById)
	.delete(protect, admin, deleteProduct)
	.put(protect, admin, updateProduct)

export default router

--#

--% /np/node-mongodb/backend/uploadRoutes.js
import path from 'path'
import express from 'express'
import multer from 'multer'

const router = express.Router()

const storage = multer.diskStorage({
	destination(req, file, cb) {
		cb(null, 'uploads/')
	},
	filename(req, file, cb) {
		cb(
			null,
			`${file.fieldname}-${Date.now()}${path.extname(file.originalname)}`
		)
	},
})

function checkFileType(file, cb) {
	const filetypes = /jpg|jpeg|png/
	const extname = filetypes.test(path.extname(file.originalname).toLowerCase())
	const mimetype = filetypes.test(file.mimetype)

	if (extname && mimetype) {
		return cb(null, true)
	} else {
		cb('Images only!')
	}
}

const upload = multer({
	storage,
	fileFilter: function (req, file, cb) {
		checkFileType(file, cb)
	},
})

router.post('/', upload.single('image'), (req, res) => {
	res.send(`/${req.file.path}`)
})

export default router

--#

--% /np/node-mongodb/backend/userRoutes.js
import express from 'express'
const router = express.Router()
import {
	authUser,
	registerUser,
	getUserProfile,
	updateUserProfile,
	getUsers,
	deleteUser,
	getUserById,
	updateUser,
} from '../controllers/userController.js'
import { protect, admin } from '../middleware/authMiddleware.js'

router.route('/').post(registerUser).get(protect, admin, getUsers)
router.post('/login', authUser)
router
	.route('/profile')
	.get(protect, getUserProfile)
	.put(protect, updateUserProfile)
router
	.route('/:id')
	.delete(protect, admin, deleteUser)
	.get(protect, admin, getUserById)
	.put(protect, admin, updateUser)

export default router

--#

--% /np/node-mongodb/backend/utils/generateToken.js
import jwt from 'jsonwebtoken'

const generateToken = (id) => {
	return jwt.sign({ id }, process.env.JWT_SECRET, {
		expiresIn: '30d',
	})
}

export default generateToken

--#

--% /np/node-mongodb/uploads/file.txt
Add to git repo
--#
