const config = {
  backend: {
    // host: 'localhost',
    host: '__IF_ETH0',
    port: __TEMPLATE_SERVER_PORT,

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

__TEMPLATE_APP_CONFIG
			// additional paths
      static_images: {
        // config.serverPath(config.backend.paths.static_images.path + product.image),
        path: 'static/images',
      },
			productTop: {
				// config.serverPath(config.backend.paths.productTop.path),
				path: 'api/products/top/',
				method: 'GET',
			},
			// config.serverPath(config.backend.paths.productReview(productId)),
			productReview: (productId) => `/api/products/${productId}/reviews/`,

      addToCart: {
        // config.serverPath(config.backend.paths.addToCart.path + `${id}/`),
        path: 'api/products/',
        method: 'GET',
      },
      listMyOrders: {
        // config.serverPath(config.backend.paths.listMyOrders.path),
        path: 'api/orders/myorders/',
        method: 'GET',
      },
      // config.backend.paths.deliverOrder(order),
      deliverOrder: (order) => this.serverPath(`api/orders/${order._id}/deliver/`),
      // config.backend.paths.payOrder(id),
      payOrder: (id) => this.serverPath(`api/orders/${id}/pay/`),
      updateUserProfile: {
        // config.serverPath(config.backend.paths.updateUserProfile.path),
        path: 'api/users/profile/update/',
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
