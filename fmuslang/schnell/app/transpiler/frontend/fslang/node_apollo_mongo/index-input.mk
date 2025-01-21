--% index/fmus
node-apollo-mg,d(/mk)
  %utama=__FILE__
__TEMPLATE_DB_INIT
__TEMPLATE_APP_INIT
  readme.md,f(e=utama=/node-apollo-template/readme.md)
  .env,f(e=utama=/node-apollo-template/.env)  
  .babelrc,f(e=utama=/node-apollo-template/.babelrc)  
  src,d(/mk)
    index.js,f(e=utama=/node-apollo-template/index.js)
    app.js,f(e=utama=/node-apollo-template/app.js)
    run.sh,f(e=utama=/node-apollo-template/run.sh)
    $*chmod a+x *.sh
    core,d(/mk)
      config,d(/mk)
        environ.js,f(e=utama=/node-apollo-template/core/config/environ.js)
      connection,d(/mk)
        db,d(/mk)
          index.js,f(e=utama=/node-apollo-template/core/connection/db/index.js)
        graphql,d(/mk)
          index.js,f(e=utama=/node-apollo-template/core/connection/graphql/index.js)
      routes,d(/mk)
        index.js,f(e=utama=/node-apollo-template/core/routes/index.js)
      middlewares,d(/mk)
        index.js,f(e=utama=/node-apollo-template/core/middlewares/index.js)
      errors,d(/mk)
        index.js,f(e=utama=/node-apollo-template/core/errors/index.js)
      logger,d(/mk)
        index.js,f(e=utama=/node-apollo-template/core/logger/index.js)
        response.js,f(e=utama=/node-apollo-template/core/logger/response.js)
        request.js,f(e=utama=/node-apollo-template/core/logger/request.js)
    apps,d(/mk)
      user,d(/mk)
        user.service.js,f(e=utama=/node-apollo-template/apps/user/user.service.js)
        index.js,f(e=utama=/node-apollo-template/apps/user/index.js)
        user.model.js,f(e=utama=/node-apollo-template/apps/user/user.model.js)
        user.controller.js,f(e=utama=/node-apollo-template/apps/user/user.controller.js)
__TEMPLATE_SERVER_APP_CONTENT

  # $*qterminal 2>/dev/null &
--#

--% /node-apollo-template/readme.md

/*
query hello {
  hello
}

query list {
  users {
    id
    name
    email
    mobile
    suspend_status
  }
}

mutation create {
  user_create(data: {
    id:"10"
    name:"monyong"
    email:"monyong@gmail.com"
    mobile:"rotterdam"
    suspend_status:true
  }) {
    id
    name
  }
}

mutation update {
  user_update(id:"3", data: {
    name:"gaia luv luv"
  }) {
    affectedRows
    user {
      id
      name
      email
      mobile
    }
  }
}

mutation delete {
  user_delete(id:"10") {
    affectedRows
  }
}
*/

yarn add @babel/core @babel/node @babel/preset-env @elastic/elasticsearch apollo-server apollo-server-express babel-node body-parser commander compression cookie-parser cors dataloader dotenv express express-graphql express-request-id graphql graphql-iso-date graphql-resolvers helmet jsonwebtoken lodash moment node-webhooks path pg pg-hstore response-time sequelize sequelize-cli typeorm winston winston-daily-rotate-file winston-elasticsearch winston-sentry
yarn add --dev apidoc buddy.js chai chai-http commitizen cz-conventional-changelog docdash eslint eslint-config-airbnb eslint-config-prettier eslint-plugin-import eslint-plugin-prettier faker husky jsdoc lint-staged mocha nodemon nyc prettier sinon supertest
yarn add babel-plugin-module-resolver
yarn add @elastic/elasticsearch@^7.7.1 winston-elasticsearch@^0.7.0
alias nodemon="/home/usef/tmp/node_modules/.bin/nodemon"

term
gen
--#

--% /node-apollo-template/.env
# Node Server Configuration
NODE_ENV=development
APP_NAME='Node_API'
PORT=9015
THROTTLE_LIMIT=1500
PREFIX=http://
DOMAIN=api.test
TZ='Asia/Jakarta'

# File storage path
FS_PATH=/tmp

# Mail server configuration
SMTP_HOST=localhost
SMTP_SECURE=false
SMTP_IGNORETLS=true
SMTP_PORT=1025
SMTP_USER=notifications@api.test
SMTP_AUTH_USER=api/api-dev
SMTP_AUTH_PASS='sfsff'

# PG database configuration connection settings
PG_DB="postgres://__TEMPLATE_DBUSER:__TEMPLATE_DBPASS@__TEMPLATE_DBHOST:__TEMPLATE_DBPORT/__TEMPLATE_DBNAME"
DB_SYNC=1

#Elastic Search Configuration
ES_URL=http://localhost:9200
ES_USER=elastic
ES_PASS=changeme

SENTRY_DSN=''
ENABLE_ES='false'
ENABLE_SENTRY='false'
--#

--% /node-apollo-template/index.js
module.exports = require('./app');
// import App from './app';

--#

--% /node-apollo-template/.babelrc
{
  "presets": [
    "@babel/preset-env"
  ],
  "plugins": [
    [
      "module-resolver",
      {
        "root": [
          "."
        ],
        "alias": {
          "S": "./",
          "C": "./core",
          "A": "./apps",
          "AU": "./apps/user",
          "F": "./core/config",
          "N": "./core/connection",
          "DB": "./core/connection/db",
          "G": "./core/connection/graphql",
          "E": "./core/errors",
          "L": "./core/logger",
          "M": "./core/middlewares",
          "R": "./core/routes",
          "U": "./core/utils"
        }
      }
    ]
  ]
}

--#

--% /node-apollo-template/app.js
const path = require('path');
const express = require('express');
const http = require('http');

// console.log(`lokasi: ${path.resolve(process.cwd())}`);
import graphqlServer from 'G';
import config from 'F/environ';
import db from 'DB';
import logger from 'L';
import middlewares from 'M';
import routes from 'R';

const app = express();
graphqlServer(app);
const server = http.createServer(app);
middlewares(app);
routes(app);

function startServer() {
  app.angularFullstack = server.listen(config.port, config.ip, () => {
    // eslint-disable-next-line no-console
    console.log(
      'Server listening on %d, in %s mode',
      config.port,
      app.get('env'),
    );
  });
}

process.on('unhandledRejection', (reason, p) => {
  logger.error('Unhandled Rejection at: Promise', p, 'reason:', reason);
});

process.on('uncaughtException', (err) => {
  logger.error('uncaughtException', err);
});

function startDBAndServer(
  ) {
  db.sequelizeDB
    .authenticate()
    .then(() => {
      startServer();
    })
    .catch((err) => {
      // eslint-disable-next-line no-console
      console.log('Server failed to start due to error: %s', err);
    });
}

startDBAndServer();

module.exports = app;

--#

--% /node-apollo-template/run.sh
# alias nodemon="/home/usef/tmp/node_modules/.bin/nodemon"
clear && nodemon --exec babel-node index.js

--#

--% /node-apollo-template/core/config/environ.js
/* eslint no-process-env:0 */
const path = require('path');
const dotenv = require('dotenv');
const _ = require('lodash');

const root = path.normalize(`${__dirname}/../..`);
const env = dotenv.config({ path: path.join(root, '.env') }).parsed;
const { DOMAIN, PREFIX } = env;

const all = {
  env: env.NODE_ENV,
  root,
  port: process.env.PORT || 3302,
  ip: process.env.IP || '0.0.0.0',
  URLS_API: `${PREFIX}api.${DOMAIN}`
};

module.exports = _.merge(
  all,
  env,
);

--#

--% /node-apollo-template/core/connection/db/index.js
const path = require('path');
const fs = require('fs');
const _ = require('lodash');
const Sequelize = require('sequelize');

const config = require('F/environ');
const logger = require('L');

const sqlDefaults = {
  dialect: 'postgres',
  timezone: '+05:30',
  logging:
    config.NODE_ENV === 'development' ? (str) => logger.debug(str) : false,
  dialectOptions: {
    connectTimeout: 20000,
  },
};

const db = {
  Sequelize,
  sequelizeDB: new Sequelize(config.PG_DB, sqlDefaults),
};

const appdir = path.resolve(config.root, 'apps')
fs.readdirSync(appdir).forEach(appname => {
  const fullpath = path.resolve(appdir, appname, `${appname}.model`);
  const Appname = _.startCase(appname);
  const model = require(fullpath)(db.sequelizeDB, Sequelize.DataTypes);
  db[Appname] = model;
});

Object.keys(db).forEach((modelName) => {
  if ('associate' in db[modelName]) {
    db[modelName].associate(db);
  }
});

if (parseInt(config.DB_SYNC) === 1) {
  console.log(`<< begin syncing...`);
  db.sequelizeDB.sync({ false: true });
  console.log(`...syncing end >>`);
}

module.exports = db;

--#

--% /node-apollo-template/core/connection/graphql/index.js
import { ApolloServer, gql } from 'apollo-server-express';
import { User as UserModel } from 'DB';
__TEMPLATE_APPS_IMPORTS__

const userType = gql`
  type User {
    id: ID
    name: String
    email: String
    mobile: String
    suspend_status: Boolean
    updated_by: Int
    created_by: Int
    deleted_by: Int
  }

  extend type Query {
    helloUser: String!
    users: [User]
    user(id: ID!): User
  }

  input UserCreateInput {
    id: ID!
    name: String!
    email: String!
    mobile: String
    suspend_status: Boolean
    updated_by: Int
    created_by: Int
    deleted_by: Int
  }

  input UserUpdateInput {
    name: String
    email: String
    mobile: String
    suspend_status: Boolean
    updated_by: Int
    created_by: Int
    deleted_by: Int
  }

  type UserDeleteResult {
    affectedRows: Int
  }

  type UserUpdateResult {
    affectedRows: Int
    user: User
  }
  
  extend type Mutation {		
    user_create(data: UserCreateInput!): User
    user_update(id: ID!, data: UserUpdateInput!): UserUpdateResult
    user_delete(id: ID!): UserDeleteResult
  }
`;

const userResolver = {

  Query: {
    helloUser: () => 'hi user!',

    user: (root, {id}) => {
      return userService.getUserDetail(id);
    },
    users: async (root, args) => {
      // const users = await userService.getUserList();
      const users = await UserModel.findAll();
      return users || [];
    },
  },

  Mutation: {
    user_create: async (_, {data}) => {
      const user = await UserModel.create(data);
      return user;
    },

    user_update: async (_, {id, data}) => {
      const result = await UserModel.update(
        data,
        {
          // https://stackoverflow.com/questions/38524938/sequelize-update-record-and-return-result
          returning: true,
          where: { id } 
        }
      );
      // console.log(`kembalian user_update:`, JSON.stringify(result));
      return {
        affectedRows: result[0],
        user: result[1][0]
      };
    },

    user_delete: async (_, {id}) => {
      const deleteResult = await UserModel.destroy({
        where: { id }
      });
      // https://stackoverflow.com/questions/43735418/sequelize-how-to-return-destroyed-row
      // https://github.com/sequelize/sequelize/issues/4124
      // console.log(`hasil hapus:`, deleteResult, typeof(deleteResult));
      return deleteResult;
    },
  }

}

const queryTypes = gql`
  type Query {
    _: Boolean
  }

  type Mutation {
    _: Boolean
  }
`;

const typeDefs = [queryTypes, userType, __TEMPLATE_APPS_TYPEDEFS_LIST__];
const resolvers = [userResolver, __TEMPLATE_APPS_RESOLVERS_LIST__];

const server = new ApolloServer({
  typeDefs, resolvers
});

export default (app) => {
  server.applyMiddleware({ app });
}

--#

--% /node-apollo-template/core/routes/index.js
const { name, version } = { name: "node-apollo-template", version: "0.0.1"};
const errors = require('E');
const logger = require('L');
const { requestLogger } = require('L/request');
const responseLogger = require('L/response');
const path = require('path');
const fs = require('fs');
const config = require('F/environ');

const INTERNAL_SERVER_ERROR = 500;
const NOT_FOUND = 404;

export default function routes(app) {

  app.use(requestLogger);
  app.use(responseLogger());

  app.get('/api/health', (req, res) => res.json({ id: req.id, name, version }));

  const appdir = path.resolve(config.root, 'apps')
  fs.readdirSync(appdir).forEach(appname => {
    const fullpath = path.resolve(appdir, appname);
    const pathname = appname + 's';
    app.use(`/api/${pathname}`, require(fullpath));
  });

  app.use((e, req, res, next) => {
    logger.error(`ERROR: ${e.message}`, {
      processingTime    : res.get('X-Response-Time'),
      url               : req.originalUrl,
      stackTrace        : e.stack,
      method            : req.method,
      requestHeader     : req.headers,
      params            : req.params,
      body              : req.body,
      query             : req.query,
    });

    return res
      .status(e.statusCode || e.code || INTERNAL_SERVER_ERROR)
      .json({ message: e.message, stack: e.stack });
  });

  app
    .route('/:url(api|auth|components|app|bower_components|assets)/*')
    .get(errors[NOT_FOUND]);
};

--#

--% /node-apollo-template/core/middlewares/index.js
const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const cors = require('cors');
const compression = require('compression');
const cookieParser = require('cookie-parser');
const responseTime = require('response-time');
const helmet = require('helmet');
const addRequestId = require('express-request-id')();

// const db = require('../conn/sqldb');
const config = require('F/environ');


module.exports = (app) => {
  const env = app.get('env');

  if (env === 'development' || env === 'test') {
    app.use(express.static(path.join(config.root, '.tmp')));
  }
  app.use(addRequestId);
  app.use(helmet());
  app.use(responseTime());
  app.use(cors());
  app.use(compression());
  app.use(cookieParser());
  app.use(bodyParser.urlencoded({ extended: false }));
  app.use(bodyParser.json({ limit: '50mb' }));

  Object.assign(app, { express });
};

--#

--% /node-apollo-template/core/errors/index.js
const NOT_FOUND = 404;
module.exports[NOT_FOUND] = function pageNotFound(req, res) {
  res.status(NOT_FOUND).json({ error: 'Not found', status: NOT_FOUND });
};
--#

--% /node-apollo-template/core/logger/index.js
const winston = require('winston');
const DailyRotateFile = require('winston-daily-rotate-file');
// const Elasticsearch = require('winston-elasticsearch');
const { ElasticsearchTransport } = require('winston-elasticsearch');
const { Client } = require('@elastic/elasticsearch');
const Sentry = require('winston-sentry');

const {
  NODE_ENV,
  ES_URL,
  ES_USER,
  ES_PASS,
  SENTRY_DSN,
  ENABLE_ES,
  ENABLE_SENTRY
} = require('F/environ');

if (ENABLE_ES === 'true') {
  const client = new Client({
    node: ES_URL,
    auth: {
      username: ES_USER,
      password: ES_PASS,
    },
  });
}

const esTransportOpts = {
  client: NODE_ENV === 'production' && client,
  clientOpts: { node: ES_URL },
  silent: ENABLE_ES === 'false',
  level: 'info'
};

const logger = winston.createLogger({
  transports: [
    new DailyRotateFile({
      datePattern: 'YYYY-MM-DD',
      filename: `/tmp/error.%DATE%.log`,
      level: 'error',
      maxFiles: '10d',
      silent: NODE_ENV === 'test',
    }),
    // new Elasticsearch({
    //   client: NODE_ENV === 'production' && client,
    //   level: 'info',
    //   silent: ENABLE_ES === 'false',
    // }),
    new ElasticsearchTransport(esTransportOpts),
    new Sentry({
      dsn: NODE_ENV === 'production' && SENTRY_DSN,
      install: true,
      config: { environment: NODE_ENV, release: '@@_RELEASE_' },
      level: 'warn',
      silent: ENABLE_SENTRY === 'false',
    }),
    new winston.transports.Console({
      name: 'console',
      level: 'debug',
      silent: NODE_ENV === 'production',
    }),
  ],
});

module.exports = logger;

--#

--% /node-apollo-template/core/logger/response.js
const logger = require('./index');
const { APP_NAME } = require('F/environ');

module.exports = function responseLogger() {
  return (req, res, next) => {
    res.on('finish', () => {
      logger.info(`RESPONSE INFO: ${res.get('X-Request-Id')}`, {
        startTime           : new Date(),
        requestId           : res.get('X-Request-Id'),
        url                 : req.originalUrl,
        method              : req.method,
        requestHeader       : req.headers,
        responseHeader      : res.headers,
        responseBody        : res.body,
        requestParams       : req.params,
        requestBody         : req.body,
        requestQuery        : req.query,
        appName             : APP_NAME,
      });
    });

    next();
  };
};

--#

--% /node-apollo-template/core/logger/request.js
const logger = require('./index');
const { APP_NAME } = require('F/environ');

const requestLogger = (req, res, next) => {
  logger.info(`REQUEST INFO: ${req.id}`, {
    startTime           : new Date(),
    requestId           : req.id,
    url                 : req.originalUrl,
    method              : req.method,
    requestHeader       : req.headers,
    requestParams       : req.params,
    requestBody         : req.body,
    requestQuery        : req.query,
    appName             : APP_NAME,
  });
  next();
};

module.exports = {
  requestLogger,
};

--#

--% /node-apollo-template/apps/user/user.service.js
const { User } = require('DB');

const checkDuplicate = (email) =>
  User.findOne({
    attributes: ['id'],
    where: { email },
    raw: true,
  }
);

async function signup(body) {
  try {
    const { id = null, name, email: e, actingUser = null, mobile } = body;

    const email = e && e.trim();
    // - Todo: Email Validation
    const found = await checkDuplicate(email);

    if (found) {
      return {
        code: 409,
        id: found.id,
        message: 'Duplicate',
      };
    }

    const user = {
      id,
      name,
      email,
      created_by: actingUser,
      mobile,
    };

    await User.upsert(user);

    return { code: 201, id: user.id };
  } catch (err) {
    return Promise.reject(err);
  }
}

module.exports = {
  signup,
};

--#

--% /node-apollo-template/apps/user/index.js
const express = require('express');
const controller = require('./user.controller');

const router = express.Router();

router.get('/', controller.index);
router.get('/:id', controller.getUser);
router.post('/', controller.create);
router.put('/:id', controller.update);

module.exports = router;

--#

--% /node-apollo-template/apps/user/user.model.js
// const { USER_ROLES } = require('../../config/buckets');

const Fields = (DataTypes) => ({
  id: {
    type: DataTypes.INTEGER,
    autoIncrement: false,
    primaryKey: true,
    allowNull: false,
    unique: true,
  },
  name: DataTypes.STRING,
  // username: DataTypes.STRING,
  // password: DataTypes.STRING,
  // role: {
  //   type: DataTypes.STRING,
  // },
  email: DataTypes.STRING,
  mobile: DataTypes.STRING,
  suspend_status: {
    type: DataTypes.BOOLEAN,
    defaultValue: false,
  },
  updated_by: DataTypes.INTEGER,
  created_by: DataTypes.INTEGER,
  deleted_by: DataTypes.INTEGER,
});

module.exports = (sequelize, DataTypes) => {
  const User = sequelize.define(
    'User', 
    Object.assign(Fields(DataTypes)), 
    {
      tableName: 'users',
      timestamps: true,
      underscored: true,
      paranoid: true,
      createdAt: 'created_on',
      updatedAt: 'updated_on',
      deletedAt: 'deleted_on',
    }
  );

  // User.associate = (db) => {};

  User.getUser = (db, Id) =>
    db.User.findOne({
      // attributes: ['name', 'email'],
      where: {
        id: Id,
      },
      order: [['id', 'asc']],
      limit: 1,
    });

  return User;
};

--#

--% /node-apollo-template/apps/user/user.controller.js
const service = require('./user.service');
const db = require('DB');

const messagesMap = {
  201: 'Your account created successfully.',
  409: 'Duplicate',
};

const { User } = db;

async function create(req, res, next) {
  try {
    const status = await service.signup(req.body);

    return res.json({ message: messagesMap[status.code], id: status.id });
  } catch (err) {
    return next(err);
  }
}

async function index(req, res, next) {
  try {
    const limit = 100;
    const offset = 0;

    const users = await User.findAll({
      limit,
      offset,
    });

    return res.json(users);
  } catch (err) {
    return next(err);
  }
}

async function getUser(req, res, next) {
  try {
    const user = await User.findOne({
      // attributes: ['id', 'mobile', 'name', 'email'],
      where: { id: req.params.id },
      raw: true,
    });
    return res.json(user);
  } catch (err) {
    return next(err);
  }
}

async function update(req, res, next) {
  const SUCCESS = 200;
  try {
    await User.update(
      {
        ...req.body,
      },
      {
        where: {
          id: req.params.id,
        },
      },
    );
    return res.sendStatus(SUCCESS);
  } catch (err) {
    return next(err);
  }
}

module.exports = {
  create,
  index,
  getUser,
  update,
};

--#

--% /node-apollo-template/package.json
{
	"name": "np",
	"version": "1.0.0",
	"main": "index.js",
	"license": "MIT",
	"scripts": {
		"test": "jest",
		"coverage": "jest --coverage",
		"apo1": "rm -rf apollo-dist && webpack serve --mode development --config webpack-apollo-template",
		"apo2": "node ./apollo-dist/index.js",
		"start": "node ./dist/server.js"
	},
	"dependencies": {
		"@babel/node": "^7.14.7",
		"@elastic/elasticsearch": "^7.7.1",
		"@emotion/react": "^11.4.0",
		"@emotion/styled": "^11.3.0",
		"@fortawesome/fontawesome-free": "^5.15.3",
		"@fortawesome/fontawesome-svg-core": "^1.2.35",
		"@fortawesome/free-brands-svg-icons": "^5.15.3",
		"@fortawesome/free-regular-svg-icons": "^5.15.3",
		"@fortawesome/free-solid-svg-icons": "^5.15.3",
		"@fortawesome/react-fontawesome": "^0.1.14",
		"@material-ui/core": "^4.11.4",
		"@material-ui/icons": "^4.11.2",
		"@material-ui/styles": "^4.11.4",
		"@reduxjs/toolkit": "^1.5.1",
		"@themesberg/react-bootstrap": "^1.4.1",
		"antd": "^4.15.5",
		"apollo-server": "^2.25.2",
		"apollo-server-express": "^2.25.2",
		"axios": "^0.21.1",
		"babel-node": "^0.0.1-security",
		"babel-plugin-module-resolver": "^4.1.0",
		"bcrypt": "^5.0.1",
		"body-parser": "^1.19.0",
		"bootstrap": "^5.0.1",
		"chart.js": "2.9.4",
		"chartist": "^0.11.4",
		"chartist-plugin-tooltips-updated": "^0.1.4",
		"classnames": "^2.3.1",
		"commander": "^8.0.0",
		"compression": "^1.7.4",
		"cookie-parser": "^1.4.5",
		"copy-webpack-plugin": "^9.0.0",
		"core-js": "^3.12.1",
		"dataloader": "^2.0.0",
		"express": "^4.17.1",
		"express-graphql": "^0.12.0",
		"express-request-id": "^1.4.1",
		"font-awesome": "^4.7.0",
		"formik": "^2.2.7",
		"graphql": "^15.5.1",
		"graphql-iso-date": "^3.6.1",
		"graphql-resolvers": "^0.4.2",
		"jsonwebtoken": "^8.5.1",
		"lodash": "^4.17.21",
		"moment": "^2.29.1",
		"mongoose": "^5.12.9",
		"mongoose-unique-validator": "^2.0.3",
		"node-webhooks": "^1.4.2",
		"path": "^0.12.7",
		"pg": "^8.6.0",
		"pg-hstore": "^2.3.4",
		"prism-react-renderer": "^1.2.1",
		"pubsub-js": "^1.9.3",
		"rand-token": "^1.0.1",
		"react": "^17.0.2",
		"react-bootstrap": "^1.6.0",
		"react-chartist": "^0.14.4",
		"react-chartjs-2": "2.10.0",
		"react-copy-to-clipboard": "^5.0.3",
		"react-datetime": "^3.0.4",
		"react-dom": "^17.0.2",
		"react-feather": "^2.0.9",
		"react-github-btn": "^1.2.0",
		"react-helmet": "^6.1.0",
		"react-hot-loader": "^4.13.0",
		"react-live": "^2.2.3",
		"react-perfect-scrollbar": "^1.5.8",
		"react-redux": "^7.2.4",
		"react-router-dom": "^5.2.0",
		"react-simple-chatbot": "^0.6.1",
		"redux": "^4.1.0",
		"redux-thunk": "^2.3.0",
		"response-time": "^2.3.2",
		"simplebar-react": "^2.3.3",
		"styled-components": "^5.3.0",
		"typeorm": "^0.2.34",
		"uid-generator": "^2.0.0",
		"use-react-router": "^1.0.7",
		"winston": "^3.3.3",
		"winston-daily-rotate-file": "^4.5.5",
		"winston-elasticsearch": "^0.7.0",
		"winston-sentry": "^0.2.1",
		"yup": "^0.32.9"
	},
	"devDependencies": {
		"@babel/core": "^7.14.6",
		"@babel/plugin-proposal-class-properties": "^7.13.0",
		"@babel/plugin-transform-react-constant-elements": "^7.13.13",
		"@babel/plugin-transform-react-inline-elements": "^7.12.13",
		"@babel/plugin-transform-runtime": "^7.14.2",
		"@babel/preset-env": "^7.14.7",
		"@babel/preset-react": "^7.13.13",
		"@babel/runtime": "^7.14.0",
		"@babel/template": "^7.12.13",
		"@babel/types": "^7.14.2",
		"@testing-library/jest-dom": "^5.12.0",
		"@testing-library/react": "^11.2.7",
		"@types/axios": "^0.14.0",
		"@types/classnames": "^2.3.1",
		"@types/jest": "^26.0.23",
		"@types/jest-plugin-context": "^2.9.4",
		"@types/lodash": "^4.14.169",
		"@types/react": "^17.0.6",
		"@types/react-dom": "^17.0.5",
		"@types/react-redux": "^7.1.16",
		"@types/react-router": "^5.1.14",
		"@types/react-router-dom": "^5.1.7",
		"@types/redux": "^3.6.0",
		"@types/tapable": "^2.2.2",
		"@types/webpack": "^5.28.0",
		"@types/webpack-env": "^1.16.0",
		"@webpack-cli/serve": "^1.4.0",
		"apidoc": "^0.28.1",
		"axios-mock-adapter": "^1.19.0",
		"babel-core": "^6.26.3",
		"babel-eslint": "^10.1.0",
		"babel-jest": "^26.6.3",
		"babel-loader": "^8.2.2",
		"babel-plugin-transform-imports": "^2.0.0",
		"babel-plugin-transform-runtime": "^6.23.0",
		"babel-polyfill": "^6.26.0",
		"buddy.js": "^0.9.3",
		"chai": "^4.3.4",
		"chai-http": "^4.3.0",
		"commitizen": "^4.2.4",
		"cors": "^2.8.5",
		"css-loader": "^5.2.4",
		"cz-conventional-changelog": "^3.3.0",
		"docdash": "^1.2.0",
		"dotenv": "^10.0.0",
		"dotenv-webpack": "^7.0.2",
		"eslint": "^7.29.0",
		"eslint-config-airbnb": "^18.2.1",
		"eslint-config-prettier": "^8.3.0",
		"eslint-loader": "^4.0.2",
		"eslint-plugin-import": "^2.23.4",
		"eslint-plugin-prettier": "^3.4.0",
		"express-fileupload": "^1.2.1",
		"express-session": "^1.17.1",
		"faker": "^5.5.3",
		"file-loader": "^6.2.0",
		"fork-ts-checker-webpack-plugin": "^6.2.10",
		"fs": "^0.0.1-security",
		"helmet": "^4.6.0",
		"html-loader": "^2.1.2",
		"html-webpack-plugin": "^5.3.1",
		"husky": "^7.0.0",
		"image-webpack-loader": "^7.0.1",
		"jest": "^26.6.3",
		"jest-plugin-context": "^2.9.0",
		"jsdoc": "^3.6.7",
		"json-loader": "^0.5.7",
		"lint-staged": "^11.0.0",
		"mini-css-extract-plugin": "^1.6.0",
		"mocha": "^9.0.1",
		"morgan": "^1.10.0",
		"nodemon": "^2.0.9",
		"nyc": "^15.1.0",
		"optimize-css-assets-webpack-plugin": "^5.0.4",
		"prettier": "^2.3.2",
		"sass": "^1.32.13",
		"sass-loader": "^11.1.1",
		"sequelize": "^6.6.4",
		"sequelize-cli": "^6.2.0",
		"sinon": "^11.1.1",
		"style-loader": "^2.0.0",
		"supertest": "^6.1.3",
		"terser-webpack-plugin": "^5.1.2",
		"ts-jest": "^26.5.6",
		"ts-loader": "^9.2.0",
		"tsconfig-paths-webpack-plugin": "^3.5.1",
		"tslint": "^6.1.3",
		"tslint-config-prettier": "^1.18.0",
		"tslint-react": "^5.0.0",
		"typescript": "^4.2.4",
		"uglifyjs-webpack-plugin": "^2.2.0",
		"url-loader": "^4.1.1",
		"webpack": "^5.37.0",
		"webpack-bundle-analyzer": "^4.4.2",
		"webpack-cli": "^4.7.0",
		"webpack-dashboard": "^3.3.3",
		"webpack-dev-middleware": "^4.2.0",
		"webpack-dev-server": "^3.11.2",
		"webpack-hot-middleware": "^2.25.0",
		"webpack-node-externals": "^3.0.0"
	}
}
--#
