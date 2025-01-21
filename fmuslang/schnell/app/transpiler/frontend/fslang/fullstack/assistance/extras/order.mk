--% index/fmus
.,d
	orderActions.js,f(e=__FILE__=/orderActions.js)	
	orderConstants.js,f(e=__FILE__=/orderConstants.js)	
	orderReducers.js,f(e=__FILE__=/orderReducers.js)	
--#

--% /orderActions.js
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

--% /orderConstants.js
export const ORDER_LIST_MY_REQUEST = 'ORDER_LIST_MY_REQUEST'
export const ORDER_LIST_MY_SUCCESS = 'ORDER_LIST_MY_SUCCESS'
export const ORDER_LIST_MY_FAIL = 'ORDER_LIST_MY_FAIL'
export const ORDER_LIST_MY_RESET = 'ORDER_LIST_MY_RESET'

export const ORDER_PAY_REQUEST = 'ORDER_PAY_REQUEST'
export const ORDER_PAY_SUCCESS = 'ORDER_PAY_SUCCESS'
export const ORDER_PAY_FAIL = 'ORDER_PAY_FAIL'
export const ORDER_PAY_RESET = 'ORDER_PAY_RESET'

export const ORDER_DELIVER_REQUEST = 'ORDER_DELIVER_REQUEST'
export const ORDER_DELIVER_SUCCESS = 'ORDER_DELIVER_SUCCESS'
export const ORDER_DELIVER_FAIL = 'ORDER_DELIVER_FAIL'
export const ORDER_DELIVER_RESET = 'ORDER_DELIVER_RESET'
--#

--% /orderReducers.js
export const orderPayReducer = (state = {}, action) => {
	switch (action.type) {
		case ORDER_PAY_REQUEST:
			return { loading: true }

		case ORDER_PAY_SUCCESS:
			return { loading: false, success: true }

		case ORDER_PAY_FAIL:
			return { loading: false, error: action.payload }

		case ORDER_PAY_RESET:
			return {}

		default:
			return state
	}
}


export const orderDeliverReducer = (state = {}, action) => {
	switch (action.type) {
		case ORDER_DELIVER_REQUEST:
			return { loading: true }

		case ORDER_DELIVER_SUCCESS:
			return { loading: false, success: true }

		case ORDER_DELIVER_FAIL:
			return { loading: false, error: action.payload }

		case ORDER_DELIVER_RESET:
			return {}

		default:
			return state
	}
}


export const orderListMyReducer = (state = { orders: [] }, action) => {
	switch (action.type) {
		case ORDER_LIST_MY_REQUEST:
			return { loading: true }

		case ORDER_LIST_MY_SUCCESS:
			return { loading: false, orders: action.payload }

		case ORDER_LIST_MY_FAIL:
			return { loading: false, error: action.payload }

		case ORDER_LIST_MY_RESET:
			return { orders: [] }

		default:
			return state
	}
}

--#
