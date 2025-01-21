--% index/fmus
.,d
	review,d
		model.js,f(f=model.js,@ra=review_model_replace_line="const reviewSchema = mongoose.Schema")
	product,d
		model.js,f(f=model.js,@ia=product_model_extra_import="// extra schemas")
		model.js,f(f=model.js,@ib=product_model_above_brand="brand: { type: String, required: false },")

		route.js,f(f=route.js,@ia=product_route_extra_imports="// extra imports")
		route.js,f(f=route.js,@ia=product_route_extra_exported_methods="// extra exported methods")
		route.js,f(f=route.js,@ia=product_route_extra_routes="// extra routes")
		route.js,f(f=route.js,@rs="productCreate)"="protect, admin, productCreate)")
		#route.js,f(f=route.js,@rs="productList)"="protect, admin, productList)")
		#route.js,f(f=route.js,@rs="productDetail)"="protect, productDetail)")
		route.js,f(f=route.js,@rs="productUpdate)"="protect, admin, productUpdate)")
		route.js,f(f=route.js,@rs="productDelete)"="protect, admin, productDelete)")
		controller.js,f(f=controller.js,@ia=product_controller_extra_controller="// extra controllers")
		controller.js,f(f=controller.js,@ia=product_controller_extra_exports="// extra exports")

		controller.js,f(f=controller.js,@rb=product_controller_create="// create starts"="// create ends")
		controller.js,f(f=controller.js,@rb=product_controller_list="// list starts"="// list ends")
		controller.js,f(f=controller.js,@rb=product_controller_update="// update starts"="// update ends")
	order,d
		model.js,f(f=model.js,@ib=order_model_above_deliveredat="deliveredAt: { type: Date, required: false },")
		route.js,f(f=route.js,@ia=order_route_extra_imports="// extra imports")
		route.js,f(f=route.js,@ia=order_route_extra_exported_methods="// extra exported methods")
		route.js,f(f=route.js,@ia=order_route_extra_routes="// extra routes")
		route.js,f(f=route.js,@rs="orderCreate)"="protect, orderCreate)")
		route.js,f(f=route.js,@rs="orderList)"="protect, admin, orderList)")
		route.js,f(f=route.js,@rs="orderDetail)"="protect, orderDetail)")
		route.js,f(f=route.js,@rs="orderUpdate)"="protect, orderUpdate)")
		route.js,f(f=route.js,@rs="orderDelete)"="protect, orderDelete)")
		controller.js,f(f=controller.js,@ia=order_controller_extra_controller="// extra controllers")
		controller.js,f(f=controller.js,@ia=order_controller_extra_exports="// extra exports")
		controller.js,f(f=controller.js,@rb=order_controller_create="// create starts"="// create ends")
		controller.js,f(f=controller.js,@rb=order_controller_list="// list starts"="// list ends")
		controller.js,f(f=controller.js,@rb=order_controller_detail="// detail starts"="// detail ends")
	user,d
		model.js,f(f=model.js,@ib=user_model_extra_methods="// extra methods")
		model.js,f(f=model.js,@ia=user_model_extra_imports="// extra imports")
		route.js,f(f=route.js,@ia=user_route_extra_imports="// extra imports")
		route.js,f(f=route.js,@ia=user_route_extra_exported_methods="// extra exported methods")
		route.js,f(f=route.js,@ia=user_route_extra_routes="// extra routes")

		route.js,f(f=route.js,@rs="userCreate)"="registerUser)")
		route.js,f(f=route.js,@rs="userList)"="protect, admin, userList)")
		route.js,f(f=route.js,@rs="userDetail)"="protect, admin, userDetail)")
		route.js,f(f=route.js,@rs="userUpdate)"="protect, admin, userUpdate)")
		route.js,f(f=route.js,@rs="userDelete)"="protect, admin, userDelete)")

		controller.js,f(f=controller.js,@ia=user_controller_extra_controller="// extra controllers")
		controller.js,f(f=controller.js,@ia=user_controller_extra_exports="// extra exports")
		controller.js,f(f=controller.js,@ia=user_controller_extra_imports="// extra imports")
		controller.js,f(f=controller.js,@rb=user_controller_create="// create starts"="// create ends")
		controller.js,f(f=controller.js,@rb=user_controller_detail="// detail starts"="// detail ends")
		controller.js,f(f=controller.js,@rb=user_controller_update="// update starts"="// update ends")
--#

--% user_controller_update
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
--#

--% user_controller_detail
  const user = await User.findById(req.params.id).select('-password')

  if (user) {
    res.json(user)
  } else {
    res.status(404)
    throw new Error('User not found')
  }
--#

--% user_controller_create
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
--#

--% product_controller_create
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
--#

--% product_controller_update
  const {
    brand,
    category,
    countInStock,
		description,
		image,
		name,
    price,        
  } = req.body

  const product = await Product.findById(req.params.id)

  if (product) {
    product.brand = brand
    product.category = category
    product.countInStock = countInStock
    product.description = description
    product.image = image
    product.name = name
    product.price = price

    const updatedProduct = await product.save()
    res.json(updatedProduct)
  } else {
    res.status(404)
    throw new Error('Product not found')
  }
--#

--% product_controller_list
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
--#

--% order_controller_detail
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
--#

--% order_controller_list
  const orders = await Order.find({}).populate('user', 'id name')
  res.json(orders)
--#

--% order_controller_create
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
--#

--% product_model_extra_import
import {reviewSchema} from '../review/model.js'
--#

--% product_model_above_brand
    reviews: [reviewSchema],
--#

--% review_model_replace_line
export const reviewSchema = mongoose.Schema(
--#

--% order_model_above_deliveredat
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
    paymentResult: {
      id: { type: String },
      status: { type: String },
      update_time: { type: String },
      email_address: { type: String },
    },
--#

--% user_model_extra_imports
import bcrypt from 'bcryptjs'
--#

--% user_model_extra_methods
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
--#

--% order_route_extra_imports
import { protect, admin } from '../../middleware/authMiddleware.js'
--#

--% order_route_extra_routes
router.route('/myorders').get(protect, getMyOrders)
router.route('/:id/pay').put(protect, updateOrderToPaid)
router.route('/:id/deliver').put(protect, admin, updateOrderToDelivered)
--#

--% order_route_extra_exported_methods
  getMyOrders,
  updateOrderToDelivered,
  updateOrderToPaid,
--#

--% order_controller_extra_controller

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
--#

--% order_controller_extra_exports
  getMyOrders,
  updateOrderToDelivered,
  updateOrderToPaid,
--#

--% product_route_extra_imports
import { protect, admin } from '../../middleware/authMiddleware.js'
--#

--% product_route_extra_exported_methods
  createProductReview,
  getTopProducts,
--#

--% product_route_extra_routes
router.route('/:id/reviews').post(protect, createProductReview)
router.get('/top', getTopProducts)
--#

--% product_controller_extra_controller

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
--#

--% product_controller_extra_exports
  createProductReview,
  getTopProducts,
--#

--% user_route_extra_imports
import { protect, admin } from '../../middleware/authMiddleware.js'
--#

--% user_route_extra_exported_methods
  userCreate as registerUser,
  authUser,
  getUserProfile,
  updateUserProfile,
--#

--% user_route_extra_routes
router.post('/login', authUser)
router
  .route('/profile')
  .get(protect, getUserProfile)
  .put(protect, updateUserProfile)
--#

--% user_controller_extra_controller

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
--#

--% user_controller_extra_exports
  authUser,
  getUserProfile,
  updateUserProfile,
--#

--% user_controller_extra_imports
import generateToken from '../../utils/generateToken.js'
--#
