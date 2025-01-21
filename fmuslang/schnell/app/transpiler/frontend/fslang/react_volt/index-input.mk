--% index/fmus
input,d(/mk)
	%utama=__FILE__
	%pertama=__CURDIR__/primary.mk
	%kedua=__CURDIR__/secondary.mk
	%sumberdaya=__CURDIR__/resources.mk
	.env,f(e=utama=/react-light/.env)
	.gitignore,f(e=utama=/react-light/.gitignore)
	gulpfile.js,f(e=kedua=/react-light/gulpfile.js)
	jsconfig.json,f(e=utama=/react-light/jsconfig.json)
	package.json,f(e=utama=/react-light/package.json)
	README.md,f(e=kedua=/react-light/README.md)
	webpack.config.js,f(e=utama=/react-light/webpack.config.js)
	.github,d(/mk)
		workflows,d(/mk)
			main.yml,f(e=utama=/react-light/.github/workflows/main.yml)
	public,d(/mk)
		apple-icon.png,f(b64=kedua=/react-light/public/apple-icon.png)
		favicon.ico,f(b64=kedua=/react-light/public/favicon.ico)
		index.html,f(e=kedua=/react-light/public/index.html)
		manifest.json,f(e=kedua=/react-light/public/manifest.json)
	src,d(/mk)
		index.js,f(e=utama=/react-light/src/index.js)
		logo.svg,f(e=sumberdaya=/react-light/src/logo.svg)
		routes.js,f(e=utama=/react-light/src/routes.js)
		assets,d(/load=__CURDIR__/assets.mk=index/fmus)
		components,d(/mk)
			FixedPlugin,d(/mk)
				FixedPlugin.js,f(e=utama=/react-light/src/components/FixedPlugin/FixedPlugin.js)
			Footer,d(/mk)
				Footer.js,f(e=utama=/react-light/src/components/Footer/Footer.js)
			Navbars,d(/mk)
				AdminNavbar.js,f(e=__CURDIR__/header.mk=/react-light/src/components/Navbars/AdminNavbar.js)
			Sidebar,d(/mk)
				Menu.js,f(e=utama=/react-light/src/components/Sidebar/Menu.js)
				Sidebar.css,f(e=utama=/react-light/src/components/Sidebar/Sidebar.css)
				Sidebar.js,f(e=utama=/react-light/src/components/Sidebar/Sidebar.js)
				SidebarToggler.css,f(e=utama=/react-light/src/components/Sidebar/SidebarToggler.css)
				SidebarToggler.js,f(e=utama=/react-light/src/components/Sidebar/SidebarToggler.js)
				SubMenu.js,f(e=utama=/react-light/src/components/Sidebar/SubMenu.js)
		layouts,d(/mk)
			Admin.css,f(e=utama=/react-light/src/layouts/Admin.css)
			Admin.js,f(e=utama=/react-light/src/layouts/Admin.js)
		views,d(/mk)
			Dashboard.js,f(e=utama=/react-light/src/views/Dashboard.js)
			Icons.js,f(e=utama=/react-light/src/views/Icons.js)
			Maps.js,f(e=utama=/react-light/src/views/Maps.js)
			Notifications.js,f(e=utama=/react-light/src/views/Notifications.js)
			TableList.js,f(e=utama=/react-light/src/views/TableList.js)
			Typography.js,f(e=utama=/react-light/src/views/Typography.js)
			Upgrade.js,f(e=utama=/react-light/src/views/Upgrade.js)
			UserProfile.js,f(e=utama=/react-light/src/views/UserProfile.js)
			.,d(/load=__CURDIR__/modal.mk=index/fmus)
--#

--% /react-light/.env
SKIP_PREFLIGHT_CHECK=true
CHOKIDAR_USEPOLLING=true
--#

--% /react-light/.gitignore
package-lock.json
node_modules/
yarn.lock
--#

--% /react-light/jsconfig.json
{
	"compilerOptions": {
		"baseUrl": "src",
		"paths": {
			"*": ["src/*"]
		}
	}
}
--#

--% /react-light/package.json
{
	"name": "light-bootstrap-dashboard-react",
	"version": "2.0.0",
	"dependencies": {
		"@babel/preset-env": "^7.16.0",
		"@babel/preset-react": "^7.16.0",
		"@babel/preset-typescript": "^7.16.0",
		"@fortawesome/fontawesome-free": "5.15.2",
		"@pmmmwh/react-refresh-webpack-plugin": "^0.5.1",
		"@popperjs/core": "2.9.3",
		"babel-loader": "^8.2.2",
		"bootstrap": "4.6.0",
		"chartist": "0.10.1",
		"css-loader": "^6.4.0",
		"css-minimizer-webpack-plugin": "^3.1.1",
		"file-loader": "^6.2.0",
		"gulp": "4.0.2",
		"gulp-append-prepend": "1.0.8",
		"html-loader": "^2.1.2",
		"html-webpack-plugin": "^5.5.0",
		"mini-css-extract-plugin": "^2.4.3",
		"node-sass": "4.14.1",
		"postcss": "^8.3.9",
		"postcss-loader": "^6.1.1",
		"react": "17.0.1",
		"react-bootstrap": "1.4.3",
		"react-chartist": "0.14.3",
		"react-dom": "17.0.1",
		"react-icons": "^4.2.0",
		"react-notification-alert": "0.0.13",
		"react-overlays": "^5.1.1",
		"react-refresh": "^0.10.0",
		"react-router": "5.2.0",
		"react-router-dom": "5.2.0",
		"react-scripts": "4.0.1",
		"sass": "^1.42.1",
		"sass-loader": "^12.1.0",
		"style-loader": "^3.3.0",
		"styled-components": "^5.3.1",
		"terser-webpack-plugin": "^5.2.4",
		"webpack": "^5.58.1",
		"webpack-bundle-analyzer": "^4.5.0",
		"webpack-cli": "^4.9.0",
		"webpack-dev-server": "^4.3.1"
	},
	"optionalDependencies": {
		"jquery": "3.5.1",
		"reactstrap": "8.9.0",
		"typescript": "4.1.3"
	},
	"scripts": {
		"start": "react-scripts start",
		"dev": "webpack serve --hot",
		"build": "react-scripts build && gulp licenses",
		"test": "react-scripts test --env=jsdom",
		"eject": "react-scripts eject",
		"install:clean": "rm -rf node_modules/ && rm -rf package-lock.json && npm install && npm start",
		"compile:scss": "node-sass src/assets/scss/light-bootstrap-dashboard-react.scss src/assets/css/light-bootstrap-dashboard-react.css",
		"minify:scss": "node-sass src/assets/scss/light-bootstrap-dashboard-react.scss src/assets/css/light-bootstrap-dashboard-react.min.css --output-style compressed",
		"map:scss": "node-sass src/assets/scss/light-bootstrap-dashboard-react.scss src/assets/css/light-bootstrap-dashboard-react.css --source-map true",
		"build:scss": "npm run compile:scss && npm run minify:scss && npm run map:scss"
	},
	"browserslist": {
		"production": [
			">0.2%",
			"not dead",
			"not op_mini all"
		],
		"development": [
			"last 1 chrome version",
			"last 1 firefox version",
			"last 1 safari version"
		]
	}
}
--#

--% /react-light/webpack.config.js
/**
"scripts": {
	"dev": "webpack serve --hot",
	"build": "NODE_ENV=production webpack"
},

"babel-loader": "^8.2.2",
"css-loader": "^6.4.0",
"file-loader": "^6.2.0",
"html-loader": "^2.1.2",
"html-webpack-plugin": "^5.3.2",
"postcss": "^8.3.9",
"postcss-loader": "^6.1.1",
"sass": "^1.42.1",
"sass-loader": "^12.1.0",
"style-loader": "^3.3.0",

"webpack": "^5.58.1",
"webpack-bundle-analyzer": "^4.4.2",
"webpack-cli": "^4.9.0",
"webpack-dev-server": "^4.3.1"
 */

// https://nodejs.org/docs/latest/api/path.html
const path = require("path"),

		// https://www.npmjs.com/package/webpack
		webpack = require('webpack'),

		// https://www.npmjs.com/package/terser-webpack-plugin
		TerserPlugin = require('terser-webpack-plugin'),

		// https://www.npmjs.com/package/mini-css-extract-plugin
		MiniCssExtractPlugin = require('mini-css-extract-plugin'),

		// https://www.npmjs.com/package/css-minimizer-webpack-plugin
		CssMinimizerPlugin = require("css-minimizer-webpack-plugin"),

		// https://www.npmjs.com/package/webpack-bundle-analyzer
		BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin,

		// https://www.npmjs.com/package/@pmmmwh/react-refresh-webpack-plugin
		ReactRefreshWebpackPlugin = require('@pmmmwh/react-refresh-webpack-plugin'),

		// https://webpack.js.org/plugins/html-webpack-plugin/
		HtmlWebPackPlugin = require('html-webpack-plugin')

const packageFolder = path.resolve(__dirname, 'build')
const isDevelopment = process.env.NODE_ENV !== "production"

module.exports = {
		mode: isDevelopment ? 'development' : 'production',
		devtool: isDevelopment ? 'source-map' : false,

		watchOptions: {
				poll: 1000,
				aggregateTimeout: 1000,
				ignored: ['**/node_modules']
		},

		entry: path.resolve(__dirname, "src", "index.js"),

		output: {
				path: packageFolder,
				sourceMapFilename: '[file].map',
				filename: `assets/js/[name].min.js`,
		},

		resolve: {
				extensions: ['.tsx', '.ts', '.jsx', '.js', '.scss', '.css'],
				modules: ['node_modules'],
				alias: {
					'layouts': path.resolve(__dirname, 'src/layouts'),
					'~asset': path.resolve(__dirname, 'src/assets'),
					'assets': path.resolve(__dirname, 'src/assets'),
					'routes.js': path.resolve(__dirname, 'src/routes.js'),
					'components': path.resolve(__dirname, 'src/components'),
					'views': path.resolve(__dirname, 'src/views'),
				},
		},

		module: {
				rules: [
						{
								test: //.(t|j)sx?$/,
								exclude: /node_modules/,
								use: {
										loader: "babel-loader",
										options: {
												presets: [
														// https://babeljs.io/docs/en/babel-preset-env
														"@babel/preset-env",
														// https://babeljs.io/docs/en/babel-preset-typescript
														"@babel/preset-typescript",
														// https://babeljs.io/docs/en/babel-preset-react
														["@babel/preset-react", { development: isDevelopment }],
												],
												plugins: [isDevelopment && require.resolve('react-refresh/babel')].filter(Boolean),
										}
								}
						},
						{
								test: //.s?[ac]ss$/i,
								use: [
										isDevelopment ? 'style-loader' :
												{
														// save the css to external file
														loader: MiniCssExtractPlugin.loader,
														options: {
																esModule: false
														},
												},
										{
												// becombine other css files into one
												// https://www.npmjs.com/package/css-loader
												loader: 'css-loader',
												options: {
														esModule: false,
														importLoaders: 2, // 2 other loaders used first, postcss-loader and sass-loader
														sourceMap: isDevelopment,
												}
										},
										// {
										//     // process tailwind stuff
										//     // https://webpack.js.org/loaders/postcss-loader/
										//     loader: "postcss-loader",
										//     options: {
										//         sourceMap: isDevelopment,
										//         postcssOptions: {
										//             plugins: [
										//                 require("tailwindcss"),
										//                 // add addtional postcss plugins here
										//                 // easily find plugins at https://www.postcss.parts/
										//             ]
										//         }
										//     },
										// },
										{
												// load sass files into css files
												loader: 'sass-loader',
												options: {
														sourceMap: isDevelopment
												}
										},
								],
						},
						{
								test: //.html$/i,
								loader: "html-loader",
								options: {
										esModule: false,
								},
						},
						{
								test: //.(png|svg|jpg|jpeg|gif|woff|woff2)$/,
								loader: 'file-loader',
								options: {
										name: 'assets/img/[name].[ext]',
										// outputPath: "images",
										esModule: false,
								},
						},
						{
								test: //.(ttf|eot|otf|woff)$/,
								loader: 'file-loader',
								options: {
										name: 'assets/fonts/[name].[ext]',
										esModule: false,
								},
						},
						{
								test: //.(ico)$/,
								loader: 'file-loader',
								options: {
										name: '[name].[ext]',
										esModule: false,
								},
						}
				],
		},

		plugins: [
				new webpack.ProvidePlugin({
						React: "react",
				}),

				// build html file
				new HtmlWebPackPlugin({
						template: "./public/index.html",
						filename: "./index.html"
				}),

				isDevelopment && new ReactRefreshWebpackPlugin(),

				// https://webpack.js.org/plugins/mini-css-extract-plugin/
				// dump css into its own files
				new MiniCssExtractPlugin({
						filename: `assets/css/[name].min.css`,
				}),

				// Bundle Analyzer, a visual view of what goes into each JS file.
				// https://www.npmjs.com/package/webpack-bundle-analyzer
				process.env.ANALYZE && new BundleAnalyzerPlugin()

		].filter(Boolean),

		optimization: {
				minimize: !isDevelopment,
				minimizer: [

						// https://webpack.js.org/plugins/terser-webpack-plugin/
						new TerserPlugin({
								terserOptions: {
										parse: {
												// We want terser to parse ecma 8 code. However, we don't want it
												// to apply minification steps that turns valid ecma 5 code
												// into invalid ecma 5 code. This is why the `compress` and `output`
												ecma: 8,
										},
										compress: {
												ecma: 5,
												inline: 2,
										},
										mangle: {
												// Find work around for Safari 10+
												safari10: true,
										},
										output: {
												ecma: 5,
												comments: false,
										}
								},

								// Use multi-process parallel running to improve the build speed
								parallel: true,

								extractComments: false,
						}),

						// https://webpack.js.org/plugins/css-minimizer-webpack-plugin/
						new CssMinimizerPlugin({
								// style do anything to the wordpress style.css file
								exclude: /style/.css$/,

								// Use multi-process parallel running to improve the build speed
								parallel: true,

								minimizerOptions: {
										preset: ["default", { discardComments: { removeAll: true } }],
										// plugins: ['autoprefixer'],
								},
						}),
				]
		},

		// https://webpack.js.org/configuration/dev-server/
		devServer: {
				port: 3005,
				host: '0.0.0.0',
				compress: true,
				allowedHosts: 'all',
				hot: true
		},

		performance: {
				hints: false,
				maxEntrypointSize: 512000,
				maxAssetSize: 512000
		}
}

--#

--% /react-light/.github/workflows/main.yml
name: Autocloser
on: [issues]
jobs:
	autoclose:
		runs-on: ubuntu-latest
		steps:
		- name: Issue auto-closer
			uses: roots/issue-closer-action@v1.1
			with:
				repo-token: ${{ secrets.GITHUB_TOKEN }}
				issue-close-message: "@${issue.user.login} this issue was automatically closed because it did not follow our rules:/n/n<pre>/n/n/n/nIMPORTANT: Please use the following link to create a new issue:/n/nhttps://www.creative-tim.com/new-issue/light-bootstrap-dashboard-react/n/n**If your issue was not created using the app above, it will be closed immediately.**/n/n/n/nLove Creative Tim? Do you need Angular, React, Vuejs or HTML? You can visit:/n👉  https://www.creative-tim.com/bundles/n👉  https://www.creative-tim.com/n/n/n</pre>/n/n"
				issue-pattern: (/#/#/# Version([/S/s.*]*?)/#/#/# Reproduction link([/S/s.*]*?)/#/#/# Operating System([/S/s.*]*?)/#/#/# Device([/S/s.*]*?)/#/#/# Browser & Version([/S/s.*]*?)/#/#/# Steps to reproduce([/S/s.*]*?)/#/#/# What is expected([/S/s.*]*?)/#/#/# What is actually happening([/S/s.*]*?)---([/S/s.*]*?)/#/#/# Solution([/S/s.*]*?)/#/#/# Additional comments([/S/s.*]*?)/</!-- generated by creative-tim-issues/. DO NOT REMOVE --/>)|(/#/#/# What is your enhancement([/S/s.*]*?)/</!-- generated by creative-tim-issues/. DO NOT REMOVE --/>)


--#

--% /react-light/src/index.js

import React from "react";
import ReactDOM from "react-dom";

import { BrowserRouter, Route, Switch, Redirect } from "react-router-dom";

import "bootstrap/dist/css/bootstrap.min.css";
import "./assets/css/animate.min.css";
import "./assets/scss/light-bootstrap-dashboard-react.scss?v=2.0.0";
import "./assets/css/demo.css";
import "@fortawesome/fontawesome-free/css/all.min.css";

import AdminLayout from "layouts/Admin.js";

ReactDOM.render(
	<BrowserRouter>
		<Switch>
			<Route path="/admin" render={(props) => <AdminLayout {...props} />} />
			<Redirect from="/" to="/admin/dashboard" />
		</Switch>
	</BrowserRouter>,
	document.getElementById("root")
);

--#

--% /react-light/src/routes.js

import Dashboard from "views/Dashboard.js";
import UserProfile from "views/UserProfile.js";
import TableList from "views/TableList.js";
import Typography from "views/Typography.js";
import Icons from "views/Icons.js";
import Maps from "views/Maps.js";
import Notifications from "views/Notifications.js";
import Upgrade from "views/Upgrade.js";

const dashboardRoutes = [
	// {
	//   upgrade: true,
	//   path: "/upgrade",
	//   name: "Upgrade to PRO",
	//   icon: "nc-icon nc-alien-33",
	//   component: Upgrade,
	//   layout: "/admin",
	// },
	{
		path: "/dashboard",
		name: "Dashboard",
		icon: "nc-icon nc-chart-pie-35",
		component: Dashboard,
		layout: "/admin",
	},
	{
		path: "/user",
		name: "User Profile",
		icon: "nc-icon nc-circle-09",
		component: UserProfile,
		layout: "/admin",
	},
	{
		path: "/table",
		name: "Table List",
		icon: "nc-icon nc-notes",
		component: TableList,
		layout: "/admin",
	},
	{
		path: "/typography",
		name: "Typography",
		icon: "nc-icon nc-paper-2",
		component: Typography,
		layout: "/admin",
	},
	{
		path: "/icons",
		name: "Icons",
		icon: "nc-icon nc-atom",
		component: Icons,
		layout: "/admin",
	},
	{
		path: "/maps",
		name: "Maps",
		icon: "nc-icon nc-pin-3",
		component: Maps,
		layout: "/admin",
	},
	{
		path: "/notifications",
		name: "Notifications",
		icon: "nc-icon nc-bell-55",
		component: Notifications,
		layout: "/admin",
	},
];

export default dashboardRoutes;
--#

--% /react-light/src/components/FixedPlugin/FixedPlugin.js

/*eslint-disable*/
import React, { Component } from "react";

import { Dropdown, Badge, Button, Form } from "react-bootstrap";

import sideBarImage1 from "assets/img/sidebar-1.jpg";
import sideBarImage2 from "assets/img/sidebar-2.jpg";
import sideBarImage3 from "assets/img/sidebar-3.jpg";
import sideBarImage4 from "assets/img/sidebar-4.jpg";

function FixedPlugin({
	hasImage,
	setHasImage,
	color,
	setColor,
	image,
	setImage,
}) {
	// constructor(props) {
	//   super(props);
	//   this.state = {
	//     classes: "dropdown show-dropdown open",
	//     bg_checked: true,
	//     bgImage: this.props.bgImage,
	//   };
	// }
	// handleClick = () => {
	//   this.props.handleFixedClick();
	// };
	// onChangeClick = () => {
	//   this.props.handleHasImage(!this.state.bg_checked);
	//   this.setState({ bg_checked: !this.state.bg_checked });
	// };
	return (
		<div className="fixed-plugin">
			<Dropdown>
				<Dropdown.Toggle
					id="dropdown-fixed-plugin"
					variant=""
					className="text-white border-0 opacity-100"
				>
					<i className="fas fa-cogs fa-2x mt-1"></i>
				</Dropdown.Toggle>
				<Dropdown.Menu>
					<li className="adjustments-line d-flex align-items-center justify-content-between">
						<p>Background Image</p>
						<Form.Check
							type="switch"
							id="custom-switch-1-image"
							checked={hasImage}
							onChange={setHasImage}
						/>
					</li>
					<li className="adjustments-line mt-3">
						<p>Filters</p>
						<div className="pull-right">
							<Badge
								variant="secondary"
								className={color === "black" ? "active" : ""}
								onClick={() => setColor("black")}
							></Badge>
							<Badge
								variant="azure"
								className={color === "azure" ? "active" : ""}
								onClick={() => setColor("azure")}
							></Badge>
							<Badge
								variant="green"
								className={color === "green" ? "active" : ""}
								onClick={() => setColor("green")}
							></Badge>
							<Badge
								variant="orange"
								className={color === "orange" ? "active" : ""}
								onClick={() => setColor("orange")}
							></Badge>
							<Badge
								variant="red"
								className={color === "red" ? "active" : ""}
								onClick={() => setColor("red")}
							></Badge>
							<Badge
								variant="purple"
								className={color === "purple" ? "active" : ""}
								onClick={() => setColor("purple")}
							></Badge>
						</div>
						<div className="clearfix"></div>
					</li>
					<li className="header-title">Sidebar Images</li>
					<li className={image === sideBarImage1 ? "active" : ""}>
						<a
							className="img-holder switch-trigger d-block"
							href="#pablo"
							onClick={(e) => {
								e.preventDefault();
								setImage(sideBarImage1);
							}}
						>
							<img alt="..." src={sideBarImage1}></img>
						</a>
					</li>
					<li className={image === sideBarImage2 ? "active" : ""}>
						<a
							className="img-holder switch-trigger d-block"
							href="#pablo"
							onClick={(e) => {
								e.preventDefault();
								setImage(sideBarImage2);
							}}
						>
							<img alt="..." src={sideBarImage2}></img>
						</a>
					</li>
					<li className={image === sideBarImage3 ? "active" : ""}>
						<a
							className="img-holder switch-trigger d-block"
							href="#pablo"
							onClick={(e) => {
								e.preventDefault();
								setImage(sideBarImage3);
							}}
						>
							<img alt="..." src={sideBarImage3}></img>
						</a>
					</li>
					<li className={image === sideBarImage4 ? "active" : ""}>
						<a
							className="img-holder switch-trigger d-block"
							href="#pablo"
							onClick={(e) => {
								e.preventDefault();
								setImage(sideBarImage4);
							}}
						>
							<img alt="..." src={sideBarImage4}></img>
						</a>
					</li>
					<li className="button-container">
						<div>
							<Button
								block
								className="btn-fill"
								href="http://www.creative-tim.com/product/light-bootstrap-dashboard-react"
								rel="noopener noreferrer"
								target="_blank"
								variant="info"
							>
								Download, it's free!
							</Button>
						</div>
					</li>
					<li className="button-container">
						<div>
							<Button
								block
								className="btn-fill"
								href="http://www.creative-tim.com/product/light-bootstrap-dashboard-react"
								rel="noopener noreferrer"
								target="_blank"
								variant="default"
							>
								Checkout docs.
							</Button>
						</div>
					</li>
					<li className="header-title pro-title text-center">
						Want more components?
					</li>
					<li className="button-container">
						<div>
							<Button
								block
								className="btn-fill"
								href="http://www.creative-tim.com/product/light-bootstrap-dashboard-pro-react"
								rel="noopener noreferrer"
								target="_blank"
								variant="primary"
							>
								Get The PRO Version!
							</Button>
						</div>
					</li>
					<li className="header-title" id="sharrreTitle">
						Thank you for sharing!
					</li>
					<li className="button-container mb-4">
						<Button
							className="btn-social btn-outline btn-round sharrre"
							id="twitter"
							variant="twitter"
						>
							<i className="fab fa-twitter"></i>· 256
						</Button>
						<Button
							className="btn-social btn-outline btn-round sharrre"
							id="facebook"
							variant="facebook"
						>
							<i className="fab fa-facebook-square"></i>· 426
						</Button>
					</li>
				</Dropdown.Menu>
			</Dropdown>
		</div>
	);
}

export default FixedPlugin;


--#

--% /react-light/src/components/Footer/Footer.js

import React, { Component } from "react";
import { Container } from "react-bootstrap";

class Footer extends Component {
	render() {
		return (
			<footer className="footer px-0 px-lg-3">
				<Container fluid>
					<nav>
						<ul className="footer-menu">
							<li>
								<a href="#pablo" onClick={(e) => e.preventDefault()}>
									Home
								</a>
							</li>
							<li>
								<a href="#pablo" onClick={(e) => e.preventDefault()}>
									Company
								</a>
							</li>
							<li>
								<a href="#pablo" onClick={(e) => e.preventDefault()}>
									Portfolio
								</a>
							</li>
							<li>
								<a href="#pablo" onClick={(e) => e.preventDefault()}>
									Blog
								</a>
							</li>
						</ul>
						<p className="copyright text-center">
							© {new Date().getFullYear()}{" "}
							<a href="http://www.creative-tim.com">Creative Tim</a>, made with
							love for a better web
						</p>
					</nav>
				</Container>
			</footer>
		);
	}
}

export default Footer;
--#

--% /react-light/src/components/Sidebar/Menu.js
import * as FaIcons from 'react-icons/fa';
import * as AiIcons from 'react-icons/ai';
import * as IoIcons from 'react-icons/io';
import * as RiIcons from 'react-icons/ri';

const Menu1 = [
	{
		title: 'Section 1',
		path: '#',
		icon: <AiIcons.AiFillHome />,
		iconClosed: <RiIcons.RiArrowDownSFill />,
		iconOpened: <RiIcons.RiArrowUpSFill />,

		subNav: [
			{
				title: 'Dashboard',
				path: '/admin/dashboard',
				icon: <IoIcons.IoIosPaper />
			},
			{
				title: 'User Profile',
				path: '/admin/user',
				icon: <IoIcons.IoIosPaper />
			},
		]
	},
]

const Menu2 = [
	{
		title: 'Section 2',
		path: '#',
		icon: <AiIcons.AiFillHome />,
		iconClosed: <RiIcons.RiArrowDownSFill />,
		iconOpened: <RiIcons.RiArrowUpSFill />,

		subNav: [
			{
				title: 'Tables',
				path: '/admin/table',
				icon: <IoIcons.IoIosPaper />
			},
			{
				title: 'Typography',
				path: '/admin/typography',
				icon: <IoIcons.IoIosPaper />
			},
		]
	},
]

const Menu3 = [
	{
		title: 'Section 3',
		path: '#',
		icon: <AiIcons.AiFillHome />,
		iconClosed: <RiIcons.RiArrowDownSFill />,
		iconOpened: <RiIcons.RiArrowUpSFill />,

		subNav: [
			{
				title: 'Icons',
				path: '/admin/icons',
				icon: <IoIcons.IoIosPaper />
			},
			{
				title: 'Maps',
				path: '/admin/maps',
				icon: <IoIcons.IoIosPaper />
			},
			{
				title: 'Notifications',
				path: '/admin/notifications',
				icon: <IoIcons.IoIosPaper />
			},
		]
	},
]

export {
	Menu1, Menu2, Menu3
};

--#

--% /react-light/src/components/Sidebar/Sidebar.css
:root {
	/* --left-distance: 15%; */
	--left-distance: 256px;
	--left-sidebar-percent: -256px; /* negative dari left-distance */
}

.sidebar-layout {
	position: fixed;
	top: 0;
	bottom: 0;
	left: var(--left-sidebar-percent);
	/* width: var(--left-distance); */
	overflow-y: auto;
	width: 256px;
	box-shadow: -3px -3px 7px #fffff7, 3px 3px 5px rgba(90,100,120,.2);
	transition: left .5s ease;
	z-index: 10;
	/* border: 1px solid crimson; */
}

.sidebar-layout.active {
	left: calc(var(--left-sidebar-percent) + var(--left-distance));
}

--#

--% /react-light/src/components/Sidebar/Sidebar.js

import React from "react";
import { useLocation, NavLink } from "react-router-dom";

import { Nav } from "react-bootstrap";
import {Menu1, Menu2, Menu3} from './Menu';
import SubMenu from './SubMenu';

import SidebarToggler from './SidebarToggler';
import './Sidebar.css';

const SidebarBottom = ({
	judul,
	data = Menu3
}) => {
	return (<>
		<h6 className="md:min-w-full text-blueGray-500 text-xs uppercase font-bold block pt-1 pb-4 no-underline">
			{judul}
		</h6>
		{data.map((item, index) => {
			return <SubMenu item={item} key={index} />;
		})}

	</>);
};

__TEMPLATE_MENU_DECLARE

function Sidebar({ 
	match, 
	// location, 
	history, active_classname, is_active, togglerMenu,
	color, image, routes 
}) {

	const location = useLocation();
	const pathname = location.pathname;

	const activeRoute = (routeName) => {
		// return location.pathname.indexOf(routeName) > -1 ? "active" : "";
		return pathname.indexOf(routeName) > -1 ? "active" : "";
	};

	return (
		<div>
			
			<SidebarToggler 
				active_classname={is_active ? 'sidebar-toggler active' : 'sidebar-toggler'} 
				togglerMenu={togglerMenu} 
				/>

			<div 
				className={`sidebar ` + active_classname} 
				data-image={image} 
				data-color={color}>

				<div
					className="sidebar-background"
					style={{
						backgroundImage: "url(" + image + ")",
					}}
				/>

				<div className="sidebar-wrapper">
					<div className="logo d-flex align-items-center justify-content-start">
						<a
							href="https://www.creative-tim.com?ref=lbd-sidebar"
							className="simple-text logo-mini mx-1"
						>
							<div className="logo-img">
								<img src={require("assets/img/reactlogo.png").default} alt="..."/>
							</div>
						</a>
						<a className="simple-text" href="http://www.creative-tim.com">
							Fulgent
						</a>
					</div>

					{/* <Nav>
						{routes.map((prop, key) => {
							if (!prop.redirect)
								return (
									<li
										className={
											prop.upgrade
												? "active active-pro"
												: activeRoute(prop.layout + prop.path)
										}
										key={key}
									>
										<NavLink
											to={prop.layout + prop.path}
											className="nav-link"
											activeClassName="active"
										>
											<i className={prop.icon} />
											<p>{prop.name}</p>
										</NavLink>
									</li>
								);
							return null;
						})}
					</Nav> */}

__TEMPLATE_MENU_CALL

				</div>
			</div>
		</div>
	);
}

export default Sidebar;
--#

--% /react-light/src/components/Sidebar/SidebarToggler.css
.sidebar-toggler {
	position: fixed;
	top: 50px;
	/* bottom: 0; */

	width: 50px;
	height: 50px;
	/* right: -50px; */
	left: 10px;
	transition: left .5s ease;
	z-index: 100;
}

.sidebar-toggler.active {
	left: calc(256px + 10px);
}

--#

--% /react-light/src/components/Sidebar/SidebarToggler.js
import React from "react";
import { 
	// Nav, Badge, Image, Dropdown, Accordion, Navbar,
	Button,  
} from "react-bootstrap";
import './SidebarToggler.css';

const SidebarToggler = (props) => {
	const {
		active_classname,
		togglerMenu,
	} = props;
	return (<div className={active_classname}>

	<Button onClick={togglerMenu}>
		<span className="sidebar-icon">
			M
		</span>
	</Button>

	</div>);
};

export default SidebarToggler;

--#

--% /react-light/src/components/Sidebar/SubMenu.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import styled from 'styled-components';

const SidebarLink = styled(Link)`
	display: flex;
	color: #e1e9fc;
	justify-content: space-between;
	align-items: center;
	padding: 20px;
	list-style: none;
	height: 60px;
	text-decoration: none;
	font-size: 18px;

	&:hover {
		background: #252831;
		border-left: 4px solid #632ce4;
		cursor: pointer;
	}
`;

const SidebarLabel = styled.span`
	margin-left: 16px;
`;

const DropdownLink = styled(Link)`
	background: #414757;
	height: 60px;
	padding-left: 3rem;
	display: flex;
	align-items: center;
	text-decoration: none;
	color: #f5f5f5;
	font-size: 18px;

	&:hover {
		background: #632ce4;
		cursor: pointer;
	}
`;

const SubMenu = ({ item }) => {
	const [subnav, setSubnav] = useState(false);

	const showSubnav = () => setSubnav(!subnav);

	return (
		<>
			<SidebarLink to={item.path} onClick={item.subNav && showSubnav}>
				<div>
					{item.icon}
					<SidebarLabel>{item.title}</SidebarLabel>
				</div>
				<div>
					{item.subNav && subnav
						? item.iconOpened
						: item.subNav
						? item.iconClosed
						: null}
				</div>
			</SidebarLink>
			{subnav &&
				item.subNav.map((item, index) => {
					return (
						<DropdownLink to={item.path} key={index}>
							{item.icon}
							<SidebarLabel>{item.title}</SidebarLabel>
						</DropdownLink>
					);
				})}
		</>
	);
};

export default SubMenu;

--#

--% /react-light/src/layouts/Admin.css
.main-section {
	transition: left .5s ease;
	margin-left: 0;
}

.main-section.active {
	margin-left: 256px;
	/* transition: left .5s ease; */
	transition: margin .5s ease-in-out;
}

--#

--% /react-light/src/layouts/Admin.js

import React, { Component } from "react";
import { useLocation, Route, Switch } from "react-router-dom";

import AdminNavbar from "components/Navbars/AdminNavbar";
import Footer from "components/Footer/Footer";
import Sidebar from "components/Sidebar/Sidebar";
// import FixedPlugin from "components/FixedPlugin/FixedPlugin.js";

import routes from "routes.js";
import sidebarImage from "assets/img/sidebar-3.jpg";
import './Admin.css';

function Admin() {
	const [image, setImage] = React.useState(sidebarImage);
	const [color, setColor] = React.useState("black");
	const [hasImage, setHasImage] = React.useState(true);

	const location = useLocation();
	const mainPanel = React.useRef(null);
	const [openSidebar, setOpenSidebar] = React.useState(false);

	const getRoutes = (routes) => {
		return routes.map((prop, key) => {
			if (prop.layout === "/admin") {
				return (
					<Route
						path={prop.layout + prop.path}
						render={(props) => <prop.component {...props} />}
						key={key}
					/>
				);
			} else {
				return null;
			}
		});
	};

	React.useEffect(() => {
		// document.documentElement.scrollTop = 0;
		// document.scrollingElement.scrollTop = 0;
		// mainPanel.current.scrollTop = 0;
		// if (
		//   window.innerWidth < 993 &&
		//   document.documentElement.className.indexOf("nav-open") !== -1
		// ) {
		//   document.documentElement.classList.toggle("nav-open");
		//   var element = document.getElementById("bodyClick");
		//   element.parentNode.removeChild(element);
		// }
	}, [location]);

	return (
		<>
			<div>
				
__TEMPLATE_SIDEBAR

				<main className={'content main-section' + (openSidebar?' active':'')}>
					<div className="main-panel" ref={mainPanel}>

						<AdminNavbar />

__TEMPLATE_CONTENT

__TEMPLATE_FOOTER

					</div>
				</main>

			</div>

__TEMPLATE_FLOATING

		</>
	);

}

export default Admin;


--#

--% /react-light/src/views/Dashboard.js
import React from "react";
import ChartistGraph from "react-chartist";
// react-bootstrap components
import {
	Badge,
	Button,
	Card,
	Navbar,
	Nav,
	Table,
	Container,
	Row,
	Col,
	Form,
	OverlayTrigger,
	Tooltip,
} from "react-bootstrap";

function Dashboard() {
	return (
		<>
			<Container fluid>
				<Row>
					<Col lg="3" sm="6">
						<Card className="card-stats">
							<Card.Body>
								<Row>
									<Col xs="5">
										<div className="icon-big text-center icon-warning">
											<i className="nc-icon nc-chart text-warning"></i>
										</div>
									</Col>
									<Col xs="7">
										<div className="numbers">
											<p className="card-category">Number</p>
											<Card.Title as="h4">150GB</Card.Title>
										</div>
									</Col>
								</Row>
							</Card.Body>
							<Card.Footer>
								<hr></hr>
								<div className="stats">
									<i className="fas fa-redo mr-1"></i>
									Update Now
								</div>
							</Card.Footer>
						</Card>
					</Col>
					<Col lg="3" sm="6">
						<Card className="card-stats">
							<Card.Body>
								<Row>
									<Col xs="5">
										<div className="icon-big text-center icon-warning">
											<i className="nc-icon nc-light-3 text-success"></i>
										</div>
									</Col>
									<Col xs="7">
										<div className="numbers">
											<p className="card-category">Revenue</p>
											<Card.Title as="h4">$ 1,345</Card.Title>
										</div>
									</Col>
								</Row>
							</Card.Body>
							<Card.Footer>
								<hr></hr>
								<div className="stats">
									<i className="far fa-calendar-alt mr-1"></i>
									Last day
								</div>
							</Card.Footer>
						</Card>
					</Col>
					<Col lg="3" sm="6">
						<Card className="card-stats">
							<Card.Body>
								<Row>
									<Col xs="5">
										<div className="icon-big text-center icon-warning">
											<i className="nc-icon nc-vector text-danger"></i>
										</div>
									</Col>
									<Col xs="7">
										<div className="numbers">
											<p className="card-category">Errors</p>
											<Card.Title as="h4">23</Card.Title>
										</div>
									</Col>
								</Row>
							</Card.Body>
							<Card.Footer>
								<hr></hr>
								<div className="stats">
									<i className="far fa-clock-o mr-1"></i>
									In the last hour
								</div>
							</Card.Footer>
						</Card>
					</Col>
					<Col lg="3" sm="6">
						<Card className="card-stats">
							<Card.Body>
								<Row>
									<Col xs="5">
										<div className="icon-big text-center icon-warning">
											<i className="nc-icon nc-favourite-28 text-primary"></i>
										</div>
									</Col>
									<Col xs="7">
										<div className="numbers">
											<p className="card-category">Followers</p>
											<Card.Title as="h4">+45K</Card.Title>
										</div>
									</Col>
								</Row>
							</Card.Body>
							<Card.Footer>
								<hr></hr>
								<div className="stats">
									<i className="fas fa-redo mr-1"></i>
									Update now
								</div>
							</Card.Footer>
						</Card>
					</Col>
				</Row>
				<Row>
					<Col md="8">
						<Card>
							<Card.Header>
								<Card.Title as="h4">Users Behavior</Card.Title>
								<p className="card-category">24 Hours performance</p>
							</Card.Header>
							<Card.Body>
								<div className="ct-chart" id="chartHours">
									<ChartistGraph
										data={{
											labels: [
												"9:00AM",
												"12:00AM",
												"3:00PM",
												"6:00PM",
												"9:00PM",
												"12:00PM",
												"3:00AM",
												"6:00AM",
											],
											series: [
												[287, 385, 490, 492, 554, 586, 698, 695],
												[67, 152, 143, 240, 287, 335, 435, 437],
												[23, 113, 67, 108, 190, 239, 307, 308],
											],
										}}
										type="Line"
										options={{
											low: 0,
											high: 800,
											showArea: false,
											height: "245px",
											axisX: {
												showGrid: false,
											},
											lineSmooth: true,
											showLine: true,
											showPoint: true,
											fullWidth: true,
											chartPadding: {
												right: 50,
											},
										}}
										responsiveOptions={[
											[
												"screen and (max-width: 640px)",
												{
													axisX: {
														labelInterpolationFnc: function (value) {
															return value[0];
														},
													},
												},
											],
										]}
									/>
								</div>
							</Card.Body>
							<Card.Footer>
								<div className="legend">
									<i className="fas fa-circle text-info"></i>
									Open <i className="fas fa-circle text-danger"></i>
									Click <i className="fas fa-circle text-warning"></i>
									Click Second Time
								</div>
								<hr></hr>
								<div className="stats">
									<i className="fas fa-history"></i>
									Updated 3 minutes ago
								</div>
							</Card.Footer>
						</Card>
					</Col>
					<Col md="4">
						<Card>
							<Card.Header>
								<Card.Title as="h4">Email Statistics</Card.Title>
								<p className="card-category">Last Campaign Performance</p>
							</Card.Header>
							<Card.Body>
								<div
									className="ct-chart ct-perfect-fourth"
									id="chartPreferences"
								>
									<ChartistGraph
										data={{
											labels: ["40%", "20%", "40%"],
											series: [40, 20, 40],
										}}
										type="Pie"
									/>
								</div>
								<div className="legend">
									<i className="fas fa-circle text-info"></i>
									Open <i className="fas fa-circle text-danger"></i>
									Bounce <i className="fas fa-circle text-warning"></i>
									Unsubscribe
								</div>
								<hr></hr>
								<div className="stats">
									<i className="far fa-clock"></i>
									Campaign sent 2 days ago
								</div>
							</Card.Body>
						</Card>
					</Col>
				</Row>
				<Row>
					<Col md="6">
						<Card>
							<Card.Header>
								<Card.Title as="h4">2017 Sales</Card.Title>
								<p className="card-category">All products including Taxes</p>
							</Card.Header>
							<Card.Body>
								<div className="ct-chart" id="chartActivity">
									<ChartistGraph
										data={{
											labels: [
												"Jan",
												"Feb",
												"Mar",
												"Apr",
												"Mai",
												"Jun",
												"Jul",
												"Aug",
												"Sep",
												"Oct",
												"Nov",
												"Dec",
											],
											series: [
												[
													542,
													443,
													320,
													780,
													553,
													453,
													326,
													434,
													568,
													610,
													756,
													895,
												],
												[
													412,
													243,
													280,
													580,
													453,
													353,
													300,
													364,
													368,
													410,
													636,
													695,
												],
											],
										}}
										type="Bar"
										options={{
											seriesBarDistance: 10,
											axisX: {
												showGrid: false,
											},
											height: "245px",
										}}
										responsiveOptions={[
											[
												"screen and (max-width: 640px)",
												{
													seriesBarDistance: 5,
													axisX: {
														labelInterpolationFnc: function (value) {
															return value[0];
														},
													},
												},
											],
										]}
									/>
								</div>
							</Card.Body>
							<Card.Footer>
								<div className="legend">
									<i className="fas fa-circle text-info"></i>
									Tesla Model S <i className="fas fa-circle text-danger"></i>
									BMW 5 Series
								</div>
								<hr></hr>
								<div className="stats">
									<i className="fas fa-check"></i>
									Data information certified
								</div>
							</Card.Footer>
						</Card>
					</Col>
					<Col md="6">
						<Card className="card-tasks">
							<Card.Header>
								<Card.Title as="h4">Tasks</Card.Title>
								<p className="card-category">Backend development</p>
							</Card.Header>
							<Card.Body>
								<div className="table-full-width">
									<Table>
										<tbody>
											<tr>
												<td>
													<Form.Check className="mb-1 pl-0">
														<Form.Check.Label>
															<Form.Check.Input
																defaultValue=""
																type="checkbox"
															></Form.Check.Input>
															<span className="form-check-sign"></span>
														</Form.Check.Label>
													</Form.Check>
												</td>
												<td>
													Sign contract for "What are conference organizers
													afraid of?"
												</td>
												<td className="td-actions text-right">
													<OverlayTrigger
														overlay={
															<Tooltip id="tooltip-488980961">
																Edit Task..
															</Tooltip>
														}
													>
														<Button
															className="btn-simple btn-link p-1"
															type="button"
															variant="info"
														>
															<i className="fas fa-edit"></i>
														</Button>
													</OverlayTrigger>
													<OverlayTrigger
														overlay={
															<Tooltip id="tooltip-506045838">Remove..</Tooltip>
														}
													>
														<Button
															className="btn-simple btn-link p-1"
															type="button"
															variant="danger"
														>
															<i className="fas fa-times"></i>
														</Button>
													</OverlayTrigger>
												</td>
											</tr>
											<tr>
												<td>
													<Form.Check className="mb-1 pl-0">
														<Form.Check.Label>
															<Form.Check.Input
																defaultChecked
																defaultValue=""
																type="checkbox"
															></Form.Check.Input>
															<span className="form-check-sign"></span>
														</Form.Check.Label>
													</Form.Check>
												</td>
												<td>
													Lines From Great Russian Literature? Or E-mails From
													My Boss?
												</td>
												<td className="td-actions text-right">
													<OverlayTrigger
														overlay={
															<Tooltip id="tooltip-537440761">
																Edit Task..
															</Tooltip>
														}
													>
														<Button
															className="btn-simple btn-link p-1"
															type="button"
															variant="info"
														>
															<i className="fas fa-edit"></i>
														</Button>
													</OverlayTrigger>
													<OverlayTrigger
														overlay={
															<Tooltip id="tooltip-21130535">Remove..</Tooltip>
														}
													>
														<Button
															className="btn-simple btn-link p-1"
															type="button"
															variant="danger"
														>
															<i className="fas fa-times"></i>
														</Button>
													</OverlayTrigger>
												</td>
											</tr>
											<tr>
												<td>
													<Form.Check className="mb-1 pl-0">
														<Form.Check.Label>
															<Form.Check.Input
																defaultChecked
																defaultValue=""
																type="checkbox"
															></Form.Check.Input>
															<span className="form-check-sign"></span>
														</Form.Check.Label>
													</Form.Check>
												</td>
												<td>
													Flooded: One year later, assessing what was lost and
													what was found when a ravaging rain swept through
													metro Detroit
												</td>
												<td className="td-actions text-right">
													<OverlayTrigger
														overlay={
															<Tooltip id="tooltip-577232198">
																Edit Task..
															</Tooltip>
														}
													>
														<Button
															className="btn-simple btn-link p-1"
															type="button"
															variant="info"
														>
															<i className="fas fa-edit"></i>
														</Button>
													</OverlayTrigger>
													<OverlayTrigger
														overlay={
															<Tooltip id="tooltip-773861645">Remove..</Tooltip>
														}
													>
														<Button
															className="btn-simple btn-link p-1"
															type="button"
															variant="danger"
														>
															<i className="fas fa-times"></i>
														</Button>
													</OverlayTrigger>
												</td>
											</tr>
											<tr>
												<td>
													<Form.Check className="mb-1 pl-0">
														<Form.Check.Label>
															<Form.Check.Input
																defaultChecked
																type="checkbox"
															></Form.Check.Input>
															<span className="form-check-sign"></span>
														</Form.Check.Label>
													</Form.Check>
												</td>
												<td>
													Create 4 Invisible User Experiences you Never Knew
													About
												</td>
												<td className="td-actions text-right">
													<OverlayTrigger
														overlay={
															<Tooltip id="tooltip-422471719">
																Edit Task..
															</Tooltip>
														}
													>
														<Button
															className="btn-simple btn-link p-1"
															type="button"
															variant="info"
														>
															<i className="fas fa-edit"></i>
														</Button>
													</OverlayTrigger>
													<OverlayTrigger
														overlay={
															<Tooltip id="tooltip-829164576">Remove..</Tooltip>
														}
													>
														<Button
															className="btn-simple btn-link p-1"
															type="button"
															variant="danger"
														>
															<i className="fas fa-times"></i>
														</Button>
													</OverlayTrigger>
												</td>
											</tr>
											<tr>
												<td>
													<Form.Check className="mb-1 pl-0">
														<Form.Check.Label>
															<Form.Check.Input
																defaultValue=""
																type="checkbox"
															></Form.Check.Input>
															<span className="form-check-sign"></span>
														</Form.Check.Label>
													</Form.Check>
												</td>
												<td>Read "Following makes Medium better"</td>
												<td className="td-actions text-right">
													<OverlayTrigger
														overlay={
															<Tooltip id="tooltip-160575228">
																Edit Task..
															</Tooltip>
														}
													>
														<Button
															className="btn-simple btn-link p-1"
															type="button"
															variant="info"
														>
															<i className="fas fa-edit"></i>
														</Button>
													</OverlayTrigger>
													<OverlayTrigger
														overlay={
															<Tooltip id="tooltip-922981635">Remove..</Tooltip>
														}
													>
														<Button
															className="btn-simple btn-link p-1"
															type="button"
															variant="danger"
														>
															<i className="fas fa-times"></i>
														</Button>
													</OverlayTrigger>
												</td>
											</tr>
											<tr>
												<td>
													<Form.Check className="mb-1 pl-0">
														<Form.Check.Label>
															<Form.Check.Input
																defaultValue=""
																disabled
																type="checkbox"
															></Form.Check.Input>
															<span className="form-check-sign"></span>
														</Form.Check.Label>
													</Form.Check>
												</td>
												<td>Unfollow 5 enemies from twitter</td>
												<td className="td-actions text-right">
													<OverlayTrigger
														overlay={
															<Tooltip id="tooltip-938342127">
																Edit Task..
															</Tooltip>
														}
													>
														<Button
															className="btn-simple btn-link p-1"
															type="button"
															variant="info"
														>
															<i className="fas fa-edit"></i>
														</Button>
													</OverlayTrigger>
													<OverlayTrigger
														overlay={
															<Tooltip id="tooltip-119603706">Remove..</Tooltip>
														}
													>
														<Button
															className="btn-simple btn-link p-1"
															type="button"
															variant="danger"
														>
															<i className="fas fa-times"></i>
														</Button>
													</OverlayTrigger>
												</td>
											</tr>
										</tbody>
									</Table>
								</div>
							</Card.Body>
							<Card.Footer>
								<hr></hr>
								<div className="stats">
									<i className="now-ui-icons loader_refresh spin"></i>
									Updated 3 minutes ago
								</div>
							</Card.Footer>
						</Card>
					</Col>
				</Row>
			</Container>
		</>
	);
}

export default Dashboard;


--#

--% /react-light/src/views/Icons.js
import React from "react";

// react-bootstrap components
import {
	Badge,
	Button,
	Card,
	Navbar,
	Nav,
	Container,
	Row,
	Col,
} from "react-bootstrap";

function Icons() {
	return (
		<>
			<Container fluid>
				<Row>
					<Col md="12">
						<Card>
							<Card.Header>
								<Card.Title as="h4">100 Awesome Nucleo Icons</Card.Title>
								<p className="card-category">
									Handcrafted by our friends from{" "}
									<a href="https://nucleoapp.com/?ref=1712">NucleoApp</a>
								</p>
							</Card.Header>
							<Card.Body className="all-icons">
								<Row>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-air-baloon"></i>
											<p>nc-air-baloon</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-album-2"></i>
											<p>nc-album-2</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-alien-33"></i>
											<p>nc-alien-33</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-align-center"></i>
											<p>nc-align-center</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-align-left-2"></i>
											<p>nc-align-left-2</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-ambulance"></i>
											<p>nc-ambulance</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-android"></i>
											<p>nc-android</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-app"></i>
											<p>nc-app</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-apple"></i>
											<p>nc-apple</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-atom"></i>
											<p>nc-atom</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-attach-87"></i>
											<p>nc-attach-87</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-audio-92"></i>
											<p>nc-audio-92</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-backpack"></i>
											<p>nc-backpack</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-badge"></i>
											<p>nc-badge</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-bag"></i>
											<p>nc-bag</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-bank"></i>
											<p>nc-bank</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-battery-81"></i>
											<p>nc-battery-81</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-bell-55"></i>
											<p>nc-bell-55</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-bold"></i>
											<p>nc-bold</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-bulb-63"></i>
											<p>nc-bulb-63</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-bullet-list-67"></i>
											<p>nc-bullet-list-67</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-bus-front-12"></i>
											<p>nc-bus-front-12</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-button-pause"></i>
											<p>nc-button-pause</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-button-play"></i>
											<p>nc-button-play</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-button-power"></i>
											<p>nc-button-power</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-camera-20"></i>
											<p>nc-camera-20</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-caps-small"></i>
											<p>nc-caps-small</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-cart-simple"></i>
											<p>nc-cart-simple</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-cctv"></i>
											<p>nc-cctv</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-chart-bar-32"></i>
											<p>nc-chart-bar-32</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-chart-pie-35"></i>
											<p>nc-chart-pie-35</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-chart-pie-36"></i>
											<p>nc-chart-pie-36</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-chart"></i>
											<p>nc-chart</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-chat-round"></i>
											<p>nc-chat-round</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-check-2"></i>
											<p>nc-check-2</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-circle-09"></i>
											<p>nc-circle-09</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-circle"></i>
											<p>nc-circle</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-cloud-download-93"></i>
											<p>nc-cloud-download-93</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-cloud-upload-94"></i>
											<p>nc-cloud-upload-94</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-compass-05"></i>
											<p>nc-compass-05</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-controller-modern"></i>
											<p>nc-controller-modern</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-credit-card"></i>
											<p>nc-credit-card</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-delivery-fast"></i>
											<p>nc-delivery-fast</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-email-83"></i>
											<p>nc-email-83</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-email-85"></i>
											<p>nc-email-85</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-explore-2"></i>
											<p>nc-explore-2</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-fav-remove"></i>
											<p>nc-fav-remove</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-favourite-28"></i>
											<p>nc-favourite-28</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-globe-2"></i>
											<p>nc-globe-2</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-grid-45"></i>
											<p>nc-grid-45</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-headphones-2"></i>
											<p>nc-headphones-2</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-html5"></i>
											<p>nc-html5</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-istanbul"></i>
											<p>nc-istanbul</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-key-25"></i>
											<p>nc-key-25</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-layers-3"></i>
											<p>nc-layers-3</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-light-3"></i>
											<p>nc-light-3</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-lock-circle-open"></i>
											<p>nc-lock-circle-open</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-map-big"></i>
											<p>nc-map-big</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-mobile"></i>
											<p>nc-mobile</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-money-coins"></i>
											<p>nc-money-coins</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-note-03"></i>
											<p>nc-note-03</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-notes"></i>
											<p>nc-notes</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-notification-70"></i>
											<p>nc-notification-70</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-palette"></i>
											<p>nc-palette</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-paper-2"></i>
											<p>nc-paper-2</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-pin-3"></i>
											<p>nc-pin-3</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-planet"></i>
											<p>nc-planet</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-preferences-circle-rotate"></i>
											<p>nc-preferences-circle-rotate</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-puzzle-10"></i>
											<p>nc-puzzle-10</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-quote"></i>
											<p>nc-quote</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-refresh-02"></i>
											<p>nc-refresh-02</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-ruler-pencil"></i>
											<p>nc-ruler-pencil</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-satisfied"></i>
											<p>nc-satisfied</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-scissors"></i>
											<p>nc-scissors</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-send"></i>
											<p>nc-send</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-settings-90"></i>
											<p>nc-settings-90</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-settings-gear-64"></i>
											<p>nc-settings-gear-64</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-settings-tool-66"></i>
											<p>nc-settings-tool-66</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-simple-add"></i>
											<p>nc-simple-add</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-simple-delete"></i>
											<p>nc-simple-delete</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-simple-remove"></i>
											<p>nc-simple-remove</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-single-02"></i>
											<p>nc-single-02</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-single-copy-04"></i>
											<p>nc-single-copy-04</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-spaceship"></i>
											<p>nc-spaceship</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-square-pin"></i>
											<p>nc-square-pin</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-stre-down"></i>
											<p>nc-stre-down</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-stre-left"></i>
											<p>nc-stre-left</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-stre-right"></i>
											<p>nc-stre-right</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-stre-up"></i>
											<p>nc-stre-up</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-sun-fog-29"></i>
											<p>nc-sun-fog-29</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-support-17"></i>
											<p>nc-support-17</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-tablet-2"></i>
											<p>nc-tablet-2</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-tag-content"></i>
											<p>nc-tag-content</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-tap-01"></i>
											<p>nc-tap-01</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-time-alarm"></i>
											<p>nc-time-alarm</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-tv-2"></i>
											<p>nc-tv-2</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-umbrella-13"></i>
											<p>nc-umbrella-13</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-vector"></i>
											<p>nc-vector</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-watch-time"></i>
											<p>nc-watch-time</p>
										</div>
									</Col>
									<Col className="font-icon-list" lg="2" md="3" sm="4" xs="6">
										<div className="font-icon-detail">
											<i className="nc-icon nc-zoom-split"></i>
											<p>nc-zoom-split</p>
										</div>
									</Col>
								</Row>
							</Card.Body>
						</Card>
					</Col>
				</Row>
			</Container>
		</>
	);
}

export default Icons;


--#

--% /react-light/src/views/Maps.js
import React from "react";

// react-bootstrap components
import { Badge, Button, Navbar, Nav, Container } from "react-bootstrap";

function Maps() {
	const mapRef = React.useRef(null);
	React.useEffect(() => {
		let google = window.google;
		let map = mapRef.current;
		let lat = "40.748817";
		let lng = "-73.985428";
		const myLatlng = new google.maps.LatLng(lat, lng);
		const mapOptions = {
			zoom: 13,
			center: myLatlng,
			scrollwheel: false,
			zoomControl: true,
		};

		map = new google.maps.Map(map, mapOptions);

		const marker = new google.maps.Marker({
			position: myLatlng,
			map: map,
			animation: google.maps.Animation.DROP,
			title: "Light Bootstrap Dashboard PRO React!",
		});

		const contentString =
			'<div class="info-window-content"><h2>Light Bootstrap Dashboard PRO React</h2>' +
			"<p>A premium Admin for React-Bootstrap, Bootstrap, React, and React Hooks.</p></div>";

		const infowindow = new google.maps.InfoWindow({
			content: contentString,
		});

		google.maps.event.addListener(marker, "click", function () {
			infowindow.open(map, marker);
		});
	}, []);
	return (
		<>
			<div className="map-container">
				<div id="map" ref={mapRef}></div>
			</div>
		</>
	);
}

export default Maps;


--#

--% /react-light/src/views/Notifications.js
import React from "react";
// react plugin for creating notifications over the dashboard
import NotificationAlert from "react-notification-alert";
// react-bootstrap components
import {
	Alert,
	Badge,
	Button,
	Card,
	Modal,
	Navbar,
	Nav,
	Container,
	Row,
	Col,
} from "react-bootstrap";

function Notifications() {
	const [showModal, setShowModal] = React.useState(false);
	const notificationAlertRef = React.useRef(null);
	const notify = (place) => {
		var color = Math.floor(Math.random() * 5 + 1);
		var type;
		switch (color) {
			case 1:
				type = "primary";
				break;
			case 2:
				type = "success";
				break;
			case 3:
				type = "danger";
				break;
			case 4:
				type = "warning";
				break;
			case 5:
				type = "info";
				break;
			default:
				break;
		}
		var options = {};
		options = {
			place: place,
			message: (
				<div>
					<div>
						Welcome to <b>Light Bootstrap Dashboard React</b> - a beautiful
						freebie for every web developer.
					</div>
				</div>
			),
			type: type,
			icon: "nc-icon nc-bell-55",
			autoDismiss: 7,
		};
		notificationAlertRef.current.notificationAlert(options);
	};
	return (
		<>
			<div className="rna-container">
				<NotificationAlert ref={notificationAlertRef} />
			</div>
			<Container fluid>
				<Card>
					<Card.Header>
						<Card.Title as="h4">Notifications</Card.Title>
						<p className="card-category">
							Handcrafted by our friend and colleague{" "}
							<a
								href="https://github.com/EINazare"
								rel="noopener noreferrer"
								target="_blank"
							>
								Nazare Emanuel-Ioan
							</a>
							. Please checkout the{" "}
							<a
								href="https://github.com/creativetimofficial/react-notification-alert"
								rel="noopener noreferrer"
								target="_blank"
							>
								full documentation.
							</a>
						</p>
					</Card.Header>
					<Card.Body>
						<Row>
							<Col md="6">
								<h5>
									<small>Notifications Style</small>
								</h5>
								<Alert variant="info">
									<span>This is a plain notification</span>
								</Alert>
								<Alert variant="info">
									<button
										aria-hidden={true}
										className="close"
										data-dismiss="alert"
										type="button"
									>
										<i className="nc-icon nc-simple-remove"></i>
									</button>
									<span>This is a notification with close button.</span>
								</Alert>
								<Alert className="alert-with-icon" variant="info">
									<button
										aria-hidden={true}
										className="close"
										data-dismiss="alert"
										type="button"
									>
										<i className="nc-icon nc-simple-remove"></i>
									</button>
									<span
										data-notify="icon"
										className="nc-icon nc-bell-55"
									></span>
									<span>
										This is a notification with close button and icon.
									</span>
								</Alert>
								<Alert className="alert-with-icon" variant="info">
									<button
										aria-hidden={true}
										className="close"
										data-dismiss="alert"
										type="button"
									>
										<i className="nc-icon nc-simple-remove"></i>
									</button>
									<span
										data-notify="icon"
										className="nc-icon nc-bell-55"
									></span>
									<span>
										This is a notification with close button and icon and have
										many lines. You can see that the icon and the close button
										are always vertically aligned. This is a beautiful
										notification. So you don't have to worry about the style.
									</span>
								</Alert>
							</Col>
							<Col md="6">
								<h5>
									<small>Notification States</small>
								</h5>
								<Alert variant="primary">
									<button
										aria-hidden={true}
										className="close"
										data-dismiss="alert"
										type="button"
									>
										<i className="nc-icon nc-simple-remove"></i>
									</button>
									<span>
										<b>Primary -</b>
										This is a regular notification made with ".alert-primary"
									</span>
								</Alert>
								<Alert variant="info">
									<button
										aria-hidden={true}
										className="close"
										data-dismiss="alert"
										type="button"
									>
										<i className="nc-icon nc-simple-remove"></i>
									</button>
									<span>
										<b>Info -</b>
										This is a regular notification made with ".alert-info"
									</span>
								</Alert>
								<Alert variant="success">
									<button
										aria-hidden={true}
										className="close"
										data-dismiss="alert"
										type="button"
									>
										<i className="nc-icon nc-simple-remove"></i>
									</button>
									<span>
										<b>Success -</b>
										This is a regular notification made with ".alert-success"
									</span>
								</Alert>
								<Alert variant="warning">
									<button
										aria-hidden={true}
										className="close"
										data-dismiss="alert"
										type="button"
									>
										<i className="nc-icon nc-simple-remove"></i>
									</button>
									<span>
										<b>Warning -</b>
										This is a regular notification made with ".alert-warning"
									</span>
								</Alert>
								<Alert variant="danger">
									<button
										aria-hidden={true}
										className="close"
										data-dismiss="alert"
										type="button"
									>
										<i className="nc-icon nc-simple-remove"></i>
									</button>
									<span>
										<b>Danger -</b>
										This is a regular notification made with ".alert-danger"
									</span>
								</Alert>
							</Col>
						</Row>
						<br></br>
						<br></br>
						<div className="places-buttons">
							<Row>
								<Col className="offset-md-3 text-center" md="6">
									<Card.Title as="h4">Notifications Places</Card.Title>
									<p className="card-category">
										<small>Click to view notifications</small>
									</p>
								</Col>
							</Row>
							<Row className="justify-content-center">
								<Col lg="3" md="3">
									<Button block onClick={() => notify("tl")} variant="default">
										Top Left
									</Button>
								</Col>
								<Col lg="3" md="3">
									<Button block onClick={() => notify("tc")} variant="default">
										Top Center
									</Button>
								</Col>
								<Col lg="3" md="3">
									<Button block onClick={() => notify("tr")} variant="default">
										Top Right
									</Button>
								</Col>
							</Row>
							<Row className="justify-content-center">
								<Col lg="3" md="3">
									<Button block onClick={() => notify("bl")} variant="default">
										Bottom Left
									</Button>
								</Col>
								<Col lg="3" md="3">
									<Button block onClick={() => notify("bc")} variant="default">
										Bottom Center
									</Button>
								</Col>
								<Col lg="3" md="3">
									<Button block onClick={() => notify("br")} variant="default">
										Bottom Right
									</Button>
								</Col>
							</Row>
						</div>
						<Row>
							<Col className="text-center" md="12">
								<h4 className="title">Modal</h4>
								<Button
									className="btn-fill btn-wd"
									variant="info"
									onClick={() => setShowModal(true)}
								>
									Launch Modal Mini
								</Button>
							</Col>
						</Row>
					</Card.Body>
				</Card>
				{/* Mini Modal */}
				<Modal
					className="modal-mini modal-primary"
					show={showModal}
					onHide={() => setShowModal(false)}
				>
					<Modal.Header className="justify-content-center">
						<div className="modal-profile">
							<i className="nc-icon nc-bulb-63"></i>
						</div>
					</Modal.Header>
					<Modal.Body className="text-center">
						<p>Always have an access to your profile</p>
					</Modal.Body>
					<div className="modal-footer">
						<Button
							className="btn-simple"
							type="button"
							variant="link"
							onClick={() => setShowModal(false)}
						>
							Back
						</Button>
						<Button
							className="btn-simple"
							type="button"
							variant="link"
							onClick={() => setShowModal(false)}
						>
							Close
						</Button>
					</div>
				</Modal>
				{/* End Modal */}
			</Container>
		</>
	);
}

export default Notifications;


--#

--% /react-light/src/views/TableList.js
import React from "react";

// react-bootstrap components
import {
	Badge,
	Button,
	Card,
	Navbar,
	Nav,
	Table,
	Container,
	Row,
	Col,
} from "react-bootstrap";

function TableList() {
	return (
		<>
			<Container fluid>
				<Row>
					<Col md="12">
						<Card className="strpied-tabled-with-hover">
							<Card.Header>
								<Card.Title as="h4">Striped Table with Hover</Card.Title>
								<p className="card-category">
									Here is a subtitle for this table
								</p>
							</Card.Header>
							<Card.Body className="table-full-width table-responsive px-0">
								<Table className="table-hover table-striped">
									<thead>
										<tr>
											<th className="border-0">ID</th>
											<th className="border-0">Name</th>
											<th className="border-0">Salary</th>
											<th className="border-0">Country</th>
											<th className="border-0">City</th>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td>1</td>
											<td>Dakota Rice</td>
											<td>$36,738</td>
											<td>Niger</td>
											<td>Oud-Turnhout</td>
										</tr>
										<tr>
											<td>2</td>
											<td>Minerva Hooper</td>
											<td>$23,789</td>
											<td>Curaçao</td>
											<td>Sinaai-Waas</td>
										</tr>
										<tr>
											<td>3</td>
											<td>Sage Rodriguez</td>
											<td>$56,142</td>
											<td>Netherlands</td>
											<td>Baileux</td>
										</tr>
										<tr>
											<td>4</td>
											<td>Philip Chaney</td>
											<td>$38,735</td>
											<td>Korea, South</td>
											<td>Overland Park</td>
										</tr>
										<tr>
											<td>5</td>
											<td>Doris Greene</td>
											<td>$63,542</td>
											<td>Malawi</td>
											<td>Feldkirchen in Kärnten</td>
										</tr>
										<tr>
											<td>6</td>
											<td>Mason Porter</td>
											<td>$78,615</td>
											<td>Chile</td>
											<td>Gloucester</td>
										</tr>
									</tbody>
								</Table>
							</Card.Body>
						</Card>
					</Col>
					<Col md="12">
						<Card className="card-plain table-plain-bg">
							<Card.Header>
								<Card.Title as="h4">Table on Plain Background</Card.Title>
								<p className="card-category">
									Here is a subtitle for this table
								</p>
							</Card.Header>
							<Card.Body className="table-full-width table-responsive px-0">
								<Table className="table-hover">
									<thead>
										<tr>
											<th className="border-0">ID</th>
											<th className="border-0">Name</th>
											<th className="border-0">Salary</th>
											<th className="border-0">Country</th>
											<th className="border-0">City</th>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td>1</td>
											<td>Dakota Rice</td>
											<td>$36,738</td>
											<td>Niger</td>
											<td>Oud-Turnhout</td>
										</tr>
										<tr>
											<td>2</td>
											<td>Minerva Hooper</td>
											<td>$23,789</td>
											<td>Curaçao</td>
											<td>Sinaai-Waas</td>
										</tr>
										<tr>
											<td>3</td>
											<td>Sage Rodriguez</td>
											<td>$56,142</td>
											<td>Netherlands</td>
											<td>Baileux</td>
										</tr>
										<tr>
											<td>4</td>
											<td>Philip Chaney</td>
											<td>$38,735</td>
											<td>Korea, South</td>
											<td>Overland Park</td>
										</tr>
										<tr>
											<td>5</td>
											<td>Doris Greene</td>
											<td>$63,542</td>
											<td>Malawi</td>
											<td>Feldkirchen in Kärnten</td>
										</tr>
										<tr>
											<td>6</td>
											<td>Mason Porter</td>
											<td>$78,615</td>
											<td>Chile</td>
											<td>Gloucester</td>
										</tr>
									</tbody>
								</Table>
							</Card.Body>
						</Card>
					</Col>
				</Row>
			</Container>
		</>
	);
}

export default TableList;


--#

--% /react-light/src/views/Typography.js
import React from "react";

// react-bootstrap components
import {
	Badge,
	Button,
	Card,
	Navbar,
	Nav,
	Container,
	Row,
	Col,
} from "react-bootstrap";

function Typography() {
	return (
		<>
			<Container fluid>
				<Row>
					<Col md="12">
						<Card>
							<Card.Header>
								<Card.Title as="h4">Light Bootstrap Table Heading</Card.Title>
								<p className="card-category">
									Created using Montserrat Font Family
								</p>
							</Card.Header>
							<Card.Body>
								<div className="typography-line">
									<h1>
										<span>Header 1</span>
										The Life of Light Bootstrap Dashboard React
									</h1>
								</div>
								<div className="typography-line">
									<h2>
										<span>Header 2</span>
										The Life of Light Bootstrap Dashboard React
									</h2>
								</div>
								<div className="typography-line">
									<h3>
										<span>Header 3</span>
										The Life of Light Bootstrap Dashboard React
									</h3>
								</div>
								<div className="typography-line">
									<h4>
										<span>Header 4</span>
										The Life of Light Bootstrap Dashboard React
									</h4>
								</div>
								<div className="typography-line">
									<h5>
										<span>Header 5</span>
										The Life of Light Bootstrap Dashboard React
									</h5>
								</div>
								<div className="typography-line">
									<h6>
										<span>Header 6</span>
										The Life of Light Bootstrap Dashboard React
									</h6>
								</div>
								<div className="typography-line">
									<p>
										<span>Paragraph</span>I will be the leader of a company that
										ends up being worth billions of dollars, because I got the
										answers. I understand culture. I am the nucleus. I think
										that’s a responsibility that I have, to push possibilities,
										to show people, this is the level that things could be at.
									</p>
								</div>
								<div className="typography-line">
									<span>Quote</span>
									<blockquote>
										<p className="blockquote blockquote-primary">
											"I will be the leader of a company that ends up being
											worth billions of dollars, because I got the answers. I
											understand culture. I am the nucleus. I think that’s a
											responsibility that I have, to push possibilities, to show
											people, this is the level that things could be at."{" "}
											<br></br>
											<br></br>
											<small>- Noaa</small>
										</p>
									</blockquote>
								</div>
								<div className="typography-line">
									<span>Muted Text</span>
									<p className="text-muted">
										I will be the leader of a company that ends up being worth
										billions of dollars, because I got the answers...
									</p>
								</div>
								<div className="typography-line">
									<span>Primary Text</span>
									<p className="text-primary">
										I will be the leader of a company that ends up being worth
										billions of dollars, because I got the answers...
									</p>
								</div>
								<div className="typography-line">
									<span>Info Text</span>
									<p className="text-info">
										I will be the leader of a company that ends up being worth
										billions of dollars, because I got the answers...
									</p>
								</div>
								<div className="typography-line">
									<span>Success Text</span>
									<p className="text-success">
										I will be the leader of a company that ends up being worth
										billions of dollars, because I got the answers...
									</p>
								</div>
								<div className="typography-line">
									<span>Warning Text</span>
									<p className="text-warning">
										I will be the leader of a company that ends up being worth
										billions of dollars, because I got the answers...
									</p>
								</div>
								<div className="typography-line">
									<span>Danger Text</span>
									<p className="text-danger">
										I will be the leader of a company that ends up being worth
										billions of dollars, because I got the answers...
									</p>
								</div>
								<div className="typography-line">
									<h2>
										<span>Small Tag</span>
										Header with small subtitle <br></br>
										<small>Use "small" tag for the headers</small>
									</h2>
								</div>
							</Card.Body>
						</Card>
					</Col>
				</Row>
			</Container>
		</>
	);
}

export default Typography;


--#

--% /react-light/src/views/Upgrade.js
import React from "react";

// react-bootstrap components
import {
	Badge,
	Button,
	Card,
	Navbar,
	Nav,
	Table,
	Container,
	Row,
	Col,
} from "react-bootstrap";

function Upgrade() {
	return (
		<>
			<Container fluid>
				<Row>
					<Col className="ml-auto mr-auto" md="8">
						<Card>
							<div className="header text-center">
								<h4 className="title">Light Bootstrap Dashboard PRO React</h4>
								<p className="category">
									Are you looking for more components? Please check our Premium
									Version of Light Bootstrap Dashboard React.
								</p>
								<br></br>
							</div>
							<Table responsive>
								<thead>
									<tr>
										<th></th>
										<th className="text-center">Free</th>
										<th className="text-center">PRO</th>
									</tr>
								</thead>
								<tbody>
									<tr>
										<td>Components</td>
										<td>16</td>
										<td>115+</td>
									</tr>
									<tr>
										<td>Plugins</td>
										<td>4</td>
										<td>14+</td>
									</tr>
									<tr>
										<td>Example Pages</td>
										<td>4</td>
										<td>22+</td>
									</tr>
									<tr>
										<td>Documentation</td>
										<td>
											<i className="fas fa-times text-danger"></i>
										</td>
										<td>
											<i className="fas fa-check text-success"></i>
										</td>
									</tr>
									<tr>
										<td>SASS Files</td>
										<td>
											<i className="fas fa-times text-danger"></i>
										</td>
										<td>
											<i className="fas fa-check text-success"></i>
										</td>
									</tr>
									<tr>
										<td>Login/Register/Lock Pages</td>
										<td>
											<i className="fas fa-times text-danger"></i>
										</td>
										<td>
											<i className="fas fa-check text-success"></i>
										</td>
									</tr>
									<tr>
										<td>Premium Support</td>
										<td>
											<i className="fas fa-times text-danger"></i>
										</td>
										<td>
											<i className="fas fa-check text-success"></i>
										</td>
									</tr>
									<tr>
										<td></td>
										<td>Free</td>
										<td>Just $49</td>
									</tr>
									<tr className="last-row">
										<td></td>
										<td>
											<Button
												className="btn-round btn-fill disabled"
												href="#pablo"
												onClick={(e) => e.preventDefault()}
												variant="default"
											>
												Current Version
											</Button>
										</td>
										<td>
											<Button
												className="btn-round btn-fill"
												href="http://www.creative-tim.com/product/light-bootstrap-dashboard-pro-react/?ref=lbdrupgrade"
												target="_blank"
												variant="info"
											>
												Upgrade to PRO
											</Button>
										</td>
									</tr>
								</tbody>
							</Table>
						</Card>
					</Col>
				</Row>
			</Container>
		</>
	);
}

export default Upgrade;


--#

--% /react-light/src/views/UserProfile.js
import React from "react";

// react-bootstrap components
import {
	Badge,
	Button,
	Card,
	Form,
	Navbar,
	Nav,
	Container,
	Row,
	Col,
} from "react-bootstrap";

function User() {
	return (
		<>
			<Container fluid>
				<Row>
					<Col md="8">
						<Card>
							<Card.Header>
								<Card.Title as="h4">Edit Profile</Card.Title>
							</Card.Header>
							<Card.Body>
								<Form>
									<Row>
										<Col className="pr-1" md="5">
											<Form.Group>
												<label>Company (disabled)</label>
												<Form.Control
													defaultValue="Creative Code Inc."
													disabled
													placeholder="Company"
													type="text"
												></Form.Control>
											</Form.Group>
										</Col>
										<Col className="px-1" md="3">
											<Form.Group>
												<label>Username</label>
												<Form.Control
													defaultValue="michael23"
													placeholder="Username"
													type="text"
												></Form.Control>
											</Form.Group>
										</Col>
										<Col className="pl-1" md="4">
											<Form.Group>
												<label htmlFor="exampleInputEmail1">
													Email address
												</label>
												<Form.Control
													placeholder="Email"
													type="email"
												></Form.Control>
											</Form.Group>
										</Col>
									</Row>
									<Row>
										<Col className="pr-1" md="6">
											<Form.Group>
												<label>First Name</label>
												<Form.Control
													defaultValue="Mike"
													placeholder="Company"
													type="text"
												></Form.Control>
											</Form.Group>
										</Col>
										<Col className="pl-1" md="6">
											<Form.Group>
												<label>Last Name</label>
												<Form.Control
													defaultValue="Andrew"
													placeholder="Last Name"
													type="text"
												></Form.Control>
											</Form.Group>
										</Col>
									</Row>
									<Row>
										<Col md="12">
											<Form.Group>
												<label>Address</label>
												<Form.Control
													defaultValue="Bld Mihail Kogalniceanu, nr. 8 Bl 1, Sc 1, Ap 09"
													placeholder="Home Address"
													type="text"
												></Form.Control>
											</Form.Group>
										</Col>
									</Row>
									<Row>
										<Col className="pr-1" md="4">
											<Form.Group>
												<label>City</label>
												<Form.Control
													defaultValue="Mike"
													placeholder="City"
													type="text"
												></Form.Control>
											</Form.Group>
										</Col>
										<Col className="px-1" md="4">
											<Form.Group>
												<label>Country</label>
												<Form.Control
													defaultValue="Andrew"
													placeholder="Country"
													type="text"
												></Form.Control>
											</Form.Group>
										</Col>
										<Col className="pl-1" md="4">
											<Form.Group>
												<label>Postal Code</label>
												<Form.Control
													placeholder="ZIP Code"
													type="number"
												></Form.Control>
											</Form.Group>
										</Col>
									</Row>
									<Row>
										<Col md="12">
											<Form.Group>
												<label>About Me</label>
												<Form.Control
													cols="80"
													defaultValue="Lamborghini Mercy, Your chick she so thirsty, I'm in
													that two seat Lambo."
													placeholder="Here can be your description"
													rows="4"
													as="textarea"
												></Form.Control>
											</Form.Group>
										</Col>
									</Row>
									<Button
										className="btn-fill pull-right"
										type="submit"
										variant="info"
									>
										Update Profile
									</Button>
									<div className="clearfix"></div>
								</Form>
							</Card.Body>
						</Card>
					</Col>
					<Col md="4">
						<Card className="card-user">
							<div className="card-image">
								<img
									alt="..."
									src={
										require("assets/img/photo-1431578500526-4d9613015464.jpeg")
											.default
									}
								></img>
							</div>
							<Card.Body>
								<div className="author">
									<a href="#pablo" onClick={(e) => e.preventDefault()}>
										<img
											alt="..."
											className="avatar border-gray"
											src={require("assets/img/faces/face-3.jpg").default}
										></img>
										<h5 className="title">Mike Andrew</h5>
									</a>
									<p className="description">michael24</p>
								</div>
								<p className="description text-center">
									"Lamborghini Mercy <br></br>
									Your chick she so thirsty <br></br>
									I'm in that two seat Lambo"
								</p>
							</Card.Body>
							<hr></hr>
							<div className="button-container mr-auto ml-auto">
								<Button
									className="btn-simple btn-icon"
									href="#pablo"
									onClick={(e) => e.preventDefault()}
									variant="link"
								>
									<i className="fab fa-facebook-square"></i>
								</Button>
								<Button
									className="btn-simple btn-icon"
									href="#pablo"
									onClick={(e) => e.preventDefault()}
									variant="link"
								>
									<i className="fab fa-twitter"></i>
								</Button>
								<Button
									className="btn-simple btn-icon"
									href="#pablo"
									onClick={(e) => e.preventDefault()}
									variant="link"
								>
									<i className="fab fa-google-plus-square"></i>
								</Button>
							</div>
						</Card>
					</Col>
				</Row>
			</Container>
		</>
	);
}

export default User;
--#
