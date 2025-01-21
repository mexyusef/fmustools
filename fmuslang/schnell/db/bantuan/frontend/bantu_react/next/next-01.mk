--% index/fm.us
__TEMPLATE_PROJECT_DIR__,d
  %utama=__FILE__
  %__TEMPLATE_SERVER_PORT__=9502
  __TEMPLATE_WEBPACK_NAME__.js,f(e=utama=/webpack.js)
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

--% /yarn.add.sh
yarn add @ant-design/icons @ant-design/react-native @esri/react-arcgis @fullpage/react-fullpage @material-ui/core @material-ui/icons @react-native-community/cli add antd axios bizcharts bootstrap docx draft-js echarts echarts-for-react eslint-plugin-react-native esri-loader express-formidable express-sanitizer firebase font-awesome highcharts highcharts-react-official jointjs jquery js-file-download jspdf jspdf-autotable jsreport jsreport-client jsreport-html-to-text jwt-decode leaflet leaflet-geosearch leaflet-search leaflet.locatecontrol localforage localforage-getitems multer mustache node-fetch parsimmon pubsub-js react react-beautiful-dnd react-csv react-dom react-html-table-to-excel react-image react-leaflet react-navigation react-otp-input react-redux react-router react-router-dom react-router-redux react-trello reactstrap redocx redux redux-saga redux-thunk saga socket.io socket.io-client thunk uid-generator

yarn add --dev @babel/core @babel/plugin-proposal-class-properties @babel/plugin-proposal-decorators @babel/plugin-syntax-dynamic-import @babel/preset-env @babel/preset-flow @babel/preset-react @react-native-community/eslint-config @types/react @types/react-native babel-jest babel-loader babel-plugin-import babel-plugin-module-resolver babel-polyfill bcrypt clean-webpack-plugin compression-webpack-plugin copy-webpack-plugin cors cross-env css-loader dotenv express-fileupload express-session express-upload file-loader helmet html-loader html-webpack-plugin imports-loader jest jsonwebtoken less less-loader metro-react-native-babel-preset mini-css-extract-plugin morgan nodemon pg pg-hstore pre-commit prettier rand-token react-hot-loader react-test-renderer redux-devtools-extension sequelize sequelize-auto source-map-loader style-loader ts-loader typescript url-loader webpack webpack-cli webpack-dev-server webpack-merge workbox-webpack-plugin
--#

--% /run.sh
./node_modules/.bin/webpack serve --mode development --config __TEMPLATE_WEBPACK_NAME__
--#
