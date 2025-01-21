--% index/fm.us
__TEMPLATE_PROJECT_DIR__,d
	%utama=__FILE__
	%__TEMPLATE_SERVER_PORT__=9500
	__TEMPLATE_WEBPACK_NAME__.js,f(e=utama=/webpack.js)
	readme.md,f(e=utama=/readme.md)
	run.sh,f(e=utama=/run.sh)	
	yarn.add.sh,f(e=utama=/yarn.add.sh)
	.babelrc,f(e=utama=/.babelrc)
	tsconfig.json,f(e=utama=/tsconfig.json)
	$*chmod a+x *.sh
	__TEMPLATE_MTS_DIR__,d(/mk)
		src,d(/mk)
			components,d(/mk)
			index.html,f(e=utama=/src/index.html)
			index.tsx,f(e=utama=/src/index.tsx)
	$*qterminal 2>/dev/null &
--#

--% /readme.md
latest demo:
/home/usef/tmp/retry-mts2/
--#

--% /tsconfig.json
{
  "compileOnSave": false,
  "compilerOptions": {
    "allowJs": true,
    "allowSyntheticDefaultImports": true,
    "baseUrl": "src",
    "esModuleInterop": true,
    "incremental": true,
    "jsx": "preserve",
    "lib": ["dom", "es2019"],
    "module": "esnext",
    "moduleResolution": "node",
    "outDir": "ts-build",
    "resolveJsonModule": true,
    "sourceMap": true,
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "strict": true,
    "strictFunctionTypes": false,
    "target": "esnext"
  },
  "include": [
    "__TEMPLATE_MTS_DIR__/src/**/*"
  ]
}
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

--% /yarn.add.sh
yarn add --dev @babel/cli @babel/core @babel/preset-env @babel/preset-react @babel/preset-typescript @types/jest @types/node @types/react @types/react-dom @typescript-eslint/eslint-plugin @typescript-eslint/parser babel-loader css-loader eslint eslint-config-prettier eslint-plugin-prettier eslint-plugin-react express file-loader html-webpack-plugin image-webpack-loader jest node-sass prettier react react-dom react-hot-loader rimraf sass-loader style-loader typescript webpack webpack-cli webpack-dev-server webpack-merge ts-loader @material-ui/core redux react-redux redux-thunk history
--#

--% /run.sh
./node_modules/.bin/webpack serve --mode development --config __TEMPLATE_WEBPACK_NAME__
--#

--% /src/index.tsx
import 'react-hot-loader';
import React from 'react';
import ReactDOM from 'react-dom';

import { Router, Redirect, Switch } from 'react-router-dom';
import { MuiThemeProvider } from '@material-ui/core/styles';
import { createMuiTheme } from "@material-ui/core/styles";

import { Provider } from 'react-redux';
import { useSelector } from 'react-redux';

import { createStore, applyMiddleware, combineReducers } from 'redux';
import { createBrowserHistory } from 'history';

const history = createBrowserHistory()


const themeConfig = {
  typography: {
    useNextVariants: true,
  },
  palette: {
    primary: indigo,
    secondary: green,
    error: red,
    // Used by `getContrastText()` to maximize the contrast between the background and
    // the text.
    contrastThreshold: 3,
    // Used to shift a color's luminance by approximately
    // two indexes within its tonal palette.
    // E.g., shift from Red 500 to Red 300 or Red 700.
    tonalOffset: 0.2
  }
};

type UserType = {
  email: string
  token: string
}

type RemoveActionType = {
  type: 'USER:REMOVE'
}

type SetActionType = {
  type: 'USER:SET'
  user: UserType
}

type UserStateType = {
  email: string | null
  token: string | null
}

const defaultUserState = {
  email: null,
  token: null
}

const userReducer = (state: UserStateType = defaultUserState, action: RemoveActionType | SetActionType) => {
  switch (action.type) {
    case actions.USER_SET:
      return {
        ...action.user
      }
    case actions.USER_REMOVE:
      return {
        ...defaultUserState
      }
    default:
      return state
  }
}

const settingsReducer = {
	toggleThemeMode: (state, action) => {
		if (action.payload) {
			state.darkMode = true;
			state.theme = {
				...themeConfig,
				palette: {
					...themeConfig.palette,
					primary: state.theme.palette.primary,
					secondary: state.theme.palette.secondary,
					type: "dark"
				}
			};
		} else {
			state.darkMode = false;
			state.theme = {
				...themeConfig,
				palette: {
					...themeConfig.palette,
					primary: state.theme.palette.primary,
					secondary: state.theme.palette.secondary
				}
			};
		}

		state.value = action.payload;
	},

	swapThemeColors: (state, action) => {
		if (action.payload) { // colorsSwaped
			state.colorsSwaped = true;
			state.theme = {
					...themeConfig,
					palette: {
						...state.theme.palette,
						primary: secondaryColor,
						secondary: primaryColor
					}
				};
		} else {
			state.colorsSwaped = false;
			state.theme = {
				...themeConfig,
				palette: {
					...state.theme.palette,
					primary: primaryColor,
					secondary: secondaryColor
				}
			};
		}
	},
},

// import store, { Provider } from 'store'
const store = createStore(
  
	combineReducers({
    user: userReducer,
    settings: settingsReducer,
  }),

  applyMiddleware(thunk)
);

const routes = {
  base: '/',

  unsigned: {
    signin: '/sign-in'
  },

  signed: {
    dashboard: '/dashboard',
    settings: '/settings',
  },
}

const signedPaths = Object.values(routes.signed)
const unsignedPaths = Object.values(routes.unsigned)

const DashboardLayout = () => {
	return (
    <div className={classes.wrapper}>
		<h1>DashboardLayout</h1>
		</div>
  )
}

const UnsignedLayout = () => {
	return (
    <div className={classes.wrapper}>
		<h1>UnsignedLayout</h1>
		</div>
  )
}

const getTheme = state => state.settings.theme;

const App = () => {
	
	const theTheme = useSelector(getTheme);

  return (
    <MuiThemeProvider theme={ createMuiTheme(theTheme) }>
      <CssBaseline />
      <Router history={history}>
        <Switch>
          <Route path={signedPaths} component={DashboardLayout} />
          <Route path={unsignedPaths} component={UnsignedLayout} />
          <Redirect to={routes.signed.dashboard} />
        </Switch>
      </Router>
    </MuiThemeProvider>
  )
}

if (module.hot) {
  module.hot.accept()
}

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('app')
)
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
			rule_ts_js,
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
			'common': path.resolve(process.cwd(), sourcedir, 'src', 'common'),
			'routes': path.resolve(process.cwd(), sourcedir, 'src', 'routes'),
		},
		extensions: ['.js', '.jsx', '.ts', '.tsx', '.json'],
		modules: [sourcedir, 'node_modules'],				
	},
	target: 'web',
}
--#
