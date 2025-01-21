
--% index/fmus
relight,d(/mk)
	routes.js,f(e=__FILE__=routes.js)
	index.js,f(e=__FILE__=index.js)
	README.md,f(e=__FILE__=README.md)
	layouts,d(/mk)
		Admin.js,f(e=__FILE__=Admin.js)
		Admin.css,f(e=__FILE__=Admin.css)
	pages,d(/mk)
		Dashboard.js,f(e=__FILE__=Dashboard.js)
		Login.js,f(e=__FILE__=Login.js)
		Register.js,f(e=__FILE__=Register.js)
		ResetPassword.js,f(e=__FILE__=ResetPassword.js)
	components,d(/mk)
		common,d(/mk)
			Loader.js,f(e=__FILE__=Loader.js)
			Message.js,f(e=__FILE__=Message.js)
			Paginate.js,f(e=__FILE__=Paginate.js)
		sidebar,d(/mk)
			Sidebar.js,f(e=__FILE__=Sidebar.js)
			Sidebar.css,f(e=__FILE__=Sidebar.css)
			SubMenu.js,f(e=__FILE__=SubMenu.js)
			SidebarToggler.js,f(e=__FILE__=SidebarToggler.js)
			SidebarToggler.css,f(e=__FILE__=SidebarToggler.css)
	apps,d(/mk)
__TEMPLATE_APP_CONTENT
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
import { Link } from 'react-router-dom';
import { Navbar, Nav, Form, FormControl, Button, NavItem } from 'react-bootstrap';
// https://stackoverflow.com/questions/70090030/is-there-a-solution-for-linkcontainer-component-from-react-router-bootstrap-erro
// Instead of using a LinkContainer component from react-router-bootstrap, I just used the as property inside the <Nav.Link> and set its value as the Link component of react-router-dom:
{/* <Nav.Link as={Link} to='/path'>children</Nav.Link> */}

function Paginate({ pages, page, keyword = '', isAdmin = false }) {
  if (keyword) {
    keyword = keyword.split('?keyword=')[1].split('&')[0]
  }

  return (pages > 1 && (
    <Pagination>
      {[...Array(pages).keys()].map((x) => {
        let goto = `/?keyword=${keyword}&page=${x + 1}`

        return (
          <LinkContainer
            key={x + 1}
            to={!isAdmin ? goto : `/admin/productlist${goto}`}
          >
            <Pagination.Item active={x + 1 === page}>{x + 1}</Pagination.Item>
          </LinkContainer>          
        )

        // return (<Nav.Link 
        //   as={Link} 
        //   key={x + 1}
        //   to={!isAdmin ? goto : `/admin/productlist${goto}` }>
        //   <Pagination.Item active={x + 1 === page}>{x + 1}</Pagination.Item>
        // </Nav.Link>)

      } // inner
      ) // map
      } // outer
    </Pagination>
  )
  )
}

export default Paginate
--#

--% Login.js
import React, { useState, useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleLeft, faEnvelope, faUnlockAlt } from '@fortawesome/free-solid-svg-icons';
import { faFacebookF, faGithub, faTwitter } from '@fortawesome/free-brands-svg-icons';
import { Col, Row, Form, Card, Button, FormCheck, Container, InputGroup } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';

import BgImage from '../assets/img/illustrations/signin.svg';
import { login } from '../store/user/userActions'

export default ({ location, history }) => {

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
    <main>
      <section className='d-flex align-items-center my-5 mt-lg-6 mb-lg-5'>
        <Container>

          <p className='text-center'>
            <Card.Link as={Link} to={'/'} className='text-gray-700'>
              <FontAwesomeIcon icon={faAngleLeft} className='me-2' /> Back to homepage
            </Card.Link>
          </p>

          <Row className='justify-content-center form-bg-image' style={{ backgroundImage: `url(${BgImage})` }}>
            <Col xs={12} className='d-flex align-items-center justify-content-center'>
              <div className='bg-white shadow-soft border rounded border-light p-4 p-lg-5 w-100 fmxw-500'>

                <div className='text-center text-md-center mb-4 mt-md-0'>
                  <h3 className='mb-0'>Sign in to our platform</h3>
                </div>

                <Form className='mt-4'>
                  
                  <Form.Group id='email' className='mb-4'>
                    <Form.Label>Your Email</Form.Label>
                    <InputGroup>
                      <InputGroup.Text>
                        <FontAwesomeIcon icon={faEnvelope} />
                      </InputGroup.Text>
                      <Form.Control autoFocus required type='email' placeholder='example@company.com' 
                        onChange={(e) => setEmail(e.target.value)}
                        value={email}
                        />
                    </InputGroup>
                  </Form.Group>

                  <Form.Group>
                    <Form.Group id='password' className='mb-4'>
                      <Form.Label>Your Password</Form.Label>
                      <InputGroup>
                        <InputGroup.Text>
                          <FontAwesomeIcon icon={faUnlockAlt} />
                        </InputGroup.Text>
                        <Form.Control required type='password' placeholder='Password' 
                          onChange={(e) => setPassword(e.target.value)}
                          value={password}
                          />
                      </InputGroup>
                    </Form.Group>
                    <div className='d-flex justify-content-between align-items-center mb-4'>
                      <Form.Check type='checkbox'>
                        <FormCheck.Input id='defaultCheck5' className='me-2' />
                        <FormCheck.Label htmlFor='defaultCheck5' className='mb-0'>Remember me</FormCheck.Label>
                      </Form.Check>
                      <Card.Link className='small text-end'>Lost password?</Card.Link>
                    </div>
                  </Form.Group>
                  
                  <Button variant='primary' type='submit' className='w-100' onClick={submitHandler}>
                    Sign in
                  </Button>

                </Form>

                <div className='mt-3 mb-4 text-center'>
                  <span className='fw-normal'>or login with</span>
                </div>

                <div className='d-flex justify-content-center my-4'>
                  <Button variant='outline-light' className='btn-icon-only btn-pill text-facebook me-2'>
                    <FontAwesomeIcon icon={faFacebookF} />
                  </Button>

                  <Button variant='outline-light' className='btn-icon-only btn-pill text-twitter me-2'>
                    <FontAwesomeIcon icon={faTwitter} />
                  </Button>

                  <Button variant='outline-light' className='btn-icon-only btn-pil text-dark'>
                    <FontAwesomeIcon icon={faGithub} />
                  </Button>
                </div>

                <div className='d-flex justify-content-center align-items-center mt-4'>
                  <span className='fw-normal'>
                    Not registered?
                    <Card.Link as={Link} to={'/register'} className='fw-bold'>
                      {` Create account `}
                    </Card.Link>
                  </span>
                </div>

              </div>
            </Col>
          </Row>

        </Container>
      </section>
    </main>
  );
};
--#

--% Register.js
import React, { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleLeft, faEnvelope, faUnlockAlt } from '@fortawesome/free-solid-svg-icons';
import { faFacebookF, faGithub, faTwitter } from '@fortawesome/free-brands-svg-icons';
import { Col, Row, Form, Card, Button, FormCheck, Container, InputGroup } from 'react-bootstrap';
import { Link } from 'react-router-dom';

import BgImage from '../assets/img/illustrations/signin.svg';
import { userCreate as register } from '../store/user/userActions'

export default ({ location, history }) => {

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
    console.log(`register clicked`);
    if (password !== confirmPassword) {
      setMessage('Passwords do not match')
    } else {
      dispatch(register(name, email, password))
      console.log(`registering ${name}, ${email}, ${password}`);
    }
  }

  return (
    <main>
      <section className='d-flex align-items-center my-5 mt-lg-6 mb-lg-5'>
        <Container>

          <p className='text-center'>
            <Card.Link as={Link} to={'/'} className='text-gray-700'>
              <FontAwesomeIcon icon={faAngleLeft} className='me-2' /> Back to homepage
            </Card.Link>
          </p>

          <Row className='justify-content-center form-bg-image' style={{ backgroundImage: `url(${BgImage})` }}>
            <Col xs={12} className='d-flex align-items-center justify-content-center'>
              <div className='mb-4 mb-lg-0 bg-white shadow-soft border rounded border-light p-4 p-lg-5 w-100 fmxw-500'>
                
                <div className='text-center text-md-center mb-4 mt-md-0'>
                  <h3 className='mb-0'>Create an account</h3>
                </div>

                <Form className='mt-4'>
                  <Form.Group id='name' className='mb-4'>
                    <Form.Label>Your Name</Form.Label>
                    <InputGroup>
                      <InputGroup.Text>
                        <FontAwesomeIcon icon={faEnvelope} />
                      </InputGroup.Text>
                      <Form.Control autoFocus required type='name' placeholder='' 
                        onChange={(e) => setName(e.target.value)}
                        value={name}
                        />
                    </InputGroup>
                  </Form.Group>

                  <Form.Group id='email' className='mb-4'>
                    <Form.Label>Your Email</Form.Label>
                    <InputGroup>
                      <InputGroup.Text>
                        <FontAwesomeIcon icon={faEnvelope} />
                      </InputGroup.Text>
                      <Form.Control required type='email' placeholder='example@company.com' 
                        onChange={(e) => setEmail(e.target.value)}
                        value={email}
                        />
                    </InputGroup>
                  </Form.Group>

                  <Form.Group id='password' className='mb-4'>
                    <Form.Label>Your Password</Form.Label>
                    <InputGroup>
                      <InputGroup.Text>
                        <FontAwesomeIcon icon={faUnlockAlt} />
                      </InputGroup.Text>
                      <Form.Control required type='password' placeholder='Password' 
                        onChange={(e) => setPassword(e.target.value)}
                        value={password}
                        />
                    </InputGroup>
                  </Form.Group>

                  <Form.Group id='confirmPassword' className='mb-4'>
                    <Form.Label>Confirm Password</Form.Label>
                    <InputGroup>
                      <InputGroup.Text>
                        <FontAwesomeIcon icon={faUnlockAlt} />
                      </InputGroup.Text>
                      <Form.Control required type='password' placeholder='Confirm Password' 
                        onChange={(e) => setConfirmPassword(e.target.value)}
                        value={confirmPassword}
                        />
                    </InputGroup>
                  </Form.Group>

                  <FormCheck type='checkbox' className='d-flex mb-4'>
                    <FormCheck.Input required id='terms' className='me-2' />
                    <FormCheck.Label htmlFor='terms'>
                      I agree to the <Card.Link>terms and conditions</Card.Link>
                    </FormCheck.Label>
                  </FormCheck>

                  <Button variant='primary' type='submit' className='w-100' onClick={submitHandler}>
                    Sign up
                  </Button>
                </Form>

                <div className='mt-3 mb-4 text-center'>
                  <span className='fw-normal'>or</span>
                </div>
                
                <div className='d-flex justify-content-center my-4'>
                  <Button variant='outline-light' className='btn-icon-only btn-pill text-facebook me-2'>
                    <FontAwesomeIcon icon={faFacebookF} />
                  </Button>
                  
                  <Button variant='outline-light' className='btn-icon-only btn-pill text-twitter me-2'>
                    <FontAwesomeIcon icon={faTwitter} />
                  </Button>

                  <Button variant='outline-light' className='btn-icon-only btn-pil text-dark'>
                    <FontAwesomeIcon icon={faGithub} />
                  </Button>
                </div>
                
                <div className='d-flex justify-content-center align-items-center mt-4'>
                  <span className='fw-normal'>
                    Already have an account?
                    <Card.Link as={Link} to={'/login'} className='fw-bold'>
                      {` Login here `}
                    </Card.Link>
                  </span>
                </div>

              </div>
            </Col>
          </Row>

        </Container>
      </section>
    </main>
  );
};
--#

--% ResetPassword.js
import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faAngleLeft, faEnvelope, faUnlockAlt } from '@fortawesome/free-solid-svg-icons';
import { Col, Row, Form, Card, Button, Container, InputGroup } from 'react-bootstrap';
import { Link } from 'react-router-dom';

import { Routes } from '../routes';

export default () => {
  return (
    <main>
      <section className='bg-soft d-flex align-items-center my-5 mt-lg-6 mb-lg-5'>
        <Container>
          <Row className='justify-content-center'>

            <p className='text-center'>
              <Card.Link as={Link} to={Routes.Signin.path} className='text-gray-700'>
                <FontAwesomeIcon icon={faAngleLeft} className='me-2' /> Back to sign in
              </Card.Link>
            </p>

            <Col xs={12} className='d-flex align-items-center justify-content-center'>
              <div className='bg-white shadow-soft border rounded border-light p-4 p-lg-5 w-100 fmxw-500'>
                <h3 className='mb-4'>Reset password</h3>

                <Form>

                  <Form.Group id='email' className='mb-4'>
                    <Form.Label>Your Email</Form.Label>
                    <InputGroup>
                      <InputGroup.Text>
                        <FontAwesomeIcon icon={faEnvelope} />
                      </InputGroup.Text>
                      <Form.Control autoFocus required type='email' placeholder='example@company.com' />
                    </InputGroup>
                  </Form.Group>

                  <Form.Group id='password' className='mb-4'>
                    <Form.Label>Your Password</Form.Label>
                    <InputGroup>
                      <InputGroup.Text>
                        <FontAwesomeIcon icon={faUnlockAlt} />
                      </InputGroup.Text>
                      <Form.Control required type='password' placeholder='Password' />
                    </InputGroup>
                  </Form.Group>

                  <Form.Group id='confirmPassword' className='mb-4'>
                    <Form.Label>Confirm Password</Form.Label>
                    <InputGroup>
                      <InputGroup.Text>
                        <FontAwesomeIcon icon={faUnlockAlt} />
                      </InputGroup.Text>
                      <Form.Control required type='password' placeholder='Confirm Password' />
                    </InputGroup>
                  </Form.Group>

                  <Button variant='primary' type='submit' className='w-100'>
                    Reset password
                  </Button>

                </Form>

              </div>
            </Col>

          </Row>
        </Container>
      </section>
    </main>
  );
};
--#

--% index.js
import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux'
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.min.css';
import '@fortawesome/fontawesome-free/css/all.min.css';
import './assets/css/animate.min.css';
import './assets/scss/light-bootstrap-dashboard-react.scss?v=2.0.0';
import './assets/css/demo.css';

import Login from './pages/Login';
import Register from './pages/Register';
import AdminLayout from 'layouts/Admin.js';
import store from './store'

ReactDOM.render(
	<Provider store={store}>
		<BrowserRouter>
			<Switch>
	
				<Route path='/admin' render={(props) => <AdminLayout {...props} />} />
	
				<Route path='/login' render={(props) => <Login {...props} />} />
				<Route path='/register' render={(props) => <Register {...props} />} />

				<Redirect from='/' to='/admin/dashboard' />

			</Switch>
		</BrowserRouter>
	</Provider>,
	document.getElementById('root')
);
--#

--% README.md
Generated by: 
WM -e'***urlr,*/B^{@Product}name,s;price,n^'
--#

--% Sidebar.js
import React from 'react';
import { useLocation, NavLink } from 'react-router-dom';

import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as RiIcons from 'react-icons/ri';

import SubMenu from './SubMenu';
import SidebarToggler from './SidebarToggler';
import './Sidebar.css';

const apps = [
__TEMPLATE_APP_SIDEBAR_ROUTES
// {
// 	title:'Product',
// 	icon: <AiIcons.AiFillHome />,
// 	iconClosed: <RiIcons.RiArrowDownSFill />,
// 	iconOpened: <RiIcons.RiArrowUpSFill />,
// 	path: '/admin/product',
// 	subNav: [
// 		{ title: 'create', path: '/admin/product/create', icon: <IoIcons.IoIosPaper /> },
// 		{ title: 'read', path: '/admin/product/list', icon: <IoIcons.IoIosPaper /> },
// 		{ title: 'detail', path: '/admin/product/:id', icon: <IoIcons.IoIosPaper /> },
// 		{ title: 'update', path: '/admin/product/:id/edit', icon: <IoIcons.IoIosPaper /> },
// 		{ title: 'delete', path: '/admin/product/:id/update', icon: <IoIcons.IoIosPaper /> },
// 	]
// },
]

const SidebarBottom = ({
	judul,
	data,
}) => {
	return (<>
		<h6 className='md:min-w-full text-blueGray-500 text-xs uppercase font-bold block pt-1 pb-4 no-underline'>
			{judul}
		</h6>

		{data.map( (item, index) => (<SubMenu item={item} key={index} />) )}
	</>);
};

function Sidebar({
	match,
	location,
	history,
	active_classname,
	is_active,
	togglerMenu,
	color,
	image,
	routes,
}) {
	const location = useLocation();
	const pathname = location.pathname;

	const activeRoute = (routeName) => {
		return pathname.indexOf(routeName) > -1 ? 'active' : '';
	};

	return (
		<div>

			<SidebarToggler 
				active_classname={is_active ? 'sidebar-toggler active' : 'sidebar-toggler'} 
				togglerMenu={togglerMenu} 
				/>

			<div 
				className={`sidebar ` + active_classname} 
				data-image={image} 
				data-color={color}>

				<div
					className='sidebar-background'
					style={{ backgroundImage: 'url(' + image + ')', }}
				/>

				<div className='sidebar-wrapper'>
					<div className='logo d-flex align-items-center justify-content-start'>
						<a href='http://fulgent.de?ref=lbd-sidebar' className='simple-text logo-mini mx-1'>
							<div className='logo-img'>
								<img src={require('assets/img/reactlogo.png').default} alt='...'/>
							</div>
						</a>
						<a className='simple-text' href='http://fulgent.de'>Fulgent</a>
					</div>

					<SidebarBottom judul='' data={[
						{ title: 'Dashboard', path: '/admin/dashboard', icon: <AiIcons.AiFillHome />, },
						{ title: 'Login', path: '/login', icon: <AiIcons.AiFillHome />, },
						{ title: 'Register', path: '/register', icon: <AiIcons.AiFillHome />, },
					]}/>
					<hr className='my-4 md:min-w-full' />
					<SidebarBottom judul='Apps' data={apps}/>

				</div>

			</div>

		</div>
	);
}

export default Sidebar;
--#

--% SubMenu.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

const SidebarLink = styled(Link)`
	display: flex;
	color: #e1e9fc;
	justify-content: space-between;
	align-items: center;
	padding: 20px;
	list-style: none;
	height: 60px;
	text-decoration: none;
	font-size: 18px;

	&:hover {
		background: #252831;
		border-left: 4px solid #632ce4;
		cursor: pointer;
	}
`;

const SidebarLabel = styled.span`
	margin-left: 16px;
`;

const DropdownLink = styled(Link)`
	background: #414757;
	height: 60px;
	padding-left: 3rem;
	display: flex;
	align-items: center;
	text-decoration: none;
	color: #f5f5f5;
	font-size: 18px;

	&:hover {
		background: #632ce4;
		cursor: pointer;
	}
`;

const SubMenu = ({ item }) => {
	const [subnav, setSubnav] = useState(false);

	const showSubnav = () => setSubnav(!subnav);

	return (
		<>
			<SidebarLink to={item.path} onClick={item.subNav && showSubnav}>
				<div>
					{item.icon}
					<SidebarLabel>{item.title}</SidebarLabel>
				</div>
				<div>
					{item.subNav && subnav
						? item.iconOpened
						: item.subNav
						? item.iconClosed
						: null}
				</div>
			</SidebarLink>
			{subnav &&
				item.subNav.map((item, index) => {
					return (
						<DropdownLink to={item.path} key={index}>
							{item.icon}
							<SidebarLabel>{item.title}</SidebarLabel>
						</DropdownLink>
					);
				})}
		</>
	);
};

export default SubMenu;
--#

--% SidebarToggler.js
import React from 'react';
import { 
	// Nav, Badge, Image, Dropdown, Accordion, Navbar,
	Button,  
} from 'react-bootstrap';
import './SidebarToggler.css';

const SidebarToggler = ({ active_classname, togglerMenu, }) => {

	return (<div className={active_classname}>

	<Button onClick={togglerMenu}>
		<span className='sidebar-icon'>
			M
		</span>
	</Button>

	</div>);
};

export default SidebarToggler;
--#

--% SidebarToggler.css
.sidebar-toggler {
	position: fixed;
	top: 50px;
	/* bottom: 0; */

	width: 50px;
	height: 50px;
	/* right: -50px; */
	left: 10px;
	transition: left .5s ease;
	z-index: 100;
}

.sidebar-toggler.active {
	left: calc(256px + 10px);
}
--#

--% Sidebar.css
:root {
	/* --left-distance: 15%; */
	--left-distance: 256px;
	--left-sidebar-percent: -256px; /* negative dari left-distance */
}

.sidebar-layout {
	position: fixed;
	top: 0;
	bottom: 0;
	left: var(--left-sidebar-percent);
	/* width: var(--left-distance); */
	overflow-y: auto;
	width: 256px;
	box-shadow: -3px -3px 7px #fffff7, 3px 3px 5px rgba(90,100,120,.2);
	transition: left .5s ease;
	z-index: 10;
	/* border: 1px solid crimson; */
}

.sidebar-layout.active {
	left: calc(var(--left-sidebar-percent) + var(--left-distance));
}
--#

--% routes.js
import Dashboard from './pages/Dashboard.js';
__TEMPLATE_APP_IMPORTS
// import ProductCreate from './apps/product/create';
// import ProductRead from './apps/product/read';
// import ProductDetail from './apps/product/detail';
// import ProductUpdate from './apps/product/update';
// import ProductDelete from './apps/product/delete';

const routes = [
	{ path: '/dashboard', name: 'Dashboard', icon: 'nc-icon nc-chart-pie-35', component: Dashboard, layout: '/admin', },

__TEMPLATE_APP_ROUTES

];

export default routes;
--#

--% Admin.css
.main-section {
	transition: left .5s ease;
	margin-left: 0;
}

.main-section.active {
	margin-left: 256px;
	/* transition: left .5s ease; */
	transition: margin .5s ease-in-out;
}
--#

--% Admin.js
import React from 'react';
import { useLocation, Route, Switch } from 'react-router-dom';

import AdminNavbar from 'components/navbars/AdminNavbar';
import Footer from 'components/footer/Footer';
import Sidebar from 'components/sidebar/Sidebar';
import FixedPlugin from 'components/fixedplugin/FixedPlugin.js';
import routes from 'routes.js';
import sidebarImage from 'assets/img/sidebar-3.jpg';
import './Admin.css';

function Admin() {
	const [image, setImage] = React.useState(sidebarImage);
	const [color, setColor] = React.useState('black');
	const [hasImage, setHasImage] = React.useState(true);

	const location = useLocation();
	const mainPanel = React.useRef(null);
	const [openSidebar, setOpenSidebar] = React.useState(false);

	return (
		<>
			<div>
				
				<Sidebar 
					active_classname={openSidebar ? 'sidebar-layout active' : 'sidebar-layout'}
					is_active={openSidebar}
					togglerMenu={()=>{ setOpenSidebar(!openSidebar); }}
					color={color} 
					image={hasImage ? image : ''} 
					routes={routes} 
					/>

				<main className={'content main-section' + (openSidebar?' active':'')}>
					<div className='main-panel' ref={mainPanel}>

						<AdminNavbar />

						<div className='content'>
							<Switch>
							{
								routes.map((prop, key) => {
									if (prop.layout === '/admin') {
										return (
											<Route
												path={prop.layout + prop.path}
												render={(props) => <prop.component {...props} />}
												key={key}
											/>
										);
									} else {
										return null;
									}
								})
							}
							</Switch>
						</div>

						<Footer />

					</div>
				</main>

			</div>

			<FixedPlugin
				hasImage={hasImage}
				setHasImage={() => setHasImage(!hasImage)}
				color={color}
				setColor={(color) => setColor(color)}
				image={image}
				setImage={(image) => setImage(image)}
			/>

		</>
	);
}

export default Admin;
--#

--% Dashboard.js
import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import ChartistGraph from 'react-chartist';
import {
	Badge,
	Button,
	Card,
  Col,
  Container,
  Form,
  Nav,
	Navbar,
  OverlayTrigger,
	Row,
	Table,	
	Tooltip,
} from 'react-bootstrap';

import Paginate from '../components/common/Paginate'
import Message from '../components/common/Message'
import Loader from '../components/common/Loader'

import ProductDetail from './apps/product/ProductDetail'
import ProductList from './apps/product/ProductList'
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
		<>
			<Container fluid>

        <Row>
          <Col md='12'>

          <h1>Latest Products</h1>
            {loading ? <Loader />
              : error ? <Message variant='danger'>{error}</Message>
                :
                <div>
                  <Row>
                    {products
                      ? products.map(product => (
                        <Col key={product._id} sm={12} md={6} lg={4} xl={3}>
                          <ProductList product={product} />
                        </Col>
                      ))
                      : null}
                  </Row>
                  <Paginate page={page} pages={pages} keyword={keyword} />
                </div>
            }
          </Col>
        </Row>

        <Row>
          <Col md='12'>
            <Card>
            <Form.Select>
              <option>Open this select menu</option>
              <option value='1'>One</option>
              <option value='2'>Two</option>
              <option value='3'>Three</option>
            </Form.Select>
            </Card>
          </Col>
        </Row>

        <Row>
          <Col md='6'>
            <Card>
              <Card.Header>
                <Card.Title as='h4'>Email Statistics</Card.Title>
                <p className='card-category'>Last Campaign Performance</p>
              </Card.Header>
              <Card.Body>
                <div
                  className='ct-chart ct-perfect-fourth'
                  id='chartPreferences'
                >
                  <ChartistGraph
                    data={{
                      labels: ['40%', '20%', '40%'],
                      series: [40, 20, 40],
                    }}
                    type='Pie'
                  />
                </div>
                <div className='legend'>
                  <i className='fas fa-circle text-info'></i>
                  Open <i className='fas fa-circle text-danger'></i>
                  Bounce <i className='fas fa-circle text-warning'></i>
                  Unsubscribe
                </div>
                <hr></hr>
                <div className='stats'>
                  <i className='far fa-clock'></i>
                  Campaign sent 2 days ago
                </div>
              </Card.Body>
            </Card>
          </Col>

          <Col md='6'>
          <Card>
            <Card.Header>
              <Card.Title as='h4'>Users Behavior</Card.Title>
              <p className='card-category'>24 Hours performance</p>
            </Card.Header>
            <Card.Body>
              <div className='ct-chart' id='chartHours'>
                <ChartistGraph
                  data={{
                    labels: [
                      '9:00AM',
                      '12:00AM',
                      '3:00PM',
                      '6:00PM',
                      '9:00PM',
                      '12:00PM',
                      '3:00AM',
                      '6:00AM',
                    ],
                    series: [
                      [287, 385, 490, 492, 554, 586, 698, 695],
                      [67, 152, 143, 240, 287, 335, 435, 437],
                      [23, 113, 67, 108, 190, 239, 307, 308],
                    ],
                  }}
                  type='Line'
                  options={{
                    low: 0,
                    high: 800,
                    showArea: false,
                    height: '245px',
                    axisX: {
                      showGrid: false,
                    },
                    lineSmooth: true,
                    showLine: true,
                    showPoint: true,
                    fullWidth: true,
                    chartPadding: {
                      right: 50,
                    },
                  }}
                  responsiveOptions={[
                    [
                      'screen and (max-width: 640px)',
                      {
                        axisX: {
                          labelInterpolationFnc: function (value) {
                            return value[0];
                          },
                        },
                      },
                    ],
                  ]}
                />
              </div>
            </Card.Body>
            <Card.Footer>
              <div className='legend'>
                <i className='fas fa-circle text-info'></i>
                Open <i className='fas fa-circle text-danger'></i>
                Click <i className='fas fa-circle text-warning'></i>
                Click Second Time
              </div>
              <hr></hr>
              <div className='stats'>
                <i className='fas fa-history'></i>
                Updated 3 minutes ago
              </div>
            </Card.Footer>
          </Card>
          </Col>
        </Row>

        <Row>
          <Col md='2'>
            <Card className='card-stats'>
              <Card.Body>
                <Row>
                  <Col xs='5'>
                    <div className='icon-big text-center icon-warning'>
                      <i className='nc-icon nc-chart text-warning'></i>
                    </div>
                  </Col>
                  <Col xs='7'>
                    <div className='numbers'>
                      <p className='card-category'>Number</p>
                      <Card.Title as='h4'>150GB</Card.Title>
                    </div>
                  </Col>
                </Row>
              </Card.Body>
              <Card.Footer>
                <hr></hr>
                <div className='stats'>
                  <i className='fas fa-redo mr-1'></i>
                  Update Now
                </div>
              </Card.Footer>
            </Card>
          </Col>

          <Col md='10'>
            <Card className='card-tasks'>
              <Card.Header>
                <Card.Title as='h4'>Tasks</Card.Title>
                <p className='card-category'>Backend development</p>
              </Card.Header>

              <Card.Body>
                <div className='table-full-width'>
                  <Table>
                    <tbody>
                      <tr>
                        <td>
                          <Form.Check className='mb-1 pl-0'>
                            <Form.Check.Label>
                              <Form.Check.Input
                                defaultValue=''
                                type='checkbox'
                              ></Form.Check.Input>
                              <span className='form-check-sign'></span>
                            </Form.Check.Label>
                          </Form.Check>
                        </td>
                        <td>
                          Sign contract for 'What are conference organizers
                          afraid of?'
                        </td>
                        <td className='td-actions text-right'>
                          <OverlayTrigger
                            overlay={
                              <Tooltip id='tooltip-488980961'>
                                Edit Task..
                              </Tooltip>
                            }
                          >
                            <Button
                              className='btn-simple btn-link p-1'
                              type='button'
                              variant='info'
                            >
                              <i className='fas fa-edit'></i>
                            </Button>
                          </OverlayTrigger>
                          <OverlayTrigger
                            overlay={
                              <Tooltip id='tooltip-506045838'>Remove..</Tooltip>
                            }
                          >
                            <Button
                              className='btn-simple btn-link p-1'
                              type='button'
                              variant='danger'
                            >
                              <i className='fas fa-times'></i>
                            </Button>
                          </OverlayTrigger>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <Form.Check className='mb-1 pl-0'>
                            <Form.Check.Label>
                              <Form.Check.Input
                                defaultChecked
                                defaultValue=''
                                type='checkbox'
                              ></Form.Check.Input>
                              <span className='form-check-sign'></span>
                            </Form.Check.Label>
                          </Form.Check>
                        </td>
                        <td>
                          Lines From Great Russian Literature? Or E-mails From
                          My Boss?
                        </td>
                        <td className='td-actions text-right'>
                          <OverlayTrigger
                            overlay={
                              <Tooltip id='tooltip-537440761'>
                                Edit Task..
                              </Tooltip>
                            }
                          >
                            <Button
                              className='btn-simple btn-link p-1'
                              type='button'
                              variant='info'
                            >
                              <i className='fas fa-edit'></i>
                            </Button>
                          </OverlayTrigger>
                          <OverlayTrigger
                            overlay={
                              <Tooltip id='tooltip-21130535'>Remove..</Tooltip>
                            }
                          >
                            <Button
                              className='btn-simple btn-link p-1'
                              type='button'
                              variant='danger'
                            >
                              <i className='fas fa-times'></i>
                            </Button>
                          </OverlayTrigger>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <Form.Check className='mb-1 pl-0'>
                            <Form.Check.Label>
                              <Form.Check.Input
                                defaultChecked
                                defaultValue=''
                                type='checkbox'
                              ></Form.Check.Input>
                              <span className='form-check-sign'></span>
                            </Form.Check.Label>
                          </Form.Check>
                        </td>
                        <td>
                          Flooded: One year later, assessing what was lost and
                          what was found when a ravaging rain swept through
                          metro Detroit
                        </td>
                        <td className='td-actions text-right'>
                          <OverlayTrigger
                            overlay={
                              <Tooltip id='tooltip-577232198'>
                                Edit Task..
                              </Tooltip>
                            }
                          >
                            <Button
                              className='btn-simple btn-link p-1'
                              type='button'
                              variant='info'
                            >
                              <i className='fas fa-edit'></i>
                            </Button>
                          </OverlayTrigger>
                          <OverlayTrigger
                            overlay={
                              <Tooltip id='tooltip-773861645'>Remove..</Tooltip>
                            }
                          >
                            <Button
                              className='btn-simple btn-link p-1'
                              type='button'
                              variant='danger'
                            >
                              <i className='fas fa-times'></i>
                            </Button>
                          </OverlayTrigger>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <Form.Check className='mb-1 pl-0'>
                            <Form.Check.Label>
                              <Form.Check.Input
                                defaultChecked
                                type='checkbox'
                              ></Form.Check.Input>
                              <span className='form-check-sign'></span>
                            </Form.Check.Label>
                          </Form.Check>
                        </td>
                        <td>
                          Create 4 Invisible User Experiences you Never Knew
                          About
                        </td>
                        <td className='td-actions text-right'>
                          <OverlayTrigger
                            overlay={
                              <Tooltip id='tooltip-422471719'>
                                Edit Task..
                              </Tooltip>
                            }
                          >
                            <Button
                              className='btn-simple btn-link p-1'
                              type='button'
                              variant='info'
                            >
                              <i className='fas fa-edit'></i>
                            </Button>
                          </OverlayTrigger>
                          <OverlayTrigger
                            overlay={
                              <Tooltip id='tooltip-829164576'>Remove..</Tooltip>
                            }
                          >
                            <Button
                              className='btn-simple btn-link p-1'
                              type='button'
                              variant='danger'
                            >
                              <i className='fas fa-times'></i>
                            </Button>
                          </OverlayTrigger>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <Form.Check className='mb-1 pl-0'>
                            <Form.Check.Label>
                              <Form.Check.Input
                                defaultValue=''
                                type='checkbox'
                              ></Form.Check.Input>
                              <span className='form-check-sign'></span>
                            </Form.Check.Label>
                          </Form.Check>
                        </td>
                        <td>Read 'Following makes Medium better'</td>
                        <td className='td-actions text-right'>
                          <OverlayTrigger
                            overlay={
                              <Tooltip id='tooltip-160575228'>
                                Edit Task..
                              </Tooltip>
                            }
                          >
                            <Button
                              className='btn-simple btn-link p-1'
                              type='button'
                              variant='info'
                            >
                              <i className='fas fa-edit'></i>
                            </Button>
                          </OverlayTrigger>
                          <OverlayTrigger
                            overlay={
                              <Tooltip id='tooltip-922981635'>Remove..</Tooltip>
                            }
                          >
                            <Button
                              className='btn-simple btn-link p-1'
                              type='button'
                              variant='danger'
                            >
                              <i className='fas fa-times'></i>
                            </Button>
                          </OverlayTrigger>
                        </td>
                      </tr>
                      <tr>
                        <td>
                          <Form.Check className='mb-1 pl-0'>
                            <Form.Check.Label>
                              <Form.Check.Input
                                defaultValue=''
                                disabled
                                type='checkbox'
                              ></Form.Check.Input>
                              <span className='form-check-sign'></span>
                            </Form.Check.Label>
                          </Form.Check>
                        </td>
                        <td>Unfollow 5 enemies from twitter</td>
                        <td className='td-actions text-right'>
                          <OverlayTrigger
                            overlay={
                              <Tooltip id='tooltip-938342127'>
                                Edit Task..
                              </Tooltip>
                            }
                          >
                            <Button
                              className='btn-simple btn-link p-1'
                              type='button'
                              variant='info'
                            >
                              <i className='fas fa-edit'></i>
                            </Button>
                          </OverlayTrigger>
                          <OverlayTrigger
                            overlay={
                              <Tooltip id='tooltip-119603706'>Remove..</Tooltip>
                            }
                          >
                            <Button
                              className='btn-simple btn-link p-1'
                              type='button'
                              variant='danger'
                            >
                              <i className='fas fa-times'></i>
                            </Button>
                          </OverlayTrigger>
                        </td>
                      </tr>
                    </tbody>
                  </Table>
                </div>
              </Card.Body>

              <Card.Footer>
                <hr></hr>
                <div className='stats'>
                  <i className='now-ui-icons loader_refresh spin'></i>
                  Updated 3 minutes ago
                </div>
              </Card.Footer>
            </Card>

          </Col>
        </Row>

			</Container>
		</>
	);
}

export default Dashboard;
--#
