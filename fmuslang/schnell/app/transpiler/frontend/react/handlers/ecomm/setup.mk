--% index/fmus
c:/tmp/hapus/coba,d(/mk)
	# $*"/mnt/c/Program Files/ConEmu/ConEmu64.exe"
	# &*wnd_create=cmd.exe
	# &*wnd_ngetik=*cmd.exe=__FILE__=coba tulis
	# &*wsl_ngetik=__FILE__=cli
	components,d(/mk)
		Layout.js,f(e=__FILE__=Layout.js)
		NavBar.js,f(e=__FILE__=NavBar.js)
	pages,d
		_document.js,f(e=__FILE__=_document.js)
		_app.js,f(e=__FILE__=_app.js)
		index.js,f(e=__FILE__=index.js)
		cart.js,f(e=__FILE__=cart.js)
		product.js,f(e=__FILE__=product.js)
		signin.js,f(e=__FILE__=signin.js)
		register.js,f(e=__FILE__=register.js)
--#

--% index.js
const Home = () => {
	return (<div>
	Home
	</div>)
}
export default Home
--#

--% _document.js
import Document, {Html, Head, Main, NextScript} from 'next/document'

class MyDocument extends Document{
	render(){
		return(
			<Html lang="en">
				<Head>
					<meta name="description" content="latihan bradda"/>
					<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" />
					<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
					<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.bundle.min.js"></script>
					<script src="https://kit.fontawesome.com/a076d05399.js"></script>
				</Head>
				<body>
					<Main />
					<NextScript />
				</body>
			</Html>
		)
	}
}

export default MyDocument

--#

--% _app.js
import '../styles/globals.css'
import Layout from '../components/Layout'
// import { DataProvider } from '../store/GlobalState'

function MyApp({ Component, pageProps }) {
  return (
		<Layout>
			<Component {...pageProps} />
		</Layout>
  )
}

export default MyApp
--#

--% Layout.js
import React from 'react'
import NavBar from './NavBar'


function Layout({children}) {
	return (
		<div className="container">
			<NavBar />

			{children}
		</div>
	)
}

export default Layout
--#

--% NavBar.js
import React, { useContext } from 'react'
import Link from 'next/link'
import {useRouter} from 'next/router'

function NavBar() {
	const cart = {
		length: 2,
	}

  const router = useRouter()
  const isActive = (r) => {
    if(r === router.pathname){
      return " active"
    }else{
      return ""
    }
  }

	return (		
		<nav className="navbar navbar-expand-lg navbar-light bg-light">
			<Link  href="/">
				<a className="navbar-brand">
				Site Brand
				</a>
			</Link>

			<button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
				<span className="navbar-toggler-icon"></span>
			</button>

			<div className="collapse navbar-collapse justify-content-end" id="navbarNavDropdown">
				<ul className="navbar-nav p-1">
					<li className="nav-item">
						<Link href="/cart">
							<a className={"nav-link" + isActive('/cart')}>
								<i className="fas fa-shopping-cart position-relative" aria-hidden="true">
									<span 
										className="position-absolute"
										style={{
											padding: '3px 6px',
											background: '#ed143dc2',
											borderRadius: '50%',
											top: '-10px',
											right: '-10px',
											color: 'white',
											fontSize: '14px'
										}}>
										{cart.length}
									</span>
								</i> Cart
							</a>
						</Link>
					</li>
					
					<li className="nav-item">
						<Link href="/signin">
							<a className={"nav-link" + isActive('/signin')}>
								<i className="fas fa-user" aria-hidden="true"></i> Sign in
							</a>
						</Link>
					</li>
				</ul>
			</div>
		</nav>
	)
}

export default NavBar
--#

--% cart.js
import Head from 'next/head'
import Link from 'next/link'

const Cart = () => {
	return(
		<div className="row mx-auto">
			<Head>
				<title>Cart Page</title>
			</Head>

			<div className="col-md-8 text-secondary table-responsive my-3">
				<h2 className="text-uppercase">Shopping Cart</h2>
			</div>

			<div className="col-md-4 my-3 text-right text-uppercase text-secondary">
				<form>
					<h2>Shipping</h2>
				</form>

				<Link href='/signin'>
					<a className="btn btn-dark my-2">
					Proceed with payment
					</a>
				</Link>            
			</div>
		</div>
	)
}

export default Cart
--#

--% product.js
const Product = () => {
	return (<div>
	Product
	</div>)
}
export default Product
--#

--% signin.js
import Head from 'next/head'
import Link from 'next/link'

const Signin = () => {

	return(
		<div>
			<Head>
				<title>Sign in Page</title>
			</Head>

			<form 
				className="mx-auto my-4" 
				style={{maxWidth: '500px'}} 				
				>
				<div className="form-group">
					<label htmlFor="exampleInputEmail1">Email address</label>
					<input 
						type="email" 
						className="form-control" 
						id="exampleInputEmail1" 
						aria-describedby="emailHelp"
						name="email" 
						/>
					<small id="emailHelp" className="form-text text-muted">
					We'll never share your email with anyone else.
					</small>
				</div>
				<div className="form-group">
					<label htmlFor="exampleInputPassword1">Password</label>
					<input 
						type="password" 
						className="form-control" 
						id="exampleInputPassword1"
						name="password" 
						/>
				</div>
				
				<button type="submit" className="btn btn-dark w-100">Login</button>

				<p className="my-2">
					You don't have an account? 
					<Link href="/register">
					<a style={{color: 'crimson'}}>
					Register Now
					</a>
					</Link>
				</p>
			</form>
		</div>
	)
}

export default Signin
--#

--% register.js
import Head from 'next/head'
import Link from 'next/link'

const Register = () => {
	return(
		<div>
			<Head>
				<title>Register Page</title>
			</Head>

			<form 
				className="mx-auto my-4" 
				style={{maxWidth: '500px'}} 
				>
				<div className="form-group">
					<label htmlFor="name">Name</label>
					<input 
						type="text" 
						className="form-control" 
						id="name"
						name="name" 
						/>
				</div>

				<div className="form-group">
					<label htmlFor="exampleInputEmail1">Email address</label>
					<input 
						type="email" 
						className="form-control" 
						id="exampleInputEmail1" 
						aria-describedby="emailHelp"
						name="email" 
						/>
					<small id="emailHelp" className="form-text text-muted">We'll never share your email with anyone else.</small>
				</div>

				<div className="form-group">
					<label htmlFor="exampleInputPassword1">Password</label>
					<input 
						type="password" 
						className="form-control" 
						id="exampleInputPassword1"
						name="password" 
						/>
				</div>

				<div className="form-group">
					<label htmlFor="exampleInputPassword2">Confirm Password</label>
					<input 
						type="password" 
						className="form-control" 
						id="exampleInputPassword2"
						name="cf_password" 
						/>
				</div>
				
				<button type="submit" className="btn btn-dark w-100">Register</button>

				<p className="my-2">
					Already have an account? <Link href="/signin"><a style={{color: 'crimson'}}>Login Now</a></Link>
				</p>
			</form>
		</div>
	)
}

export default Register
--#

--% coba tulis
rem baris 1
rem baris 2
rem baris 3
--#

--% cli
npx create-next-app .
npm i mongoose bcrypt jsonwebtoken
npm run dev
--#
