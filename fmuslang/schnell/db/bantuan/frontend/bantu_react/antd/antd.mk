--% index/fm.us
__TEMPLATE_PROJECT_DIR__,d
  %utama=__FILE__
  %__TEMPLATE_SERVER_PORT__=9502
  __TEMPLATE_WEBPACK_NAME__.js,f(e=utama=/webpack.js)
  .babelrc,f(e=utama=/.babelrc)
  .eslintrc.js,f(e=utama=/.eslintrc.js)
  yarn.add.sh,f(e=utama=/yarn.add.sh)
  run.sh,f(e=utama=/run.sh)
  $*chmod a+x *.sh
  __TEMPLATE_MTS_DIR__,d(/mk)
    assets,d(/mk)
    utils,d(/mk)
    components,d(/mk)
      App,d(/mk)
        index.js,f(e=utama=/src/components/App/index.js)
    index.html,f(e=utama=/src/index.html)
    index.css,f(e=utama=/src/index.css)
    index.js,f(e=utama=/src/index.js)
    config.js,f(e=utama=/src/config.js)
  $*qterminal 2>/dev/null &
--#

--% /yarn.add.sh/other
yarn add @babel/core @babel/preset-env @babel/preset-react bootstrap clean-webpack-plugin eslint jquery jshint lodash popper.js style-loader webpack-cli webpack-dev-server @popperjs/core

yarn add --dev babel-cli babel-core babel-loader babel-plugin-transform-class-properties babel-preset-env babel-preset-react babel-register css-loader extract-text-webpack-plugin file-loader html-loader html-webpack-plugin image-webpack-loader mini-css-extract-plugin node-sass postcss-cli postcss-cssnext postcss-extend postcss-import postcss-loader postcss-mixins postcss-nested postcss-simple-vars react react-dom sass-loader webpack webpack-merge
--#

--% /yarn.add.sh
yarn add react react-dom react-router-dom react-hot-loader antd eslint-loader babel-eslint
--#

--% /.eslintrc.js
module.exports = {
  "extends": [
    "eslint:recommended",
  ],
  "parser": "babel-eslint",
  "rules": {				
    "no-case-declarations": "off",
    "no-console": "off",
    "no-prototype-builtins": "off",
    "no-undef": "off",
    "no-unused-vars": "off",		
  }
};
--#

--% /.babelrc
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-react"
  ]
}
--#

--% /run.sh
./node_modules/.bin/webpack serve --mode development --config __TEMPLATE_WEBPACK_NAME__
--#

--% /src/components/App/index.js

import React from "react";
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link,
  useRouteMatch,
  useParams,
} from "react-router-dom";
import { hot } from 'react-hot-loader/root';

export default function App() {
  return (
    <Router>
      <div>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
          <li>
            <Link to="/topics">Topics</Link>
          </li>
        </ul>

        <Switch>
          <Route path="/about">
            <About />
          </Route>
          <Route path="/topics">
            <Topics />
          </Route>
          <Route path="/">
            <Home />
          </Route>
        </Switch>
      </div>
    </Router>
  );
}

function Home() {
  return <h2>Home</h2>;
}

function About() {
  return <h2>About</h2>;
}

function Topics() {
  let match = useRouteMatch();

  return (
    <div>
      <h2>Topics</h2>

      <ul>
        <li>
          <Link to={`${match.url}/components`}>Components</Link>
        </li>
        <li>
          <Link to={`${match.url}/props-v-state`}>
            Props v. State
          </Link>
        </li>
      </ul>

      {/* The Topics page has its own <Switch> with more routes
          that build on the /topics URL path. You can think of the
          2nd <Route> here as an "index" page for all topics, or
          the page that is shown when no topic is selected */}
      <Switch>
        <Route path={`${match.path}/:topicId`}>
          <Topic />
        </Route>
        <Route path={match.path}>
          <h3>Please select a topic.</h3>
        </Route>
      </Switch>
    </div>
  );
}

function Topic() {
  let { topicId } = useParams();
  return <h3>Requested topic ID: {topicId}</h3>;
}
--#

--% /src/index.css
@import '~antd/dist/antd.css';
/* @import '~antd/dist/antd.dark.css'; */
/* @import '~antd/dist/antd.compact.css'; */
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500&display=swap');

:root {
  --left-distance: 15%;
  --left-sidebar-percent: -15%; /* negative dari left-distance */
}

* {
  margin: 0;
  padding: 0;
}

body {
  height: 100%;
  margin: 0;
  font-family: "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
    
}

body::after {
  content: "";
  background-size: cover;
  opacity: 0.2;

  top: 0;
  left: 0;
  bottom: 0;
  right: 0;

  position: fixed;
  z-index: -1;   
}
--#

--% /src/index.js
import React from 'react';
import ReactDOM from 'react-dom';

import 'font-awesome/css/font-awesome.min.css';
import './index.css';
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

--% /src/config.js
const config = {
  
  backend: {
    host: 'localhost',
    port: 9101,

    paths: {
      login: {        
        // path: 'user/login',
        path: 'api/users/login',
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
    },
  },

};

config.server = () => `http://${config.backend.host}:${config.backend.port}`;

export default config;
--#

--% /webpack.js
const path = require('path');
const webpack = require('webpack');
const HtmlWebPackPlugin = require('html-webpack-plugin');
// const Dotenv = require('dotenv-webpack');

const sourcedir = 'react-antd'

module.exports = {

  // configuration.devtool should match pattern "^(inline-|hidden-|eval-)?(nosources-)?(cheap-(module-)?)?source-map$"
  // devtool: '#source-map',

  devServer: {
    contentBase: path.resolve(process.cwd(), 'dist'),
    hot: true,
    port: __TEMPLATE_SERVER_PORT__,
    historyApiFallback: true,
  },

  entry: {
    main: [
      // 'babel-polyfill',
      // 'webpack-hot-middleware/client?path=/__webpack_hmr&timeout=20000', 
      // './src/index.js',
      `./${sourcedir}/index.js`
    ]
  },

  mode: 'development',

  module: {
    rules: [
      {
        enforce: "pre",
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "eslint-loader",
        options: {
          emitWarning: true,
          failOnError: false,
          failOnWarning: false
        }
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader",
      },
      {
        // Loads the javacript into html template provided.
        // Entry point is set below in HtmlWebPackPlugin in Plugins 
        test: /\.html$/,
        use: [
          {
            loader: "html-loader",
            //options: { minimize: true }
          }
        ]
      },
      { 
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      },

      {
        test: /\.(ico|eot|svg|otf|ttf|woff|woff2)$/,
        use: 'file-loader',
      },

      {
       test: /\.(png|svg|jpg|gif)$/,
       use: ['file-loader']
      }

    ]
  },

  output: {
    path: path.join(__dirname, 'dist'),
    publicPath: '/',
    filename: '[name].js'
  },

  resolve: {
    modules: [sourcedir, 'node_modules'],
    extensions: ['.js'],
    alias: {
      '@': path.resolve(process.cwd(), sourcedir, 'components'),
      'assets': path.resolve(process.cwd(), sourcedir, 'assets'),
      'modules': path.resolve(process.cwd(), sourcedir, 'components', 'modules'),
      'context': path.resolve(process.cwd(), sourcedir, 'components', 'context'),
      'common': path.resolve(process.cwd(), sourcedir, 'components', 'common'),
      'utils': path.resolve(process.cwd(), sourcedir, 'utils'),
      '#': path.resolve(process.cwd(), sourcedir),
    },
  },

  plugins: [
    new HtmlWebPackPlugin({
      template: path.resolve(process.cwd(), sourcedir, 'index.html'),
      filename: "./index.html",
      favicon: path.resolve(process.cwd(), sourcedir, 'assets', 'favicon.ico'),
      // excludeChunks: [ 'server' ]
    }),
    // new Dotenv(),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin()
  ],


  target: 'web',

}
--#
