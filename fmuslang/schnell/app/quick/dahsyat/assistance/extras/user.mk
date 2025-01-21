--% index/fmus
.,d
	userActions.js,f(e=__FILE__=/userActions.js)	
	userConstants.js,f(e=__FILE__=/userConstants.js)	
	userReducers.js,f(e=__FILE__=/userReducers.js)	
--#

--% /userActions.js

export const login = (email, password) => async (dispatch) => {
	try {
		dispatch({ type: USER_LOGIN_REQUEST })

		const { data } = await axios.post(
			'/api/users/login/',
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
	dispatch({ type: USER_DETAILS_RESET })
	// dispatch({ type: ORDER_LIST_MY_RESET })
	dispatch({ type: USER_LIST_RESET })
}


export const updateUserProfile = (user) => async (dispatch, getState) => {
	try {
		dispatch({ type: USER_UPDATE_PROFILE_REQUEST })

		const { userLogin: { userInfo }, } = getState()

		const { data } = await axios.put(
				`/api/users/profile/update/`,
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

--% /userConstants.js
export const USER_LOGIN_REQUEST = 'USER_LOGIN_REQUEST'
export const USER_LOGIN_SUCCESS = 'USER_LOGIN_SUCCESS'
export const USER_LOGIN_FAIL = 'USER_LOGIN_FAIL'
export const USER_LOGOUT = 'USER_LOGOUT'

export const USER_UPDATE_PROFILE_REQUEST = 'USER_UPDATE_PROFILE_REQUEST'
export const USER_UPDATE_PROFILE_SUCCESS = 'USER_UPDATE_PROFILE_SUCCESS'
export const USER_UPDATE_PROFILE_FAIL = 'USER_UPDATE_PROFILE_FAIL'
export const USER_UPDATE_PROFILE_RESET = 'USER_UPDATE_PROFILE_RESET'
--#

--% /userReducers.js
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
