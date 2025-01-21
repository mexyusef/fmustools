--% index/fmus
.,d
	cart,d
		detail.js,f(f=detail.js,@rc=isi_cart_screen)
	order,d
		detail.js,f(f=detail.js,@rc=isi_order_screen)
		list.js,f(f=list.js,@rc=isi_orderlist_screen)
	product,d
		detail.js,f(f=detail.js,@rc=isi_productdetail_screen)
		update.js,f(f=update.js,@rc=isi_productupdate_screen)
		list.js,f(f=list.js,@rc=isi_productlist_screen)
		gallery.js,f(e=__FILE__=isi_product_gallery)
	shippingaddress,d
		detail.js,f(f=detail.js,@rc=isi_shipping_screen)
	user,d
		list.js,f(f=list.js,@rc=isi_userlist_screen)
--#

--% isi_cart_screen
import React, { useEffect } from 'react'
import { Link } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import { Row, Col, ListGroup, Image, Form, Button, Card } from 'react-bootstrap'

import Message from '../../components/Message'
import { addToCart, removeFromCart } from '../../store/cart/cartActions'
import config from '../../store/config'

function CartDetail({ match, location, history }) {
  const productId = match.params.id
  const qty = location.search ? Number(location.search.split('=')[1]) : 1
  const dispatch = useDispatch()

  const cart = useSelector(state => state.cart)
  const { cartItems } = cart

  useEffect(() => {
    if (productId) {
      dispatch(addToCart(productId, qty))
    }
  }, [dispatch, productId, qty])

  const removeFromCartHandler = (id) => {
    dispatch(removeFromCart(id))
  }

  const checkoutHandler = () => {
    history.push('/login?redirect=shipping')
  }

  return (<>
	{/* <Row>
		<Col>
		<Link className='btn btn-light my-3' to='/' onClick={()=>history.goBack()}>Back</Link>
		</Col>
	</Row> */}

    <Row>		
      <Col md={8}>
        <h1>Shopping Cart</h1>
        {cartItems.length === 0 ? (
          <Message variant='info'>
            Your cart is empty <Link to='/'>Go Back</Link>
          </Message>
        ) : (
          <ListGroup variant='flush'>
            {cartItems.map(item => (
              <ListGroup.Item key={item.product}>
                <Row>
                  <Col md={2}>
                    <Image src={item.image} alt={item.name} fluid rounded />
                  </Col>
                  <Col md={3}>
                    <Link to={`/product/${item.product}`}>{item.name}</Link>
                  </Col>

                  <Col md={2}>
                    ${item.price}
                  </Col>

                  <Col md={3}>
                    <Form.Control
                      as="select"
                      value={item.qty}
                      onChange={(e) => dispatch(addToCart(item.product, Number(e.target.value)))}
                    >
                      {
                        [...Array(item.countInStock).keys()].map((x) => (
                          <option key={x + 1} value={x + 1}>
                            {x + 1}
                          </option>
                        ))
                      }
                    </Form.Control>
                  </Col>

                  <Col md={1}>
                    <Button
                      type='button'
                      variant='light'
                      onClick={() => removeFromCartHandler(item.product)}
                    >
                      <i className='fas fa-trash'></i>
                    </Button>
                  </Col>
                </Row>
              </ListGroup.Item>
            ))}
          </ListGroup>
        )}
      </Col>

      <Col md={4}>
        <Card>
          <ListGroup variant='flush'>
            <ListGroup.Item>
              <h2>Subtotal ({cartItems.reduce((acc, item) => acc + item.qty, 0)}) items</h2>
              ${cartItems.reduce((acc, item) => acc + item.qty * item.price, 0).toFixed(2)}
            </ListGroup.Item>
          </ListGroup>

          <ListGroup.Item>
            <Button
              type='button'
              className='btn-block'
              disabled={cartItems.length === 0}
              onClick={checkoutHandler}
            >
              Proceed To Checkout
            </Button>
          </ListGroup.Item>
        </Card>
      </Col>
    </Row>
		</>
  )
}

export default CartDetail
--#

--% isi_orderlist_screen
import React, { useEffect, useState } from 'react'
import { LinkContainer } from 'react-router-bootstrap'
import { Table, Button } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'

import Loader from '../../components/Loader'
import Message from '../../components/Message'
// import MyAlert from '../../components/MyAlert'

import { orderList as listOrders } from '../../store/order/orderActions'
// import { ORDER_DELETE_RESET } from '../../store/order/orderConstants'

function OrderList({ history }) {

  const dispatch = useDispatch()
  // const [showDeleteError, setShowDeleteError] = useState(true)

  const orderList = useSelector(state => state.orderList)
  const { loading, error, orders } = orderList

  const userLogin = useSelector(state => state.userLogin)
  const { userInfo } = userLogin

  useEffect(() => {
    if (userInfo && userInfo.isAdmin) {
      dispatch(listOrders())
    } else {
      history.push('/login')
    }
  }, [dispatch, history, userInfo])


  return (
    <div>
      <h1>Orders</h1>
      {/* {error && showDeleteError ? <MyAlert body={error} hapus={()=>{
        setShowDeleteError(false)
        dispatch({type:ORDER_DELETE_RESET})
      }}/> : null} */}
      {loading
        ? (<Loader />)
        : error
          ? (<Message variant='danger'>{error}</Message>)
          : (
            <Table striped bordered hover responsive className='table-sm'>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>USER</th>
                  <th>DATE</th>
                  <th>Total</th>
                  <th>PAID</th>
                  <th>DELIVERED</th>
                  <th></th>
                </tr>
              </thead>

              <tbody>
                {orders.map(order => (
                  <tr key={order._id}>
                    <td>{order._id}</td>
                    <td>{order.user && order.user.name}</td>
                    <td>{order.created_at.substring(0, 10)}</td>
                    <td>${order.totalPrice}</td>

                    <td>{order.isPaid ? (
                      order.paidAt.substring(0, 10)
                    ) : (
                      <i className='fas fa-check' style={{ color: 'red' }}></i>
                    )}
                    </td>

                    <td>{order.isDelivered ? (
                      order.deliveredAt.substring(0, 10)
                    ) : (
                      <i className='fas fa-check' style={{ color: 'red' }}></i>
                    )}
                    </td>

                    <td>
                      <LinkContainer to={`/order/${order._id}`}>
                        <Button variant='light' className='btn-sm'>
                          Details
                        </Button>
                      </LinkContainer>
                    </td>
                  </tr>
                ))}
              </tbody>
            </Table>
          )}
    </div>
  )
}

export default OrderList
--#

--% isi_order_screen
import React, { useState, useEffect } from 'react'
import { Button, Row, Col, ListGroup, Image, Card } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'
import { PayPalButton } from 'react-paypal-button-v2'

import Message from '../../components/Message'
import Loader from '../../components/Loader'

import { orderDetail as getOrderDetails, payOrder, deliverOrder } from '../../store/order/orderActions'
import { ORDER_PAY_RESET, ORDER_DELIVER_RESET } from '../../store/order/orderConstants'
import config from '../../store/config'

function OrderDetail({ match, history }) {
  const orderId = match.params.id
  const dispatch = useDispatch()


  const [sdkReady, setSdkReady] = useState(false)

  const orderDetails = useSelector(state => state.orderDetail)
  const { order, error, loading } = orderDetails

  const orderPay = useSelector(state => state.orderPay)
  const { loading: loadingPay, success: successPay } = orderPay

  const orderDeliver = useSelector(state => state.orderDeliver)
  const { loading: loadingDeliver, success: successDeliver } = orderDeliver

  const userLogin = useSelector(state => state.userLogin)
  const { userInfo } = userLogin


  if (!loading && !error) {
    order.itemsPrice = order.orderItems.reduce((acc, item) => acc + item.price * item.qty, 0).toFixed(2)
  }


  const addPayPalScript = () => {
    const script = document.createElement('script')
    script.type = 'text/javascript'
    script.src = 'https://www.paypal.com/sdk/js?client-id=AeDXja18CkwFUkL-HQPySbzZsiTrN52cG13mf9Yz7KiV2vNnGfTDP0wDEN9sGlhZHrbb_USawcJzVDgn'
    script.async = true
    script.onload = () => {
      setSdkReady(true)
    }
    document.body.appendChild(script)
  }

  useEffect(() => {

    if (!userInfo) {
      history.push('/login')
    }

    if (!order || successPay || order._id !== Number(orderId) || successDeliver) {
      dispatch({ type: ORDER_PAY_RESET })
      dispatch({ type: ORDER_DELIVER_RESET })

      dispatch(getOrderDetails(orderId))
    } else if (!order.isPaid) {
      if (!window.paypal) {
        addPayPalScript()
      } else {
        setSdkReady(true)
      }
    }
  }, [dispatch, history, userInfo, order, orderId, successPay, successDeliver])


  const successPaymentHandler = (paymentResult) => {
    dispatch(payOrder(orderId, paymentResult))
  }

  const deliverHandler = () => {
    dispatch(deliverOrder(order))
  }

  return loading ? (
    <Loader />
  ) : error ? (
    <Message variant='danger'>{error}</Message>
  ) : (
    <div>
      <h1>Order: {order.Id}</h1>
      <Row>
        <Col md={8}>
          <ListGroup variant='flush'>
            <ListGroup.Item>
              <h2>Shipping</h2>
              <p><strong>Name: </strong> {order.user.name}</p>
              <p><strong>Email: </strong><a href={`mailto:${order.user.email}`}>{order.user.email}</a></p>
              <p>
                <strong>Shipping: </strong>
                {order.shippingAddress.address},  {order.shippingAddress.city}
                {'  '}
                {order.shippingAddress.postalCode},
                {'  '}
                {order.shippingAddress.country}
              </p>

              {order.isDelivered ? (
                <Message variant='success'>Delivered on {order.deliveredAt}</Message>
              ) : (
                <Message variant='warning'>Not Delivered</Message>
              )}
            </ListGroup.Item>

            <ListGroup.Item>
              <h2>Payment Method</h2>
              <p>
                <strong>Method: </strong>
                {order.paymentMethod}
              </p>
              {order.isPaid ? (
                <Message variant='success'>Paid on {order.paidAt}</Message>
              ) : (
                <Message variant='warning'>Not Paid</Message>
              )}

            </ListGroup.Item>

            <ListGroup.Item>
              <h2>Order Items</h2>
              {order.orderItems.length === 0 ? <Message variant='info'>
                Order is empty
              </Message> : (
                <ListGroup variant='flush'>
                  {order.orderItems.map((item, index) => (
                    <ListGroup.Item key={index}>
                      <Row>
                        <Col md={1}>
                          <Image src={config.img(item.image)} alt={item.name} fluid rounded />
                        </Col>

                        <Col>
                          <Link to={`/product/${item.product}`}>{item.name}</Link>
                        </Col>

                        <Col md={4}>
                          {item.qty} X ${item.price} = ${(item.qty * item.price).toFixed(2)}
                        </Col>
                      </Row>
                    </ListGroup.Item>
                  ))}
                </ListGroup>
              )}
            </ListGroup.Item>

          </ListGroup>

        </Col>

        <Col md={4}>
          <Card>
            <ListGroup variant='flush'>
              <ListGroup.Item>
                <h2>Order Summary</h2>
              </ListGroup.Item>

              <ListGroup.Item>
                <Row>
                  <Col>Items:</Col>
                  <Col>${order.itemsPrice}</Col>
                </Row>
              </ListGroup.Item>

              <ListGroup.Item>
                <Row>
                  <Col>Shipping:</Col>
                  <Col>${order.shippingPrice}</Col>
                </Row>
              </ListGroup.Item>

              <ListGroup.Item>
                <Row>
                  <Col>Tax:</Col>
                  <Col>${order.taxPrice}</Col>
                </Row>
              </ListGroup.Item>

              <ListGroup.Item>
                <Row>
                  <Col>Total:</Col>
                  <Col>${order.totalPrice}</Col>
                </Row>
              </ListGroup.Item>


              {!order.isPaid && (
                <ListGroup.Item>
                  {loadingPay && <Loader />}

                  {!sdkReady ? (
                    <Loader />
                  ) : (
                    <PayPalButton
                      amount={order.totalPrice}
                      onSuccess={successPaymentHandler}
                    />
                  )}
                </ListGroup.Item>
              )}
            </ListGroup>
            {loadingDeliver && <Loader />}
            {userInfo && userInfo.isAdmin && order.isPaid && !order.isDelivered && (
              <ListGroup.Item>
                <Button
                  type='button'
                  className='btn btn-block'
                  onClick={deliverHandler}
                >
                  Mark As Delivered
                </Button>
              </ListGroup.Item>
            )}
          </Card>
        </Col>
      </Row>
    </div>
  )
}

export default OrderDetail
--#

--% isi_product_gallery
import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link } from 'react-router-dom'
import { Carousel, Image } from 'react-bootstrap'

import Loader from '../../components/Loader'
import Message from '../../components/Message'

import { listTopProducts } from '../../store/product/productActions'
import config from '../../store/config'

function ProductGallery() {
  const dispatch = useDispatch()

  const productTopRated = useSelector(state => state.productTopRated)
  const { error, loading, products } = productTopRated

  useEffect(() => {
    dispatch(listTopProducts())
  }, [dispatch])

  return (loading ? <Loader />
    : error
      ? <Message variant='danger'>{error}</Message>
      : (
        <Carousel pause='hover' className='bg-dark'>
          {products.map(product => (
            <Carousel.Item key={product._id}>
              <Link to={`/product/${product._id}`}>
                <Image src={config.serverPath(config.backend.paths.static_images.path + product.image)} alt={product.name} fluid />
                <Carousel.Caption className='carousel.caption'>
                  <h4>{product.name} (${product.price})</h4>
                </Carousel.Caption>
              </Link>
            </Carousel.Item>
          ))}
        </Carousel>
      )
  )
}

export default ProductGallery
--#

--% isi_productlist_screen
import React, { useEffect, useState } from 'react'
import { LinkContainer } from 'react-router-bootstrap'
import { Table, Button, Row, Col } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'

import Loader from '../../components/Loader'
import Message from '../../components/Message'
import Paginate from '../../components/Paginate'
import MyAlert from '../../components/MyAlert'

import { productList as listProducts, productDelete as deleteProduct, productCreate as createProduct } from '../../store/product/productActions'
import { PRODUCT_CREATE_RESET, PRODUCT_DELETE_RESET } from '../../store/product/productConstants'

function ProductList({ history, match }) {

  const dispatch = useDispatch()
  const [showDeleteError, setShowDeleteError] = useState(true)

  const productList = useSelector(state => state.productList)
  const { loading, error, products, pages, page } = productList

  const productDelete = useSelector(state => state.productDelete)
  const { loading: loadingDelete, error: errorDelete, success: successDelete } = productDelete

  const productCreate = useSelector(state => state.productCreate)
  const { loading: loadingCreate, error: errorCreate, success: successCreate, product: createdProduct } = productCreate

  const userLogin = useSelector(state => state.userLogin)
  const { userInfo } = userLogin

  let keyword = history.location.search
  useEffect(() => {
    dispatch({ type: PRODUCT_CREATE_RESET })

    if (!userInfo.isAdmin) {
      history.push('/login')
    }

    if (successCreate) {
      history.push(`/product/${createdProduct._id}/edit`)
    } else {
      dispatch(listProducts(keyword))
    }

  }, [dispatch, history, userInfo, successDelete, successCreate, createdProduct, keyword])


  const deleteHandler = (id) => {

    if (window.confirm('Are you sure you want to delete this product?')) {
      dispatch(deleteProduct(id))
    }
  }

  const createProductHandler = () => {
    dispatch(createProduct())
  }

  return (
    <div>
      <Row className='align-items-center'>
        <Col>
          <h1>Products</h1>
        </Col>

        <Col className='text-right'>
          <Button className='my-3' onClick={createProductHandler}>
            <i className='fas fa-plus'></i> Create Product
          </Button>
        </Col>
      </Row>

      {loadingDelete && <Loader />}
      {errorDelete && <Message variant='danger'>{errorDelete}</Message>}

      {loadingCreate && <Loader />}
      {errorCreate && <Message variant='danger'>{errorCreate}</Message>}

      {errorDelete && showDeleteError ? <MyAlert body={errorDelete} hapus={()=>{
        setShowDeleteError(false)
        dispatch({type:PRODUCT_DELETE_RESET})
      }}/> : null}

      {loading
        ? (<Loader />)
        : error
          ? (<Message variant='danger'>{error}</Message>)
          : (
            <div>
              <Table striped bordered hover responsive className='table-sm'>
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>NAME</th>
                    <th>PRICE</th>
                    <th>CATEGORY</th>
                    <th>BRAND</th>
                    <th></th>
                  </tr>
                </thead>

                <tbody>
                  {products.map(product => (
                    <tr key={product._id}>
                      <td>{product._id}</td>
                      <td>{product.name}</td>
                      <td>${product.price}</td>
                      <td>{product.category}</td>
                      <td>{product.brand}</td>

                      <td>
                        <LinkContainer to={`/admin/product/${product._id}/edit`}>
                          <Button variant='light' className='btn-sm'>
                            <i className='fas fa-edit'></i>
                          </Button>
                        </LinkContainer>

                        <Button variant='danger' className='btn-sm' onClick={() => deleteHandler(product._id)}>
                          <i className='fas fa-trash'></i>
                        </Button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </Table>
              <Paginate pages={pages} page={page} isAdmin={true} />
            </div>
          )}
    </div>
  )
}

export default ProductList
--#

--% isi_productupdate_screen
import React, { useState, useEffect } from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import { Form, Button } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'

import Loader from '../../components/Loader'
import Message from '../../components/Message'
import FormContainer from '../../components/FormContainer'

import { productDetail as listProductDetails, productUpdate as updateProduct } from '../../store/product/productActions'
import { PRODUCT_UPDATE_RESET } from '../../store/product/productConstants'
import config from '../../store/config'

const ProductUpdate = ({ match, history }) => {
	const product_list_route = '/admin/productlist'

	const productId = match.params.id

  const [name, setName] = useState('')
  const [price, setPrice] = useState(0)
  const [image, setImage] = useState('')
  const [brand, setBrand] = useState('')
  const [category, setCategory] = useState('')
  const [countInStock, setCountInStock] = useState(0)
  const [description, setDescription] = useState('')
  const [uploading, setUploading] = useState(false)

  const dispatch = useDispatch()

  const productDetails = useSelector(state => state.productDetail)
  const { error, loading, product } = productDetails

  const productUpdate = useSelector(state => state.productUpdate)
  const { error: errorUpdate, loading: loadingUpdate, success: successUpdate } = productUpdate

  useEffect(() => {
    if (successUpdate) {
      dispatch({ type: PRODUCT_UPDATE_RESET })
      history.push(product_list_route)
    } else {
      if (!product.name || product._id !== Number(productId)) {
        dispatch(listProductDetails(productId))
      } else {
        setName(product.name)
        setPrice(product.price)
        setImage(product.image)
        setBrand(product.brand)
        setCategory(product.category)
        setCountInStock(product.countInStock)
        setDescription(product.description)
      }
    }
  }, [dispatch, product, productId, history, successUpdate])

  const submitHandler = (e) => {
    e.preventDefault()
    dispatch(updateProduct({
      _id: productId,
      name,
      price,
      image,
      brand,
      category,
      countInStock,
      description
    }))
  }

  const uploadFileHandler = async (e) => {
    const file = e.target.files[0]
    const formData = new FormData()
    formData.append('image', file)
    formData.append('product_id', productId)
    setUploading(true)
    try {
      const { data } = await axios.post(
				config.serverPath(config.backend.paths.upload_image.path),
				formData, 
				{ headers: { 'Content-Type': 'multipart/form-data' } }
			)
      setImage(data)
      setUploading(false)
    } catch (error) {
      setUploading(false)
    }
  }

	return (<>
    <Link to={product_list_route} className='btn btn-light my-3'>Back</Link>
		<h1>ProductUpdate</h1>

		<FormContainer>
        <h1>Edit Product</h1>
        {loadingUpdate && <Loader />}
        {errorUpdate && <Message variant='danger'>{errorUpdate}</Message>}

        {loading ? <Loader /> : error ? <Message variant='danger'>{error}</Message>
          : (
            <Form onSubmit={submitHandler}>


		{/* auto for _id */}
		
		<Form.Group controlId='brand'>
		  <Form.Label>brand</Form.Label>
		  <Form.Control
		    type='text'
		    placeholder='Enter brand'
		    value={brand}
		    onChange={(e) => setBrand(e.target.value)}
		  >
		  </Form.Control>
		</Form.Group>
		
		<Form.Group controlId='category'>
		  <Form.Label>category</Form.Label>
		  <Form.Control
		    type='text'
		    placeholder='Enter category'
		    value={category}
		    onChange={(e) => setCategory(e.target.value)}
		  >
		  </Form.Control>
		</Form.Group>
		
		<Form.Group controlId='countinstock'>
		  <Form.Label>countInStock</Form.Label>
		  <Form.Control
		    type='number'
		    placeholder='Enter countinstock'
		    value={countInStock}
		    onChange={(e) => setCountInStock(e.target.value)}
		  >
		  </Form.Control>
		</Form.Group>
		
		<Form.Group controlId='description'>
		  <Form.Label>description</Form.Label>
		  <Form.Control
		    type='text'
		    placeholder='Enter description'
		    value={description}
		    onChange={(e) => setDescription(e.target.value)}
		  >
		  </Form.Control>
		</Form.Group>
		
		<Form.Group controlId='image'>
		  <Form.Label>image</Form.Label>
		  <Form.Control
		    type='text'
		    placeholder='Enter image'
		    value={image}
		    onChange={(e) => setImage(e.target.value)}
		  >
		  </Form.Control>
		
		    <Form.File
		      id='image-file'
		      label='Choose File'
		      custom
		      onChange={uploadFileHandler}
		    >
		    </Form.File>
		    {uploading && <Loader />}
		
		</Form.Group>
		
		<Form.Group controlId='name'>
		  <Form.Label>name</Form.Label>
		  <Form.Control
		    type='text'
		    placeholder='Enter name'
		    value={name}
		    onChange={(e) => setName(e.target.value)}
		  >
		  </Form.Control>
		</Form.Group>
		
		{/* <Form.Group controlId='numreviews'>
		  <Form.Label>numReviews</Form.Label>
		  <Form.Control
		    type='number'
		    placeholder='Enter numreviews'
		    value={numReviews}
		    onChange={(e) => setNumReviews(e.target.value)}
		  >
		  </Form.Control>
		</Form.Group> */}
		
		<Form.Group controlId='price'>
		  <Form.Label>price</Form.Label>
		  <Form.Control
		    type='number'
		    placeholder='Enter price'
		    value={price}
		    onChange={(e) => setPrice(e.target.value)}
		  >
		  </Form.Control>
		</Form.Group>
		
		{/* <Form.Group controlId='rating'>
		  <Form.Label>rating</Form.Label>
		  <Form.Control
		    type='number'
		    placeholder='Enter rating'
		    value={rating}
		    onChange={(e) => setRating(e.target.value)}
		  >
		  </Form.Control>
		</Form.Group> */}
		
		{/* django_foreign_key for user */}


              <Button type='submit' variant='primary'>Update</Button>
            </Form>
          )}

      </FormContainer >
	</>);
};

export default ProductUpdate;
--#

--% isi_productdetail_screen
import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link } from 'react-router-dom'
import { Row, Col, Image, ListGroup, Button, Card, Form } from 'react-bootstrap'

import Rating from '../../components/Rating'
import Loader from '../../components/Loader'
import Message from '../../components/Message'

import { productDetail as listProductDetails, createProductReview } from '../../store/product/productActions'
import { PRODUCT_CREATE_REVIEW_RESET } from '../../store/product/productConstants'
import config from '../../store/config'

function ProductDetail({ match, history }) {
  const [qty, setQty] = useState(1)
  const [rating, setRating] = useState(0)
  const [comment, setComment] = useState('')

  const dispatch = useDispatch()

  const productDetails = useSelector(state => state.productDetail)
  const { loading, error, product } = productDetails

  const userLogin = useSelector(state => state.userLogin)
  const { userInfo } = userLogin

  const productReviewCreate = useSelector(state => state.productReviewCreate)
  const {
    loading: loadingProductReview,
    error: errorProductReview,
    success: successProductReview,
  } = productReviewCreate

  useEffect(() => {
    if (successProductReview) {
      setRating(0)
      setComment('')
      dispatch({ type: PRODUCT_CREATE_REVIEW_RESET })
    }
    console.log(`
      ProductDetail, product detail request ${match.params.id}
    `);
    dispatch(listProductDetails(match.params.id))
  }, [dispatch, match, successProductReview])

  const addToCartHandler = () => {
    history.push(`/cart/${match.params.id}?qty=${qty}`)
  }

  const submitHandler = (e) => {
    e.preventDefault()
    dispatch(createProductReview(
      match.params.id, {
      rating,
      comment
    }
    ))
  }

  return (
    <div>
      <Link to='/' className='btn btn-light my-3'>Back</Link>
      {loading ?
        <Loader />
        : error
          ? <Message variant='danger'>{error}</Message>
          : (
            <div>
              <Row>
                <Col md={6}>
                  <Image src={config.serverPath(config.backend.paths.static_images.path + product.image)} alt={product.name} fluid />
                </Col>

                <Col md={3}>
                  <ListGroup variant="flush">
                    <ListGroup.Item>
                      <h3>{product.name}</h3>
                    </ListGroup.Item>

                    <ListGroup.Item>
                      <Rating value={product.rating} text={`${product.numReviews} reviews`} color={'#f8e825'} />
                    </ListGroup.Item>

                    <ListGroup.Item>
                      Price: ${product.price}
                    </ListGroup.Item>

                    <ListGroup.Item>
                      Description: {product.description}
                    </ListGroup.Item>
                  </ListGroup>
                </Col>

                <Col md={3}>
                  <Card>
                    <ListGroup variant='flush'>
                      <ListGroup.Item>
                        <Row>
                          <Col>Price:</Col>
                          <Col>
                            <strong>${product.price}</strong>
                          </Col>
                        </Row>
                      </ListGroup.Item>

                      <ListGroup.Item>
                        <Row>
                          <Col>Status:</Col>
                          <Col>
                            {product.countInStock > 0 ? 'In Stock' : 'Out of Stock'}
                          </Col>
                        </Row>
                      </ListGroup.Item>

                      {product.countInStock > 0 && (
                        <ListGroup.Item>
                          <Row>
                            <Col>Qty</Col>
                            <Col xs='auto' className='my-1'>
                              <Form.Control
                                as="select"
                                value={qty}
                                onChange={(e) => setQty(e.target.value)}
                              >
                                {

                                  [...Array(product.countInStock).keys()].map((x) => (
                                    <option key={x + 1} value={x + 1}>
                                      {x + 1}
                                    </option>
                                  ))
                                }

                              </Form.Control>
                            </Col>
                          </Row>
                        </ListGroup.Item>
                      )}


                      <ListGroup.Item>
                        <Button
                          onClick={addToCartHandler}
                          className='btn-block'
                          disabled={product.countInStock === 0}
                          type='button'>
                          Add to Cart
                        </Button>
                      </ListGroup.Item>
                    </ListGroup>
                  </Card>
                </Col>
              </Row>

              <Row>
                <Col md={6}>
                  <h4>Reviews</h4>
                  {product.reviews.length === 0 && <Message variant='info'>No Reviews</Message>}

                  <ListGroup variant='flush'>
                    {product.reviews.map((review) => (
                      <ListGroup.Item key={review._id}>
                        <strong>{review.name}</strong>
                        <Rating value={review.rating} color='#f8e825' />
                        <p>{review.created_at.substring(0, 10)}</p>
                        <p>{review.comment}</p>
                      </ListGroup.Item>
                    ))}

                    <ListGroup.Item>
                      <h4>Write a review</h4>

                      {loadingProductReview && <Loader />}
                      {successProductReview && <Message variant='success'>Review Submitted</Message>}
                      {errorProductReview && <Message variant='danger'>{errorProductReview}</Message>}

                      {userInfo ? (
                        <Form onSubmit={submitHandler}>
                          <Form.Group controlId='rating'>
                            <Form.Label>Rating</Form.Label>
                            <Form.Control
                              as='select'
                              value={rating}
                              onChange={(e) => setRating(e.target.value)}
                            >
                              <option value=''>Select...</option>
                              <option value='1'>1 - Poor</option>
                              <option value='2'>2 - Fair</option>
                              <option value='3'>3 - Good</option>
                              <option value='4'>4 - Very Good</option>
                              <option value='5'>5 - Excellent</option>
                            </Form.Control>
                          </Form.Group>

                          <Form.Group controlId='comment'>
                            <Form.Label>Review</Form.Label>
                            <Form.Control
                              as='textarea'
                              row='5'
                              value={comment}
                              onChange={(e) => setComment(e.target.value)}
                            ></Form.Control>
                          </Form.Group>

                          <Button
                            disabled={loadingProductReview}
                            type='submit'
                            variant='primary'
                          >
                            Submit
                          </Button>

                        </Form>
                      ) : (
                        <Message variant='info'>Please <Link to='/login'>login</Link> to write a review</Message>
                      )}
                    </ListGroup.Item>
                  </ListGroup>
                </Col>
              </Row>
            </div>
          )
      }
    </div >
  )
}

export default ProductDetail
--#

--% isi_userlist_screen
import React, { useEffect, useState } from 'react'
import { LinkContainer } from 'react-router-bootstrap'
import { Alert, Table, Button } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'

import Loader from '../../components/Loader'
import Message from '../../components/Message'
import MyAlert from '../../components/MyAlert'

import { userList as listUsers, userDelete as deleteUser } from '../../store/user/userActions'
import { USER_DELETE_RESET } from '../../store/user/userConstants'

// const MyAlert = ({body, hapus}) => (<Alert variant="danger" onClose={hapus} dismissible>
//   <Alert.Heading>Oh snap! You got an error!</Alert.Heading>
//   <p>
//     {body}
//   </p>
// </Alert>)

function UserList({ history }) {

  const dispatch = useDispatch()

  const userList = useSelector(state => state.userList)
  const { loading, error, users } = userList

  const { loading: muat, error: gagal, success } = useSelector(state => state.userDelete)
  const [showDeleteError, setShowDeleteError] = useState(true)

  const userLogin = useSelector(state => state.userLogin)
  const { userInfo } = userLogin

  const userDelete = useSelector(state => state.userDelete)
  const { success: successDelete } = userDelete

  useEffect(() => {
    if (userInfo && userInfo.isAdmin) {
      dispatch(listUsers())
    } else {
      history.push('/login')
    }
    if (gagal) {
      setShowDeleteError(true)
    }
  }, [dispatch, history, successDelete, userInfo, gagal])

  const deleteHandler = (id) => {
    if (window.confirm('Are you sure you want to delete this user?')) {
      dispatch(deleteUser(id))
    }
  }

  return (
    <div>
      <h1>Users</h1>
      {gagal && showDeleteError ? <MyAlert body={gagal} hapus={()=>{
        setShowDeleteError(false)
        dispatch({type:USER_DELETE_RESET})
      }}/> : null}
      {loading
        ? (<Loader />)
        : error
          ? (<Message variant='danger'>{error}</Message>)
          : (
            <Table striped bordered hover responsive className='table-sm'>
              <thead>
                <tr>
                  <th>ID</th>
                  <th>NAME</th>
                  <th>EMAIL</th>
                  <th>ADMIN</th>
                  <th></th>
                </tr>
              </thead>

              <tbody>
                {users.map(user => (
                  <tr key={user._id}>
                    <td>{user._id}</td>
                    <td>{user.name}</td>
                    <td>{user.email}</td>
                    <td>{user.isAdmin ? (
                      <i className='fas fa-check' style={{ color: 'green' }}></i>
                    ) : (
                      <i className='fas fa-check' style={{ color: 'red' }}></i>
                    )}</td>

                    <td>
                      <LinkContainer to={`/admin/user/${user._id}/edit`}>
                        <Button variant='light' className='btn-sm'>
                          <i className='fas fa-edit'></i>
                        </Button>
                      </LinkContainer>

                      <Button variant='danger' className='btn-sm' onClick={() => deleteHandler(user._id)}>
                        <i className='fas fa-trash'></i>
                      </Button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </Table>
          )}
    </div>
  )
}

export default UserList
--#


--% isi_shipping_screen
import React, { useState } from 'react'
import { Form, Button } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'

import FormContainer from '../../components/FormContainer'
import CheckoutSteps from '../../components/CheckoutSteps'

import { saveShippingAddress } from '../../store/cart/cartActions'

function ShippingScreen({ history }) {

  const cart = useSelector(state => state.cart)
  const { shippingAddress } = cart

  const dispatch = useDispatch()

  const [address, setAddress] = useState(shippingAddress.address)
  const [city, setCity] = useState(shippingAddress.city)
  const [postalCode, setPostalCode] = useState(shippingAddress.postalCode)
  const [country, setCountry] = useState(shippingAddress.country)

  const submitHandler = (e) => {
    e.preventDefault()
    dispatch(saveShippingAddress({ address, city, postalCode, country }))
    history.push('/payment')
  }

  return (
    <FormContainer>
      <CheckoutSteps step1 step2 />
      <h1>Shipping</h1>
      <Form onSubmit={submitHandler}>

        <Form.Group controlId='address'>
          <Form.Label>Address</Form.Label>
          <Form.Control
            required
            type='text'
            placeholder='Enter address'
            value={address ? address : ''}
            onChange={(e) => setAddress(e.target.value)}
          >
          </Form.Control>
        </Form.Group>

        <Form.Group controlId='city'>
          <Form.Label>City</Form.Label>
          <Form.Control
            required
            type='text'
            placeholder='Enter city'
            value={city ? city : ''}
            onChange={(e) => setCity(e.target.value)}
          >
          </Form.Control>
        </Form.Group>

        <Form.Group controlId='postalCode'>
          <Form.Label>Postal Code</Form.Label>
          <Form.Control
            required
            type='text'
            placeholder='Enter postal code'
            value={postalCode ? postalCode : ''}
            onChange={(e) => setPostalCode(e.target.value)}
          >
          </Form.Control>
        </Form.Group>

        <Form.Group controlId='country'>
          <Form.Label>Country</Form.Label>
          <Form.Control
            required
            type='text'
            placeholder='Enter country'
            value={country ? country : ''}
            onChange={(e) => setCountry(e.target.value)}
          >
          </Form.Control>
        </Form.Group>

        <Button type='submit' variant='primary'>
          Continue
        </Button>
      </Form>
    </FormContainer>
  )
}

export default ShippingScreen
--#
