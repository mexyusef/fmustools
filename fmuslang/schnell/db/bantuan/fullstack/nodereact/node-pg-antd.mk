--% program/fm.us
__REPLACE_WITH_PROJECT_DIR_OR_INPUT__,d(/mk)
  %utama=__FILE__
  %__TEMPLATE_SERVER_HOST=localhost
__TEMPLATE_DB_INIT
__TEMPLATE_APP_INIT
  package.json,f(e=utama=/np/package.json)
  .env,f(e=utama=/np/.env)
  webpack-antd.js,f(e=utama=/np/webpack-antd.js)
  webpack-node-pg.js,f(e=utama=/np/webpack-node-pg.js)
  node-postgres,d(/mk)
    .gitignore,f(e=utama=/np/node-postgres/.gitignore)
    .eslintrc.js,f(e=utama=/np/node-postgres/.eslintrc.js)
    README.md,f(e=utama=/np/node-postgres/README.md)
    .babelrc,f(e=utama=/np/node-postgres/.babelrc)
    src,d(/mk)
      config.js,f(e=utama=/np/node-postgres/src/config.js)
      public,d(/mk)
      core,d(/mk)
        crud-mongoose.js,f(e=utama=/np/node-postgres/src/core/crud-mongoose.js)
        extender.js,f(e=utama=/np/node-postgres/src/core/extender.js)
        crud.js,f(e=utama=/np/node-postgres/src/core/crud.js)
        app.js,f(e=utama=/np/node-postgres/src/core/app.js)
        routes,d(/mk)
          index.js,f(e=utama=/np/node-postgres/src/core/routes/index.js)
          extension,d(/mk)
            index.js,f(e=utama=/np/node-postgres/src/core/routes/extension/index.js)
          dummy,d(/mk)
            index.js,f(e=utama=/np/node-postgres/src/core/routes/dummy/index.js)
          api,d(/mk)
            users.js,f(e=utama=/np/node-postgres/src/core/routes/api/users.js)
            index.js,f(e=utama=/np/node-postgres/src/core/routes/api/index.js)
            auth.js,f(e=utama=/np/node-postgres/src/core/routes/api/auth.js)
          generic,d(/mk)
            index.js,f(e=utama=/np/node-postgres/src/core/routes/generic/index.js)
        middlewares,d(/mk)
          cors.js,f(e=utama=/np/node-postgres/src/core/middlewares/cors.js)
          index.js,f(e=utama=/np/node-postgres/src/core/middlewares/index.js)
          session.js,f(e=utama=/np/node-postgres/src/core/middlewares/session.js)
          body.js,f(e=utama=/np/node-postgres/src/core/middlewares/body.js)
          uploader.js,f(e=utama=/np/node-postgres/src/core/middlewares/uploader.js)
          morgan.js,f(e=utama=/np/node-postgres/src/core/middlewares/morgan.js)
        utils,d(/mk)
        db,d(/mk)
          mongo.js,f(e=utama=/np/node-postgres/src/core/db/mongo.js)
          postgres.js,f(e=utama=/np/node-postgres/src/core/db/postgres.js)
          index.js,f(e=utama=/np/node-postgres/src/core/db/index.js)
      apps,d(/mk)
        index.js,f(e=utama=/np/node-postgres/src/apps/index.js/hasil_creation)
        user,d(/mk)
          # user_extender.js,f(e=utama=/np/node-postgres/src/apps/user/extender.js)
          models,d(/mk)
            mongo.js,f(e=utama=/np/node-postgres/src/apps/user/models/mongo.js)
            postgres.js,f(e=utama=/np/node-postgres/src/apps/user/models/postgres.js)
            index.js,f(e=utama=/np/node-postgres/src/apps/user/models/index.js)
          auth,d(/mk)
            index.js,f(e=utama=/np/node-postgres/src/apps/user/auth/index.js)
            token.js,f(e=utama=/np/node-postgres/src/apps/user/auth/token.js)
            token_mongo.js,f(e=utama=/np/node-postgres/src/apps/user/auth/token_mongo.js)
            provider.js,f(e=utama=/np/node-postgres/src/apps/user/auth/provider.js)
            kripto.js,f(e=utama=/np/node-postgres/src/apps/user/auth/kripto.js)
            jwt.js,f(e=utama=/np/node-postgres/src/apps/user/auth/jwt.js)
__TEMPLATE_SERVER_APP_CONTENT
        user,d(/mk)
          extender.js,f(e=utama=/np/node-postgres/src/apps/user/extender.js)
      server,d(/mk)
        server-dev.js,f(e=utama=/np/node-postgres/src/server/server-dev.js)
        server-prod.js,f(e=utama=/np/node-postgres/src/server/server-prod.js)
    __mocks__,d(/mk)
      styleMock.js,f(e=utama=/np/node-postgres/__mocks__/styleMock.js)
      fileMock.js,f(e=utama=/np/node-postgres/__mocks__/fileMock.js)
  react-antd,d(/mk)
    index.html,f(e=utama=/np/react-antd/index.html)
    .env,f(e=utama=/np/react-antd/.env)
    .eslintrc.js,f(e=utama=/np/react-antd/.eslintrc.js)
    index.js,f(e=utama=/np/react-antd/index.js)
    .babelrc,f(e=utama=/np/react-antd/.babelrc)
    config.js,f(e=utama=/np/react-antd/config.js)
    index.css,f(e=utama=/np/react-antd/index.css)
    assets,d(/mk)
__TEMPLATE_CLIENT_JSON_MODEL
      menu.json,f(e=utama=/np/react-antd/assets/menu.json)
      favicon.ico,f(b64=utama=/np/react-antd/assets/favicon.ico)
    components,d(/mk)
      Setting,d(/mk)
        Settings_Popup.js,f(e=utama=/np/react-antd/components/Setting/Settings_Popup.js)
      modules,d(/mk)
__TEMPLATE_CLIENT_APP_CONTENT
        Dashboard,d(/mk)
          Dashboard.js,f(e=utama=/np/react-antd/components/modules/Dashboard/Dashboard.js)
      Layout,d(/mk)
        BaseLayout.css,f(e=utama=/np/react-antd/components/Layout/BaseLayout.css)
        BaseLayout.js,f(e=utama=/np/react-antd/components/Layout/BaseLayout.js)
        Header,d(/mk)
          index.js,f(e=utama=/np/react-antd/components/Layout/Header/index.js)
          style.css,f(e=utama=/np/react-antd/components/Layout/Header/style.css)
        Sidebar,d(/mk)
          index.js,f(e=utama=/np/react-antd/components/Layout/Sidebar/index.js)
          style.css,f(e=utama=/np/react-antd/components/Layout/Sidebar/style.css)
        Floating,d(/mk)
          index.js,f(e=utama=/np/react-antd/components/Layout/Floating/index.js)
          style.css,f(e=utama=/np/react-antd/components/Layout/Floating/style.css)
        Footer,d(/mk)
      App,d(/mk)
        index.js,f(e=utama=/np/react-antd/components/App/index.js)
        style.css,f(e=utama=/np/react-antd/components/App/style.css)
      common,d(/mk)
        TabPage,d(/mk)
          index.js,f(e=utama=/np/react-antd/components/common/TabPage/index.js)
          style.css,f(e=utama=/np/react-antd/components/common/TabPage/style.css)
        BoModule,d(/mk)
          BoModule.css,f(e=utama=/np/react-antd/components/common/BoModule/BoModule.css)
          BoModule.js,f(e=utama=/np/react-antd/components/common/BoModule/BoModule.js)
        Table,d(/mk)
          SimpleTable.js,f(e=utama=/np/react-antd/components/common/Table/SimpleTable.js)
      context,d(/mk)
        ToolbarContext.js,f(e=utama=/np/react-antd/components/context/ToolbarContext.js)
        SessionProvider.js,f(e=utama=/np/react-antd/components/context/SessionProvider.js)
        SessionContext.js,f(e=utama=/np/react-antd/components/context/SessionContext.js)
      Route,d(/mk)
        AuthenticatedRoute.js,f(e=utama=/np/react-antd/components/Route/AuthenticatedRoute.js)
        Routes.js,f(e=utama=/np/react-antd/components/Route/Routes.js)
      Menu,d(/mk)
        Shortcut.js,f(e=utama=/np/react-antd/components/Menu/Shortcut.js)
        index.js,f(e=utama=/np/react-antd/components/Menu/index.js)
        MainMenu.js,f(e=utama=/np/react-antd/components/Menu/MainMenu.js)
        MainMenu.css,f(e=utama=/np/react-antd/components/Menu/MainMenu.css)
      Login,d(/mk)
        login.css,f(e=utama=/np/react-antd/components/Login/login.css)
        index.js,f(e=utama=/np/react-antd/components/Login/index.js)
    utils,d(/mk)
      useAxios.js,f(e=utama=/np/react-antd/utils/useAxios.js)
  $*qterminal 2>/dev/null &
  &*showtext=__FILE__=/np/node-postgres/README.md
--#

--% /np/node-postgres/README.md
TODO:

0) yarn add sequelize sequelize-cli
1)
npx sequelize init
config/config.json:
{
  "development": {
    "username": "usef",
    "password": "rahasia",
    "database": "hapuslah",
    "host": "gisel.ddns.net",
    "port": 9022,
    "dialect": "postgresql"
  },
  "test": {
    "username": "usef",
    "password": "rahasia",
    "database": "hapuslah",
    "host": "gisel.ddns.net",
    "port": 9022,
    "dialect": "postgresql"
  },
  "production": {
    "username": "usef",
    "password": "rahasia",
    "database": "hapuslah",
    "host": "gisel.ddns.net",
    "port": 9022,
    "dialect": "postgresql"
  }
}

2)
npx sequelize-cli seed:generate --name <nama model sesuai nama database biar enak>
npx sequelize-cli seed:generate --name __NAMATABLE__

3)
gunakan:
createdAt: new Date(),
updatedAt: new Date()

modify dg content:
'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.bulkInsert(
      '__NAMATABLE__', 
      [
        {
          name: 'John Doe',
          rating: 2,
          comment: 'sebuah text comment',
        },
      ],
      {}
    );
  },
  down: async (queryInterface, Sequelize) => {
  }
};
4) run migration
npx sequelize-cli db:seed:all

# create table manual
docker exec -it pg psql -U usef insurance_development -c "create table insurances(id serial primary key,coverage varchar(255),government boolean);"
# select/check table
docker exec -it pg psql -U usef insurance_development -c "select * from insurances;"
docker exec -it pg psql -U usef insurance_development -c "SELECT id, coverage, government FROM insurances AS insurances;"


switching postgres <-> mongo

  apps/index.js
    comment out "khusus mongo"

  apps/user/models/index.js
    ganti import

  apps/task/models/index.js
    ganti import

  core/db/index.js
    ganti import

  core/routes/generic/index.js
    ganti import
      import Cruder from 'C/crud';
      // import Cruder from 'C/crud-mongoose';

  apps/user/auth/jwt.js
    ganti import
      import Token from './token';
      // import Token from './token_mongo';

  apps/user/auth/provider
    mungkin logic nya hrs diubah, ngikutin node ecommerce???

--#

--% /np/package.json
{
  "name": "np",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "scripts": {
    "test": "jest",
    "coverage": "jest --coverage",

    "antd": "webpack serve --mode development --config webpack-antd",
    "client": "webpack serve --mode development --config webpack-antd",

    "buildServer": "rm -rf dist && webpack --mode development --config webpack-node-pg",
    "server": "npm run buildServer && npm run start",
    "mulai": "npm run buildServer && npm run start",
    "go": "npm run buildServer && npm run start",
    "start": "node ./dist/server.js"
  },
  "dependencies": {
    "antd": "^4.15.5",
    "axios": "^0.21.1",
    "bcrypt": "^5.0.1",
    "express": "^4.17.1",
    "font-awesome": "^4.7.0",
    "jsonwebtoken": "^8.5.1",
    "mongoose": "^5.12.9",
    "mongoose-unique-validator": "^2.0.3",
    "pg": "^8.6.0",
    "pg-hstore": "^2.3.3",
    "pubsub-js": "^1.9.3",
    "rand-token": "^1.0.1",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-hot-loader": "^4.13.0",
    "react-router-dom": "^5.2.0",		
    "uid-generator": "^2.0.0"
  },
  "devDependencies": {
    "@babel/core": "^7.14.2",
    "@babel/plugin-proposal-class-properties": "^7.13.0",
    "@babel/plugin-transform-runtime": "^7.14.2",
    "@babel/preset-env": "^7.14.2",
    "@babel/preset-react": "^7.13.13",
    "@babel/runtime": "^7.14.0",
    "@webpack-cli/serve": "^1.4.0",
    "babel-core": "^6.26.3",
    "babel-eslint": "^10.1.0",
    "babel-jest": "^26.6.3",
    "babel-loader": "^8.2.2",
    "babel-plugin-transform-runtime": "^6.23.0",
    "babel-polyfill": "^6.26.0",
    "cors": "^2.8.5",
    "css-loader": "^5.2.4",
    "dotenv": "^9.0.2",
    "dotenv-webpack": "^7.0.2",
    "eslint": "^7.26.0",
    "eslint-loader": "^4.0.2",
    "express-fileupload": "^1.2.1",
    "express-session": "^1.17.1",
    "file-loader": "^6.2.0",
    "fs": "^0.0.1-security",
    "helmet": "^4.6.0",
    "html-loader": "^2.1.2",
    "html-webpack-plugin": "^5.3.1",
    "jest": "^26.6.3",
    "mini-css-extract-plugin": "^1.6.0",
    "morgan": "^1.10.0",
    "optimize-css-assets-webpack-plugin": "^5.0.4",
    "sequelize": "^6.6.2",
    "sequelize-cli": "^6.2.0",
    "style-loader": "^2.0.0",
    "uglifyjs-webpack-plugin": "^2.2.0",
    "url-loader": "^4.1.1",
    "webpack": "^5.37.0",
    "webpack-cli": "^4.7.0",
    "webpack-dev-middleware": "^4.2.0",
    "webpack-dev-server": "^3.11.2",
    "webpack-hot-middleware": "^2.25.0",
    "webpack-node-externals": "^3.0.0"
  }
}
--#

--% /np/.env
HOST=localhost
PORT=9101

#mongo or postgres
DB_CHOICE=postgres
DB_SCHEMA=public
DB_SYNC=1

SESSION_SECRET=K1nG.5up3rM4rk3t!
JWT_SECRET=Qu33n.5up3rM4rk3t!
NODE_ENV=development

MONGO_DB=__TEMPLATE_DBNAME
MONGO_HOST=__TEMPLATE_DBHOST
MONGO_PORT=__TEMPLATE_DBPORT
MONGO_USER=__TEMPLATE_DBUSER
MONGO_PASS=__TEMPLATE_DBPASS

POSTGRES_DB=__TEMPLATE_DBNAME
POSTGRES_USER=__TEMPLATE_DBUSER
POSTGRES_PASS=__TEMPLATE_DBPASS
POSTGRES_HOST=__TEMPLATE_DBHOST
POSTGRES_PORT=__TEMPLATE_DBPORT
--#

--% /np/webpack-antd.js
const path = require('path');
const webpack = require('webpack');
const HtmlWebPackPlugin = require('html-webpack-plugin');
// const Dotenv = require('dotenv-webpack');

const sourcedir = 'react-antd'

module.exports = {
  entry: {
    main: [
      // 'babel-polyfill',
      // 'webpack-hot-middleware/client?path=/__webpack_hmr&timeout=20000', 
      // './src/index.js',
      `./${sourcedir}/index.js`
    ]
  },
  output: {
    path: path.join(__dirname, 'dist'),
    publicPath: '/',
    filename: '[name].js'
  },

  mode: 'development',
  // https://stackoverflow.com/questions/51946848/webpack-nodejs-module-not-found-error-cant-resolve-fs
  target: 'web',
  // target: 'node',

  // configuration.devtool should match pattern "^(inline-|hidden-|eval-)?(nosources-)?(cheap-(module-)?)?source-map$"
  // devtool: '#source-map',

  devServer: {
    contentBase: path.resolve(process.cwd(), 'dist'),
    hot: true,
    port: 9001,
    historyApiFallback: true,
  },

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
}

--#

--% /np/webpack-node-pg.js

const path = require('path');
const webpack = require('webpack');
const nodeExternals = require('webpack-node-externals');


const sourcedir = 'node-postgres/src'

module.exports = (env = undefined, argv = {mode: 'development'}) => {
  const SERVER_PATH = (argv.mode === 'production') ?
    `./${sourcedir}/server/server-prod.js` :
    `./${sourcedir}/server/server-dev.js`

  return ({
    entry: {
      server: SERVER_PATH,
    },
    output: {
      path: path.join(__dirname, 'dist'),
      publicPath: '/',
      filename: '[name].js'
    },
    mode: argv.mode,

    target: 'node',

    node: {
      // Need this when working with express, otherwise the build fails
      __dirname: false,   // if you don't put this is, __dirname
      __filename: false,  // and __filename return blank or /
    },
    externals: [nodeExternals()], // Need this to avoid error when working with Express

    resolve: {
      modules: [sourcedir, 'node_modules'],
      extensions: ['.js'],
      alias: {
        S: path.resolve(process.cwd(), sourcedir),
        C: path.resolve(process.cwd(), sourcedir, 'core'),
        A: path.resolve(process.cwd(), sourcedir, 'apps'),
        AU: path.resolve(process.cwd(), sourcedir, 'apps/user'),
        D: path.resolve(process.cwd(), sourcedir, 'core/db'),
        M: path.resolve(process.cwd(), sourcedir, 'core/middlewares'),
        R: path.resolve(process.cwd(), sourcedir, 'core/routes'),
        U: path.resolve(process.cwd(), sourcedir, 'core/utils'),
      },
    },

    module: {
      rules: [
        // {
        //   enforce: "pre",
        //   test: /\.js$/,
        //   exclude: /node_modules/,
        //   loader: "eslint-loader",
        //   options: {
        //     emitWarning: true,
        //     failOnError: false,
        //     failOnWarning: false
        //   }
        // },
        {
          // Transpiles ES6-8 into ES5
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader"
          }
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
         test: /\.(png|svg|jpg|gif)$/,
         use: ['file-loader']
        }
      ]
    },

    plugins: [
      new webpack.HotModuleReplacementPlugin(),
      new webpack.NoEmitOnErrorsPlugin()
    ],

  })
}


--#

--% /np/node-postgres/.gitignore
node_modules
.DS_Store
dist

Coverage
coverage

--#

--% /np/node-postgres/.eslintrc.js
module.exports = {
  "extends": [
    "eslint:recommended",
  ],
  "parser": "babel-eslint",
  "rules": {
    "no-unused-vars": "off",
    "no-undef": "off",
    "no-console": "off",
    "no-empty": "off",
  }
};


--#

--% /np/node-postgres/.babelrc
{
  "presets": [
    "@babel/preset-env"
  ],
  "plugins": [
    ["@babel/transform-runtime"]
  ]
}

--#

--% /np/node-postgres/src/config.js
module.exports = {
  secret: process.env.NODE_ENV === 'production' 
  ? process.env.JWT_SECRET 
  : 'jangan tatap mataku'
};



--#

--% /np/node-postgres/src/core/crud-mongoose.js
export default function(Model) {
  return {

    create: async ({body}, res, _) => {
      try {
        console.log(`crud create: start body: ${JSON.stringify(body)}`);
        const object = Model.build(body);
        const data = await object.save();
        return res.json(data);
      } catch(err) {
        console.log(`crud create: error ${err}, data: ${JSON.stringify(body)}.`);
        return res.status(422).json({ 
          message: 'Invalid request', 
          error: err,
          data: body
        });
      }
    },

    all: async (req, res)  => {
      try {
        // const options = {
        //   order: [ ['id', 'DESC'] ],
        // }
        // const data = await Model.findAll(options);
        const data = await Model.find({}).exec();
        const total = await Model.countDocuments().exec();
        return res.json({
          result: data,
          total,
        });
      } catch(err) {
        console.log(`CRUD/read/list error: [${err}]`);
      }
    },

    read: async ({params: {id}}, res)  => {
      try {
        const options = {
          where: {id}
        }
        const data = await Model.findOne(options);
        return res.json(data);
      } catch(err) {
      }
    },

    update: async ({body, params: {id}}, res, next)  => {
      try {
        const options = {
          where: {id}
        }
        const data = await Model.update(body, options);
        return res.json(data);
      } catch(err) {
        console.log(`crud update: error ${err}, data: ${JSON.stringify(body)}, id: ${id}`);
        return res.status(422).json({ 
          message: 'Invalid request',
          error: err,
          data: body 
        });
      }
    },

    destroy: async ({params: {id}}, res, next) => {
      try {
        const options = {
          where: {id}
        }
        const data = await Model.destroy(options);
        return res.json(data);
      } catch(err) {
        next(err);
      }
    },
    
  }

}


--#

--% /np/node-postgres/src/core/extender.js
// module.exports = () => ({
export default () => ({
  getFunc1: async(req, res, next) => res.json({
    'message': 'get-func1',
  }),
  
  getFunc2: async(req, res, next) => res.json({
    'message': 'get-func2',
  }),
  
  postFunc1: async(req, res, next) => res.json({
    'message': 'post-func1',
  }),

  postFunc2: async(req, res, next) => res.json({
    'message': 'post-func2',
  }),
});



--#

--% /np/node-postgres/src/core/crud.js
import { default as dbConnect } from 'D';
import Enkripsi from 'AU/auth';

export default function(Model) {
  return {
    create: async ({body}, res, _) => {
      try {
        console.log(`crud create: start body: ${JSON.stringify(body)}`);

        if (Model === dbConnect.models.users && body.hasOwnProperty('password')) {
          const encrypted = await Enkripsi.encrypt(body.password);
          console.log(`\n   *** changing pass from ${body.password} to ${encrypted}\n`);
          body.password = encrypted;
        }

        const object = Model.build(body);
        const data = await object.save();
        return res.json(data);
      } catch(err) {
        console.log(`crud create: error ${err}, data: ${JSON.stringify(body)}.`);
        return res.status(422).json({ 
          message: 'Invalid request', 
          error: err,
          data: body
        });
      }
    },
    all: async (req, res)  => {
      try {
        // const options = {
        //   order: [ ['id', 'DESC'] ],
        // }
        // const data = await Model.findAll(options);
        const data = await Model.findAll();
        const total = await Model.count();
        return res.json({
          result: data,
          total,
        });
      } catch(err) {
      }
    },
    read: async ({params: {id}}, res)  => {
      try {
        const options = {
          where: {id}
        }
        const data = await Model.findOne(options);
        return res.json(data);
      } catch(err) {
      }
    },
    update: async ({body, params: {id}}, res, next)  => {
      try {
        const options = {
          where: {id}
        }
        const data = await Model.update(body, options);
        return res.json(data);
      } catch(err) {
        console.log(`crud update: error ${err}, data: ${JSON.stringify(body)}, id: ${id}`);
        return res.status(422).json({ 
          message: 'Invalid request',
          error: err,
          data: body 
        });
      }
    },
    destroy: async ({params: {id}}, res, next) => {
      try {
        const options = {
          where: {id}
        }
        const data = await Model.destroy(options);
        return res.json(data);
      } catch(err) {
        next(err);
      }
    },
  }
}

--#

--% /np/node-postgres/src/core/app.js
// const express = require('express');
import express from 'express';
// import { setModel } from 'D';
import { devMiddlewares } from 'M';
import routes from 'R';
function setupApp(app) {
  app.use(express.json());
  app.use('/static', express.static('public'));

  // const { setModel } = require('D');
  // setModel(app);

  app.get('/', (_, res) => res.send(`dari dalam setupApp dg resolve!`));

  // const { devMiddlewares } = require('M');
  devMiddlewares(app);

  // app.use(require('R'));
  app.use(routes);
}

// module.exports = (app) => {
//   setupApp(app);
// }
const App = (app) => setupApp(app);
export default App;


--#

--% /np/node-postgres/src/core/routes/index.js
const express = require('express');
import GenericRouter from './generic';
// import DummyRouter from './dummy';
// import ExtensionRouter from './extension';
import AppModels from 'A';

const router = express.Router();

// server:port/model      GET
// server:port/model/:id  GET
// server:port/model      POST
// server:port/model/:id  PATCH
// server:port/model/:id  DELETE
router.use('/', GenericRouter(express));

AppModels.extenders.forEach(Extender => {
  // console.log(`jenis data extender adlh: ${typeof(Extender)}`);
  // router.use('/', Extender(router));
  router.use('/', Extender(new express.Router()));
});

// const helloRouter = require('./dummy')(express);
// console.log(`pake dummy`);
// const helloRouter = DummyRouter(express);
// router.use('/', helloRouter);

// router.use('/ext', require('./extension')(helloRouter));
// router.use('/ext', ExtensionRouter(helloRouter));

export default router;



--#

--% /np/node-postgres/src/core/routes/extension/index.js
// const Extender = require('C/extender')();
import Extender from 'C/extender';
const ExtenderObj = Extender();

const ExtensionRouter = Router => Router

  .get('/func1', ExtenderObj.getFunc1)
  .post('/func1', ExtenderObj.postFunc1)

  .get('/func2', ExtenderObj.getFunc2)
  .post('/func2', ExtenderObj.postFunc2);

// module.exports = RouterExtender;
export default ExtensionRouter;



--#

--% /np/node-postgres/src/core/routes/dummy/index.js
const waktu = new Date();

const greetingService = (req, res) => res.json({
  'status'		: 'ok',
  'day'				: waktu.toLocaleDateString(),
  'time'			: waktu.toLocaleTimeString(),
  'message'		: `Hello, ${req.params.name || "World"}!`,
});

// module.exports = (express) => express
const DummyRouter = (express) => express
  .Router()
  .get('/hello', greetingService)
  .get('/hello/:name', greetingService);

export default DummyRouter;


--#

--% /np/node-postgres/src/core/routes/api/users.js
var mongoose = require('mongoose');
var router = require('express').Router();
var passport = require('passport');
var User = mongoose.model('User');
var auth = require('./auth');

router.get('/user', auth.required, function(req, res, next){
  User.findById(req.payload.id).then(function(user){
    if(!user){ return res.sendStatus(401); }

    return res.json({user: user.toAuthJSON()});
  }).catch(next);
});

router.put('/user', auth.required, function(req, res, next){
  User.findById(req.payload.id).then(function(user){
    if(!user){ return res.sendStatus(401); }

    // only update fields that were actually passed...
    if(typeof req.body.user.username !== 'undefined'){
      user.username = req.body.user.username;
    }
    if(typeof req.body.user.email !== 'undefined'){
      user.email = req.body.user.email;
    }
    if(typeof req.body.user.bio !== 'undefined'){
      user.bio = req.body.user.bio;
    }
    if(typeof req.body.user.image !== 'undefined'){
      user.image = req.body.user.image;
    }
    if(typeof req.body.user.password !== 'undefined'){
      user.setPassword(req.body.user.password);
    }

    return user.save().then(function(){
      return res.json({user: user.toAuthJSON()});
    });
  }).catch(next);
});

router.post('/users/login', function(req, res, next){
  if(!req.body.user.email){
    return res.status(422).json({errors: {email: "can't be blank"}});
  }

  if(!req.body.user.password){
    return res.status(422).json({errors: {password: "can't be blank"}});
  }

  passport.authenticate('local', {session: false}, function(err, user, info){
    if(err){ return next(err); }

    if(user){
      user.token = user.generateJWT();
      return res.json({user: user.toAuthJSON()});
    } else {
      return res.status(422).json(info);
    }
  })(req, res, next);
});

router.post('/users', function(req, res, next){
  var user = new User();

  user.username = req.body.user.username;
  user.email = req.body.user.email;
  user.setPassword(req.body.user.password);

  user.save().then(function(){
    return res.json({user: user.toAuthJSON()});
  }).catch(next);
});

module.exports = router;
--#

--% /np/node-postgres/src/core/routes/api/index.js
const router = require('express').Router();

router.use('/', require('./users'));
// router.use('/profiles', require('./profiles'));
// router.use('/articles', require('./articles'));
// router.use('/tags', require('./tags'));

router.use(function(err, req, res, next){
  if(err.name === 'ValidationError'){
    return res.status(422).json({
      errors: Object.keys(err.errors).reduce(function(errors, key){
        errors[key] = err.errors[key].message;
        return errors;
      }, {})
    });
  }

  return next(err);
});

// module.exports = router;
export default router;



--#

--% /np/node-postgres/src/core/routes/api/auth.js
var jwt = require('express-jwt');
var secret = require('S/config').secret;

function getTokenFromHeader(req){
  if (req.headers.authorization && 
      req.headers.authorization.split(' ')[0] === 'Token' ||
      req.headers.authorization && 
      req.headers.authorization.split(' ')[0] === 'Bearer') {
    return req.headers.authorization.split(' ')[1];
  }

  return null;
}

var auth = {
  required: jwt({
    secret: secret,
    userProperty: 'payload',
    getToken: getTokenFromHeader
  }),
  optional: jwt({
    secret: secret,
    userProperty: 'payload',
    credentialsRequired: false,
    getToken: getTokenFromHeader
  })
};

module.exports = auth;



--#

--% /np/node-postgres/src/core/routes/generic/index.js
import Cruder from 'C/crud';
// import Cruder from 'C/crud-mongoose';

import AppModels from 'A';

const GenericRouter = (express, Controller) => {
  // const router = express.Router();
  // return router;
  return express.Router()	
    .post("/", Controller.create)
    .get("/", Controller.all)
    .get("/:id", Controller.read)
    .patch("/:id", Controller.update)
    .delete("/:id", Controller.destroy)	
}

// module.exports = (express) => {
export default function (express) {
  const router = new express.Router();    
  // router.use(`/task`, GenericRouter(express, Cruder(Task)));
  // router.use(`/user`, GenericRouter(express, Cruder(User)));
  Object.entries(AppModels.base).forEach(([k,v]) => {
    router.use(`/${k}`, GenericRouter(express, Cruder(v)));
  });

  return router;
}



--#

--% /np/node-postgres/src/core/middlewares/cors.js
const cors = require('cors');

const corsMiddleware = (app) => {
  
  if (process.env.NODE_ENV === 'production') {
    app.use(cors({
      // origin: process.env.CORS_ORIGIN.split(','),
      origin: '*',
      methods: process.env.CORS_METHOD.split(','),
      allowedHeaders: process.env.CORS_ALLOWED_HEADERS.split(','),
      exposedHeaders: ['File-Name'],
      maxAge: parseInt(process.env.CORS_MAX_AGE),
      credentials: process.env.CORS_CREDENTIALS === 'true',
    }));
  } else {
    app.use(cors({
      origin: '*',
      exposedHeaders: ['File-Name'],
    }));
  }
}

module.exports = corsMiddleware;


--#

--% /np/node-postgres/src/core/middlewares/index.js
const bodyParserMiddleware = require('./body');
const corsMiddleware = require('./cors');
const fileUploader = require('./uploader');
const morganMiddleware = require('./morgan');
const sessionMiddleware = require('./session');

const devMiddlewares = app => {

  const activeMiddlewares = [
    bodyParserMiddleware,
    corsMiddleware,
    fileUploader,
    // helmetMiddleware,
    morganMiddleware,
    sessionMiddleware,
  ];

  for (let _middleware of activeMiddlewares) {
    _middleware(app);
  }
}

module.exports = {
  devMiddlewares,
};




--#

--% /np/node-postgres/src/core/middlewares/session.js
const session = require('express-session');

// express-session deprecated req.secret; 
// provide secret option backend/node2/middlewares/index.js:50:11
const sessionMiddleware = (app) => {
  
  app.use(session({
    name: app.appName,
    secret: process.env.SESSION_SECRET,
    resave: true,
    saveUninitialized: true,
    rolling: true,
    captcha: null,
    user: null,
    cookie: {
      httpOnly: false,
      secure: false,
      maxAge: 2000000,
    },
  }));
}

module.exports = sessionMiddleware;



--#

--% /np/node-postgres/src/core/middlewares/body.js
const bodyParser = require('body-parser');

const bodyParserMiddleware = (app) => {	
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({
      extended: true
  }));
}

module.exports = bodyParserMiddleware;


--#

--% /np/node-postgres/src/core/middlewares/uploader.js
const fileUpload = require('express-fileupload');

const fileUploader = (app) => {	
  app.use(fileUpload());
}

module.exports = fileUploader;



--#

--% /np/node-postgres/src/core/middlewares/morgan.js
const helmet = require('helmet');
const morgan = require('morgan');

// hidePoweredBy does not take options. Remove the property to silence this warning.
const helmetMiddleware = (app) => {
  
  app.use(helmet({
    hidePoweredBy: {
      setTo: process.env.POWERED_BY,
    },
  }));
}


const morganMiddleware = (app) => {	
  app.use(morgan('dev'));
}

module.exports = morganMiddleware;


--#

--% /np/node-postgres/src/core/db/mongo.js
import mongoose from 'mongoose';

function connectionString(tryCount=1) {
  const dbHost = process.env.MONGO_HOST;

  const user_pass = `${process.env.MONGO_USER}:${process.env.MONGO_PASS}`;
  const host_port = `${dbHost}:${process.env.MONGO_PORT}`;
  const dbName = process.env.MONGO_DB || 'admin';
  
  const connstring = `mongodb://${user_pass}@${host_port}/${dbName}?authSource=admin`;
  console.log(`
    #${tryCount} Mongo Konek ke:
    ${connstring}
  `);
  return connstring;
}

mongoose.set('debug', true);

if (process.env.hasOwnProperty('MONGO_PORT')) {
  mongoose.connect(
    connectionString(),
    { 
      useNewUrlParser: true, 
      useUnifiedTopology: true 
    }
  );
} else {
  // tunggu sampai env populated
  // populating environment variables could take some times
  
  const timeout = 2000;
  console.log(`tunggu selama ${timeout} untuk koneksi ke mongo.`);
  setTimeout(function() {
  
    mongoose.connect(
      connectionString(2),
      { 
        useCreateIndex: true,
        useFindAndModify: false,
        useNewUrlParser: true, 
        useUnifiedTopology: true,
      }
    );

  }, timeout);

}

export default mongoose;

--#

--% /np/node-postgres/src/core/db/postgres.js
import Sequelize from 'sequelize';

// let sequelize;
let sequelize = new Sequelize(`postgres://__TEMPLATE_DBUSER:__TEMPLATE_DBPASS@__TEMPLATE_DBHOST:__TEMPLATE_DBPORT/__TEMPLATE_DBNAME`);

function otentikasi() {

  const dbname = process.env.POSTGRES_DB;
  const dbuser = process.env.POSTGRES_USER;
  const dbpass = process.env.POSTGRES_PASS;
  const dbhost = process.env.POSTGRES_HOST;
  const dbport = process.env.POSTGRES_PORT;
  
  const connstring = `postgres://${dbuser}:${dbpass}@${dbhost}:${dbport}/${dbname}`;
  
  sequelize = new Sequelize(connstring);
  // const sequelize = new Sequelize(`postgres://${process.env.POSTGRES_USER}:${process.env.POSTGRES_PASS}@${process.env.POSTGRES_HOST}:${process.env.POSTGRES_PORT}/${process.env.POSTGRES_DB}`);
  // const sequelize = new Sequelize(`postgres://usef:rahasia@gisel.ddns.net:9022/hapuslah`);
  console.log(`\n\n\n******* koneksi ke ${connstring}.`);

  sequelize
  .authenticate()
  .then(() => {
    console.log(`${__filename} => Succeed connect to ${dbhost}:${dbport}/${dbname} as ${dbuser}`);
  })
  .catch(err => {
    console.log(`${__filename} => Failed connect to ${dbhost}:${dbport}/${dbname} as ${dbuser} => ${JSON.stringify(err)}.`);	
  });
}

// tunggu sampai env populated
// populating environment variables could take some times
const timeout = 2000;
setTimeout(function() {

  otentikasi();

}, timeout);

export default sequelize;

--#

--% /np/node-postgres/src/core/db/index.js
// import sequelize from './mongo';
import sequelize from './postgres';

export default sequelize;
--#

--% /np/node-postgres/src/apps/user/extender.js

import AuthProvider from './auth/provider';
// import User from './models';

// const Extender = () => ({
  
//   createOrUpdateUser: async (req, res) => {
//     const { name, picture, email } = req.user;
  
//     const user = await User.findOneAndUpdate(
//       { email },
//       { name: email.split("@")[0], picture },
//       { new: true }
//     );
//     if (user) {
//       console.log("USER UPDATED", user);
//       res.json(user);
//     } else {
//       const newUser = await new User({
//         email,
//         name: email.split("@")[0],
//         picture,
//       }).save();
//       console.log("USER CREATED", newUser);
//       res.json(newUser);
//     }
//   },

//   currentUser: async (req, res) => {
//     User.findOne({ email: req.user.email }).exec((err, user) => {
//       if (err) throw new Error(err);
//       res.json(user);
//     });
//   },

// });

// const ExtenderObj = Extender();

const ExtensionRouter = Router => Router
  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  // .post("/current-admin", ExtenderObj.currentUser)

  .post("/api/users/login", AuthProvider.login)
  .post("/api/users/register", AuthProvider.register)
  .post("/api/users/update_password", AuthProvider.updatePassword)
  ;

export default ExtensionRouter;
--#

--% /np/node-postgres/src/apps/user/models/mongo.js
import mongoose from 'mongoose';
// const { ObjectId } = mongoose.Schema;

const userSchema = new mongoose.Schema(
  {

    created_at: Date,
    email: { type: String, required: true, },
    firstname: String,
    lastname: String,
    password: String,
    phone: String,
    role: String,
    username: String,

    // name: String,
    // address: String,

    // email: {
    //   type: String,
    //   required: true,
    //   index: true,
    // },
    // role: {
    //   type: String,
    //   default: "subscriber",
    // },
    // cart: {
    //   type: Array,
    //   default: [],
    // },    
    // wishlist: [
    // 	{ type: mongoose.Schema.Types.ObjectId, ref: "Product" }
    // ],
  },
  { 
    timestamps: true
  }
);

export default mongoose.model("User", userSchema);

--#

--% /np/node-postgres/src/apps/user/models/postgres.js
import { default as dbConnect } from 'D';
import { 
  BIGINT, 
  BOOLEAN, 
  DATE,
  DECIMAL,
  DOUBLE, 
  ENUM, 
  FLOAT, 
  INTEGER, 
  STRING, 
  TEXT, 
  UUID, 
  UUIDV1, 
  UUIDV4,
} from 'sequelize';

const tableName = 'users';
const fieldsMap = {
  
  created_at: DATE,
  email: {
    type: STRING,
    allowNull: false,
  },
  firstname: STRING,
  lastname: STRING,
  password: STRING,
  phone: STRING,
  role: STRING,
  username: STRING,	
};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const User = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

if (parseInt(process.env.DB_SYNC)===1) {
  console.log(`\n\nDO SYNC'ing database...`);
  dbConnect.sync({force: true});
} else {
  console.log(`\n\nnot synching database...`);
}

export default User;
--#

--% /np/node-postgres/src/apps/user/models/index.js
// import User from './mongo';
import User from './postgres';

export default User;

--#

--% /np/node-postgres/src/apps/user/auth/index.js
import Kripto from './kripto';
const Enkripsi = new Kripto('bcrypt');

export default Enkripsi;
--#

--% /np/node-postgres/src/apps/user/auth/token.js
import { default as dbConnect } from 'D';

const {
  // DATE,
  INTEGER,
  STRING,  
} = require('sequelize');

const tableName = 'tokens';

const Token = dbConnect.define(
  
  tableName,

  {
    id_user: {
      type: INTEGER,
      allowNull: false
    },
    refresh_expired_time: {
      type: 'TIMESTAMP',
      allowNull: false
    },
    refresh_token: {
      type: STRING,
      allowNull: false
    },    
  },

  {
    freezeTableName: true,
    schema: process.env.DB_SCHEMA,
    timestamps: false
  }
  
)

Token.removeAttribute('id');

export default Token;


--#

--% /np/node-postgres/src/apps/user/auth/token_mongo.js
import mongoose from 'mongoose';

const fieldsMap = {
  id_user: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  refresh_token: String,
  refresh_expired_time: Date,
}

const optionsMap = {
  timestamps: true
}

const TokenSchema = new mongoose.Schema(  
  fieldsMap,
  optionsMap
)

export default mongoose.model('Token', TokenSchema);

--#

--% /np/node-postgres/src/apps/user/auth/provider.js
import User from 'AU/models';
import Kripto from './kripto';
import Monyong from './jwt';

const Enkripsi = new Kripto('bcrypt');

const {
  doGenToken,
  generateToken,
  refreshToken,
  decodeToken,
} = Monyong;

const login = async (req, res, next) => {
  const process = async () => {

    // loginAxios(
    //   { 
    //     data: {
    //       username: values.username,
    //       password: values.password,
    //     }
    //   },

    const {
      email,
      password
    } = req.body;

    if (email == null || email == undefined || password === null || password === undefined)
      res.status(512).send({
        status: 'Error',
        message: 'Login not found',
      });

    let pengguna_attributes = [ 'id', 'email', 'phone', 'role', 'username', 'password' ];
    let pengguna_where = { email };
    const pengguna = await User.findOne({
      attributes: pengguna_attributes,
      where: pengguna_where,
    });

    if (pengguna) {

      let check = await Enkripsi.check(password, pengguna.password);

      if (!check) {
        console.log(`gagal cek login ${email} dengan password ${password}.`);
        res.status(512).send({
            status: 'Error',
            message: 'Login not found',
        });
      }

      const jwt_token = await 
        generateToken(
          pengguna.id, 
          // pengguna.username, 
          // pengguna.name, 
          pengguna.email, 
          pengguna.phone, 
          pengguna.role
        );
      let response = {
        response: 'ok',
        data: {
          jwt: jwt_token,
          token: doGenToken(),          
          email: pengguna.email,
          username: pengguna.username,
          phone: pengguna.phone,
          role: pengguna.role,
        },
      };
      console.log(`login ${email}, user ${pengguna}, successful: ${JSON.stringify(response)}`);
      res.json(response);
    }

  }

  try {
    process();
  } catch (err) {
    console.log(`Login processing error: ${err}.`);
    return next(err);
  }
};

const register = async (req, res, next) => {
  try {
    const {
      email,
      password,
      ...sisa
    } = req.body;

    const pengguna = User.build({
      email,
      password: Enkripsi.encrypt(password),
      ...sisa
    });

    const result = await pengguna.save();
    res.json(result);
  } catch (e) {
    return next(e);
  }
};

const updatePassword = async (req, res, next) => {
  try {
    const {
      email,
      password
    } = await req.body;

    console.log(`updatePassword, email: ${email}, password = ${password}.`);

    const pengguna = await User.findOne({
      attributes: ['id', 'email', 'password'],
      where: {
          email,
      }
    });

    if (pengguna && password !== '') {
      // ternyata ini [object Promise]
      let hasil_enkripsi = await Enkripsi.encrypt(password);
      console.log(`updatePassword, email: ${email}, password = ${password} => ${hasil_enkripsi}.`);
      pengguna.password = hasil_enkripsi;
      const result = await pengguna.save();
      res.json(result);
    } else {
      console.log(`update ${email} not found.`);
      res.status(512).send({
        status: 'Error',
        message: 'Email not found',
      });
    }

  } catch (err) {
    return next(err);
  }
};

export default {
  login,
  register,
  updatePassword,
};

--#

--% /np/node-postgres/src/apps/user/auth/kripto.js
import bcrypt from 'bcrypt';
import crypto from 'crypto';

class Kripto {
  constructor(which_encryption = 'md5') {
    this.encrypt = this.hash_md5
    if (which_encryption == 'sha') {
      this.encrypt = this.hmac_sha256;
    } else if (which_encryption == 'bcrypt') {
      this.encrypt = this.hash_bcrypt;
      this.check = this.check_bcrypt;
    }
  }

  hash_md5 = (password) => crypto
    .createHash("md5")
    .update(password)
    .digest("hex");

  hmac_sha256 = (password) => crypto
    .createHmac("sha256", process.env.APP_SECRET)
    .update(password)
    .digest("hex");

  hmac_sha256_longer = (password) => crypto
    .createHmac("sha256", process.env.APP_SECRET)
    .update(password)
    .digest("hext").toString("hex");

  hash_bcrypt = async (password) => {
    const hashed = await bcrypt.hash(password, bcrypt.genSaltSync(+process.env.SALT_ROUNDS));
    return hashed;
  }

  check_bcrypt = async (suppliedPlainPassword, internallySavedHashedPassword) => {
    console.log(suppliedPlainPassword, '>>>>', await this.hash_bcrypt(suppliedPlainPassword), '>>>', internallySavedHashedPassword);
    const compare = await bcrypt.compare(suppliedPlainPassword, internallySavedHashedPassword);
    return compare;
  }
}

export default Kripto;
--#

--% /np/node-postgres/src/apps/user/auth/jwt.js
const jwt = require('jsonwebtoken');
const moment = require('moment');
const randToken = require('rand-token');
const UIDGenerator = require('uid-generator');

import Token from './token';
// import Token from './token_mongo';

const doGenToken = () => {
  // Default is a 128-bit UID encoded in base58
  const uidgen = new UIDGenerator(256);
  return uidgen.generateSync();
}

const generateToken = async (userId, email=null, phone=null, role=null) => {
  let refreshToken = randToken.uid(64);
  let age = process.env.NODE_ENV == 'production' ? 10 : 3 * 60 * 60;
  // let age = 3 * 60 * 60
  let expTime = Date.now() / 1000 + age;
  
  // refresh token
  let oldToken = await Token.findOne({ where: { id_user: userId } });
  if (!oldToken) {
    await Token.build({
      id_user: userId,
      refresh_token: refreshToken,
      expired_time: moment().add(7, "days"),
    });
  } else {
    console.log(`updating old token.`);
    await oldToken.update({
      refresh_token: refreshToken,
      expired_time: moment().add(7, "days"),
    });
  }

  // access token
  let jwt_internal_data = { id_user: userId, };

  if (email !== null && phone !== null && role !== null) {
    jwt_internal_data = { 
      id_user: userId, 
      email, 
      phone, 
      role 
    };
  }

  let jwt_data = {
    exp: expTime,
    data: jwt_internal_data,
  };

  let jwt_key = process.env.JWT_SECRET;
  let jwt_algo = { algorithm: "HS256" };
  const accessToken = jwt.sign( jwt_data, jwt_key, jwt_algo );
  
  return { accessToken, refreshToken, expTime }
}


const refreshToken = async (refresh_token) => {
  let authToken = await Token.findOne({ where: {refresh_token} });
  if (authToken) {
    if (moment(authToken.expired_time) < moment()) {
      throw new Error("refresh token already expired.");
    } else {
      let newToken = await generateToken(authToken.id_user);
      return newToken;
    }
  } else {
    throw new Error("auth token not valid.");
  }
}

const decodeToken = token => {
  try {
    return jwt.verify(token, process.env.JWT_SECRET);
  } catch (err) {
    throw err;
  }
}

export default {
  doGenToken,
  generateToken,
  refreshToken,
  decodeToken,
};
--#

--% /np/node-postgres/src/server/server-dev.js
import express from 'express';
import webpack from 'webpack';
import webpackDevMiddleware from 'webpack-dev-middleware';
import webpackHotMiddleware from 'webpack-hot-middleware';
// import config from '../../webpack.dev.config.js';
import config_func from 'S/../../webpack-node-pg';
import App from 'C/app';

import dotenv from 'dotenv';
dotenv.config();

const config = config_func();

const app = express();
const compiler = webpack(config);

app.use(webpackDevMiddleware(compiler, {
  publicPath: config.output.publicPath
}));

app.use(webpackHotMiddleware(compiler));

App(app);

// const PORT = process.env.PORT || 8080
// app.listen(PORT, () => {
//   console.log(`App listening to ${PORT}....`)
//   console.log('Press Ctrl+C to quit.')
// })
// tunggu 2 detik
const timeout = 2000;
setTimeout(function() {
  const PORT = process.env.PORT || 8080;
  app.listen(PORT, () => {
    console.log(`App listening to ${PORT}....`)
    console.log('Press Ctrl+C to quit.')
  });
}, timeout);


--#

--% /np/node-postgres/src/server/server-prod.js
import path from 'path'
import express from 'express'

const app = express(),
            DIST_DIR = __dirname,
            HTML_FILE = path.join(DIST_DIR, 'index.html')


app.use(express.static(DIST_DIR))

app.get('*', (req, res) => {
  res.sendFile(HTML_FILE)
})

const PORT = process.env.PORT || 8080
app.listen(PORT, () => {
  console.log(`App listening to ${PORT}....`)
  console.log('Press Ctrl+C to quit.')
})


--#

--% /np/node-postgres/__mocks__/styleMock.js
module.exports = {};


--#

--% /np/node-postgres/__mocks__/fileMock.js
module.exports = 'test-file-stub';


--#

--% /np/react-antd/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fullstack Template | Fulgent</title>

</head>
<body>
  <div id="app"></div>
</body>
</html>

--#

--% /np/react-antd/.env
HOST=localhost
PORT=9000

SALT_ROUNDS=14
#mongo or postgres
DB_CHOICE=postgres
DB_SCHEMA=public
SESSION_SECRET=K1nG.5up3rM4rk3t!
JWT_SECRET=Qu33n.5up3rM4rk3t!
NODE_ENV=development

MONGO_DB=hapuslah
MONGO_HOST=gisel.ddns.net
MONGO_PORT=27017
MONGO_USER=usef
MONGO_PASS=rahasia

POSTGRES_DB=hapuslah
POSTGRES_USER=usef
POSTGRES_PASS=rahasia
POSTGRES_HOST=gisel.ddns.net
POSTGRES_PORT=9022

--#

--% /np/react-antd/.eslintrc.js
module.exports = {
  "extends": [
    "eslint:recommended",
  ],
  "parser": "babel-eslint",
  "rules": {
    "no-unused-vars": "off",
    "no-undef": "off",
    "no-console": "off",
    "no-case-declarations": "off",
    "no-prototype-builtins": "off",
  }
};


--#

--% /np/react-antd/index.js
import React from 'react';
import ReactDOM from 'react-dom';

import './index.css';
import 'font-awesome/css/font-awesome.min.css';
// import { App } from './components/App';
import App from './components/App';

ReactDOM.render(<App />, document.querySelector('#app'));


--#

--% /np/react-antd/.babelrc
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-react"
  ],
  "plugins": [
    "react-hot-loader/babel",
    "@babel/plugin-proposal-class-properties",
    ["@babel/transform-runtime"]
  ]
}



--#

--% /np/react-antd/config.js
const config = {
  
  backend: {
    host: '__TEMPLATE_SERVER_HOST',
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

--% /np/react-antd/index.css
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

--% /np/react-antd/assets/favicon.ico
AAABAAMAEBAAAAEAIABoBAAANgAAACAgAAABACAAKBEAAJ4EAAAwMAAAAQAgAGgmAADGFQAAKAAAABAAAAAgAAAAAQAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPr59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//nw7//69fP/+vn3//r59//6+ff/+vn3//r59//50tX/+vn3//nLz//6+ff/+s3R//mttP/5r7f/+vn3//nP0//5yc3/+brA//r39f/65OX/+amx//mxuf/65OT/+cfL//r19P/5vsT/+vn3//nEyf/6+ff/+aav//r59//5u8H/+cHG//nLz//51df/+cTI//r59//5wMb/+d7f//m7wf/5lJ//+vTz//r59//5yMz/+vn3//nJzf/6+ff/+cvP//rY2v/51Nf/+c7S//nHzP/6+ff/+d/g//ni4//5x8v/+c7S//nLz//6+ff/+bnA//r59//5u8H/+vn3//m1vP/5usD/+trc//nFyv/5wMX/+vLx//m7wf/6+Pb/+cfL//r59//509b/+vn3//rp6f/5rLT/+uvr//r59//5uL7/+cHG//nIzf/5uL//+vf2//mzuf/619n/+vn3//nHy//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+tfZ//nV2P/5s7r/+dPW//r59//6+ff/+vn3//r59//66ur/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3/9rFzP9m1eT/+urq//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59/+a8vn/R7bM//j59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/7vj3/917i//61Nb/+vn3//r59//6+ff/+vn3//r59//5ztL/+aOs//m7wf/6+ff/+cbL//mttf/5rLT/+vn3//r59//5pq//+dDT//r59//64OL/+amx//mstP/64uP/+vXz//r59//5sbj/+vn3//nFyf/6+ff/+aqy//r59//66en/+amy//mirP/6+ff/+cTJ//r59//5xMn/+d7f//ri4//5qLD/+trc//r59//5x8z/+vn3//nJzf/6+ff/+dTX//nCx//5xMn/+t7g//nHzP/6+ff/+d7f//nj5P/5vML/+uzs//nO0v/6+ff/+bi+//r29f/5usD/+vn3//nM0P/53uD/+dfZ//nV2P/5wsf/+u7u//m4v//6+Pf/+vf1//mwuP/65OX/+vn3//rr6//5r7b/+vLw//r59//50dT/+vn3//rp6f/66en/+vj2//m2vf/63N7/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAACAAAABAAAAAAQAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPr59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+Pb/+ejo//no6P/66en/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+cHH//r59//6+ff/+vn3//m9w//6+ff/+vn3//r59//64eL/+XGB//l8iv/67e3/+cPI//r59//6+ff/+vn3//nN0f/5j5v/+aev//l9i//68vD/+vn3//r59//6+ff/+vn3//mlrv/4Znf/+bi///rh4v/62tz/+vn3//r59//5laD/+vn3//r59//67u7/+YqW//r59//6+ff/+vLx//lqe//65eX/+uHi//h1hP/5maP/+vn3//r59//64OH/+Zei//r29f/6+ff/+u3t//mMmf/68/H/+vn3//r59//5pa7/+aSt//r29P/5oar/+YyY//nDyP/6+ff/+vn3//mVoP/6+ff/+vn3//mRnP/65eb/+vn3//r59//5naf/+uLj//r59//6+ff/+tTX//hQZP/6+ff/+vn3//mnsP/67Oz/+ZKd//iSnv/5oKr/+vDv//mutf/6+ff/+vf1//mJlf/6+ff/+vn3//r59//5YHL/+cPI//r59//6+ff/+ZWg//r59//66+r/+YmW//r59//6+ff/+vn3//mXov/6+ff/+vn3//r59//6+ff/+XyK//r59//6+ff/+bO6//mosP/66ur/+vf1//rd3v/5wMb/+bO6//r59//50NP/+cDF//r59//6+ff/+vn3//mwuP/5w8j/+vn3//r59//5c4L/+uPj//mKl//65+f/+vn3//r59//6+ff/+Zij//r59//6+ff/+vn3//r59//5maP/+vn3//r59//5t77/+cjM//mUn//69PP/+vn3//m2vP/5tbz/+vn3//m3vf/52tz/+vn3//r59//6+ff/+czQ//nEyP/6+ff/+vn3//mIlf/4YnT/+YKP//r59//6+ff/+vn3//r59//5laD/+vn3//r59//6+ff/+vn3//mZo//6+ff/+vn3//mzuv/6+ff/+t/g//r59//65+j/+brA//mSnf/6+ff/+cLI//nLz//6+ff/+vn3//r59//5vsT/+dTW//r59//6+ff/+ZWg//rs7P/4aXr/+ubm//r59//6+ff/+vn3//mOmv/68fD/+vn3//r59//67Oz/+Zql//r59//6+ff/+YuX//rk5f/66ur/+uTl//mWof/64eL/+Zij//rh4v/67+7/+ZGc//r59//6+ff/+vn3//mRnP/69vT/+vn3//r59//5laD/+vn3//rq6v/4ZXb/+unp//r59//6+ff/+t/g//mIlf/6+ff/+vj2//l7if/66ur/+vn3//r59//60dX/+ZSf//mDkP/5lqH/+vn3//r59//5p7D/+vX0//r59//5iZX/+t7g//r59//509b/+ZGc//r59//6+ff/+vn3//mVoP/6+ff/+vn3//rp6f/4c4L/+vn3//r59//6+ff/+brA//ljdf/4XW//+cLH//r59//6+ff/+vn3//mqsv/5s7r/+ZCc//nFyv/6ztL/+vn3//lgcv/69/X/+vn3//rz8v/5doT/+GN0//l1hP/69fP/+vn3//r59//6+ff/+ZWg//r59//6+ff/+vn3//r49//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+u3s//mWoP/53+D/+dDT//mvt//5rLT/+ZKe//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//5laD/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6wcb/+u7t//nd3//50dT/+bm///rX2f/5laD/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//mVoP/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//m0u//6+ff/+ba8//ry8P/5nKb/+aCq//nEyf/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+b7E//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+cDF/9nd4f+Xl6r/vvX4//rn5//60NP/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//69/X/nICW/xbf9P8s6/z/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59/8q6/z/MsPZ/wzp/f/y+Pf/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3/0vt+/+bXnj/Q87h//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/yvb4/7BfeP/VgJH/+tTX//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+Gl5//mjrP/5iZX/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+u7t//mJlv/4aHn/+ba8//r59//6+ff/+vn3//r59//5yM3/+GJ0//lzg//66ur/+bm///r59//6+ff/+vn3//r59//5j5v/+tPW//nCx//66Oj/+vn3//r59//6+ff/+vj2//mLmP/4YnT/+aKr//rc3v/61Nf/+vn3//r59//4Wm3/+ba9//nk5f/5d4b/+sbL//r59//6+ff/+uLj//h3hv/69fP/+uvq//h0hP/5mKP/+vn3//r59//6+ff/+vn3//m8wv/5eoj/+tnb//m8wv/6+ff/+vn3//r59//5mKP/+b3D//r59//5uL7/+XyK//nDyP/6+ff/+vn3//rp6f/6+ff/+vn3//nn5//5h5T/+vn3//r59//5kJz/+vLx//r59//6+ff/+s/S//hfcf/6+ff/+vn3//r59//69vT/+Y+b//mBj//5pK3/+bG5//r59//6+ff/+vXz//mNmf/6+ff/+vn3//r59//5anv/+cPI//r59//6+ff/+vn3//r59//6+ff/+a61//mosf/6+ff/+vn3//mYov/6+ff/+vn3//r59//6+ff/+ICO//r59//6+ff/+vn3//m7wf/67Oz/+aix//mDkf/5sbn/+vn3//r59//5y8//+cXK//r59//6+ff/+vn3//m1vP/5w8j/+vn3//r59//6+ff/+ay0//hkdf/5gY7/+vf2//r59//6+ff/+Zij//r59//6+ff/+vn3//r59//4mKL/+vn3//r59//6+ff/+bG5//nO0f/4kJz/+Y+b//rT1v/619n/+vn3//m3vf/52tz/+vn3//r59//6+ff/+czQ//nEyf/6+ff/+vn3//mfqP/5mqT/+vX0//r59//6+ff/+vn3//r59//5lJ//+vn3//r59//6+ff/+vn3//mZo//6+ff/+vn3//r59//5r7f/+bC3//r59//5zND/+uHi//mxuf/6+ff/+cbL//nHy//6+ff/+vn3//r59//5usD/+dfZ//r59//6+ff/+HiH//r59//6+ff/+vn3//r49v/6+ff/+vn3//mKlv/69PL/+vn3//r59//619r/+a21//r59//6+ff/+crO//re3//5tLv/+vn3//r29P/5uL//+bG5//r59//68vH/+YuY//r59//6+ff/+vn3//mNmf/69/b/+vn3//r59//5h5T/+cfM//r39f/5g5H/+cbL//r59//6+ff/+tze//mFkv/6+Pb/+u/v//lwf//69vT/+vn3//r59//5r7f/+trc//nT1v/6+ff/+vn3//m0u//5usD/+vDv//r59//5kp7/+c/S//r59//5wcf/+Zul//r59//6+ff/+vn3//ry8P/5eIb/+Fhr//mlrv/6+ff/+vn3//r59//6+ff/+cDG//hldv/5ZHb/+tzd//r59//6+ff/+vn3//mwt//5tbz/+vj2//r59//6+ff/+brA//rw7//5wcb/+vn3//r39f/5hZL/+GN0//mGk//6+Pb/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+u/u//rv7v/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAADAAAABgAAAAAQAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPr59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vb1//nd3v/53d7/+d3e//nd3//67ez/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//67+//+tja//r59//6+ff/+vn3//r59//69fT/+tPW//r59//6+ff/+vn3//r59//6+ff/+uvr//rCx//5pa7/+s3R//rz8f/67Oz/+tze//r59//6+ff/+vn3//r59//6+ff/+cDG//hXav/4cYD/+HGA//hneP/5l6L/+vj2//r59//6+ff/+vn3//r59//6+ff/+vn3//rk5P/5trz/+aav//rZ2//69fP/+uXm//rf4P/6+ff/+vn3//r59//509b/+YeU//r59//6+ff/+vn3//r59//6xcr/+X2L//r59//6+ff/+vn3//r59//64eL/+W19//lkdv/5fYv/+Wt7//mIlf/5w8j/+Zei//r59//6+ff/+vn3//r59//61dj/+YSR//rX2f/6+ff/+vn3//rq6v/5l6L/+dHU//r59//6+ff/+vn3//r59//6+ff/+tPW//hbbv/5bn7/+X2L//hpev/5qrL/+bG5//mgqf/6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//rz8v/5h5T/+szQ//r59//6+ff/+vn3//r19P/5ipf/+Z+p//ru7v/6+Pb/+u3s//mXov/5bX3/+ZWg//r59//6+ff/+vn3//rr6//5laD/+tLV//r39v/6+ff/+vn3//r49v/63+D/+G+A//ro6P/6+ff/+vn3//r59//67u3/+FJl//q9wv/68vH/+vj2//rg4f/4dYT/+Y+a//mfqf/6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//rV2P/5go//+u7t//r59//6+ff/+vn3//rd3v/5hJH/+uzs//r59//6+ff/+vn3//rm5//5TGH/+X2L//r59//6+ff/+vn3//rM0P/5sLf/+vLx//rO0f/5vsT/+b3D//rKzv/67ez/+uLj//mBjv/6+Pb/+vn3//r59//5qrL/+Z2n//r59//6+ff/+vn3//r59//6xMn/+CQ9//mfqf/6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//mEkf/5tbv/+vn3//r59//6+ff/+vn3//m+w//5o6z/+vn3//r59//6+ff/+vn3//r39v/5jZr/+YKQ//r59//6+ff/+vn3//mTn//66Oj/+Zyn//mRnf/5pa7/+aWu//mXov/5pa7/+vLx//mbpf/64uP/+vn3//rz8v/5kp3/+tvc//r59//6+ff/+vn3//r59//69fT/+E9j//mfqf/6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+tLU//hXav/68vH/+vn3//r59//6+ff/+vn3//mWof/5y8//+vn3//r59//6+ff/+vn3//r59//5t73/+Y+a//r59//6+ff/+vn3//mGlP/64eH/+Zmk//rx8P/65eX/+vj2//r19P/5q7P/+uLj//rQ0//5wcb/+vn3//rp6f/5mKP/+unp//r59//6+ff/+vn3//r59//6+ff/+Y+a//mfqf/6+ff/+vn3//r59//50tX/+Wp7//rt7P/68/L/+F1v//nHzP/6+ff/+vn3//r59//6+ff/+vn3//mAjv/5293/+vn3//r59//6+ff/+vn3//r59//5ys7/+Zag//r59//6+ff/+vn3//iMmP/5y8//+c/T//mXo//5p7D/+vb1//r59//5tbz/+uLj//ri4//5tbz/+vn3//rj5P/5mqP/+u/u//r59//6+ff/+vn3//r59//6+ff/+a21//mgqf/6+ff/+vn3//r59//50tX/+D9V//lufv/5n6n/+HaG//r59//6+ff/+vn3//r59//6+ff/+vn3//l/jf/52tz/+vn3//r59//6+ff/+vn3//r59//5yc3/+Zul//r59//6+ff/+vn3//mJlv/67Oz/+vHw//mPm//6+Pb/+vn3//r59//5s7r/+uLj//rb3f/5usD/+vn3//rj5P/5l6H/+u7t//r59//6+ff/+vn3//r59//6+ff/+auz//mnr//6+ff/+vn3//r59//50tX/+X+N//mWoP/4KEH/+szQ//r59//6+ff/+vn3//r59//6+ff/+vn3//mTnv/5x8v/+vn3//r59//6+ff/+vn3//r59//5t73/+bG4//r59//6+ff/+vn3//mFkv/69/b/+vn3//rq6v/6+ff/+vn3//rv7v/5o63/+ubn//mFkv/5s7r/+vn3//ro6f/5lJ//+ujo//r59//6+ff/+vn3//r59//6+ff/+Y6a//nEyf/6+ff/+vn3//r59//50tX/+YaT//ry8f/5gpD/+YmW//rv7v/6+ff/+vn3//r59//6+ff/+vn3//m8wv/5nab/+vj2//r59//6+ff/+vn3//r49v/5laD/+tHV//r59//6+ff/+vn3//mkrf/5xMn/+vPy//ry8f/68vH/+vHw//l5h//5q7P/+tTX//mBj//5pa7/+vLx//rz8v/5jZn/+tbY//r59//6+ff/+vn3//r59//69fT/+Fls//rw7//6+ff/+vn3//r59//50tX/+YaT//r59//66+v/+XyK//l0g//65+f/+vn3//r59//6+ff/+vn3//rf4P/5fYv/+unp//r59//6+ff/+vn3//rj5P/5g5D/+uXm//r59//6+ff/+vn3//m1vP/5jJj/+aav//nEyf/5maT/+cbL//rZ2//69/X/+uXm//rV2P/5rLT/+vPy//r59//5rrX/+Y+a//r59//6+ff/+vn3//r59//5vsT/+YGP//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vHw//mLmP/5eYf/+vDv//r59//6+ff/+vn3//r29P/5kp3/+ZOe//r59//6+ff/+vf1//h1hP/5oar/+vf2//r59//6+ff/+vn3//rx8P/5xsv/+YCO//l3hv/5pa3/+X+N//r59//6+ff/+vn3//rAxv/5usD/+vn3//r59//68O//+F1v//mwt//6+ff/+vn3//ri5P/5Z3j/+tTW//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//rw7//5eYj/+Y6a//r59//6+ff/+vn3//r59//67+7/+WFy//lcbv/5gY7/+Epf//lufv/68/L/+vn3//r59//6+ff/+vn3//mXof/5Z3j/+sjM//l8iv/5s7r/+Zym//rN0f/6+ff/+vn3//mHlP/5pa7/+vn3//r59//6+ff/+ujo//hKXv/5a3z/+X+N//hEWv/5n6j/+vf1//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//r59//66en/+auz//r59//6+ff/+vn3//r59//6+ff/+vLx//mzuv/5l6L/+ba9//r19P/6+ff/+vn3//r59//6+ff/+vn3//r39f/68O//+YeT//rW2f/5tLv/+uTl//mCj//66en/+dze//hneP/5sLj/+vj2//r59//6+ff/+vn3//ro6P/5qLH/+Zei//rFyv/69vX/+vn3//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//ry8f/5maP/+rG4//rx8P/5tr3/+urq//mcpv/5xsr/+Y+b//hrfP/66en/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//rN0f/6n6j/+vPy//rx8P/5tr3/+uvq//mkrv/55+f/+Z2n//hbbf/68O//+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//ro6P/60tX/+vn3//rq6v/5s7r/+vHw//mkrf/56en/+u/v//lygv/69vT/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//rg4v/5s7v/+vn3//rg4f/5rbT/+vj2//mep//5gY7/+E5i//m3vv/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//62dv/+Zah//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//ri4//5rrX/5/Ly/8iir/+0xc//7/j3//ru7f/5pa7/+tDU//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//69vT/+u3t//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//rx8P/1o63/rYWZ/2WSqv8W5/r/lvL5//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//UzNP/UbTJ/xHk+P8M6f3/K+v8//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59/+i8/n/Fur9/xXg9P8V4PT/DOn9/+/49//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59/+o8/n/Ger9/2yLo/9SpLv/F+X5//P59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//O9vj/Jev8/51cdv98fJX/VePx//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//5+ff/fPH6/65Tbv+jZX3/17/I//rl5f/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/9fn3/91tgP/lfIz/9k9j//ljdP/69vT/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//lufv/5foz/+s3R//mBjv/6yMz/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vPy//rW2f/5srn/+a+2//rZ2//69PP/+vn3//r59//6+ff/+vn3//r59//6+Pb/+t/g//mWof/5g5D/+r3D//rx8P/52tz/+tnb//r59//6+ff/+vn3//r59//6+ff/+vn3//mXov/5laD/+ufn//rj5P/5rbX/+vb0//r59//6+ff/+vn3//r59//6+ff/+vn3//rX2f/5k5//+YKQ//rDyf/68fD/+tnb//rQ0//6+ff/+vn3//r59//66+v/+X+N//hFWv/4ZHX/+GZ4//hPY//5pa7/+vX0//r59//6+ff/+vn3//r59//5yc7/+Ftt//mAjv/5lqH/+XSD//mDkf/5rrb/+bC3//r59//6+ff/+vn3//r59//6+ff/+vn3//rKzv/5hZL/+t7f//rv7//5tLv/+uzr//r59//6+ff/+vn3//r59//6+ff/+sHG//lVaP/5hJL/+Zei//lxgf/5m6X/+a+2//mfqf/6+ff/+vn3//r59//5qbL/+Etg//ra3P/68O//+vHw//rLz//5Y3X/+uHi//r59//6+ff/+vn3//rs7P/5e4n/+cLH//r39f/6+ff/+vHw//mZo//5V2r/+a61//r59//6+ff/+vn3//r59//6+ff/+vn3//rp6f/4a3z/+Fdq//m8wv/5sbn/+uLj//r59//6+ff/+vn3//r59//65eb/+FFk//rS1f/69/X/+vn3//rr6//5fYv/+XuJ//mfqf/6+ff/+vn3//r59//65eX/+ujp//r59//6+ff/+vn3//ry8f/4dIT/+tPW//r59//6+ff/+vn3//rO0v/5i5j/+vX0//r59//6+ff/+vn3//rl5f/5QVf/+Zul//r59//6+ff/+vn3//r59//6+ff/+vf2//m6wP/5jZj/+WJz//hjdf/5ub//+tbY//r59//6+ff/+vn3//r59//5oKr/+a+3//r59//6+ff/+vn3//r59//60dT/+CI8//mfqf/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//rx8P/4coH/+tTX//r59//6+ff/+vn3//meqP/5vsP/+vn3//r59//6+ff/+vn3//r39f/5go//+Z+p//r59//6+ff/+vn3//r59//6+ff/+sbK//mUn//64+T/+VZp//l/jf/50tb/+Z+p//r59//6+ff/+vn3//ry8f/5k57/+t7g//r59//6+ff/+vn3//r59//6+Pb/+Vps//mfqf/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//rLz//4W23/+uPk//r59//6+ff/+vn3//h2hf/54uP/+vn3//r59//6+ff/+vn3//r59//5qLD/+amx//r59//6+ff/+vn3//r59//6+ff/+YuX//ry8f/6+Pb/+XuJ//hhc//5xsv/+YOQ//r59//6+ff/+vn3//ro6P/5maP/+urq//r59//6+ff/+vn3//r59//6+ff/+ZWh//mfqf/6+ff/+vn3//r59//6+ff/+vn3//rm5v/5vML/+XqI//g5T//5sLf/+vj2//r59//6+ff/+vn3//hjdP/68fD/+vn3//r59//6+ff/+vn3//r59//5t77/+a+2//r59//6+ff/+vn3//r59//68/L/+YyY//r08v/50dT/+ba9//mLl//5tLv/+aew//rU1v/6+ff/+vn3//rj5P/5maP/+u/u//r59//6+ff/+vn3//r59//6+ff/+a62//mgqf/6+ff/+vn3//r59//6+ff/+svP//hZbP/5anv/+Zqk//rX2f/6+ff/+vn3//r59//6+ff/+vn3//hmd//67Oz/+vn3//r59//6+ff/+vn3//r59//5s7r/+be+//r59//6+ff/+vn3//r59//5ys7/+b3D//nIzP/5jJj/+aSt//rX2v/5tLv/+ufn//mTnv/6+ff/+vn3//rk5P/5lqH/+u3t//r59//6+ff/+vn3//r59//6+ff/+aix//mqs//6+ff/+vn3//r59//68vH/+EVa//m1vP/67+//+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//l+jP/51tj/+vn3//r59//6+ff/+vn3//r59//5n6n/+s/S//r59//6+ff/+vn3//r59//5sbj/+t/g//mXov/66+r/+vn3//rt7P/5tLv/+u7t//mGk//69vT/+vn3//rq6v/5k57/+ubm//r59//6+ff/+vn3//r59//6+ff/+YaT//nLz//6+ff/+vn3//r59//519n/+E5i//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//mstP/5pq7/+vj2//r59//6+ff/+vn3//rz8v/5j5v/+tvd//r59//6+ff/+vn3//ru7f/5r7f/+uzr//mGk//6+ff/+vn3//r39f/5tbz/+uTl//m3vv/50dT/+vn3//r19P/5jJj/+tDU//r59//6+ff/+vn3//r59//68vH/+FVo//r19P/6+ff/+vn3//r59//53d7/+EZc//r19P/6+ff/+vn3//rv7v/5trz/+uzs//r59//6+ff/+vn3//rb3f/5fIr/+urq//r59//6+ff/+vn3//rO0f/5iJT/+u/u//r59//6+ff/+vn3//rh4v/5sLf/+ujp//mWoP/6+ff/+vn3//r59//5tLz/+uLj//re3//5tLv/+vn3//r59//5ucD/+XyL//r39f/6+ff/+vn3//r49v/5r7b/+ZGd//r59//6+ff/+vn3//r59//69vT/+FVo//mAjv/68PD/+vPx//mGk//5aHn/+u3t//r59//6+ff/+vn3//r19P/5kZ3/+YiV//r49v/6+ff/+t/g//hOYv/5wsf/+vn3//r59//6+ff/+vn3//nBx//5xsv/+ba9//nKzf/6+ff/+vn3//r59//5xMn/+c3Q//rm5v/5sbj/+vTz//r59//68/L/+XOD//mLmP/69vT/+vn3//rQ1P/5YnT/+tzd//r59//6+ff/+vn3//r59//6+ff/+uXl//hIXf/4LET/+CdA//hKXv/61tn/+vn3//r59//6+ff/+vn3//r59//68O//+Wt8//hFWv/4XG//+DJJ//mosP/6+ff/+vn3//r59//6+ff/+vn3//mIlP/68vH/+YqW//r29P/6+ff/+vn3//r59//65eb/+aSu//r08//5tLv/+ufn//r59//6+ff/+vTz//hidP/4TGD/+Fxv//g5UP/6t77/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//ry8P/5ztL/+c3Q//ry8P/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vf1//nHy//5srn/+tnb//r59//6+ff/+vn3//r59//6+ff/+vn3//qstP/6+ff/+q+3//r59//6+ff/+vn3//r59//6+Pb/+srO//r59//6293/+u/u//r59//6+ff/+vn3//rz8f/5w8j/+bG5//rc3v/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//rz8v/6+ff/+vPy//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==
--#

--% /np/react-antd/components/Setting/Settings_Popup.js
import React, { useEffect, useReducer, useState } from 'react';
import {
  Button,
  Collapse,
  DatePicker,
  Divider,
  Drawer,
  List,
  Modal,
  Popover,
  Select,
  Space,
} from 'antd';
import { ExclamationCircleOutlined } from '@ant-design/icons';
// import localForage from 'localforage';
// import { forage_cache_get, } from '@/utils/forage_cache';
// import DateAdder from '#c/Primitives/DateAdder/DateAdder';

const Settings_Popup = (props) => {
  
  // const [kycList, setKycList] = useState([]);

  // const sortByFirstName = (records) => {
  //   // return records.sort((a,b) => b.split('|')[1] - a.split('|')[1])
  //   records.sort();
  //   return records;
  // }

  // const skycTransformer = item => `${item.firstname.toLowerCase()} ${item.middlename.toLowerCase()} ${item.lastname.toLowerCase()} | ${item.email} | ${item.id_user} `;

  // const skycSetter = (items) => {
  //   let sorted = sortByFirstName(items)
  //   let unique = Array.from(new Set(sorted))
  //   setKycList(unique)
  // }

  // useEffect(() => {
  //   forage_cache_get(
  //     's_kyc', 
  //     skycTransformer,
  //     skycSetter
  //   );
  // }, []);

  function onChange(value, dateString) {
    console.log('Selected Time: ', value)
    // Formatted Selected Time:  2020-08-15 20:36:33
    console.log('Formatted Selected Time: ', dateString)
  }

  function onOk(value) {
    console.log('onOk: ', JSON.stringify(value)) // iso string
  }

  let Popuper = () => (<>
    <Select showSearch placeholder="Pilih nasabah" style={{ width: 450, marginBottom:'10px' }}>
      {/* {Array.from(new Set(kycList)).map( (item, index) => {
        let [fullname, email, uid] = item.split('|')
        return <Select.Option key={index} value={email.trim()}>{fullname} &lt;{email.trim()}&gt;, {uid.trim()}</Select.Option>
      })} */}
    </Select>
    <Divider dashed orientation='center'>Kirim Email Mutual Fund Activity</Divider>
    
    <DatePicker showTime onChange={onChange} onOk={onOk} size='small' style={{ marginTop:'10px'}}/>

    <Button type='primary' style={{ marginLeft: '20px', marginTop:'10px'}}>Set</Button>
  </>);

  let Container = () => (<Collapse accordion defaultActiveKey={['4']} style={{ width: 500 }}>

    {/* <Collapse.Panel header="Add date" key="4">
      <DateAdder />
    </Collapse.Panel> */}

    <Collapse.Panel header="Kirim email manual dan otomatis" key="1">
      <Popuper />
    </Collapse.Panel>

    <Collapse.Panel header="New BO User" key="2">
      <h1>Create BO User here</h1>
    </Collapse.Panel>

    {/* <Collapse.Panel header="Local Cache" key="3">
      <List
        size="small"
        bordered
        dataSource={kycList}
        renderItem={item => <List.Item>{item}</List.Item>}
        header={<div><Button onClick={() => {
          localForage.removeItem('bo/s_kyc/list')
          localForage.removeItem('bo/s_kyc/list/config')
          setKycList([])
        }}>Clear</Button></div>}
        footer={<div>Users cache used for selection</div>}
      >

      </List>
    </Collapse.Panel> */}

  </Collapse>);

  return <Container />;
}

export default Settings_Popup;


--#

--% /np/react-antd/components/modules/Dashboard/Dashboard.js
import React, { useEffect, useState } from 'react';

import {
  Button,
  DatePicker,
  Divider,
  Drawer,
  Input, InputNumber ,
  Modal,
  Popover,
  Select,
  Space,
} from 'antd';
import ToolbarContext from 'context/ToolbarContext';

const Dashboard = () => {
  const { setToolbar } = React.useContext(ToolbarContext);

  let Toolbar = () => (<Space>
    <h1>Dashboard</h1>
    <Button type="primary">Do something</Button>
    {/* <Button type="default" disabled onClick={generateBlotter2}>Blotter Subscription</Button> */}
    {/* <Popover placement="bottom" title={<span>Pilih nasabah dan tanggal Blotter subscription</span>} content={Blotter_Popup} trigger="click"> */}
    {/* <Button disabled type="primary">Blotter Subscription</Button> */}
    {/* </Popover> */}			
  </Space>);

  useEffect(function() {
    setToolbar(<Toolbar />)
  }, []);

  return <h1>Dashboard</h1>;
};

export default Dashboard;


--#

--% /np/react-antd/components/Layout/BaseLayout.css
.main-section {
  background-color: #e1e1e1;
  box-shadow: -3px -3px 7px #fffff7, 3px 3px 5px rgba(90,100,120,.2);
  
  margin-top: 50px;
  
  margin-left: var(--left-mainbar-percent);
  transition: all .5s ease;

  width: 100%;
  height: 100%;
  border: 1px solid red;
  

  padding: 15px;
}

.main-section.geser {
  margin-left: calc(var(--left-mainbar-percent) + var(--left-distance));
}


--#

--% /np/react-antd/components/Layout/BaseLayout.js
import React, { Fragment, useEffect, useState } from 'react';
import { hot } from 'react-hot-loader/root';
import { Route, Switch, withRouter } from 'react-router-dom';
import MainRoutes from '@/Route/Routes';
import './BaseLayout.css';
import Sidebar from './Sidebar';
import Header from './Header';
import Floating from './Floating';

const BaseLayout = ({ history, children }) => {

  const [show_menu, set_show_menu] = useState(false);

  function toggle_menu() {
    set_show_menu(!show_menu);
  }

  useEffect(function() {
    history.push('/dashboard');
  }, []);

  return <Fragment>

    <Header />

    <Sidebar active_classname={show_menu ? 'layout-sidebar active' : 'layout-sidebar'} toggler={toggle_menu} />
    
    <main className={'main-section' + (show_menu?' geser':'')}>
      
      {children}

      {MainRoutes.map(
        (item, index) => {
          return (<Route key={index} path={item.path} component={item.component} />)
        }
      )}

    </main>

    <Floating active_classname={show_menu ? 'layout-floating active' : 'layout-floating'} onClick={toggle_menu} />

  </Fragment>;
}

export default hot(withRouter(BaseLayout));


--#

--% /np/react-antd/components/Layout/Header/index.js
import React, { useContext } from 'react';
import { 
    PageHeader,
    Popover,
    Statistic,
    Tooltip,
} from 'antd';
import { Menu, Dropdown, Button } from 'antd';

import SessionContext from 'context/SessionContext';
import ToolbarContext from 'context/ToolbarContext';
import Settings_Popup from '@/Setting/Settings_Popup';
import './style.css';

// import { useHistory } from 'react-router-dom';
// import { useHistory } from 'react-router';
import { withRouter } from 'react-router-dom';

const Header = ({
  history,
}) => {

  const session = useContext(SessionContext);
  const toolbar = useContext(ToolbarContext);

  function clearSession() {
    session.sessionLogout();
    // clean up forage
    // forageHousekeeping();
    console.log(`Header => Session cleared...`);
    history.push('/');
  }

  function printSession() {
    console.log(`${JSON.stringify(session)}`);
  }

  const DropdownChoice = (<Menu>
    <Menu.Item key="1">
      {
        <>
        <h1>{session.username}</h1>
        <br/>
        <h4>{session.email}</h4>
        <br/>
        <h4>{session.phone}</h4>
        <br/>
        <h4>{session.role}</h4>
        </>
      }
    </Menu.Item>
  </Menu>);

  let UserDropdown = () => (<Dropdown overlay={DropdownChoice} placement="bottomRight">
    <i className='fa fa-user kiri'></i>
  </Dropdown>);

  const Settings = () => (<Popover placement="bottom" title={<span>Settings</span>} content={Settings_Popup} trigger="click">
    <Tooltip title='Setting' key="5"><i className='fa fa-cogs kiri'></i></Tooltip>
  </Popover>);

  return (<PageHeader
    className="layout-header"
    // onBack={() => null}
    title="Judul"
    subTitle="Subjudul"
    avatar={{ src: 'favicon.ico', shape: 'square' }}

    extra={[
      <Tooltip title='Pencarian' key="1"><i className='fa fa-search kiri'></i></Tooltip>,
      <Tooltip title='Notifikasi umum' key="2"><i className='fa fa-bell kiri' onClick={printSession}></i></Tooltip>,
      <UserDropdown key="3"/>,
      <Settings key="5"/>,
      <Tooltip title='Klik untuk logout' key="4"><i className='fa fa-sign-out kanan' onClick={clearSession}></i></Tooltip>,
    ]}
>
    {toolbar.ToolbarComponent}

    {/* <Clock />
    <Calendar /> */}

  </PageHeader>);
}

export default withRouter(Header);

--#

--% /np/react-antd/components/Layout/Header/style.css
.layout-header {
  background-color: rgba(141, 128, 235, 0.8);
  padding: 5px;

  font-size: .8rem;
}

.tombol {
  position: absolute;
  right: 0;
  padding: 10px;
}

.kiri, .kanan {
  margin: 5px;
  padding: 5px;
  transform: scale(1.5);
}

.kanan:hover, .kiri:hover {
  filter: hue-rotate(90deg);
}


--#

--% /np/react-antd/components/Layout/Sidebar/index.js

import React, { useContext } from 'react'
import classNames from 'classnames'
import './style.css'
import { Menu } from '@/Menu';

export default ({
    active_classname,
    toggler,
}) => {
  return (<div className={active_classname}>
    <Menu toggler={toggler} />
  </div>);
}


--#

--% /np/react-antd/components/Layout/Sidebar/style.css
.layout-sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: var(--left-sidebar-percent);
  width: var(--left-distance);
  box-shadow: -3px -3px 7px #fffff7, 3px 3px 5px rgba(90,100,120,.2);
  transition: left .2s ease;
  z-index: 10;
}

.layout-sidebar.active {
  left: calc(var(--left-sidebar-percent) + var(--left-distance));
}


--#

--% /np/react-antd/components/Layout/Floating/index.js
import React, { useContext } from 'react';
import { Button, Tooltip } from 'antd';
import { SketchOutlined } from '@ant-design/icons';

import './style.css';

export default ({
  active_classname,
  onClick
}) => {
  return (<div className={active_classname}>
    <Tooltip title="Toggle sidebar menu">
      <Button type="primary" shape="circle" icon={<SketchOutlined />} onClick={onClick} />
    </Tooltip>
  </div>);
}


--#

--% /np/react-antd/components/Layout/Floating/style.css
.layout-floating {
  position: fixed;
  bottom: 0px;
  left: 15px;
  width: 50px;
  height: 50px;
  transition: left .2s ease;
  z-index: 11;
}

.layout-floating.active {
  left: calc(15px + var(--left-distance));
}


--#

--% /np/react-antd/components/App/index.js
import React, { Suspense, useEffect, useState } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { hot } from 'react-hot-loader/root';

const LoginForm = React.lazy(() => import('../Login'));
import BaseLayout from '../Layout/BaseLayout';

import SessionProvider from 'context/SessionProvider';
import ToolbarContext from 'context/ToolbarContext';

import classNames from 'classnames';
import './style.css'
import AuthenticatedRoute from '../Route/AuthenticatedRoute';

const GlobalError = ({ message = 'Terjadi Kesalahan Pada Aplikasi' }) => (
  <div
    className={classNames([
      'd-flex',
      'flex-grow-1',
      'align-items-center',
      'align-content-center',
      'justify-content-center',
      'global-error',
    ])}>
  <div>{message}</div>
  </div>
)

const NotFound = () => <GlobalError message="Error 404 Not Found" />;

const FullPage = ({ message = 'Now Loading.' }) => (
  <div
      className={classNames([
        'd-flex',
        'flex-grow-1',
        'align-items-center',
        'align-content-center',
        'justify-content-center',
        'global-error',
      ])}>
      <div className="spinner-border" role="status" />
      <div>{message}</div>
  </div>
);

const App = () => {

  // useEffect(() => {
  //   SocketHandler()
  // }, []);

  const [Toolbar, setToolbar] = useState(null);

  return <SessionProvider>

    <ToolbarContext.Provider value={{
      ToolbarComponent: Toolbar,
      setToolbar,
    }}>

      <Router>
        <Suspense fallback={<FullPage />}>
          <Switch>
            <Route path="/login" exact component={LoginForm} />
            <AuthenticatedRoute path="/" component={BaseLayout} />
            <Route path="/404" exact component={NotFound} />
            <Route component={NotFound} />
          </Switch>
        </Suspense>
      </Router>

    </ToolbarContext.Provider>

  </SessionProvider>;
}

export default hot(App);


--#

--% /np/react-antd/components/App/style.css
.global-error {
  height: 100%;
}

--#

--% /np/react-antd/components/common/TabPage/index.js
import React, { useState } from 'react';
import { 
  Tabs 
} from 'antd';


const TabPage = ({
  tabs_data,
  // tabpos = 'left',
  // tabpos = 'bottom',
  tabpos = 'top',
}) => {
  return (
    <div className="card-container">
      <Tabs type="card" tabPosition={tabpos}>
        {tabs_data.map(
          (tab_page, index) => {
            let icon_title = tab_page.icon ? <span>{tab_page.icon} {tab_page.title}</span> : tab_page.title
            return <Tabs.TabPane tab={icon_title} key={index}>
              {tab_page.component}
            </Tabs.TabPane>
          }
        )}
      </Tabs>
    </div>
  );
}

export default TabPage;


--#

--% /np/react-antd/components/common/TabPage/style.css
.card-container p {
  margin: 0;
}

/* .card-container>.ant-tabs-card .ant-tabs-content {
  height: 120px;
  margin-top: -16px;
}

.card-container>.ant-tabs-card .ant-tabs-content>.ant-tabs-tabpane {
  background: #fff;
  padding: 16px;
}

.card-container>.ant-tabs-card>.ant-tabs-nav::before {
  display: none;
}

.card-container>.ant-tabs-card .ant-tabs-tab,
[data-theme='compact'] .card-container>.ant-tabs-card .ant-tabs-tab {
  border-color: transparent;
  background: transparent;
}

.card-container>.ant-tabs-card .ant-tabs-tab-active,
[data-theme='compact'] .card-container>.ant-tabs-card .ant-tabs-tab-active {
  border-color: #fff;
  background: #fff;
}

#components-tabs-demo-card-top .code-box-demo {
  background: #f5f5f5;
  overflow: hidden;
  padding: 24px;
}

[data-theme='compact'] .card-container>.ant-tabs-card .ant-tabs-content {
  height: 120px;
  margin-top: -8px;
}

[data-theme='dark'] .card-container>.ant-tabs-card .ant-tabs-tab {
  border-color: transparent;
  background: transparent;
}

[data-theme='dark'] #components-tabs-demo-card-top .code-box-demo {
  background: #000;
}

[data-theme='dark'] .card-container>.ant-tabs-card .ant-tabs-content>.ant-tabs-tabpane {
  background: #141414;
}

[data-theme='dark'] .card-container>.ant-tabs-card .ant-tabs-tab-active {
  border-color: #141414;
  background: #141414;
} */


--#

--% /np/react-antd/components/common/BoModule/BoModule.css
.custom-filter-dropdown {
  padding: 8px;
  border-radius: 6px;
  background: #fff;
  box-shadow: 0 1px 6px rgba(0, 0, 0, .2);
}

.custom-filter-dropdown input {
  width: 130px;
  margin-right: 8px;
}


--#

--% /np/react-antd/components/common/BoModule/BoModule.js
import React, { useEffect, useState } from 'react';

import { 
  Button, Drawer, Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,
  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';

import './BoModule.css';

function column_sorter(a, b, column) {
  // console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`)
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    return b[column].toLowerCase() > a[column].toLowerCase();
      
  return b[column] > a[column];
}

const BoModule = ({  
  json_data,  
  ContentComponent = null,
  close_is_reload = false,
  cacheImage = false,
  isPending = false,
  modal_title = '',
  module_title = 'Module',
  paymentReference = false,
  resource_path,
  selectionCallback = () => {},
  recordTransformer = record => record
}) => {

  const [drawerVisible, setDrawerVisible] = useState(false);
  const [table_data, set_table_data] = useState([]);
  const [filter_table_data, set_filter_table_data] = useState(null);
  const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

  const [api, contextHolder] = notification.useNotification()
  const openError = (judul, isi, placement='topRight') => {
    api.error({
      message: judul,
      description: isi,
      placement,
    });
  }
  const openSuccess = (judul, isi, placement='topRight') => {
    api.success({
      message: judul,
      description: isi,
      placement,
    });
  }

  const handleDelete = record => {
    const key = record.key;
    const table_data_temp = [...table_data].filter(item => item.key !== key);
    let column_primary = 'id';
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    }

    console.log(`berhasil hapus ${kunci}`);

    // else if (record.hasOwnProperty('orderno')) {
    //   kunci = record.orderno;
    //   column_primary = 'orderno';
    // }
    // else {
    //   console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
    //   return;
    // }

    // let _deleteUrl = `${resource_path}/${kunci}`;
    // if (delete_url_mapper.hasOwnProperty(resource_path)) {
    //   if (column_primary !== 'id') // bo/module/kv/column/kunci
    //     _deleteUrl = `${delete_url_mapper[resource_path]}/${column_primary}/${kunci}`
    //   else // bo/module/kunci
    //     _deleteUrl = `${delete_url_mapper[resource_path]}/${kunci}`
    // }
    // setDeleteUrl(_deleteUrl);
    
    // console.log(`hapus table key ${key} dari ${JSON.stringify(record)} 
    //     => resource_path: ${resource_path}
    //     => hapus: ${_deleteUrl}, jumlah baris dari ${table_data.length} ke ${table_data_temp.length}`);
    
    // if (deleteUrl === _deleteUrl) {
    //   console.log(`deleting ${deleteUrl}`);
    //   deleteResource({},
    //     () => {
    //       console.log(`berhasil hapus ${kunci}`);
    //       set_table_data(table_data_temp);
    //       getResourceData({}, successHandler);
    //       openSuccess('Berhasil', `Berhasil hapus id ${kunci}`);
    //     },
    //     err => {
    //       console.log(`gagal hapus ${kunci}`);
    //       openError('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
    //     }
    //   );
    // } else {
    //   console.log(`NOT+RE deleting ${deleteUrl} as ${_deleteUrl}`);
    //   deleteResource(
    //     {
    //       url: useUrlBuilder(_deleteUrl)
    //     },
    //     () => {
    //       console.log(`berhasil hapus ${kunci}`);
    //       set_table_data(table_data_temp);
    //       getResourceData({}, successHandler);
    //       openSuccess('Berhasil', `Berhasil hapus ${column_primary} ${kunci}`);
    //     },
    //     err => {
    //       console.log(`gagal hapus ${kunci}`);
    //       openError('Gagal hapus...', `Tidak berhasil hapus ${column_primary} ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
    //     }
    //   );
    // }   
  }

  const table_header = json_data.headers.map((column, index) => {

    if (column === "") {
      return {
        title: "Show",
        fixed: 'left',
        width: 100,
        render: data => <Button onClick={() => {
          set_modal_bomodule_content(data);
          setDrawerVisible(true);
        }}>Show </Button>,
      };

    } else if (column === "delete") {
      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: 60,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {
      
      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? 75 : 150,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  // const modalSelectionHandler = (selections) => {
  //   set_modal_bomodule_selected(selections)
  //   // set_modal_bomodule(true)
  //   // selection bisa kosong jk dia unselect
  //   if (selectionCallback !== undefined) {            
  //     // kirim id dari record, bukan index selection
  //     let id_list = []
  //     selections.forEach(index => {
  //       let ketemu = table_data.find(record => record.key == index);
  //       if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
  //         id_list .push(ketemu.id + "," + ketemu.id_user);
  //       else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
  //         id_list .push(ketemu.orderno + "," + ketemu.customerno);
  //     })
  //     if (id_list.length > 0) {
  //       selectionCallback(id_list);
  //       console.log(`selection ${id_list}`);
  //     }
  //   }
  //   console.log(`bomodule selected: ${selections}, ${typeof(selections)}, siap masuk cc: ${modal_bomodule_selected}.`)
  // }

  function searchTable(value) {
    let saring = table_data.filter(o =>
      Object.keys(o).some(k =>
        String(o[k])
          .toLowerCase()
          .includes(value.toLowerCase())
      )
    )
    set_filter_table_data(saring);
  }

  const getResourceData = useAxios({ url: resource_path, });
  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  }

  useEffect(() => {
    getResourceData({}, successHandler);
  }, []);

  return <>
    <Table
      size="small"
      columns={[
        {
          title: '',
          key: 1,
          dataIndex: 'action',
          width: '50px',
          render: () => <Button icon={<ReloadOutlined />} 
            onClick={() => {
            set_filter_table_data(table_data)
            getResourceData({}, successHandler)
            }}>
              Reload
            </Button>
        },

        {
          title: '',
          key: 2,
          dataIndex: 'action',
          width: '200px',
          render: () => <Input.Search 
            style={{ margin: "0 20px 0 0" }}
            placeholder="Cari lalu tekan Enter..."
            enterButton
            onSearch={searchTable}
            />
        },
      ]}
      dataSource={[{key:0}]}
      pagination={false}
      />

    <SimpleTable 
      header={table_header} 
      body={filter_table_data === null ? table_data : filter_table_data} 
      selectCallback={modalSelectionHandler} />

    {contextHolder}
  </>;
}

export default BoModule;


--#

--% /np/react-antd/components/common/Table/SimpleTable.js
import React, { useState } from 'react';
import { Table } from 'antd';

const SimpleTable = ({
  header,
  body,
  selectCallback = null,
  tableSelection = true,
}) => {

  const [selectedRows, setSelectedRows] = useState([])

  // ini peroleh semua yg terselect
  const rowSelection = {
    selectedRows,
    onChange: (pilihan) => {
      setSelectedRows(pilihan)
      // console.log(`#1 selection now: ${selectedRows} dg ${pilihan}`)
      if (selectCallback) selectCallback(pilihan)
    }
  }

  const modifySelection = (record) => {
    // selectedRows.length > 0 ? [...selectedRows] : []
    const newrows = [...selectedRows]; 
    if (newrows.indexOf(record.key) >= 0) {
      newrows.splice(newrows.indexOf(record.key), 1);
    } else {
      newrows.push(record.key);
    }
    setSelectedRows(newrows);
    console.log(`#2 selection now: ${selectedRows} dg ${newrows}`);
  }
  
  // ini row yg diklik (1 saja)
  const onRowSelection = (record) => ({
      onClick: () => {
        // console.log(`something is being clicked ${JSON.stringify(record)}`)
        modifySelection(record);
        // console.log(`selected: ${selectedRows}`)
      }
  })

  if (tableSelection) {
    return <Table
      bordered      
      columns={header}
      dataSource={body}
      rowSelection={rowSelection}
      size='small'
      scroll={{ x: 1500, y: 300 }}
      // scroll={{ y: 240 }}
      // components={components}
      // pagination={{ position: ['topLeft', 'bottomRight'], pageSize: 10 }}
      pagination={{ position: ['topLeft', 'bottomRight'] }}
      // pagination={{ position: 'both', pageSize: 10 }}
      
      // onRow={onRowSelection}
    >
    </Table>;
  } else {
    return (<Table columns={header} dataSource={body} />);
  }
}

export default SimpleTable;


--#

--% /np/react-antd/components/context/ToolbarContext.js
import React from 'react';

const ToolbarContext = React.createContext({
});

export default ToolbarContext;


--#

--% /np/react-antd/components/context/SessionProvider.js
import React, { useState, useEffect } from 'react';
import { hot } from 'react-hot-loader/root';
import SessionContext from './SessionContext';

const sessionName = `shut-the-fuck-up`;

const SessionProvider = ({ children }) => {

  // ini bikin token yg sdh ada, masuk di initial state
  // sewaktu nilai lain null/false
  // maka, AuthenticatedRoute hrs berbasis authenticated instead of token
  const initializedToken = localStorage.getItem(sessionName) || null;
  const [state, setState] = useState({
    authenticated: false,
    token: initializedToken,

    username: null,
    email: null,
    role: null,
    phone: null,
  });

  useEffect(() => {
    if (state.token !== initializedToken) {
      localStorage.setItem(sessionName, state.token);
    }
  }, [state.token]);

  const sessionLogout = () => {
    
    localStorage.removeItem(sessionName);
    let terhapus = localStorage.getItem(sessionName);
    console.log(`logging out locally...pastikan sudah null [${terhapus}].`);
    // setState({ token: null, });
    setState({});

  };

  return (
  <SessionContext.Provider
    value={{
      ...state,
      setSession: setState,
      sessionLogout,
    }}>
    {children}
  </SessionContext.Provider>
  );
};

export default hot(SessionProvider);


--#

--% /np/react-antd/components/context/SessionContext.js
import React from 'react';

const SessionContext = React.createContext({
  authenticated: false,
  token: null,

  email: null,
  username: null,
  phone: null,
  role: null,

  data: [],
  setSession: () => {},
});

export default SessionContext;


--#

--% /np/react-antd/components/Route/AuthenticatedRoute.js
import React, { useContext } from 'react';
import {
  Route,
  Redirect
} from 'react-router-dom';

import SessionContext from '../context/SessionContext';

export default ({
  name,
  path,
  exact = false,
  component: Component,
  // roles = [],
}) => {

  const session = useContext(SessionContext);

  return (
    <Route
      path={path}
      name={name}
      exact={exact}
      render={(props) => 
        // session.authenticated
        session.token
          ? (<Component {...props} />)
          : (<Redirect
            to={{
              pathname: '/login',
              state: { from: props.location },
            }}
          />)
      }
    />
  );
};


--#

--% /np/react-antd/components/Menu/Shortcut.js


--#

--% /np/react-antd/components/Menu/index.js
export { default as Menu } from './MainMenu';


--#

--% /np/react-antd/components/Menu/MainMenu.js
import React, { useEffect, useState } from 'react';

// import { useHistory } from 'react-router-dom';
// import { useHistory } from 'react-router';
import { withRouter } from 'react-router-dom';

import { Switch, Menu, Button } from 'antd';
import {
  AppstoreOutlined,
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  PieChartOutlined,
  DesktopOutlined,
  ContainerOutlined,
  MailOutlined,
} from '@ant-design/icons';

import MenuJson from 'assets/menu.json';
import './MainMenu.css';


const { SubMenu } = Menu;

const MainMenu = ({
  history,
  toggler,
  rootMenu=null,
}) => {
  // let history = useHistory();
  // const [theme, setTheme] = useState('dark')
  // const toggleTheme = (value) => setTheme(value ? 'dark' : 'light');

  function handleClick(e) {
    // console.log('click ', e, 'atau: props.link nya', e.item.props.link);
    if (e.item.props.link !== undefined) {
      history.push('/' + e.item.props.link);
      toggler();
    }
  }

  let counter=0;
  let CreateMenu = (parent, level=0) => {
    return parent.map( (item, index) => {
      // console.log(`oprek ${JSON.stringify(item)} level=${level} key=${level}-${index}-${counter}`)
      counter +=1;
      if (item.hasOwnProperty("children")) {
        return <SubMenu key={`${level}-${index}-${counter}`} icon={<AppstoreOutlined />} title={item.label}>
            
          {CreateMenu(item.children, level+1)}

        </SubMenu>
      } else {
        return <Menu.Item key={`${level}-${index}-${counter}`} icon={<PieChartOutlined />} link={item.link}>{item.label}</Menu.Item>;
      }
    });
  }

  let NewReturn = () => (
    <div className="menu-component">
      <Menu
        defaultSelectedKeys={['1']}
        defaultOpenKeys={['1-0-0']}        
        // theme={theme}
        // mode="inline"
        // inlineCollapsed={this.state.collapsed}
        // onClick={this.handleClick}
        onClick={handleClick}
      >

      {CreateMenu(rootMenu ? rootMenu : MenuJson)}

      </Menu>
    </div>
  );
  return <NewReturn />;
}

// export default MainMenu;
export default withRouter(MainMenu);


--#

--% /np/react-antd/components/Menu/MainMenu.css
.menu-component {
  width: 100%;
  font-size: .5rem;
}

--#

--% /np/react-antd/components/Login/login.css

.login-container-div {
  width: 400px;
  height: 250px;

  margin: 150px auto;
  padding: 15px;

  background-color: rgba(33, 3, 248, .5);
  border-radius: 10px;

  box-shadow: 10px 15px 18px #888888;
}

--#

--% /np/react-antd/components/Login/index.js
import React, { Suspense, useContext, useEffect, useRef, useState } from 'react';
import { 
  Button, 
  Checkbox,
  Form, 
  Input,   
  notification,
} from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';
import SessionContext from '../context/SessionContext';
import './login.css';

import useAxios from '#/utils/useAxios';
import config from '#/config';

const LoginForm = (props) => {

  const session = useContext(SessionContext);

  const [api, contextHolder] = notification.useNotification();
  const openNotification = (judul, isi, placement='bottomRight') => {
    api.error({
      message: judul,
      description: isi,
      placement,
    });
  };

  const loginAxios = useAxios(config.backend.paths.login);
  // const mounted = useRef();

  useEffect(
    function() {
      // if (!mounted.current) {
      //   if (props.history) {
      //     if (session.authenticated) {
      //       console.log('User is authenticated...');
      //       props.history.push('/');
      //     }
      //   }
      // }

      if (session.authenticated) {
        console.log('User is authenticated...');
        props.history.push('/');
      }

    },
    [session]
    // []
  );

  const onFinish = values => {

    console.log(`Data utk login: ${JSON.stringify(values)}`);

    loginAxios(
      { 
        data: {
          email: values.email,
          password: values.password,
        }
      },

      response => {
        let { token: mainToken, ...responseData } = response.data;
        let sessionData = {
          authenticated: true,
          token: mainToken && mainToken !== "" ? mainToken : responseData.jwt.accessToken,
          ...responseData
        }
        session.setSession(sessionData);
        console.log(`sukses login: ${JSON.stringify(sessionData)}`);
        // props.history.push('/');
      },

      error => {
        let isi = JSON.stringify(error);
        console.log(`gagal login: ${isi}`);
        openNotification(`gagal login`, isi);
      },

    );
  };

  return (<div className="login-container-div">
    <Form
      name="normal_login"
      className="login-form"
      initialValues={{
        remember: true,
      }}
      onFinish={onFinish}>

      <Form.Item
        name="email"
        rules={[
          {
            required: true,
            message: 'Please input your Email!',
          },
        ]}>

        <Input 
          prefix={<UserOutlined className="site-form-item-icon" />} 
          placeholder="Email" />

      </Form.Item>

      <Form.Item
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your Password!',
          },
        ]}>

        <Input
          prefix={<LockOutlined className="site-form-item-icon" />}
          type="password"
          placeholder="Password"
        />

      </Form.Item>

      <Form.Item>
        
        <Form.Item name="remember" valuePropName="checked" noStyle><Checkbox>Remember me</Checkbox></Form.Item>
        <a className="login-form-forgot" href="">Forgot password</a>

      </Form.Item>

      <Form.Item>
        
        <Button type="primary" htmlType="submit" className="login-form-button">Log in</Button>
        {' '} Or <a href="">register now!</a>

      </Form.Item>

    </Form>

    {contextHolder}

  </div>);
}

export default LoginForm;


--#

--% /np/react-antd/utils/useAxios.js
import React, { useState, useContext } from 'react';

import axios from 'axios';
import config from '#/config';

const initialState = {
  isFetching: false,
  isError: false,
  // statusCode: null,
  // code: null,
  // message: null,
  // details: null,
  data: null,
}

export default ({
  method = 'GET',
  path,
  headers = {},
}) => {

  const [state, setState] = useState(initialState);

  if (path === undefined) path = '';
  const url = `${config.server()}/${path}`;

  const originalArgs = {
    method,
    url,
    data: null,
    params: {},
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      ...headers,
    }
  }

  const sender = (newArgs={}, successCb=undefined, errorCb=undefined) => {    

    let updatedArgs = {
      ...originalArgs,
      ...newArgs,
    };
    if (newArgs.hasOwnProperty('path')) {
      updatedArgs['url'] = `${config.server()}/${newArgs["path"]}`;
    }
    console.log(`useAxios: sending request to => ${url}.`);

    setState({
      ...initialState,
      isFetching: true,
    });

    axios(updatedArgs)
    .then(response => {
      if (response.data) {
        
        setState(prevState => ({
          ...prevState,
          data: response.data,
        }));

        if (successCb) {
          successCb(response.data);
        }

      }
    })
    .catch(error => {
      console.log(`useAxios: catch error => ${JSON.stringify(error)}.`);
      
      setState(prevState => ({
        ...prevState,
        isError: true,
      }));

      if (errorCb) {
        errorCb(error);
      }

    })
    .then(() => {
      
      setState({
        ...initialState,
        isFetching: false,
      });

    });
  }
  
  return sender;
}

--#
