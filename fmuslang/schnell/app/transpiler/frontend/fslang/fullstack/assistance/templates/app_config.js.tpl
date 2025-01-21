const config = {
  backend: {
    // host: 'localhost',
    host: '__IF_ETH0',
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

__TEMPLATE_APP_CONFIG

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
