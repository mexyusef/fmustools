--% index/fm.us
__TEMPLATE_PROJECT_DIR__,d
  %utama=__FILE__
  %__TEMPLATE_SERVER_PORT__=9501
  __TEMPLATE_WEBPACK_NAME__.js,f(e=utama=/webpack.js)
  run.sh,f(e=utama=/run.sh)
  yarn.add.sh,f(e=utama=/yarn.add.sh)
  $*chmod a+x *.sh
  __TEMPLATE_MTS_DIR__,d(/mk)
    src,d(/mk)
      $*ln -s /home/usef/tmp/react-bs/assets/ assets
      components,d(/mk)
        App,d(/mk)
          index.js,f(e=utama=/src/components/index.js)
          style.css,f(e=utama=/src/components/style.css)
        dashboard,d(/mk)
          index.js,f(e=utama=/src/components/dashboard/index.js)
        pages,d(/mk)
          not-found,d(/mk)
            index.js,f(e=utama=/src/components/pages/not-found/index.js)
        routes,d(/mk)
          index.js,f(e=utama=/src/components/routes/index.js)
      index.html,f(e=utama=/src/index.html)
      index.js,f(e=utama=/src/index.js)
  $*qterminal 2>/dev/null &
--#

--% /src/components/dashboard/index.js
import React from 'react';

const Dashboard = () => {
  return (<h1>Dashboard</h1>)
}
export default Dashboard;
--#

--% /src/components/pages/not-found/index.js
import React from 'react';

const NotFound = () => {
  return (<h1>not found!</h1>)
}
export default NotFound;
--#

--% /src/components/routes/index.js
const Routes = {
  // Presentation:         { path: "/presentation" },
  DashboardOverview:    { path: "/" },
  NotFound:             { path: "/pages/404" },
};
export default Routes;
--#

--% /src/components/index.js
import React, { useState, useEffect } from 'react';
import { Route, Switch, Redirect } from 'react-router-dom';
import { HashRouter } from "react-router-dom";
import Routes from 'routes';
import Dashboard from '@/dashboard';
import NotFoundPage from '@/pages/not-found';

const App = () => {
  return (<HashRouter>
    <ScrollToTop />
    <Switch>

      <RouteWithSidebar exact path={Routes.DashboardOverview.path} component={Dashboard} />
      <RouteWithLoader exact path={Routes.NotFound.path} component={NotFoundPage} />

      <Redirect to={Routes.NotFound.path} />
    </Switch>
  </HashRouter>);
}
export default App;
--#

--% /src/components/style.css
.main-section {
  transition: left .2s ease;
  margin-left: 0;
}

.main-section.active {
  margin-left: 256px;
}
--#

--% /yarn.add.sh
yarn add 
yarn add --dev 
--#

--% /run.sh
./node_modules/.bin/webpack serve --mode development --config __TEMPLATE_WEBPACK_NAME__
--#

--% /src/index.js
import React from 'react';
import ReactDOM from 'react-dom';

import 'assets/scss/volt.scss';
import "@fortawesome/fontawesome-free/css/all.css";
import "react-datetime/css/react-datetime.css";
import App from './components/App';

ReactDOM.render(<App />, document.querySelector('#app'));
--#

--% /src/index.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>My React Lovesite</title>
    <meta name="description" content="Tiny news site">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
  </head>
  <body>
    <div id="app"></div>
  </body>
</html>
--#

--% /webpack.js
const path = require('path');
const webpack = require('webpack');
const HtmlWebPackPlugin = require('html-webpack-plugin');
__TEMPLATE_ADDITIONAL_IMPORTS__

const sourcedir = '__TEMPLATE_MTS_DIR__'

console.log(`
**********************************************
*** WEBPACK
process.cwd:    ${process.cwd()}
sourcedir:      ${path.resolve(process.cwd(), sourcedir)}
`);

const rule_ts_js = {
  test: /\.(ts|js)x?$/,
  exclude: /node_modules/,
  use: [
    {
      loader: 'babel-loader',
      options: { cacheDirectory: true }
    },
    {
      loader: 'ts-loader',
      options: { transpileOnly: true, experimentalWatchApi: true }
    }
  ]
};

const rule_js = {
  test: /\.js$/,
  exclude: /node_modules/,
  loader: "babel-loader",
};

const rule_js_eslint = {
  enforce: "pre",
  test: /\.js$/,
  exclude: /node_modules/,
  loader: "eslint-loader",
  options: {
    emitWarning: true,
    failOnError: false,
    failOnWarning: false
  }
};

const rule_html = {
  // Loads the javacript into html template provided.
  // Entry point is set below in HtmlWebPackPlugin in Plugins 
  test: /\.html$/,
  use: [
    {
      loader: "html-loader",
      // options: { minimize: true }
    }
  ]
};

const rule_css = { 
  test: /\.css$/,
  use: [ 'style-loader', 'css-loader' ]
};

const rule_sass = {
  test: /\.s[ac]ss$/i,
  use: [		
    "style-loader",	// Creates `style` nodes from JS strings
    "css-loader", // Translates CSS into CommonJS		
    "sass-loader", // Compiles Sass to CSS
  ],
};

const rule_ico = {
  test: /\.(ico|eot|svg|otf|ttf|woff|woff2)$/,
  use: 'file-loader',
};

const rule_png = {
  test: /\.(png|svg|jpg|gif)$/,
  use: ['file-loader']
};

module.exports = {
  devServer: {
    contentBase: path.resolve(process.cwd(), 'dist'),
    hot: true,
    port: __TEMPLATE_SERVER_PORT__,
    historyApiFallback: true,
  },
  entry: {
    main: [`./${sourcedir}/src/index`,],
  },
  mode: 'development',
  module: {
    rules: [
      rule_js,
      rule_html,
      rule_css,
      rule_sass,
      rule_ico,
      rule_png,
    ],
  },
  output: {
    path: path.join(__dirname, 'dist'),
    publicPath: '/',
    filename: '[name].js'
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(),
    new HtmlWebPackPlugin({
      template: path.resolve(process.cwd(), sourcedir, 'src', 'index.html'),
      filename: "./index.html",
      favicon: path.resolve(process.cwd(), sourcedir, 'assets', 'favicon.ico'),
      // excludeChunks: [ 'server' ]
    }),
__TEMPLATE_ADDITIONAL_PLUGINS__
  ],
  resolve: {
    alias: {
      'nomo': path.resolve(process.cwd(), 'node_modules'),
      '#': path.resolve(process.cwd(), sourcedir),
      '$': path.resolve(process.cwd(), sourcedir, 'src'),
      '@': path.resolve(process.cwd(), sourcedir, 'src', 'components'),
      'assets': path.resolve(process.cwd(), sourcedir, 'assets'),
      'utils': path.resolve(process.cwd(), sourcedir, 'utils'),
      
      // 'common': path.resolve(process.cwd(), sourcedir, 'src', 'common'),
      // 'routes': path.resolve(process.cwd(), sourcedir, 'src', 'routes'),

      'modules': path.resolve(process.cwd(), sourcedir, 'components', 'modules'),
      'context': path.resolve(process.cwd(), sourcedir, 'components', 'context'),
      'common': path.resolve(process.cwd(), sourcedir, 'components', 'common'),
      'routes': path.resolve(process.cwd(), sourcedir, 'components', 'routes'),
    },
    extensions: ['.js', '.jsx', '.ts', '.tsx', '.json'],
    modules: [sourcedir, 'node_modules'],				
  },
  target: 'web',
}
--#
