--% index/fm.us
__TEMPLATE_PROJECT_DIR__,d
  %utama=__FILE__
  %__TEMPLATE_SERVER_PORT__=9500
  __TEMPLATE_WEBPACK_NAME__.js,f(e=utama=/webpack.js)
  .babelrc,f(e=utama=/.babelrc)
  yarn.add.sh,f(e=utama=/yarn.add.sh)
  run.sh,f(e=utama=/run.sh)
  $*chmod a+x *.sh
  __TEMPLATE_MTS_DIR__,d(/mk)
    src,d(/mk)
      components,d(/mk)
        App,d(/mk)
          index.js,f(e=utama=/src/components/App/index.js)
      index.html,f(e=utama=/src/index.html)
      index.js,f(e=utama=/src/index.js)
  $*qterminal 2>/dev/null &
--#

--% /yarn.add.sh
yarn add @babel/core @babel/preset-env @babel/preset-react bootstrap clean-webpack-plugin eslint jquery jshint lodash popper.js style-loader webpack-cli webpack-dev-server @popperjs/core

yarn add --dev babel-cli babel-core babel-loader babel-plugin-transform-class-properties babel-preset-env babel-preset-react babel-register css-loader extract-text-webpack-plugin file-loader html-loader html-webpack-plugin image-webpack-loader mini-css-extract-plugin node-sass postcss-cli postcss-cssnext postcss-extend postcss-import postcss-loader postcss-mixins postcss-nested postcss-simple-vars react react-dom sass-loader webpack webpack-merge
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
import React, { Component } from 'react';
import ReactDOM from 'react-dom';

const App = () => {
  return (
    <div className="container">
      <h1>Let's go baby!</h1>
    </div>
  );
};

export default App;
--#

--% /src/index.js
import React from 'react';
import ReactDOM from 'react-dom';

import 'bootstrap';
import App from './components/App';

ReactDOM.render(<App />, document.querySelector('#app'));
module.hot.accept();
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
const HtmlWebPackPlugin = require('html-webpack-plugin');

//const ExtractTextPlugin = require('extract-text-webpack-plugin');

const { CleanWebpackPlugin } = require('clean-webpack-plugin');

const webpack = require('webpack');

const sourcedir = '__TEMPLATE_MTS_DIR__'

module.exports = {
  // mode: 'production',
  entry: { app: `./${sourcedir}/src/index.js` },
  output: {
    filename: '[name].[hash].js',
  },
  module: {
    rules: [

      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },

      {
        test: /\.(png|svg|jpg|gif)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              // name: "./images/[name].[hash].[ext]",
              name: '[path][name]-[hash:8].[ext]',
            },
          },
          {
            loader: 'image-webpack-loader',
            options: {
              mozjpeg: {
                progressive: true,
                quality: 65,
              },
              // optipng.enabled: false will disable optipng
              optipng: {
                enabled: false,
              },
              pngquant: {
                quality: [0.65, 0.90],
                speed: 4,
              },
              gifsicle: {
                interlaced: false,
              },
              // the webp option will enable WEBP
              webp: {
                quality: 75,
              },
            },
          },
        ],
      },

      {
        test: /\.html$/,
        use: [
          {
            loader: 'html-loader',
            options: { minimize: true },
          },
        ],
      },

      {
        test: /\.s[ac]ss$/i,
        use: [
          // Creates `style` nodes from JS strings
          "style-loader",
          // Translates CSS into CommonJS
          "css-loader",
          // Compiles Sass to CSS
          "sass-loader",
        ],
      },

      { 
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      },

    ],
  },
  devServer: {
    port: __TEMPLATE_SERVER_PORT__,
    contentBase: './dist',
    hot: true,
  },

  plugins: [

    new HtmlWebPackPlugin({
      template: `./${sourcedir}/src/index.html`,
      filename: './index.html',
    }),

    new CleanWebpackPlugin(),

    new webpack.HotModuleReplacementPlugin(),
  ],

  optimization: {
    splitChunks: {
      cacheGroups: {
        commons: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendor',
          chunks: 'all',
        },
      },
    },
  },
};

--#
