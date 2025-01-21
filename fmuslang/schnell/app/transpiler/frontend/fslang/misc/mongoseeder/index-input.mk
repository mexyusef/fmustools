--% index/fmus
mongoseeder,d(/mk)
	package.json,f(e=__FILE__=package.json)
	seeder.js,f(e=__FILE__=seeder.js)
	db.js,f(e=__FILE__=db.js)
	models.js,f(e=__FILE__=models.js)
	.env,f(e=__FILE__=.env)
	data,d(/mk)
		products.js,f(e=__FILE__=products.js)
		users.js,f(e=__FILE__=users.js)
--#

--% .env
MONGO_URI=mongodb://usef:rahasia@localhost/tempdb?authSource=admin
--#

--% models.js
import mongoose from 'mongoose'
import bcrypt from 'bcryptjs'

const productSchema = mongoose.Schema(  
  {
    brand: { type: String, required: false },
    category: { type: String, required: false },
    countInStock: { type: Number, required: false, default: 0 },
    description: { type: String, required: false },
    image: { type: String, required: false },
    name: { type: String, required: false },
    numReviews: { type: Number, required: false, default: 0 },
    price: { type: Number, required: false },
    rating: { type: Number, required: false },
    user: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: false }
	},
  {
    timestamps: true,
  }
)
export const Product = mongoose.model('Product', productSchema)


const userSchema = mongoose.Schema(  
  {
    email: String,
    first_name: String,
    isAdmin: { type: Boolean, required: true, default: true },
    is_active: Boolean,
    is_staff: Boolean,
    last_name: String,
    name: String,
    password: { type: String, required: true },
    phone: String,
    roles: { type: String, default: "user", enum: ['admin', 'user', 'guest'] },
    username: String
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

export const User = mongoose.model('User', userSchema)
--#


--% package.json
{
	"name": "mongoseeder",
	"version": "1.0.0",
	"description": "Mongo Seeder",
	"main": "server.js",
	"type": "module",
	"scripts": {
		"start": "node seeder",
		"data:import": "node seeder",
		"data:destroy": "node seeder -d",

		"heroku-postbuild": "NPM_CONFIG_PRODUCTION=false npm install --prefix frontend && npm run build --prefix frontend",
		"server": "nodemon backend/server",
		"client": "npm start --prefix frontend",
		"dev": "concurrently \"npm run server\" \"npm run client\""
	},
	"author": "Yusef Ulum",
	"license": "MIT",
	"dependencies": {
		"bcryptjs": "^2.4.3",
		"colors": "^1.4.0",
		"dotenv": "^8.2.0",
		"mongoose": "^5.10.6"
	},
	"devDependencies": {
		"concurrently": "^5.3.0",
		"nodemon": "^2.0.4"
	}
}
--#

--% seeder.js
import mongoose, { models } from 'mongoose'
import dotenv from 'dotenv'
// import colors from 'colors'

import users from './data/users.js'
import products from './data/products.js'

import {Product,User} from './models.js'

import connectDB from './db.js'

dotenv.config()

connectDB()

const importData = async () => {
	try {

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

--% db.js
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

--% products.js
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

--% users.js
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
