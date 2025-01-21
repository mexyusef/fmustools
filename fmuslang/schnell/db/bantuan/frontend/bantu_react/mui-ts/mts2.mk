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
        App.tsx,f(e=utama=/src/components/App.tsx)
        App.scss,f(e=utama=/src/components/App.scss)
      index.html.ejs,f(e=utama=/src/index.html.ejs)
      index.tsx,f(e=utama=/src/index.tsx)
  $*qterminal 2>/dev/null &
--#

--% /yarn.add.sh
yarn add --dev @babel/cli @babel/core @babel/preset-env @babel/preset-react @babel/preset-typescript @types/jest @types/node @types/react @types/react-dom @typescript-eslint/eslint-plugin @typescript-eslint/parser babel-loader css-loader eslint eslint-config-prettier eslint-plugin-prettier eslint-plugin-react express file-loader html-webpack-plugin image-webpack-loader jest node-sass prettier react react-dom react-hot-loader rimraf sass-loader style-loader typescript webpack webpack-cli webpack-dev-server webpack-merge ts-loader @material-ui/core redux react-redux redux-thunk history
--#

--% /.babelrc
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-react",
    "@babel/preset-typescript"
  ],
  "plugins": [
    "react-hot-loader/babel"
  ],
  "env": {
    "production": {
      "presets": [
        "minify"
      ]
    }
  }
}
--#

--% /run.sh
./node_modules/.bin/webpack serve --mode development --config __TEMPLATE_WEBPACK_NAME__
--#

--% /src/components/App.scss
$bg-color: yellow;
$border-color: red;

.app {
  font-family: helvetica, arial, sans-serif;
  padding: 2em;
  border: 5px solid $border-color;

  p {
    background-color: $bg-color;
  }
}
--#

--% /src/components/App.tsx
import * as React from "react";
import { hot } from "react-hot-loader";

import "./App.scss";

class App extends React.Component<Record<string, unknown>, undefined> {
  public render() {
    return (
      <div className="app">
        <h1>Selamat malam di MTS 2!</h1>
        <p>Semoga berkenan dg kesederhanaan kami...</p>
      </div>
    );
  }
}

declare let module: Record<string, unknown>;

export default hot(module)(App);
--#

--% /src/index.tsx
import * as React from "react";
import { render } from "react-dom";
import App from "./components/App";

const rootEl = document.getElementById("root");

render(<App />, rootEl);
--#

--% /src/index.html.ejs
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="UTF-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Hello React!</title>
  </head>
  <body>
    <div id="root"></div>

    <!-- Dependencies -->
    <% if (webpackConfig.mode == 'production') { %>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react/17.0.2/umd/react.production.min.js" integrity="sha512-qlzIeUtTg7eBpmEaS12NZgxz52YYZVF5myj89mjJEesBd/oE9UPsYOX2QAXzvOAZYEvQohKdcY8zKE02ifXDmA==" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/17.0.2/umd/react-dom.production.min.js" integrity="sha512-9jGNr5Piwe8nzLLYTk8QrEMPfjGU0px80GYzKZUxi7lmCfrBjtyCc1V5kkS5vxVwwIB7Qpzc7UxLiQxfAN30dw==" crossorigin="anonymous"></script>
    <% } else { %>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react/17.0.2/umd/react.development.js" integrity="sha512-Vf2xGDzpqUOEIKO+X2rgTLWPY+65++WPwCHkX2nFMu9IcstumPsf/uKKRd5prX3wOu8Q0GBylRpsDB26R6ExOg==" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/17.0.2/umd/react-dom.development.min.js" integrity="sha512-aNBFq6ue8EmNDwVD/l0mWFy3iVZLIxtQaD7fEYBn3HluJer36T1AhJK0THj6MKKfhZrexxWsKX1T16TxLZo6uQ==" crossorigin="anonymous"></script>
    <% } %>
  </body>
</html>
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
    <div id="root"></div>
  </body>
</html>
--#

--% /webpack.js
const { resolve } = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

const commonConfig = {
  resolve: {
    extensions: [".js", ".jsx", ".ts", ".tsx"],
  },
  context: resolve(__dirname, "__TEMPLATE_MTS_DIR__/src"),
  module: {
    rules: [
      {
        test: [/\.jsx?$/, /\.tsx?$/],
        use: ["babel-loader"],
        exclude: /node_modules/,
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"],
      },
      {
        test: /\.(scss|sass)$/,
        use: ["style-loader", "css-loader", "sass-loader"],
      },
      {
        test: /\.(jpe?g|png|gif|svg)$/i,
        use: [
          "file-loader?hash=sha512&digest=hex&name=img/[contenthash].[ext]",
          "image-webpack-loader?bypassOnDebug&optipng.optimizationLevel=7&gifsicle.interlaced=false",
        ],
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({ 
      template: "index.html.ejs" 
    }),
  ],
  externals: {
    react: "React",
    "react-dom": "ReactDOM",
  },
  performance: {
    hints: false,
  },
};

// development config
const { merge } = require("webpack-merge");
const webpack = require("webpack");
// const commonConfig = require("./common");

module.exports = merge(commonConfig, {
  mode: "development",
  entry: [
    "react-hot-loader/patch", // activate HMR for React
    "webpack-dev-server/client?http://localhost:__TEMPLATE_SERVER_PORT__", // bundle the client for webpack-dev-server and connect to the provided endpoint
    "webpack/hot/only-dev-server", // bundle the client for hot reloading, only- means to only hot reload for successful updates
    "./index.tsx", // the entry point of our app
  ],
  devServer: {
    port: __TEMPLATE_SERVER_PORT__,
    hot: true, // enable HMR on the server
    historyApiFallback: true, // fixes error 404-ish errors when using react router :see this SO question: https://stackoverflow.com/questions/43209666/react-router-v4-cannot-get-url 
  },
  devtool: "cheap-module-source-map",
  plugins: [
    new webpack.HotModuleReplacementPlugin(), // enable HMR globally
  ],
});
--#
