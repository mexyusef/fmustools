--% index/fmus
store,d(/mk)
	%utama=__FILE__
	config.js,f(e=utama=/tmp/rework/store/config.js)
	index.js,f(e=utama=/tmp/rework/store/index.js)
	product,d(/mk)
		productActions.js,f(e=utama=/tmp/rework/store/product/productActions.js)
		productConstants.js,f(e=utama=/tmp/rework/store/product/productConstants.js)
		productReducers.js,f(e=utama=/tmp/rework/store/product/productReducers.js)
--#

--% /tmp/rework/store/config.js
const config = {
  backend: {
    // host: 'localhost',
    host: '172.31.164.237',
    port: 7201,

    paths: {
      login: {
        path: '/api/users/login/',
        method: 'POST',
      },
      logout: {
        path: 'api/users/logout',
        method: 'POST',
      },
      register: {
        path: 'api/users/register',
        method: 'POST',
      },
      forgot: {
        path: 'api/users/forgot',
        method: 'POST',
      },
      update: {
        path: 'api/users/update_password',
        method: 'POST',
      },

      productCreate: {
        // config.serverPath(config.backend.paths.productCreate.path),
        path: 'api/products/create/',
        method: 'GET',
      },
      productList: {
        // config.serverPath(config.backend.paths.productList.path + `${keyword}`),
        path: 'api/products/',
        method: 'GET',
      },
      productDetail: {
        // config.serverPath(config.backend.paths.productDetail.path + `${id}/`),
        path: 'api/products/',
        method: 'GET',
      },
      productUpdate: {
        // config.serverPath(config.backend.paths.productUpdate.path + `${product._id}`),
        path: '/api/products/update/',
        method: 'PUT',
      },
      productDelete: {
        // config.serverPath(config.backend.paths.productDelete.path + `${id}/`),
        path: 'api/products/delete/',
        method: 'GET',
      },
    },

  },
};

config.server = () => `http://${config.backend.host}:${config.backend.port}`;
config.serverPath = (path) => {
  let fullpath = path;
  if (path && !path.startsWith('/')) fullpath = '/' + fullpath;
  return `http://${config.backend.host}:${config.backend.port}${fullpath}`;
}

export default config;
--#

--% /tmp/rework/store/index.js
import { createStore, combineReducers, applyMiddleware } from 'redux'
import thunk from 'redux-thunk'
import { composeWithDevTools } from 'redux-devtools-extension'
import {
  productCreateReducer,
  productListReducer,
  productDetailReducer,
  productUpdateReducer,
  productDeleteReducer,
} from './product/productReducers'

const reducer = combineReducers({
  productCreateReducer: productCreateReducer,
  productListReducer: productListReducer,
  productDetailReducer: productDetailReducer,
  productUpdateReducer: productUpdateReducer,
  productDeleteReducer: productDeleteReducer,
})

const cartItemsFromStorage = localStorage.getItem('cartItems') ?
  JSON.parse(localStorage.getItem('cartItems')) : []

const shippingAddressFromStorage = localStorage.getItem('shippingAddress') ?
  JSON.parse(localStorage.getItem('shippingAddress')) : {}

const userInfoFromStorage = localStorage.getItem('userInfo') ?
  JSON.parse(localStorage.getItem('userInfo')) : null

  const initialState = {
  cart: {
    cartItems: cartItemsFromStorage,
    shippingAddress: shippingAddressFromStorage,
  },
  userLogin: { userInfo: userInfoFromStorage },
}

const middleware = [thunk]

const store = createStore(reducer, initialState,
  composeWithDevTools(applyMiddleware(...middleware)))

export default store
--#

--% /tmp/rework/store/product/productActions.js
import axios from 'axios'
import config from '../config'
import {
  PRODUCT_CREATE_REQUEST,
  PRODUCT_CREATE_SUCCESS,
  PRODUCT_CREATE_FAIL,
  PRODUCT_CREATE_RESET,

  PRODUCT_LIST_REQUEST,
  PRODUCT_LIST_SUCCESS,
  PRODUCT_LIST_FAIL,
  PRODUCT_LIST_RESET,

  PRODUCT_DETAIL_REQUEST,
  PRODUCT_DETAIL_SUCCESS,
  PRODUCT_DETAIL_FAIL,
  PRODUCT_DETAIL_RESET,

  PRODUCT_UPDATE_REQUEST,
  PRODUCT_UPDATE_SUCCESS,
  PRODUCT_UPDATE_FAIL,
  PRODUCT_UPDATE_RESET,

  PRODUCT_DELETE_REQUEST,
  PRODUCT_DELETE_SUCCESS,
  PRODUCT_DELETE_FAIL,
  PRODUCT_DELETE_RESET,

} from './productConstants'

export const productCreate = () => async (dispatch, getState) => {
  try {
    dispatch({
      type: PRODUCT_CREATE_REQUEST
    })
    const {
      userLogin: { userInfo },
    } = getState()
    const { data } = await axios.post(
      config.serverPath(config.backend.paths.productCreate.path),
      {},
      {
        headers: {
          'Content-type': 'application/json',
          Authorization: `Bearer ${userInfo.token}`
        }
      },
    )
    dispatch({
      type: PRODUCT_CREATE_SUCCESS,
      payload: data,
    })
  } catch (error) {
    dispatch({
      type: PRODUCT_CREATE_FAIL,
      payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message,
    })
  }
}

export const productList = () => async (dispatch) => {
  try {
    dispatch({
      type: PRODUCT_LIST_REQUEST
    })
    // const {
    //   userLogin: { userInfo },
    // } = getState()
    const { data } = await axios.get(
      config.serverPath(config.backend.paths.productList.path),
      // {},
      // {
      //   headers: {
      //     'Content-type': 'application/json',
      //     Authorization: `Bearer ${userInfo.token}`
      //   }
      // },
    )
    dispatch({
      type: PRODUCT_LIST_SUCCESS,
      payload: data,
    })
  } catch (error) {
    dispatch({
      type: PRODUCT_LIST_FAIL,
      payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message,
    })
  }
}

export const productDetail = (id) => async (dispatch) => {
  try {
    dispatch({
      type: PRODUCT_DETAIL_REQUEST
    })
    // const {
    //   userLogin: { userInfo },
    // } = getState()
    const { data } = await axios.get(
      config.serverPath(config.backend.paths.productDetail.path + id),
      // {},
      // {
      //   headers: {
      //     'Content-type': 'application/json',
      //     Authorization: `Bearer ${userInfo.token}`
      //   }
      // },
    )
    dispatch({
      type: PRODUCT_DETAIL_SUCCESS,
      payload: data,
    })
  } catch (error) {
    dispatch({
      type: PRODUCT_DETAIL_FAIL,
      payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message,
    })
  }
}

export const productUpdate = (product) => async (dispatch, getState) => {
  try {
    dispatch({
      type: PRODUCT_UPDATE_REQUEST
    })
    const {
      userLogin: { userInfo },
    } = getState()
    const { data } = await axios.put(
      config.serverPath(config.backend.paths.productUpdate.path + product.id),
      product,
      {
        headers: {
          'Content-type': 'application/json',
          Authorization: `Bearer ${userInfo.token}`
        }
      },
    )
    dispatch({
      type: PRODUCT_UPDATE_SUCCESS,
      payload: data,
    })
  } catch (error) {
    dispatch({
      type: PRODUCT_UPDATE_FAIL,
      payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message,
    })
  }
}

export const productDelete = (id) => async (dispatch, getState) => {
  try {
    dispatch({
      type: PRODUCT_DELETE_REQUEST
    })
    const {
      userLogin: { userInfo },
    } = getState()
    const { data } = await axios.delete(
      config.serverPath(config.backend.paths.productDelete.path + id),
      // {},
      {
        headers: {
          'Content-type': 'application/json',
          Authorization: `Bearer ${userInfo.token}`
        }
      },
    )
    dispatch({
      type: PRODUCT_DELETE_SUCCESS,
      payload: data,
    })
  } catch (error) {
    dispatch({
      type: PRODUCT_DELETE_FAIL,
      payload: error.response && error.response.data.detail
        ? error.response.data.detail
        : error.message,
    })
  }
}

--#

--% /tmp/rework/store/product/productConstants.js
export const PRODUCT_CREATE_REQUEST   = 'PRODUCT_CREATE_REQUEST'
export const PRODUCT_CREATE_SUCCESS   = 'PRODUCT_CREATE_SUCCESS'
export const PRODUCT_CREATE_FAIL      = 'PRODUCT_CREATE_FAIL'
export const PRODUCT_CREATE_RESET     = 'PRODUCT_CREATE_RESET'

export const PRODUCT_LIST_REQUEST     = 'PRODUCT_LIST_REQUEST'
export const PRODUCT_LIST_SUCCESS     = 'PRODUCT_LIST_SUCCESS'
export const PRODUCT_LIST_FAIL        = 'PRODUCT_LIST_FAIL'
export const PRODUCT_LIST_RESET       = 'PRODUCT_LIST_RESET'

export const PRODUCT_DETAIL_REQUEST   = 'PRODUCT_DETAIL_REQUEST'
export const PRODUCT_DETAIL_SUCCESS   = 'PRODUCT_DETAIL_SUCCESS'
export const PRODUCT_DETAIL_FAIL      = 'PRODUCT_DETAIL_FAIL'
export const PRODUCT_DETAIL_RESET     = 'PRODUCT_DETAIL_RESET'

export const PRODUCT_UPDATE_REQUEST   = 'PRODUCT_UPDATE_REQUEST'
export const PRODUCT_UPDATE_SUCCESS   = 'PRODUCT_UPDATE_SUCCESS'
export const PRODUCT_UPDATE_FAIL      = 'PRODUCT_UPDATE_FAIL'
export const PRODUCT_UPDATE_RESET     = 'PRODUCT_UPDATE_RESET'

export const PRODUCT_DELETE_REQUEST   = 'PRODUCT_DELETE_REQUEST'
export const PRODUCT_DELETE_SUCCESS   = 'PRODUCT_DELETE_SUCCESS'
export const PRODUCT_DELETE_FAIL      = 'PRODUCT_DELETE_FAIL'
export const PRODUCT_DELETE_RESET     = 'PRODUCT_DELETE_RESET'

--#

--% /tmp/rework/store/product/productReducers.js
import {
  PRODUCT_CREATE_REQUEST,
  PRODUCT_CREATE_SUCCESS,
  PRODUCT_CREATE_FAIL,
  PRODUCT_CREATE_RESET,

  PRODUCT_LIST_REQUEST,
  PRODUCT_LIST_SUCCESS,
  PRODUCT_LIST_FAIL,
  PRODUCT_LIST_RESET,

  PRODUCT_DETAIL_REQUEST,
  PRODUCT_DETAIL_SUCCESS,
  PRODUCT_DETAIL_FAIL,
  PRODUCT_DETAIL_RESET,

  PRODUCT_UPDATE_REQUEST,
  PRODUCT_UPDATE_SUCCESS,
  PRODUCT_UPDATE_FAIL,
  PRODUCT_UPDATE_RESET,

  PRODUCT_DELETE_REQUEST,
  PRODUCT_DELETE_SUCCESS,
  PRODUCT_DELETE_FAIL,
  PRODUCT_DELETE_RESET,

} from './productConstants'

export const productCreateReducer = (state = {}, action) => {
  switch (action.type) {
    case PRODUCT_CREATE_REQUEST:
      return { loading: true }
    case PRODUCT_CREATE_SUCCESS:
      return { loading: false, success: true, product: action.payload }
    case PRODUCT_CREATE_FAIL:
      return { loading: false, error: action.payload }
    case PRODUCT_CREATE_RESET:
      return {}
    default:
      return state    
  }
}

export const productListReducer = (state = { products: []}, action) => {
  switch (action.type) {
    case PRODUCT_LIST_REQUEST:
      return { loading: true, products: [] }
    case PRODUCT_LIST_SUCCESS:
      return {
        loading: false,
        products: action.payload.products,
        page: action.payload.page,
        pages: action.payload.pages
      }
    case PRODUCT_LIST_FAIL:
      return { loading: false, error: action.payload }
    case PRODUCT_LIST_RESET:
      return {}
    default:
      return state    
  }
}

export const productDetailReducer = (state = { product: {} }, action) => {
  switch (action.type) {
    case PRODUCT_DETAIL_REQUEST:
      return { loading: true, ...state }
    case PRODUCT_DETAIL_SUCCESS:
      return { loading: false, product: action.payload }
    case PRODUCT_DETAIL_FAIL:
      return { loading: false, error: action.payload }
    case PRODUCT_DETAIL_RESET:
      return {}
    default:
      return state    
  }
}

export const productUpdateReducer = (state = { product: {} }, action) => {
  switch (action.type) {
    case PRODUCT_UPDATE_REQUEST:
      return { loading: true }
    case PRODUCT_UPDATE_SUCCESS:
      return { loading: false, success: true, product: action.payload }
    case PRODUCT_UPDATE_FAIL:
      return { loading: false, error: action.payload }
    case PRODUCT_UPDATE_RESET:
      return { product: {} }
    default:
      return state    
  }
}

export const productDeleteReducer = (state = {}, action) => {
  switch (action.type) {
    case PRODUCT_DELETE_REQUEST:
      return { loading: true }
    case PRODUCT_DELETE_SUCCESS:
      return { loading: false, success: true }
    case PRODUCT_DELETE_FAIL:
      return { loading: false, error: action.payload }
    case PRODUCT_DELETE_RESET:
      return {}
    default:
      return state    
  }
}

--#
