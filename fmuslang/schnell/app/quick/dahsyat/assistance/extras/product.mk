--% index/fmus
.,d
	productActions.js,f(e=__FILE__=/productActions.js)	
	productConstants.js,f(e=__FILE__=/productConstants.js)	
	productReducers.js,f(e=__FILE__=/productReducers.js)	
--#

--% /productActions.js
export const createProductReview = (productId, review) => async (dispatch, getState) => {
	try {
		dispatch({ type: PRODUCT_CREATE_REVIEW_REQUEST })

		const { userLogin: { userInfo }, } = getState()

		const { data } = await axios.post(
			`/api/products/${productId}/reviews/`,
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

export const listTopProducts = () => async (dispatch) => {
	try {
		dispatch({ type: PRODUCT_TOP_REQUEST })

		const { data } = await axios.get(`/api/products/top/`)

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

--#

--% /productConstants.js
export const PRODUCT_CREATE_REVIEW_REQUEST = 'PRODUCT_CREATE_REVIEW_REQUEST'
export const PRODUCT_CREATE_REVIEW_SUCCESS = 'PRODUCT_CREATE_REVIEW_SUCCESS'
export const PRODUCT_CREATE_REVIEW_FAIL = 'PRODUCT_CREATE_REVIEW_FAIL'
export const PRODUCT_CREATE_REVIEW_RESET = 'PRODUCT_CREATE_REVIEW_RESET'

export const PRODUCT_TOP_REQUEST = 'PRODUCT_TOP_REQUEST'
export const PRODUCT_TOP_SUCCESS = 'PRODUCT_TOP_SUCCESS'
export const PRODUCT_TOP_FAIL = 'PRODUCT_TOP_FAIL'
export const PRODUCT_TOP_RESET = 'PRODUCT_TOP_RESET'
--#

--% /productReducers.js
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
