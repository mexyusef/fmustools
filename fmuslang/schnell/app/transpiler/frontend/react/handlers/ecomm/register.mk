--% index/fmus
c:/tmp/hapus/coba,d(/mk)	
	components,d
		Loading.js,f(e=__FILE__=Loading.js)
		Toast.js,f(e=__FILE__=Toast.js)
		Notify.js,f(e=__FILE__=Notify.js)
	pages,d
        _app.js,f(e=__FILE__=_app.js)
        register.js,f(e=__FILE__=register.js)
		api,d(/mk)
			auth,d(/mk)
				register.js,f(e=__FILE__=api/auth/register.js)
	models,d(/mk)
		userModel.js,f(e=__FILE__=userModel.js)
	utils,d(/mk)
		connectDB.js,f(e=__FILE__=connectDB.js)
		valid.js,f(e=__FILE__=valid.js)
        fetchData.js,f(e=__FILE__=fetchData.js)
	store,d(/mk)
		GlobalState.js,f(e=__FILE__=GlobalState.js)
		Actions.js,f(e=__FILE__=Actions.js)
		Reducers.js,f(e=__FILE__=Reducers.js)
    next.config.js,f(e=__FILE__=next.config.js)
	#&*wsl_ngetik=__FILE__=cli
--#

--% fetchData.js
const baseUrl = process.env.BASE_URL

export const getData = async (url, token) => {
    const res = await fetch(`${baseUrl}/api/${url}`, {
        method: 'GET',
        headers: {
            'Authorization': token
        }
    })

    const data = await res.json()
    return data
}

export const postData = async (url, post, token) => {
    const res = await fetch(`${baseUrl}/api/${url}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        },
        body: JSON.stringify(post)
    })

    const data = await res.json()
    return data
}



export const putData = async (url, post, token) => {
    const res = await fetch(`${baseUrl}/api/${url}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        },
        body: JSON.stringify(post)
    })

    const data = await res.json()
    return data
}

export const patchData = async (url, post, token) => {
    const res = await fetch(`${baseUrl}/api/${url}`, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        },
        body: JSON.stringify(post)
    })

    const data = await res.json()
    return data
}


export const deleteData = async (url, token) => {
    const res = await fetch(`${baseUrl}/api/${url}`, {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': token
        }
    })

    const data = await res.json()
    return data
}
--#

--% register.js
import Head from 'next/head'
import Link from 'next/link'
import {useState, useContext, useEffect} from 'react'
import valid from '../utils/valid'
import {DataContext} from '../store/GlobalState'
import {postData} from '../utils/fetchData'
import { useRouter } from 'next/router'


const Register = () => {
  const initialState = { name: '', email: '', password: '', cf_password: '' }
  const [userData, setUserData] = useState(initialState)
  const { name, email, password, cf_password } = userData

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
    const errMsg = valid(name, email, password, cf_password)
    if(errMsg) return dispatch({ type: 'NOTIFY', payload: {error: errMsg} })

    dispatch({ type: 'NOTIFY', payload: {loading: true} })

    const res = await postData('auth/register', userData)
    
    if(res.err) return dispatch({ type: 'NOTIFY', payload: {error: res.err} })

    return dispatch({ type: 'NOTIFY', payload: {success: res.msg} })
  }

  useEffect(() => {
    if(Object.keys(auth).length !== 0) router.push("/")
  }, [auth])

    return(
        <div>
        <Head>
            <title>Register Page</title>
        </Head>

        <form className="mx-auto my-4" style={{maxWidth: '500px'}} onSubmit={handleSubmit}>
            <div className="form-group">
            <label htmlFor="name">Name</label>
            <input type="text" className="form-control" id="name"
            name="name" value={name} onChange={handleChangeInput} />
            </div>

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

            <div className="form-group">
            <label htmlFor="exampleInputPassword2">Confirm Password</label>
            <input type="password" className="form-control" id="exampleInputPassword2"
            name="cf_password" value={cf_password} onChange={handleChangeInput} />
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

--% _app.js
import '../styles/globals.css'
import Layout from '../components/Layout'
import { DataProvider } from '../store/GlobalState'

function MyApp({ Component, pageProps }) {
  return (
    <DataProvider>
      <Layout>
        <Component {...pageProps} />
      </Layout>
    </DataProvider>
  )
}

export default MyApp

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
        // case ACTIONS.ADD_CART:
        //     return {
        //         ...state,
        //         cart: action.payload
        //     };
        // case ACTIONS.ADD_MODAL:
        //     return {
        //         ...state,
        //         modal: action.payload
        //     };
        // case ACTIONS.ADD_ORDERS:
        //     return {
        //         ...state,
        //         orders: action.payload
        //     };
        // case ACTIONS.ADD_USERS:
        //     return {
        //         ...state,
        //         users: action.payload
        //     };
        // case ACTIONS.ADD_CATEGORIES:
        //     return {
        //         ...state,
        //         categories: action.payload
        //     };
        default:
            return state;
    }
}

export default reducers
--#

--% Actions.js
export const ACTIONS = {
    NOTIFY: 'NOTIFY',
    AUTH: 'AUTH',
    // ADD_CART: 'ADD_CART',
    // ADD_MODAL: 'ADD_MODAL',
    // ADD_ORDERS: 'ADD_ORDERS',
    // ADD_USERS: 'ADD_USERS',
    // ADD_CATEGORIES: 'ADD_CATEGORIES',
}

// export const addToCart = (product, cart) => {
//     if(product.inStock === 0)
//     return ({ type: 'NOTIFY', payload: {error: 'This product is out of stock.'} }) 

//     const check = cart.every(item => {
//         return item._id !== product._id
//     })

//     if(!check) return ({ type: 'NOTIFY', payload: {error: 'The product has been added to cart.'} }) 

//     return ({ type: 'ADD_CART', payload: [...cart, {...product, quantity: 1}] }) 
// }

// export const decrease = (data, id) => {
//     const newData = [...data]
//     newData.forEach(item => {
//         if(item._id === id) item.quantity -= 1
//     })

//     return ({ type: 'ADD_CART', payload: newData })
// }

// export const increase = (data, id) => {
//     const newData = [...data]
//     newData.forEach(item => {
//         if(item._id === id) item.quantity += 1
//     })

//     return ({ type: 'ADD_CART', payload: newData })
// }


// export const deleteItem = (data, id, type) => {
//     const newData = data.filter(item => item._id !== id)
//     return ({ type, payload: newData})
// }

// export const updateItem = (data, id, post, type) => {
//     const newData = data.map(item => (item._id === id ? post : item))
//     return ({ type, payload: newData})
// }
--#

--% GlobalState.js
import { createContext, useReducer, useEffect } from 'react'
import reducers from './Reducers'
import { getData } from '../utils/fetchData'


export const DataContext = createContext()


export const DataProvider = ({children}) => {
    const initialState = { 
        notify: {}, 
        auth: {}, 
        // cart: [], modal: [], orders: [], users: [], categories: []
    }

    const [state, dispatch] = useReducer(reducers, initialState)
    // const { cart, auth } = state

    // useEffect(() => {
    //     const firstLogin = localStorage.getItem("firstLogin");
    //     if(firstLogin){
    //         getData('auth/accessToken').then(res => {
    //             if(res.err) return localStorage.removeItem("firstLogin")
    //             dispatch({ 
    //                 type: "AUTH",
    //                 payload: {
    //                     token: res.access_token,
    //                     user: res.user
    //                 }
    //             })
    //         })
    //     }

    //     getData('categories').then(res => {
    //         if(res.err) return dispatch({type: 'NOTIFY', payload: {error: res.err}})

    //         dispatch({ 
    //             type: "ADD_CATEGORIES",
    //             payload: res.categories
    //         })
    //     })
        
    // },[])

    // useEffect(() => {
    //     const __next__cart01__devat = JSON.parse(localStorage.getItem('__next__cart01__devat'))

    //     if(__next__cart01__devat) dispatch({ type: 'ADD_CART', payload: __next__cart01__devat })
    // }, [])

    // useEffect(() => {
    //     localStorage.setItem('__next__cart01__devat', JSON.stringify(cart))
    // }, [cart])

    // useEffect(() => {
    //     if(auth.token){
    //         getData('order', auth.token)
    //         .then(res => {
    //             if(res.err) return dispatch({type: 'NOTIFY', payload: {error: res.err}})
                
    //             dispatch({type: 'ADD_ORDERS', payload: res.orders})
    //         })

    //         if(auth.user.role === 'admin'){
    //             getData('user', auth.token)
    //             .then(res => {
    //                 if(res.err) return dispatch({type: 'NOTIFY', payload: {error: res.err}})
                
    //                 dispatch({type: 'ADD_USERS', payload: res.users})
    //             })
    //         }
    //     }else{
    //         dispatch({type: 'ADD_ORDERS', payload: []})
    //         dispatch({type: 'ADD_USERS', payload: []})
    //     }
    // },[auth.token])

    return(
        <DataContext.Provider value={{state, dispatch}}>
            {children}
        </DataContext.Provider>
    )
}
--#

--% Loading.js
const Loading = () => {
    return (
        <div className="position-fixed w-100 h-100 text-center loading"
        style={{background: '#0008', color: 'white', top: 0, left: 0, zIndex: 9}}>
            <svg width="205" height="250" viewBox="0 0 40 50">
                <polygon strokeWidth="1" stroke="#fff" fill="none"
                points="20,1 40,40 1,40"></polygon>
                <text fill="#fff" x="5" y="47">Loading</text>
            </svg>
        </div>
    )
}

export default Loading
--#

--% Notify.js
import {useContext} from 'react'
import {DataContext} from '../store/GlobalState'
import Loading from './Loading'
import Toast from './Toast'

const Notify = () => {
    const {state, dispatch} = useContext(DataContext)
    const { notify } = state

    return(
        <> 
            {notify.loading && <Loading />}
            {notify.error && 
                <Toast
                    msg={{ msg: notify.error, title: "Error" }}
                    handleShow={() => dispatch({ type: 'NOTIFY', payload: {} })}
                    bgColor="bg-danger"
                />
            }

            {notify.success && 
                <Toast
                    msg={{ msg: notify.success, title: "Success" }}
                    handleShow={() => dispatch({ type: 'NOTIFY', payload: {} })}
                    bgColor="bg-success"
                />
            }
        </>
    )
}


export default Notify
--#

--% Toast.js
const Toast = ({msg, handleShow, bgColor}) => {
    return(
        <div className={`toast show position-fixed text-light ${bgColor}`}
        style={{ top: '5px', right: '5px', zIndex: 9, minWidth: '280px' }} >

            <div className={`toast-header ${bgColor} text-light`}>
                <strong className="mr-auto text-light">{msg.title}</strong>

                <button type="button" className="ml-2 mb-1 close text-light" 
                data-dismiss="toast" style={{ outline: 'none'}} 
                onClick={handleShow}>x</button>
            </div>

            <div className="toast-body">{msg.msg}</div>

        </div>
    )
}

export default Toast
--#

--% api/auth/register.js
import connectDB from '../../../utils/connectDB'
import Users from '../../../models/userModel'
import valid from '../../../utils/valid'
import bcrypt from 'bcrypt'


connectDB()

export default async (req, res) => {
    switch(req.method){
        case "POST":
            await register(req, res)
            break;
    }
}

const register = async (req, res) => {
    try{
        const { name, email, password, cf_password } = req.body

        const errMsg = valid(name, email, password, cf_password)
        if(errMsg) return res.status(400).json({err: errMsg})

        const user = await Users.findOne({ email })
        if(user) return res.status(400).json({err: 'This email already exists.'})

        const passwordHash = await bcrypt.hash(password, 12)

        const newUser = new Users({ 
            name, email, password: passwordHash, cf_password 
        })

        await newUser.save()
        res.json({msg: "Register Success!"})

    }catch(err){
        return res.status(500).json({err: err.message})
    }
}
--#

--% connectDB.js
import mongoose from 'mongoose'

const connectDB = () => {
    if(mongoose.connections[0].readyState){
        console.log('Already connected.')
        return;
    }
    mongoose.connect(process.env.MONGODB_URL, {
        useCreateIndex: true,
        useFindAndModify: false,
        useNewUrlParser: true,
        useUnifiedTopology: true
    }, err => {
        if(err) throw err;
        console.log('Connected to mongodb.')
    })
}


export default connectDB
--#

--% valid.js
const valid = (name, email, password, cf_password) => {
	if(!name || !email || !password)
	return 'Please add all fields.'

	if(!validateEmail(email))
	return 'Invalid emails.'

	if(password.length < 6)
	return 'Password must be at least 6 characters.'

	if(password !== cf_password)
	return 'Confirm password did not match.'
}

function validateEmail(email) {
	const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	return re.test(email);
}

export default valid
--#

--% userModel.js
import mongoose from 'mongoose'

const userSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    email: {
        type: String,
        required: true,
        unique: true
    },
    password: {
        type: String,
        required: true
    },
    role: {
        type: String,
        default: 'user'
    },
    root: {
        type: Boolean,
        default: false
    },
    avatar: {
        type: String,
        default: 'https://res.cloudinary.com/devatchannel/image/upload/v1602752402/avatar/avatar_cugq40.png'
    }
}, {
    timestamps: true
})

let Dataset = mongoose.models.user || mongoose.model('user', userSchema)
export default Dataset
--#

--% next.config.js
// mongodb+srv://usef:<password>@cluster0.rjg8z.mongodb.net/myFirstDatabase?retryWrites=true&w=majority
module.exports = {
	env: {
		"BASE_URL": "http://localhost:3000",
		// "MONGODB_URL": "mongodb://usef:rahasia@localhost:27017/tempdb",
		"MONGODB_URL": "mongodb+srv://usef:rahasia@cluster0.rjg8z.mongodb.net/tempdb?retryWrites=true&w=majority",
		//"ACCESS_TOKEN_SECRET": "b825234d450139f812cfd83e45d306172539607e815c48cf1d",
		//"REFRESH_TOKEN_SECRET": "dc2f75f83ce1f0403f0fc0572efd4bb1477b212a382b952cce6391ebfdd2e71c96a0c10089b90048",
		//"PAYPAL_CLIENT_ID": "AfGpUJHDDbQYnBia9ZWfxzuf4vX5jo1HqPnd2lGL_tWCLRiY1wIVqarspZYDXLaGskSUqCrnb8f8KgPX",
		//"CLOUD_UPDATE_PRESET": "next_store",
		//"CLOUD_NAME": "dwte8omc0",
		//"CLOUD_API": "https://api.cloudinary.com/v1_1/dwte8omc0/image/upload"
	}
}
--#

--% cli
welcome to register baby!
--#
