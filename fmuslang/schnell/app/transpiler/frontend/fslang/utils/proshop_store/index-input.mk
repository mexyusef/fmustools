
--% index/fmus
proshop,d(/mk)
	%__TEMPLATE_SERVER_PORT=__NILAI_SERVER_PORT__
	src/store,d(/mk)
		config.js,f(e=__FILE__=/tmp/rework/store/config.js)
		index.js,f(e=__FILE__=/tmp/rework/store/index.js)
__TEMPLATE_APP_CONTENT
	src/store,d(/mk)
		# .,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_store/tambahan.mk=index/fmus*)
		user,d(/mk)
			userActions.js,f(t=)
			userActions.js,f(f=userActions.js,@ia=tambahan_user_action="akhir file actions")
			userActions.js,f(f=userActions.js,@ia=import_user_action="akhir import actions")
			userConstants.js,f(f=userConstants.js,@ia=tambahan_user_constant="akhir file constants")
			userReducers.js,f(f=userReducers.js,@ia=tambahan_user_reducer="akhir file reducers")
			userReducers.js,f(f=userReducers.js,@ia=import_user_reducer="akhir import reducers")
			userActions.js,f(f=userActions.js,@ia=user_action_extra_imports="// extra imports")
			userActions.js,f(f=userActions.js,@rm=1="Authorization: `Bearer")
		order,d(/mk)
			orderActions.js,f(t=)
			orderActions.js,f(f=orderActions.js,@ia=tambahan_order_action="akhir file actions")
			orderActions.js,f(f=orderActions.js,@ia=import_order_action="akhir import actions")
			orderConstants.js,f(f=orderConstants.js,@ia=tambahan_order_constant="akhir file constants")
			orderReducers.js,f(f=orderReducers.js,@ia=tambahan_order_reducer="akhir file reducers")
			orderReducers.js,f(f=orderReducers.js,@ia=import_order_reducer="akhir import reducers")
			orderActions.js,f(f=orderActions.js,@ia=order_action_extra_imports="// extra imports")
			orderActions.js,f(f=orderActions.js,@ia=order_action_extra_create="// extra create")
		product,d(/mk)
			productActions.js,f(t=)
			productActions.js,f(f=productActions.js,@ia=tambahan_product_action="akhir file actions")
			productActions.js,f(f=productActions.js,@ia=import_product_action="akhir import actions")
			productConstants.js,f(f=productConstants.js,@ia=tambahan_product_constant="akhir file constants")
			productReducers.js,f(f=productReducers.js,@ia=tambahan_product_reducer="akhir file reducers")
			productReducers.js,f(f=productReducers.js,@ia=import_product_reducer="akhir import reducers")
			productReducers.js,f(f=productReducers.js,@ra=replacing_product_detail_reducer_params="export const productDetailReducer =")
		cart,d(/mk)
			cartActions.js,f(t=)
			cartActions.js,f(f=cartActions.js,@ia=tambahan_cart_action="akhir file actions")
			cartActions.js,f(f=cartActions.js,@ia=import_cart_action="akhir import actions")
			cartConstants.js,f(f=cartConstants.js,@ia=tambahan_cart_constant="akhir file constants")
			cartReducers.js,f(f=cartReducers.js,@ia=tambahan_cart_reducer="akhir file reducers")
			cartReducers.js,f(f=cartReducers.js,@ia=import_cart_reducer="akhir import reducers")
	src,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/utils/proshop_store/tambahan.mk=index/fmus*)
--#

--% order_action_extra_create
    dispatch({
      type: CART_CLEAR_ITEMS,
      payload: data
    })
    localStorage.removeItem('cartItems')
--#

--% order_action_extra_imports
import { CART_CLEAR_ITEMS } from '../cart/cartConstants'
--#

--% user_action_extra_imports
import { ORDER_LIST_MY_RESET } from '../order/orderConstants'
--#

--% replacing_product_detail_reducer_params
export const productDetailReducer = (state = { product: { reviews: [] } }, action) => {
--#

--% import_order_action
	ORDER_PAY_REQUEST,
	ORDER_PAY_SUCCESS,
	ORDER_PAY_FAIL,
	ORDER_PAY_RESET,

	ORDER_LIST_MY_REQUEST,
	ORDER_LIST_MY_SUCCESS,
	ORDER_LIST_MY_FAIL,
	ORDER_LIST_MY_RESET,

	ORDER_DELIVER_REQUEST,
	ORDER_DELIVER_SUCCESS,
	ORDER_DELIVER_FAIL,
	ORDER_DELIVER_RESET,
--#

--% import_order_reducer
	ORDER_PAY_REQUEST,
	ORDER_PAY_SUCCESS,
	ORDER_PAY_FAIL,
	ORDER_PAY_RESET,

	ORDER_LIST_MY_REQUEST,
	ORDER_LIST_MY_SUCCESS,
	ORDER_LIST_MY_FAIL,
	ORDER_LIST_MY_RESET,
	
	ORDER_DELIVER_REQUEST,
	ORDER_DELIVER_SUCCESS,
	ORDER_DELIVER_FAIL,
	ORDER_DELIVER_RESET,
--#

--% import_product_action
	PRODUCT_CREATE_REVIEW_REQUEST,
	PRODUCT_CREATE_REVIEW_SUCCESS,
	PRODUCT_CREATE_REVIEW_FAIL,
	PRODUCT_CREATE_REVIEW_RESET,

	PRODUCT_TOP_REQUEST,
	PRODUCT_TOP_SUCCESS,
	PRODUCT_TOP_FAIL,
--#

--% import_product_reducer
	PRODUCT_CREATE_REVIEW_REQUEST,
	PRODUCT_CREATE_REVIEW_SUCCESS,
	PRODUCT_CREATE_REVIEW_FAIL,
	PRODUCT_CREATE_REVIEW_RESET,

	PRODUCT_TOP_REQUEST,
	PRODUCT_TOP_SUCCESS,
	PRODUCT_TOP_FAIL,
--#

--% import_cart_action
	CART_ADD_ITEM,
	CART_REMOVE_ITEM,
	CART_CLEAR_ITEMS,

	CART_SAVE_SHIPPING_ADDRESS,
	CART_SAVE_PAYMENT_METHOD,
--#

--% import_cart_reducer
	CART_ADD_ITEM,
	CART_REMOVE_ITEM,
	CART_CLEAR_ITEMS,

	CART_SAVE_SHIPPING_ADDRESS,
	CART_SAVE_PAYMENT_METHOD,
--#

--% tambahan_order_action
export const payOrder = (id, paymentResult) => async (dispatch, getState) => {
	try {
		dispatch({ type: ORDER_PAY_REQUEST })

		const { userLogin: { userInfo }, } = getState()

		const { data } = await axios.put(
			`/api/orders/${id}/pay/`,
			paymentResult,
			{
				headers: {
					'Content-type': 'application/json',
					Authorization: `Bearer ${userInfo.token}`
				}
			}
		)

		dispatch({ type: ORDER_PAY_SUCCESS, payload: data })

	} catch (error) {
		dispatch({
			type: ORDER_PAY_FAIL,
			payload: error.response && error.response.data.detail
				? error.response.data.detail
				: error.message,
		})
	}
}

export const deliverOrder = (order) => async (dispatch, getState) => {
	try {
		dispatch({ type: ORDER_DELIVER_REQUEST })

		const { userLogin: { userInfo }, } = getState()

		const { data } = await axios.put(
			`/api/orders/${order._id}/deliver/`,
			{},
			{
				headers: {
					'Content-type': 'application/json',
					Authorization: `Bearer ${userInfo.token}`
				}
			}
		)

		dispatch({ type: ORDER_DELIVER_SUCCESS, payload: data })

	} catch (error) {
		dispatch({
			type: ORDER_DELIVER_FAIL,
			payload: error.response && error.response.data.detail
				? error.response.data.detail
				: error.message,
		})
	}
}

export const listMyOrders = () => async (dispatch, getState) => {
	try {
		dispatch({ type: ORDER_LIST_MY_REQUEST })

		const { userLogin: { userInfo }, } = getState()

		const { data } = await axios.get(
			`/api/orders/myorders/`,
			{
				headers: {
					'Content-type': 'application/json',
					Authorization: `Bearer ${userInfo.token}`
				}
			}
		)

		dispatch({ type: ORDER_LIST_MY_SUCCESS, payload: data })

	} catch (error) {
		dispatch({
			type: ORDER_LIST_MY_FAIL,
			payload: error.response && error.response.data.detail
				? error.response.data.detail
				: error.message,
		})
	}
}
--#

--% tambahan_order_constant
export const ORDER_DELIVER_REQUEST = 'ORDER_DELIVER_REQUEST'
export const ORDER_DELIVER_SUCCESS = 'ORDER_DELIVER_SUCCESS'
export const ORDER_DELIVER_FAIL = 'ORDER_DELIVER_FAIL'
export const ORDER_DELIVER_RESET = 'ORDER_DELIVER_RESET'

export const ORDER_PAY_REQUEST = 'ORDER_PAY_REQUEST'
export const ORDER_PAY_SUCCESS = 'ORDER_PAY_SUCCESS'
export const ORDER_PAY_FAIL = 'ORDER_PAY_FAIL'
export const ORDER_PAY_RESET = 'ORDER_PAY_RESET'

export const ORDER_LIST_MY_REQUEST = 'ORDER_LIST_MY_REQUEST'
export const ORDER_LIST_MY_SUCCESS = 'ORDER_LIST_MY_SUCCESS'
export const ORDER_LIST_MY_FAIL = 'ORDER_LIST_MY_FAIL'
export const ORDER_LIST_MY_RESET = 'ORDER_LIST_MY_RESET'
--#

--% tambahan_order_reducer
export const orderPayReducer = (state = {}, action) => {
	switch (action.type) {
		case ORDER_PAY_REQUEST:
			return {
				loading: true
			}

		case ORDER_PAY_SUCCESS:
			return {
				loading: false,
				success: true
			}

		case ORDER_PAY_FAIL:
			return {
				loading: false,
				error: action.payload
			}

		case ORDER_PAY_RESET:
			return {}

		default:
			return state
	}
}

export const orderDeliverReducer = (state = {}, action) => {
	switch (action.type) {
		case ORDER_DELIVER_REQUEST:
			return {
				loading: true
			}

		case ORDER_DELIVER_SUCCESS:
			return {
				loading: false,
				success: true
			}

		case ORDER_DELIVER_FAIL:
			return {
				loading: false,
				error: action.payload
			}

		case ORDER_DELIVER_RESET:
			return {}

		default:
			return state
	}
}

export const orderListMyReducer = (state = { orders: [] }, action) => {
	switch (action.type) {
		case ORDER_LIST_MY_REQUEST:
			return {
				loading: true
			}

		case ORDER_LIST_MY_SUCCESS:
			return {
				loading: false,
				orders: action.payload
			}

		case ORDER_LIST_MY_FAIL:
			return {
				loading: false,
				error: action.payload
			}

		case ORDER_LIST_MY_RESET:
			return {
				orders: []
			}

		default:
			return state
	}
}
--#

--% tambahan_product_action
export const listTopProducts = () => async (dispatch) => {
	try {
		dispatch({ type: PRODUCT_TOP_REQUEST })

		const { data } = await axios.get(
      // `/api/products/top/`,
      config.serverPath(config.backend.paths.productTop.path),
    )

		dispatch({ type: PRODUCT_TOP_SUCCESS, payload: data })
	} catch (error) {
		dispatch({
			type: PRODUCT_TOP_FAIL,
			payload: error.response && error.response.data.detail
				? error.response.data.detail
				: error.message,
		})
	}
}

export const createProductReview = (productId, review) => async (dispatch, getState) => {
	try {
		dispatch({ type: PRODUCT_CREATE_REVIEW_REQUEST })

		const { userLogin: { userInfo }, } = getState()

		const { data } = await axios.post(
			// `/api/products/${productId}/reviews/`,
      config.serverPath(config.backend.paths.productReview(productId)),
			review,
			{
				headers: {
					'Content-type': 'application/json',
					Authorization: `Bearer ${userInfo.token}`
				}
			}
		)

		dispatch({ type: PRODUCT_CREATE_REVIEW_SUCCESS, payload: data, })

	} catch (error) {
		dispatch({
			type: PRODUCT_CREATE_REVIEW_FAIL,
			payload: error.response && error.response.data.detail
				? error.response.data.detail
				: error.message,
		})
	}
}
--#

--% tambahan_product_constant
export const PRODUCT_CREATE_REVIEW_REQUEST = 'PRODUCT_CREATE_REVIEW_REQUEST'
export const PRODUCT_CREATE_REVIEW_SUCCESS = 'PRODUCT_CREATE_REVIEW_SUCCESS'
export const PRODUCT_CREATE_REVIEW_FAIL = 'PRODUCT_CREATE_REVIEW_FAIL'
export const PRODUCT_CREATE_REVIEW_RESET = 'PRODUCT_CREATE_REVIEW_RESET'

export const PRODUCT_TOP_REQUEST = 'PRODUCT_TOP_REQUEST'
export const PRODUCT_TOP_SUCCESS = 'PRODUCT_TOP_SUCCESS'
export const PRODUCT_TOP_FAIL = 'PRODUCT_TOP_FAIL'
--#

--% tambahan_product_reducer
export const productReviewCreateReducer = (state = {}, action) => {
	switch (action.type) {
		case PRODUCT_CREATE_REVIEW_REQUEST:
			return { loading: true }

		case PRODUCT_CREATE_REVIEW_SUCCESS:
			return { loading: false, success: true, }

		case PRODUCT_CREATE_REVIEW_FAIL:
			return { loading: false, error: action.payload }

		case PRODUCT_CREATE_REVIEW_RESET:
			return {}

		default:
			return state
	}
}

export const productTopRatedReducer = (state = { products: [] }, action) => {
	switch (action.type) {
		case PRODUCT_TOP_REQUEST:
			return { loading: true, products: [] }

		case PRODUCT_TOP_SUCCESS:
			return { loading: false, products: action.payload, }

		case PRODUCT_TOP_FAIL:
			return { loading: false, error: action.payload }

		default:
			return state
	}
}
--#

--% tambahan_cart_action
export const addToCart = (id, qty) => async (dispatch, getState) => {
	const { data } = await axios.get(
    // `/api/products/${id}`
    config.serverPath(config.backend.paths.productDetail.path + id)
  )

	dispatch({
		type: CART_ADD_ITEM,
		payload: {
			product: data._id,
			name: data.name,
			image: data.image,
			price: data.price,
			countInStock: data.countInStock,
			qty
		}
	})
	localStorage.setItem('cartItems', JSON.stringify(getState().cart.cartItems))
}

export const removeFromCart = (id) => (dispatch, getState) => {
	dispatch({ type: CART_REMOVE_ITEM, payload: id, })
	localStorage.setItem('cartItems', JSON.stringify(getState().cart.cartItems))
}

export const saveShippingAddress = (data) => (dispatch) => {
	dispatch({ type: CART_SAVE_SHIPPING_ADDRESS, payload: data, })
	localStorage.setItem('shippingAddress', JSON.stringify(data))
}

export const savePaymentMethod = (data) => (dispatch) => {
	dispatch({ type: CART_SAVE_PAYMENT_METHOD, payload: data, })
	localStorage.setItem('paymentMethod', JSON.stringify(data))
}
--#

--% tambahan_cart_constant
export const CART_ADD_ITEM = 'CART_ADD_ITEM'
export const CART_REMOVE_ITEM = 'CART_REMOVE_ITEM'
export const CART_CLEAR_ITEMS = 'CART_CLEAR_ITEMS'

export const CART_SAVE_SHIPPING_ADDRESS = 'CART_SAVE_SHIPPING_ADDRESS'

export const CART_SAVE_PAYMENT_METHOD = 'CART_SAVE_PAYMENT_METHOD'
--#

--% tambahan_cart_reducer
export const cartReducer = (state = { cartItems: [], shippingAddress: {} }, action) => {
	switch (action.type) {
		case CART_ADD_ITEM:
			const item = action.payload
			const existItem = state.cartItems.find(x => x.product === item.product)

			if (existItem) {
				return {
					...state,
					cartItems: state.cartItems.map(x => x.product === existItem.product ? item : x)
				}

			} else {
				return {
					...state,
					cartItems: [...state.cartItems, item]
				}
			}

		case CART_REMOVE_ITEM:
			return {
				...state,
				cartItems: state.cartItems.filter(x => x.product !== action.payload)
			}

		case CART_SAVE_SHIPPING_ADDRESS:
			return {
				...state,
				shippingAddress: action.payload
			}

		case CART_SAVE_PAYMENT_METHOD:
			return {
				...state,
				paymentMethod: action.payload
			}

		case CART_CLEAR_ITEMS:
			return {
				...state,
				cartItems: []
			}

		default:
			return state
	}
}
--#

--% import_user_action
	USER_LOGIN_REQUEST,
	USER_LOGIN_SUCCESS,
	USER_LOGIN_FAIL,
	USER_LOGOUT,

	USER_UPDATE_PROFILE_REQUEST,
	USER_UPDATE_PROFILE_SUCCESS,
	USER_UPDATE_PROFILE_FAIL,
	USER_UPDATE_PROFILE_RESET,
--#

--% import_user_reducer
	USER_LOGIN_REQUEST,
	USER_LOGIN_SUCCESS,
	USER_LOGIN_FAIL,
	USER_LOGOUT,

	USER_UPDATE_PROFILE_REQUEST,
	USER_UPDATE_PROFILE_SUCCESS,
	USER_UPDATE_PROFILE_FAIL,
	USER_UPDATE_PROFILE_RESET,
--#

--% tambahan_user_action
export const login = (email, password) => async (dispatch) => {
	try {
		dispatch({ type: USER_LOGIN_REQUEST })

		const { data } = await axios.post(
			// '/api/users/login/',
      config.serverPath(config.backend.paths.login.path),
			{ 'username': email, 'password': password },
			{ headers: { 'Content-type': 'application/json' } }
		)

		dispatch({ type: USER_LOGIN_SUCCESS, payload: data })

		localStorage.setItem('userInfo', JSON.stringify(data))

	} catch (error) {
		dispatch({
			type: USER_LOGIN_FAIL,
			payload: error.response && error.response.data.detail
				? error.response.data.detail
				: error.message,
		})
	}
}

export const logout = () => (dispatch) => {
	localStorage.removeItem('userInfo')
	dispatch({ type: USER_LOGOUT })
	dispatch({ type: USER_DETAIL_RESET })
	dispatch({ type: ORDER_LIST_MY_RESET })
	dispatch({ type: USER_LIST_RESET })
}

export const updateUserProfile = (user) => async (dispatch, getState) => {
	try {
		dispatch({ type: USER_UPDATE_PROFILE_REQUEST })

		const { userLogin: { userInfo }, } = getState()

		const { data } = await axios.put(
				// `/api/users/profile/update/`,
        config.serverPath(config.backend.paths.updateUserProfile.path),
				user,
				{
					headers: {
						'Content-type': 'application/json',
						Authorization: `Bearer ${userInfo.token}`
					}
				}
		)

		dispatch({ type: USER_UPDATE_PROFILE_SUCCESS, payload: data })

		dispatch({ type: USER_LOGIN_SUCCESS, payload: data })

		localStorage.setItem('userInfo', JSON.stringify(data))

	} catch (error) {
		dispatch({
			type: USER_UPDATE_PROFILE_FAIL,
			payload: error.response && error.response.data.detail
				? error.response.data.detail
				: error.message,
		})
	}
}
--#

--% tambahan_user_constant
export const USER_LOGIN_REQUEST = 'USER_LOGIN_REQUEST'
export const USER_LOGIN_SUCCESS = 'USER_LOGIN_SUCCESS'
export const USER_LOGIN_FAIL = 'USER_LOGIN_FAIL'
export const USER_LOGOUT = 'USER_LOGOUT'

export const USER_UPDATE_PROFILE_REQUEST = 'USER_UPDATE_PROFILE_REQUEST'
export const USER_UPDATE_PROFILE_SUCCESS = 'USER_UPDATE_PROFILE_SUCCESS'
export const USER_UPDATE_PROFILE_FAIL = 'USER_UPDATE_PROFILE_FAIL'
export const USER_UPDATE_PROFILE_RESET = 'USER_UPDATE_PROFILE_RESET'
--#

--% tambahan_user_reducer
export const userLoginReducer = (state = {}, action) => {
	switch (action.type) {
		case USER_LOGIN_REQUEST:
			return { loading: true }

		case USER_LOGIN_SUCCESS:
			return { loading: false, userInfo: action.payload }

		case USER_LOGIN_FAIL:
			return { loading: false, error: action.payload }

		case USER_LOGOUT:
			return {}

		default:
			return state
	}
}

export const userUpdateProfileReducer = (state = {}, action) => {
	switch (action.type) {
		case USER_UPDATE_PROFILE_REQUEST:
			return { loading: true }

		case USER_UPDATE_PROFILE_SUCCESS:
			return { loading: false, success: true, userInfo: action.payload }

		case USER_UPDATE_PROFILE_FAIL:
			return { loading: false, error: action.payload }

		case USER_UPDATE_PROFILE_RESET:
			return {}

		default:
			return state
	}
}
--#
