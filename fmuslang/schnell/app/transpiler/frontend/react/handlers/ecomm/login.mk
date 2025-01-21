--% index/fmus
c:/tmp/hapus/coba,d(/mk)	
	components,d
		NavBar.js,f(e=__FILE__=NavBar.js)
	utils,d
		generateToken.js,f(e=__FILE__=generateToken.js)
	pages,d
		api,d(/mk)
			auth,d(/mk)
				login.js,f(e=__FILE__=login.js)
		signin.js,f(e=__FILE__=signin.js)
	styles,d(/mk)
		loading.css,f(e=__FILE__=loading.css)
		globals.css,f(e=__FILE__=globals.css)
	store,d(/mk)
		GlobalState.js,f(e=__FILE__=GlobalState.js)
		Actions.js,f(e=__FILE__=Actions.js)
		Reducers.js,f(e=__FILE__=Reducers.js)
	next.config.js,f(e=__FILE__=next.config.js)
	#&*wsl_ngetik=__FILE__=cli
--#

--% globals.css
html,
body {
  padding: 0;
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen,
    Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
}

a {
  color: inherit;
  text-decoration: none;
}

* {
  box-sizing: border-box;
}

img{
  object-fit: cover;
  object-position: 0 30%;
}

/* ----------- Loading ------------- */
@import url("./loading.css");

/* ----------- Products ------------- */
/* @import url("./product.css"); */

/* ----------- Profile ------------- */
/* @import url("./profile.css"); */

/* ----------- Products Manager ------------- */
/* @import url("./products_manager.css"); */
--#

--% NavBar.js
import React, { useContext } from 'react'
import Link from 'next/link'
import {useRouter} from 'next/router'
import {DataContext} from '../store/GlobalState'
import Cookie from 'js-cookie'

function NavBar() {
    const router = useRouter()
    const {state, dispatch} = useContext(DataContext)
    const { auth, cart } = state


    const isActive = (r) => {
        if(r === router.pathname){
            return " active"
        }else{
            return ""
        }
    }

    const handleLogout = () => {
        Cookie.remove('refreshtoken', {path: 'api/auth/accessToken'})
        localStorage.removeItem('firstLogin')
        dispatch({ type: 'AUTH', payload: {} })
        dispatch({ type: 'NOTIFY', payload: {success: 'Logged out!'} })
        return router.push('/')
    }

    const adminRouter = () => {
        return(
            <>
            <Link href="/users">
                <a className="dropdown-item">Users</a>
            </Link>
            <Link href="/create">
                <a className="dropdown-item">Products</a>
            </Link>
            <Link href="/categories">
                <a className="dropdown-item">Categories</a>
            </Link>
            </>
        )
    }

    const loggedRouter = () => {
        return(
            <li className="nav-item dropdown">
                <a className="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                    <img src={auth.user.avatar} alt={auth.user.avatar} 
                    style={{
                        borderRadius: '50%', width: '30px', height: '30px',
                        transform: 'translateY(-3px)', marginRight: '3px'
                    }} /> {auth.user.name}
                </a>

                <div className="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                    <Link href="/profile">
                        <a className="dropdown-item">Profile</a>
                    </Link>
                    {
                        auth.user.role === 'admin' && adminRouter()
                    }
                    <div className="dropdown-divider"></div>
                    <button className="dropdown-item" onClick={handleLogout}>Logout</button>
                </div>
            </li>
        )
    }

    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <Link  href="/">
                <a className="navbar-brand">DEVAT</a>
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
                                    <span className="position-absolute"
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
                    {
                        Object.keys(auth).length === 0 
                        ? <li className="nav-item">
                            <Link href="/signin">
                                <a className={"nav-link" + isActive('/signin')}>
                                    <i className="fas fa-user" aria-hidden="true"></i> Sign in
                                </a>
                            </Link>
                        </li>
                        : loggedRouter()
                    }
                </ul>
            </div>
        </nav>
    )
}

export default NavBar
--#

--% GlobalState.js
import { createContext, useReducer, useEffect } from 'react'
import reducers from './Reducers'
import { getData } from '../utils/fetchData'


export const DataContext = createContext()


export const DataProvider = ({children}) => {
    const initialState = { 
        notify: {}, auth: {}, cart: [], modal: [], orders: [], users: [], categories: []
    }

    const [state, dispatch] = useReducer(reducers, initialState)
    const { cart, auth } = state

    useEffect(() => {
        const firstLogin = localStorage.getItem("firstLogin");
        if(firstLogin){
            getData('auth/accessToken').then(res => {
                if(res.err) return localStorage.removeItem("firstLogin")
                dispatch({ 
                    type: "AUTH",
                    payload: {
                        token: res.access_token,
                        user: res.user
                    }
                })
            })
        }

        getData('categories').then(res => {
            if(res.err) return dispatch({type: 'NOTIFY', payload: {error: res.err}})

            dispatch({ 
                type: "ADD_CATEGORIES",
                payload: res.categories
            })
        })
        
    },[])

    useEffect(() => {
        const __next__cart01__devat = JSON.parse(localStorage.getItem('__next__cart01__devat'))

        if(__next__cart01__devat) dispatch({ type: 'ADD_CART', payload: __next__cart01__devat })
    }, [])

    useEffect(() => {
        localStorage.setItem('__next__cart01__devat', JSON.stringify(cart))
    }, [cart])

    useEffect(() => {
        if(auth.token){
            getData('order', auth.token)
            .then(res => {
                if(res.err) return dispatch({type: 'NOTIFY', payload: {error: res.err}})
                
                dispatch({type: 'ADD_ORDERS', payload: res.orders})
            })

            if(auth.user.role === 'admin'){
                getData('user', auth.token)
                .then(res => {
                    if(res.err) return dispatch({type: 'NOTIFY', payload: {error: res.err}})
                
                    dispatch({type: 'ADD_USERS', payload: res.users})
                })
            }
        }else{
            dispatch({type: 'ADD_ORDERS', payload: []})
            dispatch({type: 'ADD_USERS', payload: []})
        }
    },[auth.token])

    return(
        <DataContext.Provider value={{state, dispatch}}>
            {children}
        </DataContext.Provider>
    )
}
--#

--% Actions.js
export const ACTIONS = {
    NOTIFY: 'NOTIFY',
    AUTH: 'AUTH',
    ADD_CART: 'ADD_CART',
    ADD_MODAL: 'ADD_MODAL',
    ADD_ORDERS: 'ADD_ORDERS',
    ADD_USERS: 'ADD_USERS',
    ADD_CATEGORIES: 'ADD_CATEGORIES',
}

export const addToCart = (product, cart) => {
    if(product.inStock === 0)
    return ({ type: 'NOTIFY', payload: {error: 'This product is out of stock.'} }) 

    const check = cart.every(item => {
        return item._id !== product._id
    })

    if(!check) return ({ type: 'NOTIFY', payload: {error: 'The product has been added to cart.'} }) 

    return ({ type: 'ADD_CART', payload: [...cart, {...product, quantity: 1}] }) 
}

export const decrease = (data, id) => {
    const newData = [...data]
    newData.forEach(item => {
        if(item._id === id) item.quantity -= 1
    })

    return ({ type: 'ADD_CART', payload: newData })
}

export const increase = (data, id) => {
    const newData = [...data]
    newData.forEach(item => {
        if(item._id === id) item.quantity += 1
    })

    return ({ type: 'ADD_CART', payload: newData })
}


export const deleteItem = (data, id, type) => {
    const newData = data.filter(item => item._id !== id)
    return ({ type, payload: newData})
}

export const updateItem = (data, id, post, type) => {
    const newData = data.map(item => (item._id === id ? post : item))
    return ({ type, payload: newData})
}
--#

--% Reducers.js
import { ACTIONS } from './Actions'


const reducers = (state, action) => {
    switch(action.type){
        case ACTIONS.NOTIFY:
            return {
                ...state,
                notify: action.payload
            };
        case ACTIONS.AUTH:
            return {
                ...state,
                auth: action.payload
            };
        case ACTIONS.ADD_CART:
            return {
                ...state,
                cart: action.payload
            };
        case ACTIONS.ADD_MODAL:
            return {
                ...state,
                modal: action.payload
            };
        case ACTIONS.ADD_ORDERS:
            return {
                ...state,
                orders: action.payload
            };
        case ACTIONS.ADD_USERS:
            return {
                ...state,
                users: action.payload
            };
        case ACTIONS.ADD_CATEGORIES:
            return {
                ...state,
                categories: action.payload
            };
        default:
            return state;
    }
}

export default reducers
--#

--% signin.js
import Head from 'next/head'
import Link from 'next/link'
import {useState, useContext, useEffect} from 'react'
import {DataContext} from '../store/GlobalState'
import {postData} from '../utils/fetchData'
import Cookie from 'js-cookie'
import { useRouter } from 'next/router'

const Signin = () => {
  const initialState = { email: '', password: '' }
  const [userData, setUserData] = useState(initialState)
  const { email, password } = userData

  const {state, dispatch} = useContext(DataContext)
  const { auth } = state

  const router = useRouter()

  const handleChangeInput = e => {
    const {name, value} = e.target
    setUserData({...userData, [name]:value})
    dispatch({ type: 'NOTIFY', payload: {} })
  }

  const handleSubmit = async e => {
    e.preventDefault()
    dispatch({ type: 'NOTIFY', payload: {loading: true} })
    const res = await postData('auth/login', userData)
    
    if(res.err) return dispatch({ type: 'NOTIFY', payload: {error: res.err} })
    dispatch({ type: 'NOTIFY', payload: {success: res.msg} })

    dispatch({ type: 'AUTH', payload: {
      token: res.access_token,
      user: res.user
    }})

    Cookie.set('refreshtoken', res.refresh_token, {
      path: 'api/auth/accessToken',
      expires: 7
    })

    localStorage.setItem('firstLogin', true)
  }

  useEffect(() => {
    if(Object.keys(auth).length !== 0) router.push("/")
  }, [auth])

	return(
		<div>
			<Head>
				<title>Sign in Page</title>
			</Head>

			<form className="mx-auto my-4" style={{maxWidth: '500px'}} onSubmit={handleSubmit}>
				<div className="form-group">
					<label htmlFor="exampleInputEmail1">Email address</label>
					<input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp"
					name="email" value={email} onChange={handleChangeInput} />
					<small id="emailHelp" className="form-text text-muted">We'll never share your email with anyone else.</small>
				</div>
				<div className="form-group">
					<label htmlFor="exampleInputPassword1">Password</label>
					<input type="password" className="form-control" id="exampleInputPassword1"
					name="password" value={password} onChange={handleChangeInput} />
				</div>
				
				<button type="submit" className="btn btn-dark w-100">Login</button>

				<p className="my-2">
					You don't have an account? <Link href="/register"><a style={{color: 'crimson'}}>Register Now</a></Link>
				</p>
			</form>
		</div>
	)
}

export default Signin
--#

--% next.config.js
// mongodb+srv://usef:<password>@cluster0.rjg8z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
module.exports = {
	env: {
		"BASE_URL": "http://localhost:3000",
		// "MONGODB_URL": "mongodb://usef:rahasia@localhost:27017/tempdb",
		"MONGODB_URL": "mongodb+srv://usef:rahasia@cluster0.rjg8z.mongodb.net/tempdb?retryWrites=true&w=majority",
		"ACCESS_TOKEN_SECRET": "b825234d450139f812cfd83e45d306172539607e815c48cf1d",
		"REFRESH_TOKEN_SECRET": "dc2f75f83ce1f0403f0fc0572efd4bb1477b212a382b952cce6391ebfdd2e71c96a0c10089b90048",
		//"PAYPAL_CLIENT_ID": "AfGpUJHDDbQYnBia9ZWfxzuf4vX5jo1HqPnd2lGL_tWCLRiY1wIVqarspZYDXLaGskSUqCrnb8f8KgPX",
		//"CLOUD_UPDATE_PRESET": "next_store",
		//"CLOUD_NAME": "dwte8omc0",
		//"CLOUD_API": "https://api.cloudinary.com/v1_1/dwte8omc0/image/upload"
	}
}
--#

--% generateToken.js
import jwt from 'jsonwebtoken'

export const createAccessToken = (payload) => {
	console.log(process.env.ACCESS_TOKEN_SECRET)
	return jwt.sign(payload, process.env.ACCESS_TOKEN_SECRET, {expiresIn: '15m'})
}

export const createRefreshToken = (payload) => {
	return jwt.sign(payload, process.env.REFRESH_TOKEN_SECRET, {expiresIn: '7d'})
}
--#

--% login.js
import connectDB from '../../../utils/connectDB'
import Users from '../../../models/userModel'
import bcrypt from 'bcrypt'
import { createAccessToken, createRefreshToken } from '../../../utils/generateToken'

connectDB()

export default async (req, res) => {
	switch(req.method){
		case "POST":
			await login(req, res)
			break;
	}
}

const login = async (req, res) => {
	try{
		const { email, password } = req.body

		const user = await Users.findOne({ email })
		if(!user) return res.status(400).json({err: 'This user does not exist.'})

		const isMatch = await bcrypt.compare(password, user.password)
		if(!isMatch) return res.status(400).json({err: 'Incorrect password.'})

		const access_token = createAccessToken({id: user._id})
		const refresh_token = createRefreshToken({id: user._id})
		
		res.json({
			msg: "Login Success!",
			refresh_token,
			access_token,
			user: {
				name: user.name,
				email: user.email,
				role: user.role,
				avatar: user.avatar,
				root: user.root
			}
		})

	} catch(err) {
		return res.status(500).json({err: err.message})
	}
}
--#

--% loading.css
.loading{
	display: flex;
	justify-content: center;
	align-items: center;
}
.loading svg{
	font-size: 5px;
	font-weight: 900;
	text-transform: uppercase;
	letter-spacing: 1px;
	animation: text 1s ease-in-out infinite;
}
@keyframes text{
	50%{ opacity: 0.1;}
}
.loading polygon{
	stroke-dasharray: 22;
	stroke-dashoffset: 1;
	animation: dash 4s cubic-bezier(0.455, 0.03, 0.515, 0.955)
	infinite alternate-reverse;
}
@keyframes dash{
	to{stroke-dashoffset: 234;}
}
--#

--% cli
welcome to LOGIN baby!
--#
