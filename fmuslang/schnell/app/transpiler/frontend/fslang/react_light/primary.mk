--% index/fmus
.,d
	.env,f(e=__FILE__=.env)
	jsconfig.json,f(e=__FILE__=jsconfig.json)
	package.json,f(e=__FILE__=package.json)
	src,d(/mk)
		assets,d(/mk)
		components,d(/mk)
		layouts,d(/mk)
		views,d(/mk)
		index.js,f(e=__FILE__=index.js)
		routes.js,f(e=__FILE__=routes.js)
	public,d(/mk)
		apple-icon.png,f(b64=__FILE__=apple-icon.png)
		favicon.ico,f(b64=__FILE__=favicon.ico)
		manifest.json,f(e=__FILE__=manifest.json)
		index.html,f(e=__FILE__=public/index.html)
--#

--% .env
SKIP_PREFLIGHT_CHECK=true
CHOKIDAR_USEPOLLING=true
--#

--% jsconfig.json
{
  "compilerOptions": {
    "baseUrl": "src",
    "paths": {
      "*": ["src/*"]
    }
  }
}
--#

--% package.json
{
  "name": "frontend-light",
  "version": "0.0.1",
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
