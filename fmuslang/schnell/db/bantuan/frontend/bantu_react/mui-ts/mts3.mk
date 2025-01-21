--% index/fm.us
__TEMPLATE_PROJECT_DIR__,d(/mk)
  %utama=__FILE__
	%__TEMPLATE_SERVER_PORT__=9500
  $*qterminal 2>/dev/null &
  __TEMPLATE_MTS_DIR__,d(/mk)
    .editorconfig,f(e=utama=/mts-admin/.editorconfig)
    package.json,f(e=utama=/mts-admin/package.json)
    .gitignore,f(e=utama=/mts-admin/.gitignore)
    tsconfig.json,f(e=utama=/mts-admin/tsconfig.json)
    .eslintrc,f(e=utama=/mts-admin/.eslintrc)
    __TEMPLATE_WEBPACK_NAME__.js,f(e=utama=/mts-admin/__TEMPLATE_WEBPACK_NAME__.js)
    README.md,f(e=utama=/mts-admin/README.md)
    .babelrc,f(e=utama=/mts-admin/.babelrc)
    .stylelintrc,f(e=utama=/mts-admin/.stylelintrc)
    postcss.config.js,f(e=utama=/mts-admin/postcss.config.js)
    __TEMPLATE_WEBPACK_NAME__.dev.js,f(e=utama=/mts-admin/__TEMPLATE_WEBPACK_NAME__.dev.js)
    __TEMPLATE_WEBPACK_NAME__.prod.js,f(e=utama=/mts-admin/__TEMPLATE_WEBPACK_NAME__.prod.js)
    .prettierrc,f(e=utama=/mts-admin/.prettierrc)
    $*ln -s ../node_modules .
    local-types,d(/mk)
      README.md,f(e=utama=/mts-admin/local-types/README.md)
      recharts,d(/mk)
        package.json,f(e=utama=/mts-admin/local-types/recharts/package.json)
        index.d.ts,f(e=utama=/mts-admin/local-types/recharts/index.d.ts)
    src,d(/mk)
      global.d.ts,f(e=utama=/mts-admin/src/global.d.ts)
      App.tsx,f(e=utama=/mts-admin/src/App.tsx)
      index.tsx,f(e=utama=/mts-admin/src/index.tsx)
      app.events.tsx,f(e=utama=/mts-admin/src/app.events.tsx)
      helpers,d(/mk)
        ajax.tsx,f(e=utama=/mts-admin/src/helpers/ajax.tsx)
        url.tsx,f(e=utama=/mts-admin/src/helpers/url.tsx)
        utils.tsx,f(e=utama=/mts-admin/src/helpers/utils.tsx)
        storage.tsx,f(e=utama=/mts-admin/src/helpers/storage.tsx)
      theme,d(/mk)
        index.tsx,f(e=utama=/mts-admin/src/theme/index.tsx)
        config.tsx,f(e=utama=/mts-admin/src/theme/config.tsx)
      pages,d(/mk)
        public,d(/mk)
          index.tsx,f(e=utama=/mts-admin/src/pages/public/index.tsx)
          NotFound.tsx,f(e=utama=/mts-admin/src/pages/public/NotFound.tsx)
          Home.tsx,f(e=utama=/mts-admin/src/pages/public/Home.tsx)
        admin,d(/mk)
          index.tsx,f(e=utama=/mts-admin/src/pages/admin/index.tsx)
          Admin.tsx,f(e=utama=/mts-admin/src/pages/admin/Admin.tsx)
          markdown,d(/mk)
            Markdown.tsx,f(e=utama=/mts-admin/src/pages/admin/markdown/Markdown.tsx)
          core,d(/mk)
            index.tsx,f(e=utama=/mts-admin/src/pages/admin/core/index.tsx)
            Header.tsx,f(e=utama=/mts-admin/src/pages/admin/core/Header.tsx)
            SidePanelContent.tsx,f(e=utama=/mts-admin/src/pages/admin/core/SidePanelContent.tsx)
            Sidebar.tsx,f(e=utama=/mts-admin/src/pages/admin/core/Sidebar.tsx)
            Frame.tsx,f(e=utama=/mts-admin/src/pages/admin/core/Frame.tsx)
          dashboard,d(/mk)
            ChartExample.tsx,f(e=utama=/mts-admin/src/pages/admin/dashboard/ChartExample.tsx)
            Dashboard.tsx,f(e=utama=/mts-admin/src/pages/admin/dashboard/Dashboard.tsx)
          examples,d(/mk)
            index.tsx,f(e=utama=/mts-admin/src/pages/admin/examples/index.tsx)
            DataTable.tsx,f(e=utama=/mts-admin/src/pages/admin/examples/DataTable.tsx)
        auth,d(/mk)
          index.tsx,f(e=utama=/mts-admin/src/pages/auth/index.tsx)
          Callback.tsx,f(e=utama=/mts-admin/src/pages/auth/Callback.tsx)
          Login.tsx,f(e=utama=/mts-admin/src/pages/auth/Login.tsx)
          Logout.tsx,f(e=utama=/mts-admin/src/pages/auth/Logout.tsx)
      redux,d(/mk)
        reducer.tsx,f(e=utama=/mts-admin/src/redux/reducer.tsx)
        saga.tsx,f(e=utama=/mts-admin/src/redux/saga.tsx)
        index.tsx,f(e=utama=/mts-admin/src/redux/index.tsx)
        store.tsx,f(e=utama=/mts-admin/src/redux/store.tsx)
        history.tsx,f(e=utama=/mts-admin/src/redux/history.tsx)
      config,d(/mk)
        index.tsx,f(e=utama=/mts-admin/src/config/index.tsx)
        app.mock.tsx,f(e=utama=/mts-admin/src/config/app.mock.tsx)
        app.oauth-code.tsx,f(e=utama=/mts-admin/src/config/app.oauth-code.tsx)
        menus.user.tsx,f(e=utama=/mts-admin/src/config/menus.user.tsx)
        menus.admin.tsx,f(e=utama=/mts-admin/src/config/menus.admin.tsx)
        app.dev.tsx,f(e=utama=/mts-admin/src/config/app.dev.tsx)
        app.common.tsx,f(e=utama=/mts-admin/src/config/app.common.tsx)
        app.github.tsx,f(e=utama=/mts-admin/src/config/app.github.tsx)
        app.prod.tsx,f(e=utama=/mts-admin/src/config/app.prod.tsx)
        types.ts,f(e=utama=/mts-admin/src/config/types.ts)
        routes.admin.tsx,f(e=utama=/mts-admin/src/config/routes.admin.tsx)
        app.oauth-password.tsx,f(e=utama=/mts-admin/src/config/app.oauth-password.tsx)
      routers,d(/mk)
        routes.tsx,f(e=utama=/mts-admin/src/routers/routes.tsx)
      ui,d(/mk)
        SlidePanel.tsx,f(e=utama=/mts-admin/src/ui/SlidePanel.tsx)
        index.tsx,f(e=utama=/mts-admin/src/ui/index.tsx)
        VerticalMenu.tsx,f(e=utama=/mts-admin/src/ui/VerticalMenu.tsx)
        Overlay.tsx,f(e=utama=/mts-admin/src/ui/Overlay.tsx)
        RawHtml.tsx,f(e=utama=/mts-admin/src/ui/RawHtml.tsx)
        Panel.tsx,f(e=utama=/mts-admin/src/ui/Panel.tsx)
        MiniCard.tsx,f(e=utama=/mts-admin/src/ui/MiniCard.tsx)
        ALink.tsx,f(e=utama=/mts-admin/src/ui/ALink.tsx)
        LinkButton.tsx,f(e=utama=/mts-admin/src/ui/LinkButton.tsx)
        Alert.tsx,f(e=utama=/mts-admin/src/ui/Alert.tsx)
        Notifier.tsx,f(e=utama=/mts-admin/src/ui/Notifier.tsx)
        PageHeader.tsx,f(e=utama=/mts-admin/src/ui/PageHeader.tsx)
        Loading.tsx,f(e=utama=/mts-admin/src/ui/Loading.tsx)
        DataTable.tsx,f(e=utama=/mts-admin/src/ui/DataTable.tsx)
        Chart.tsx,f(e=utama=/mts-admin/src/ui/Chart.tsx)
        Tag.tsx,f(e=utama=/mts-admin/src/ui/Tag.tsx)
        HorizontalMenu.tsx,f(e=utama=/mts-admin/src/ui/HorizontalMenu.tsx)
      types,d(/mk)
        index.tsx,f(e=utama=/mts-admin/src/types/index.tsx)
        MenuItem.tsx,f(e=utama=/mts-admin/src/types/MenuItem.tsx)
      styles,d(/mk)
        _mixins.scss,f(e=utama=/mts-admin/src/styles/_mixins.scss)
        default.scss,f(e=utama=/mts-admin/src/styles/default.scss)
        _variables.scss,f(e=utama=/mts-admin/src/styles/_variables.scss)
      service,d(/mk)
        global.tsx,f(e=utama=/mts-admin/src/service/global.tsx)
        locales.tsx,f(e=utama=/mts-admin/src/service/locales.tsx)
        auth.tsx,f(e=utama=/mts-admin/src/service/auth.tsx)
        resource.tsx,f(e=utama=/mts-admin/src/service/resource.tsx)
        index.d.ts,f(e=utama=/mts-admin/src/service/index.d.ts)
    assets,d(/mk)
      user.json,f(e=utama=/mts-admin/assets/user.json)
      index.html,f(e=utama=/mts-admin/assets/index.html)
      _redirects,f(e=utama=/mts-admin/assets/_redirects)
      datatable.json,f(e=utama=/mts-admin/assets/datatable.json)
      images,d(/mk)
        bg.jpg,f(b64=utama=/mts-admin/assets/images/bg.jpg)
      locales,d(/mk)
        json,d(/mk)
          pro.babel,f(e=utama=/mts-admin/assets/locales/json/pro.babel)
          en-US.json,f(e=utama=/mts-admin/assets/locales/json/en-US.json)
          zh-CN.json,f(e=utama=/mts-admin/assets/locales/json/zh-CN.json)
    .github,d(/mk)
      workflows,d(/mk)
        main.yml,f(e=utama=/mts-admin/.github/workflows/main.yml)
    .vscode,d(/mk)
      launch.json,f(e=utama=/mts-admin/.vscode/launch.json)
      settings.json,f(e=utama=/mts-admin/.vscode/settings.json)
--#

--% /mts-admin/.editorconfig
#root = true

[*]
indent_style = space
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
max_line_length = 600
indent_size = 4

[*.md]
trim_trailing_whitespace = false
--#

--% /mts-admin/package.json
{
  "name": "admin-template-for-react",
  "title": "Admin Template for React",
  "version": "1.0.0",
  "description": "Admin template for react",
  "main": "src/index.tsx",
  "scripts": {
  "start": "webpack-dev-server --open --config __TEMPLATE_WEBPACK_NAME__.dev.js",
  "build": "webpack --config __TEMPLATE_WEBPACK_NAME__.prod.js",
  "deploy-build": "webpack --config __TEMPLATE_WEBPACK_NAME__.prod.js --env.baseHref=/admin-template-for-react/",
  "format": "prettier --write ./src/**",
  "lint": "eslint ./src/**/*.{ts,tsx} || stylelint ./src/**/*.{scss,css}",
  "precommit": "lint-staged",
  "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
  "admin template",
  "material design",
  "react",
  "react redux"
  ],
  "dependencies": {
  "@bndynet/dialog": "^2.8.1",
  "@bndynet/dialog-themes": "^1.0.0",
  "@bndynet/recharts-wrapper": "^1.2.1",
  "@bndynet/header-injection-webpack-plugin": "^4.0.1",
  "@material-ui/core": "^4.11.4",
  "@material-ui/icons": "^4.11.2",
  "@material-ui/styles": "^4.11.4",
  "axios": "^0.18.1",
  "classnames": "^2.2.6",
  "connected-react-router": "^5.0.1",
  "github-markdown-css": "^2.10.0",
  "lodash-es": "^4.17.14",
  "mui-datatables": "^2.3.0",
  "query-string": "^6.4.2",
  "react": "^16.14.0",
  "react-dom": "^16.14.0",
  "react-intl-universal": "^1.16.2",
  "react-markdown": "^4.0.3",
  "react-redux": "^5.1.1",
  "react-router-config": "^5.0.0",
  "react-router-dom": "^5.0.1",
  "recharts": "^1.5.0",
  "redux": "^4.0.1",
  "redux-saga": "^0.16.2"
  },
  "devDependencies": {
  "@babel/core": "^7.4.3",
  "@babel/plugin-proposal-class-properties": "^7.12.1",
  "@babel/plugin-proposal-object-rest-spread": "^7.12.1",
  "@babel/plugin-transform-runtime": "^7.12.1",
  "@babel/preset-env": "^7.4.3",
  "@babel/preset-react": "^7.0.0",
  "@babel/preset-typescript": "^7.12.1",  
  "@pmmmwh/react-refresh-webpack-plugin": "^0.4.2",
  "@types/classnames": "^2.2.6",
  "@types/lodash-es": "^4.17.3",
  "@types/react": "^16.8.17",
  "@types/react-dom": "^16.8.3",
  "@types/react-redux": "^6.0.14",
  "@types/react-router-config": "^5.0.1",
  "@types/react-router-dom": "^4.3.1",
  "@types/recharts": "file:local-types/recharts",
  "@types/redux-logger": "^3.0.7",
  "@typescript-eslint/eslint-plugin": "^1.9.0",
  "@typescript-eslint/parser": "^1.9.0",
  "@webpack-cli/serve": "^1.5.1",
  "autoprefixer": "^9.5.0",
  "babel-loader": "^8.0.4",
  "base-href-webpack-plugin": "^2.0.0",
  "clean-webpack-plugin": "^1.0.1",
  "copy-webpack-plugin": "^4.6.0",
  "css-loader": "^1.0.1",
  "eslint": "^5.16.0",
  "eslint-config-prettier": "^4.3.0",
  "eslint-config-react": "^1.1.7",
  "eslint-loader": "^2.1.2",
  "eslint-plugin-prettier": "^3.1.0",
  "eslint-plugin-react": "^7.12.4",
  "file-loader": "^2.0.0",
  "html-webpack-plugin": "^3.2.0",
  "husky": "^1.3.1",
  "lint-staged": "^8.1.5",
  "mini-css-extract-plugin": "^0.5.0",
  "node-sass": "^4.13.0",
  "postcss-loader": "^3.0.0",
  "prettier": "^1.17.1",
  "print-time-webpack": "^2.0.3",
  "react-refresh": "^0.9.0",
  "redux-devtools-extension": "^2.13.8",
  "redux-logger": "^3.0.6",
  "sass-loader": "^7.0.1",
  "source-map-loader": "^0.2.4",
  "style-loader": "^0.23.1",
  "stylelint": "^9.10.1",
  "stylelint-config-prettier": "^5.2.0",
  "stylelint-config-recommended": "^2.1.0",
  "stylelint-scss": "^3.5.4",
  "typescript": "^3.4.1",
  "url-loader": "^1.0.1",
  "webpack": "^4.44.2",
  "webpack-cli": "^4.7.2",
  "webpack-dev-server": "^3.2.1",
  "webpack-merge": "^4.1.2"
  },
  "husky": {
  "hooks": {
    "pre-commit": "lint-staged"
  }
  },
  "lint-staged": {
  "*.{ts,tsx}": [
    "prettier --write",
    "git add"
  ],
  "*.scss": "stylelint --syntax=scss"
  }
}

--#

--% /mts-admin/.gitignore
node_modules/
dist/
--#

--% /mts-admin/tsconfig.json
{
  "compilerOptions": {
    "outDir": "./dist/",
    "sourceMap": true,
    "module": "commonjs",
    "target": "es6",
    "jsx": "react",
    "baseUrl": ".",
    "lib": ["es6", "dom"],
    "noImplicitAny": false,
    "noImplicitThis": true,
    "strictNullChecks": false,
    "declaration": true,
    "emitDeclarationOnly": true,
    "isolatedModules": false,
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true,
    "paths": {
      "app/ui": ["src/ui"],
      "app/types": ["src/types"],
      "app/config": ["src/config"],
      "app/theme": ["src/theme"],
      "app/redux": ["src/redux"],
      "app/locales": ["src/locales"],
      "app/pages/*": ["src/pages/*"],
      "app/service/*": ["src/service/*"],
      "app/types/*": ["src/types/*"],
      "app/helpers/*": ["src/helpers/*"]
    }
  },
  "include": [
    "./src/**/*"
  ],
  "exclude": [
    "node_modules"
  ]
}
--#

--% /mts-admin/.eslintrc
{
  "extends": [
    "eslint:recommended",
    "plugin:react/recommended",
    "plugin:@typescript-eslint/recommended",
    "prettier/@typescript-eslint",
    "plugin:prettier/recommended"
  ],
  "plugins": ["react", "@typescript-eslint", "prettier"],
  "env": {
    "es6": true,
    "browser": true,
    "node": true,
    "jasmine": true,
    "jest": true
  },
  "globals": {
    "Promise": true,
    "APP_BASEHREF": true
  },
  "rules": {
    "prettier/prettier": [
      "error",
      {
        "endOfLine": "lf"
      }
    ],
    "no-console": "warn",
    "@typescript-eslint/explicit-function-return-type": [
      0,
      {
        "allowTypedFunctionExpressions": true
      }
    ],
    "@typescript-eslint/no-explicit-any": "off",
    "@typescript-eslint/no-var-require": "off",
    "@typescript-eslint/camelcase": "warn",
    "@typescript-eslint/no-use-before-define": "warn",
    "@typescript-eslint/explicit-member-accessibility": "warn"
  },
  "settings": {
    "react": {
      "pragma": "React",
      "version": "detect"
    }
  },
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "project": "./tsconfig.json",
    "ecmaVersion": 6,
    "sourceType": "module",
    "ecmaFeatures": {
      "jsx": true
    }
  }
}

--#

--% /mts-admin/__TEMPLATE_WEBPACK_NAME__.js
const path = require('path');
const webpack = require('webpack');
const app = require('./package.json');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const PrintTimeWebpackPlugin = require('print-time-webpack');
const HeaderInjectionWebpackPlugin = require('@bndynet/header-injection-webpack-plugin');
// const ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin');
const { BaseHrefWebpackPlugin } = require('base-href-webpack-plugin');

function resolveTsconfigPathsToAlias({
  tsconfigPath = './tsconfig.json',
  webpackConfigBasePath = './',
} = {}) {
  const { paths } = require(tsconfigPath).compilerOptions;

  const aliases = {};

  Object.keys(paths).forEach(item => {
    const key = item.replace('/*', '');
    const value = path.resolve(
      webpackConfigBasePath,
      paths[item][0].replace('/*', ''),
    );

    aliases[key] = value;
  });

  return aliases;
}

const isDevelopment = process.env.NODE_ENV !== 'production';

module.exports = env => ({
  entry: ['./src/index.tsx'],
  performance: {
    hints: false,
  }, // disable to show warnings about performance
  output: {
    filename: '[name].[chunkhash].js',
    path: path.resolve(__dirname, 'dist'),
  },
  resolve: {
    extensions: ['.ts', '.tsx', '.js', '.jsx', '.scss', 'css'],
    alias: {
      ...resolveTsconfigPathsToAlias(),
      react: path.join(__dirname, 'node_modules/react'),
    },
  },
  module: {
    rules: [
      {
        test: /\.(png|jpg|gif)$/,
        use: [
          {
            loader: 'url-loader',
            options: {
              limit: 8192,
            },
          },
        ],
      },
      {
        test: /\.(woff(2)?|ttf|eot|svg)(\?v=\d+\.\d+\.\d+)?$/,
        use: [
          {
            loader: 'url-loader',
          },
        ],
      },
      {
        test: /\.(sa|sc|c)ss$/,
        use: [
          isDevelopment
            ? 'style-loader'
            : MiniCssExtractPlugin.loader,
          MiniCssExtractPlugin.loader,
          'css-loader',
          // 'postcss-loader',
          {
            loader: `postcss-loader`,
            options: { options: {}, }
          },
          'sass-loader',
        ],
      },
      {
        test: /\.[jt]sx?$/,
        exclude: /node_modules/,
        use: [
          {
            loader: 'babel-loader',
            // options: {
            //     plugins: [
            //         isDevelopment && 'react-refresh/babel',
            //     ].filter(Boolean),
            // },
          },
        ],
      },
    ],
  },
  plugins: [
    new PrintTimeWebpackPlugin(),
    new CleanWebpackPlugin(['dist']),
    new HtmlWebpackPlugin({
      title: app.title,
      meta: {
        author: app.author,
        description: app.description,
      },
      inject: true,
      template: './assets/index.html',
    }),
    new BaseHrefWebpackPlugin({
      baseHref: env && env.baseHref,
    }),
    // This makes it possible for us to safely use env vars on our code
    new webpack.DefinePlugin({
      APP_NAME: JSON.stringify(app.name),
      APP_VERSION: JSON.stringify(app.version),
      APP_BUILD: JSON.stringify(Date.now()),
      APP_BASEHREF: JSON.stringify(
        env && env.baseHref ? env.baseHref : '/',
      ),
    }),
    new webpack.ProvidePlugin({
      React: 'react',
      ReactDOM: 'react-dom',
    }),
    new CopyWebpackPlugin([
      {
        from: './assets',
      },
      {
        from: './README.md',
      },
    ]),
    new MiniCssExtractPlugin({
      filename: '[name].[hash].css',
      chunkFilename: '[id].[hash].css',
    }),
    new HeaderInjectionWebpackPlugin(),

    // react refresh
    // isDevelopment && new webpack.HotModuleReplacementPlugin(),
    // isDevelopment && new ReactRefreshWebpackPlugin(),
  ],
  // .filter(Boolean)
  optimization: {
    splitChunks: {
      chunks: 'async',
      minSize: 30000,
      minChunks: 1,
      maxAsyncRequests: 5,
      maxInitialRequests: 3,
      name: true,
      cacheGroups: {
        default: {
          minChunks: 2,
          priority: -20,
          reuseExistingChunk: true,
        },
        vendors: {
          test: /[\\/]node_modules[\\/]/,
          priority: -10,
        },
      },
    },
  },
});

--#

--% /mts-admin/README.md
# Admin Template for React
yarn add webpack-cli/serve

![](https://img.shields.io/badge/Language-TypeScript-blue.svg)
![](https://img.shields.io/badge/Language-SCSS-blue.svg)
![](https://img.shields.io/badge/React-16.3-brightgreen.svg?logo=react)
![](https://img.shields.io/badge/React-Redux-brightgreen.svg?logo=react)
![](https://img.shields.io/badge/React-react--router--config-brightgreen.svg?logo=react)
![](https://img.shields.io/badge/React-react--intl-brightgreen.svg?logo=react)
![](https://img.shields.io/badge/React-connected--react--router-brightgreen.svg?logo=react)
![](https://img.shields.io/badge/React-Redux%20Saga-brightgreen.svg?logo=react)
[![code style: prettier](https://img.shields.io/badge/Code_Style-Prettier-ff69b4.svg)](https://github.com/prettier/prettier)

A starter admin template with React, React Redux, Material UI and TypeScript that packages using Webpack and integrates a minimal project structure.

- AJAX component: **[axios](https://github.com/axios/axios)**
- UI component: **[material-ui](https://material-ui.com/)**
- REACT stack: react, react-dom, react-redux, react-router-config, react-router-dom, redux, redux-saga, react-intl-universal
- You can custom theme in **./src/theme/config.tsx** file

## ❯ Getting Started

1. Clone repo `git clone <git-url>`
2. `npm install` to install all dependencies
3. `npm start` to start web server or `npm run build` to build production code into **dist** folder

## ❯ Development

### Application Configuration Examples

- ./src/config/app.common.tsx - _all common configurations_
- ./src/config/app.dev.tsx - _configurations used in local_
- ./src/config/app.prod.tsx - _configurations used in production_
- ./src/config/app.github.tsx - _example for github authorization_
- ./src/config/app.auth-code.tsx - _example for authorization code grant type_
- ./src/config/app.auth-password.tsx - _example for password grant type_
- ./src/config/app.mock.tsx - _just for local development without login system_

### Customize more environments

1. New file **./src/config/app.[env_name].tsx** to override your configurations

2. Recommend to import configurations in **app.dev.tsx**

  ```ts
  import config = require('./app.your-env');
  ```

  Or add below code in **./src/config/index.tsx** or **./index.html** to freeze your environment

  ```ts
  window.__APP_ENV__ = 'your-env';
  ```

3. `npm start` and `npm run build` will always use the environment you defined

### Components based on Material UI or some else

`Alert`, `Loading`, `MiniCard`, `Notifier`, `Overlay`, `Panel`, `Tag`, `DataTable`, ...

### i18n/l10n Support

```tsx
import * as intl from 'react-intl-universal';

const message = intl.get('i18nKey');
```

### Available Services

- `import { service as resourceService } from "app/service/resource";` to call APIs which has appended access token in request header
- `import { getState as getAuthState } from "app/service/auth";` to get current user information

### Debug with **Chrome** in **Visual Studio Code**

1. Requires **[Visual Studio Code](https://code.visualstudio.com/)** as IDE and extension **[Debugger for Chrome](https://marketplace.visualstudio.com/items?itemName=msjsdiag.debugger-for-chrome)**

1. `npm start` to run application

1. Click menu **Debug** > **Start Debugging** to debug with generated **.vscode/launch.json** file as below:

  ```json
  {
    "version": "0.2.0",
    "configurations": [
      {
        "type": "chrome",
        "request": "launch",
        "name": "Launch Chrome against localhost",
        "url": "http://localhost:8080",
        "webRoot": "${workspaceFolder}"
      }
    ]
  }
  ```

1. Set breakpoints in your **vscode** and operate in the new Chrome window **Start Debugging** opened

### Recommendatory extensions for **Chrome**

- React Developer Tools
- Redux DevTools

Above extensions will show you the **Actions**, **States** and **Reducers** in **Chrome** console.

--#

--% /mts-admin/.babelrc
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-react",
    "@babel/preset-typescript"
  ],
  "plugins": [
    "@babel/plugin-transform-runtime",
    "@babel/proposal-class-properties",
    "@babel/proposal-object-rest-spread"
  ]
}

--#


--% /mts-admin/.stylelintrc
{
  "plugins": [
    "stylelint-scss"
  ],
  "rules": {
  }
}
--#

--% /mts-admin/postcss.config.js
module.exports = {
  plugins: [ 
    require('autoprefixer')
  ]
}
--#

--% /mts-admin/__TEMPLATE_WEBPACK_NAME__.dev.js
const merge = require('webpack-merge');
const globalConfig = require('./__TEMPLATE_WEBPACK_NAME__.js');

// printing warning details to catch where throw it
process.traceDeprecation = true;

module.exports = env =>
  merge(globalConfig(env), {
    mode: 'development',
    devtool: 'inline-source-map',
    devServer: {
			port: __TEMPLATE_SERVER_PORT__,
      contentBase: './dist',
      historyApiFallback: true,
      // openPage: globalConfig(env).output.publicPath.startsWith('/')
      // ? globalConfig(env).output.publicPath.substr(
      // 1,
      // globalConfig(env).output.publicPath.length - 1,
      // )
      // : globalConfig(env).output.publicPath,
    },
  });

--#

--% /mts-admin/__TEMPLATE_WEBPACK_NAME__.prod.js
const merge = require('webpack-merge');
const globalConfig = require('./__TEMPLATE_WEBPACK_NAME__.js');

module.exports = env => merge(globalConfig(env), {
  mode: 'production',
  devtool: 'source-map',
});
--#

--% /mts-admin/.prettierrc
{
  "trailingComma": "all",
  "semi": true,
  "printWidth": 80,
  "tabWidth": 4,
  "singleQuote": true,
  "endOfLine": "lf",
  "jsxBracketSameLine": false
}

--#

--% /mts-admin/local-types/README.md
# Use locally

- From local-types/[package], run `npm init --scope types --yes`.
- From the root of project, run `npm install -D ./local-types/[package]`

## Recommendations

- Send Pull Request to **[DefinitelyTyped](https://github.com/DefinitelyTyped/DefinitelyTyped)** for package.
--#

--% /mts-admin/local-types/recharts/package.json
{
  "name": "@types/recharts",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
  "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC"
}

--#

--% /mts-admin/local-types/recharts/index.d.ts
// Type definitions for Recharts 1.1
// Project: http://recharts.org/
// Definitions by: Maarten Mulders <https://github.com/mthmulders>
//                 Raphael Mueller <https://github.com/rapmue>
//                 Roy Xue <https://github.com/royxue>
//                 Zheyang Song <https://github.com/ZheyangSong>
//                 Rich Baird <https://github.com/richbai90>
//                 Dan Torberg <https://github.com/caspeco-dan>
//                 Peter Keuter <https://github.com/pkeuter>
//                 Jamie Saunders <https://github.com/jrsaunde>
//                 Paul Melnikow <https://github.com/paulmelnikow>
//                 Harry Cruse <https://github.com/crusectrl>
//                 Andrew Palugniok <https://github.com/apalugniok>
//                 Robert Stigsson <https://github.com/RobertStigsson>
// Definitions: https://github.com/DefinitelyTyped/DefinitelyTyped
// TypeScript Version: 2.8

import * as React from "react";
import {
  getTickValues,
  getNiceTickValues,
  getTickValuesFixedDomain,
} from "recharts-scale";
import { CurveFactory } from "d3-shape";

export type Percentage = string;
export type RechartsFunction = (...args: any[]) => void;
export type LegendValueFormatter = (
  value?: LegendPayload["value"],
  entry?: LegendPayload,
  i?: number,
) => any;
export type TickFormatterFunction = (value: any) => any;
export type TickGeneratorFunction = (noTicksProps: object) => any[];
export type LabelFormatter = (label: string | number) => React.ReactNode;
export type TooltipFormatter = (
  value: string | number | Array<string | number>,
  name: string,
  entry: TooltipPayload,
  index: number,
) => React.ReactNode;
export type ItemSorter<T> = (a: T, b: T) => number;
export type ContentRenderer<P> = (props: P) => React.ReactNode;
export type DataKey =
  | string
  | number
  | ((dataObject: any) => number | [number, number] | null);

export type IconType =
  | "plainline"
  | "line"
  | "square"
  | "rect"
  | "circle"
  | "cross"
  | "diamond"
  | "star"
  | "triangle"
  | "wye"
  | "plainline";
export type LegendType = IconType | "none";
export type LayoutType = "horizontal" | "vertical";
export type AnimationEasingType =
  | "ease"
  | "ease-in"
  | "ease-out"
  | "ease-in-out"
  | "linear";
export type ScaleType =
  | "auto"
  | "linear"
  | "pow"
  | "sqrt"
  | "log"
  | "identity"
  | "time"
  | "band"
  | "point"
  | "ordinal"
  | "quantile"
  | "quantize"
  | "utcTime"
  | "sequential"
  | "threshold";
export type PositionType =
  | "top"
  | "left"
  | "right"
  | "bottom"
  | "inside"
  | "outside"
  | "insideLeft"
  | "insideRight"
  | "insideTop"
  | "insideBottom"
  | "insideTopLeft"
  | "insideBottomLeft"
  | "insideTopRight"
  | "insideBottomRight"
  | "insideStart"
  | "insideEnd"
  | "end"
  | "center";
export type StackOffsetType =
  | "sign"
  | "expand"
  | "none"
  | "wiggle"
  | "silhouette";
export type LineType =
  | "basis"
  | "basisClosed"
  | "basisOpen"
  | "linear"
  | "linearClosed"
  | "natural"
  | "monotoneX"
  | "monotoneY"
  | "monotone"
  | "step"
  | "stepBefore"
  | "stepAfter"
  | CurveFactory;
export type IfOverflowType = "hidden" | "visible" | "discard" | "extendDomain";
export type AxisInterval =
  | number
  | "preserveStart"
  | "preserveEnd"
  | "preserveStartEnd";

export type PickedCSSStyleDeclarationKeys =
  | "alignmentBaseline"
  | "baselineShift"
  | "clip"
  | "clipPath"
  | "clipRule"
  | "color"
  | "colorInterpolationFilters"
  | "cursor"
  | "direction"
  | "display"
  | "dominantBaseline"
  | "enableBackground"
  | "fill"
  | "fillRule"
  | "filter"
  | "floodColor"
  | "floodOpacity"
  | "font"
  | "fontFamily"
  | "fontStretch"
  | "fontStyle"
  | "fontVariant"
  | "glyphOrientationHorizontal"
  | "glyphOrientationVertical"
  | "letterSpacing"
  | "lightingColor"
  | "markerEnd"
  | "markerMid"
  | "markerStart"
  | "mask"
  | "overflow"
  | "pointerEvents"
  | "stopColor"
  | "strokeDasharray"
  | "strokeLinecap"
  | "strokeLinejoin"
  | "textAnchor"
  | "textDecoration"
  | "unicodeBidi"
  | "visibility"
  | "writingMode"
  | "transform";

export interface Point {
  x: number;
  y: number;
  value: number | any[];
}

export interface Margin {
  top: number;
  right: number;
  bottom: number;
  left: number;
}

export interface Animatable {
  onAnimationStart?: RechartsFunction;
  onAnimationEnd?: RechartsFunction;
  animationId?: number;
  isAnimationActive?: boolean;
  isUpdateAnimationActive?: boolean;
  animationBegin?: number;
  animationDuration?: number;
  animationEasing?: AnimationEasingType;
}

export interface CategoricalChartWrapper<L = LayoutType> {
  syncId?: string | number;
  compact?: boolean;
  width?: number;
  height?: number;
  data?: object[];
  layout?: L;
  stackOffset?: StackOffsetType;
  throttleDelay?: number;
  margin?: Partial<Margin>;
  barCategoryGap?: number | string;
  barGap?: number | string;
  barSize?: number | string;
  maxBarSize?: number;
  style?: object;
  className?: string;
  children?: React.ReactNode | React.ReactNode[];
  onClick?: RechartsFunction;
  onMouseLeave?: RechartsFunction;
  onMouseEnter?: RechartsFunction;
  onMouseMove?: RechartsFunction;
  onMouseDown?: RechartsFunction;
  onMouseUp?: RechartsFunction;
  reverseStackOrder?: boolean;
}

export interface EventAttributes {
  onClick?: RechartsFunction;
  onMouseDown?: RechartsFunction;
  onMouseUp?: RechartsFunction;
  onMouseOver?: RechartsFunction;
  onMouseMove?: RechartsFunction;
  onMouseOut?: RechartsFunction;
  onMouseEnter?: RechartsFunction;
  onMouseLeave?: RechartsFunction;
  onTouchEnd?: RechartsFunction;
  onTouchMove?: RechartsFunction;
  onTouchStart?: RechartsFunction;
  onTouchCancel?: RechartsFunction;
}

export interface PresentationAttributes<X = number, Y = number>
  extends Pick<CSSStyleDeclaration, PickedCSSStyleDeclarationKeys> {
  angle: number;
  colorInterpolation: string;
  colorProfile: string;
  colorRendering: string;
  fill: string;
  fillOpacity: number | string;
  fontSize: number | string;
  fontSizeAdjust: number | string;
  fontWeight:
    | "normal"
    | "bold"
    | "bolder"
    | "lighter"
    | 100
    | 200
    | 300
    | 400
    | 500
    | 600
    | 700
    | 800
    | 900
    | "inherit";
  imageRendering: "auto" | "optimizeSpeed" | "optimizeQuality" | "inherit";
  kerning: number | string;
  opacity: number | string;
  shapeRendering:
    | "auto"
    | "optimizeSpeed"
    | "crispEdges"
    | "geometricPrecision"
    | "inherit";
  stopOpacity: number | string;
  stroke: number | string;
  strokeDashoffset: number | string;
  strokeMiterlimit: number | string;
  strokeOpacity: number | string;
  strokeWidth: number | string;
  textRendering:
    | "auto"
    | "optimizeSpeed"
    | "optimizeLegibility"
    | "geometricPrecision"
    | "inherit";
  wordSpacing: number | string;
  style: object;
  width: number;
  height: number;
  dx: number;
  dy: number;
  x: X;
  y: Y;
  r: number;
}

export interface AreaProps
  extends EventAttributes,
    Partial<PresentationAttributes>,
    Animatable {
  dataKey: DataKey; // As the source code states, dataKey will replace valueKey in 1.1.0 and it'll be required (it's already required in current implementation).
  className?: string;
  type?: LineType;
  unit?: string | number;
  name?: string | number;
  xAxisId?: string | number;
  yAxisId?: string | number;
  xAxis?: object;
  yAxis?: object;
  stackId?: string | number;
  legendType?: LegendType;
  connectNulls?: boolean;
  activeDot?:
    | boolean
    | object
    | React.ReactElement<any>
    | ContentRenderer<any>;
  dot?:
    | boolean
    | object
    | React.ReactElement<any>
    | ContentRenderer<DotProps>;
  label?: boolean | object | ContentRenderer<any> | React.ReactElement<any>;
  hide?: boolean;
  layout?: LayoutType;
  baseLine?: number | any[];
  isRange?: boolean;
  points?: Point[];
}

export class Area extends React.Component<AreaProps> {}

// NOTE: the lib's implementation doesn't inherits the event props (it's kept in this definition due to the previous typing definition has it).
export type AreaChartProps = CategoricalChartWrapper & EventAttributes;

export class AreaChart extends React.Component<AreaChartProps> {}

export interface BarData {
  x: number;
  y: number;
  width: number;
  height: number;
  radius: number | any[];
  value: number | string | any[];
}

export interface BarProps
  extends EventAttributes,
    Partial<PresentationAttributes>,
    Animatable {
  dataKey: DataKey; // As the source code states, dataKey will replace valueKey in 1.1.0 and it'll be required (it's already required in current implementation).
  className?: string;
  fill?: string;
  layout?: LayoutType;
  xAxisId?: string | number;
  yAxisId?: string | number;
  yAxis?: object;
  xAxis?: object;
  stackId?: string | number;
  barSize?: number;
  unit?: string | number;
  name?: string | number;
  legendType?: LegendType;
  minPointSize?: number;
  maxBarSize?: number;
  hide?: boolean;
  shape?: React.ReactElement<any> | ContentRenderer<RectangleProps>;
  data?: BarData[];
  // see label section at http://recharts.org/#/en-US/api/Bar
  label?:
    | boolean
    | Label
    | React.SFC<LabelProps>
    | React.ReactElement<LabelProps>
    | ContentRenderer<any>;
}

export class Bar extends React.Component<BarProps> {}

// NOTE: the lib's implementation doesn't inherits the event props (it's kept in this definition due to the previous typing definition has it).
export type BarChartProps = CategoricalChartWrapper & EventAttributes;

export class BarChart extends React.Component<BarChartProps> {}

export interface BrushProps {
  className?: string;
  fill?: string;
  stroke?: string;
  x?: number;
  y?: number;
  width?: number;
  height?: number;
  travellerWidth?: number;
  padding?: Partial<Margin>;
  dataKey?: DataKey;
  data?: any[];
  startIndex?: number;
  endIndex?: number;
  tickFormatter?: TickFormatterFunction;
  children?: React.ReactNode;
  onChange?: RechartsFunction;
  updateId?: string | number;
}

export class Brush extends React.Component<BrushProps> {}

export interface CartesianAxisProps
  extends EventAttributes,
    Partial<PresentationAttributes> {
  className?: string;
  x?: number;
  y?: number;
  width?: number;
  height?: number;
  orientation?: "top" | "bottom" | "left" | "right";
  viewBox?: ViewBox;
  tick?: boolean | ContentRenderer<any> | object | React.ReactElement<any>;
  axisLine?: boolean | object;
  tickLine?: boolean | object;
  mirror?: boolean;
  minTickGap?: number;
  ticks?: any[];
  tickSize?: number;
  stroke?: string;
  tickFormatter?: TickFormatterFunction;
  ticksGenerator?: TickGeneratorFunction;
  interval?: AxisInterval;
}

export class CartesianAxis extends React.Component<CartesianAxisProps> {}

export type CoordinatesGenerator = (
  arg: {
    yAxis: CartesianGridProps["yAxis"];
    width: CartesianGridProps["chartWidth"];
    height: CartesianGridProps["chartHeight"];
    offset: CartesianGridProps["offset"];
  },
) => number[];

export interface CartesianGridProps extends Partial<PresentationAttributes> {
  y?: number;
  width?: number;
  height?: number;
  horizontal?:
    | object
    | React.ReactElement<any>
    | ContentRenderer<LineProps & CartesianGridProps>
    | boolean;
  vertical?:
    | object
    | React.ReactElement<any>
    | ContentRenderer<LineProps & CartesianGridProps>
    | boolean;
  horizontalPoints?: number[];
  verticalPoints?: number[];
  horizontalCoordinatesGenerator?: CoordinatesGenerator;
  verticalCoordinatesGenerator?: CoordinatesGenerator;
  xAxis?: object;
  yAxis?: object;
  offset?: object;
  chartWidth?: number;
  chartHeight?: number;
  horizontalFill?: string[];
  verticalFill?: string[];
}

export class CartesianGrid extends React.Component<CartesianGridProps> {}

// NOTE: the lib's implementation doesn't inherits the event props (it's kept in this definition due to the previous typing definition has it).
export type CellProps = Partial<PresentationAttributes>;

export class Cell extends React.Component<CellProps> {}

// NOTE: the lib's implementation doesn't inherits the event props (it's kept in this definition due to the previous typing definition has it).
export type ComposedChartProps = CategoricalChartWrapper & EventAttributes;

export class ComposedChart extends React.Component<ComposedChartProps> {}

export interface CrossProps extends Partial<PresentationAttributes> {
  className?: string;
  x?: number;
  y?: number;
  width?: number;
  height?: number;
  top?: number;
  left?: number;
}

export class Cross extends React.Component<CrossProps> {}

// NOTE: the lib's implementation doesn't inherits the event props (it's kept in this definition due to the previous typing definition has it).
export interface CurveProps
  extends EventAttributes,
    Partial<PresentationAttributes> {
  className?: string;
  type?: LineType;
  layout?: LayoutType;
  baseLine?: number | any[];
  points?: object[];
  connectNulls?: boolean;
  path?: string;
  pathRef?: React.Ref<any>;
}

export class Curve extends React.Component<CurveProps> {}

// NOTE: the lib's implementation doesn't inherits the event props (it's kept in this definition due to the previous typing definition has it).
export interface DotProps extends EventAttributes {
  className?: string;
  cx?: number;
  cy?: number;
  r?: number;
}

export class Dot extends React.Component<DotProps> {}

export type DataPointFormatter = (
  entry: any,
  dataKey: DataKey,
) => { x: number; y: number; value: any; errorVal: any };

export interface ErrorBarProps {
  dataKey: DataKey; // As the source code states, dataKey will replace valueKey in 1.1.0 and it'll be required (it's already required in current implementation).
  data?: any[];
  xAxis?: object;
  yAxis?: object;
  layout?: string;
  dataPointFormatter?: DataPointFormatter;
  stroke?: string;
  strokeWidth?: number;
  width?: number;
  offset?: number;
}

export class ErrorBar extends React.Component<ErrorBarProps> {}

export interface LegendPayload {
  value: any;
  id: any;
  type: LegendType;
  color?: string;
}

export type BBoxUpdateCallback = (
  box: { width: number; height: number },
) => void;

export interface LegendProps {
  content?: React.ReactElement<any> | ContentRenderer<LegendProps>;
  wrapperStyle?: object;
  chartWidth?: number;
  chartHeight?: number;
  width?: number;
  height?: number;
  iconSize?: number;
  iconType?: IconType;
  layout?: LayoutType;
  align?: "left" | "center" | "right";
  verticalAlign?: "top" | "middle" | "bottom";
  margin?: Partial<Margin>;
  payload?: LegendPayload[];
  formatter?: LegendValueFormatter;
  onClick?: RechartsFunction;
  onMouseEnter?: RechartsFunction;
  onMouseLeave?: RechartsFunction;
  onBBoxUpdate?: BBoxUpdateCallback;
}

export class Legend extends React.Component<LegendProps> {}

export interface LineProps
  extends EventAttributes,
    Partial<PresentationAttributes>,
    Animatable {
  className?: string;
  type?: LineType;
  unit?: string | number;
  name?: string | number;
  xAxisId?: string | number;
  yAxisId?: string | number;
  yAxis?: object;
  xAxis?: object;
  legendType?: LegendType;
  layout?: LayoutType;
  connectNulls?: boolean;
  hide?: boolean;
  activeDot?:
    | object
    | React.ReactElement<any>
    | ContentRenderer<any>
    | boolean;
  dot?:
    | object
    | React.ReactElement<any>
    | ContentRenderer<DotProps>
    | boolean;
  top?: number;
  left?: number;
  width?: number;
  height?: number;
  data?: object[];
  dataKey: DataKey; // As the source code states, dataKey will replace valueKey in 1.1.0 and it'll be required (it's already required in current implementation).
  label?: boolean | object | React.ReactElement<any> | ContentRenderer<any>;
  points?: Point[];
}

export class Line extends React.Component<LineProps> {}

// NOTE: the lib's implementation doesn't inherits the event props (it's kept in this definition due to the previous typing definition has it).
export type LineChartProps = CategoricalChartWrapper & EventAttributes;

export class LineChart extends React.Component<LineChartProps> {}

export interface PieProps
  extends EventAttributes,
    Partial<PresentationAttributes>,
    Animatable {
  className?: string;
  dataKey: DataKey; // As the source code states, dataKey will replace valueKey in 1.1.0 and it'll be required (it's already required in current implementation).
  cx?: number | string;
  cy?: number | string;
  startAngle?: number;
  endAngle?: number;
  paddingAngle?: number;
  innerRadius?: number | string;
  outerRadius?: number | string;
  cornerRadius?: number | string;
  nameKey?: string | number | ((dataObject: any) => number);
  valueKey?: string | number | ((dataObject: any) => number);
  data?: object[];
  minAngle?: number;
  legendType?: LegendType;
  maxRadius?: number;
  sectors?: object[];
  hide?: boolean;
  labelLine?:
    | object
    | ContentRenderer<LineProps & any>
    | React.ReactElement<any>
    | boolean;
  label?:
    | {
        offsetRadius: number;
      }
    | React.ReactElement<any>
    | ContentRenderer<any>
    | boolean;
  activeShape?: object | ContentRenderer<any> | React.ReactElement<any>;
  activeIndex?: number | number[];
  blendStroke?: boolean;
}

export class Pie extends React.Component<PieProps> {}

// NOTE: the lib's implementation doesn't inherits the event props (it's kept in this definition due to the previous typing definition has it).
export interface PieChartProps
  extends EventAttributes,
    CategoricalChartWrapper<"centric"> {
  startAngle?: number;
  endAngle?: number;
  cx?: number | string;
  cy?: number | string;
  innerRadius?: number | string;
  outerRadius?: number | string;
}

export class PieChart extends React.Component<PieChartProps> {}

export interface PolarAngleAxisTick {
  value: any;
  coordinate: number;
}

export interface PolarAngleAxisProps
  extends EventAttributes,
    Partial<PresentationAttributes> {
  type?: "number" | "category";
  angleAxisId?: string | number;
  dataKey?: DataKey; // As the source code states, dataKey will replace valueKey in 1.1.0 and it'll be required (it's already required in current implementation).
  cx?: number;
  cy?: number;
  radius?: Percentage | number;
  hide?: boolean;
  scale?: ScaleType | RechartsFunction; // this seems not being used by the lib.
  axisLine?: boolean | object;
  axisLineType?: "polygon" | "circle";
  tickLine?: boolean | object;
  tick?: boolean | ContentRenderer<any> | object | React.ReactElement<any>;
  ticks?: PolarAngleAxisTick[];
  stroke?: string;
  orientation?: "inner" | "outer";
  tickFormatter?: TickFormatterFunction;
}

export class PolarAngleAxis extends React.Component<PolarAngleAxisProps> {}

export interface PolarGridProps extends Partial<PresentationAttributes> {
  cx?: number;
  cy?: number;
  innerRadius?: number;
  outerRadius?: number;
  polarAngles?: number[];
  polarRadius?: number[];
  gridType?: "polygon" | "circle";
}

export class PolarGrid extends React.Component<PolarGridProps> {}

export interface PolarRadiusAxisTick {
  value: any;
  coordinate: number;
}

export type PolarRadiusAxisDomain = number | "auto" | "dataMin" | "dataMax";

export interface PolarRadiusAxisProps
  extends EventAttributes,
    Partial<PresentationAttributes> {
  type?: "number" | "category";
  cx?: number;
  cy?: number;
  hide?: boolean;
  radiusAxisId?: string | number;
  angle?: number;
  tickCount?: number;
  ticks?: PolarRadiusAxisTick[];
  orientation?: "left" | "right" | "middle";
  axisLine?: boolean | object;
  tick?: boolean | object | React.ReactElement<any> | ContentRenderer<any>;
  stroke?: string;
  tickFormatter?: TickFormatterFunction;
  domain?: [PolarRadiusAxisDomain, PolarRadiusAxisDomain];
  scale?: ScaleType | RechartsFunction;
  allowDataOverflow?: boolean;
}

export class PolarRadiusAxis extends React.Component<PolarRadiusAxisProps> {}

export interface PolygonPoint {
  x: number;
  y: number;
}

export interface PolygonProps
  extends EventAttributes,
    Partial<PresentationAttributes> {
  className?: string;
  points?: PolygonPoint[];
}

export class Polygon extends React.Component<PolygonProps> {}

export interface RadarPoint {
  x: number;
  y: number;
  cx: number;
  cy: number;
  angle: number;
  radius: number;
  value: number;
  payload: object;
}

export interface RadarProps
  extends EventAttributes,
    Partial<PresentationAttributes>,
    Animatable {
  className?: string;
  dataKey: DataKey; // As the source code states, dataKey will replace valueKey in 1.1.0 and it'll be required (it's already required in current implementation).
  points?: RadarPoint[];
  shape?: React.ReactElement<any> | ContentRenderer<RadarProps>;
  activeDot?:
    | object
    | React.ReactElement<any>
    | ContentRenderer<any>
    | boolean;
  dot?:
    | object
    | React.ReactElement<any>
    | ContentRenderer<DotProps>
    | boolean;
  label?: object | React.ReactElement<any> | ContentRenderer<any> | boolean;
  legendType?: LegendType;
  hide?: boolean;
}

export class Radar extends React.Component<RadarProps> {}

// NOTE: the lib's implementation doesn't inherits the event props (it's kept in this definition due to the previous typing definition has it).
export interface RadarChartProps
  extends EventAttributes,
    CategoricalChartWrapper<"centric"> {
  startAngle?: number;
  endAngle?: number;
  cx?: number | string;
  cy?: number | string;
  innerRadius?: number | string;
  outerRadius?: number | string;
}

export class RadarChart extends React.Component<RadarChartProps> {}

export interface RadialBarData {
  cx: number;
  cy: number;
  innerRadius: number;
  outerRadius: number;
  value: any;
}

export interface RadialBarProps
  extends EventAttributes,
    Partial<PresentationAttributes>,
    Animatable {
  className?: string;
  dataKey: DataKey; // As the source code states, dataKey will replace valueKey in 1.1.0 and it'll be required (it's already required in current implementation).
  angleAxisId?: string | number;
  radiusAxisId?: string | number;
  shape?: ContentRenderer<any> | React.ReactElement<any>;
  activeShape?: object | ContentRenderer<any> | React.ReactElement<any>;
  cornerRadius?: number | string;
  minPointSize?: number;
  maxBarSize?: number;
  data?: RadialBarData[];
  legendType?: LegendType;
  label?: boolean | React.ReactElement<any> | ContentRenderer<any> | object;
  background?:
    | boolean
    | React.ReactElement<any>
    | ContentRenderer<any>
    | object;
  hide?: boolean;
}

export class RadialBar extends React.Component<RadialBarProps> {}

export interface RadialBarChartProps extends CategoricalChartWrapper<"radial"> {
  startAngle?: number;
  endAngle?: number;
  cx?: string | number;
  cy?: string | number;
  innerRadius?: string | number;
  outerRadius?: string | number;
}

export class RadialBarChart extends React.Component<RadialBarChartProps> {}

export interface RectangleProps
  extends EventAttributes,
    Partial<PresentationAttributes>,
    Animatable {
  className?: string;
  x?: number;
  y?: number;
  width?: number;
  height?: number;
  radius?: number | any[];
}

export class Rectangle extends React.Component<RectangleProps> {}

export interface ReferenceAreaProps extends Partial<PresentationAttributes> {
  className?: number | string;
  viewBox?: ViewBox;
  xAxis?: object;
  yAxis?: object;
  isFront?: boolean;
  alwaysShow?: boolean;
  ifOverflow?: IfOverflowType;
  x1?: number | string;
  x2?: number | string;
  y1?: number | string;
  y2?: number | string;
  xAxisId?: string | number;
  yAxisId?: string | number;
  shape?:
    | ContentRenderer<ReferenceAreaProps & RectangleProps>
    | React.ReactElement<any>;
}

export class ReferenceArea extends React.Component<ReferenceAreaProps> {}

export type ScaleCalculator = (x: number | string) => number;
export interface ReferenceDotAxisConfiguration {
  scale: ScaleCalculator;
}

export interface ReferenceDotProps
  extends EventAttributes,
    Partial<PresentationAttributes<number | string, number | string>> {
  className?: number | string;
  r?: number;
  xAxis?: ReferenceDotAxisConfiguration;
  yAxis?: ReferenceDotAxisConfiguration;
  isFront?: boolean;
  alwaysShow?: boolean;
  ifOverflow?: IfOverflowType;
  x?: number | string;
  y?: number | string;
  xAxisId?: string | number;
  yAxisId?: string | number;
  shape?:
    | ContentRenderer<
        EventAttributes &
          Partial<
            PresentationAttributes<number | string, number | string>
          > & { cx: number; cy: number }
      >
    | React.ReactElement<any>;
}

export class ReferenceDot extends React.Component<ReferenceDotProps> {}

export interface ReferenceLineProps
  extends Partial<PresentationAttributes<number | string, number | string>> {
  className?: number | string;
  viewBox?: ViewBox;
  xAxis?: object;
  yAxis?: object;
  isFront?: boolean;
  alwaysShow?: boolean;
  ifOverflow?: IfOverflowType;
  x?: number | string;
  y?: number | string;
  label?: string | number | ContentRenderer<any> | React.ReactElement<any>;
  xAxisId?: string | number;
  yAxisId?: string | number;
  shape?:
    | ContentRenderer<
        EventAttributes &
          Partial<
            PresentationAttributes<number | string, number | string>
          > & { x1: number; y1: number; x2: number; y2: number }
      >
    | React.ReactElement<any>;
}

export class ReferenceLine extends React.Component<ReferenceLineProps> {}

export interface ResponsiveContainerProps {
  aspect?: number;
  width?: string | number;
  height?: string | number;
  minHeight?: string | number;
  minWidth?: string | number;
  maxHeight?: string | number;
  children: React.ReactNode;
  debounce?: number;
  id?: string | number;
  className?: string | number;
}

export class ResponsiveContainer extends React.Component<
  ResponsiveContainerProps
> {}

export interface ScatterPoint {
  cx?: number;
  cy?: number;
  size?: number;
  node?: {
    x?: number | string;
    y?: number | string;
    z?: number | string;
  };
  payload?: any;
}

export interface ScatterProps
  extends EventAttributes,
    Partial<PresentationAttributes>,
    Animatable {
  xAxisId?: string | number;
  yAxisId?: string | number;
  zAxisId?: string | number;
  line?: boolean | object | RechartsFunction | React.ReactElement<any>;
  lineType?: "joint" | "fitting";
  lineJointType?: LineType;
  legendType?: LegendType;
  activeIndex?: number;
  activeShape?: object | RechartsFunction | React.ReactElement<any>;
  shape?:
    | "circle"
    | "cross"
    | "diamond"
    | "square"
    | "star"
    | "triangle"
    | "wye"
    | React.ReactElement<any>
    | ContentRenderer<any>;
  points?: ScatterPoint[];
  hide?: boolean;
  data?: object[];
  name?: string | number;
}

export class Scatter extends React.Component<ScatterProps> {}

// NOTE: the lib's implementation doesn't inherits the event props (it's kept in this definition due to the previous typing definition has it).
export type ScatterChartProps = CategoricalChartWrapper & EventAttributes;

export class ScatterChart extends React.Component<ScatterChartProps> {}

export interface SectorProps
  extends EventAttributes,
    Partial<PresentationAttributes> {
  className?: string;
  cx?: number;
  cy?: number;
  innerRadius?: number;
  outerRadius?: number;
  startAngle?: number;
  endAngle?: number;
  cornerRadius?: number | string;
}

export class Sector extends React.Component<SectorProps> {}

export interface TextProps extends Partial<PresentationAttributes> {
  scaleToFit?: boolean;
  angle?: number;
  textAnchor?: "start" | "middle" | "end" | "inherit";
  verticalAnchor?: "start" | "middle" | "end";
  style?: object;
  capHeight?: string;
  lineHeight?: string;
}

export class Text extends React.Component<TextProps> {}

export interface ViewBox {
  x?: number;
  y?: number;
  width?: number;
  height?: number;
}

export interface PolarViewBox {
  cx?: number;
  cy?: number;
  innerRadius?: number;
  outerRadius?: number;
  startAngle?: number;
  endAngle?: number;
}

export interface Coordinate {
  x: number;
  y: number;
}

export interface TooltipPayload {
  name: string;
  value: string | number | Array<string | number>;
  unit?: string;
  color?: string;
  fill?: string;
  dataKey?: DataKey;
  formatter?: TooltipFormatter;
  payload?: any;
}

export interface TooltipProps extends Animatable {
  content?:
    | React.ReactElement<any>
    | React.StatelessComponent<any>
    | ContentRenderer<TooltipProps>;
  viewBox?: ViewBox;
  active?: boolean;
  separator?: string;
  formatter?: TooltipFormatter;
  offset?: number;
  itemStyle?: object;
  labelStyle?: object;
  wrapperStyle?: object;
  cursor?:
    | boolean
    | object
    | React.ReactElement<any>
    | React.StatelessComponent<any>;
  coordinate?: Coordinate;
  position?: Coordinate;
  label?: string | number;
  labelFormatter?: LabelFormatter;
  payload?: TooltipPayload[];
  itemSorter?: ItemSorter<TooltipPayload>;
  filterNull?: boolean;
  useTranslate3d?: boolean;
}

export class Tooltip extends React.Component<TooltipProps> {}

export interface TreemapProps extends EventAttributes, Animatable {
  width?: number;
  height?: number;
  data?: any[];
  style?: object;
  aspectRatio?: number;
  content?: React.ReactElement<any> | ContentRenderer<any>;
  fill?: string;
  stroke?: string;
  className?: string;
  nameKey?: string | number | RechartsFunction;
  dataKey?: DataKey; // As the source code states, dataKey will replace valueKey in 1.1.0 and it'll be required (it's already required in current implementation).
  children?: React.ReactNode[] | React.ReactNode;
}

export class Treemap extends React.Component<TreemapProps> {}

export class Label extends React.Component<LabelProps> {}

export interface LabelProps extends Partial<PresentationAttributes> {
  angle?: number;
  viewBox?: ViewBox | PolarViewBox;
  formatter?: LabelFormatter;
  value?: number | string;
  offset?: number;
  position?: PositionType;
  children?: React.ReactNode[] | React.ReactNode;
  className?: string;
  content?: React.ReactElement<any> | ContentRenderer<any>;
}

export class LabelList extends React.Component<LabelListProps> {}

export interface LabelListProps {
  angle?: number;
  children?: React.ReactNode[] | React.ReactNode;
  className?: string;
  clockWise?: boolean;
  content?: React.ReactElement<any> | ContentRenderer<LabelProps>;
  data?: number;
  dataKey: string | number | RechartsFunction;
  formatter?: LabelFormatter;
  id?: string;
  offset?: number;
  position?: PositionType;
  valueAccessor?: RechartsFunction;
}

export type AxisDomain =
  | string
  | number
  | ContentRenderer<any>
  | "auto"
  | "dataMin"
  | "dataMax";

export interface XPadding {
  left: number;
  right: number;
}

/**
 * In the current lib, there is not actual implementation for XAxis.
 */
// NOTE: the lib's implementation doesn't inherits the event props (it's kept in this definition due to the previous typing definition has it).
export interface XAxisProps extends EventAttributes {
  allowDecimals?: boolean;
  hide?: boolean;
  // The name of data displayed in the axis
  name?: string | number;
  // The unit of data displayed in the axis
  unit?: string | number;
  // The unique id of x-axis
  xAxisId?: string | number;
  domain?: [AxisDomain, AxisDomain];
  // The key of data displayed in the axis
  dataKey?: DataKey;
  // The width of axis which is usually calculated internally
  width?: number;
  // The height of axis, which need to be set by user
  height?: number;
  mirror?: boolean;
  // The orientation of axis
  orientation?: "top" | "bottom";
  type?: "number" | "category";
  // Ticks can be any type when the axis is the type of category
  // Ticks must be numbers when the axis is the type of number
  ticks?: any[];
  // The count of ticks
  tickCount?: number;
  // The formatter function of tick
  tickFormatter?: TickFormatterFunction;
  padding?: XPadding;
  allowDataOverflow?: boolean;
  scale?: ScaleType | RechartsFunction;
  tick?: boolean | ContentRenderer<any> | object | React.ReactElement<any>;
  axisLine?: boolean | object;
  tickLine?: boolean | object;
  minTickGap?: number;
  tickSize?: number;
  // The margin between tick line and the label
  tickMargin?: number;
  interval?: AxisInterval;
  reversed?: boolean;
  // see label section at http://recharts.org/#/en-US/api/XAxis
  label?: string | number | Label | LabelProps;
  allowDuplicatedCategory?: boolean;
  stroke?: string;
}

export class XAxis extends React.Component<XAxisProps> {}

export interface YPadding {
  top: number;
  bottom: number;
}

// NOTE: the lib's implementation doesn't inherits the event props (it's kept in this definition due to the previous typing definition has it).
export interface YAxisProps extends EventAttributes {
  allowDecimals?: boolean;
  hide?: boolean;
  // The name of data displayed in the axis
  name?: string | number;
  // The unit of data displayed in the axis
  unit?: string | number;
  // The unique id of y-axis
  yAxisId?: string | number;
  domain?: [AxisDomain, AxisDomain];
  // The key of data displayed in the axis
  dataKey?: DataKey;
  // Ticks can be any type when the axis is the type of category
  // Ticks must be numbers when the axis is the type of number
  ticks?: any[];
  // The count of ticks
  tickCount?: number;
  // The formatter function of tick
  tickFormatter?: TickFormatterFunction;
  // The width of axis, which need to be set by user
  width?: number;
  // The height of axis which is usually calculated in Chart
  height?: number;
  mirror?: boolean;
  // The orientation of axis
  orientation?: "left" | "right";
  type?: "number" | "category";
  padding?: YPadding;
  allowDataOverflow?: boolean;
  scale?: ScaleType | RechartsFunction;
  tick?: boolean | ContentRenderer<any> | object | React.ReactElement<any>;
  axisLine?: boolean | object;
  tickLine?: boolean | object;
  minTickGap?: number;
  tickSize?: number;
  // The margin between tick line and the label
  tickMargin?: number;
  interval?: AxisInterval;
  reversed?: boolean;
  // see label section at http://recharts.org/#/en-US/api/YAxis
  label?: string | number | Label | LabelProps;
  stroke?: string;
}

export class YAxis extends React.Component<YAxisProps> {}

export interface ZAxisProps {
  type?: "number" | "category";
  // The name of data displayed in the axis
  name?: string | number;
  // The unit of data displayed in the axis
  unit?: string | number;
  // The unique id of z-axis
  zAxisId?: string | number;
  // The key of data displayed in the axis
  dataKey?: DataKey;
  // The range of axis
  range?: number[];
  scale?: ScaleType | RechartsFunction;
}

export class ZAxis extends React.Component<ZAxisProps> {}

export interface SurfaceProps {
  width?: number;
  height?: number;
  viewBox?: ViewBox;
  className?: string;
  style?: object;
  children?: React.ReactNode[] | React.ReactNode;
}

export class Surface extends React.Component<SurfaceProps> {}

export interface SymbolsProps extends Partial<PresentationAttributes> {
  className?: string;
  type?:
    | "circle"
    | "cross"
    | "diamond"
    | "square"
    | "star"
    | "triangle"
    | "wye";
  cx?: number;
  cy?: number;
  size?: number;
  sizeType?: "area" | "diameter";
}

export class Symbols extends React.Component<SymbolsProps> {}

--#

--% /mts-admin/src/global.d.ts
declare const APP_NAME: string;
declare const APP_VERSION: string;
declare const APP_BUILD: string;
declare const APP_BASEHREF: string;

interface Window {
  __APP_CONF__: any;
  __APP_ENV__: string;
}

--#

--% /mts-admin/src/App.tsx
import * as React from 'react';
import _merge from 'lodash-es/merge';
import { connect } from 'react-redux';
import { Dispatch, Action } from 'redux';

import { MuiThemeProvider, createMuiTheme } from '@material-ui/core/styles';
import {
  Theme,
  createStyles,
  withStyles,
  LinearProgress,
} from '@material-ui/core';

import { routes } from './routers/routes';
import { themeConfig } from 'app/theme';
import { Notifier, NotifierOptions, Overlay, Loading } from 'app/ui';
import { actions as globalActions } from 'app/service/global';
import { KEY_THEME } from 'app/theme';
import storage from 'app/helpers/storage';
import { onAppInit } from './app.events';
import utils from './helpers/utils';

const styles = (theme: Theme) => {
  return createStyles({
    '@global': {
      a: {
        color: 'inherit',
      },
      '.recharts-tooltip-label': {
        color: theme.palette.common.black,
      },
    },
    progressBar: {
      position: 'fixed',
      top: 0,
      left: 0,
      width: '100%',
      zIndex: 2000,
    },
  });
};

interface AppComponentProps {
  classes?: any;
  loading: boolean;
  loadingText: string;
  requesting: boolean;
  showNotifier: boolean;
  notifierOptions: NotifierOptions;
  theme: any;
  onCloseNotifier: () => void;
}

interface AppComponentState {
  initDone: boolean;
}

class App extends React.Component<AppComponentProps, AppComponentState> {
  public constructor(props) {
    super(props);
    this.state = {
      initDone: false,
    };
  }

  public componentDidMount() {
    onAppInit({
      localeDone: () => {
        this.setState({ initDone: true });
      },
    });
  }

  public render() {
    const { classes, theme, notifierOptions, showNotifier } = this.props;
    return (
      this.state.initDone && (
        <div className={theme.palette.type}>
          <MuiThemeProvider theme={theme}>
            <LinearProgress
              hidden={!this.props.requesting}
              color="secondary"
              className={classes.progressBar}
            />
            <Notifier
              options={notifierOptions}
              open={showNotifier}
              onCloseButtonClick={this.props.onCloseNotifier}
              hasCloseButton={true}
            />
            <Overlay open={this.props.loading}>
              <Loading loadingText={this.props.loadingText} />
            </Overlay>
            {utils.renderRoutes(routes)}
          </MuiThemeProvider>
        </div>
      )
    );
  }
}

const mapStateToProps = state => {
  const clientTheme = state.global.theme || storage.get(KEY_THEME);
  const finalTheme = clientTheme
    ? _merge({}, themeConfig, clientTheme)
    : themeConfig;
  const muiFinalTheme = createMuiTheme(finalTheme);
  return {
    loading: state.global.loading,
    loadingText: state.global.loadingText,
    requesting: state.global.requesting,
    notifierOptions: state.global.notifierOptions,
    showNotifier: state.global.showNotifier,
    theme: muiFinalTheme,
  };
};

const mapDispatchToProps = (dispatch: Dispatch<Action>) => ({
  onCloseNotifier: () => dispatch(globalActions.unnotify()),
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(withStyles(styles)(App));

--#

--% /mts-admin/src/index.tsx
import 'github-markdown-css/github-markdown.css';
import '@bndynet/dialog/dist/dialog.css';
import '@bndynet/dialog-themes/dist/dialog-dark.css';
import './styles/default.scss';

import * as React from 'react';
import * as ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import { ConnectedRouter } from 'connected-react-router';
import { store, history } from './redux';

import App from './App';

ReactDOM.render(
  <Provider store={store}>
    <ConnectedRouter history={history}>
      <App />
    </ConnectedRouter>
  </Provider>,
  document.querySelector('#app'),
);

--#

--% /mts-admin/src/app.events.tsx
import * as intl from 'react-intl-universal';
import { setup as dialogSetup } from '@bndynet/dialog';
import { getCurrentTheme } from './theme';
import { initLocales } from './service/locales';

function getDialogOptions(options?: any) {
  return {
    labelOK: intl.get('ok'),
    labelCancel: intl.get('cancel'),
    ...options,
  };
}

export function onAppLocaleChanged() {
  dialogSetup(getDialogOptions());
}

export function onAppThemeChanged(isDark: boolean) {
  if (isDark) {
    dialogSetup(
      getDialogOptions({
        theme: isDark ? 'dialog-dark' : '',
      }),
    );
  } else {
    document.body.classList.remove('dialog-dark');
  }
}

export interface AppInitCallbacks {
  localeDone: () => void;
}

function onAppLocaleInit(done: () => void) {
  initLocales(null, done);
}

function onAppThemeInit() {
  const themeConfig = getCurrentTheme();
  onAppThemeChanged(themeConfig.palette.type === 'dark');
}

export function onAppInit(callbacks: AppInitCallbacks) {
  onAppThemeInit();
  onAppLocaleInit(callbacks.localeDone);
  dialogSetup(getDialogOptions());
}

--#

--% /mts-admin/src/helpers/ajax.tsx
import axios, {
  AxiosInstance,
  AxiosRequestConfig,
  AxiosPromise,
  AxiosResponse,
  AxiosError,
} from 'axios';
import _merge from 'lodash-es/merge';

export interface AjaxOptions {
  baseURL?: string;
  headers?: object;
  headerAuthorization?: string | (() => string);
  onRequest?: (config: AxiosRequestConfig) => AxiosRequestConfig;
  onRequestError?: (error) => void;
  onResponse?: (response: any) => any;
  onResponseError?: (error) => any;
}

export type AjaxError = AxiosResponse;

export class Ajax {
  public static setGlobalOptions(options: AjaxOptions) {
    axios.defaults = _merge({}, axios.defaults, Ajax.buildOptions(options));
  }

  private static buildOptions(options: AjaxOptions): AxiosRequestConfig {
    if (!options) {
      return null;
    }

    const config: AxiosRequestConfig = {};
    if (options.baseURL) {
      config.baseURL = options.baseURL;
    }
    if (options.headerAuthorization) {
      if (!config.headers) {
        config.headers = {};
      }
      if (!config.headers.common) {
        config.headers.common = {};
      }
      const authorization =
        typeof options.headerAuthorization === 'string'
          ? options.headerAuthorization
          : options.headerAuthorization();
      const keyAuthorization = 'Authorization';
      config.headers.common[keyAuthorization] = authorization;
    }
    if (options.headers) {
      if (!config.headers) {
        config.headers = {};
      }
      if (!config.headers.common) {
        config.headers.common = {};
      }
      for (const key of Object.keys(options.headers)) {
        config.headers.common[key] = options.headers[key];
      }
    }
    return config;
  }

  private static instance(options?: AjaxOptions): AxiosInstance {
    const result: AxiosInstance = options
      ? axios.create(Ajax.buildOptions(options))
      : axios.create();

    if (options) {
      if (options.onRequest || options.onRequestError) {
        result.interceptors.request.use(
          options.onRequest ||
            ((config: AxiosRequestConfig) => config),
          options.onRequestError ||
            ((error: any) => Promise.reject(error)),
        );
      }
      if (options.onResponse || options.onResponseError) {
        result.interceptors.response.use(
          options.onResponse || ((response: any) => response),
          options.onResponseError ||
            ((error: any) => Promise.reject(error)),
        );
      }
    }

    result.interceptors.response.use(
      (response: AxiosResponse) => response.data,
      (error: AxiosError) => Promise.reject(error.response),
    );

    return result;
  }

  private options: AjaxOptions;

  public constructor(options?: AjaxOptions) {
    this.options = options;
  }

  public instance = (): AxiosInstance => Ajax.instance(this.options);

  public get = (url: string): AxiosPromise => {
    return this.instance().get(url) as AxiosPromise;
  };
  public post = (url: string, data: any): AxiosPromise => {
    return this.instance().post(url, data);
  };
  public postForm = (url: string, data: any): AxiosPromise => {
    const formData = new FormData(); // Must be FormData so that the ajax request will be Form post
    Object.keys(data).forEach(k => {
      formData.append(k, data[k]);
    });
    return this.instance().post(url, formData);
  };
  public remove = (url: string): AxiosPromise => {
    return this.instance().delete(url);
  };
  public put = (url: string, data: any): AxiosPromise => {
    return this.instance().put(url, data);
  };
  public patch = (url: string, data: any): AxiosPromise => {
    return this.instance().patch(url, data);
  };
}

const ajax = new Ajax();

export default ajax;

--#

--% /mts-admin/src/helpers/url.tsx
import { parse, parseUrl, ParsedQuery, stringify } from 'query-string';

export class Url {
  public static current(): Url {
    return new Url(location.href);
  }

  public readonly url: string;
  public readonly rootUrl: string;
  public readonly queries: ParsedQuery;
  public readonly hashs: ParsedQuery;
  public readonly originUrl: string;

  public constructor(url?: string) {
    if (url) {
      this.originUrl = url;
      // eslint-disable-next-line no-useless-escape
      this.rootUrl = url.replace(/^(.*\/\/[^\/?#]*).*$/, '$1');
      this.url = parseUrl(url).url;
      this.queries = parse(location.search);
      this.hashs = parse(location.hash);
    }
  }

  public appendQueries(queries: object | string): string {
    if (typeof queries === 'string') {
      return `${this.originUrl}${
        this.originUrl.indexOf('?') < 0 ? '?' : ''
      }${queries}`;
    } else if (queries) {
      return `${this.originUrl}${
        this.originUrl.indexOf('?') < 0 ? '?' : ''
      }${stringify(queries)}`;
    } else {
      return this.originUrl;
    }
  }

  public merge(absolutePath: string, queries?: object | string): string {
    return new Url(`${this.rootUrl}${absolutePath}`).appendQueries(queries);
  }

  public redirect(queriesOrUrl: object | string) {
    if (typeof queriesOrUrl === 'string') {
      location.href = queriesOrUrl;
    } else {
      location.search = stringify(queriesOrUrl);
    }
  }
}

--#

--% /mts-admin/src/helpers/utils.tsx
import { renderRoutes, RouteConfig } from 'react-router-config';

const utils = {
  /**
   * Generates a random string.
   * @param length The result length
   * @returns A random string
   */
  randomString(length: number) {
    let result = '';
    const possible =
      'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    for (let i = 0; i < length; i++) {
      result += possible.charAt(
        Math.floor(Math.random() * possible.length),
      );
    }
    return result;
  },
  /**
   * Deplays to execute a promise like ajax call.
   * @param seconds The delay seconds
   * @param promise The promise to delay
   * @returns A promise
   */
  delay(seconds: number, ...promises: Promise<any>[]): Promise<any[]> {
    return Promise.all([
      ...promises,
      new Promise(presolve => setTimeout(presolve, seconds * 1000)),
    ]);
  },
  /**
   * Overwrites existing method
   * @param routes The route config
   */
  renderRoutes(routes: RouteConfig[]): JSX.Element {
    // const baseHref = document.querySelector('head > base')
    //     ? document.querySelector('head > base').getAttribute('href')
    //     : '';

    // routes.forEach((route: RouteConfig) => {
    //     if (
    //         typeof route.path === 'string' &&
    //         baseHref &&
    //         route.path.indexOf(baseHref) < 0
    //     ) {
    //         route.path = baseHref ? baseHref + route.path : route.path;
    //         route.path = route.path.replace(/\/+/g, '/');
    //     }
    // });
    // console.debug(routes);
    return renderRoutes(routes);
  },
};

export default utils;

--#

--% /mts-admin/src/helpers/storage.tsx
export interface CookieAttribute {
  path?: string;
  domain?: string;
  expires?: number | Date | string;
}

const storage = {
  set: (key: string, value: any) => {
    localStorage.setItem(
      key,
      typeof value === 'object' ? JSON.stringify(value) : value,
    );
  },
  get: (key: string) => {
    const result = localStorage.getItem(key);
    if (result && (result.startsWith('[') || result.startsWith('{'))) {
      return JSON.parse(result);
    } else {
      return result;
    }
  },
  remove: (key: string) => {
    localStorage.removeItem(key);
  },

  setSession: (key: string, value: any) => {
    sessionStorage.setItem(
      key,
      typeof value === 'object' ? JSON.stringify(value) : value,
    );
  },
  getSession: (key: string) => {
    const result = sessionStorage.getItem(key);
    if (result && (result.startsWith('[') || result.startsWith('{'))) {
      return JSON.parse(result);
    } else {
      return result;
    }
  },

  setCookie: (key: string, value: any, attributes?: CookieAttribute) => {
    if (typeof document === 'undefined') {
      return;
    }

    attributes = {
      path: '/',
      ...attributes,
    };

    if (typeof attributes.expires === 'number') {
      attributes.expires = new Date(
        new Date().getTime() + attributes.expires * 1000,
      );
    }

    // using "exipres" because "max-age" is not supported by IE
    attributes.expires = attributes.expires
      ? (attributes.expires as Date).toUTCString()
      : '';

    try {
      const result = JSON.stringify(value);
      // eslint-disable-next-line no-useless-escape
      if (/^[\{\[]/.test(result)) {
        value = result;
      }
    } catch (e) {
      // nothing to do
    }

    value = encodeURIComponent(String(value)).replace(
      /%(23|24|26|2B|3A|3C|3E|3D|2F|3F|40|5B|5D|5E|60|7B|7D|7C)/g,
      decodeURIComponent,
    );
    key = encodeURIComponent(String(key))
      .replace(/%(23|24|26|2B|5E|60|7C)/g, decodeURIComponent)
      // eslint-disable-next-line no-useless-escape
      .replace(/[\(\)]/g, escape);

    let stringifiedAttributes = '';
    for (const attributeName in attributes) {
      if (!attributes[attributeName]) {
        continue;
      }

      stringifiedAttributes += ';' + attributeName;
      if (attributes[attributeName] === true) {
        continue;
      }

      // Considers RFC 6265 section 5.2:
      // ...
      // 3.  If the remaining unparsed-attributes contains a %x3B (";")
      //     character:
      // Consume the characters of the unparsed-attributes up to,
      // not including, the first %x3B (";") character.
      // ...
      stringifiedAttributes +=
        '=' + attributes[attributeName].split(';')[0];
    }

    return (document.cookie = key + '=' + value + stringifiedAttributes);
  },

  getCookie: (key: string) => {
    let result: any;
    if (typeof document === 'undefined') {
      return;
    }

    const decode = (s: string) =>
      s.replace(/(%[0-9A-Z]{2})+/g, decodeURIComponent);
    const cookies = document.cookie ? document.cookie.split('; ') : [];
    let index = 0;
    for (; index < cookies.length; index++) {
      const arr = cookies[index].split('=');
      const name = arr[0];
      if (key === name) {
        result = arr.slice(1).join('=');
        try {
          result = JSON.parse(decode(result));
        } catch (e) {
          // nothing to do
        }
        break;
      }
    }
    return result;
  },

  removeCookie: (key: string, attributes?: any) => {
    storage.setCookie(key, '', {
      ...attributes,
      expires: -1,
    });
  },
};

export default storage;

--#

--% /mts-admin/src/theme/index.tsx
import CheckCircleIcon from '@material-ui/icons/CheckCircle';
import ErrorIcon from '@material-ui/icons/Error';
import InfoIcon from '@material-ui/icons/Info';
import WarningIcon from '@material-ui/icons/Warning';
import { Theme } from '@material-ui/core/styles/createMuiTheme';

import themeConfig from './config';
import { Palette } from '@material-ui/core/styles/createPalette';
import storage from 'app/helpers/storage';

export const KEY_THEME = 'theme';

export type AppPalette = Palette & {
  info: string;
  success: string;
  warning: string;
};

export interface AppTheme extends Theme {
  layout: 'classic' | 'popular';
  palette: AppPalette;
  headerHeight: number;
  sidebarWidth: number;
  sidebarWidthMini: number;
}

export const ifTheme = (theme: Theme, lightResult: any, darkResult: any): any =>
  theme.palette.type === 'light' ? lightResult : darkResult;

export const ifLayout = (
  theme: AppTheme,
  layoutValues: { [key: string]: any },
): any => layoutValues[theme.layout];

export const variantIcon = {
  success: CheckCircleIcon,
  warning: WarningIcon,
  error: ErrorIcon,
  info: InfoIcon,
};

export const variantColor = (theme: Theme) => ({
  primary: {
    color: theme.palette.common.white,
    backgroundColor: themeConfig.palette.primary[500],
  },
  secondary: {
    color: theme.palette.common.white,
    backgroundColor: themeConfig.palette.secondary[500],
  },
  success: {
    color: theme.palette.common.white,
    backgroundColor: themeConfig.palette.success,
  },
  error: {
    color: theme.palette.common.white,
    backgroundColor: theme.palette.error.main,
  },
  info: {
    color: theme.palette.common.white,
    backgroundColor: themeConfig.palette.info,
  },
  warning: {
    color: theme.palette.common.white,
    backgroundColor: themeConfig.palette.warning,
  },
});

export const variantBorderColor = (theme: Theme) => ({
  primary: {
    borderColor: themeConfig.palette.primary[500],
  },
  secondary: {
    borderColor: themeConfig.palette.secondary[500],
  },
  success: {
    borderColor: themeConfig.palette.success,
  },
  error: {
    borderColor: theme.palette.error.main,
  },
  info: {
    borderColor: themeConfig.palette.info,
  },
  warning: {
    borderColor: themeConfig.palette.warning,
  },
});

export { default as themeConfig } from './config';

export function getCurrentTheme(): AppTheme {
  const result: AppTheme = { ...themeConfig, ...storage.get(KEY_THEME) };
  return result;
}

export function isClassic(theme?: AppTheme): boolean {
  return (theme || getCurrentTheme()).layout === 'classic';
}

export function isPopular(theme?: AppTheme): boolean {
  return (theme || getCurrentTheme()).layout === 'popular';
}

--#

--% /mts-admin/src/theme/config.tsx
import { PaletteType } from '@material-ui/core';
import indigo from '@material-ui/core/colors/indigo';
import red from '@material-ui/core/colors/red';
import pink from '@material-ui/core/colors/pink';
import green from '@material-ui/core/colors/green';
import lightBlue from '@material-ui/core/colors/lightBlue';
import amber from '@material-ui/core/colors/amber';

// default theme at https://material-ui.com/customization/default-theme/
const config = {
  layout: 'classic', // popular or classic
  typography: {
    useNextVariants: true,
  },
  overrides: {
    // Name of the component
    MuiSvgIcon: {
      root: {
        fontSize: '1rem',
        verticalAlign: 'text-top',
      },
      fontSizeSmall: {
        fontSize: '0.875rem',
      },
      fontSizeLarge: {
        fontSize: '1.5rem',
      },
    },
    MuiList: {
      padding: {
        paddingTop: 4,
        paddingBottom: 4,
      },
    },
    MuiListItem: {
      root: {
        paddingTop: 8,
        paddingBottom: 8,
        paddingLeft: 16,
        paddingRight: 16,
        '&$dense': {
          fontSize: '0.875rem',
        },
      },
      dense: {
        paddingTop: 4,
        paddingBottom: 4,
        paddingLeft: 8,
        paddingRight: 8,
      },
    },
  },
  palette: {
    type: 'light' as PaletteType, // or dark
    primary: {
      main: indigo[500]
    },
    secondary: {
      main: pink[500]
    },
    error: {
      main: red[500]
    },

    // custom colors
    info: {main: lightBlue[500]},
    success: {main: green[500]},
    warning: {main: amber[700]},
    // end custom colors
  },
  headerHeight: 60,
  sidebarWidth: 200,
  sidebarWidthMini: 56,
};

export default config;

--#

--% /mts-admin/src/pages/public/index.tsx
export { default as Home } from './Home';
export { default as NotFound } from './NotFound';

--#

--% /mts-admin/src/pages/public/NotFound.tsx
import * as React from 'react';
import * as intl from 'react-intl-universal';
import { connect } from 'react-redux';
import { createStyles, withStyles, Typography } from '@material-ui/core';

const styles = createStyles({
  root: {
    marginTop: 100,
    width: 600,
    margin: 'auto',
    textAlign: 'center',
  },
});

class NotFound extends React.Component<
  {
    classes: any;
  },
  {}
> {
  public render() {
    const { classes } = this.props;
    return (
      <div className={classes.root}>
        <i className="far fa-frown fa-5x" />
        <br />
        <br />
        <Typography component="h2" variant="h4">
          {intl.get('errors.404.title')}
        </Typography>
        <br />
        <br />
        <Typography>{intl.get('errors.404.description')}</Typography>
      </div>
    );
  }
}

export default connect(
  null,
  null,
)(withStyles(styles)(NotFound));

--#

--% /mts-admin/src/pages/public/Home.tsx
import * as React from 'react';
import * as intl from 'react-intl-universal';
import ReactMarkdown from 'react-markdown';
import { Dispatch, Action } from 'redux';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom';

import { withStyles, Theme, createStyles } from '@material-ui/core/styles';
import {
  Typography,
  Button,
  Fab,
  MenuItem,
  Select,
  Tooltip,
} from '@material-ui/core';
import AccountCircleIcon from '@material-ui/icons/AccountCircle';
import { loading } from '@bndynet/dialog';

import { service as resourceService } from 'app/service/resource';
import { actions as authActions, getState } from 'app/service/auth';
import { actions as globalActions } from 'app/service/global';

import { getConfig } from 'app/config';
import { setLocale } from 'app/service/locales';

const styles = (theme: Theme) =>
  createStyles({
    '@global': {
      body: {
        paddingTop: theme.spacing(4),
        color: theme.palette.text.primary,
        backgroundColor: theme.palette.background.default,
      },
      '.markdown-body a': {
        color: theme.palette.text.primary,
        textDecoration: 'underline',
      },
    },
    main: {
      maxWidth: 845,
      marginLeft: 'auto',
      marginRight: 'auto',
      marginBottom: 20,
    },
    fab: {
      position: 'fixed',
      right: theme.spacing(2),
      bottom: theme.spacing(2),
      fontSize: 24,
      fontWeight: 700,
      '&.disabled': {
        color: theme.palette.common.white,
      },
    },
    forkMe: {
      position: 'absolute',
      top: 0,
      right: 0,
      border: 0,
    },
  });

interface HomeComponentProps {
  history: any;
  classes: any;
  user: any;
  readme: string;
  onLogout(): void;
  onPreLogout(): void;
}

interface HomeComponentState {
  locale?: string;
  logoutDelay?: number;
  readme?: string;
}

class Home extends React.Component<HomeComponentProps, HomeComponentState> {
  private interval: any;

  public constructor(props: HomeComponentProps) {
    super(props);
    this.handleLogin = this.handleLogin.bind(this);
    this.handleLogout = this.handleLogout.bind(this);
    this.state = {
      locale: intl.getInitOptions().currentLocale,
      logoutDelay: null,
      readme: '',
    };
  }

  public componentWillMount() {
    this.getReadme();
  }

  public render() {
    const config = getConfig();
    const { classes } = this.props;
    const btn = this.props.user ? (
      <Tooltip title={this.props.user.name}>
        <Fab
          disabled={!!this.state.logoutDelay}
          classes={{ root: classes.fab, disabled: 'disabled' }}
          onClick={this.handleLogout}
          color="secondary"
        >
          {this.state.logoutDelay && this.state.logoutDelay > 0
            ? this.state.logoutDelay
            : this.props.user.name[0]}
        </Fab>
      </Tooltip>
    ) : (
      <Fab
        classes={{ root: classes.fab, disabled: 'disabled' }}
        onClick={this.handleLogin}
        color="primary"
      >
        <AccountCircleIcon />
      </Fab>
    );

    return (
      <div className={classes.body}>
        <a href="https://github.com/">
          <img
            className={classes.forkMe}
            src="https://s3.amazonaws.com/github/ribbons/forkme_right_red_aa0000.png"
            alt="Fork me on GitHub"
          />
        </a>
        <main className={classes.main}>
          <div className="margin-bottom-2">
            <Link to="/admin">
              <Button variant="outlined">
                <Typography>
                  {intl.get('admin.brand')}
                </Typography>
              </Button>
            </Link>
            <Select
              className="margin-left-2"
              value={this.state.locale}
              onChange={evt => this.handleChangeLocale(evt)}
              displayEmpty={true}
            >
              <MenuItem value="">
                <em>None</em>
              </MenuItem>
              {config.locales.map(locale => (
                <MenuItem
                  key={locale.value}
                  value={locale.value}
                  selected={
                    this.state.locale === locale.value
                  }
                >
                  {locale.name}
                </MenuItem>
              ))}
            </Select>
          </div>
          <ReactMarkdown
            source={this.state.readme}
            className={'markdown-body'}
          />
          {btn}
        </main>
      </div>
    );
  }

  private handleLogout() {
    this.setState({
      logoutDelay: 5,
    });
    this.props.onPreLogout();
    this.interval = setInterval(() => {
      const delay = this.state.logoutDelay - 1;
      this.setState({
        logoutDelay: delay,
      });
      if (delay <= 0) {
        clearInterval(this.interval);
        this.props.onLogout();
        return;
      }
    }, 1000);
  }

  private handleLogin() {
    this.props.history.push('login');
  }

  private handleChangeLocale(evt) {
    const locale = evt.target.value;
    setLocale(locale, () => {
      this.setState({
        locale: evt.target.value,
      });
      this.getReadme();
    });
  }

  private getReadme() {
    loading();
    const filename =
      intl.getInitOptions().currentLocale === 'en-US'
        ? 'README.md'
        : `README.${intl.getInitOptions().currentLocale}.md`;
    resourceService
      .get(filename)
      .then((res: any) => {
        this.setState({
          readme: res,
        });
      })
      .finally(() => {
        loading(false);
      });
  }
}

const mapStateToProps = () => ({
  user: getState().user,
});

const mapDispatchToProps = (dispatch: Dispatch<Action>) => ({
  onLogout: () => {
    dispatch(authActions.logout());
  },
  onPreLogout: () => {
    dispatch(
      globalActions.notify({
        message: 'Logging out...',
        variant: 'info',
        duration: 5000,
        placement: 'bottom left',
      }),
    );
  },
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(withStyles(styles)(Home));

--#

--% /mts-admin/src/pages/admin/index.tsx
export { default as Admin } from './Admin';
export { default as Dashboard } from './dashboard/Dashboard';
export { default as Markdown } from './markdown/Markdown';
export * from './examples';

--#

--% /mts-admin/src/pages/admin/Admin.tsx
import * as React from 'react';
import { renderRoutes } from 'react-router-config';
import {
  withStyles,
  createStyles,
  withWidth,
  CssBaseline,
} from '@material-ui/core';

import { themeConfig, isClassic, AppTheme } from 'app/theme';
import { adminRoutes } from 'app/config';
import { Frame } from './core';

const styles = (theme: AppTheme) =>
  createStyles({
    '@global': {
      body: {
        color: theme.palette.text.primary,
      },
      '.markdown-body pre': {
        backgroundColor: theme.palette.background.paper,
      },
    },
    root: {
      display: 'flex',
    },
    content: {
      flexGrow: 1,
      paddingTop: isClassic(theme) ? themeConfig.headerHeight : 0,
      paddingBottom: theme.spacing(),
      paddingLeft: theme.spacing(3),
      paddingRight: theme.spacing(3),
      height: '100vh',
      overflow: 'auto',
    },
  });

interface AdminProps {
  classes: any;
}

interface AdminState {
  sidePanelOpen: boolean;
}

class Admin extends React.PureComponent<AdminProps, AdminState> {
  public constructor(props: AdminProps) {
    super(props);
    this.state = {
      sidePanelOpen: false,
    };
  }

  public render() {
    const { classes } = this.props;
    return (
      <div className={classes.root}>
        <CssBaseline />
        <Frame />
        <main className={classes.content}>
          {renderRoutes(adminRoutes)}
        </main>
      </div>
    );
  }
}

export default withStyles(styles)(withWidth()(Admin));

--#

--% /mts-admin/src/pages/admin/markdown/Markdown.tsx
import * as React from 'react';
import classNames from 'classnames';
import ReactMarkdown from 'react-markdown';
import {
  Grid,
  Theme,
  createStyles,
  withStyles,
  TextField,
} from '@material-ui/core';

import { PageHeader } from 'app/ui';

const styles = (theme: Theme) =>
  createStyles({
    textarea: {
      width: '100%',
      marginRight: theme.spacing(),
      '& div': {
        height: 'calc(100vh - 150px)',
        paddingTop: theme.spacing(2),
        paddingBottom: theme.spacing(),
      },
    },
    textareaRoot: {},
    preview: {
      width: '100%',
      height: 'calc(100vh - 150px)',
      border: `1px solid ${theme.palette.divider}`,
      marginLeft: theme.spacing(),
      padding: theme.spacing(3),
      borderRadius: 4,
    },
  });

class Markdown extends React.Component<
  {
    classes: any;
  },
  { input: string }
> {
  public constructor(props) {
    super(props);
    this.state = {
      input: `# Hi, I am Markdown.
- one
- two
- ...

\`\`\`
Code block
\`\`\`
`,
    };

    this.handleInputChange = this.handleInputChange.bind(this);
  }

  public render() {
    const { classes } = this.props;
    return (
      <div>
        <PageHeader title="Markdown Editor" />
        <Grid container={true}>
          <Grid item={true} xs={6}>
            <TextField
              id="outlined-multiline-flexible"
              label="Markdown Content"
              multiline={true}
              value={this.state.input}
              onChange={this.handleInputChange}
              className={classes.textarea}
              variant="outlined"
            />
          </Grid>
          <Grid item={true} xs={6}>
            <ReactMarkdown
              className={classNames(
                'markdown-body',
                classes.preview,
              )}
              source={this.state.input}
            />
          </Grid>
        </Grid>
      </div>
    );
  }

  private handleInputChange(e) {
    this.setState({ input: e.target.value });
  }
}

export default withStyles(styles)(Markdown);

--#

--% /mts-admin/src/pages/admin/core/index.tsx
export { default as Frame } from './Frame';

--#

--% /mts-admin/src/pages/admin/core/Header.tsx
import * as React from 'react';
import * as intl from 'react-intl-universal';
import classNames from 'classnames';
import { Link } from 'react-router-dom';
import { connect } from 'react-redux';
import { push } from 'connected-react-router';
import { Dispatch, Action } from 'redux';
import {
  AppBar,
  IconButton,
  Toolbar,
  Tooltip,
  Avatar,
  Typography,
  Divider,
  List,
  ListItem,
  ListItemText,
  Theme,
  createStyles,
  withStyles,
  withWidth,
  Badge,
  Popover,
} from '@material-ui/core';
import { Breakpoint } from '@material-ui/core/styles/createBreakpoints';
import NotificationsIcon from '@material-ui/icons/Notifications';
import MoreVertIcon from '@material-ui/icons/MoreVert';

import { HorizontalMenu, SlidePanel } from 'app/ui';
import { themeConfig } from 'app/theme';
import { getConfig, adminMenus } from 'app/config';
import { actions as globalActions } from 'app/service/global';
import { onAppThemeChanged } from '../../../app.events';
import SidePanelContent from './SidePanelContent';

const styles = (theme: Theme) =>
  createStyles({
    appBar: {
      zIndex: theme.zIndex.drawer + 1,
      flexDirection: 'row',
      $IconButton: {
        borderRadius: 0,
      },
    },
    menuButton: {
      paddingLeft: theme.spacing(),
      paddingRight: theme.spacing(),
      borderRadius: 0,
      minWidth: 45,
      [theme.breakpoints.down('sm')]: {
        display: 'inherit',
        marginLeft: 0,
      },
    },
    menuButtonHidden: {
      display: 'none',
      [theme.breakpoints.down('sm')]: {
        display: 'inherit',
      },
    },
    brandTitle: {
      color: '#ffffff',
      width: themeConfig.sidebarWidth,
      textAlign: 'center',
      display: 'flex',
      alignItems: 'center',
      paddingLeft: theme.spacing(),
      paddingRight: theme.spacing(),
      fontSize: 22,
      justifyContent: 'center',
      [theme.breakpoints.down('sm')]: {
        display: 'none',
      },
      '&.hidden': {
        display: 'none',
      },
    },

    toolbar: {
      flex: 'inherit',
      minHeight: themeConfig.headerHeight,
      paddingRight: 0,
      display: 'flex',
      alignItems: 'stretch',
    },
    avatar: {
      width: 30,
      height: 30,
      backgroundColor: theme.palette.grey[100],
      color: theme.palette.primary.main,
    },
    bigAvatar: {
      width: 100,
      height: 100,
      margin: '0 auto 5px auto',
      fontSize: 70,
      backgroundColor: theme.palette.grey[100],
      color: theme.palette.primary.main,
    },
    avatarPopup: {
      minWidth: 200,
      maxHeight: '50vh',
    },
    iconButton: {
      padding: theme.spacing(),
    },
    badge: {
      fontSize: '11px',
      right: 5,
      borderWidth: 2,
      borderStyle: 'solid',
      borderColor: theme.palette.primary.main,
    },
  });

interface HeaderProps {
  user?: any;
  classes?: any;
  history?: any;
  isDarkTheme?: boolean;
  width?: Breakpoint;
  push?: (path: string) => void;
  onThemeChange?: (toDark: boolean) => void;
  onToggleClick?: () => void;
  hideBrand?: boolean;
}

interface HeaderState {
  avatarPopupAnchor: any;
  sidePanelOpen: boolean;
}

class Header extends React.PureComponent<HeaderProps, HeaderState> {
  public constructor(props: HeaderProps) {
    super(props);
    this.state = {
      avatarPopupAnchor: null,
      sidePanelOpen: false,
    };
  }

  public render() {
    const config = getConfig();
    const { classes, isDarkTheme, hideBrand } = this.props;
    const { avatarPopupAnchor } = this.state;
    const user = this.props.user || {};
    return (
      <AppBar position="absolute" className={classes.appBar}>
        <Link
          to="/"
          className={classNames('clickable', classes.brandTitle, {
            hidden: hideBrand,
          })}
        >
          <img
            src={config.logoUri}
            style={{ maxHeight: themeConfig.headerHeight }}
          />
          {intl.get(config.title)}
        </Link>

        <IconButton
          color="inherit"
          aria-label="Open drawer"
          onClick={this.handleToggleClick}
          className={classNames(classes.menuButton)}
          style={{ width: themeConfig.sidebarWidthMini }}
        >
          <i
            className={classNames(
              'fa fa-bars animated',
              hideBrand && 'rotateIn',
            )}
          />
        </IconButton>

        <HorizontalMenu data={adminMenus} />

        <Toolbar disableGutters={hideBrand} className={classes.toolbar}>
          <Tooltip title="Toggle light/dark theme">
            <IconButton
              color="inherit"
              onClick={() => this.handleThemeChange()}
              className={classNames(classes.menuButton)}
            >
              <i
                className={classNames(
                  'fa-lightbulb',
                  isDarkTheme ? 'fas' : 'far',
                )}
              />
            </IconButton>
          </Tooltip>
          <IconButton
            color="inherit"
            className={classNames(classes.menuButton)}
          >
            <Badge
              badgeContent={4}
              color="secondary"
              classes={{ badge: classes.badge }}
            >
              <NotificationsIcon fontSize="large" />
            </Badge>
          </IconButton>
          <Tooltip title={user.name || 'Not logged in'}>
            <IconButton
              color="inherit"
              aria-haspopup="true"
              aria-owns={
                avatarPopupAnchor ? 'avatar-popup' : undefined
              }
              className={classNames(classes.menuButton)}
              onClick={this.handleAvatarClick}
            >
              <Avatar
                alt={user.name}
                src={user.avatar}
                className={classes.avatar}
              >
                {!user.avatar &&
                  user.name &&
                  user.name[0] &&
                  user.name[0].toUpperCase()}
              </Avatar>
            </IconButton>
          </Tooltip>
          <Popover
            id="avatar-popup"
            classes={{ paper: classes.avatarPopup }}
            anchorEl={avatarPopupAnchor}
            open={Boolean(avatarPopupAnchor)}
            anchorOrigin={{
              vertical: 'bottom',
              horizontal: 'right',
            }}
            transformOrigin={{
              vertical: 'top',
              horizontal: 'right',
            }}
            onClose={this.handleavatarPopupClose}
          >
            <div className="text-center padding-2">
              <Avatar
                alt={user.name}
                src={user.avatar}
                className={classes.bigAvatar}
              >
                {!user.avatar &&
                  user.name &&
                  user.name[0] &&
                  user.name[0].toUpperCase()}
              </Avatar>
              <Typography variant="subtitle1">
                {user.name}
              </Typography>
              <Typography>{user.email}</Typography>
            </div>
            <Divider />
            <List component="nav">
              <ListItem button={true}>
                <ListItemText primary={intl.get('myProfile')} />
              </ListItem>
              <ListItem button={true} onClick={this.handleLogout}>
                <ListItemText primary={intl.get('signOut')} />
              </ListItem>
            </List>
          </Popover>
          <IconButton
            color="inherit"
            className={classNames(classes.menuButton)}
            onClick={() => this.setState({ sidePanelOpen: true })}
          >
            <MoreVertIcon fontSize="large" />
          </IconButton>
        </Toolbar>
        <SlidePanel
          width={600}
          height={100}
          anchor="right"
          title="Panel Title"
          open={this.state.sidePanelOpen}
          onClose={this.handleSidePanelClose}
        >
          <SidePanelContent />
        </SlidePanel>
      </AppBar>
    );
  }

  private handleToggleClick = () => {
    if (this.props.onToggleClick) {
      this.props.onToggleClick();
    }
  };

  private handleSidePanelClose = () => {
    this.setState({
      sidePanelOpen: false,
    });
  };

  private handleAvatarClick = e => {
    if (!this.props.user) {
      this.props.push('/login');
      return;
    }
    this.setState({ avatarPopupAnchor: e.currentTarget });
  };

  private handleThemeChange = () => {
    this.props.onThemeChange(!this.props.isDarkTheme);
  };

  private handleavatarPopupClose = () => {
    this.setState({ avatarPopupAnchor: null });
  };

  private handleLogout = () => {
    this.handleavatarPopupClose();
    this.props.push('/logout');
  };
}

const mapStateToProps = state => ({
  user: state.auth.user,
  isDarkTheme:
    state.global.theme &&
    state.global.theme.palette &&
    state.global.theme.palette.type === 'dark',
});

const mapDispatchToProps = (dispatch: Dispatch<Action>) => ({
  push: (path: string) => {
    dispatch(push(path));
  },
  onThemeChange: (toDark: boolean) => {
    onAppThemeChanged(toDark);
    dispatch(
      globalActions.changeTheme({
        palette: {
          type: toDark ? 'dark' : 'light',
        },
      }),
    );
  },
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(withStyles(styles)(withWidth()(Header)));

--#

--% /mts-admin/src/pages/admin/core/SidePanelContent.tsx
import * as React from 'react';
import { Typography } from '@material-ui/core';

class SidePanelContent extends React.PureComponent {
  public render() {
    return <Typography>This is a side panel.</Typography>;
  }
}

export default SidePanelContent;

--#

--% /mts-admin/src/pages/admin/core/Sidebar.tsx
import * as React from 'react';
import * as intl from 'react-intl-universal';
import classNames from 'classnames';
import { connect } from 'react-redux';
import {
  Drawer,
  Divider,
  createStyles,
  withStyles,
  Typography,
  IconButton,
  Avatar,
} from '@material-ui/core';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import ChevronRightIcon from '@material-ui/icons/ChevronRight';

import { VerticalMenu } from 'app/ui';
import {
  themeConfig,
  getCurrentTheme,
  ifLayout,
  AppTheme,
  isPopular,
} from 'app/theme';
import { getConfig, adminMenus, userMenus } from 'app/config';
import { UserInfo } from 'app/service/auth';
import { MenuItem } from 'app/types/MenuItem';

interface SidebarProps {
  classes: any;
  open?: boolean;
  user?: UserInfo;
  onToggleClick?: () => void;
}

const styles = (theme: AppTheme) => {
  return createStyles({
    root: {
      height: '100vh',
      '& .MuiIconButton-root': {
        color: ifLayout(theme, { popular: 'inherit' }),
      },
    },
    brandBlock: {
      textAlign: 'center',
      margin: 15,
      '& img': {
        width: '100%',
        backgroundColor: theme.palette.primary.main,
        borderRadius: '50%',
      },
    },
    brandBlockMini: {
      margin: '10px 5px 5px 5px',
    },
    avatar: {
      backgroundColor: theme.palette.grey[100],
      color: theme.palette.primary.main,
    },
    avatarMini: {
      width: 30,
      height: 30,
    },
    drawerPaper: {
      position: 'relative',
      paddingTop: ifLayout(theme, {
        classic: themeConfig.headerHeight,
        popular: 0,
      }),
      paddingBottom: 45,
      whiteSpace: 'nowrap',
      color: ifLayout(theme, {
        classic: theme.palette.common.black,
        popular: theme.palette.common.white,
      }),
      backgroundColor: ifLayout(theme, {
        classic: theme.palette.background.paper,
        popular: theme.palette.primary.main,
      }),
      width: themeConfig.sidebarWidth + 1, // include right border width
      transition: theme.transitions.create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.enteringScreen,
      }),
      overflowX: 'hidden',
      [theme.breakpoints.down('sm')]: {
        position: 'fixed',
      },
    },
    drawerPaperClose: {
      overflowX: 'visible',
      overflowY: 'inherit',
      width: themeConfig.sidebarWidthMini + 1, // include right border width
      [theme.breakpoints.down('sm')]: {
        width: 0,
      },
    },
    drawerPaperFooter: {
      position: 'fixed',
      bottom: 0,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'flex-end',
      backgroundColor: ifLayout(theme, {
        classic: theme.palette.background.paper,
        popular: theme.palette.primary.dark,
      }),
      borderTopWidth: 1,
      borderTopColor: theme.palette.divider,
      borderTopStyle: 'solid',
      width: themeConfig.sidebarWidth,
      overflow: 'hidden',
      minHeight: 'inherit',
      padding: theme.spacing() / 2,
      transition: theme.transitions.create('width', {
        easing: theme.transitions.easing.sharp,
        duration: theme.transitions.duration.enteringScreen,
      }),
    },
    drawerPaperFooterClose: {
      justifyContent: 'center',
      width: themeConfig.sidebarWidthMini,
      [theme.breakpoints.down('sm')]: {
        width: 0,
        padding: 0,
      },
    },
    copyright: {
      flex: 1,
      paddingLeft: theme.spacing(),
    },
    copyrightHidden: {
      display: 'none',
    },
  });
};

class Sidebar extends React.PureComponent<SidebarProps> {
  public constructor(props: SidebarProps) {
    super(props);
  }

  public render() {
    const config = getConfig();
    const { classes, open } = this.props;
    const theme = getCurrentTheme();
    const isPopularTheme = isPopular();
    return (
      <Drawer
        variant="permanent"
        className={classNames(classes.root, theme.layout)}
        classes={{
          paper: classNames(
            classes.drawerPaper,
            !open && classes.drawerPaperClose,
          ),
        }}
        open={open}
      >
        {isPopularTheme && (
          <div>
            <div
              className={classNames(
                classes.brandBlock,
                !open && classes.brandBlockMini,
              )}
            >
              <img
                title={intl.get(config.title)}
                src={config.logoUri}
              />
            </div>
            <Divider />
            <VerticalMenu
              mini={!open}
              width={themeConfig.sidebarWidth}
              minWidth={themeConfig.sidebarWidthMini}
              data={this.getUserMenus()}
            />
            <Divider />
          </div>
        )}
        <VerticalMenu
          mini={!open}
          width={themeConfig.sidebarWidth}
          minWidth={themeConfig.sidebarWidthMini}
          data={adminMenus}
        />
        <div
          className={classNames(
            classes.drawerPaperFooter,
            !open && classes.drawerPaperFooterClose,
          )}
        >
          <a
            className={classNames(
              classes.copyright,
              !open && classes.copyrightHidden,
            )}
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
          >
            <Typography variant="caption">
              Fulgent
            </Typography>
          </a>
          <IconButton
            className={classes.iconButton}
            onClick={this.handleToggle}
          >
            {open ? (
              <ChevronLeftIcon fontSize="small" />
            ) : (
              <ChevronRightIcon fontSize="small" />
            )}
          </IconButton>
        </div>
      </Drawer>
    );
  }

  private handleToggle = () => {
    if (this.props.onToggleClick) {
      this.props.onToggleClick();
    }
  };

  private getUserMenus(): MenuItem[] {
    return [
      {
        icon: (
          <Avatar
            src={this.props.user.avatar}
            className={this.props.classes.avatar}
          />
        ),
        text: this.props.user.name,
        description: this.props.user.email,
        children: userMenus,
      },
    ];
  }
}

const mapStateToProps = state => ({
  user: state.auth.user,
});

export default connect(
  mapStateToProps,
  null,
)(withStyles(styles)(Sidebar));

--#

--% /mts-admin/src/pages/admin/core/Frame.tsx
import * as React from 'react';
import { isClassic } from 'app/theme';
import { default as Header } from './Header';
import { default as Sidebar } from './Sidebar';

interface FrameProps {
  onSidebarToggle?: (open: boolean) => void;
}

interface FrameState {
  sidebarOpen: boolean;
}

class Frame extends React.Component<FrameProps, FrameState> {
  public constructor(props: any) {
    super(props);
    this.state = {
      sidebarOpen: true,
    };
  }

  public render() {
    const hasHeader = isClassic();
    return (
      <div>
        {hasHeader && (
          <Header
            hideBrand={!this.state.sidebarOpen}
            onToggleClick={this.handleSidebarToggle}
          />
        )}
        <Sidebar
          open={this.state.sidebarOpen}
          onToggleClick={this.handleSidebarToggle}
        />
      </div>
    );
  }

  private handleSidebarToggle = () => {
    this.setState({
      sidebarOpen: !this.state.sidebarOpen,
    });
  };
}

export default Frame;

--#

--% /mts-admin/src/pages/admin/dashboard/ChartExample.tsx
import * as React from 'react';
import { Theme, createStyles, withStyles } from '@material-ui/core';
import { Chart } from '@bndynet/recharts-wrapper';
import { fade } from '@material-ui/core/styles/colorManipulator';

let chartIsMounted = false;
const data = [
  { name: 'Mon', Visits: 0, Orders: 20 },
  { name: 'Tue', Visits: 100, Orders: 0 },
  { name: 'Wed', Visits: 0, Orders: 430 },
];
function loadData() {
  return new Promise<any[]>(resolve => {
    setTimeout(() => {
      const response = [
        {
          name: 'Mon',
          Visits: 2200,
          Orders: 3400,
          ShoppingCart: 1210,
          s3: 4000,
        },
        {
          name: 'Tue',
          Visits: 1280,
          Orders: 2398,
          ShoppingCart: 3000,
          s3: 1212,
        },
        {
          name: 'Wed',
          Visits: 5000,
          Orders: 4300,
          ShoppingCart: 2300,
          s3: 3333,
        },
        {
          name: 'Thu',
          Visits: 4780,
          Orders: 2908,
          ShoppingCart: 4500,
          s3: 2321,
        },
        {
          name: 'Fri',
          Visits: 5890,
          Orders: 4800,
          ShoppingCart: 1000,
          s3: 5422,
        },
        {
          name: 'Sat',
          Visits: 4390,
          Orders: 3800,
          ShoppingCart: 3400,
          s3: 1,
        },
        {
          name: 'Sun',
          Visits: 4490,
          Orders: 4300,
          ShoppingCart: 2300,
          s3: 0,
        },
      ];
      if (chartIsMounted) {
        resolve(response);
      }
    }, 5000);
  });
}

const styles = (theme: Theme) =>
  createStyles({
    loadingElement: {
      backgroundColor: fade(theme.palette.background.paper, 0.5),
    },
  });

class ChartExample extends React.Component<{
  classes: { loadingElement: any };
}> {
  public componentDidMount() {
    chartIsMounted = true;
  }

  public componentWillUnmount() {
    chartIsMounted = false;
  }

  public render() {
    return (
      <Chart
        classes={{ loadingElement: this.props.classes.loadingElement }}
        data={data}
        xKey="name"
        dataSource={loadData}
        series={[
          { key: 'Visits', color: '#82ca9d', type: 'bar' },
          { key: 'Orders', color: '#8884d8', type: 'area' },
          { key: 'ShoppingCart', color: '#ff0000' },
        ]}
        loadingElement={<span>Loading...</span>}
      />
    );
  }
}

export default withStyles(styles)(ChartExample);

--#

--% /mts-admin/src/pages/admin/dashboard/Dashboard.tsx
import * as React from 'react';

import Typography from '@material-ui/core/Typography';
import {
  Theme,
  createStyles,
  withStyles,
  Grid,
  IconButton,
  Button,
} from '@material-ui/core';
import HelpIcon from '@material-ui/icons/Help';
import ShoppingCartIcon from '@material-ui/icons/ShoppingCart';

import { Alert, PageHeader, Panel, MiniCard, Tag } from 'app/ui';
import ChartExample from './ChartExample';

const styles = (theme: Theme) =>
  createStyles({
    contentHeader: {
      display: 'flex',
      paddingTop: theme.spacing(2),
      paddingBottom: theme.spacing(2),
      marginBottom: theme.spacing(),
      '& h2': {
        flex: 1,
      },
    },
    breadcrumb: {
      display: 'flex',
      '& > *': {
        alignSelf: 'flex-end',
        textDecoration: 'none',
      },
      '& > *:not(:last-child):after': {
        content: '">"',
        display: 'inline-block',
        marginLeft: 5,
        marginRight: 5,
      },
    },
    chartContainer: {},
  });

const renderCard = props => {
  return (
    <Grid item={true} md={3} xs={6}>
      <MiniCard
        title="150"
        description="New Orders"
        {...props}
        links={{ Home: '/', 'More info': '/admin/dashboard' }}
        icon={<ShoppingCartIcon />}
      />
    </Grid>
  );
};

const renderAlert = props => {
  /* eslint-disable */
  return (
    <Grid item={true} sm={6}>
      <Alert
        title="Alert Title"
        message="Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos blanditiis tenetur unde suscipit, quam beatae rerum inventore consectetur, neque doloribus, cupiditate numquam dignissimos laborum fugiat deleniti? Eum quasi quidem quibusdam."
        variant={props.variant}
        shadow={props.shadow}
        square={props.square}
        closeable={props.closeable}
      />
    </Grid>
  );
};

const renderPanel = props => {
  return (
    <Grid item={true} sm={6}>
      <Panel
        title="Panel Title"
        variant={props.variant}
        closeable={props.closeable}
        minimizeable={props.minimizeable}
        actions={props.actions}
      >
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quos
        blanditiis tenetur unde suscipit, quam beatae rerum inventore
        consectetur, neque doloribus, cupiditate numquam dignissimos
        laborum fugiat deleniti? Eum quasi quidem quibusdam.
      </Panel>
    </Grid>
  );
};

class Dashboard extends React.Component<
  {
    classes: any;
  },
  {}
> {
  public render() {
    const { classes } = this.props;
    return (
      <div data-name="top">
        <PageHeader
          title="Dashboard"
          navigation={{
            Home: '/',
            Dashboard: null,
          }}
        />
        <Grid container={true} spacing={2}>
          {renderCard({ variant: 'info' })}
          {renderCard({ variant: 'success' })}
          {renderCard({ variant: 'warning' })}
          {renderCard({})}
        </Grid>

        <PageHeader title="Chart" />
        <Typography component="div" className={classes.chartContainer}>
          <ChartExample />
        </Typography>

        <PageHeader title="Alerts" />
        <Grid container={true} spacing={2}>
          {renderAlert({
            variant: 'info',
            square: true,
            closeable: false,
          })}
          {renderAlert({
            variant: 'success',
            square: true,
            closeable: false,
          })}
          {renderAlert({
            variant: 'warning',
            square: false,
            closeable: true,
            shadow: 3,
          })}
          {renderAlert({
            variant: 'error',
            square: false,
            closeable: true,
            shadow: 3,
          })}
        </Grid>

        <PageHeader
          title="Panels"
          toolbox={
            <div>
              <Button variant="contained">Button</Button>
              <Button>Button</Button>
            </div>
          }
        />
        <Grid container={true} spacing={2}>
          {renderPanel({})}
          {renderPanel({ variant: 'info' })}
          {renderPanel({ variant: 'success' })}
          {renderPanel({
            variant: 'warning',
            closeable: true,
            minimizeable: true,
          })}
          {renderPanel({
            variant: 'error',
            closeable: true,
            minimizeable: true,
            actions: [
              <Tag key="1" variant="error">
                8 New Members
              </Tag>,
              <IconButton key="2" onClick={() => alert('Help')}>
                <HelpIcon />
              </IconButton>,
            ],
          })}
        </Grid>
      </div>
    );
  }
}

export default withStyles(styles)(Dashboard);

--#

--% /mts-admin/src/pages/admin/examples/index.tsx
export { default as DataTableExample } from './DataTable';

--#

--% /mts-admin/src/pages/admin/examples/DataTable.tsx
import * as React from 'react';
import * as intl from 'react-intl-universal';
import { alert, confirm, loading } from '@bndynet/dialog';

import { service as resourceService } from 'app/service/resource';
import {
  DataTable,
  PageHeader,
  DataTableRequestParameters,
  DataTablePageMeta,
} from 'app/ui';
import utils from 'app/helpers/utils';

class DataTableExample extends React.Component {
  private arrayData = [
    ['Name', 'Location', 'Age', 'Salary'],
    ['Andy1', 'Hefei', 30, '$121,120'],
    ['Andy2', 'Hefei', 33, '$121,110'],
    ['Andy3', 'Hefei', 32, '$121,140'],
    ['Andy4', 'Hefei', 35, '$121,130'],
    ['Andy5', 'Hefei', 31, '$121,120'],
  ];
  private objectData = [
    {
      name: 'Joe James',
      company: 'Test Corp',
      city: 'Yonkers',
      state: 'NY',
    },
    {
      name: 'John Walsh',
      company: 'Test Corp',
      city: 'Hartford',
      state: 'CT',
    },
    { name: 'Bob Herm', company: 'Test Corp', city: 'Tampa', state: 'FL' },
    {
      name: 'James Houston',
      company: 'Test Corp',
      city: 'Dallas',
      state: 'TX',
    },
    {
      name: 'Joe James1',
      company: 'Test Corp',
      city: 'Yonkers',
      state: 'NY',
    },
    {
      name: 'John Walsh',
      company: 'Test Corp',
      city: 'Hartford',
      state: 'CT',
    },
    { name: 'Bob Herm', company: 'Test Corp', city: 'Tampa', state: 'FL' },
    {
      name: 'James Houston',
      company: 'Test Corp',
      city: 'Dallas',
      state: 'TX',
    },
    {
      name: 'Joe James2',
      company: 'Test Corp',
      city: 'Yonkers',
      state: 'NY',
    },
    {
      name: 'John Walsh',
      company: 'Test Corp',
      city: 'Hartford',
      state: 'CT',
    },
    { name: 'Bob Herm', company: 'Test Corp', city: 'Tampa', state: 'FL' },
    {
      name: 'James Houston',
      company: 'Test Corp',
      city: 'Dallas',
      state: 'TX',
    },
  ];

  public constructor(props) {
    super(props);
  }

  public render() {
    return (
      <div>
        <PageHeader title="DataTable" />
        <DataTable
          title="Remote Data"
          dataPromise={this.tableDataPromise}
          scrollable={true}
          onRowClick={this.handleRowClick}
          onRowsDelete={this.handleRowsDelete}
        />
        <br />
        <DataTable
          title="Array Data"
          data={this.arrayData}
          pagination={false}
          onRowClick={this.handleRowClick}
          onRowsDelete={this.handleRowsDelete}
          selectable={false}
        />
        <br />
        <DataTable
          title="Object Data"
          data={this.objectData}
          onRowClick={this.handleRowClick}
          onRowsDelete={this.handleRowsDelete}
          selectable="single"
        />
        <br />
      </div>
    );
  }

  private handleRowClick(rowData: any) {
    alert(JSON.stringify(rowData));
  }

  private handleRowsDelete() {
    return confirm(intl.get('deleteConfirmMessage')).then(() => {
      // TODO: here to call api
    });
  }

  private tableDataPromise(args: DataTableRequestParameters): Promise<any> {
    let url = '/datatable.json';
    if (args) {
      url += `?page=${args.page || 1}`;
      url += `&pageSize=${args.pageSize || 10}`;

      if (args.sort) {
        url += `&sort=${args.sort}&sortDirection=${args.sortDirection}`;
      }
      if (args.searchText) {
        url += `&search=${args.searchText}`;
      }
    }

    const ajax = resourceService.get(url).then((res: any) => {
      res.forEach(item => {
        item.name = item.name + ' for page #' + args.page;
      });
      const result: DataTablePageMeta = {
        data: res,
        page: (args && args.page) || 1,
        count: 132,
      };
      return result;
    });

    const promiseLoading = new Promise(resolve => {
      loading();
      setTimeout(() => {
        loading(false);
        resolve();
      }, 3000);
    });

    return utils
      .delay(3, ajax, promiseLoading)
      .then((values: any[]) => values[0]);
  }
}

export default DataTableExample;

--#

--% /mts-admin/src/pages/auth/index.tsx
export { default as Callback } from './Callback';
export { default as Login } from './Login';
export { default as Logout } from './Logout';

--#

--% /mts-admin/src/pages/auth/Callback.tsx
import * as React from 'react';

import { Alert } from 'app/ui';
import { Url } from 'app/helpers/url';
import { Dispatch, Action } from 'redux';
import { connect } from 'react-redux';
import { push } from 'connected-react-router';

import {
  actions as authActions,
  getAccessTokenUri,
  TokenInfo,
  getValidState,
} from '../../service/auth';
import { Ajax } from 'app/helpers/ajax';

const KEY_CODE = 'code';
const KEY_STATE = 'state';
const KEY_TOKEN = 'access_token';
const KEY_ERROR = 'error_description';

class CallbackComponent extends React.Component<{
  onAuthSuccess: (tokenInfo: TokenInfo) => void;
  push: (path: string) => void;
}> {
  private error: any;

  public constructor(props) {
    super(props);
    const currentUrl = Url.current();
    if (currentUrl.queries[KEY_CODE]) {
      // validate the state
      const state = currentUrl.queries[KEY_STATE] as string;
      if (state === getValidState()) {
        const code = currentUrl.queries[KEY_CODE] as string;
        const ajax = new Ajax().post(getAccessTokenUri(code), null);
        ajax.then((tokenInfo: any) => {
          this.props.onAuthSuccess(tokenInfo);
          this.props.push('/admin');
        });
      } else {
        this.error = 'Invalid state from server.';
      }
    } else if (currentUrl.queries[KEY_TOKEN]) {
      this.props.onAuthSuccess({
        /* eslint-disable-next-line @typescript-eslint/camelcase */
        access_token: currentUrl.queries[KEY_TOKEN] as string,
      });
    } else {
      this.error = currentUrl.queries[KEY_ERROR];
      if (!this.error) {
        this.error = (
          <p>
            Invalid request.{' '}
            <a className={'clickable'} onClick={() => (location.href = '/')}>
              Click here to go home.
            </a>
          </p>
        );
      }
    }
  }

  public render() {
    return (
      <div className="screen-center text-left">
        <Alert
          title={this.error ? 'Oops...' : 'Authorizing...'}
          message={
            this.error ||
            'Application is obtaining authorization from 3rd-party application, please waiting...'
          }
          variant={this.error ? 'error' : 'info'}
        />
      </div>
    );
  }
}

const mapDispatchToProps = (dispatch: Dispatch<Action>) => ({
  onAuthSuccess: (tokenInfo: TokenInfo) => {
    dispatch(authActions.authSuccess(tokenInfo));
  },
  push: (path: string) => {
    dispatch(push(path));
  },
});

export default connect(
  null,
  mapDispatchToProps,
)(CallbackComponent);

--#

--% /mts-admin/src/pages/auth/Login.tsx
import * as React from 'react';
import * as intl from 'react-intl-universal';
import { connect } from 'react-redux';
import { Dispatch, Action } from 'redux';

import { withStyles, createStyles, Theme } from '@material-ui/core/styles';
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import FormControl from '@material-ui/core/FormControl';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Input from '@material-ui/core/Input';
import InputLabel from '@material-ui/core/InputLabel';
import AccountCircleRounded from '@material-ui/icons/AccountCircleRounded';
import Paper from '@material-ui/core/Paper';
import Typography from '@material-ui/core/Typography';

import { actions as authActions } from 'app/service/auth';
import { actions as globalActions } from 'app/service/global';

const styles = (theme: Theme) =>
  createStyles({
    main: {
      width: 'auto',
      display: 'block',
      marginLeft: theme.spacing(3),
      marginRight: theme.spacing(3),
      [theme.breakpoints.up(400 + theme.spacing(6))]: {
        width: 400,
        marginLeft: 'auto',
        marginRight: 'auto',
      },
    },
    paper: {
      marginTop: theme.spacing(8),
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      padding: `${theme.spacing(2)}px ${theme.spacing(
        3,
      )}px ${theme.spacing(3)}px`,
    },
    avatar: {
      margin: theme.spacing(),
      backgroundColor: theme.palette.secondary.main,
      width: 100,
      height: 100,
      fontSize: 110,
    },
    form: {
      width: '100%',
      marginTop: theme.spacing(),
    },
    submit: {
      marginTop: theme.spacing(3),
    },
  });

interface LoginComponentProps {
  history: any;
  classes: any;
  onLogin: (
    username: string,
    password: string,
    rememberMe: boolean,
  ) => boolean;
}

interface LoginComponentState {
  username: string;
  password: string;
  rememberMe: boolean;
}

class Login extends React.Component<LoginComponentProps, LoginComponentState> {
  public constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
      rememberMe: true,
    };
    this.onLogin = this.onLogin.bind(this);
  }

  public render() {
    const { classes } = this.props;
    return (
      <main className={classes.main}>
        <CssBaseline />
        <Paper className={classes.paper}>
          <Avatar className={classes.avatar}>
            <AccountCircleRounded fontSize="inherit" />
          </Avatar>
          <Typography component="h1" variant="h5">
            {intl.get('admin.brand')}
          </Typography>
          <form className={classes.form}>
            <FormControl
              margin="normal"
              required={true}
              fullWidth={true}
            >
              <InputLabel htmlFor="username">
                {intl.get('username')}
              </InputLabel>
              <Input
                id="username"
                name="username"
                type="text"
                autoComplete="username"
                autoFocus={true}
                onChange={e => {
                  this.setState({ username: e.target.value });
                }}
              />
            </FormControl>
            <FormControl
              margin="normal"
              required={true}
              fullWidth={true}
            >
              <InputLabel htmlFor="password">
                {intl.get('password')}
              </InputLabel>
              <Input
                name="password"
                type="password"
                id="password"
                autoComplete="current-password"
                onChange={e => {
                  this.setState({ password: e.target.value });
                }}
              />
            </FormControl>
            <FormControlLabel
              control={
                <Checkbox
                  value="remember"
                  color="primary"
                  checked={this.state.rememberMe}
                  onChange={(e, v) => {
                    this.setState({ rememberMe: v });
                  }}
                />
              }
              label={intl.get('rememberMe')}
            />
            <Button
              type="submit"
              fullWidth={true}
              variant="contained"
              color="primary"
              className={classes.submit}
              onClick={this.onLogin}
            >
              {intl.get('signIn')}
            </Button>
          </form>
        </Paper>
      </main>
    );
  }

  private onLogin(event) {
    this.props.onLogin(
      this.state.username,
      this.state.password,
      this.state.rememberMe,
    );
    event.preventDefault();
  }
}

const mapStateToProps = state => ({
  user: state.auth.user,
});

const mapDispatchToProps = (dispatch: Dispatch<Action>) => ({
  onLogin: (
    username: string,
    password: string,
    rememberMe: boolean,
  ): boolean => {
    if (!username || !password) {
      dispatch(
        globalActions.notify({
          message: 'Please enter your username and password!',
          variant: 'error',
          placement: 'bottom center',
        }),
      );
      return false;
    }
    dispatch(authActions.login({ username, password, rememberMe }));
    return true;
  },
});

export default connect(
  mapStateToProps,
  mapDispatchToProps,
)(withStyles(styles)(Login));

--#

--% /mts-admin/src/pages/auth/Logout.tsx
import * as React from 'react';
import * as intl from 'react-intl-universal';
import classNames from 'classnames';
import { Link } from 'react-router-dom';
import {
  CssBaseline,
  Typography,
  Theme,
  createStyles,
  withStyles,
} from '@material-ui/core';
import { themeConfig } from 'app/theme';
import { Panel } from 'app/ui';
import { Dispatch, Action } from 'redux';
import { connect } from 'react-redux';

import {
  actions as authActions,
  service as authService,
} from '../../service/auth';

const styles = (theme: Theme) =>
  createStyles({
    panel: {
      marginTop: theme.spacing(8),
      marginLeft: 'auto',
      marginRight: 'auto',
      paddingTop: theme.spacing(4),
      paddingBottom: theme.spacing(4),
      width: 400,
      textAlign: 'center',
    },
    body: {
      wordBreak: 'break-all',
    },
    icon: {
      marginBottom: 30,
    },
    success: {
      color: themeConfig.palette.success,
    },
    warning: {
      color: themeConfig.palette.warning,
    },
    textColor: {
      color: theme.palette.text.primary,
    },
  });

interface LogoutComponentProps {
  classes: any;
  handleLogout: () => void;
}

class Logout extends React.Component<
  LogoutComponentProps,
  {
    loading: boolean;
    error: any;
  }
> {
  public constructor(props) {
    super(props);
    this.state = {
      loading: true,
      error: null,
    };
  }

  public componentWillMount() {
    const logoutResult = authService.logout();
    if (logoutResult && logoutResult.then) {
      logoutResult
        .then(null, error => {
          this.setState({ error });
        })
        .finally(() => {
          this.setState({
            loading: false,
          });
        });
    }
    this.props.handleLogout();
  }

  public render() {
    const { classes } = this.props;
    return (
      <main>
        <CssBaseline />
        <Panel
          variant={
            this.state.loading
              ? 'default'
              : this.state.error
              ? 'warning'
              : 'success'
          }
          className={classes.panel}
        >
          {this.state.loading && (
            <div>
              <Typography
                gutterBottom={true}
                component="h1"
                variant="h6"
              >
                Logging out your session...
              </Typography>
            </div>
          )}
          {!this.state.loading &&
            (this.state.error ? (
              <div>
                <i
                  className={classNames(
                    'fa fa-exclamation-triangle fa-5x',
                    classes.icon,
                    classes.warning,
                  )}
                />
                <Typography
                  gutterBottom={true}
                  variant="body2"
                  className={classes.body}
                >
                  {JSON.stringify(this.state.error)}
                </Typography>
              </div>
            ) : (
              <div>
                <i
                  className={classNames(
                    'fa fa-check-circle fa-5x',
                    classes.icon,
                    classes.success,
                  )}
                />
                <Typography
                  gutterBottom={true}
                  component="h1"
                  variant="h6"
                >
                  {intl.get('logout.success')}
                </Typography>
              </div>
            ))}
          {!this.state.loading && (
            <Typography variant="body1">
              <Link className={classes.textColor} to="/">
                {intl.get('goHome')}
              </Link>
            </Typography>
          )}
        </Panel>
      </main>
    );
  }
}

const mapDispatchToProps = (dispatch: Dispatch<Action>) => ({
  handleLogout: () => {
    dispatch(authActions.logout());
  },
});

export default connect(
  null,
  mapDispatchToProps,
)(withStyles(styles)(Logout));

--#

--% /mts-admin/src/redux/reducer.tsx
// tslint:disable-next-line
import { History } from 'history';
import { combineReducers } from 'redux';
import { connectRouter } from 'connected-react-router';
import history from './history';
import { reducer as auth } from 'app/service/auth';
import { reducer as global } from 'app/service/global';

const createRootReducer = (his: History) =>
  combineReducers({
    router: connectRouter(his),
    global,
    auth,
  });

const rootReducer = createRootReducer(history);

export default rootReducer;

--#

--% /mts-admin/src/redux/saga.tsx
import { all } from 'redux-saga/effects';

import { saga as authSaga } from 'app/service/auth';

export default function* rootSaga() {
  yield all([authSaga()]);
}

--#

--% /mts-admin/src/redux/index.tsx
export { default as history } from './history';
export { default as store } from './store';
export { default as createRootReducer } from './reducer';
export { default as createRootSaga } from './saga';

--#

--% /mts-admin/src/redux/store.tsx
import createSagaMiddleware from 'redux-saga';
import { createStore, applyMiddleware, compose, Store } from 'redux';
import { routerMiddleware } from 'connected-react-router';

import history from './history';
import rootSaga from './saga';
import rootReducer from './reducer';

const composeEnhancer: typeof compose =
  (window as any).__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
const appSagaMiddleware = createSagaMiddleware();
const appRouterMiddleware = routerMiddleware(history);

const middlewares = [appRouterMiddleware, appSagaMiddleware];

// Middlewarees only in development
if (process.env.NODE_ENV === 'development') {
  // eslint-disable-next-line @typescript-eslint/no-var-requires
  const { logger } = require('redux-logger');
  middlewares.push(logger);
}

const store: Store<any, any> = createStore(
  rootReducer,
  composeEnhancer(applyMiddleware(...middlewares)),
);

// then run the saga
appSagaMiddleware.run(rootSaga);

if (process.env.NODE_ENV === `development`) {
  // Every time the state changes, log it
  // Note that subscribe() returns a function for unregistering the listener
  const unsubscribe: any = store.subscribe(() => {
    // eslint-disable-next-line no-console
    console.debug(store.getState());
  });

  // Stop listening to state updates
  unsubscribe();
}

export default store;

--#

--% /mts-admin/src/redux/history.tsx
import { createBrowserHistory } from 'history';

// tell eslint below is global variables
// or declare them in globals section of eslint config file.
/* global APP_BASEHREF */
export default createBrowserHistory({
  basename: APP_BASEHREF,
});

--#

--% /mts-admin/src/config/index.tsx
import _merge from 'lodash-es/merge';
import { Config } from './types';
import { config as commonConfig } from './app.common';
import { config as prodConfig } from './app.prod';
import { config as mockConfig } from './app.mock';

// Uncomment or define it in index.html to specify your environment.
// window.__APP_ENV__ = 'github';

let config: Config;
export function getConfig(): Config {
  if (config) {
    return config;
  }

  const env = window.__APP_ENV__ || process.env.NODE_ENV;

  // eslint-disable-next-line no-console
  console.info(`Application is running in '${env}' mode.`);

  switch (env) {
    case 'production':
      config = window.__APP_CONF__ = _merge(commonConfig, prodConfig);
      break;

    case 'development':
      config = window.__APP_CONF__ = _merge(commonConfig, mockConfig);
      break;

    default:
      config = window.__APP_CONF__ = _merge(
        require('./app.common'),
        require(`./app.${env}`),
      );
      break;
  }
  return config;
}

export * from './types';
export { default as adminRoutes } from './routes.admin';
export { default as adminMenus } from './menus.admin';
export { default as userMenus } from './menus.user';

--#

--% /mts-admin/src/config/app.mock.tsx
import { Config, AuthType } from './types';

export const config: Config = {
  authType: AuthType.Mock,
  userConverter: (mockUser: any) => {
    return {
      id: '-1',
      name: mockUser.username,
      email: 'usef@gmail.com',
      avatar: 'https://seeklogo.com/images/U/ufc-logo-9ED3D1B101-seeklogo.com.png',
    };
  },
};

--#

--% /mts-admin/src/config/app.oauth-code.tsx
import { Config, AuthType } from './types';

export const config: Config = {
  authType: AuthType.OAuth,
  authConfig: {
    clientId: 'foo',
    clientSecret: '1',
    authorizationUri:
      'http://localhost:9110/oauth/authorize?response_type=code&client_id={clientId}&redirect_uri={callbackUri}&&scope={scope}',
    accessTokenUri:
      'http://localhost:9110/oauth/token?client_id={clientId}&client_secret={clientSecret}&grant_type=authorization_code&code={code}&redirect_uri={callbackUri}',
    userProfileUri: 'http://localhost:9110/oauth/me',
    logoutUri: 'http://localhost:9110/oauth/logout',
    // clientId: "188c0da703",
    // clientSecret: "f3dd317369ae622113f0",
    // authorizationUri: "https://cloud.bndy.net/service-sso/oauth/authorize?response_type=code&client_id={clientId}&redirect_uri={callbackUri}&&scope={scope}",
    // accessTokenUri: "https://cloud.bndy.net/service-sso/oauth/token?client_id={clientId}&client_secret={clientSecret}&grant_type=authorization_code&code={code}&redirect_uri={callbackUri}",
    // userProfileUri: "https://cloud.bndy.net/service-sso/oauth/me",
    // logoutUri: "https://cloud.bndy.net/service-sso/oauth/logout",
    scope: 'user_info',
  },
  userConverter: (backendUser: any) => {
    return {
      name: backendUser.username,
      email: backendUser.email,
    };
  },
};

--#

--% /mts-admin/src/config/menus.user.tsx
import { MenuItem } from 'app/types';

const menus: MenuItem[] = [
  {
    icon: 'fa fa-cogs',
    text: 'Settings',
    link: '/settings',
  },
  {
    icon: 'fa fa-sign-out',
    text: 'Log out',
    link: '/logout',
  },
];

export default menus;

--#

--% /mts-admin/src/config/menus.admin.tsx
import * as React from 'react';
import BuildIcon from '@material-ui/icons/Build';
import DashboardIcon from '@material-ui/icons/Dashboard';
import DnsIcon from '@material-ui/icons/Dns';
import PeopleIcon from '@material-ui/icons/People';
import BarChartIcon from '@material-ui/icons/BarChart';
import LayersIcon from '@material-ui/icons/Layers';
import { MenuItem } from 'app/types';

const menus: MenuItem[] = [
  {
    icon: 'fa fa-home',
    text: 'Home',
    description: 'Go to public home',
    link: '',
  },
  {
    icon: 'fa fa-tachometer',
    text: 'Dashboard',
    description: '',
    link: '/admin/dashboard',
  },
  {
    icon: 'fa fa-edit',
    text: 'Markdown',
    description: '',
    link: '/admin/markdown',
  },
  {
    icon: 'fa fa-table',
    text: 'DataTable',
    description: '',
    link: '/admin/examples/datatable',
  },
  {
    icon: 'fa fa-exclamation-triangle',
    text: '404 Page',
    description: '',
    link: '/admin/this_page_not_found',
  },
  {
    icon: <DnsIcon />,
    text: 'Behavior',
    description: '',
    link: '',
  },
  {
    icon: <BuildIcon />,
    text: 'Conversions',
    description: '',
    link: '',
  },
  {
    icon: <DashboardIcon />,
    text: 'Others',
    description: '',
    link: '',
    children: [
      {
        icon: <PeopleIcon />,
        text: 'Users',
        description: '',
        link: '',
      },
      {
        icon: <BarChartIcon />,
        text: 'Reports',
        description: '',
        children: [
          {
            icon: <BarChartIcon />,
            text: 'Menu 3-1',
          },
          {
            icon: <BarChartIcon />,
            text: 'Menu 3-2',
          },
          {
            icon: <BarChartIcon />,
            text: 'Menu 3-3',
          },
        ],
      },
      {
        icon: <LayersIcon />,
        text: 'Integrations',
        description: '',
        link: '',
      },
    ],
  },
];

export default menus;

--#

--% /mts-admin/src/config/app.dev.tsx
export { config } from './app.mock';

--#

--% /mts-admin/src/config/app.common.tsx
import { Config } from './types';

export const config: Config = {
  title: 'admin.brand',
  logoUri: 'https://seeklogo.com/images/U/ufc-logo-42740DDFF6-seeklogo.com.png',
  resourceBaseUri: APP_BASEHREF || '/',
  defaultLocale: 'en-US', // empty to use navigator language
  locales: [
    {
      name: 'English',
      value: 'en-US',
      // uncomment that will load locale file(file name format: en-US.json) via ajax
      messages: require('../../assets/locales/json/en-US.json'),
    },
    {
      name: '简体中文',
      value: 'zh-CN',
      messages: require('../../assets/locales/json/zh-CN.json'),
    },
  ],
};

--#

--% /mts-admin/src/config/app.github.tsx
import { Config, AuthType } from './types';

const config: Config = {
  authType: AuthType.OAuth,
  authConfig: {
    clientId: '500bd7533a',
    clientSecret: 'bc55228ce6c70e97f4ee',
    authorizationUri:
      'http://localhost:9100/authorize?redirect_uri={callbackUri}&target=github',
    // clientId: "eb6ab71a97ef2692d857",
    // clientSecret: "014e9f84049964807d751c81658d133a1e37acd3",
    // authorizationUri: "https://cloud.bndy.net/service-oauth/authorize?redirect_uri={callbackUri}&target=github",
    userProfileUri: 'https://api.github.com/user',
    logoutUri: 'https://github.com/logout',
  },
  userConverter: (backendUser: any) => {
    return {
      name: backendUser.name,
      email: backendUser.email,
      avatar: backendUser.avatar_url,
      // TODO: here to map more backend user informations
    };
  },
  logoutHandler: (url: string) => {
    window.location.href = url;
    return;
  },
};

module.exports = config;

--#

--% /mts-admin/src/config/app.prod.tsx
export { config } from './app.mock';

// import _merge from 'lodash-es/merge';
// import { Config } from './types';
// import { config as oauthCodeConfig } from './app.oauth-code';

// export const config: Config = _merge(oauthCodeConfig, {
//     authConfig: {
//         clientId: '188c0da703',
//         clientSecret: 'f3dd317369ae622113f0',
//         authorizationUri:
//             'https://cloud.bndy.net/service-sso/oauth/authorize?response_type=code&client_id={clientId}&redirect_uri={callbackUri}&scope={scope}',
//         accessTokenUri:
//             'https://cloud.bndy.net/service-sso/oauth/token?client_id={clientId}&client_secret={clientSecret}&grant_type=authorization_code&code={code}&redirect_uri={callbackUri}',
//         userProfileUri: 'https://cloud.bndy.net/service-sso/oauth/me',
//         logoutUri: 'https://cloud.bndy.net/service-sso/oauth/logout',
//     },
// });

--#

--% /mts-admin/src/config/types.ts
import { UserInfo, AuthState } from 'app/service/auth';

export enum AuthType {
  OAuth = 'oauth', // alias for OAuthCode
  OAuthCode = 'oauthCode',
  OAuthPassword = 'oauthPassword',
  Custom = 'custom',
  Mock = 'mock',
}

export interface Config {
  title?: string;
  logoUri?: string;
  resourceBaseUri?: string;
  defaultLocale?: string;
  locales?: { name: string; value: string; messages?: any }[];
  authType?: AuthType;
  authConfig?: OAuthConfig;
  userConverter?: (backendUser: any) => UserInfo;
  logoutHandler?: (url: string, authState: AuthState) => void;
}

export interface OAuthConfig {
  clientId: string;
  clientSecret: string;
  authorizationUri: string;
  accessTokenUri?: string;
  userProfileUri: string;
  logoutUri: string;
  callbackUri?: string;
  scope?: string;
}

--#

--% /mts-admin/src/config/routes.admin.tsx
import { Dashboard, Markdown, DataTableExample } from 'app/pages/admin';
import { NotFound } from 'app/pages/public';

const routes = [
  {
    path: '/admin',
    exact: true,
    component: Dashboard,
  },
  {
    path: '/admin/dashboard',
    exact: true,
    component: Dashboard,
  },
  {
    path: '/admin/markdown',
    exact: true,
    component: Markdown,
  },
  {
    path: '/admin/examples/datatable',
    exact: true,
    component: DataTableExample,
  },
  {
    component: NotFound,
  },
];

export default routes;

--#

--% /mts-admin/src/config/app.oauth-password.tsx
import { Config, AuthType } from './types';

export const config: Config = {
  authType: AuthType.OAuthPassword,
  authConfig: {
    clientId: 'foo',
    clientSecret: '1',
    authorizationUri: 'http://localhost:9110/oauth/token',
    userProfileUri: 'http://localhost:9110/oauth/me',
    logoutUri: 'http://localhost:9110/oauth/logout',
    // authorizationUri: "https://cloud.bndy.net/service-sso/oauth/token",
    // userProfileUri: "https://cloud.bndy.net/service-sso/oauth/me",
    // logoutUri: "https://cloud.bndy.net/service-sso/oauth/logout",
  },
  userConverter: (backendUser: any) => {
    return {
      name: backendUser.username,
      email: backendUser.email,
    };
  },
};

--#

--% /mts-admin/src/routers/routes.tsx
import * as React from 'react';
import { Redirect } from 'react-router';
import { isAuthorized, getAuthUri } from 'app/service/auth';
import { Home, NotFound } from 'app/pages/public';
import { Admin } from 'app/pages/admin';
import { Login, Logout, Callback } from 'app/pages/auth';
import { RouteConfig } from 'react-router-config';

export const routes: RouteConfig[] = [
  {
    path: '/',
    exact: true,
    // component: Home,
    /* eslint-disable */
    render: () => {
      if (isAuthorized()) {
        return <Admin />;
      } else {
        if (
          getAuthUri() &&
          !getAuthUri()
            .toLowerCase()
            .startsWith('http')
        ) {
          return <Redirect to={getAuthUri()} />;
        }
      }
      location.href = getAuthUri();
      return null;
    },
  },
  {
    path: '/login',
    component: Login,
  },
  {
    path: '/logout',
    component: Logout,
  },
  {
    path: '/auth/callback',
    component: Callback,
  },
  {
    path: '/admin',
    // `render()` method support in react-router-config v5.0
    /* eslint-disable */
    render: () => {
      if (isAuthorized()) {
        return <Admin />;
      } else {
        if (
          getAuthUri() &&
          !getAuthUri()
            .toLowerCase()
            .startsWith('http')
        ) {
          return <Redirect to={getAuthUri()} />;
        }
      }
      location.href = getAuthUri();
      return null;
    },
  },
  {
    component: NotFound,
  },
];

--#

--% /mts-admin/src/ui/SlidePanel.tsx
import * as React from 'react';
import {
  Theme,
  createStyles,
  withStyles,
  IconButton,
  Drawer,
  Typography,
} from '@material-ui/core';
import CloseIcon from '@material-ui/icons/Close';
import { variantBorderColor } from '../theme';

const styles = (theme: Theme) =>
  createStyles({
    ...variantBorderColor(theme),
    root: {
      backgroundColor: theme.palette.background.default,
    },
    header: {
      display: 'flex',
      alignItems: 'flex-end',
      padding: `${theme.spacing()}px ${theme.spacing(2)}px`,
      borderBottom: `solid 1px ${theme.palette.divider}`,
    },
    headerTitle: {
      flex: 1,
    },
    headerToolbox: {
      flex: 1,
      textAlign: 'right',
    },
    body: {
      padding: `${theme.spacing()}px ${theme.spacing(2)}px`,
    },
  });

class SlidePanel extends React.Component<{
  classes: any;
  className?: string;
  title: string | JSX.Element;
  anchor: 'top' | 'right' | 'left' | 'bottom';
  width: number | string;
  height: number | string;
  open: boolean;
  closeable?: boolean;
  onClose?: () => void;
  onOpen?: () => void;
}> {
  public constructor(props) {
    super(props);
  }

  public render() {
    const {
      classes,
      className,
      anchor,
      title,
      width,
      height,
      open,
    } = this.props;
    const closeable =
      typeof this.props.closeable === 'undefined'
        ? true
        : this.props.closeable;
    return (
      <Drawer
        classes={{ paper: classes.root }}
        anchor={anchor || 'right'}
        open={open}
      >
        <div className={className} style={{ width, height }}>
          {title && (
            <div className={classes.header}>
              <Typography
                className={classes.headerTitle}
                component="h2"
                variant="h5"
              >
                {title}
              </Typography>
              {closeable && (
                <div className={classes.headerToolbox}>
                  <IconButton
                    aria-label="Close"
                    onClick={this.close}
                  >
                    <CloseIcon />
                  </IconButton>
                </div>
              )}
            </div>
          )}
          <div className={classes.body}>{this.props.children}</div>
        </div>
      </Drawer>
    );
  }

  private close = () => {
    this.props.onClose();
  };
}

export default withStyles(styles)(SlidePanel);

--#

--% /mts-admin/src/ui/index.tsx
export { default as ALink } from './ALink';
export { default as Alert } from './Alert';
export { default as PageHeader } from './PageHeader';
export { default as Loading } from './Loading';
export { default as MiniCard } from './MiniCard';
export * from './Notifier';
export { default as Overlay } from './Overlay';
export { default as Panel } from './Panel';
export { default as Tag } from './Tag';
export { default as RawHtml } from './RawHtml';
export { default as SlidePanel } from './SlidePanel';
export { default as LinkButton } from './LinkButton';
export { default as VerticalMenu } from './VerticalMenu';
export { default as HorizontalMenu } from './HorizontalMenu';
export * from './DataTable';

--#

--% /mts-admin/src/ui/VerticalMenu.tsx
import * as React from 'react';
import classNames from 'classnames';
import { Link, LinkProps } from 'react-router-dom';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import { createStyles, withStyles, List, Collapse } from '@material-ui/core';
import ExpandLessIcon from '@material-ui/icons/ExpandLess';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';

import { MenuItem } from 'app/types';
import { themeConfig, AppTheme, ifLayout } from 'app/theme';

const styles = (theme: AppTheme) =>
  createStyles({
    root: {
      '& .MuiListItemIcon-root': {
        color: ifLayout(theme, {
          popular: 'inherit',
        }),
      },
      '& .MuiTypography-colorTextSecondary': {
        color: ifLayout(theme, {
          popular: 'inherit',
        }),
      },
    },
    rootMini: {
      '& $listItem': {
        justifyContent: 'center',
        [theme.breakpoints.down('sm')]: {
          overflow: 'hidden',
        },
      },
      '& $childList.level-1': {
        position: 'absolute',
        width: '100%',
        marginTop: -5,
        backgroundColor: ifLayout(theme, {
          classic: theme.palette.background.paper,
          popular: theme.palette.primary.dark,
        }),
        borderTopRightRadius: 0,
        borderBottomRightRadius: theme.shape.borderRadius,
      },
      '& > li': {
        position: 'relative',
        width: '100%',
      },
      '& > li:hover': {
        width: themeConfig.sidebarWidth,
        backgroundColor: ifLayout(theme, {
          classic: theme.palette.background.paper,
          popular: theme.palette.primary.dark,
        }),
        borderTopRightRadius: theme.shape.borderRadius,
        borderBottomRightRadius: theme.shape.borderRadius,
        boxShadow: theme.shadows[2],
        zIndex: 100,
      },
      '& > li $listItemText': {
        visibility: 'hidden',
      },
      '& > li:hover $listItemText': {
        visibility: 'visible',
      },
      '& > li:hover $childList': {
        display: 'block',
      },

      '& > li $childList': {
        display: 'none',
      },
      '& $expandIcon': {
        display: 'none',
      },
    },
    listItem: {
      paddingLeft: 0,
      paddingRight: 0,
    },
    listItemIcon: {
      marginRight: 0,
      justifyContent: 'center',
    },
    listItemText: {
      paddingLeft: 0,
      paddingRight: 0,
    },
    listItemTextPrimary: {
      fontSize: '0.875rem',
    },
    listItemTextSecondary: {
      fontSize: '0.75rem',
    },
    childList: {
      '& $listItem': {
        paddingLeft: theme.spacing(),
      },
      '& $childList $listItem': {
        paddingLeft: theme.spacing(2),
      },
      '& $childList $childList $listItem': {
        paddingLeft: theme.spacing(3),
      },
    },
    expandIcon: {
      marginRight: 10,
      color: ifLayout(theme, {
        popular: 'inherit',
      }),
    },
  });

class VerticalMenu extends React.Component<
  {
    classes: any;
    mini?: boolean;
    data: MenuItem[];
    width: number | string;
    minWidth: number | string;
  },
  {
    itemHovered: boolean;
    menuStatusSet: { [key: string]: boolean };
  }
> {
  private itemHoveredStyle;

  public constructor(props) {
    super(props);
    this.state = {
      itemHovered: false,
      menuStatusSet: {},
    };
    this.itemHoveredStyle = {
      // width: this.props.width || 200,
    };

    this.handleMenuClick = this.handleMenuClick.bind(this);
    this.handleToggleChildMenu = this.handleToggleChildMenu.bind(this);
  }

  public render() {
    const { classes, mini, data } = this.props;
    return (
      <List
        className={classNames(classes.root, mini && classes.rootMini)}
      >
        {data && data.map(menu => this.renderMenuItem(menu, classes))}
      </List>
    );
  }

  private getMenuKey(menu) {
    return `${menu.text}_${menu.link || ''}`;
  }

  private handleMenuClick(menu) {
    this.handleToggleChildMenu(menu);
  }

  private handleToggleChildMenu(menu) {
    const menuKey = this.getMenuKey(menu);
    if (menu.children) {
      this.setState({
        menuStatusSet: {
          ...this.state.menuStatusSet,
          [menuKey]: !this.state.menuStatusSet[menuKey],
        },
      });
    }
  }

  private renderMenuItem(menu, classes, level?) {
    const menuKey = this.getMenuKey(menu);
    const mini = this.props.mini;
    const getLink = React.forwardRef<HTMLAnchorElement, Partial<LinkProps>>(
      (props, ref) => <Link to={menu.link} {...props} ref={ref as any} />,
    );
    getLink.displayName = 'ListItemLink';
    if (!level) {
      level = 1;
    }
    const ListItemComponent = menu.link ? getLink : null;
    return (
      <li
        key={menuKey}
        style={this.state.itemHovered ? this.itemHoveredStyle : null}
        onMouseEnter={() => this.setState({ itemHovered: true })}
      >
        <ListItem
          button={true}
          className={classes.listItem}
          onClick={() => this.handleMenuClick(menu)}
          component={ListItemComponent}
        >
          <ListItemIcon
            className={classes.listItemIcon}
            style={{ width: this.props.minWidth }}
          >
            {typeof menu.icon !== 'string' ? (
              menu.icon
            ) : (
              <i className={menu.icon} />
            )}
          </ListItemIcon>
          <ListItemText
            className={classes.listItemText}
            classes={{
              primary: classes.listItemTextPrimary,
              secondary: classes.listItemTextSecondary,
            }}
            primary={menu.text}
            secondary={menu.description}
          />
          {menu.children &&
            !mini &&
            (this.state.menuStatusSet[menuKey] ? (
              <ExpandLessIcon
                className={classes.expandIcon}
                onClick={() => this.handleToggleChildMenu(menu)}
              />
            ) : (
              <ExpandMoreIcon
                className={classes.expandIcon}
                onClick={() => this.handleToggleChildMenu(menu)}
              />
            ))}
        </ListItem>
        {menu.children &&
          (mini ? (
            <List
              className={classNames(
                classes.childList,
                `level-${level}`,
              )}
            >
              {menu.children.map(child =>
                this.renderMenuItem(child, classes, level + 1),
              )}
            </List>
          ) : (
            <Collapse
              in={!!this.state.menuStatusSet[menuKey]}
              timeout="auto"
            >
              <List
                className={classNames(
                  classes.childList,
                  `level-${level}`,
                )}
              >
                {menu.children.map(child =>
                  this.renderMenuItem(
                    child,
                    classes,
                    level + 1,
                  ),
                )}
              </List>
            </Collapse>
          ))}
      </li>
    );
  }
}

export default withStyles(styles)(VerticalMenu);

--#

--% /mts-admin/src/ui/Overlay.tsx
import * as React from 'react';
import classNames from 'classnames';
import { createStyles, Theme, withStyles } from '@material-ui/core';
import { fade } from '@material-ui/core/styles/colorManipulator';

const styles = (theme: Theme) =>
  createStyles({
    overlay: {
      position: 'fixed',
      top: 0,
      left: 0,
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      width: '100%',
      height: '100vh',
      backgroundColor: fade(theme.palette.background.default, 0.5),
      zIndex: 9999,
    },
    overlayClose: {
      display: 'none',
    },
  });

class Overlay extends React.Component<{ classes: any; open: boolean }, {}> {
  public render() {
    const { classes, open } = this.props;
    return (
      <div
        className={classNames(
          classes.overlay,
          !open && classes.overlayClose,
        )}
      >
        {this.props.children}
      </div>
    );
  }
}

export default withStyles(styles)(Overlay);

--#

--% /mts-admin/src/ui/RawHtml.tsx
import * as React from 'react';

export default class RawHtml extends React.Component<{
  content: string;
}> {
  public render() {
    return <div dangerouslySetInnerHTML={this.createMarkup()} />;
  }

  private createMarkup() {
    return {
      __html: this.props.content
        .replace('<', '&lt;')
        .replace('>', '&gt;'),
    };
  }
}

--#

--% /mts-admin/src/ui/Panel.tsx
import * as React from 'react';
import classNames from 'classnames';
import {
  Paper,
  Theme,
  createStyles,
  withStyles,
  Typography,
  IconButton,
  Collapse,
} from '@material-ui/core';
import AddIcon from '@material-ui/icons/Add';
import CloseIcon from '@material-ui/icons/Close';
import RemoveIcon from '@material-ui/icons/Remove';
import { variantBorderColor } from '../theme';

export const getPanelIconButtonStyle = (theme: Theme) => ({
  padding: theme.spacing() / 2,
});

const panelStyles = (theme: Theme) =>
  createStyles({
    ...variantBorderColor(theme),
    root: {
      marginBottom: theme.spacing(2),
    },
    rootForBordered: {
      borderTopStyle: 'solid',
    },
    header: {
      display: 'flex',
      alignItems: 'center',
      borderBottom: `solid 1px ${theme.palette.divider}`,
      padding: `${theme.spacing() / 2}px ${theme.spacing() +
        1}px ${theme.spacing() / 2}px ${theme.spacing(1.5)}px`,
    },
    headerForNonBordered: {
      paddingTop: theme.spacing() / 2 + 2,
    },
    headerForCollapsed: {
      borderBottom: 'none',
    },
    headerTitle: {
      flex: 1,
    },
    headerToolbox: {
      display: 'flex',
      alignItems: 'center',
    },
    headerToolboxButton: getPanelIconButtonStyle(theme),
    body: {
      padding: `${theme.spacing()}px ${theme.spacing(1.5)}px`,
    },
  });

class Panel extends React.Component<
  {
    classes: any;
    className?: string;
    title?: string | JSX.Element;
    variant?: string;
    closeable?: boolean;
    minimizeable?: boolean;
    bodyPadding?: string;
    actions?: any[];
  },
  { open: boolean; collapsed: boolean; collapsedDone: boolean }
> {
  public constructor(props) {
    super(props);
    this.state = {
      open: true,
      collapsed: false,
      collapsedDone: false,
    };
  }

  public render() {
    const { classes, className, title, bodyPadding, actions } = this.props;
    const actionEls = [];
    if (actions) {
      actions.forEach((action: any, index) => {
        actionEls.push(
          React.cloneElement(action, {
            className:
              action.type === IconButton
                ? classes.headerToolboxButton
                : '',
            key: `ACTION-${index}`,
          }),
        );
      });
    }
    return (
      <Collapse in={this.state.open}>
        <Paper
          className={classNames(
            classes.root,
            classes[this.props.variant],
            this.props.variant && classes.rootForBordered,
            className,
          )}
        >
          {title && (
            <div
              className={classNames(
                classes.header,
                this.state.collapsedDone &&
                  classes.headerForCollapsed,
                this.props.variant ||
                  classes.headerForNonBordered,
              )}
            >
              <Typography
                className={classes.headerTitle}
                variant="subtitle1"
                component="h4"
              >
                {title}
              </Typography>
              <div className={classes.headerToolbox}>
                {actionEls}
                {this.props.minimizeable && (
                  <IconButton
                    className={classes.headerToolboxButton}
                    onClick={() =>
                      this.setState({
                        collapsed: !this.state
                          .collapsed,
                      })
                    }
                  >
                    {this.state.collapsed ? (
                      <AddIcon />
                    ) : (
                      <RemoveIcon />
                    )}
                  </IconButton>
                )}
                {this.props.closeable && (
                  <IconButton
                    className={classes.headerToolboxButton}
                    onClick={() =>
                      this.setState({ open: false })
                    }
                  >
                    <CloseIcon />
                  </IconButton>
                )}
              </div>
            </div>
          )}
          <Collapse
            in={!this.state.collapsed}
            onEnter={() => this.setState({ collapsedDone: false })}
            onExited={() => this.setState({ collapsedDone: true })}
          >
            <div
              className={classes.body}
              style={{ padding: bodyPadding }}
            >
              <Typography component="div">
                {this.props.children}
              </Typography>
            </div>
          </Collapse>
        </Paper>
      </Collapse>
    );
  }
}

export default withStyles(panelStyles)(Panel);

--#

--% /mts-admin/src/ui/MiniCard.tsx
import * as React from 'react';
import { Link } from 'react-router-dom';
import classNames from 'classnames';
import {
  Paper,
  Theme,
  createStyles,
  withStyles,
  Typography,
} from '@material-ui/core';
import { fade } from '@material-ui/core/styles/colorManipulator';
import { variantColor } from '../theme';

const miniCardStyles = (theme: Theme) =>
  createStyles({
    ...variantColor(theme),
    root: {
      position: 'relative',
      color:
        theme.palette.type === 'light'
          ? ''
          : theme.palette.text.primary,
      '&:hover $icon': {
        transform: 'scale(4)',
      },
    },
    body: {
      padding: `${theme.spacing()}px ${theme.spacing(
        1.5,
      )}px ${theme.spacing(2)}px ${theme.spacing(1.5)}px`,
    },
    icon: {
      position: 'absolute',
      top: theme.spacing(),
      right: theme.spacing(),
      opacity: 0.3,
      transform: 'scale(3.5)',
      transformOrigin: 'top right',
      transition: 'all .2s ease-in-out',
    },
    linkContainer: {
      display: 'flex',
      backgroundColor: fade(theme.palette.common.black, 0.1),
      borderBottomLeftRadius: 4,
      borderBottomRightRadius: 4,
      overflow: 'hidden',
      '& > *': {
        flex: 1,
        display: 'block',
        textAlign: 'center',
        paddingTop: theme.spacing() / 4,
        paddingBottom: theme.spacing() / 4,
        opacity: 0.8,
        '&:hover': {
          backgroundColor: fade(theme.palette.common.black, 0.2),
          opacity: 1,
        },
      },
    },
  });

class MiniCard extends React.Component<
  {
    classes: any;
    className?: string;
    title: string;
    description: string;
    icon: any;
    variant?: string;
    links: { [key: string]: string };
  },
  {}
> {
  public constructor(props) {
    super(props);
  }

  public render() {
    const {
      classes,
      className,
      icon,
      title,
      description,
      links,
    } = this.props;
    const linkEls = [];
    if (links) {
      for (const key of Object.keys(links)) {
        linkEls.push(this.getLink(key, links[key]));
      }
    }
    return (
      <Paper
        className={classNames(
          classes.root,
          classes[this.props.variant],
          className,
        )}
      >
        <div className={classes.body}>
          <Typography color="inherit" variant="h4" component="h4">
            {title}
          </Typography>
          <Typography color="inherit" variant="caption">
            {description}
          </Typography>
        </div>
        <div className={classes.icon}>{icon}</div>
        <Typography
          className={classes.linkContainer}
          color="inherit"
          variant="caption"
          component="div"
        >
          {linkEls}
        </Typography>
      </Paper>
    );
  }

  private getLink(text: string, url?: string): JSX.Element {
    if (url) {
      if (url.indexOf('://') > 0) {
        return (
          <Typography color="inherit" variant="caption" key={text}>
            <a href={url} target="_blank" rel="noopener noreferrer">
              {' '}
              {text}{' '}
            </a>
          </Typography>
        );
      } else {
        return (
          <Link color="default" key={text} to={url}>
            <Typography color="inherit" variant="caption">
              {text}
            </Typography>
          </Link>
        );
      }
    } else {
      return (
        <Typography color="inherit" variant="caption" key={text}>
          {text}
        </Typography>
      );
    }
  }
}

export default withStyles(miniCardStyles)(MiniCard);

--#

--% /mts-admin/src/ui/ALink.tsx
import * as React from 'react';
import { Link } from 'react-router-dom';
import { Typography } from '@material-ui/core';

export default class ALink extends React.Component<{
  to: string;
}> {
  public constructor(props) {
    super(props);
  }

  public render() {
    let result;
    const { to, ...others } = this.props;
    const isEmptyLink = !this.props.to;
    const isExternalLink =
      this.props.to &&
      this.props.to
        .toString()
        .toLowerCase()
        .startsWith('http');
    if (isEmptyLink) {
      result = (
        <a {...others}>
          <Typography color="inherit" component="span">
            {this.props.children}
          </Typography>
        </a>
      );
    } else if (isExternalLink) {
      result = (
        <a href={to as string} {...others}>
          <Typography color="inherit" component="span">
            {this.props.children}
          </Typography>
        </a>
      );
    } else {
      result = (
        <Link to={to} {...others}>
          <Typography color="inherit">
            {this.props.children}
          </Typography>
        </Link>
      );
    }
    return result;
  }
}

--#

--% /mts-admin/src/ui/LinkButton.tsx
import * as React from 'react';
import classNames from 'classnames';
import { Button, createStyles, withStyles } from '@material-ui/core';
import { ButtonProps } from '@material-ui/core/Button';
import ALink from './ALink';

interface LinkButtonProps extends ButtonProps {
  to: string;
  classes: any;
  contentAlign?: 'left' | 'center' | 'right';
  square?: boolean;
}

const styles = () =>
  createStyles({
    root: {
      width: '100%',
    },
    rootSquare: {
      borderRadius: 0,
    },
    labelLeft: {
      justifyContent: 'left',
    },
    labelRight: {
      justifyContent: 'right',
    },
  });

class LinkButton extends React.Component<LinkButtonProps, {}> {
  public render() {
    const { classes, to, contentAlign, square, ...others } = this.props;
    return (
      <Button
        className={classNames(square && classes.rootSquare)}
        classes={{
          label: classNames(
            contentAlign === 'left' && classes.labelLeft,
            contentAlign === 'right' && classes.labelRight,
          ),
        }}
        {...others}
      >
        <ALink to={to}>{this.props.children}</ALink>
      </Button>
    );
  }
}

export default withStyles(styles)(LinkButton);

--#

--% /mts-admin/src/ui/Alert.tsx
import * as React from 'react';
import classNames from 'classnames';

import Paper from '@material-ui/core/Paper';
import CloseIcon from '@material-ui/icons/Close';
import {
  createStyles,
  Theme,
  withStyles,
  Typography,
  Collapse,
  IconButton,
} from '@material-ui/core';

import { variantIcon, variantColor } from '../theme';

const styles = (theme: Theme) =>
  createStyles({
    ...variantColor(theme),
    root: {
      position: 'relative',
      padding: `${theme.spacing(1.5)}px ${theme.spacing(2)}px`,
      marginBottom: theme.spacing(2),
    },
    header: {
      display: 'flex',
    },
    icon: {
      marginRight: theme.spacing() / 2,
      position: 'relative',
      marginTop: 3,
      fontSize: '1.2em',
    },
    title: {
      flex: 1,
      paddingRight: 24,
    },
    message: {
      marginLeft: 2,
    },
    close: {
      position: 'absolute',
      top: 4,
      right: 4,
    },
  });

class Alert extends React.Component<
  {
    classes: any;
    className?: string;
    title: string;
    message?: string;
    shadow?: number;
    variant?: string;
    square?: boolean;
    closeable?: boolean;
  },
  { close: boolean }
> {
  public constructor(props) {
    super(props);
    this.state = {
      close: false,
    };
    this.handleClose = this.handleClose.bind(this);
  }

  public render() {
    const {
      classes,
      className,
      title,
      message,
      shadow,
      variant,
      square,
      closeable,
    } = this.props;
    const Icon = variantIcon[variant];
    return (
      <Collapse in={!this.state.close} className={className}>
        <Paper
          className={classNames(classes.root, classes[variant])}
          elevation={shadow}
          square={square}
        >
          {title && (
            <Typography
              className={classes.header}
              variant="subtitle1"
              component="h3"
              color="inherit"
            >
              <Icon className={classes.icon} />
              <span className={classes.title}>{title}</span>
            </Typography>
          )}
          {message && (
            <Typography
              className={classes.message}
              component="p"
              color="inherit"
            >
              {message}
            </Typography>
          )}
          {closeable && (
            <IconButton
              key="close"
              aria-label="Close"
              color="inherit"
              className={classes.close}
              onClick={this.handleClose}
            >
              <CloseIcon fontSize="small" />
            </IconButton>
          )}
        </Paper>
      </Collapse>
    );
  }

  private handleClose() {
    this.setState({
      close: true,
    });
  }
}

export default withStyles(styles)(Alert);

--#

--% /mts-admin/src/ui/Notifier.tsx
import * as React from 'react';
import classNames from 'classnames';
import CloseIcon from '@material-ui/icons/Close';
import IconButton from '@material-ui/core/IconButton';
import Snackbar, { SnackbarOrigin } from '@material-ui/core/Snackbar';
import SnackbarContent from '@material-ui/core/SnackbarContent';
import { withStyles, Theme, createStyles } from '@material-ui/core/styles';
import { ifTheme, variantIcon, variantColor } from '../theme';

const notifierContentStyles = (theme: Theme) =>
  createStyles({
    ...variantColor(theme),
    common: {
      opacity: 0.9,
      paddingLeft: theme.spacing(2),
      paddingRight: theme.spacing(5),
    },
    info: {
      backgroundColor: ifTheme(
        theme,
        theme.palette.common.black,
        theme.palette.common.white,
      ),
    },
    icon: {
      fontSize: 20,
    },
    iconVariant: {
      opacity: 0.9,
      marginRight: theme.spacing(),
    },
    message: {
      display: 'flex',
      alignItems: 'center',
    },
    close: {
      position: 'absolute',
      top: 3,
      right: 0,
    },
  });

interface NotifierContentProps {
  classes?: any;
  className?: string;
  message?: string;
  hasCloseButton?: boolean;
  onCloseButtonClick?: (event: any) => void;
  onClose?: (event: any) => void;
  variant?: string;
}

class NotifierContentComponent extends React.Component<
  NotifierContentProps,
  {}
> {
  public constructor(props) {
    super(props);
  }

  public render() {
    const {
      classes,
      className,
      message,
      onCloseButtonClick,
      variant,
    } = this.props;
    const Icon = variantIcon[variant];
    const actions = [];

    if (this.props.hasCloseButton) {
      actions.push(
        <IconButton
          key="close"
          aria-label="Close"
          color="inherit"
          className={classes.close}
          onClick={onCloseButtonClick}
        >
          <CloseIcon className={classes.icon} />
        </IconButton>,
      );
    }
    return (
      <SnackbarContent
        className={classNames(
          classes.common,
          classes[variant],
          className,
        )}
        aria-describedby="client-snackbar"
        message={
          <span id="client-snackbar" className={classes.message}>
            <Icon
              className={classNames(
                classes.icon,
                classes.iconVariant,
              )}
            />
            {message}
          </span>
        }
        action={actions}
      />
    );
  }
}

const NotifierContent = withStyles(notifierContentStyles)(
  NotifierContentComponent,
);

export interface NotifierOptions {
  message: string;
  variant?: string;
  placement?: string;
  duration?: number;
}

interface NotifierProps {
  classes?: any;
  options: NotifierOptions;
  placement?: string;
  open?: boolean;
  hasCloseButton?: boolean;
  onCloseButtonClick?: (event: any) => void;
}

interface NotifierState {
  open: boolean;
}

const NotifierStyles = () =>
  createStyles({
    root: {
      maxWidth: 640,
    },
  });

class NotifierComponent extends React.Component<NotifierProps, NotifierState> {
  public constructor(props) {
    super(props);
    this.state = {
      open: false,
    };
  }

  public render() {
    const { classes, hasCloseButton, onCloseButtonClick } = this.props;
    // const defaultNotifierOptions = {} as NotifierOptions;
    const open = this.props.open || this.state.open;
    const options = (this.props.options || {}) as NotifierOptions;
    let origin: SnackbarOrigin = {
      vertical: 'bottom',
      horizontal: 'right',
    };
    if (options.placement) {
      const p = options.placement.split(' ');
      origin = {
        vertical: p[0] as 'bottom',
        horizontal: p[1] as 'right',
      };
    }
    return (
      <Snackbar
        className={classes.root}
        anchorOrigin={origin}
        open={open}
        autoHideDuration={options.duration || 5000}
        onClose={this.handleClose}
      >
        <NotifierContent
          onClose={this.handleClose}
          hasCloseButton={hasCloseButton}
          onCloseButtonClick={onCloseButtonClick}
          variant={options.variant || 'info'}
          message={options.message || ''}
        />
      </Snackbar>
    );
  }

  private handleClose = e => {
    this.setState({
      open: false,
    });
    if (this.props.onCloseButtonClick) {
      this.props.onCloseButtonClick(e);
    }
  };
}

export const Notifier = withStyles(NotifierStyles)(NotifierComponent);

--#

--% /mts-admin/src/ui/PageHeader.tsx
import * as React from 'react';
import { Link } from 'react-router-dom';

import Typography from '@material-ui/core/Typography';
import { createStyles, Theme, withStyles } from '@material-ui/core';

const styles = (theme: Theme) =>
  createStyles({
    pageHeader: {
      display: 'flex',
      paddingTop: theme.spacing(2),
      paddingBottom: theme.spacing(),
      marginBottom: theme.spacing(2),
      '& h2': {
        flex: 1,
      },
      '& > *': {
        alignSelf: 'flex-end',
      },
    },
    breadcrumb: {
      display: 'flex',
      '& > *': {
        color: theme.palette.text.primary,
        textDecoration: 'none',
      },
      '& > *:not(:last-child):after': {
        content: '">"',
        display: 'inline-block',
        marginLeft: 5,
        marginRight: 5,
      },
      '& > span': {
        color: theme.palette.text.disabled,
      },
    },
    toolbox: {
      display: 'flex',
      '& > *': {
        display: 'flex',
      },
    },
  });

const renderNavItem = navigation => {
  const items = [];
  for (const key of Object.keys(navigation)) {
    items.push(
      navigation[key] ? (
        <Link key={key} to={navigation[key]}>
          {key}
        </Link>
      ) : (
        <span key={key}>{key}</span>
      ),
    );
  }
  return items;
};

class PageHeader extends React.Component<
  {
    classes: any;
    title: string | JSX.Element;
    toolbox?: JSX.Element;
    navigation?: { [key: string]: string };
  },
  {}
> {
  public render() {
    const { classes, title, navigation, toolbox } = this.props;
    return (
      <div className={classes.pageHeader}>
        <Typography component="h2" variant="h5">
          {title}
        </Typography>
        {navigation && (
          <Typography
            variant="caption"
            className={classes.breadcrumb}
          >
            {renderNavItem(navigation)}
          </Typography>
        )}
        {toolbox && <div className={classes.toolbox}>{toolbox}</div>}
      </div>
    );
  }
}

export default withStyles(styles)(PageHeader);

--#

--% /mts-admin/src/ui/Loading.tsx
import * as React from 'react';
import {
  createStyles,
  Theme,
  withStyles,
  CircularProgress,
  Typography,
} from '@material-ui/core';
import { fade } from '@material-ui/core/styles/colorManipulator';

const styles = (theme: Theme) =>
  createStyles({
    circularProgressContainer: {
      backgroundColor: theme.palette.background.paper,
      padding: theme.spacing(2),
      borderStyle: 'solid',
      borderWidth: 2,
      borderColor: fade(theme.palette.primary.main, 0.2),
      borderRadius: theme.shape.borderRadius,
      textAlign: 'center',
    },
    circularProgressWrapper: {
      position: 'relative',
      display: 'inline-block',
      margin: theme.spacing(2),
    },
    circularProgressDeterminate: {
      color: fade(theme.palette.primary.main, 0.2),
    },
    circularProgressIndeterminate: {
      color: theme.palette.primary.main,
      animationDuration: '600ms',
      position: 'absolute',
      left: 0,
    },
    circularProgressText: {
      display: 'block',
      textAlign: 'center',
    },
  });

class Loading extends React.Component<
  { classes: any; loadingText?: string },
  {}
> {
  public render() {
    const { classes, loadingText } = this.props;
    return (
      <div className={classes.circularProgressContainer}>
        <div className={classes.circularProgressWrapper}>
          <CircularProgress
            variant="determinate"
            value={100}
            className={classes.circularProgressDeterminate}
            size={48}
            thickness={4}
          />
          <CircularProgress
            variant="indeterminate"
            disableShrink={true}
            className={classes.circularProgressIndeterminate}
            size={48}
            thickness={4}
          />
        </div>
        {loadingText && (
          <Typography
            classes={{ root: classes.circularProgressText }}
          >
            {' '}
            {loadingText}{' '}
          </Typography>
        )}
      </div>
    );
  }
}

export default withStyles(styles)(Loading);

--#

--% /mts-admin/src/ui/DataTable.tsx
import * as React from 'react';
import * as intl from 'react-intl-universal';
import _merge from 'lodash-es/merge';
import MUIDataTable from 'mui-datatables';
import { createStyles, withStyles } from '@material-ui/core';

export type SortDirection = 'asc' | 'desc';
export interface DataTableColumn {
  key: string;
  title: string;
  hint?: string;
  filter?: boolean;
  filterType?: 'checkbox' | 'dropdown' | 'multiselect' | 'textField';
  sort?: boolean;
  sortDirection?: SortDirection;
  searchable?: boolean;
  displayInPrint?: boolean;
  displayInDownloadCsv?: boolean;
}

export interface DataTablePageMeta {
  page: number;
  count: number;
  data: any[];
}

export interface DataTableOptions {
  sort?: boolean;
  filter?: boolean;
  search?: boolean;
  print?: boolean;
  download?: boolean;
  viewColumns?: boolean;
  selectableRows?: 'multiple' | 'single' | 'none';
}

export interface MuiDataTableState {
  announceText?: string;
  page: number;
  rowsPerPage: number;
  filterList: any[];
  selectedRows: {
    data: any[];
    lookup: object;
  };
  showResponsive: boolean;
  searchText?: string;
}

export interface DataTableRequestParameters {
  sort?: string;
  sortDirection?: SortDirection;
  page?: number;
  pageSize?: number;
  searchText?: string;
}

export interface DataTableProps {
  classes: any;
  data?: any[];
  columns?: DataTableColumn[];
  options?: DataTableOptions | any;
  className?: string;
  title?: string;
  rowsPerPageOptions?: number[];
  pagination?: boolean;
  scrollable?: boolean;
  selectable?: 'multiple' | 'single' | 'none' | boolean;
  localePrefix?: string;
  onRowClick?: (rowData: any, dataIndex: number) => void;
  onRowsDelete?: (rowsData: any[]) => Promise<any>;
  dataPromise?: (
    parameters?: DataTableRequestParameters,
  ) => Promise<DataTablePageMeta>;
}

export interface DataTableState extends DataTableRequestParameters {
  isLoading: boolean;
  data?: any[];
  recordCount?: number;
}

const styles = () => createStyles({});

class DataTableComponent extends React.Component<
  DataTableProps,
  DataTableState
> {
  private data: any[];
  private columns: any[];
  private searchDelayTimer: any;
  private rowsPerPageOptions: number[];
  private defaultRowsPerPageOptions: number[] = [10, 20, 50];

  public constructor(props: Readonly<DataTableProps>) {
    super(props);
    this.rowsPerPageOptions =
      this.props.rowsPerPageOptions || this.defaultRowsPerPageOptions;
    this.state = {
      page: 1,
      isLoading: false,
      recordCount: 0,
      pageSize: this.rowsPerPageOptions[0],
    };
  }

  public componentDidMount() {
    this.getData();
  }

  public componentWillUnmount() {
    if (this.searchDelayTimer) {
      clearTimeout(this.searchDelayTimer);
    }
  }

  public render() {
    this.data = this.props.data || this.state.data;
    const { title, options } = this.props;
    const { isLoading } = this.state;
    const defaultOptions = {
      filterType: 'dropdown',
      responsive: 'scroll',
      selectableRows:
        this.props.selectable === true
          ? 'multiple'
          : this.props.selectable === false
          ? 'none'
          : this.props.selectable,
      textLabels: {
        body: {
          noMatch: isLoading
            ? intl.get('loadingData')
            : intl.get('noData'),
        },
        filter: {
          all: intl.get('all'),
          title: intl.get('filters'),
          reset: intl.get('reset'),
        },
        selectedRows: {
          text: intl.get('itemsSelected'),
          delete: intl.get('delete'),
          deleteAria: intl.get('delete'),
        },
        pagination: {
          next: intl.get('nextPage'),
          previous: intl.get('previousPage'),
          rowsPerPage: intl.get('rowsPerPage'),
          displayRows: intl.get('of'),
        },
        toolbar: {
          search: intl.get('search'),
          downloadCsv: intl.get('downloadCsv'),
          print: intl.get('print'),
          viewColumns: intl.get('viewColumns'),
          filterTable: intl.get('filter'),
        },
        viewColumns: {
          title: intl.get('viewColumns'),
          titleAria: intl.get('toggleColumns'),
        },
      },
    };

    if (!this.props.columns) {
      this.generateColumnsFromData();
    } else {
      this.generateColumnsFromProps();
    }

    if (this.state.sort) {
      this.columns.forEach(column => {
        if (column.label === this.state.sort) {
          column.options.sortDirection =
            this.state.sortDirection || 'asc';
        }
      });
    }

    const finalOptions = _merge(defaultOptions, options, {
      responsive: this.props.scrollable ? 'scroll' : 'stacked',
      pagination:
        typeof this.props.pagination === 'undefined'
          ? true
          : this.props.pagination,
      count: this.state.recordCount,
      page: this.state.page - 1,
      rowsPerPage: this.state.pageSize,
      rowsPerPageOptions: this.rowsPerPageOptions,
      onRowClick: (
        rowData: string[],
        rowMeta: { dataIndex: number; rowIndex: number },
      ) => {
        if (this.props.onRowClick) {
          this.props.onRowClick(
            this.data[rowMeta.dataIndex],
            rowMeta.dataIndex,
          );
        }
      },
      onRowsDelete: (rowsDeleted: {
        lookup: { [dataIndex: number]: boolean };
        data: { index: number; dataIndex: number }[];
      }) => {
        if (this.props.onRowsDelete) {
          const needDeleteRows = [];
          rowsDeleted.data.forEach(item => {
            needDeleteRows.push(this.data[item.dataIndex]);
          });
          this.props.onRowsDelete(needDeleteRows).then(() => {
            this.getData();
          });
          // false to prevent the deletion on UI
          return false;
        }
        return true;
      },
      onSearchChange: (searchText: string) => {
        if (this.searchDelayTimer) {
          clearTimeout(this.searchDelayTimer);
        }
        this.searchDelayTimer = setTimeout(() => {
          this.setState(
            {
              page: 1,
              searchText,
            },
            () => {
              this.getData();
            },
          );
        }, 1000);
      },
      onSearchClose: () => {
        this.setState(
          {
            page: 1,
            searchText: null,
          },
          () => {
            this.getData();
          },
        );
      },
      onChangePage: (currentPage: number) => {
        this.setState(
          {
            page: currentPage + 1,
          },
          () => {
            this.getData();
          },
        );
      },
      onColumnSortChange: (column: string) => {
        let sortDirection: SortDirection = 'asc';
        if (
          column === this.state.sort &&
          this.state.sortDirection === 'asc'
        ) {
          sortDirection = 'desc';
        }
        const changedState = this.props.dataPromise
          ? {
              page: 1,
              sort: column,
              sortDirection,
            }
          : {
              sort: column,
              sortDirection,
            };
        this.setState(changedState, () => {
          this.getData();
        });
      },
      onTableChange: (action: string, tableState: MuiDataTableState) => {
        switch (action) {
          case 'changeRowsPerPage':
            this.setState(
              {
                page: 1,
                pageSize: tableState.rowsPerPage,
              },
              () => {
                this.getData();
              },
            );
            break;
        }
      },
    });

    if (this.props.dataPromise) {
      finalOptions.serverSide = true;
    }

    // The `key` attribute for fixing count does not refresh in pagination
    // More info: https://github.com/gregnb/mui-datatables/issues/610
    return (
      <MUIDataTable
        key={this.state.recordCount}
        title={title}
        count={this.state.recordCount}
        data={this.data}
        columns={this.columns}
        options={finalOptions}
      />
    );
  }

  private getData() {
    if (this.props.dataPromise) {
      this.setState({
        isLoading: true,
      });
      this.props
        .dataPromise(this.state)
        .then((result: DataTablePageMeta) => {
          const totalPages = Math.ceil(
            result.count / this.state.pageSize,
          );
          this.setState({
            isLoading: false,
            data: result.data,
            recordCount: result.count,
            page:
              result.page > totalPages ? totalPages : result.page,
          });
        });
    }
  }

  private generateColumnsFromProps() {
    this.columns = [];
    this.props.columns.forEach(column => {
      this.columns.push({
        name: column.title,
        label: column.key,
        hint: column.hint,
        options: {
          filter: column.filter,
          filterType: column.filterType,
          sort: column.sort,
          sortDirection: column.sortDirection,
          print: column.displayInPrint,
          download: column.displayInDownloadCsv,
          searchable: column.searchable,
        },
      });
    });
  }

  private generateColumnsFromData() {
    if (this.data && this.data.length > 0) {
      if (Array.isArray(this.data[0])) {
        this.columns = this.data[0];
        this.data = this.data.slice(1);
      } else {
        this.columns = [];
        for (const key of Object.keys(this.data[0])) {
          this.columns.push({
            name: intl
              .get(`${this.props.localePrefix || ''}${key}`)
              .defaultMessage(key),
            label: key,
            options: {
              filter: true,
              sort: true,
            },
          });
        }
      }
    }
  }
}

export const DataTable = withStyles(styles)(DataTableComponent);

--#

--% /mts-admin/src/ui/Chart.tsx
import * as React from 'react';
import classNames from 'classnames';
import {
  ResponsiveContainer,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  Line,
  LineType,
  ComposedChart,
  Bar,
  Area,
  Surface,
  Symbols,
  IconType,
  LegendProps,
} from 'recharts';
import {
  CircularProgress,
  createStyles,
  withStyles,
  Theme,
} from '@material-ui/core';
import { fade } from '@material-ui/core/styles/colorManipulator';

export interface Serie {
  key: string;
  label: string;
  color?: string;
  width?: number;
  type?: 'area' | 'line' | 'bar';
  legendIconType?:
    | 'circle'
    | 'cross'
    | 'diamond'
    | 'square'
    | 'star'
    | 'triangle'
    | 'wye';
  visualizationType?: LineType;
}

const styles = (theme: Theme) =>
  createStyles({
    root: {
      position: 'relative',
    },
    loadingBox: {
      position: 'absolute',
      top: 0,
      margin: `0 auto`,
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      backgroundColor: fade(theme.palette.background.paper, 0.6),
    },
    legendItemInactive: {
      color: theme.palette.grey[500],
    },
  });

interface ChartLegendContentProps extends LegendProps {
  classes?: { itemInactive: string };
  series: Serie[];
  onItemClick: (serie: Serie) => void;
}

const ICON_SIZE = 32;

class ChartLegendContent extends React.Component<
  ChartLegendContentProps,
  {
    offSeries: any;
  }
> {
  public constructor(props) {
    super(props);
    this.state = {
      offSeries: {},
    };
  }

  public render() {
    const { classes, align, iconSize } = this.props;
    return (
      <div
        className="customized-legend"
        style={{
          textAlign: align,
        }}
      >
        {this.props.series &&
          this.props.series.map((serie, index) => {
            const { key, label } = serie;
            const inactive = !!this.state.offSeries[key];
            const margin = {
              left: `0 16px 0 0`,
              right: `0 0 0 16px`,
              center: `0 8px 0 8px`,
            };
            const itemStyles = {
              margin: margin[align],
              cursor: 'pointer',
              display: 'inline-flex',
              alignItems: 'center',
            };

            return (
              <span
                key={`legend-item-${index}`}
                className={classNames(
                  'legend-item',
                  inactive && classes.itemInactive,
                )}
                onClick={() =>
                  this.handleLegendItemClick(serie)
                }
                style={itemStyles}
              >
                <Surface
                  width={iconSize}
                  height={iconSize}
                  viewBox={{
                    x: 0,
                    y: 0,
                    width: ICON_SIZE,
                    height: ICON_SIZE,
                  }}
                  style={{
                    marginRight: 4,
                  }}
                >
                  {this.renderIcon(serie, inactive)}
                </Surface>
                <span>{label || key}</span>
              </span>
            );
          })}
      </div>
    );
  }

  private handleLegendItemClick = serie => {
    this.setState({
      offSeries: {
        ...this.state.offSeries,
        [serie.key]: !this.state.offSeries[serie.key],
      },
    });
    if (this.props.onItemClick) {
      this.props.onItemClick(serie);
    }
  };

  private renderIcon(serie: Serie, inactive: boolean = false) {
    const halfSize = ICON_SIZE / 2;
    const sixthSize = ICON_SIZE / 6;
    const thirdSize = ICON_SIZE / 3;
    const color = serie.color;
    if (!serie.legendIconType) {
      if (serie.type === 'line') {
        // show line as the legend icon
        return inactive ? (
          <path
            strokeWidth={4}
            fill="none"
            stroke={'#9e9e9e'}
            d={`M0,${halfSize}h${thirdSize}
                A${sixthSize},${sixthSize},0,1,1,${2 *
              thirdSize},${halfSize}
                H${ICON_SIZE}M${2 * thirdSize},${halfSize}
                A${sixthSize},${sixthSize},0,1,1,${thirdSize},${halfSize}`}
            className="recharts-legend-icon"
          />
        ) : (
          <path
            strokeWidth={4}
            fill="none"
            stroke={color}
            d={`M0,${halfSize}h${thirdSize}
                A${sixthSize},${sixthSize},0,1,1,${2 *
              thirdSize},${halfSize}
                H${ICON_SIZE}M${2 * thirdSize},${halfSize}
                A${sixthSize},${sixthSize},0,1,1,${thirdSize},${halfSize}`}
            className="recharts-legend-icon"
          />
        );
      } else {
        // for area, bar show rect legend
        return inactive ? (
          <path
            strokeWidth={4}
            stroke={color}
            fill="none"
            d={`M0,${sixthSize}h${ICON_SIZE}v${halfSize}h${-ICON_SIZE}z`}
            className="recharts-legend-icon"
          />
        ) : (
          <path
            stroke="none"
            fill={color}
            d={`M0,${sixthSize}h${ICON_SIZE}v${halfSize}h${-ICON_SIZE}z`}
            className="recharts-legend-icon"
          />
        );
      }
    }

    return inactive ? (
      <Symbols
        fill="none"
        strokeWidth={4}
        stroke={color}
        cx={halfSize}
        cy={halfSize}
        size={ICON_SIZE - 10}
        sizeType="diameter"
        type={serie.legendIconType || 'circle'}
      />
    ) : (
      <Symbols
        fill={color}
        cx={halfSize}
        cy={halfSize}
        size={ICON_SIZE - 10}
        sizeType="diameter"
        type={serie.legendIconType || 'circle'}
      />
    );
  }
}

export class Chart extends React.Component<
  {
    classes?: any;
    className?: string;
    data: any[];
    xKey: string;
    series: Serie[];
    width?: number | string;
    height?: number | string;
    xHeight?: number;
    yWidth?: number;
    legendHeight?: number;
    legendItemIconType?: IconType;
    dataSource?: Promise<any[]> | (() => Promise<any[]>);
    onDataSourceError: (error) => void;
    onLegendClick: (options) => void;
  },
  {
    loadingDataSource: boolean;
    data: any[];
    offSeries: any;
  }
> {
  private _mounted = false;

  public constructor(props) {
    super(props);
    this.state = {
      loadingDataSource: false,
      data: this.props.data,
      offSeries: {},
    };
  }

  public componentDidMount() {
    this._mounted = true;
    if (this.props.dataSource) {
      const promise =
        typeof this.props.dataSource === 'object'
          ? this.props.dataSource
          : this.props.dataSource();
      this.setState({
        loadingDataSource: true,
      });
      promise
        .then(result => {
          this._mounted &&
            this.setState({
              data: result,
              loadingDataSource: false,
            });
        })
        .catch(error => {
          this._mounted &&
            this.setState({
              loadingDataSource: false,
            });
          if (this.props.onDataSourceError) {
            this.props.onDataSourceError(error);
          }
        });
    }
  }

  public componentWillUnmount() {
    this._mounted = false;
  }

  public componentWillReceiveProps(props) {
    if (!this.props.dataSource) {
      this.setState({
        data: props.data,
      });
    }
  }

  public render() {
    const { classes } = this.props;
    const height = this.props.height || 320;
    return (
      <div
        className={classNames(classes.root, this.props.className)}
        style={{ width: this.props.width, height }}
      >
        <ResponsiveContainer width="100%" height="100%">
          <ComposedChart data={this.state.data}>
            <XAxis
              dataKey={this.props.xKey}
              height={this.props.xHeight}
            />
            <YAxis
              width={
                this.state.data && this.state.data.length > 0
                  ? this.props.yWidth
                  : 0
              }
            />
            <CartesianGrid vertical={false} strokeDasharray="3 3" />
            {this.props.data && this.props.data.length > 0 && (
              <Tooltip />
            )}
            <Legend
              height={this.props.legendHeight || 45}
              iconType={this.props.legendItemIconType || 'square'}
              onClick={this.onLegendClick}
              content={props => (
                <ChartLegendContent
                  {...props}
                  series={this.props.series}
                  onItemClick={this.onLegentItemClick}
                  classes={{
                    itemInactive:
                      classes.legendItemInactive,
                  }}
                />
              )}
            />
            {this.props.series &&
              this.props.series.map((serie, index) => {
                if (this.state.offSeries[serie.key]) {
                  return;
                }
                switch (serie.type) {
                  case 'area':
                    return (
                      <Area
                        key={index}
                        type={
                          serie.visualizationType ||
                          'monotone'
                        }
                        dataKey={serie.key}
                        fill={serie.color}
                        stroke={serie.color}
                      />
                    );

                  case 'bar':
                    return (
                      <Bar
                        key={index}
                        dataKey={serie.key}
                        barSize={serie.width || 20}
                        fill={serie.color}
                      />
                    );

                  case 'line':
                  default:
                    return (
                      <Line
                        key={index}
                        type={
                          serie.visualizationType ||
                          'monotone'
                        }
                        dataKey={serie.key}
                        stroke={serie.color}
                      />
                    );
                }
              })}
          </ComposedChart>
        </ResponsiveContainer>
        {this.state.loadingDataSource && (
          <div
            className={classes.loadingBox}
            style={{ height, width: '100%' }}
          >
            <CircularProgress disableShrink={true} />
          </div>
        )}
      </div>
    );
  }

  private onLegendClick = p => {
    if (this.props.onLegendClick) {
      this.props.onLegendClick(p);
    }
  };

  private onLegentItemClick = serie => {
    const dataKey = serie.key;
    this.setState({
      offSeries: {
        ...this.state.offSeries,
        [dataKey]: !this.state.offSeries[dataKey],
      },
    });
  };
}

export default withStyles(styles)(Chart);

--#

--% /mts-admin/src/ui/Tag.tsx
import * as React from 'react';
import classNames from 'classnames';

import { createStyles, Theme, withStyles, Typography } from '@material-ui/core';

import { variantColor } from '../theme';

const styles = (theme: Theme) =>
  createStyles({
    ...variantColor(theme),
    root: {
      borderRadius: 3,
      display: 'inline-block',
      fontSize: '0.75rem',
      lineHeight: '1em',
      padding: `${theme.spacing() / 2}px ${theme.spacing() / 2}px`,
    },
    spacing: {
      marginBottom: theme.spacing(),
      marginRight: theme.spacing(),
    },
  });

class Tag extends React.Component<{
  classes: any;
  className?: string;
  variant: string;
  hasSpacing?: boolean;
}> {
  public render() {
    const { classes, className, variant, hasSpacing } = this.props;
    return (
      <Typography
        color="inherit"
        variant="caption"
        className={classNames(
          className,
          classes.root,
          classes[variant],
          hasSpacing && classes.spacing,
        )}
      >
        {this.props.children}
      </Typography>
    );
  }
}

export default withStyles(styles)(Tag);

--#

--% /mts-admin/src/ui/HorizontalMenu.tsx
import * as React from 'react';
import classNames from 'classnames';
import {
  Theme,
  createStyles,
  withStyles,
  Popper,
  Grow,
  ClickAwayListener,
  MenuList,
  Paper,
  MenuItem,
} from '@material-ui/core';
import { LinkButton } from 'app/ui';
import { MenuItem as TMenuItem } from 'app/types';

const styles = (theme: Theme) =>
  createStyles({
    root: {
      flex: 1,
      display: 'flex',
      '& > *': {
        display: 'flex',
        alignItems: 'center',
      },
    },
    menuItem: {
      color: theme.palette.common.white,
      fontSize: '1.5em',
      height: '100%',
      paddingLeft: theme.spacing(1.5),
      paddingRight: theme.spacing(1.5),
      borderRadius: 0,
    },
    subMenuWrapper: {
      display: 'flex',
      flexDirection: 'column',
      '& $subMenuWrapper $menuItem': {
        paddingLeft: theme.spacing(4),
      },
    },
    subMenuItem: {
      color: theme.palette.text.primary,
    },
    text: {
      display: 'inline-block',
      marginLeft: theme.spacing() / 2,
    },
  });

class HorizontalMenu extends React.Component<
  { classes: any; data: TMenuItem[] },
  { menuStatusSet: { [key: string]: boolean } }
> {
  private anchors;

  public constructor(props) {
    super(props);
    this.state = {
      menuStatusSet: {},
    };
    this.anchors = {};
  }

  public render() {
    const { classes, data } = this.props;
    return (
      <div className={classes.root}>
        {data &&
          data.map(item =>
            item.children ? (
              <div key={item.text}>
                {this.getMenuElement(item, true)}
                <Popper
                  open={
                    !!this.state.menuStatusSet[
                      this.getMenuKey(item)
                    ]
                  }
                  anchorEl={
                    this.anchors[this.getMenuKey(item)]
                  }
                  transition={true}
                  disablePortal={true}
                >
                  {({ TransitionProps, placement }) => (
                    <Grow
                      {...TransitionProps}
                      style={{
                        transformOrigin:
                          placement === 'bottom'
                            ? 'center top'
                            : 'center bottom',
                      }}
                    >
                      <Paper square={true}>
                        <ClickAwayListener
                          onClickAway={e =>
                            this.handleClose(
                              e,
                              item,
                            )
                          }
                        >
                          {this.generateSubMenu(item)}
                        </ClickAwayListener>
                      </Paper>
                    </Grow>
                  )}
                </Popper>
              </div>
            ) : (
              this.getMenuElement(item, true)
            ),
          )}
      </div>
    );
  }

  private getMenuKey(menu) {
    return `${menu.text}_${menu.link || ''}`;
  }

  private getMenuElement = (menu, isRoot) => {
    const { classes } = this.props;
    const menuKey = this.getMenuKey(menu);
    return (
      <LinkButton
        contentAlign="left"
        key={menu.text}
        to={menu.link}
        className={classNames(
          classes.menuItem,
          !isRoot && classes.subMenuItem,
        )}
        buttonRef={node => {
          this.anchors[menuKey] = node;
        }}
        color="inherit"
        aria-haspopup="true"
        aria-owns={
          this.state.menuStatusSet[menuKey] ? menuKey : undefined
        }
        onClick={() => this.handleToggle(menu)}
      >
        {typeof menu.icon !== 'string' ? (
          menu.icon
        ) : (
          <i className={menu.icon} />
        )}
        <span className={classes.text}>{menu.text}</span>
      </LinkButton>
    );
  };

  private generateSubMenu = menu => {
    const { classes } = this.props;
    return (
      menu.children &&
      menu.children.length > 0 && (
        <MenuList>
          {menu.children.map(subItem => (
            <div
              key={subItem.text}
              className={classes.subMenuWrapper}
            >
              <MenuItem
                onClick={e => this.handleClose(e, subItem)}
                component={props =>
                  this.menuItem(props, subItem, false)
                }
              />
              {this.generateSubMenu(subItem)}
            </div>
          ))}
        </MenuList>
      )
    );
  };

  private handleToggle = menu => {
    const menuKey = this.getMenuKey(menu);
    this.setState({
      menuStatusSet: {
        [menuKey]: !this.state.menuStatusSet[menuKey],
      },
    });
  };

  private menuItem = (props, menu, isRoot) =>
    this.getMenuElement(menu, isRoot);

  private handleClose = (event, menu) => {
    const menuKey = this.getMenuKey(menu);
    this.setState({
      menuStatusSet: { ...this.state.menuStatusSet, [menuKey]: false },
    });
  };
}

export default withStyles(styles)(HorizontalMenu);

--#

--% /mts-admin/src/types/index.tsx
export * from './MenuItem';

--#

--% /mts-admin/src/types/MenuItem.tsx
export interface MenuItem {
  icon?: string | JSX.Element;
  text: string;
  link?: string;
  description?: string;
  children?: MenuItem[];
}

--#

--% /mts-admin/src/styles/_mixins.scss
@mixin hover {
  &:hover {
    @content;
  }
}

@mixin hover-focus {
  &:hover,
  &:focus {
    @content;
  }
}

@mixin plain-hover-focus {
  &,
  &:hover,
  &:focus {
    @content;
  }
}

@mixin hover-focus-active {
  &:hover,
  &:focus,
  &:active {
    @content;
  }
}

@mixin colorVariant($variant, $color) {
  .bg-#{$variant} {
    background-color: $color !important;
  }
  a.bg-#{$variant},
  button.bg-#{$variant} {
    @include hover-focus {
      background-color: darken($color, 10%) !important;
    }
  }
  .text-#{$variant} {
    color: $color !important;
  }
  .border-#{$variant} {
    border-color: $color !important;
  }
}

@mixin generateTRBL($property, $units...) {
  @each $unit in $units {
    @if $unit == 1 {
      .#{$property} {
        #{$property}: $unit * 8px;
      }
    } @else {
      .#{$property}-#{$unit} {
        #{$property}: $unit * 8px;
      }
    }
    @each $item in $TRBL {
      @if $unit == 1 {
        .#{$property}-#{$item} {
          #{$property}-#{$item}: $unit * 8px;
        }
      } @else {
        .#{$property}-#{$item}-#{$unit} {
          #{$property}-#{$item}: $unit * 8px;
        }
      }
    }
  }
}

--#

--% /mts-admin/src/styles/default.scss
@import 'variables';
@import 'mixins';

@include generateTRBL('margin', 0, 1, 2);
@include generateTRBL('padding', 0, 1, 2);
@include colorVariant('primary', $color-primary);
@include colorVariant('secondary', $color-secondary);
@include colorVariant('success', $color-success);
@include colorVariant('error', $color-error);
@include colorVariant('warning', $color-warning);
@include colorVariant('info', $color-info);
@include colorVariant('dark', $color-dark);
@include colorVariant('light', $color-light);

html,
body {
  margin: 0;
}

* {
  font-family: 'Roboto', 'Helvetica', 'Arial', sans-serif;
}

a {
  text-decoration: none;
}

.starting {
  img {
    width: 70px;
    height: 70px;
  }
}

.app-error {
  position: absolute;
  z-index: 999999;
  background-color: maroon;
  top: 0;
  left: 0;
  right: 0;
  padding: 5px 10px;
  color: white;
  text-align: center;
  font-size: 0.85em;

  a {
    color: #05a1bf;
    text-decoration: none;
  }
}

.clickable {
  cursor: pointer;
}

.hidden {
  display: none;
}

.markdown-body {
  color: inherit;
}

.screen-center {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  & > * {
    margin-top: -10rem;
  }
}

.text-left {
  text-align: left;
}

.text-center {
  text-align: center;
}

.text-right {
  text-align: right;
}

.font-xs {
  font-size: 0.5em;
}

.font-sm {
  font-size: 0.75em;
}

.font-lg {
  font-size: 1.25em;
}

.font-xl {
  font-size: 1.5em;
}

.font-b {
  font-weight: bold;
}

.text-center {
  text-align: center;
}

.dark {
  .markdown-body {
    pre {
      background-color: #424242;
    }
  }
}

.bn-loading-overlay .bn-loading-container .bicon.bicon-loading {
  border-left-color: #303f9f;
}
/* TODO: remove after the dialog bugfix */
.notification-item {
  max-width: 360px;
}

--#

--% /mts-admin/src/styles/_variables.scss
$TRBL: top, right, bottom, left;

$color-primary: #007bff !default;
$color-secondary: #6c757d !default;
$color-success: #28a745 !default;
$color-error: #dc3545 !default;
$color-warning: #ffc107 !default;
$color-info: #17a2b8 !default;
$color-dark: #343a40 !default;
$color-light: #f8f9fa !default;

--#

--% /mts-admin/src/service/global.tsx
import { NotifierOptions } from '../ui';
import storage from 'app/helpers/storage';
import { KEY_THEME } from 'app/theme';

export const ACTION_LOADING_SHOW = 'G_LOADING_SHOW';
export const ACTION_LOADING_HIDE = 'G_LOADING_HIDE';
export const ACTION_NOTIFIER_SHOW = 'G_NOTIFIER_SHOW';
export const ACTION_NOTIFIER_HIDE = 'G_NOTIFIER_HIDE';
export const ACTION_REQUESTING_SHOW = 'G_REQUESTING_SHOW';
export const ACTION_REQUESTING_HIDE = 'G_REQUESTING_HIDE';
export const ACTION_THEME_CHANGE = 'G_THEME_CHANGE';
export const ACTION_LOCALE_CHANGE = 'G_LOCALE_CHANGE';

export const actions = {
  showLoading: (text?: string) => ({
    type: ACTION_LOADING_SHOW,
    payload: {
      loadingText: text || 'Loading...',
    },
  }),
  hideLoading: () => ({
    type: ACTION_LOADING_HIDE,
  }),

  showRequesting: () => ({
    type: ACTION_REQUESTING_SHOW,
  }),
  hideRequesting: () => ({
    type: ACTION_REQUESTING_HIDE,
  }),

  notify: (notifierOptions: NotifierOptions) => ({
    type: ACTION_NOTIFIER_SHOW,
    notifierOptions,
  }),
  notifyInfo: (message: string) => ({
    type: ACTION_NOTIFIER_SHOW,
    notifierOptions: {
      message,
      variant: 'info',
    },
  }),
  notifySuccess: (message: string) => ({
    type: ACTION_NOTIFIER_SHOW,
    notifierOptions: {
      message,
      variant: 'success',
    },
  }),
  notifyWarning: (message: string) => ({
    type: ACTION_NOTIFIER_SHOW,
    notifierOptions: {
      message,
      variant: 'warning',
    },
  }),
  notifyError: (message: string) => ({
    type: ACTION_NOTIFIER_SHOW,
    notifierOptions: {
      message,
      variant: 'error',
    },
  }),
  unnotify: () => ({
    type: ACTION_NOTIFIER_HIDE,
  }),

  changeTheme: theme => ({
    type: ACTION_THEME_CHANGE,
    theme,
  }),

  changeLocale: (locale: string) => ({
    type: ACTION_LOCALE_CHANGE,
    locale,
  }),
};

export const reducer = (state = { loading: false }, action) => {
  switch (action.type) {
    case ACTION_LOADING_SHOW: {
      const { loadingText } = action.payload;
      return { ...state, loading: true, loadingText };
    }
    case ACTION_LOADING_HIDE: {
      return { ...state, loading: false };
    }

    case ACTION_REQUESTING_SHOW: {
      return { ...state, requesting: true };
    }
    case ACTION_REQUESTING_HIDE: {
      return { ...state, requesting: false };
    }

    case ACTION_NOTIFIER_SHOW: {
      const notifierOptions = action.notifierOptions;
      return { ...state, showNotifier: true, notifierOptions };
    }
    case ACTION_NOTIFIER_HIDE:
      return { ...state, showNotifier: false };

    case ACTION_THEME_CHANGE: {
      storage.set(KEY_THEME, action.theme);
      return { ...state, theme: action.theme };
    }

    default:
      return state;
  }
};

--#

--% /mts-admin/src/service/locales.tsx
import * as intl from 'react-intl-universal';
import { getConfig } from 'app/config';
import storage from 'app/helpers/storage';
import ajax from 'app/helpers/ajax';
import { onAppLocaleChanged } from '../app.events';

const config = getConfig();
const KEY_LOCALE = 'locale';
function getCurrentLocale() {
  return (
    storage.getCookie(KEY_LOCALE) ||
    config.defaultLocale ||
    navigator.language
  );
}

export function initLocales(currentLocale?: string, callback?: () => void) {
  if (currentLocale) {
    storage.setCookie(KEY_LOCALE, currentLocale);
  } else {
    storage.removeCookie(KEY_LOCALE);
  }
  currentLocale = currentLocale || getCurrentLocale();
  const locales = {};
  config.locales.forEach(item => {
    locales[item.value] = item.messages;
  });

  const initIntl = l => {
    intl.init({
      currentLocale,
      fallbackLocale: config.locales[0].value,
      locales: l,
    }).then(() => {
      onAppLocaleChanged();
      if (callback) {
        callback();
      }
    });
  };
  if (locales[currentLocale]) {
    initIntl(locales);
  } else {
    // load messages from remote file if the messages not specified in service/locales.tsx
    ajax.get(`locales/json/${currentLocale}.json`).then(messages => {
      initIntl({
        [currentLocale]: messages,
      });
    });
  }
}

export function setLocale(currentLocale?: string, callback?: () => void) {
  initLocales(currentLocale, callback);
}

// eslint-disable-next-line no-console
console.info(`Locale is '${getCurrentLocale()}'.`);

--#

--% /mts-admin/src/service/auth.tsx
/* eslint-disable */
import { AxiosPromise } from 'axios';
import { Ajax, AjaxError } from '../helpers/ajax';
import { store } from '../redux';
import { getConfig, AuthType } from '../config';
import { push } from 'connected-react-router';
import { call, put, takeLatest } from 'redux-saga/effects';
import { actions as globalActions } from './global';
import { Url } from 'app/helpers/url';
import storage from 'app/helpers/storage';
import utils from 'app/helpers/utils';

export const KEY_TOKEN = 'token';

export const ACTION_AUTH_REQUEST = 'USER_AUTH_REQUEST';
export const ACTION_AUTH_SUCCESS = 'USER_AUTH_SUCCESS';
export const ACTION_AUTH_FAILURE = 'USER_AUTH_FAILURE';

export const ACTION_LOGIN_REQUEST = 'USER_LOGIN_REQUEST';
export const ACTION_LOGIN_SUCCESS = 'USER_LOGIN_SUCCESS';
export const ACTION_LOGIN_FAILURE = 'USER_LOGIN_FAILURE';

export const ACTION_LOGOUT_REQUEST = 'USER_LOGOUT_REQUEST';
export const ACTION_LOGOUT_SUCCESS = 'USER_LOGOUT_SUCCESS';
export const ACTION_LOGOUT_FAILURE = 'USER_LOGOUT_FAILURE';

export const ACTION_GETUSER_REQUEST = 'USER_GETUSER_REQUEST';
export const ACTION_GETUSER_SUCCESS = 'USER_GETUSER_SUCCESS';
export const ACTION_GETUSER_FAULURE = 'USER_GETUSER_FAILURE';

export interface UserInfo {
  id?: string;
  name?: string;
  email?: string;
  avatar?: string;
}

export interface AuthState {
  user?: UserInfo;
  token?: TokenInfo;
  error?: any;
}

export interface LoginData {
  username: string;
  password: string;
  rememberMe: boolean;
  client_id?: string;
  client_secret?: string;
  grant_type?: string;
}

export interface TokenInfo {
  access_token: string;
  refresh_token?: string;
  token_type?: string;
  expires_in?: number;
  scope?: string;
}

export const actions = {
  authSuccess: (tokenInfo: TokenInfo) => ({
    type: ACTION_AUTH_SUCCESS,
    payload: tokenInfo,
  }),
  login: (data: LoginData) => ({
    type: ACTION_LOGIN_REQUEST,
    payload: data,
  }),
  loginSuccess: (response: TokenInfo) => ({
    type: ACTION_LOGIN_SUCCESS,
    payload: response,
  }),
  loginFailure: error => ({
    type: ACTION_LOGIN_FAILURE,
    payload: error,
  }),
  getUserInfo: (accessToken: string) => ({
    type: ACTION_GETUSER_REQUEST,
    payload: accessToken,
  }),
  getUserInfoSuccess: (userInfo: UserInfo) => ({
    type: ACTION_GETUSER_SUCCESS,
    payload: userInfo,
  }),
  logout: () => ({
    type: ACTION_LOGOUT_REQUEST,
  }),
  logoutSuccess: () => ({
    type: ACTION_LOGOUT_SUCCESS,
  }),
};

export function reducer(state: AuthState = {}, action): AuthState {
  switch (action.type) {
    case ACTION_AUTH_SUCCESS:
      return {
        ...state,
        token: action.payload,
      };

    case ACTION_LOGIN_REQUEST:
      return { ...state };
    case ACTION_LOGIN_SUCCESS:
      return {
        ...state,
        token: action.payload,
      };
    case ACTION_GETUSER_SUCCESS:
      return {
        ...state,
        user: action.payload,
      };

    case ACTION_LOGOUT_SUCCESS:
      return { ...state, user: null, token: null };

    default:
      return state;
  }
}

const config = getConfig();

export const service = {
  login: (data: LoginData) => {
    switch (config.authType) {
      case AuthType.OAuthPassword:
        data.grant_type = 'password';
        data.client_id = config.authConfig.clientId;
        data.client_secret = config.authConfig.clientSecret;
        return new Ajax().postForm(
          config.authConfig.authorizationUri,
          data,
        );

      case AuthType.Mock:
        return new Promise((resolve, reject) => {
          const token: TokenInfo = {
            access_token: JSON.stringify(data),
          };
          storage.set(KEY_TOKEN, token);
          resolve(token);
        });

      default:
        return new Promise((resolve, reject) => {
          const error: AjaxError = {
            data: {
              error_description: `No handler found for ${
                config.authType
              }`,
            },
            status: 404,
            statusText: 'No `AuthType` matched.',
            headers: null,
            config: null,
            request: null,
          };
          reject(error);
        });
    }
  },
  getUser: (): AxiosPromise | any => {
    if (config.authType === AuthType.Mock) {
      return new Promise((resolve, reject) => {
        const user: UserInfo = JSON.parse(
          getState().token.access_token,
        ) as UserInfo;
        resolve(user);
      });
    }
    return new Ajax({
      headerAuthorization: () =>
        `${getState().token.token_type || 'Bearer'} ${
          getState().token.access_token
        }`,
    }).get(config.authConfig.userProfileUri);
  },
  logout: (): AxiosPromise | any => {
    if (config.authType === AuthType.Mock) {
      return new Promise((resolve, reject) => {
        storage.remove(KEY_TOKEN);
        resolve('ok');
      });
    }
    if (config.logoutHandler) {
      return config.logoutHandler(
        config.authConfig.logoutUri,
        getState(),
      );
    } else {
      return new Ajax({
        headerAuthorization: () => {
          if (getState().token) {
            return `${getState().token.token_type} ${
              getState().token.access_token
            }`;
          }
          return '';
        },
      }).remove(config.authConfig.logoutUri);
    }
  },
};

function* auth() {
  yield put(globalActions.showLoading('Redirecting to authorize...'));
}

function* authSuccess(action) {
  yield put(actions.getUserInfo(action.payload));
}

function* login(action) {
  try {
    // effects(call, put):
    // trigger off the code that we want to call that is asynchronous
    // and also dispatched the result from that asynchrous code.
    const loginData: LoginData = action.payload;
    yield put(globalActions.showLoading('Logging in...'));
    const tokenInfo: TokenInfo = yield call(service.login, {
      ...loginData,
    });
    yield put(actions.loginSuccess(tokenInfo));
    yield put(actions.getUserInfo(tokenInfo.access_token));
    yield put(globalActions.hideLoading());
    yield put(push('/admin'));
  } catch (err) {
    yield put(globalActions.hideLoading());
    if (err) {
      const ajaxError = err as AjaxError;
      yield put(
        globalActions.notifyError(
          `${ajaxError.status}: ${ajaxError.data.error_description}`,
        ),
      );
    } else {
      yield put(globalActions.notifyError(`Service Unavailable`));
    }
  }
}

function* logout(action) {
  yield put(actions.logoutSuccess());
}

function* getUser(action) {
  try {
    yield put(globalActions.showLoading('Getting user info...'));
    const response = yield call(service.getUser);
    const userInfo: UserInfo =
      typeof config.userConverter === 'function'
        ? config.userConverter(response)
        : { ...response };
    yield put(actions.getUserInfoSuccess(userInfo));
    yield put(globalActions.hideLoading());
    yield put(push('/admin'));
  } catch (e) {
    yield put(globalActions.hideLoading());
  }
}

export function* saga() {
  // takeEvery:
  // listen for certain actions that are going to be dispatched and take them and run through our worker saga.
  yield takeLatest(ACTION_AUTH_REQUEST, auth);
  yield takeLatest(ACTION_AUTH_SUCCESS, authSuccess);
  yield takeLatest(ACTION_LOGIN_REQUEST, login);
  yield takeLatest(ACTION_LOGOUT_REQUEST, logout);
  yield takeLatest(ACTION_GETUSER_REQUEST, getUser);
}

export function getState(): AuthState {
  return store.getState().auth as AuthState;
}

export function isAuthorized(): boolean {
  if (config.authType === AuthType.Mock) {
    let token: TokenInfo = storage.get(KEY_TOKEN);
    if (token) {
      let user = JSON.parse(token.access_token);
      if (config.userConverter) {
        user = config.userConverter(user);
      }
      const state = getState();
      state.token = token;
      state.user = user;
    }
  }
  return !!getState().token;
}

export function getAuthUri(): string {
  if (
    config.authType === AuthType.Custom ||
    config.authType === AuthType.OAuthPassword ||
    config.authType === AuthType.Mock
  ) {
    return '/login';
  }

  if (
    config.authType === AuthType.OAuth ||
    config.authType === AuthType.OAuthCode
  ) {
    let authUrl = config.authConfig.authorizationUri;
    if (!config.authConfig.callbackUri) {
      const callbackUri = Url.current().merge('/auth/callback');
      authUrl = authUrl.replace('{callbackUri}', callbackUri);
    }

    Object.keys(config.authConfig).forEach(key => {
      authUrl = authUrl.replace(`{${key}}`, config.authConfig[key]);
    });

    return `${authUrl}&state=${getValidState()}`;
  }
}

export function getValidState(): string {
  const KEY_AUTH_STATE = 'AUTH_STATE';
  if (!storage.getSession(KEY_AUTH_STATE)) {
    storage.setSession(KEY_AUTH_STATE, utils.randomString(10));
  }

  return storage.getSession(KEY_AUTH_STATE);
}

export function getAccessTokenUri(code: string): string {
  if (
    config.authType === AuthType.OAuth ||
    config.authType === AuthType.OAuthCode
  ) {
    let tokenUrl = config.authConfig.accessTokenUri;
    tokenUrl = tokenUrl.replace('{code}', code);
    if (!config.authConfig.callbackUri) {
      const callbackUri = Url.current().merge('/auth/callback');
      tokenUrl = tokenUrl.replace('{callbackUri}', callbackUri);

      Object.keys(config.authConfig).forEach(key => {
        tokenUrl = tokenUrl.replace(`{${key}}`, config.authConfig[key]);
      });
    }
    return tokenUrl;
  }
}

--#

--% /mts-admin/src/service/resource.tsx
import { notify } from '@bndynet/dialog';
import { getConfig } from '../config';
import { Ajax } from '../helpers/ajax';
import { getState } from './auth';

class ResourceService extends Ajax {
  public constructor() {
    const config = getConfig();
    console.debug(config);
    super({
      headerAuthorization: () => {
        if (getState().token) {
          return `${getState().token.token_type} ${
            getState().token.access_token
          }`;
        }
        return '';
      },
      baseURL: config.resourceBaseUri,
      onResponseError: error => {
        notify(JSON.stringify(error), 'error');
      },
    });
  }
}

export const service = new ResourceService();

--#

--% /mts-admin/src/service/index.d.ts
export interface AppAction {
  type: string;
  payload: any;
  resolve: () => void;
  reject: () => void;
}

--#

--% /mts-admin/assets/user.json
{
  "username": "Bendy Zhang",
  "token": "TOKEN"
}
--#

--% /mts-admin/assets/index.html
<!DOCTYPE html>
<html>
  <head>
    <title>
      <%= htmlWebpackPlugin.options.title %>
    </title>
    <meta charset="UTF-8" />
    <meta name="viewport" content="minimum-scale=1, initial-scale=1, width=device-width, shrink-to-fit=no" />
    
    <link href="data:image/x-icon;base64,AAABAAEAEBACAAAAAACwAAAAFgAAACgAAAAQAAAAIAAAAAEAAQAAAAAAQAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//wAA//8AAP//AAD//wAA//8AAP//AAAF4QAABOEAACTvAAAk5wAApCcAALQnAACX5wAAk+cAAJIQAACSEAAA" rel="icon" type="image/x-icon" />

    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,400,500" />
    <link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/animate.css@3.5.2/animate.min.css" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/font-awesome@4.7.0/css/font-awesome.min.css" />

    <!-- Global site tag (gtag.js) - Google Analytics
    -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-93843808-3"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());

    gtag('config', 'UA-93843808-3');
    </script>
  </head>

  <body>
    <noscript>
      <div class="app-error">
        JavaScript is not enabled. Please enable it and reload the page.
      </div>
    </noscript>
    <!--[if lt IE 11]>
      <div class="app-error">
        You are using an <strong>outdated</strong> version of Internet Explorer. Please <a href="http://windows.microsoft.com/en-us/internet-explorer/download-ie" target="_blank">upgrade your browser</a> to version 11 or higher.
      </div>
    <![endif]-->
    <div id="app">
      <div class="screen-center text-center starting">
        <img class="animated infinite bounce" src="https://seeklogo.com/images/U/ufc-logo-42740DDFF6-seeklogo.com.png" />
        <br />
        Loading...
      </div>
    </div>
  </body>
</html>

--#

--% /mts-admin/assets/_redirects
# This file is for netlify.com redirects
/*    /index.html    404

--#

--% /mts-admin/assets/datatable.json
[
  { "name": "Joe James", "company": "Test Corp", "city": "Yonkers", "state": "NY" },
  { "name": "John Walsh", "company": "Test Corp", "city": "Hartford", "state": "CT" },
  { "name": "Bob Herm", "company": "Test Corp", "city": "Tampa", "state": "FL" },
  { "name": "James Houston", "company": "Test Corp", "city": "Dallas", "state": "TX" },
  { "name": "Joe James1", "company": "Test Corp", "city": "Yonkers", "state": "NY" },
  { "name": "John Walsh", "company": "Test Corp", "city": "Hartford", "state": "CT" },
  { "name": "Bob Herm", "company": "Test Corp", "city": "Tampa", "state": "FL" },
  { "name": "James Houston", "company": "Test Corp", "city": "Dallas", "state": "TX" },
  { "name": "Joe James2", "company": "Test Corp", "city": "Yonkers", "state": "NY" },
  { "name": "Bob Herm", "company": "Test Corp", "city": "Tampa", "state": "FL" }
]
--#

--% /mts-admin/assets/images/bg.jpg
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AABwAAD/////////////////////////////A+gAAAAA/////////////////////////////wPoAAAAAP////////////////////////////8D6AAAAAD/////////////////////////////A+gAADhCSU0EAAAAAAAAAgABOEJJTQQCAAAAAAAEAAAAADhCSU0EMAAAAAAAAgEBOEJJTQQtAAAAAAAGAAEAAAACOEJJTQQIAAAAAAAQAAAAAQAAAkAAAAJAAAAAADhCSU0EHgAAAAAABAAAAAA4QklNBBoAAAAAAzkAAAAGAAAAAAAAAAAAAAQ4AAAHgAAAAAIAYgBnAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAeAAAAEOAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAABAAAAABAAAAAAAAbnVsbAAAAAIAAAAGYm91bmRzT2JqYwAAAAEAAAAAAABSY3QxAAAABAAAAABUb3AgbG9uZwAAAAAAAAAATGVmdGxvbmcAAAAAAAAAAEJ0b21sb25nAAAEOAAAAABSZ2h0bG9uZwAAB4AAAAAGc2xpY2VzVmxMcwAAAAFPYmpjAAAAAQAAAAAABXNsaWNlAAAAEgAAAAdzbGljZUlEbG9uZwAAAAAAAAAHZ3JvdXBJRGxvbmcAAAAAAAAABm9yaWdpbmVudW0AAAAMRVNsaWNlT3JpZ2luAAAADWF1dG9HZW5lcmF0ZWQAAAAAVHlwZWVudW0AAAAKRVNsaWNlVHlwZQAAAABJbWcgAAAABmJvdW5kc09iamMAAAABAAAAAAAAUmN0MQAAAAQAAAAAVG9wIGxvbmcAAAAAAAAAAExlZnRsb25nAAAAAAAAAABCdG9tbG9uZwAABDgAAAAAUmdodGxvbmcAAAeAAAAAA3VybFRFWFQAAAABAAAAAAAAbnVsbFRFWFQAAAABAAAAAAAATXNnZVRFWFQAAAABAAAAAAAGYWx0VGFnVEVYVAAAAAEAAAAAAA5jZWxsVGV4dElzSFRNTGJvb2wBAAAACGNlbGxUZXh0VEVYVAAAAAEAAAAAAAlob3J6QWxpZ25lbnVtAAAAD0VTbGljZUhvcnpBbGlnbgAAAAdkZWZhdWx0AAAACXZlcnRBbGlnbmVudW0AAAAPRVNsaWNl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LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iIHhtbG5zOnBob3Rvc2hvcD0iaHR0cDovL25zLmFkb2JlLmNvbS9waG90b3Nob3AvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0RXZ0PSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VFdmVudCMiIHhtbG5zOnRpZmY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vdGlmZi8xLjAvIiB4bWxuczpleGlmPSJodHRwOi8vbnMuYWRvYmUuY29tL2V4aWYvMS4wLyIgeG1wOkNyZWF0b3JUb29sPSJBZG9iZSBQaG90b3Nob3AgQ1M0IFdpbmRvd3MiIHhtcDpDcmVhdGVEYXRlPSIyMDE4LTA2LTIxVDIzOjAyOjQ0KzA4OjAwIiB4bXA6TW9kaWZ5RGF0ZT0iMjAxOC0wNi0yMVQyMzoxMjowOCswODowMCIgeG1wOk1ldGFkYXRhRGF0ZT0iMjAxOC0wNi0yMVQyMzoxMjowOCswODowMCIgZGM6Zm9ybWF0PSJpbWFnZS9qcGVnIiBwaG90b3Nob3A6Q29sb3JNb2RlPSIzIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjEyQTNCMkFBNjQ3NUU4MTFBMkYxQUI5OTdDNjJDNkVDIiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjEyQTNCMkFBNjQ3NUU4MTFBMkYxQUI5OTdDNjJDNkVDIiB4bXBNTTpPcmlnaW5hbERvY3VtZW50SUQ9InhtcC5kaWQ6MTJBM0IyQUE2NDc1RTgxMUEyRjFBQjk5N0M2MkM2RUMiIHRpZmY6T3JpZW50YXRpb249IjEiIHRpZmY6WFJlc29sdXRpb249IjcyMDAwMC8xMDAwMCIgdGlmZjpZUmVzb2x1dGlvbj0iNzIwMDAwLzEwMDAwIiB0aWZmOlJlc29sdXRpb25Vbml0PSIyIiB0aWZmOk5hdGl2ZURpZ2VzdD0iMjU2LDI1NywyNTgsMjU5LDI2MiwyNzQsMjc3LDI4NCw1MzAsNTMxLDI4MiwyODMsMjk2LDMwMSwzMTgsMzE5LDUyOSw1MzIsMzA2LDI3MCwyNzEsMjcyLDMwNSwzMTUsMzM0MzI7MkNGRUEwNEMwRjgxOUUwNUNERTI0MEYxQzFEMjM3NTgiIGV4aWY6UGl4ZWxYRGltZW5zaW9uPSIxOTIwIiBleGlmOlBpeGVsWURpbWVuc2lvbj0iMTA4MCIgZXhpZjpDb2xvclNwYWNlPSI2NTUzNSIgZXhpZjpOYXRpdmVEaWdlc3Q9IjM2ODY0LDQwOTYwLDQwOTYxLDM3MTIxLDM3MTIyLDQwOTYyLDQwOTYzLDM3NTEwLDQwOTY0LDM2ODY3LDM2ODY4LDMzNDM0LDMzNDM3LDM0ODUwLDM0ODUyLDM0ODU1LDM0ODU2LDM3Mzc3LDM3Mzc4LDM3Mzc5LDM3MzgwLDM3MzgxLDM3MzgyLDM3MzgzLDM3Mzg0LDM3Mzg1LDM3Mzg2LDM3Mzk2LDQxNDgzLDQxNDg0LDQxNDg2LDQxNDg3LDQxNDg4LDQxNDkyLDQxNDkzLDQxNDk1LDQxNzI4LDQxNzI5LDQxNzMwLDQxOTg1LDQxOTg2LDQxOTg3LDQxOTg4LDQxOTg5LDQxOTkwLDQxOTkxLDQxOTkyLDQxOTkzLDQxOTk0LDQxOTk1LDQxOTk2LDQyMDE2LDAsMiw0LDUsNiw3LDgsOSwxMCwxMSwxMiwxMywxNCwxNSwxNiwxNywxOCwyMCwyMiwyMywyNCwyNSwyNiwyNywyOCwzMDszOTlGQkFBNEQ5QkQ3MDAzOUQ2QzgwQUJDMUZGMDY1NyI+IDx4bXBNTTpIaXN0b3J5PiA8cmRmOlNlcT4gPHJkZjpsaSBzdEV2dDphY3Rpb249ImNyZWF0ZWQiIHN0RXZ0Omluc3RhbmNlSUQ9InhtcC5paWQ6MTJBM0IyQUE2NDc1RTgxMUEyRjFBQjk5N0M2MkM2RUMiIHN0RXZ0OndoZW49IjIwMTgtMDYtMjFUMjM6MTI6MDgrMDg6MDAiIHN0RXZ0OnNvZnR3YXJlQWdlbnQ9IkFkb2JlIFBob3Rvc2hvcCBDUzQgV2luZG93cyIvPiA8L3JkZjpTZXE+IDwveG1wTU06SGlzdG9yeT4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+ICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgPD94cGFja2V0IGVuZD0idyI/Pv/uACFBZG9iZQBkAAAAAAEDABADAgMGAAAAAAAAAAAAAAAA/9sAhAAGBAQHBQcLBgYLDgoICg4RDg4ODhEWExMTExMWEQwMDAwMDBEMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMAQcJCRMMEyITEyIUDg4OFBQODg4OFBEMDAwMDBERDAwMDAwMEQwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAz/wgARCAQ4B4ADAREAAhEBAxEB/8QAmwAAAwEBAQEBAQAAAAAAAAAAAAIDAQQFBgcIAQEAAAAAAAAAAAAAAAAAAAAAEAACAwACAgEFAQABBQACAAcBAgARAxIEIQUTEDEiFAYVIDBBMiMWQAdQYOAkoEIzEQACAgICAgICAQUAAwEBAQAAEQEhEDECEiAwQSJAYVBgcFEyA3ETI4GAsBIBAAAAAAAAAAAAAAAAAAAA4P/aAAwDAQECEQMRAAAA/lg0wY7D1j1iJM6DDjNO8w4TqLkjCRxnnHGTMAUBypUcQ5CYABowxUY0Y0qdJ2nrnpnMchQqOUFAUUqYWKmCCHOc5yExhwMNEOM8o4SRgDHUeseqdY5opowDGjGjHSegXHOYYU0c0U5jmJgOMYaAABop555B5xEQUodB3npHUUGAQUDDAMMGO86SZE0UmaIBYDiOQkBgxhgxUYUiTFMHLlRBCJIQUUww009I9QsIMBEQQwcYUQYmRKFxDnOM5iYGlhzoO46ipgwwpgxA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
--#

--% /mts-admin/assets/locales/json/pro.babel
<?xml version="1.0" encoding="UTF-8"?>
<babeledit_project be_version="2.8.0" version="1.2">
  <!--

  BabelEdit project file
  https://www.codeandweb.com/babeledit

  This file contains meta data for all translations, but not the translation texts itself.
  They are stored in framework-specific message files (.json / .vue / .yaml / .properties)

  -->
  <preset_collections/>
  <framework>ngx-translate</framework>
  <filename>pro.babel</filename>
  <source_root_dir/>
  <folder_node>
    <name/>
    <children>
      <folder_node>
        <name>admin</name>
        <children>
          <concept_node>
            <name>brand</name>
            <definition_loaded>false</definition_loaded>
            <description/>
            <comment/>
            <default_text/>
            <translations>
              <translation>
                <language>en-US</language>
                <approved>false</approved>
              </translation>
              <translation>
                <language>zh-CN</language>
                <approved>false</approved>
              </translation>
            </translations>
          </concept_node>
        </children>
      </folder_node>
      <concept_node>
        <name>all</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>cancel</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>column</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>delete</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>deleteConfirmMessage</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>downloadCsv</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <folder_node>
        <name>errors</name>
        <children>
          <folder_node>
            <name>404</name>
            <children>
              <concept_node>
                <name>description</name>
                <definition_loaded>false</definition_loaded>
                <description/>
                <comment/>
                <default_text/>
                <translations>
                  <translation>
                    <language>en-US</language>
                    <approved>false</approved>
                  </translation>
                  <translation>
                    <language>zh-CN</language>
                    <approved>false</approved>
                  </translation>
                </translations>
              </concept_node>
              <concept_node>
                <name>title</name>
                <definition_loaded>false</definition_loaded>
                <description/>
                <comment/>
                <default_text/>
                <translations>
                  <translation>
                    <language>en-US</language>
                    <approved>false</approved>
                  </translation>
                  <translation>
                    <language>zh-CN</language>
                    <approved>false</approved>
                  </translation>
                </translations>
              </concept_node>
            </children>
          </folder_node>
        </children>
      </folder_node>
      <concept_node>
        <name>filter</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>filters</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>forgotPassword</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>goHome</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>hi</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>home</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>itemsSelected</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>loadingData</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>loginWithGitHub</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <folder_node>
        <name>logout</name>
        <children>
          <concept_node>
            <name>success</name>
            <definition_loaded>false</definition_loaded>
            <description/>
            <comment/>
            <default_text/>
            <translations>
              <translation>
                <language>en-US</language>
                <approved>false</approved>
              </translation>
              <translation>
                <language>zh-CN</language>
                <approved>false</approved>
              </translation>
            </translations>
          </concept_node>
        </children>
      </folder_node>
      <concept_node>
        <name>myProfile</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>nextPage</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>noData</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>of</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>ok</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>other</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>password</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>previousPage</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>print</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>rememberMe</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>required</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>reset</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>rowsPerPage</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>search</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>signIn</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>signOut</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>toggleColumns</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>username</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
      <concept_node>
        <name>viewColumns</name>
        <definition_loaded>false</definition_loaded>
        <description/>
        <comment/>
        <default_text/>
        <translations>
          <translation>
            <language>en-US</language>
            <approved>false</approved>
          </translation>
          <translation>
            <language>zh-CN</language>
            <approved>false</approved>
          </translation>
        </translations>
      </concept_node>
    </children>
  </folder_node>
  <isTemplateProject>false</isTemplateProject>
  <languages>
    <language>
      <code>en-US</code>
      <source_id/>
      <source_file>en-US.json</source_file>
    </language>
    <language>
      <code>zh-CN</code>
      <source_id/>
      <source_file>zh-CN.json</source_file>
    </language>
  </languages>
  <translation_files>
    <translation_file>
      <file>en-US.json</file>
    </translation_file>
    <translation_file>
      <file>zh-CN.json</file>
    </translation_file>
  </translation_files>
  <editor_configuration>
    <save_empty_translations>true</save_empty_translations>
    <copy_templates>
      <copy_template>{{'%1' | translate}}</copy_template>
      <copy_template>[translate]=&quot;'%1'&quot;</copy_template>
      <copy_template>_('%1')</copy_template>
    </copy_templates>
  </editor_configuration>
  <primary_language/>
  <configuration>
    <indent>tab</indent>
    <format>json</format>
    <support_arrays>true</support_arrays>
  </configuration>
</babeledit_project>

--#

--% /mts-admin/assets/locales/json/en-US.json
{
  "admin.brand": "U",
  "all": "All",
  "cancel": "Cancel",
  "column": "Column",
  "delete": "Delete",
  "deleteConfirmMessage": "Are you sure you want to delete the items?",
  "downloadCsv": "Download CSV",
  "errors.404.description": "The page you are looking for might have been removed had its name changed or is temporarily unavailable.",
  "errors.404.title": "404 - Page Not Found",
  "filter": "Filter",
  "filters": "Filters",
  "forgotPassword": "Forgot password?",
  "goHome": "Go Home",
  "hi": "Hi {name}",
  "home": "Home",
  "itemsSelected": "item(s) selected",
  "loadingData": "Loading data...",
  "loginWithGitHub": "Log in width GitHub",
  "logout.success": "You have logged out successfully.",
  "myProfile": "My Profile",
  "nextPage": "Next Page",
  "noData": "Sorry we could not find any data!",
  "of": "of",
  "ok": "OK",
  "other": "Other",
  "password": "Password",
  "previousPage": "Previous Page",
  "print": "Print",
  "rememberMe": "Remember me",
  "required": "Required.",
  "reset": "Reset",
  "rowsPerPage": "Rows per page:",
  "search": "Search",
  "signIn": "Sign in",
  "signOut": "Sign out",
  "toggleColumns": "Show/Hide Table Columns",
  "username": "Username",
  "viewColumns": "View Columns"
}

--#

--% /mts-admin/assets/locales/json/zh-CN.json
{
  "admin.brand": "控制台",
  "all": "全部",
  "cancel": "取消",
  "column": "列",
  "delete": "删除",
  "deleteConfirmMessage": "您确定要执行删除操作吗？",
  "downloadCsv": "下载表格",
  "errors.404.description": "您访问的页面，可能被删除，名称改变，又或是短时间内不能访问。",
  "errors.404.title": "404 - 页面没有找到",
  "filter": "过滤",
  "filters": "过滤条件",
  "forgotPassword": "忘记密码？",
  "goHome": "返回主页",
  "hi": "{name} 您好！",
  "home": "主页",
  "itemsSelected": "项已选择",
  "loadingData": "正在加载...",
  "loginWithGitHub": "使用GitHub账号登录",
  "logout.success": "您已成功退出登录。",
  "myProfile": "我的设置",
  "nextPage": "下页",
  "noData": "很抱歉，我们没有找到任何数据!",
  "of": "/",
  "ok": "确定",
  "other": "其它",
  "password": "密码",
  "previousPage": "上页",
  "print": "打印",
  "rememberMe": "记住我",
  "required": "必填项",
  "reset": "重置",
  "rowsPerPage": "每页行数",
  "search": "搜索",
  "signIn": "登录",
  "signOut": "退出登录",
  "toggleColumns": "显示或隐藏列",
  "username": "用户名",
  "viewColumns": "显示列"
}

--#

--% /mts-admin/.github/workflows/main.yml
# This is a basic workflow to help you get started with Actions

name: CI

# Controls when the action will run. Triggers the workflow on push or pull request
# events but only for the master branch
on:
  push:
  branches: [ master ]
  pull_request:
  branches: [ master ]

# A workflow run is made up of one or more jobs that can run sequentially or in parallel
jobs:
  # This workflow contains a single job called "build"
  build:
  # The type of runner that the job will run on
  runs-on: ubuntu-latest

  # Steps represent a sequence of tasks that will be executed as part of the job
  steps:
    - name: Setup Node
    uses: actions/setup-node@v1
    with:
      node-version: '10.x'

    # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
    - name: Checkout Code
    uses: actions/checkout@v2

    # Runs a single command using the runners shell
    - name: Install Dependencies
    run: npm install

    - name: Deploy Build
    run: npm run deploy-build

    # Runs a set of commands using the runners shell
    - name: Publish to GitHub Pages
    uses: JamesIves/github-pages-deploy-action@3.7.1
    with:
      BRANCH: gh-pages
      FOLDER: dist
      CLEAN: true



--#

--% /mts-admin/.vscode/launch.json
{
  // Use IntelliSense to learn about possible attributes.
  // Hover to view descriptions of existing attributes.
  // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
  "version": "0.2.0",
  "configurations": [
    {
      "type": "chrome",
      "request": "launch",
      "name": "Launch Chrome against localhost",
      "url": "http://localhost:8080",
      "webRoot": "${workspaceFolder}"
    }
  ]
}
--#

--% /mts-admin/.vscode/settings.json
{
  "liveServer.settings.root": "./",
  "workbench.colorCustomizations": {
    "tab.activeForeground": "#ffffff",
    "tab.activeBackground": "#6c69fb"
  }
}
--#
