--% index/fmus
.,d
	@ready to load tambahan store/index.js untuk extra imports dan reducers*
	store,d
		index.js,f(f=index.js,@ia=extra_imports="// extra imports")
		index.js,f(f=index.js,@ia=extra_reducers="// extra reducers")
--#

--% extra_imports
import {
  orderPayReducer,
  orderListMyReducer,
  orderDeliverReducer,
} from './order/orderReducers'
import {
  productReviewCreateReducer,
  productTopRatedReducer,
} from './product/productReducers'
import {
  cartReducer,
} from './cart/cartReducers'
import {
  userUpdateProfileReducer,
  userLoginReducer,
} from './user/userReducers'
--#

--% extra_reducers
  cart: cartReducer,
  orderPay: orderPayReducer,
  orderListMy: orderListMyReducer,
  orderDeliver: orderDeliverReducer,
  productReviewCreate: productReviewCreateReducer,
  productTopRated: productTopRatedReducer,
  userUpdateProfile: userUpdateProfileReducer,
  userLogin: userLoginReducer,
--#
