--% index/fmus
proshop_routes,d(/mk)
	%__TEMPLATE_CLIENT_PORT=__NILAI_CLIENT_PORT__
	package.json,f(e=__FILE__=package.json)	
	.env,f(n=CHOKIDAR_USEPOLLING=true)
	$*ln -s /mnt/c/node_modules/proshop_django/node_modules .
	public,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_routes/public.mk=index/fmus*)
	src,d(/mk)
		bootstrap.min.css,f(e=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_routes/bootstrap.mk=index/fmus)
		App.js,f(e=__FILE__=App.js)
		index.js,f(e=__FILE__=index.js)
		index.css,f(e=__FILE__=index.css)
		README.md,f(e=__FILE__=README.md)
		components,d(/mk)
			CheckoutSteps.js,f(e=__FILE__=CheckoutSteps.js)
			Footer.js,f(e=__FILE__=Footer.js)
			FormContainer.js,f(e=__FILE__=FormContainer.js)
			Header.js,f(e=__FILE__=Header.js)
			Loader.js,f(e=__FILE__=Loader.js)
			Message.js,f(e=__FILE__=Message.js)
			MyAlert.js,f(e=__FILE__=MyAlert.js)
			Paginate.js,f(e=__FILE__=Paginate.js)
			Rating.js,f(e=__FILE__=Rating.js)
			SearchBox.js,f(e=__FILE__=SearchBox.js)
		pages,d(/mk)
			Dashboard.js,f(e=__FILE__=Dashboard.js)
			LoginScreen.js,f(e=__FILE__=LoginScreen.js)
			ProfileScreen.js,f(e=__FILE__=ProfileScreen.js)
			RegisterScreen.js,f(e=__FILE__=RegisterScreen.js)
			PlaceOrderScreen.js,f(e=__FILE__=PlaceOrderScreen.js)
			PaymentScreen.js,f(e=__FILE__=PaymentScreen.js)
		apps,d(/mk)
__TEMPLATE_APP_CONTENT
		apps,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_routes/extras.mk=index/fmus*)
--#

--% CheckoutSteps.js
import React from 'react'
import { Nav } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'

function CheckoutSteps({ step1, step2, step3, step4 }) {
  return (
    <Nav className='justify-content-center mb-4'>
      <Nav.Item>
        {step1 ? (
          <LinkContainer to='/login'>
            <Nav.Link>Login</Nav.Link>
          </LinkContainer>
        ) : (
          <Nav.Link disabled>Login</Nav.Link>
        )}
      </Nav.Item>

      <Nav.Item>
        {step2 ? (
          <LinkContainer to='/shipping'>
            <Nav.Link>Shipping</Nav.Link>
          </LinkContainer>
        ) : (
          <Nav.Link disabled>Shipping</Nav.Link>
        )}
      </Nav.Item>

      <Nav.Item>
        {step3 ? (
          <LinkContainer to='/payment'>
            <Nav.Link>Payment</Nav.Link>
          </LinkContainer>
        ) : (
          <Nav.Link disabled>Payment</Nav.Link>
        )}
      </Nav.Item>

      <Nav.Item>
        {step4 ? (
          <LinkContainer to='/placeorder'>
            <Nav.Link>Place Order</Nav.Link>
          </LinkContainer>
        ) : (
          <Nav.Link disabled>Place Order</Nav.Link>
        )}
      </Nav.Item>
    </Nav>
  )
}

export default CheckoutSteps
--#

--% FormContainer.js
import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'

function FormContainer({ children }) {
  return (
    <Container>
      <Row className="justify-content-md-center">
        <Col xs={12} md={6}>
          {children}
        </Col>
      </Row>
    </Container>
  )
}

export default FormContainer
--#

--% MyAlert.js
import { Alert } from 'react-bootstrap'

const MyAlert = ({body, hapus}) => (<Alert variant="danger" onClose={hapus} dismissible>
  <Alert.Heading>Oh snap! You got an error!</Alert.Heading>
  <p>
    {body}
  </p>
</Alert>)

export default MyAlert
--#

--% Dashboard.js
import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Row, Col } from 'react-bootstrap'

import Loader from '../components/Loader'
import Message from '../components/Message'
import Paginate from '../components/Paginate'

import ProductItem from '../apps/product/item'
import { productList as listProducts } from '../store/product/productActions'

function Dashboard({ history }) {
	const dispatch = useDispatch()
	const productList = useSelector(state => state.productList)
	const { error, loading, products, page, pages } = productList

	let keyword = history.location.search

	useEffect(() => {
		dispatch(listProducts(keyword))
	}, [dispatch, keyword])

	return (
		<div>

			<h1>Latest Products</h1>

			{loading ? <Loader />
				: error ? <Message variant='danger'>{error}</Message>
					:
					<div>
						<Row>
							{products
								? products.map(product => (
									<Col key={product._id} sm={12} md={6} lg={4} xl={3}>
										<ProductItem product={product} />
									</Col>
								))
								: null}
						</Row>
						<Paginate page={page} pages={pages} keyword={keyword} />
					</div>
			}

		</div>
	)
}
export default Dashboard
--#

--% index.css
main{
	min-height: 80vh;
}

h1{
	font-size: 1.8rem;
	padding:1rem 0;
}

h2{
	font-size: 1.4rem;
	padding:0.5rem 0;
}

h3{
	padding:1rem 0;
}

.rating span{
	margin:0.1rem;
}

/* carousel */
.carousel-item-next,
.carousel-item-prev,
.carousel-item.active {
	display: flex;
}
.carousel-caption {
	position: absolute;
	top: 0;
}

.carousel-caption h4 {
	color: #fff;
}

.carousel img {
	display:block;
	height: 300px;
	padding: 30px;
	margin: 40px;
	border-radius: 50%;
	margin-left: auto;
	margin-right: auto;
}
.carousel a {
	margin: 0 auto;
}
@media (max-width: 900px) {
	.carousel-caption h2 {
		font-size: 2.5vw;
	}
}
--#

--% index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';

import store from './store';
import './index.css';
import './bootstrap.min.css'
import App from './App';

ReactDOM.render(
	<Provider store={store}>
		<App />
	</Provider>,
	document.getElementById('root')
);
--#

--% SearchBox.js
import React, { useState } from 'react'
import { Button, Form } from 'react-bootstrap'
import { useHistory } from 'react-router-dom'

function SearchBox() {
	const [keyword, setKeyword] = useState('')

	let history = useHistory()

	const submitHandler = (e) => {
		e.preventDefault()
		if (keyword) {
			history.push(`/?keyword=${keyword}&page=1`)
		} else {
			history.push(history.push(history.location.pathname))
		}
	}
	return (
		<Form onSubmit={submitHandler} inline>
			<Form.Control
				type='text'
				name='q'
				onChange={(e) => setKeyword(e.target.value)}
				className='mr-sm-2 ml-sm-5'
			></Form.Control>

			<Button
				type='submit'
				variant='outline-success'
				className='p-2'
			>
				Submit
			</Button>
		</Form>
	)
}

export default SearchBox
--#

--% Footer.js
import React from 'react'
import { Container, Row, Col } from 'react-bootstrap'

function Footer() {
	return (
		<footer>
			<Container>
				<Row>
					<Col className="text-center py-3">Copyright &copy; ProShop</Col>
				</Row>
			</Container>
		</footer>
	)
}

export default Footer
--#

--% Header.js
import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Navbar, Nav, Container, NavDropdown } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'
import SearchBox from './SearchBox'
import { logout } from '../store/user/userActions'

function Header() {

	const userLogin = useSelector(state => state.userLogin)
	const { userInfo } = userLogin

	const dispatch = useDispatch()

	const logoutHandler = () => {
		dispatch(logout())
	}
	/**
	 * 
	 {
		"id": 4,
		"bio": "",
		"image": "",
		"token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ1NTQ0NzE3LCJqdGkiOiIyOTc3OWRkMWE3NWI0NmM0OTc3ZmY0MDk0MTRjYjBkNyIsInVzZXJfaWQiOjR9.lBj08__tVVUZPlhUN2R3yLTmd-6QWWh_uD5cSTpJhxQ",
		"last_login": null,
		"is_superuser": false,
		"created_at": "2022-01-23T15:45:17.171296Z",
		"updated_at": "2022-01-23T15:45:17.171323Z",
		"username": "sample-email@gmail.com",
		"first_name": "wieke",
		"last_name": null,
		"email": "sample-email@gmail.com",
		"phone": "",
		"is_active": true,
		"is_staff": false,
		"roles": "user",
		"groups": [],
		"user_permissions": []
	}          
	*/

	return (
		<header>
			<Navbar bg="dark" variant="dark" expand="lg" collapseOnSelect>
				<Container>
					<LinkContainer to='/'>
						<Navbar.Brand>ProShop</Navbar.Brand>
					</LinkContainer>

					<Navbar.Toggle aria-controls="basic-navbar-nav" />

					<Navbar.Collapse id="basic-navbar-nav">
						<SearchBox />
						<Nav className="ml-auto">

							<LinkContainer to='/cart'>
								<Nav.Link ><i className="fas fa-shopping-cart"></i>Cart</Nav.Link>
							</LinkContainer>

							{userInfo ? (
								<NavDropdown title={userInfo.username + ` | ` + userInfo.email} id='username'>
									<LinkContainer to='/profile'>
										<NavDropdown.Item>Profile</NavDropdown.Item>
									</LinkContainer>

									<NavDropdown.Item onClick={logoutHandler}>Logout</NavDropdown.Item>

								</NavDropdown>
							) : (
								<LinkContainer to='/login'>
									<Nav.Link><i className="fas fa-user"></i>Login</Nav.Link>
								</LinkContainer>
							)}

							{userInfo && userInfo.isAdmin && (
								<NavDropdown title='Admin' id='adminmenue'>

									<LinkContainer to='/admin/userlist'>
										<NavDropdown.Item>Users</NavDropdown.Item>
									</LinkContainer>

									<LinkContainer to='/admin/productlist'>
										<NavDropdown.Item>Products</NavDropdown.Item>
									</LinkContainer>

									<LinkContainer to='/admin/orderlist'>
										<NavDropdown.Item>Orders</NavDropdown.Item>
									</LinkContainer>

								</NavDropdown>
							)}

						</Nav>
					</Navbar.Collapse>
				</Container>
			</Navbar>
		</header>
	)
}

export default Header
--#

--% README.md
Generated by: 
WM -e'***upsr,*/B^{@Product}name,s;price,n^'
--#

--% App.js
import { Container } from 'react-bootstrap'
import { HashRouter as Router, Route } from 'react-router-dom'

import Dashboard from './pages/Dashboard'
import Footer from './components/Footer'
import Header from './components/Header'
import LoginScreen from './pages/LoginScreen'
import RegisterScreen from './pages/RegisterScreen'
import ProfileScreen from './pages/ProfileScreen'
import PaymentScreen from './pages/PaymentScreen'
import PlaceOrderScreen from './pages/PlaceOrderScreen'

__TEMPLATE_APP_IMPORTS

function App() {
	return (
		<Router>
			<Header />
			<main className="py-3">
				<Container>
					<Route path='/' component={Dashboard} exact />
					<Route path='/login' component={LoginScreen} />
					<Route path='/register' component={RegisterScreen} />
					<Route path='/profile' component={ProfileScreen} />
					<Route path='/payment' component={PaymentScreen} />
					<Route path='/placeorder' component={PlaceOrderScreen} />

__TEMPLATE_APP_ROUTES
				</Container>
			</main>
			<Footer />
		</Router>
	);
}

export default App;
--#

--% Loader.js
import React from 'react'
import { Spinner } from 'react-bootstrap'

function Loader() {
	return (
		<Spinner
			animation='border'
			role='status'
			style={{
				height: '100px',
				width: '100px',
				margin: 'auto',
				display: 'block'
			}}
		>
			<span className='sr-only'>Loading...</span>
		</Spinner>
	)
}

export default Loader
--#

--% Message.js
import React from 'react'
import { Alert } from 'react-bootstrap'

function Message({ variant, children }) {
	return (
		<Alert variant={variant}>
			{children}
		</Alert>
	)
}

export default Message
--#

--% Paginate.js
import React from 'react'
import { Pagination } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'
import { Link } from "react-router-dom";
import { Navbar, Nav, Form, FormControl, Button, NavItem } from 'react-bootstrap';

// https://stackoverflow.com/questions/70090030/is-there-a-solution-for-linkcontainer-component-from-react-router-bootstrap-erro
// Instead of using a LinkContainer component from react-router-bootstrap, I just used the as property inside the <Nav.Link> and set its value as the Link component of react-router-dom:
{/* <Nav.Link as={Link} to="/path">children</Nav.Link> */}

function Paginate({ pages, page, keyword = '', isAdmin = false }) {
	if (keyword) {
		keyword = keyword.split('?keyword=')[1].split('&')[0]
	}

	return (pages > 1 && (
		<Pagination>
			{[...Array(pages).keys()].map((x) => {
				let goto = `/?keyword=${keyword}&page=${x + 1}`
				let item_link = !isAdmin ? goto : `/admin/productlist${goto}`
				return (
					<LinkContainer
						key={x + 1}
						to={item_link}
					>
						<Pagination.Item active={x + 1 === page}>{x + 1}</Pagination.Item>
					</LinkContainer>
				)

				// return (<Nav.Link 
				//   as={Link}
				//   key={x + 1}
				//   to={item_link}>
				//   <Pagination.Item active={x + 1 === page}>{x + 1}-{item_link}</Pagination.Item>
				// </Nav.Link>)
			}
			) // map
			}
			<h4>{page}/{pages} [admin = {isAdmin}]</h4>
		</Pagination>
	)
	)
}

export default Paginate
--#

--% Rating.js
import React from 'react'

function Rating({ value, text, color }) {
	return (
		<div className="rating">
			<span>
				<i style={{ color }} className={
					value >= 1
						? 'fas fa-star'
						: value >= 0.5
							? 'fas fa-star-half-alt'
							: 'far fa-star'
				}>

				</i>
			</span>

			<span>
				<i style={{ color }} className={
					value >= 2
						? 'fas fa-star'
						: value >= 1.5
							? 'fas fa-star-half-alt'
							: 'far fa-star'
				}>

				</i>
			</span>

			<span>
				<i style={{ color }} className={
					value >= 3
						? 'fas fa-star'
						: value >= 2.5
							? 'fas fa-star-half-alt'
							: 'far fa-star'
				}>

				</i>
			</span>

			<span>
				<i style={{ color }} className={
					value >= 4
						? 'fas fa-star'
						: value >= 3.5
							? 'fas fa-star-half-alt'
							: 'far fa-star'
				}>

				</i>
			</span>

			<span>
				<i style={{ color }} className={
					value >= 5
						? 'fas fa-star'
						: value >= 4.5
							? 'fas fa-star-half-alt'
							: 'far fa-star'
				}>

				</i>
			</span>

			<span>{text && text}</span>
		</div>
	)
}

export default Rating
--#

--% package.json
{
	"name": "auto-frontend",
	"proxy": "http://127.0.0.1:8000",
	"version": "0.1.0",
	"private": true,
	"dependencies": {
		"@testing-library/jest-dom": "^5.11.6",
		"@testing-library/react": "^11.2.2",
		"@testing-library/user-event": "^12.6.0",
		"axios": "^0.21.1",
		"react": "^17.0.1",
		"react-bootstrap": "^1.4.0",
		"react-dom": "^17.0.1",
		"react-paypal-button-v2": "^2.6.2",
		"react-redux": "^7.2.2",
		"react-router-bootstrap": "^0.25.0",
		"react-router-dom": "^5.2.0",
		"react-scripts": "4.0.1",
		"redux": "^4.0.5",
		"redux-devtools-extension": "^2.13.8",
		"redux-thunk": "^2.3.0",
		"web-vitals": "^0.2.4"
	},
	"scripts": {
		"start": "PORT=__TEMPLATE_CLIENT_PORT react-scripts start",
		"build": "react-scripts build",
		"test": "react-scripts test",
		"eject": "react-scripts eject"
	},
	"eslintConfig": {
		"extends": [
			"react-app",
			"react-app/jest"
		]
	},
	"browserslist": {
		"production": [
			">0.2%",
			"not dead",
			"not op_mini all"
		],
		"development": [
			"last 1 chrome version",
			"last 1 firefox version",
			"last 1 safari version"
		]
	}
}
--#

--% LoginScreen.js
import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Form, Button, Row, Col } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Loader from '../components/Loader'
import Message from '../components/Message'
import FormContainer from '../components/FormContainer'

import { login } from '../store/user/userActions'

function LoginScreen({ location, history }) {
	const [email, setEmail] = useState('')
	const [password, setPassword] = useState('')

	const dispatch = useDispatch()

	const redirect = location.search ? location.search.split('=')[1] : '/'

	const userLogin = useSelector(state => state.userLogin)
	const { error, loading, userInfo } = userLogin

	useEffect(() => {
		if (userInfo) {
			history.push(redirect)
		}
	}, [history, userInfo, redirect])

	const submitHandler = (e) => {
		e.preventDefault()
		dispatch(login(email, password))
	}

	return (
		<FormContainer>
			<h1>Sign In</h1>
			{error && <Message variant='danger'>{error}</Message>}
			{loading && <Loader />}
			<Form onSubmit={submitHandler}>

				<Form.Group controlId='email'>
					<Form.Label>Email Address</Form.Label>
					<Form.Control
						type='email'
						placeholder='Enter Email'
						value={email}
						onChange={(e) => setEmail(e.target.value)}
					>
					</Form.Control>
				</Form.Group>


				<Form.Group controlId='password'>
					<Form.Label>Password</Form.Label>
					<Form.Control
						type='password'
						placeholder='Enter Password'
						value={password}
						onChange={(e) => setPassword(e.target.value)}
					>
					</Form.Control>
				</Form.Group>

				<Button type='submit' variant='primary'>
					Sign In
				</Button>
			</Form>

			<Row className='py-3'>
				<Col>
					New Customer? <Link
						to={redirect ? `/register?redirect=${redirect}` : '/register'}>
						Register
					</Link>
				</Col>
			</Row>

		</FormContainer>
	)
}

export default LoginScreen
--#

--% ProfileScreen.js
import React, { useState, useEffect } from 'react'
import { Form, Button, Row, Col, Table } from 'react-bootstrap'
import { LinkContainer } from 'react-router-bootstrap'
import { useDispatch, useSelector } from 'react-redux'

import Loader from '../components/Loader'
import Message from '../components/Message'

import { userDetail as detailUser, updateUserProfile } from '../store/user/userActions'
import { USER_UPDATE_PROFILE_RESET } from '../store/user/userConstants'
import { listMyOrders } from '../store/order/orderActions'

function ProfileScreen({ history }) {

	const [name, setName] = useState('')
	const [email, setEmail] = useState('')
	const [password, setPassword] = useState('')
	const [confirmPassword, setConfirmPassword] = useState('')
	const [message, setMessage] = useState('')

	const dispatch = useDispatch()

	const userDetails = useSelector(state => state.userDetail)
	const { error, loading, user } = userDetails

	const userLogin = useSelector(state => state.userLogin)
	const { userInfo } = userLogin

	const userUpdateProfile = useSelector(state => state.userUpdateProfile)
	const { success } = userUpdateProfile

	const orderListMy = useSelector(state => state.orderListMy)
	const { loading: loadingOrders, error: errorOrders, orders } = orderListMy


	useEffect(() => {
		if (!userInfo) {
			history.push('/login')
		} else {

			/**
			 * 
				!user false
				!user.name true <- django_pg gak kasih name why?
				!success true <- butuh dari pemanggil dispatch updateUserProfile, yg hanya ada di profilescreen = submithandler
			 */
			if (!user || !user.name || success || userInfo._id !== user._id) {
			// if (!user || !user.name || success) {
				dispatch({ type: USER_UPDATE_PROFILE_RESET })
				dispatch(detailUser('profile'))
				dispatch(listMyOrders())
			} else {
				setName(user.name)
				setEmail(user.email)
			}
		}
	}, [dispatch, history, userInfo, user, success])

	const submitHandler = (e) => {
		e.preventDefault()

		if (password !== confirmPassword) {
			setMessage('Passwords do not match')
		} else {
			dispatch(updateUserProfile({
				'id': user._id,
				'name': name,
				'email': email,
				'password': password
			}))
			setMessage('')
		}

	}
	return (
		<Row>
			<Col md={3}>
				<h2>User Profile</h2>

				{message && <Message variant='danger'>{message}</Message>}
				{error && <Message variant='danger'>{error}</Message>}
				{loading && <Loader />}
				<Form onSubmit={submitHandler}>

					<Form.Group controlId='name'>
						<Form.Label>Name</Form.Label>
						<Form.Control
							required
							type='name'
							placeholder='Enter name'
							value={name}
							onChange={(e) => setName(e.target.value)}
						>
						</Form.Control>
					</Form.Group>

					<Form.Group controlId='email'>
						<Form.Label>Email Address</Form.Label>
						<Form.Control
							required
							type='email'
							placeholder='Enter Email'
							value={email}
							onChange={(e) => setEmail(e.target.value)}
						>
						</Form.Control>
					</Form.Group>

					<Form.Group controlId='password'>
						<Form.Label>Password</Form.Label>
						<Form.Control

							type='password'
							placeholder='Enter Password'
							value={password}
							onChange={(e) => setPassword(e.target.value)}
						>
						</Form.Control>
					</Form.Group>

					<Form.Group controlId='passwordConfirm'>
						<Form.Label>Confirm Password</Form.Label>
						<Form.Control

							type='password'
							placeholder='Confirm Password'
							value={confirmPassword}
							onChange={(e) => setConfirmPassword(e.target.value)}
						>
						</Form.Control>
					</Form.Group>

					<Button type='submit' variant='primary'>
						Update
					</Button>

				</Form>
			</Col>

			<Col md={9}>
				<h2>My Orders</h2>
				{loadingOrders ? (
					<Loader />
				) : errorOrders ? (
					<Message variant='danger'>{errorOrders}</Message>
				) : (
					<Table striped responsive className='table-sm'>
						<thead>
							<tr>
								<th>ID</th>
								<th>Date</th>
								<th>Total</th>
								<th>Paid</th>
								<th>Delivered</th>
								<th></th>
							</tr>
						</thead>

						<tbody>
							{orders.map(order => (
								<tr key={order._id}>
									<td>{order._id}</td>
									{/* <td>{order.createdAt.substring(0, 10)}</td> */}
									<td>{order.created_at.substring(0, 10)}</td>
									<td>${order.totalPrice}</td>
									<td>{order.isPaid ? order.paidAt.substring(0, 10) : (
										<i className='fas fa-times' style={{ color: 'red' }}></i>
									)}</td>
									<td>
										<LinkContainer to={`/order/${order._id}`}>
											<Button className='btn-sm'>Details</Button>
										</LinkContainer>
									</td>
								</tr>
							))}
						</tbody>
					</Table>
				)}
			</Col>
		</Row>
	)
}

export default ProfileScreen
--#

--% RegisterScreen.js
import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Form, Button, Row, Col } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'
import Loader from '../components/Loader'
import Message from '../components/Message'
import FormContainer from '../components/FormContainer'

import { userCreate as register } from '../store/user/userActions'

function RegisterScreen({ location, history }) {

	const [name, setName] = useState('')
	const [email, setEmail] = useState('')
	const [password, setPassword] = useState('')
	const [confirmPassword, setConfirmPassword] = useState('')
	const [message, setMessage] = useState('')

	const dispatch = useDispatch()

	const redirect = location.search ? location.search.split('=')[1] : '/'

	const userRegister = useSelector(state => state.userRegister)
	const { error, loading, userInfo } = userRegister

	useEffect(() => {
		if (userInfo) {
			history.push(redirect)
		}
	}, [history, userInfo, redirect])

	const submitHandler = (e) => {
		e.preventDefault()

		if (password !== confirmPassword) {
			setMessage('Passwords do not match')
		} else {
			dispatch(register(name, email, password))
		}
	}

	return (
		<FormContainer>
			<h1>Sign In</h1>
			{message && <Message variant='danger'>{message}</Message>}
			{error && <Message variant='danger'>{error}</Message>}
			{loading && <Loader />}
			<Form onSubmit={submitHandler}>

				<Form.Group controlId='name'>
					<Form.Label>Name</Form.Label>
					<Form.Control
						required
						type='name'
						placeholder='Enter name'
						value={name}
						onChange={(e) => setName(e.target.value)}
					>
					</Form.Control>
				</Form.Group>

				<Form.Group controlId='email'>
					<Form.Label>Email Address</Form.Label>
					<Form.Control
						required
						type='email'
						placeholder='Enter Email'
						value={email}
						onChange={(e) => setEmail(e.target.value)}
					>
					</Form.Control>
				</Form.Group>

				<Form.Group controlId='password'>
					<Form.Label>Password</Form.Label>
					<Form.Control
						required
						type='password'
						placeholder='Enter Password'
						value={password}
						onChange={(e) => setPassword(e.target.value)}
					>
					</Form.Control>
				</Form.Group>

				<Form.Group controlId='passwordConfirm'>
					<Form.Label>Confirm Password</Form.Label>
					<Form.Control
						required
						type='password'
						placeholder='Confirm Password'
						value={confirmPassword}
						onChange={(e) => setConfirmPassword(e.target.value)}
					>
					</Form.Control>
				</Form.Group>

				<Button type='submit' variant='primary'>
					Register
				</Button>

			</Form>

			<Row className='py-3'>
				<Col>
					Have an Account? <Link
						to={redirect ? `/login?redirect=${redirect}` : '/login'}>
						Sign In
					</Link>
				</Col>
			</Row>
		</FormContainer >
	)
}

export default RegisterScreen
--#

--% PlaceOrderScreen.js
import React, { useEffect } from 'react'
import { Button, Row, Col, ListGroup, Image, Card } from 'react-bootstrap'
import { Link } from 'react-router-dom'
import { useDispatch, useSelector } from 'react-redux'

import Message from '../components/Message'
import CheckoutSteps from '../components/CheckoutSteps'

import { orderCreate as createOrder } from '../store/order/orderActions'
import { ORDER_CREATE_RESET } from '../store/order/orderConstants'
import { USER_DETAIL_RESET } from '../store/user/userConstants'
import config from '../store/config'

function PlaceOrderScreen({ history }) {

	const orderCreate = useSelector(state => state.orderCreate)
	const { order, error, success } = orderCreate

	const dispatch = useDispatch()

	const cart = useSelector(state => state.cart)

	cart.itemsPrice = cart.cartItems.reduce((acc, item) => acc + item.price * item.qty, 0).toFixed(2)
	cart.shippingPrice = (cart.itemsPrice > 100 ? 0 : 10).toFixed(2)
	cart.taxPrice = Number((0.082) * cart.itemsPrice).toFixed(2)

	cart.totalPrice = (Number(cart.itemsPrice) + Number(cart.shippingPrice) + Number(cart.taxPrice)).toFixed(2)


	if (!cart.paymentMethod) {
		history.push('/payment')
	}

	useEffect(() => {
		console.log(`PlaceOrderScreen, orderCreate dari state/reducer adlh:
			${JSON.stringify(orderCreate, null, 2)}
		`)
		if (success) {
			history.push(`/order/${order._id}`)
			dispatch({ type: USER_DETAIL_RESET })
			dispatch({ type: ORDER_CREATE_RESET })
		}
	}, [success, history, dispatch, order._id])

	const placeOrder = () => {
		let belanjaan = {
			orderItems: cart.cartItems,
			shippingAddress: cart.shippingAddress,
			paymentMethod: cart.paymentMethod,
			itemsPrice: cart.itemsPrice,
			shippingPrice: cart.shippingPrice,
			taxPrice: cart.taxPrice,
			totalPrice: cart.totalPrice,
		}
		console.log(`belanjaan adlh: ${JSON.stringify(belanjaan)}`);
		dispatch(createOrder(belanjaan))
	}

	return (
		<div>
			<CheckoutSteps step1 step2 step3 step4 />
			<Row>
				<Col md={8}>
					<ListGroup variant='flush'>
						<ListGroup.Item>
							<h2>Shipping</h2>

							<p>
								<strong>Shipping: </strong>
								{cart.shippingAddress.address},  {cart.shippingAddress.city}
								{'  '}
								{cart.shippingAddress.postalCode},
								{'  '}
								{cart.shippingAddress.country}
							</p>
						</ListGroup.Item>

						<ListGroup.Item>
							<h2>Payment Method</h2>
							<p>
								<strong>Method: </strong>
								{cart.paymentMethod}
							</p>
						</ListGroup.Item>

						<ListGroup.Item>
							<h2>Order Items</h2>
							{cart.cartItems.length === 0 ? <Message variant='info'>
								Your cart is empty
							</Message> : (
								<ListGroup variant='flush'>
									{cart.cartItems.map((item, index) => (
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
									<Col>${cart.itemsPrice}</Col>
								</Row>
							</ListGroup.Item>

							<ListGroup.Item>
								<Row>
									<Col>Shipping:</Col>
									<Col>${cart.shippingPrice}</Col>
								</Row>
							</ListGroup.Item>

							<ListGroup.Item>
								<Row>
									<Col>Tax:</Col>
									<Col>${cart.taxPrice}</Col>
								</Row>
							</ListGroup.Item>

							<ListGroup.Item>
								<Row>
									<Col>Total:</Col>
									<Col>${cart.totalPrice}</Col>
								</Row>
							</ListGroup.Item>


							<ListGroup.Item>
								{error && <Message variant='danger'>{error}</Message>}
							</ListGroup.Item>

							<ListGroup.Item>
								<Button
									type='button'
									className='btn-block'
									disabled={cart.cartItems === 0}
									onClick={placeOrder}
								>
									Place Order
								</Button>
							</ListGroup.Item>

						</ListGroup>
					</Card>
				</Col>
			</Row>
		</div>
	)
}

export default PlaceOrderScreen
--#

--% PaymentScreen.js
import React, { useState } from 'react'
import { Form, Button, Col } from 'react-bootstrap'
import { useDispatch, useSelector } from 'react-redux'

import FormContainer from '../components/FormContainer'
import CheckoutSteps from '../components/CheckoutSteps'

import { savePaymentMethod } from '../store/cart/cartActions'

function PaymentScreen({ history }) {

	const cart = useSelector(state => state.cart)
	const { shippingAddress } = cart

	const dispatch = useDispatch()

	const [paymentMethod, setPaymentMethod] = useState('PayPal')

	if (!shippingAddress.address) {
		history.push('/shipping')
	}

	const submitHandler = (e) => {
		e.preventDefault()
		dispatch(savePaymentMethod(paymentMethod))
		history.push('/placeorder')
	}

	return (
		<FormContainer>
			<CheckoutSteps step1 step2 step3 />

			<Form onSubmit={submitHandler}>
				<Form.Group>
					<Form.Label as='legend'>Select Method</Form.Label>
					<Col>
						<Form.Check
							type='radio'
							label='PayPal or Credit Card'
							id='paypal'
							name='paymentMethod'
							checked
							onChange={(e) => setPaymentMethod(e.target.value)}
						>

						</Form.Check>
					</Col>
				</Form.Group>

				<Button type='submit' variant='primary'>
					Continue
				</Button>
			</Form>
		</FormContainer>
	)
}

export default PaymentScreen
--#
