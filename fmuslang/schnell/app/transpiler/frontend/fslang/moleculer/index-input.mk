--% index/fmus
moleculer,d(/mk)
  %utama=__FILE__
  $*qterminal 2>/dev/null &
  flyway.conf,f(e=utama=/smartapp01/flyway.conf)
  package.json,f(e=utama=/smartapp01/package.json)
  docker-compose.yml,f(e=utama=/smartapp01/docker-compose.yml)
  stop.sh,f(e=utama=/smartapp01/stop.sh)
  .gitignore,f(e=utama=/smartapp01/.gitignore)
  man.sh,f(e=utama=/smartapp01/man.sh)
  .env,f(e=utama=/smartapp01/.env)
  README.md,f(e=utama=/smartapp01/README.md)
  run.sh,f(e=utama=/smartapp01/run.sh)
  docs,d(/mk)
    spec.yaml,f(e=utama=/smartapp01/docs/spec.yaml)
  persistence,d(/mk)
    package.json,f(e=utama=/smartapp01/persistence/package.json)
    .env,f(e=utama=/smartapp01/persistence/.env)
    .dockerignore,f(e=utama=/smartapp01/persistence/.dockerignore)
    Dockerfile,f(e=utama=/smartapp01/persistence/Dockerfile)
    src,d(/mk)
      persist.js,f(e=utama=/smartapp01/persistence/src/persist.js)
      persistence.service.js,f(e=utama=/smartapp01/persistence/src/persistence.service.js)
      data,d(/mk)
        data.js,f(e=utama=/smartapp01/persistence/src/data/data.js)
    test,d(/mk)
      persistence.service.test.js,f(e=utama=/smartapp01/persistence/test/persistence.service.test.js)
  api,d(/mk)
    Dockerfile,f(e=utama=/smartapp01/api/Dockerfile)
    api,d(/mk)
      package.json,f(e=utama=/smartapp01/api/api/package.json)
      .env,f(e=utama=/smartapp01/api/api/.env)
      .dockerignore,f(e=utama=/smartapp01/api/api/.dockerignore)
      public,d(/mk)
        .gitkeep,f(e=utama=/smartapp01/api/api/public/.gitkeep)
      src,d(/mk)
        api.service.js,f(e=utama=/smartapp01/api/api/src/api.service.js)
    web,d(/mk)
      package.json,f(e=utama=/smartapp01/api/web/package.json)
      .gitignore,f(e=utama=/smartapp01/api/web/.gitignore)
      tsconfig.json,f(e=utama=/smartapp01/api/web/tsconfig.json)
      .env,f(e=utama=/smartapp01/api/web/.env)
      public,d(/mk)
        robots.txt,f(e=utama=/smartapp01/api/web/public/robots.txt)
        manifest.json,f(e=utama=/smartapp01/api/web/public/manifest.json)
        apple-touch-icon.png,f(b64=utama=/smartapp01/api/web/public/apple-touch-icon.png)
        index.html,f(e=utama=/smartapp01/api/web/public/index.html)
        favicon.ico,f(b64=utama=/smartapp01/api/web/public/favicon.ico)
      src,d(/mk)
        App.tsx,f(e=utama=/smartapp01/api/web/src/App.tsx)
        react-app-env.d.ts,f(e=utama=/smartapp01/api/web/src/react-app-env.d.ts)
        reportWebVitals.ts,f(e=utama=/smartapp01/api/web/src/reportWebVitals.ts)
        App.css,f(e=utama=/smartapp01/api/web/src/App.css)
        logo.svg,f(e=utama=/smartapp01/api/web/src/logo.svg)
        index.tsx,f(e=utama=/smartapp01/api/web/src/index.tsx)
        setupTests.ts,f(e=utama=/smartapp01/api/web/src/setupTests.ts)
        App.test.tsx,f(e=utama=/smartapp01/api/web/src/App.test.tsx)
        index.css,f(e=utama=/smartapp01/api/web/src/index.css)
        view,d(/mk)
          LandingView.tsx,f(e=utama=/smartapp01/api/web/src/view/LandingView.tsx)
          MainView.tsx,f(e=utama=/smartapp01/api/web/src/view/MainView.tsx)
        assets,d(/mk)
          img 900x900.png,f(b64=utama=/smartapp01/api/web/src/assets/img 900x900.png)
          img.png,f(b64=utama=/smartapp01/api/web/src/assets/img.png)
        components,d(/mk)
          IRBDataCollection.tsx,f(e=utama=/smartapp01/api/web/src/components/IRBDataCollection.tsx)
          GovernmentCoverage.tsx,f(e=utama=/smartapp01/api/web/src/components/GovernmentCoverage.tsx)
          WQ5508.tsx,f(e=utama=/smartapp01/api/web/src/components/WQ5508.tsx)
        api,d(/mk)
          index.ts,f(e=utama=/smartapp01/api/web/src/api/index.ts)
  auth,d(/mk)
    package.json,f(e=utama=/smartapp01/auth/package.json)
    .env,f(e=utama=/smartapp01/auth/.env)
    .dockerignore,f(e=utama=/smartapp01/auth/.dockerignore)
    Dockerfile,f(e=utama=/smartapp01/auth/Dockerfile)
    src,d(/mk)
      auth.service.js,f(e=utama=/smartapp01/auth/src/auth.service.js)
    test,d(/mk)
      auth.service.test.js,f(e=utama=/smartapp01/auth/test/auth.service.test.js)
  visualize,d(/mk)
    package.json,f(e=utama=/smartapp01/visualize/package.json)
    .env,f(e=utama=/smartapp01/visualize/.env)
    .dockerignore,f(e=utama=/smartapp01/visualize/.dockerignore)
    Dockerfile,f(e=utama=/smartapp01/visualize/Dockerfile)
    src,d(/mk)
      load.js,f(e=utama=/smartapp01/visualize/src/load.js)
      visualize.service.js,f(e=utama=/smartapp01/visualize/src/visualize.service.js)
      data,d(/mk)
        data.js,f(e=utama=/smartapp01/visualize/src/data/data.js)
    test,d(/mk)
      visualize.service.test.js,f(e=utama=/smartapp01/visualize/test/visualize.service.test.js)
  migrations,d(/mk)
    V2__create_table.sql,f(e=utama=/smartapp01/migrations/V2__create_table.sql)
    V3__create_irbdatacollection.sql,f(e=utama=/smartapp01/migrations/V3__create_irbdatacollection.sql)
    V1__create_initial_tables.sql,f(e=utama=/smartapp01/migrations/V1__create_initial_tables.sql)
    Dockerfile,f(e=utama=/smartapp01/migrations/Dockerfile)
--#

--% /smartapp01/flyway.conf
flyway.url=jdbc:jtds:sqlserver://localhost:1456/tempdb
flyway.user=sa
flyway.password=MoonPie1
flyway.locations=filesystem:./migrations

--#

--% /smartapp01/package.json
{
  "name": "bzbt-smart-billing-app",
  "version": "0.0.1",
  "scripts": {
    "install:api": "cd api/api && npm install --production",
    "install:auth": "cd auth && npm install --production",
    "install:audit": "cd audit && npm install --production",
    "install:visualize": "cd visualize && npm install --production",
    "postinstall": "run-p install:*",
    "test": "mocha --config ./.mocharc.json",
    "coverage:test": "nyc mocha --config ./.mocharc.json",
    "coverage:report": "nyc report --reporter=html"
  },
  "files": [
    "docker-compose.yml",
    ".env",
    "*/.env"
  ],
  "devDependencies": {
    "chai": "^4.2.0",
    "chai-as-promised": "^7.1.1",
    "mocha": "^8.0.1",
    "nock": "^13.0.4",
    "npm-run-all": "^4.1.5",
    "nyc": "^15.1.0",
    "sinon": "^9.0.3",
    "superagent": "^6.1.0"
  },
  "dependencies": {
    "mssql": "^7.1.3"
  }
}

--#

--% /smartapp01/docker-compose.yml
version: '3.4'

services:
  api:
  build: api
  image: smart-billing-app/api:latest
  env_file:
    - .env
  depends_on:
    - nats.service
  ports:
    - '12300:3000'
  links:
    - nats.service
  volumes:
    - "./logs/api:/app/logs"

  auth:
  build: auth
  image: smart-billing-app/auth:latest
  env_file:
    - .env
    - auth/.env
  links:
    - nats.service
  depends_on:
    - nats.service
  volumes:
    - "./logs/auth:/app/logs"

  visualize:
  build: visualize
  image: smart-billing-app/visualize:latest
  env_file:
    - .env
    - visualize/.env
  depends_on:
    - nats.service
  links:
    - nats.service
  volumes:
    - "./logs/visualize:/app/logs"
  environment:
    DB_HOST: mssql
    DB_PORT: 1433
    DB_DATABASE: 'tempdb'
    DB_USER: sa
    DB_PASSWORD: MoonPie1

  persistence:
  build: persistence
  image: smart-billing-app/persistence:latest
  env_file:
    - .env
    - persistence/.env
  depends_on:
    - nats.service
  links:
    - nats.service
  volumes:
    - "./logs/persistence:/app/logs"
  environment:
    DB_HOST: mssql
    DB_PORT: 1433
    DB_DATABASE: 'tempdb'
    DB_USER: sa
    DB_PASSWORD: MoonPie1

  nats.service:
  image: nats

  mssql:
  image: mcr.microsoft.com/mssql/server:2017-latest
  environment:
    - SA_PASSWORD=MoonPie1
    - ACCEPT_EULA=Y
  ports:
    - "1456:1433"
  volumes:
    - database:/var/opt/mssql/data

  flyway:
  build: migrations
  image: smart-billing-app/migration:latest
  command: -connectRetries=20 migrate
  environment:
    FLYWAY_USER: sa
    FLYWAY_PASSWORD: MoonPie1
    FLYWAY_URL: jdbc:jtds:sqlserver://mssql:1433/tempdb
  depends_on:
    - mssql
  links:
    - mssql

volumes:
  database:

--#

--% /smartapp01/stop.sh
docker-compose -f docker-compose.yml down

--#

--% /smartapp01/.gitignore
*.iml
**/node_modules
node_modules
**/yarn.lock
logs
.idea
api/web/build
.nyc_output
**/.nyc_output
terraform/.terraform/*
terraform/.terraform/**/*
terraform/*.log
terraform/*.tfstate
terraform/*.backup
coverage
coverage.tar.gz
package-lock.json
public/*
public/**/*

--#

--% /smartapp01/man.sh
(cd api/web && yarn start)
--#

--% /smartapp01/.env
LOGLEVEL=info
TRANSPORTER=nats://nats.service:4222
CACHER=memory
NAMESPACE=smart-billing-app

#Logging
LOGGER=File
METRICS=true
CORS=true

--#

--% /smartapp01/README.md

# Smart Billing App

## Technologies
- [ReactJS](https://reactjs.org/) as frontend library
- [AntDesign](https://ant.design/) as frontend library
- [Moleculer](https://moleculer.services/) as microservice framework

## Deploy

### Recommended versions
- docker = 19.03.12 or above
- docker-compose = 1.28.2 or above
- on windows machines using `wsl2` with `docker desktop` provide better performance than legacy `hyper V` backends

### Single Instance (For development purpose)
##### 1. Build
run ``docker-compose -f docker-compose.yml build``
##### 2. Start Services
run ``docker-compose -f docker-compose.yml up -d``
##### 3. Stop Services
run ``docker-compose -f docker-compose.yml down``


#### API 
REST api is available via [localhost:12300/api/{path}](http://localhost:12300/api/)

#### Web Application
Web app can be access via [localhost:12300](http://localhost:12300)

## Database Connection
Find the following in `docker-compose.yml`
```java 
45 environment:
46  DB_HOST: <db-server>
47  DB_PORT: <db-port>
48  DB_DATABASE: <db-name>
49  DB_USER: <db-username>
50  DB_PASSWORD: <db-password>
```
Change the above variables with the DB connection information.

---
### Additional Instructions
#### Installation of Docker / Docker Compose
##### Ubuntu (Recommended)
##### 1. Install Docker Engine
1. Update the apt package index and install packages to allow apt to use a repository over HTTPS::
 ``` 
sudo apt-get update

sudo apt-get install \
  apt-transport-https \
  ca-certificates \
  curl \
  gnupg \
  lsb-release
```
2. Add Docker’s official GPG key::
 `` curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg``
 1. Update the apt package index and install packages to allow apt to use a repository over HTTPS::
 ``` 
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

```
 4. Install Docker Engine
 ``` 
 sudo apt-get update
 
 sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo apt-get install docker-ce=18.06.3~ce~3-0~ubuntu docker-ce-cli=18.06.3~ce~3-0~ubuntu containerd.io
  ```
   5. Verify that Docker Engine is installed correctly by running the `hello-world` image.
 ``sudo docker run hello-world``


If the installation failed, follow the [Official instructions](https://docs.docker.com/engine/install/ubuntu/)

##### 2. Install Docker Compose
  1. Run this command to download the current stable release of Docker Compose:
 ``sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose``
 2. Apply executable permissions to the binary:
``sudo chmod +x /usr/local/bin/docker-compose``
 3. Test the installation.
 ``$ docker-compose --version``
  
If the installation failed, follow the [Official instructions](https://docs.docker.com/compose/install/) and click Linux
 ##### Windows
 - Follow the [Official instructions](https://docs.docker.com/docker-for-windows/install/)
--#

--% /smartapp01/run.sh
docker-compose -f docker-compose.yml up -d

--#

--% /smartapp01/docs/spec.yaml
swagger: "2.0"
info:
  title: Smart Billing App API
  description: Smart Billing App REST api specification.
  version: 1.0.0
host: api.xxx
basePath: /api
schemes:
  - https
tags:
  - name: visualize
  description: Visualize API

securityDefinitions:
  bzbt_auth:
  type: oauth2
  authorizationUrl: /authorize
  flow: implicit
  scopes:
    read: read
    write: write

paths:
  /visualize/{tableName}:
  get:
    tags:
    - visualize
    summary: Visualize table data
    produces:
    - application/json
    consumes:
    - application/json
    responses:
    200:
      description: OK
    404:
      description: Not Found


definitions:
--#

--% /smartapp01/persistence/package.json
{
  "name": "persistence",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
  "test": "mocha",
  "coverage": "nyc mocha",
  "start": "moleculer-runner ./src"
  },
  "keywords": [],
  "author": "sptr",
  "license": "ISC",
  "dependencies": {
  "moleculer": "^0.14.13",
  "nats": "^1.4.9",
  "sequelize": "^6.6.5",
  "tedious": "^11.0.9",
  "mssql" : "^7.1.3"
  },
  "devDependencies": {
  "chai": "^4.2.0",
  "chai-as-promised": "^7.1.1",
  "mocha": "^8.0.1",
  "nock": "^13.0.4",
  "nyc": "^15.1.0",
  "sinon": "^9.0.3"
  }
}

--#

--% /smartapp01/persistence/.env

--#

--% /smartapp01/persistence/.dockerignore
node_modules
--#

--% /smartapp01/persistence/Dockerfile
FROM node:12-alpine

ENV NODE_ENV=production

RUN mkdir /app
WORKDIR /app

COPY package.json .

RUN npm install --production

COPY . .

CMD ["npm", "start"]
--#

--% /smartapp01/persistence/src/persist.js
const { Sequelize } = require('sequelize');
var sql = require("mssql");

let dbConfig = {
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  server: process.env.DB_HOST,
  database: process.env.DB_DATABASE,
  port: parseInt(process.env.DB_PORT),
  options: { encrypt: false }
};


const sequelize = new Sequelize('TestDB', 'SA', 'MoonPie1', {
  host: 'localhost',
  dialect:'mssql'
  });

async function update_data_with_key(id, tableName, key, val){
  try{
  const res = await sql.connect(dbConfig)
  switch(typeof val){
    case "string":
    return await sql.query(`update ${tableName} set [${key}] = '${val}' where id = ${id}`)
    default:
    return await sql.query(`update ${tableName} set [${key}] = ${val} where id = ${id}`)
  }
  }
  catch(err){
  return err
  }
}

module.exports = {
  update_data_with_key
}

--#

--% /smartapp01/persistence/src/persistence.service.js

module.exports = {
  name: "persistence",
  actions:{
  update_data:{
    async handler(ctx){
    return await this.update_data_with_key(ctx.params.id, ctx.params.tableName, ctx.params.key, ctx.params.val)
    }
  },
  },
  created(){
  const {update_data_with_key} = require('./persist')
  this.update_data_with_key = update_data_with_key.bind(this)

  }
}

--#

--% /smartapp01/persistence/src/data/data.js
const data = [
  {
  "UID": 1537504855,
  "primary_coverage": "*LA CARE MCL CMMNTY FAM CARE",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 2138663502,
  "primary_coverage": "*CIGNA POS GRTR NEWPORT PHYS",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 434201408,
  "primary_coverage": "*BLUE SHIELD MCR GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1171126358,
  "primary_coverage": "*BLUE SHIELD HMO REGAL MG CAP",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1560360744,
  "primary_coverage": "BLUE CROSS OF CALIFORNIA EPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 771244835,
  "primary_coverage": "OUT OF STATE BS PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1181510274,
  "primary_coverage": "*SCAN MCR EMPIRE PHYS MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1824027568,
  "primary_coverage": "WRITERS GUILD OF AMERICA",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1388533909,
  "primary_coverage": "*BC OF CA PRIMECARE/NAMM",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1372265719,
  "primary_coverage": "*BS COVCA SILV GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 183643417,
  "primary_coverage": "GENERIC COMMERCIAL PLAN",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 218175239,
  "primary_coverage": "BLUE CROSS OF CALIFORNIA POS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1127224574,
  "primary_coverage": "*HLTH NET ELECT REGAL MG CAP",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 717060577,
  "primary_coverage": "*IEHP MCL PHYS HEALTHWAYS",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1400148003,
  "primary_coverage": "TRICARE WEST REGION",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 730213833,
  "primary_coverage": "BC COVCA PPO SILVER",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1227586970,
  "primary_coverage": "URN BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1147323347,
  "primary_coverage": "CCS RIVERSIDE",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1442148398,
  "primary_coverage": "*IEHP MCL HORIZON VALLEY",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1538100975,
  "primary_coverage": "BCBS FEDERAL EMPLOYEE PROGRAM",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 444943960,
  "primary_coverage": "KAISER SOUTHERN MEDICARE HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 2104544917,
  "primary_coverage": "*SECURE HORIZONS MCR CEDARS HLTH ASSOC",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1916401506,
  "primary_coverage": "*LA CARE MCL GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1491411420,
  "primary_coverage": "TRICARE PRIME",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 600320165,
  "primary_coverage": "GEHA - ASA",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1728425355,
  "primary_coverage": "CIGNA OPEN ACCESS PLUS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 2095459458,
  "primary_coverage": "BC COVCA PPO GOLD",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 871264926,
  "primary_coverage": "GOLD COAST MCL HEALTH PLAN DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 275562133,
  "primary_coverage": "*SECURE HORIZONS MCR AXMINSTER MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 816072237,
  "primary_coverage": "CAREMORE MCR HEALTH PLAN DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 488595671,
  "primary_coverage": "BLUE SHIELD PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1396303610,
  "primary_coverage": "CIGNA PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 476274903,
  "primary_coverage": "BLUE SHIELD EPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 156147313,
  "primary_coverage": "*LA CARE MCL HEALTHCARE LA IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 2142270678,
  "primary_coverage": "*HLTH NET MCR ST JUDE HERITAGE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 116786235,
  "primary_coverage": "BCCTP",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1555519842,
  "primary_coverage": "LA COUNTY FIREFIGHTERS LOCAL 1014",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1217023299,
  "primary_coverage": "LA CARE MEDI-CAL HMO DIRECT",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 580522855,
  "primary_coverage": "*CIGNA HMO BEAVER MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 251614032,
  "primary_coverage": "*IEHP MCL ALPHA CARE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1684460796,
  "primary_coverage": "*BLUE SHIELD PROMISE MCL HEALTHCARE LA IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1788066700,
  "primary_coverage": "*IEHP MCL INLAND FACULTY MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1360695274,
  "primary_coverage": "AETNA BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 765207896,
  "primary_coverage": "*SCAN MCR PRIMECARE/NAMM",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1537921777,
  "primary_coverage": "*BLUE SHIELD MCR ALAMITOS",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1095235732,
  "primary_coverage": "*BLUE SHIELD MCR PRIMECARE/NAMM",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1568758937,
  "primary_coverage": "CCS VENTURA",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 482569787,
  "primary_coverage": "BLUE SHIELD BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 2000388457,
  "primary_coverage": "CCS LOS ANGELES",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1243982196,
  "primary_coverage": "KAISER COVCA HMO GOLD DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1408917668,
  "primary_coverage": "KAISER SOUTHERN CALIFORNIA BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1542275121,
  "primary_coverage": "*BC OF CA POS HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 53795751,
  "primary_coverage": "*PAC HMO PRIMECARE INLAND VALLEY CAP",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 423949474,
  "primary_coverage": "NATIONAL MARROW DONOR PROGRAM BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 128402595,
  "primary_coverage": "*PAC HMO GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 651762858,
  "primary_coverage": "*BLUE SHIELD HMO GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1778275139,
  "primary_coverage": "*BLUE CROSS MCR GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 682720398,
  "primary_coverage": "*EASY CHOICE MCR REGAL MED GROUP FFS",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 106869151,
  "primary_coverage": "HEALTHCARE PARTNERS EMPLOYEES",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 2117314283,
  "primary_coverage": "KAISER MEDI-CAL HMO DIRECT",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1355190238,
  "primary_coverage": "AETNA POS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 592431495,
  "primary_coverage": "*SECURE HORIZONS MCR ST JOSEPH IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 763287496,
  "primary_coverage": "MERITAIN HEALTH",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 892919568,
  "primary_coverage": "*HLTH NET ALLIED PACIFIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1632643614,
  "primary_coverage": "CIGNA GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1584050311,
  "primary_coverage": "CCS MEDI-CAL",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 244675029,
  "primary_coverage": "*BLUE SHIELD PROMISE MCL CAL CARE IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1388899533,
  "primary_coverage": "MEDICARE PART A+B",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 39687950,
  "primary_coverage": "IEHP MEDICONNECT DUAL DIRECT",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 598302723,
  "primary_coverage": "*SCAN MCR HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1869443488,
  "primary_coverage": "GENERIC BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1635133987,
  "primary_coverage": "AETNA GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 2103445477,
  "primary_coverage": "*CIGNA HMO GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 87538195,
  "primary_coverage": "*BLUE SHIELD MCR PRIMECARE CAP IV",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1051190868,
  "primary_coverage": "KAISER COVCA HMO BRONZE DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1022821363,
  "primary_coverage": "*BS COVCA PLAT ALLIED PACIFIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 500728315,
  "primary_coverage": "UNITED HEALTHCARE OXFORD",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1879913767,
  "primary_coverage": "AETNA REPLACEMENT MCR PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1917878129,
  "primary_coverage": "CIGNA BMT - TN",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1897391354,
  "primary_coverage": "MEDICARE RAILROAD",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1071924003,
  "primary_coverage": "OUT OF STATE BC EPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1334293434,
  "primary_coverage": "BLUE CROSS MCR REPLACEMENT PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 218351422,
  "primary_coverage": "BLUE CROSS OF CALIFORNIA BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1533324086,
  "primary_coverage": "CAL OPTIMA MCL DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1617069156,
  "primary_coverage": "UNITED HEALTH CARE MCR REPLACEMENT PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1436033849,
  "primary_coverage": "MEDI-CAL",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1217871477,
  "primary_coverage": "*BLUE SHIELD HMO AXMINSTER MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 676379035,
  "primary_coverage": "*BLUE SHIELD HMO ST JOSEPH IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1513681355,
  "primary_coverage": "*BLUE SHIELD HMO RMG INTERCOMMUNITY",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1527862477,
  "primary_coverage": "HUMANA GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1501874099,
  "primary_coverage": "*AETNA HMO HCP CAP MTHDST",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1814933728,
  "primary_coverage": "*CAL OPTIMA MCL MONARCH FAMILY HEALTHCARE",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 862012406,
  "primary_coverage": "KAISER SOUTHERN CALIFORNIA HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 862943734,
  "primary_coverage": "KAISER NORTHERN CALIFORNIA HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 240655867,
  "primary_coverage": "MEDICARE PART B",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1042036906,
  "primary_coverage": "*BS COVCA SILV MEMORIALCARE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1396303906,
  "primary_coverage": "CIGNA POS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 712550447,
  "primary_coverage": "CCS TULARE",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1168702954,
  "primary_coverage": "BDCT GENERIC BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 997924970,
  "primary_coverage": "*BC OF CA GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 414550640,
  "primary_coverage": "BLUE CROSS GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 981219044,
  "primary_coverage": "UMR",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 56626789,
  "primary_coverage": "*AETNA HMO GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 2023103327,
  "primary_coverage": "BS COVCA PPO PLATINUM",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1597654292,
  "primary_coverage": "*BLUE SHIELD HMO GLOBAL CARE",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1147204803,
  "primary_coverage": "MOTION PICTURE SCREEN ACTORS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 306198724,
  "primary_coverage": "*BLUE SHIELD POS HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1917877197,
  "primary_coverage": "CIGNA BMT - PA",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 6362666,
  "primary_coverage": "*LA CARE MCL ALTAMED MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1493703328,
  "primary_coverage": "*BC OF CA SANSUM MC",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 43161578,
  "primary_coverage": "DELTA HEALTH SYSTEMS",
  "CurrentCoverage": "",
  "government": 0
  },
  {
  "UID": 711690761,
  "primary_coverage": "BLUE SHIELD HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 298989248,
  "primary_coverage": "OUT OF STATE MCR BS PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1682004932,
  "primary_coverage": "*BLUE SHIELD MCR HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 2046971352,
  "primary_coverage": "BLUE SHIELD MEDICARE HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1963951790,
  "primary_coverage": "CENCAL MEDI-CAL HMO",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 2024789996,
  "primary_coverage": "SIERRA HEALTH AND LIFE",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 471534270,
  "primary_coverage": "CIGNA SENIOR HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1050166051,
  "primary_coverage": "OUT OF STATE BC PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 527829327,
  "primary_coverage": "PINNACLE GROUP CLAIMS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 801710251,
  "primary_coverage": "OPERATING ENGINEERS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1887275435,
  "primary_coverage": "IEHP MEDI-CAL HMO DIRECT",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 523550920,
  "primary_coverage": "*LA CARE MEDI DUAL APPLECARE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 712052554,
  "primary_coverage": "CAL PERS PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 971034193,
  "primary_coverage": "KAISER COVCA HMO SILVER DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1138159113,
  "primary_coverage": "*SECURE HORIZONS MCR PRIMECARE CAP IV",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 607864312,
  "primary_coverage": "*MOLINA MCL INLAND FACULTY MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 587122935,
  "primary_coverage": "BLUE CROSS OF CALIFORNIA PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 289352998,
  "primary_coverage": "*MOLINA COVCA SILV VANTAGE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 625014119,
  "primary_coverage": "UNITED HEALTHCARE GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1734969266,
  "primary_coverage": "*BLUE SHIELD PROMISE MEDI DUAL HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 426872091,
  "primary_coverage": "BCBS NEVADA MEDICAID",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1355186438,
  "primary_coverage": "AETNA PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1199975883,
  "primary_coverage": "BS COVCA PPO SILVER",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 9,
  "primary_coverage": null,
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1192903551,
  "primary_coverage": "*LA CARE MCL DHS",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1419698406,
  "primary_coverage": "TRISTAR RISK MANAGEMENT POLICE",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1406057435,
  "primary_coverage": "BS COVCA PPO BRONZE",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 569317289,
  "primary_coverage": "SELF INSURED SCHOOLS CA PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1373142263,
  "primary_coverage": "*BC COVCA SILV GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 828779650,
  "primary_coverage": "BS COVCA PPO GOLD",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 307502581,
  "primary_coverage": "*BC OF CA HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 2100745759,
  "primary_coverage": "*BLUE SHIELD HMO PRIMECARE CAP IV",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1606417776,
  "primary_coverage": "WORKERS COMPENSATION GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1171675772,
  "primary_coverage": "UNITED HEALTHCARE PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1521972295,
  "primary_coverage": "PHCS GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 552860996,
  "primary_coverage": "SCREEN ACTORS GUILD",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1113994192,
  "primary_coverage": "*BLUE CROSS MCL ACCOUNTABLE IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 791709537,
  "primary_coverage": "KAISER HAWAII HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1227325046,
  "primary_coverage": "URN CRS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 653876433,
  "primary_coverage": "*HLTH NET MCL OMNICARE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 826788476,
  "primary_coverage": "*SECURE HORIZONS MCR HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 398681715,
  "primary_coverage": "MULTIPLAN GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1950441493,
  "primary_coverage": "*BC OF CA APPLECARE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1797743489,
  "primary_coverage": "*AETNA HMO MEMORIALCARE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1480920405,
  "primary_coverage": "*SECURE HORIZONS MCR GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 66621630,
  "primary_coverage": "KAISER SOUTHERN CALIFORNIA EPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 914518814,
  "primary_coverage": "*SCAN MCR PRIMECARE CAP IV",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 331857060,
  "primary_coverage": "*PAC HMO HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 834153197,
  "primary_coverage": "*BLUE SHIELD HMO PRIMECARE/NAMM",
  "CurrentCoverage": "",
  "government": 1
  }
]

module.exports = {
  data
}
--#

--% /smartapp01/persistence/test/persistence.service.test.js
const { ServiceBroker, Context } = require("moleculer");
const assert = require('assert');
const schema = require('../src/visualize.service')
const sinon = require('sinon')
const chai = require('chai')
const expect = chai.expect
chai.use(require('chai-as-promised'))

describe("Visualization Actions",()=> {
  let broker = new ServiceBroker({logger: false});
  let service = broker.createService(schema);

  before(() => broker.start());
  after(() => broker.stop());

  afterEach(()=>{

  })

  describe("Load Page data", ()=>{
  before(()=>{

  })
  it('should load data for the table', async function () {
    const res = await broker.call('visualize.load', {tableName: 'hello'});
    console.log(res)
  });
  })

});

--#

--% /smartapp01/api/Dockerfile
FROM node:12-alpine as web
ENV NODE_ENV=production
RUN mkdir /app
WORKDIR /app
COPY web/package.json .
RUN npm install --production
COPY web/src src
COPY web/public public
RUN npm run build

FROM node:12-alpine
ENV NODE_ENV=production
RUN mkdir /app
WORKDIR /app
COPY api/package.json .
RUN npm install --production
COPY api/src src
COPY api/public public
COPY --from=web /app/build /app/public/
CMD ["npm", "start"]

--#

--% /smartapp01/api/api/package.json
{
  "name": "api",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
  "test": "mocha",
  "coverage": "nyc mocha",
  "start": "moleculer-runner ./src"
  },
  "keywords": [],
  "author": "sptr",
  "license": "ISC",
  "dependencies": {
  "moleculer": "^0.14.13",
  "moleculer-web": "0.10.0",
  "nats": "^1.4.9"
  },
  "devDependencies": {
  "chai": "^4.2.0",
  "chai-as-promised": "^7.1.1",
  "mocha": "^8.0.1",
  "nock": "^13.0.4",
  "nyc": "^15.1.0",
  "sinon": "^9.0.3"
  }
}

--#

--% /smartapp01/api/api/.env

--#

--% /smartapp01/api/api/.dockerignore
node_modules
--#

--% /smartapp01/api/api/public/.gitkeep

--#

--% /smartapp01/api/api/src/api.service.js
const ApiGateway = require("moleculer-web");

module.exports = {
  name: process.env.npm_package_name,
  mixins: [ApiGateway],
  settings: {
  port: process.env.PORT || 3000,
  cors: `${process.env.CORS}` === 'true',
  routes: [{
    path: "/api",
    authorization: true,
    aliases: {
    "GET /visualize/:tableName" : "visualize.load",
    "POST /update" : "persistence.update_data"

    },
    mappingPolicy: "restrict",
    cors: `${process.env.CORS}` === 'true',
    bodyParsers: {
    json: {
      strict: false
    },
    urlencoded: {
      extended: false
    }
    }
  }],
  assets: {
    folder: "./public"
  },
  },
  methods: {
  authorize(ctx, route, req, res){
    this.logger.info("authorize method")
    ctx.meta.user_id = 1;
    return Promise.resolve(ctx)
  }
  }
}

--#

--% /smartapp01/api/web/package.json
{
  "name": "smart-billing-app-ui",
  "version": "0.1.0",
  "private": true,
  "dependencies": {
  "@ant-design/icons": "^4.6.2",
  "@testing-library/jest-dom": "^5.11.4",
  "@testing-library/react": "^11.1.0",
  "@testing-library/user-event": "^12.1.10",
  "@types/antd": "^1.0.0",
  "@types/jest": "^26.0.15",
  "@types/node": "^12.0.0",
  "@types/react": "^17.0.0",
  "@types/react-dom": "^17.0.0",
  "@types/react-router-dom": "^5.1.7",
  "antd": "^4.16.3",
  "axios": "^0.21.1",
  "i18next": "^20.3.2",
  "react": "^17.0.2",
  "react-dom": "^17.0.2",
  "react-i18next": "^11.11.0",
  "react-perfect-scrollbar": "^1.5.8",
  "react-router-dom": "^5.2.0",
  "react-scripts": "^4.0.3",
  "typescript": "^4.1.2",
  "web-vitals": "^1.0.1"
  },
  "scripts": {
  "start": "react-scripts start",
  "build": "react-scripts build",
  "test": "react-scripts test",
  "eject": "react-scripts eject"
  },
  "eslintConfig": {
  "extends": [
    "react-app",
    "react-app/jest"
  ]
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

--% /smartapp01/api/web/.gitignore
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.js

# testing
/coverage

# production
/build

# misc
.DS_Store
.env.local
.env.development.local
.env.test.local
.env.production.local

npm-debug.log*
yarn-debug.log*
yarn-error.log*

--#

--% /smartapp01/api/web/tsconfig.json
{
  "compilerOptions": {
  "target": "es5",
  "lib": [
    "dom",
    "dom.iterable",
    "esnext"
  ],
  "allowJs": true,
  "skipLibCheck": true,
  "esModuleInterop": true,
  "allowSyntheticDefaultImports": true,
  "strict": true,
  "forceConsistentCasingInFileNames": true,
  "noFallthroughCasesInSwitch": true,
  "module": "esnext",
  "moduleResolution": "node",
  "resolveJsonModule": true,
  "isolatedModules": true,
  "noEmit": true,
  "jsx": "react-jsx"
  },
  "include": [
  "src"
  ]
}

--#

--% /smartapp01/api/web/.env
REACT_APP_SERVER_URL=http://localhost:12300

--#

--% /smartapp01/api/web/public/robots.txt
# https://www.robotstxt.org/robotstxt.html
User-agent: *
Disallow:

--#

--% /smartapp01/api/web/public/manifest.json
{
  "short_name": "React App",
  "name": "Create React App Sample",
  "icons": [
  {
    "src": "favicon.ico",
    "sizes": "64x64 32x32 24x24 16x16",
    "type": "image/x-icon"
  },
  {
    "src": "logo192.png",
    "type": "image/png",
    "sizes": "192x192"
  },
  {
    "src": "logo512.png",
    "type": "image/png",
    "sizes": "512x512"
  }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}

--#

--% /smartapp01/api/web/public/apple-touch-icon.png
iVBORw0KGgoAAAANSUhEUgAAALQAAAC0CAYAAAA9zQYyAAAAAXNSR0IB2cksfwAAAAlwSFlzAABcRgAAXEYBFJRDQQAAI+1JREFUeJztnQlYFEfaxzeGXXVjTJaI0Y1Ro3hl1BgUbxGv4AWIiicqoCiHt+LFITeIyKV4ooCA4IAiIEowIqjRaEzUJJxyKBhNMMzFIMTj4/vXPA6LUaS7pwfG3fo/Tz0MPV33r95+q7qm+29/o6KioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKi+u/XqmOFdcui8hgH1+QScy75BJ0rd2CTj31Mwe0D2b9qc8mLlJFNXg6xBXWpt/7Q4pIXlYaJdOjCQzmMw+bEIk5Ae52+68AmH8sjuZWBGWWdueRFysgmLxJ8z9wdzyUvKg2TpgJtgeCUVGzNJS8uQCNO9g93Za245EelQdJUoEmAK3CdS15cgMYVQeJyquQTLvlRaZA0GehF4Tl1ezLLe7LNiwvQJLgklfhxqRuVBkmTgSbBOanEi21eXIFecTS/lEvdqDRImg40yvfg8KWH/2KTF1egSQg6Vz6CS/2oNESaDjTcjv/zSC2dwSYvVYDeeqI4mkv9qBoo/vrv7Xeml5mzCSm3HrXnI29NB5qElccKLrHJSxWgl0bmPdqX9evHXOrIVX/ePvNP2ZFl/SVhc+ZLgkz8JMGmmeIg4wrxTqM6ka8hwrg68a6pdWL/rwole8zTJaEzPaR755nKjjroPi298ffmLCsjobMFbBs+9JtyAR95vw1ALz6c+zTu2u+M16RVAZosF+KKsJJLHdnqceb+7tK9871FfuMLRO7Dnla6fFnHJog8RtSKd025KQ23WltzKZIXA8eLKNBNB5dTJduY5qUK0CTYRhfc4lJHJqq5GtdKun9RH/HOyQdF7kOfsIW4Ubh9xlYjTRdpuDWnm1G86m0F+s+bqe1lh5fNkuyZEyw9sPhn6b4FOZK9885JDy7xqop3HPHnT+n1t5NVBXpFdH5R6u0/2jGpk6pALwrPrYu68rAPH+3bUDXZ4e1hkWMq3YbK+QL5FbA9R1UCaren939pzXf5GettARoTtKewlBOrjm/qAJ/OGf5d4x3jqqfw+dCBM2suR7/ne+aejUU4d8jgdtT5n703jUmdVAWahPXH77jx0b5KyaLsp8EXLlEXyH8N8MUvwcfuz2cdGOttAJr4sa6nSjbLImwN0DFljBvXdfBzceD0y3nXLuk6JtxJUQUy+5iCVCZ14gPo5UfzH8R89xunzVEN9STvgpYsYsU2WGXWPjIP1louT3RmtULEizQdaGJZtyQWbZSFLzVAx1RzaVxY9FxxdnT/lbGFN7lCtjQyrw6TwybXpPkAmrgdbimlM1VpW8CkJdk1Lbhy+5BmBfmlAD9dsnuWjSr1YC1NB9ohtiBLluQxWOQ5slKVxoULciPq4t3PkaeIK2hbThQvb6pOfABNgl1MQRbXdn18LhQwT/UjrleLwfyfq+RTyb75FlzrwlqaDLTVkdzHh7LK9cUBU37io3GlByxWOSeVrOYK2eq4wuLkW4/avKlOfAFtdSSvLvrqb5xWDTBJ3lm5fXDLw/wiiNyHPZFFr1zMjRKW0mSgNyUWJcuEW6bxZWlE3mN+K0o92MUmKr+WC2Tw5Z/5nrk75k114gtoEpyTijezbdOq+I1msIrPWhriV9reY7i8+rQf76s3r0iTgfY8fXeiJNgkjb/Ln16d7IiNzepjhUlcIVsTXyh8U534BHrlsYJS4fe//5Npe1bFO/YQeRv80dLwNhYwQb9ZFb3qPdXJeYM0FWjLI7l1Dy4Ku4k8Rv7OZ6NKgk2zUWdbrpBZR+TVZuSIGr0zxifQmBw+d00uMWDanqjbhZaGtimDIj24JIAPdhqVpgK9PCq/AtZUIPIYwWujijxH5a+JKxSQtWWuoLmcKml0ksMn0CQ4CovSmbRlVdzGcXA1VGgbvTqR15gK8Y5Jp6Xh1s6yw8sm1d5MMay9nmAo3Tt/uvTgYn+x34Qs9IdYpfZ3Hy6vOr5Zhw9+XisCtA2soU/8HUZhTVR+swBtFZGXIz1kNYTvZSdMMJ/6p5cJyDIcV8gwObz9bZH0tXfD+AYa7fAkM1/8xr0SNd/GtBYHmdxWYZBXSMOtXB9n7H4jaM9+L25VFbP6E0nY3HD4xLVc88OAiVQBmzeLAL0iIq8uSFjEKGw42jxAw+XIkYTMGFC5XZ9foHdOrvU7c09grQLQS47kPtmZXjb0dXXiG2gSnE4Wv3HZSxZpO0nkPoyLC/BcHDA5u+ZSJGuLWZ3mP1jkO66AWHb2A2ikVJ7i04NtnoykqUDbxRTUyKLs+6DyvM7YRd5jcrYnl+iTmxcquQIJRXGvq5M6gLaPKfgh5dajRh91IPYbf5qTpdxvsV8Wacd5CyjcHG1M9LK55C3ZPYvxhi9W0lSgCXDfX8zuLvIaXc6rhQ6cJvRILXVSFTKbqHx59NXfXnE71AE0uSL4p9977RWh9rtj7TFI2Vpm4nol8dGHj8+FvocBVci6H/y/Kucj/1ekqUCTAEs6UxJkHMkb0PDHMcs2W3ms4Bs+QPNJu/vKXgV1AE3ClhPF4a9rQ1nMGhPWVykfw5Lq9MBufPQhUVXMGgNM9qpYlcNNv676tF8nvspQL00Gel38nSt/HHf6AiA+58Xd8DXM+fr8t7qq+M8Ng110Qcbp2y8/9UhdQFtF5D46+eOjV64I0n0L2A14WOeq41tU2ifyOknDlwaw7Q9ZxApLvsuh0UAvPpxb63m61FASYpapMtDkpkq4lfm2k8U7eIPsSG7N3sz7AxrWSV1Ak+CfXjalYV7PHhb8Q7xrKqvLPdyToufiX3l/9Fh12s6OsNKsVj5wtYzhuxwaDTQJK47mF/98cn9X8Y6J+dyB1nsuCZ0Z75laaohBIucTso0JRbsb1kmdQDvEFqSfzxPVwyg/5fGxyGMEqzuDgMibj757nTA/yWBTFkwoc59Xlr3DayE0HWgSNgjvhFTEbtKDy1DBBWhMQBLSUs70wOAo4hsyTA4rSh7V1LsC6gTaKiJPvi/rfm9lXlXRq8gqEPO9zm5Dn1UdddDjo+9eJ9nhpQ6srhY+Yx88yc1k9ZiIJvU2AE32RK86VnigLCtxoDjI5DxTn1rkMbIKljnQ98zdLrBuueoCDZPDeldAnUCTsPVEcaAyL/FOIwGbG0+w5hXVqT5qu0sn2T1LwGY9HC5KhVy4pSOjxG2jC+wtj+S6NRWWReaHsQV6+dH8MCZpMwisOtMjtdTkZk5JR/jUKzBTz26s8WDJa8UBk5Ml8ZuNDmTf1/NOY/300To2ZVsbfydZ2e5sgbZgCTSuMvXLXdL9FvpsdiLCIpY/u/+L2n6hXRXvqCvyHMXcj3YbWik9bM1spcMhOj9nx/GiOibB/zgzmEkIYJgmCcsj+FlNUAYCC64o2euP3wmBPzy24Grm51Uxa5fDd3OX7JzshRm/mzzJfV7wufIu+H4OzruJkMPhcboViPcti/PluGr1Je3OFmhylbKNzn/IJg7qN4HkJT/lacrmTp3I26DwWWW52p6lAUPzgchr9GFJ2NxfJMGmOZiw5oj9J+VgIOXANcpB/veI24iJaQW53S72HVcmP+HKbPlwZXRBDlNI1RVs1QD09uTSbPIZ/iQB4dqauMJY64g8N1w13JZG5vnAtUhYEZ1/T3kncF08N6D9zt6zZBPHOanEhyvQLkkl+9nEWRtfGEnyAiwD2GxIAlAVT/Kz1bcx6A36P7mo1bNHdzs/e5An+PPnrwU12YcF8kSnPvKTrsxWXP7bgWYauAINi6uDQfKIaRy76PyKS4USLU5AnyrpRqw80zhWEbmSQxd/7S49ZMlqNyJcNJk03LqrmtlVjyjQqgONCVg4m3i+afeGcgH6ZlmVFq40l5jGIX63e0qpY1Xsum4AmvlzNmDNpQeWGLc0m5xEgVYdaLfk0h74/JhpvE0JRacwCOayBZr0l+upkq/YxLOPKSj585eMD+Cf3mezVCYJMv6mpdnkJAq06kB/e0fyD1hOxpNDqyO5lU4ni1n9CFcJ9LUSaTvMBaRM45E5wp7M+30xEbvAau3XY0Tt44yQLi3NJ2tRoFUHmrQjLKcRm7gAmtV6txJoItQvgk1cx4SiMFnECkc2QCusdOjMo4+/Dn673rxFgeYH6Av54nZLI5lbTrY/7WoIdMDXZaOWHM59wjSuTVTeg/zTEaNZ/yp+u36t7IjN/Jajk4Mo0PwATbQxoSiaz3o0BnTiDxVtVsYWMH66k0V4znNMDi1FvoalbK20yGNkhXS/xeCWoZODbI/m52yJLqhjElxiCxlD6nmskFGaJFir8ENUTQI6MKNsJCznn+oGmmjryeKlbOKvjS/8QRI2x40t0AqoPUeVyw4v430rqVrkn37PHh3p1lRwSyllfevbI7U0jEnaTQUrlha8pYA+fftRm9XHCn9sDqCjrzzURrswfhAOBtrTb0+fGCnyHsPpUWnkV9iSPeZ+spjVnzU/pWrQ27A5qaWBJtp2snhRcwBNtOpYYSqbNFC2rdJDVju5AF0PttfoUkmwqbcsyt7g2YO8lnu+s6qiQDMDmryLBpPDmuYA2u/MPWPyCGGmadhE5RfcSk/oLvI2eKQK1Ipnc3gMl8MnzxfvmHRevGOiULzTSCgOMhYC9nBJ6Cw36b4FS2RHHYbJU300c+mPAs0MaKJ1x++cbA6g92f9+t6yyLwcpmksCs995pN2dyqstF3l9iFqfxa0yHNknXjnV2Vivwn7JbtnL6xO9dGsd6xQoJkBTV4yz8ZycgWaaFNikSPLemZUZ4S0kQSZxKgb6JeXAIc8g7uSLwkyDqmK26Bfc+34u3ywwVkUaOZAH7v2e1u7mIKfmwPoPZn3O1mx2JNtFZFbG3Xl4b9qLkXoiHzH32lWqJWW22dsjSTQ+FB1mn93PvjgJAo0c6CJPFJLNzQH0EQrjxVeZpOWW0qpPYlXFbdxCPzg4paA+gXYdyV75218nB2u3ieNvk4UaHZAwwp+hO85PV+aLdDwiy3ZPOHJPqbgR+XDb6pi1gwk+59bCmqysw+TyePyJLfmnTxSoNkBTbQmrjC9OYDed+G+9vKj+feZprXocG4t6lr/vvCqY+tHi3wMr7cc1Hp1Yt9xP8O3br47khRo9kB7pJROBjzP1A000baTxaHs6lv40vvCq+I36YgDppxtyZcHkd8ySvfOG9FYHXkVAdrqcG6dY3QBo0Dg/18H+vClB+/bRucXNgfQfmfu6rLZ8IT05Kf/8pJQ+UmXdpI95qtFPmSdumVeJCTyHHkfvr36LbWmPvBck4Emcj1VovIDH5kATQTfmPGaNAluySWv3Z8hT/UdRG6QkD3RLQG1eKdRqTxha3eOuDATBZob0AcvPuiiylsA2ADtkVq6lU2aDrEFGY2l9eTOFS1ZpN1oya6poSKv0c0MtR6ZKGZyYYWxKNDcgCZaG3/nSnMAHfJNeeelkXmVLMpfizgDm0q39rv4rrJw68XiXdMiRL7jfsQErlnAlh6yWs+UEdaiQHMH2impxFyVd4gzBbq44nGrTQlFiWzS3XqyOIhNX1Sn+mpLw60EVTFrTTCJtJAdstwu9hvvJnLTd5PsmZMm3jn5tshjOE/+9Kg/qo5v6s6mfIxFgeYO9NErDz/E5JDxshpXoIlQBz02T1lacTS/Mv9hNa+75mqvCbWrYlabiwOnRYu8xshUgVoSPOMMn2WrFwWaO9BEzkklwc0B9I27Mi2cW840XQL/jrP3RqvWQ69X7feJWrLoVXqSIJMLnF+K6jb06eP0oN5N58ZSFGjVgD548dfPlqgwOWQKNJFTUrEXm7TXH7+Twr13mlbNxSNa0v0WlqyeZ9fQSofNi+S9UBRo1YAmsospuN0cQAdllPdl84Ql64g8sX/6vU+49Q5zVR1btwQWt5q1L+0z9o/qs7s+5rUwFGjVgSY/VF3EcXLIBujSP2q0UB9Wv2ZxTCjawq132EkWaTubvDeFFdSug+tkUXZLeC0IBVp1oAMzyjrAGv6mbqCJPFJLjdmkj8lhPvueYa/nsop3xEEmSazdDsThtSAUaNWBJtpyopjT5JAt0LkPqlvbROX/wTR9sqwYeK5sCLue4Sb40x3JQ9XZAC32m1DBayEo0PwAvffC/YHNATQR3IgINnlsO1m8j20eXCXZM/sgu9UO/bqnpTf4+wkXBZofoIkwOfylOYDe9XXZQDZ7suEOVQR8Xcbs1Q8qSn7SbTRbtwP+d3/eCkCB5g9op5PFa5sD6NjvftNyiC24xjQP4nZ4ppYuZZsPF/15O6012z0iVfGOprwVgALNH9Ch58s/Xn40/zvEz2EaYNVzuLSdd9pdczb5rI4r5P+dgI0IfnQRq4nh3nnmvGVOgeYP6N+kf77jlFT80abEIh2mwTW5hNMrIirOR+iWp+wOI6EswS/sXozLK6F0nx3CCkUoi3QM4JIPF4k8R+WwmhgGGf/XAE2eds84AOguANqQTRwAbYQ66rKJA6BNUEeNfnpQlXALq3d8i3dMZO3acBVrCx32X2KhqbhLEmw6kPVqQvF3/L7kshHBh37Gpmxy4WbNAvrWrVta169f5/3pOQEBAa0sLCwYd8K1a9fa/vzzz23/eryiouKdxYsXa78p7ubNm7UmT57cYffu3a24lJWrrK2t27q6urK+GtReie3LdjUBk6+p6qhDQ1Wn+gxnWy7pIUvNWuUwNjbuM2zYsHDeCvVC69evN/zss89KyeeuXbsaffXVV0ZvOl9fX996/vz51n89vmbNmk86depUEhsb2+hP6seMGRNhYmJyfO3atWrf+6Cnp6c9YMCASPJ51KhRERhIrG9PP/ujTIvtaoJ034ITvFfmL5LutwhiBbTr4Lo/f0z+iLcC8AG0oaGhoG/fvsLQ0ND2K1as6CUUCl+yOI6Ojp/Y29v3TE5Orn8NgpeXl866des6k8+7du1qm5iY2Hbbtm06JH5UVJQi/uXLl7USEhL6pqamttXV1V1qZGS09NixYwoLHBYW1pqc6+zs/FFkZGTbAwcOtO3du7cDBpfD6+qZlJQ0kFhq5PsB8tFycHDQ3bJly/vkOxIXgyHf09OzAz4rLLSLi8sHq1ev7uvu7q7Ij8QNDg5uv3Xr1s5BQUHasOQfor4f2Nra6kZHR2uR7zEYeqJOL10JduzYoY10+oSEhLRF3u+T9BcsWNCvT58+3yINbdRP5+zZs4qrG+rWCul9Ymdn9+np06fffVFPrUOHDrVD2d5H2n327NlT/+JMke+4QjbwwLeVVB3f0pMbKU2rKmZNB+TxkJVv7zehktdC8AX0oEGDcoYPH55mamoaN3DgwPNOTk4fZmRk/H3o0KF7xo0blzZ9+vQ4dGJGv379Ply1atVAWMQbEydOzJ42bdoEwGqN7zNggc/BSsZ8/vnnV+bOndsPkHUYMmTIKcAwYfDgwVdHjx591dvb2wjp9cMAugJ4o/E5Y9KkSRn4zvpNQPfv3/9Sbm6uNs75GmVKnzlzZpxAILiMPAUbNmww6tmzp3TOnDkx27dv72hmZub4xRdfZM2ePVuIvzc2bdpkiLi9UK9S5Je4cOFCU5TxW9T7AsqdiKtTGspwmJQd53yPeH1InlOmTNmI767h//gvv/zyG5ThHODuDaCTunXrVoFBHtiuXTuTRYsWmZDzkVcyynMa7XIC5Uy5efPme2iDPsjzu5EjR36Ntj0B635BWSf40RFsL+/iwOkneQWogSRBxvvY/qoccdJ5LQRfQPfo0eMRLKbCsuJyum/p0qXm0ALAI1Seh+PG6LQ4WCBLdFLQ3bt3W9+/f//df//73w6AOk15no2NjSHgvwTgdBCyyLGOHTuaIx/F5AHQ3IKFrX/OA9yRdADv8CagUb4cSKdz584VsLL6L8ptiIEYQT6jnIr14IMHD3bCYPkB6SgeYzV27FgdlOXG1atXh+jo6JT4+PgQi63ToUOHcljLD8g5n3766RUMTGfyGYNiAlwIf1w5OmPw3kBdFelgoOjAfapEuQWkXihr1ouikXYyHz9+vB1g3aAsLwbCckC8lZyMMueibRXp4NhBKysrxd6MqviNpqyft0F2uEWvWsAKEgaSHbExrHQbyrIsenWw6va8FoQvoGHh6ndNAU4HWBMHAwODWECsrzweGBjYEfBlL1u27D1Y6N0AJQmW7UMC9MqVK+tBTE9PbwUYchsDGmnmlpaW1k/eYM1XMwUasNbfyACsAkCmGHBKoC0tLaeAr7CGcQHRbbgVM1FmZVwCZ5byewAthC+smNggrgAwhsGKmyGvVQ3TQV2SGwO6TZs2YSkpKfXtigH07xEjRlwnJ8MI1O/FeP/99xfAss8inx9/s7eDyMfwN7ZWWuQ+TCyLXDHjde3ERdWpvibw50Wsy+E1Rio/vYPfR4Xx6UMr/1eChcvnWrgCHsrjuJQOBqhnr1+/3oqEqVOnOiBuGAEarsVB5Xnksgz92BjQSCMHl+36yRsAj2AKNCaHWQ3L/Veg4X7ownW6vHfvXoWvCh/4PQzW7zMzMw1Qn3qgGwD5N5IGSYt8VgINH1yAOmXD31akA9+5DdqotDGg4ZI4w0WZpUwTbsh0uDX+5GSSXoOqmCON+mUu6SGrMLYgKYKbfq0sdo1VzZVYzo+/rbl4pJX04JKvRJ4juf1iJXTmUa55Nyp1Ao1L73vwG4/j/wj0SyDCD7h06iNswPmxgOw8LrXzCNCw5rdJGrDavgD2NuCZ2BjQuKzPxlXgB5zv26tXLyFgvM0X0EQYhLuQ1jkEL5TlewzEGYgrYAM0+QwLG4jB8A3K6ImynkdajQKNgaSNMtxE/Q+hbmFwhW4uXrxYpymg5afcu5AHkHOE+qkkcFq6/IQL67uVNd8e1YH/mwg34wmnvOEqVZ/ZOYhtvk2KD6BxmW4NkOovHfAntdHoitk+Zv+t4H6MBoQmmNwpZvORkZFamEyNmDFjhh75nwANi+tgZGQkwATKFBM/xc4wTLK0ELqTz7jct0c+9WvdXl5enefPnz8TaQtwXBvpazfM969C2rpFRUVacDO6Nyw3IFWUG26LbsPzYSEFOGZma2urOB9xW8O3V5wDxrRwdalPh6RB0iKf161b13revHmdld8BSgH+N3Nzc+uCeUMXlLs1qZcyPtJqv379ekW9PDw8WiPPCZiUTlDOR3DuS+mR85HGS2v+khCzRE5Q1V/6R9eKA6ZEyGJW69VejW30fsLjrENt5YlOepJQs3DEUfFX36YXG8tHJWnCnUIl0Hym+b+kquObesJKi1UB7IVv/VTkbVAu3ml0Vuw3IRR/3QC6m3jHxBCx/6QUfFci8hiu8isvkI+8Km6DnloaQxOALigo0EZow2ea/2uShVuvaqkHMbIN0gOLPNXWEJoANJXqwuTu77CkmS0Na1MBFj+/5lLkK9sTeBMFmruWLFnSH36vyvsQ0tLS2iItlZfRqtP8u4p8xrLa6dacAWWrkAu39FK1nm8UBZq7iO/f2KoKG4WFhekgrSweivQ3+QmXASLvMfKWhvcVmOE3yyKWvx3Ph3ZwcOi8cuXKLaNGjXLv37+/cOnSpYMmTpw49IsvvhBiZr8tJydHsYfD0tKy69ChQ4MGDBgQb25uvhD/O/n7+7ezsrLasnjx4vGDBw8Wjh49OgyzfsVdMXd393YTJkxw7NevnyKd1atXr5wxY0YXsm9i7ty5Q/T09OIQItasWWNob2+veKIlzvlw/PjxYSQOymNhY2Pzd+TfFuULQJksBAKBcNKkSeaurq7dhwwZEvHll1/uNTU1VeSHc9obGhp6kOVDIyOjbT4+Pv94UW7nWbNmjcO5wjFjxgRu3769jZOT00CU90eU78cNGzbU/6qarKQgXxe0QwTK1BVt4x4QEKBYsYiJiXkXltgLddYeNGiQP8ruT1Zl0F4HPv300wr8DSTnYZAIhg8fHoF2ip02bZrRi3p1QT1XoOz+SDuaLA9OnTp1GmlLHFseGBhYv09GdmydASZwnF6VrCaYK8W7phqok+N68bUO3atXr6fo8Kljx47V79GjRzmOxZN9Ep9//vnRhQsXGjo6OrZGR+QCqnnoAIGBgcHejh07lqNDdbp3734bIF8GtAJ05oYpU6aEkHQBzxl0rPf06dMF+Ly4a9euj3FYYGJiMqxnz55XJk+erI9z9cmtaoSzZMkMkJzPzMysu3fvXh3cgedIN4CsPyOPCgAQjPwFvXv3/mHkyJE3Aak+YN6AMu8g+SHuWQC0FekKMPCcMSj8yPEOHTrcJmUh5QbEG1D2jcirPayqJz57YnDVL3XZ2tr2JzAC9BGzZ88ege8dZ86cuYh8BwgHDRw4MAPf26AczmifmYjbDceHdurU6bq+vn7PzZs368AQ5GKwjUS59ADsBbSREVmP7tatmxjpzsKgmIt2LUUd9pIyoS3OoB1eWjWoTg80YPtIAbXA7DmqWha9qnlgJuLxxsol5f+6uro30Gk9yGczMzNzgGyNzpkLKF66bw/IfiRAYzDcwHc9lMfRsTmJiYk90YeZxBorjwOmZPwRIL1kQFJ/Sx0WWR8dfBYDB/wY1IWGhioCrFYdLGEtARpxKkpLSxWWElZeCJgdyeeysrIO5Ja2s7OzLvKTIg2hMqBcvwG2TgD3KuD8lJx/586dTkhTsUHodS4H2V2HstxGmxg9ePCgVXR0dHtyQyk4OPifAPUEBiNZkzfEoLqEMnx+//79dxq6HGg3R0B7RVkGnJuOwZVNgAa4kcp8unTpknP+/PkPyecRI0Y4AO5XXJ/qs4GfYBKWzvmBiioFvTrxrmnXquI2dGWIIj/iC+g+ffo0vFOYBcAVd5/IXTAAaofL8CJYJcuG8QDMVQI0OioLlrT+bhXAzYmKiupLwG14PmAleQhgSb9ZsGDBAOVxWDl9WLKzuCybkZ10ggaC1R9IgEbc+geazJs3TwiXQwEABsz7yDsHVk8Ai5zcMC4s+hcuLi6tAU8W/uooz0daijuGjfnQKA/ZmZeCdlFsAkK6B2D5zVCfa/Pnz9fKz89vBVD10Wbfw7IObwg0Br4/6rC4YTkQlwxuAb6rv2OI9OvvbCIfB3Kn9HX9+zgjpLX0kGWIyH14s72GgqxnS3bP3otJasu8p5AnC/0S0OT2LvmsBBrWqD2O56KzB+/atetjdKS9trb2QwI0LHoW0ngJaPIXLgyx9LP27dunA7iGwkWpwmGBtbW1OazSd0izNyxnX8D8HQbHWbg1H8I63gBk/WGhdeCqrMR5Ca8D2s3N7SWgyWek8z3ANt69ezc53wjH03Nzc7Xg32bhfEZAwwXovGjRov6rVq2aBBdhDzkGN0SANOS4Mpi9OEcPg68n/m5Hee0bAo38ewH0TPjzPdeuXdsZV5+DcE3MCdBk34syH1h7RkAr9fhcaHfxjonxAFt97wJ3G/pUEjLjkjzRSW17rpsUH0DD2nwGQHcq/4clPoBLq+IWNCY6hnA7ZpPPAGkcOiID8GehkwLRWVHbtm37EJfYQ+T2tTI+/FrF4Ni4cWMPAC0kwOOSegJAhJAr708//dQFHW+KY+dgtYjfu3jYsGGJJA4A00XnZhKrD/DiAbU2gG6PcVW/79bOzs7Tz89PsQcZgLbFwIgjny0sLPogzTMkLsp5cvny5R3IcQBzGOd/oDwfacW9OD4f5TBr2BY41hlxM2GNL6NdFG4U/GJtQJqfkpKicHmQx3gMnos47xTq/dH+/fs/gNtzWJkG6rkIbs1FxMkG9DvhrpAtALoYvPXbS1HPBOVnWP3ZaOM5TfV1zZWYd2WRtnriwOkZ8K95A1tEQA42vS6Lsh9d/XWQVlPlUKvexmU7DARrXHJPkH0c6PwBZJAAHrOmY7aMiI+Lq83mli5HQ9VkH/mXNNx6pdj/q3Ow2pWV21k8OXT7EOJWiCRBJt9L9y9cW3PxSOemc2wmvY1AwyUgm4yMhwwZIoQ/LYSFnubt7d2sP25lI3t7ew+4Q5rT6X8RJm6dq2LXjZOEmDnCZRAi/Cz2m5Aj8jZQBLHf+BxJ8IwcACwUBxk7yk84G8Mad34u/c+EXWMEoNsvZPHMChIANO+/8KaioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKi4qD/B8knJA2V30/QAAAAAElFTkSuQmCC
--#

--% /smartapp01/api/web/public/index.html
<!DOCTYPE html>
<html lang="en">
  <head>
  <meta charset="utf-8" />
  <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <meta name="theme-color" content="#000000" />
  <meta
    name="description"
    content="Web site created using create-react-app"
  />
  <link rel="apple-touch-icon" href="%PUBLIC_URL%/apple-touch-icon.png" />
  <!--
    manifest.json provides metadata used when your web app is installed on a
    user's mobile device or desktop. See https://developers.google.com/web/fundamentals/web-app-manifest/
  -->
  <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
  <!--
    Notice the use of %PUBLIC_URL% in the tags above.
    It will be replaced with the URL of the `public` folder during the build.
    Only files inside the `public` folder can be referenced from the HTML.

    Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
    work correctly both with client-side routing and a non-root public URL.
    Learn how to configure a non-root public URL by running `npm run build`.
  -->
  <title>React App</title>
  </head>
  <body>
  <noscript>You need to enable JavaScript to run this app.</noscript>

  <!--
    This HTML file is a template.
    If you open it directly in the browser, you will see an empty page.

    You can add webfonts, meta tags, or analytics to this file.
    The build step will place the bundled scripts into the <body> tag.

    To begin the development, run `npm start` or `yarn start`.
    To create a production bundle, use `npm run build` or `yarn build`.
  -->
  </body>
</html>

--#

--% /smartapp01/api/web/public/favicon.ico
AAABAAEAMDAAAAEAIACoJQAAFgAAACgAAAAwAAAAYAAAAAEAIAAAAAAAACQAAEZcAABGXAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANqmbQDap24E1p5gT9adXmzWnV5s16BjN8yGOAD///8A////AEZGRgJtbW0B////AEpKSgJQUFADOzs7GTo6Og4pKSkBe3t7AP///wCYmJgAQUFBAo6OjgD///8A////ADo6OgFOTk4HR0dHB05OTgGVlZUAPz8/ApOTkwD///8A////AP///wBOj/AAWpfxBESJ7x1Bh+84P4buPkKI7i1Mju8Pv9j5AICv9AAAAAAAAAAAAAAAAAAAAAAAAAAAANmlagDZpWsJ1p1dvNWbW//Vm1v/2J9hgykxOhY5OTkpPT09Lzo6Oj46OjpGOTk5Jz4+Pj01NTVGPj4+Wzo6OlxMTExPVlZWO1xcXC9EREQ5PDw8Sjo6OjJDQ0MrOTk5ITs7Ox83NzdDNzc3Pzk5OTo4ODg0PDw8STo6OjM7OzsoOjo6IWeGtAJAh+40OIHumTR/7dozfu3xM37t9DN/7eo2gO3EO4TubkeL7xM+he4AYpzyAAAAAAAAAAAAAAAAANmlagDZpWsJ1pxdvNWbW//Vm1v/2KBhgiwxNyIzMzNRNjY2SDc3N0M2NjZUNzc3STw8PEUxMTFLNDQ0REVFRVl3d3eCUFBQWj8/P1M9PT1NOzs7WzQ0NE04ODhJNDQ0QTw8PCk9PT1DPDw8Qjo6Okw1NTVYOjo6WjU1NU80NDNQNDU3Lz2F7100f+3iMX3t/zF97f8xfe3/MX3t/zF97f8xfe3/Mn7t/DaA7bE/hu4iMX3tALDO+QAAAAAAAAAAANmlagDZpWsJ1pxdvNWbW//Vm1v/1p5ghP//EQA6OjoHOjo6BTs7OwZMTEwLR0dHDjk5OQREREQGPDw8B1JSUgVRUVEGUlJSBDU1NQc2NjYENDQ0BUlJSQQ5OTkJPj4+ET4+PgJMTEwFU1NTA0VFRQpCQkIRNDQ0BUxNTQVGGgAFPoLnTTR/7eoxfe3/MX3t/zF97f4zfu3yM37t6zJ+7fkxfe3/MX3t/zF97f83ge6wSo3vEkaK7wAAAAAAAAAAANmlagDZpWsJ1pxdvNWbW//Vm1v/159ggxolMBExMTEiNzc3Nz09PTc0NDRKNTU1STU1NTM0NDQrNzc3NzAwMDwzMzMKNDQ0JTY2NiUwMDArOjo6MURERD5EREQtLCwsIjg4OCg5OTk5Ojo6OjExMS05OTk3NDQ0Ni0rKCFIaZkjNoHvvjF97f8xfe3/M37t7zmC7ow+he48PITuLT2E7lc2gO2/Mn3t/jF97f8yfu37PITuZh5x6wAAAAAAAAAAANmlagDZpWsJ1pxdvNWbW//Vm1v/2aBhgiktMis3NzdQOzs7Rzo6Okk4OTlRNTY3STY3OVE1NjdcODk6Ri8wMVgwMTITNzg5PDk6O1AyMzRXOzs8TUNDQ1M+Pj5YNjY2Uzw8PE08PDxHPDw8WDc3N145OTlLNDQ0TDYzLUk/c8FfM37u8zF97f8yfu35OoPub3Gm8gNPkO8AmL/3ADqD7gBIi+8dNYDtvzF97f8xfe3/N4DuuFWU8AsAAAAAAAAAANmlagDZpWsJ1pxdvNWbW//Vm1v/159ghCUyQQ1DQ0MQR0hIB0xJRgiqg1gXqoJWIpByUCx5Y0ouqoJXIJFyTyuuhVcekHRVJaV+VCODaEoygGhOI0tKSghQUFAKSElKDDA5RgcoNUQGJjA8DTY6Ph5EREUOQ0NDB14uAAY7g+1vMn7v+jF+7/s1gO7NS43vF0qN7wAAAAAAAAAAAFmX8AAvfO0AOoPuYDJ97f0xfe3/NH/t3ESJ7yIAAAAAAAAAANmlagDZpWsJ1pxdvNWbW//Vm1v/1p5ghNGQSQDgtYYA3KpyAN2ueATWnV6V1Ztb2dabW9XYoWSs1p1dy9abW9bWnV7J2KBjsdWbW9bWnFvY155fierJpwHgr3kA5beEAtefYV7WnV2O1p1djdifYG/dqW8J3qpyACxfsgCsm5B5oZWS3qCUkd+alZqTg6rmBI+lygAAAAAAAAAAAAAAAAA1gO0AOoPuSTJ+7fgxfe3/NH/t4kKI7ikAAAAAAAAAANmlagDZpWsJ1pxdvNWbW//Vm1v/1p5ghNGQSQDgtYYA26lyANyteAXWnV6y1Ztb/9WbW//XoGPP1pxd89WbW//WnV7x16Bj1dWbW//Vm1v/1p1fpOjHpALZpGkA2aRpINadXtnVm1v/1Ztb/9adXszZpW0Q2qZtANmmbhTXnV3J15tZ/9icWfzboF5l0pdZAP+/WQAAAAAAAAAAAFOS8AD///8AOYLugzF97f8xfe3/NX/t0EiL7xkAAAAAAAAAANmlagDZpWsJ1pxdvNWbW//Vm1v/1p5ghNGQSQDgtYYA26lyANyteAXWnV6y1Ztb/9WbW//XoGPP1pxd89WbW//WnV7x16Bj1NWbW//Vm1v/1p1fpOnIpgLUmVcA16BjZNWbXPzVm1v/1Ztb/9adXsvZpWwQ159iANehZE3VnFz21Ztb/9acXdvZo2gh2KJnAAAAAACmx/gAKnnsAFqX8Qg+he5aM37t6DF97f8xfe3/OYLumo239QMAAAAAAAAAANmlagDZpWsJ1ZxdvNWbWv/Vm1r/1p5ghNCQSADgtYYA26lyANyteAXWnV6y1Ztb/9WbW//XoGPP1pxd89WbW//WnV7x16Bj1NWbW//Vm1v/1p1fpPPgzgHcqnQK1p1ftdWbW//Vm1v/1Ztb/9adXsvZpWwQ5sKbAtaeYJ7Vm1v/1Ztb/9efYJb/47wCSIzwFj6F7k06g+52N4HuiTeB7rUzfu3yMX3t/zF97f80f+3nQYfuOzWA7QAAAAAAAAAAANmlawDYo2QJ2KFuvNiicv/YonL/2KNvhNWbbQDgtIUA26lyANyteAXWnV6y1Ztb/9WbW//XoGPP1pxd89WbW//WnV7x16Bj1NWbW//Vm1v/1p1fpMR1HADYomY61Zxd7tWbW//Vm1v/1Ztb/9adXsvZpm0O2KNoJdacXeDVm1v/1pxc89Gga0k2g/RVNoDtyzJ+7fgxfe3/MX3t/zF97f8xfe3/MX3t/zN+7fI7g+5siLP1AleV8AAAAAAAAAAAANmkbADXoFwJ26eDvNyqj//cqo7/26iChNunmQDgtIMA26lyANyteAXWnV6y1Ztb/9WbW//XoGPP1pxd89WbW//WnV7x16Bj1NWbW//Vm1v/1p1fpP///wHXn2GI1Ztb/9WbW//Vm1v/1Ztb/9adXsvbqXIN159ibNWbXP7Vm1v/1Z1gxE6I338yfu7xMX3t/zF97f8xfe3/MX3t/zF97f8yfe39NX/t1T2F7l5WlfAFTI/vAAAAAADCcgAA4rmFBeK5gQjcqmwR26eCvtyqj//cqo7/26iCiOS/cQXht4AI47yOCOG2hw3WnV+01Ztb/9WbW//XoGPP1pxd89WbW//WnV7x16Bj1NWbW//Vm1v/1p1fotqnbxzWnV7S1Ztb/9WbW//Vm1v/1Ztb/9adXsvap24d1p1eu9WbW//XnFr8npaWuTF+7+kxfe3/MX3t/zJ+7fQ1gO3JN4DutDiC7p87g+5mRYrvIJe99wBemvEAAAAAAAAAAADrx/8A26mAbtyqh7zcqoa826mI7dyqj//cqo//26mI3dyqh7ncqoa52KJsudefYrvWnV3q1Ztb/9WbW//XoGPP1pxd89WbW//WnV7x16Bj1NWbW//Vm1v/1p1foNihZVzVnFz61Ztb/9WbW//Vm1v/1Ztb/9adXsjYomdQ1Zxc8NWbW//SnGHrV4jT1i997v8xfe3/M37t4jyE7llNj+8PZp7yBoez9AJUk/AA////AAAAAAAAAAAAAAAAAAAAAAD+6f8A26eEl9yqj//cqo//3KqP/9yqj//cqo//3KqP/9yqj//cqY3/159o/9WbWv/Vm1v/1Ztb/9WbW//XoGPP15xc89ebWf/XnV3x16Bj1NWbW//Vm1v/1p5gqtaeYK3Vm1v/1Ztc+9aeYODVm1v+1Ztb/9adXsvXn2Ke1Ztb/9abWv+7mnrKN4Dr5zF97f8yfu39O4PubwBT5wBUk/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD21v8A2qeBkNupivfcqYrz3KmN/Nyqj//cqo//3KmM+dypi/PbqInz159o89WbW/PVm1v71Ztb/9WbW//YoWPGxZxyy7WYfc/JnXDN2aFjztWbW//Vm1v/1p5g1dacXerVm1v/1pxd39egY5zVm1v/1Ztb/9adX+bWnV7l1Ztb/9icWvWWlJ6QMH3v7zF97f8zf+3qQofuLUCH7gAAAAAAAAAAAGyi8wA5gu0ASIvvIUKH7kFBh+5HRYrvMXep8wHiqeMA2aNyI9mkdzzZo3RC26eDzNyqj//cqo7/26eBodmkdTnZpHY7155kO9adXz/WnV3E1Ztb/9WcXfCIkqu4O4Hp2zR/7exAg+bVnJaZuNacW/fVm1v/1Zxc/NWbW/7Vm1v/1p5gndefYnfVm1v/1Ztb/9WbXP7Vm1v/1Ztb/9idW8tojcpTMX7u8TF97f8zf+3rQYfuLz+G7gAAAAAAAAAAAFqX8QD///8BOYLulDN+7fkzfu37OYLuncfc+gEAAAAAAAAAANmkbADXoFsJ26eDvNyqkP/cqo7/26iChNunmQDhtYQA26pzANyueAXWnV6x15ta/7KYgsw1f+3nMH3t/zF97f8wfe7/PoLn3cKbctXWm1r/1Ztb/9WbW//VnFz32KFlS9afYW/Vm1v/1Ztb/9WbW//Vm1v/1Ztb/9mfXoJBi/YjNH/t4TF97f8yfe3+OoPud////wBSkvAAcqbzAD6G7gBEie8kNH/t1zF97f8xfe3/OoPufhFp6gAAAAAAAAAAANmkbADYoV8J2qV8vNunhv/bp4X/2qZ8hNmjigDgtIQA26lyANyteAXWnV6y2JxZ/4iRp8UvffD6MX3t/zF97f8xfe3/MX7v86SXkcvXm1n/1Ztb/9WbW//WnV7K3Kp0ENaeYXHVm1v/1Ztb/9WbW//Vm1v/1Zxd7NmiZDcAl/8DOIHupjF97f8xfe3/M37t6DyE7mdKje8XUpLwDkGH7jQ2ge2yMX3t/zF97f8zfu3uQIbuPDqD7gAAAAAAAAAAANmlagDZpWoJ1p1gvNWcX//WnF//159jhNGSTwDgtYYA26lyANyteAXWnV6y15xZ/5qUmccwfvD0MX3t/zF97f8xfe3/M3/u7LGYg83Xm1n/1Ztb/9WbW//Xn2J90ZFLANafYXPVm1v/1Ztb/9WbW//Vm1v/1p5ftNyrdQlUh9UAQIfuPzR/7ecxfe3/MX3t/zJ+7fg1f+3VNoDtyTN/7ekxfe3/MX3t/zF97f84gu6ZWpfxBk+Q8AAAAAAAAAAAANmlagDZpWsJ1ZxdvNWbW//Vm1v/1p5ghNGQSADgtYYA26lyANyteAXWnV6y1pta/8ycaN5Th9bMMX3u+zF97f8xfu74Z4zIx9KcYejVm1v/1Ztb/9WcXejYomcx1ZxcANafYXPVm1v/1Ztb/9WbW//Vm1z816BiY9SZVwBfl+sAjLf1AjuD7mQzfu3sMX3t/zF97f8xfe3/MX3t/zF97f8xfe3/Mn3t/jaA7bNFiu8dPITuAAAAAAAAAAAAAAAAANmlawDZpmwJ1p1fuNWcXP3VnF39159hgdGRSgDgtocA26lyANyteAXWnV6y1Ztb/9abWv/DnHOXOYTyYzuE7oo9hfBZzJ5sotabWv/Vm1v/1Ztb/9aeYKvdrnsG1ZpZANafYXPVm1v/1Ztb/9WbW//WnV3Z2aRpINijaAAAAAAAUpLwAF+b8gM+he5LNYDtvTN+7fMyfe3/Mn3t/zJ+7fs0f+3fOYLuhkeL7xk8hO4AYpzxAAAAAAAAAAAAAAAAANysdgDcrHcD2aRqOdmjaE7Zo2hO2qZtKNSZVwDiu5AA26lyANyteAXWnV6y1Ztb/9WbW//Xnl+QxH8wAOK2gQD///8A1p5gntWbW//Vm1v/1Zxc+tegY1jVm1sA1JhWANafYXPVm1v/1Ztb/9WbW//WnmGU8d3HAd2ueQAAAAAAAAAAAGae8QAte+0ASIzvDz+G7j86g+5mOYLubjyE7lVDie8kU5PwA02P7wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA26lyANyteAXWnV6y1Ztb/9WbW//WnmCRyH4qAOC1hgD///8B1p5gntWbW//Vm1v/1p1e0tmkahnZpGkA1JhWANafYXPVm1v/1Ztb/9WcXPPXoWVE1p5gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA3Kx2AN2vfAPXoGNj1p5gkdaeYJHYoWRQyoMyAOG4igD///8A2KFlWNaeYJHWnmCR16BjXeK4iwLdrXkA1ZtbANihZUDWnmCP1p5gkNefYnjapm4O2qZuAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////8AAP///////wAA////////AAD///////8AAP///////wAA////////AAD///////8AAP///////wAA////////AAD///////8AAP///////wAA4OQdwvgfAADgAAAAAAcAAOAAAAAAAwAA4IAAAAABAADgAAAAAAEAAOAAAAABwAAA4AAAAAPgAADg4ACBg+AAAODgAIEH4AAA4OAAgQeAAADg4AAAAAEAAODgAQAAAQAA4OAAAAADAACAAAAAAA8AAIAAAAAAPwAAgAAAAAP/AACAAAAAA+AAAIAAAAADwAAA4OAAAAPBAADg4AAAAAEAAODgAEBAAQAA4OAAQMADAADg4ABA4AcAAODg4MD4DwAA/+DAwf//AAD/4ODB//8AAP///////wAA////////AAD///////8AAP///////wAA////////AAD///////8AAP///////wAA////////AAD///////8AAP///////wAA////////AAA=
--#

--% /smartapp01/api/web/src/App.tsx
import React from 'react';
import './App.css';
import {MainView} from "./view/MainView";



function App() {
  return (
  <div className="App">
    <MainView/>
  </div>
  );
}

export default App;

--#

--% /smartapp01/api/web/src/react-app-env.d.ts
/// <reference types="react-scripts" />

--#

--% /smartapp01/api/web/src/reportWebVitals.ts
import { ReportHandler } from 'web-vitals';

const reportWebVitals = (onPerfEntry?: ReportHandler) => {
  if (onPerfEntry && onPerfEntry instanceof Function) {
  import('web-vitals').then(({ getCLS, getFID, getFCP, getLCP, getTTFB }) => {
    getCLS(onPerfEntry);
    getFID(onPerfEntry);
    getFCP(onPerfEntry);
    getLCP(onPerfEntry);
    getTTFB(onPerfEntry);
  });
  }
};

export default reportWebVitals;

--#

--% /smartapp01/api/web/src/App.css
.App {
  text-align: center;
  height: 100%;
}

.App-logo {
  height: 40vmin;
  pointer-events: none;
}

@media (prefers-reduced-motion: no-preference) {
  .App-logo {
  animation: App-logo-spin infinite 20s linear;
  }
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-size: calc(10px + 2vmin);
  color: white;
}

.App-link {
  color: #61dafb;
}

@keyframes App-logo-spin {
  from {
  transform: rotate(0deg);
  }
  to {
  transform: rotate(360deg);
  }
}

--#

--% /smartapp01/api/web/src/logo.svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 841.9 595.3"><g fill="#61DAFB"><path d="M666.3 296.5c0-32.5-40.7-63.3-103.1-82.4 14.4-63.6 8-114.2-20.2-130.4-6.5-3.8-14.1-5.6-22.4-5.6v22.3c4.6 0 8.3.9 11.4 2.6 13.6 7.8 19.5 37.5 14.9 75.7-1.1 9.4-2.9 19.3-5.1 29.4-19.6-4.8-41-8.5-63.5-10.9-13.5-18.5-27.5-35.3-41.6-50 32.6-30.3 63.2-46.9 84-46.9V78c-27.5 0-63.5 19.6-99.9 53.6-36.4-33.8-72.4-53.2-99.9-53.2v22.3c20.7 0 51.4 16.5 84 46.6-14 14.7-28 31.4-41.3 49.9-22.6 2.4-44 6.1-63.6 11-2.3-10-4-19.7-5.2-29-4.7-38.2 1.1-67.9 14.6-75.8 3-1.8 6.9-2.6 11.5-2.6V78.5c-8.4 0-16 1.8-22.6 5.6-28.1 16.2-34.4 66.7-19.9 130.1-62.2 19.2-102.7 49.9-102.7 82.3 0 32.5 40.7 63.3 103.1 82.4-14.4 63.6-8 114.2 20.2 130.4 6.5 3.8 14.1 5.6 22.5 5.6 27.5 0 63.5-19.6 99.9-53.6 36.4 33.8 72.4 53.2 99.9 53.2 8.4 0 16-1.8 22.6-5.6 28.1-16.2 34.4-66.7 19.9-130.1 62-19.1 102.5-49.9 102.5-82.3zm-130.2-66.7c-3.7 12.9-8.3 26.2-13.5 39.5-4.1-8-8.4-16-13.1-24-4.6-8-9.5-15.8-14.4-23.4 14.2 2.1 27.9 4.7 41 7.9zm-45.8 106.5c-7.8 13.5-15.8 26.3-24.1 38.2-14.9 1.3-30 2-45.2 2-15.1 0-30.2-.7-45-1.9-8.3-11.9-16.4-24.6-24.2-38-7.6-13.1-14.5-26.4-20.8-39.8 6.2-13.4 13.2-26.8 20.7-39.9 7.8-13.5 15.8-26.3 24.1-38.2 14.9-1.3 30-2 45.2-2 15.1 0 30.2.7 45 1.9 8.3 11.9 16.4 24.6 24.2 38 7.6 13.1 14.5 26.4 20.8 39.8-6.3 13.4-13.2 26.8-20.7 39.9zm32.3-13c5.4 13.4 10 26.8 13.8 39.8-13.1 3.2-26.9 5.9-41.2 8 4.9-7.7 9.8-15.6 14.4-23.7 4.6-8 8.9-16.1 13-24.1zM421.2 430c-9.3-9.6-18.6-20.3-27.8-32 9 .4 18.2.7 27.5.7 9.4 0 18.7-.2 27.8-.7-9 11.7-18.3 22.4-27.5 32zm-74.4-58.9c-14.2-2.1-27.9-4.7-41-7.9 3.7-12.9 8.3-26.2 13.5-39.5 4.1 8 8.4 16 13.1 24 4.7 8 9.5 15.8 14.4 23.4zM420.7 163c9.3 9.6 18.6 20.3 27.8 32-9-.4-18.2-.7-27.5-.7-9.4 0-18.7.2-27.8.7 9-11.7 18.3-22.4 27.5-32zm-74 58.9c-4.9 7.7-9.8 15.6-14.4 23.7-4.6 8-8.9 16-13 24-5.4-13.4-10-26.8-13.8-39.8 13.1-3.1 26.9-5.8 41.2-7.9zm-90.5 125.2c-35.4-15.1-58.3-34.9-58.3-50.6 0-15.7 22.9-35.6 58.3-50.6 8.6-3.7 18-7 27.7-10.1 5.7 19.6 13.2 40 22.5 60.9-9.2 20.8-16.6 41.1-22.2 60.6-9.9-3.1-19.3-6.5-28-10.2zM310 490c-13.6-7.8-19.5-37.5-14.9-75.7 1.1-9.4 2.9-19.3 5.1-29.4 19.6 4.8 41 8.5 63.5 10.9 13.5 18.5 27.5 35.3 41.6 50-32.6 30.3-63.2 46.9-84 46.9-4.5-.1-8.3-1-11.3-2.7zm237.2-76.2c4.7 38.2-1.1 67.9-14.6 75.8-3 1.8-6.9 2.6-11.5 2.6-20.7 0-51.4-16.5-84-46.6 14-14.7 28-31.4 41.3-49.9 22.6-2.4 44-6.1 63.6-11 2.3 10.1 4.1 19.8 5.2 29.1zm38.5-66.7c-8.6 3.7-18 7-27.7 10.1-5.7-19.6-13.2-40-22.5-60.9 9.2-20.8 16.6-41.1 22.2-60.6 9.9 3.1 19.3 6.5 28.1 10.2 35.4 15.1 58.3 34.9 58.3 50.6-.1 15.7-23 35.6-58.4 50.6zM320.8 78.4z"/><circle cx="420.9" cy="296.5" r="45.7"/><path d="M520.5 78.1z"/></g></svg>
--#

--% /smartapp01/api/web/src/index.tsx
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import 'antd/dist/antd.css'
import {
  BrowserRouter as Router,
  Switch,
  Route
} from 'react-router-dom'


ReactDOM.render(
  <React.StrictMode>
  <Router>
    <Switch>
    <Route path={"/"}>
    <App />
    </Route>
    </Switch>
  </Router>
  </React.StrictMode>,
  document.getElementsByTagName('body')[0]
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

--#

--% /smartapp01/api/web/src/setupTests.ts
// jest-dom adds custom jest matchers for asserting on DOM nodes.
// allows you to do things like:
// expect(element).toHaveTextContent(/react/i)
// learn more: https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom';

--#

--% /smartapp01/api/web/src/App.test.tsx
import React from 'react';
import { render, screen } from '@testing-library/react';
import App from './App';

test('renders learn react link', () => {
  render(<App />);
  const linkElement = screen.getByText(/learn react/i);
  expect(linkElement).toBeInTheDocument();
});

--#

--% /smartapp01/api/web/src/index.css
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
  'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
  sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-family: -apple-system,BlinkMacSystemFont,Segoe UI,Roboto,Helvetica Neue,Arial,Noto Sans,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
  monospace;
}

.ant-menu-sub.ant-menu-inline{
  background-color: transparent !important;
  border-bottom: 1px solid #e4e9f0;
}

.custom-text-btn{
  color: black !important;
}
/*
!* width *!
*::-webkit-scrollbar {
  width: 3px;
}

!*auto hide*!
.scroll-panel{
  overflow-y: hidden;
}
.scroll-panel:hover{
  overflow-y: auto;
}

!* Track *!
*::-webkit-scrollbar-track {
  background: #f1f1f1;
}

!* Handle *!
*::-webkit-scrollbar-thumb {
  background: #888;
}

!* Handle on hover *!
*::-webkit-scrollbar-thumb:hover {
  background: #555;
}*/

--#

--% /smartapp01/api/web/src/view/LandingView.tsx
import React from "react";

--#

--% /smartapp01/api/web/src/view/MainView.tsx
import React from "react";
import { Route, useHistory } from "react-router-dom";
import {Drawer, Grid, Layout, Button, Dropdown, Card, Menu, Avatar, Space, Badge} from 'antd'
import {
  MenuOutlined,
  AccountBookOutlined,
  ProfileOutlined,
  BookOutlined
} from '@ant-design/icons'
import PerfectScrollbar  from 'react-perfect-scrollbar'
import "react-perfect-scrollbar/dist/css/styles.css";
import fullImage from '../assets/img.png'
import compactImage from '../assets/img 900x900.png'
import {GovernmentCoverage} from "../components/GovernmentCoverage"
import {WQ5508} from "../components/WQ5508"
import {IRBDataCollection} from "../components/IRBDataCollection"

export interface ViewPortContextProps {
  isMobileView?: boolean
}

export interface ResponsiveMenuContextProps {
  collapsed?: boolean
  setCollapsed: (data:boolean)=>void
}

export const ViewPortContext = React.createContext<ViewPortContextProps>({isMobileView: false})
export const ResponsiveMenuContext = React.createContext<ResponsiveMenuContextProps | undefined>(undefined)

export const ResponsiveMenu : React.FunctionComponent = (props)=>{

  return <ViewPortContext.Consumer>
  {
    view=><ResponsiveMenuContext.Consumer>
    {
      state => <React.Fragment>

      {!view.isMobileView && state && <Layout.Sider theme={"light"} style={{borderRight: "1px solid #e4e9f0"}} collapsed={state.collapsed}
             onCollapse={state.setCollapsed}>
        {props.children}
      </Layout.Sider>}
      {view.isMobileView && state &&
      <Drawer bodyStyle={{padding: 0}} visible={!state.collapsed} onClose={() => state.setCollapsed(true)} title={"App Menu"} placement={"left"}>
        {props.children}
      </Drawer>}
      </React.Fragment>
    }
    </ResponsiveMenuContext.Consumer>
  }
  </ViewPortContext.Consumer>
}



export const MainView: React.FunctionComponent = (props) => {

  const [collapsed, setCollapsed] = React.useState(false)
  const [view, setView] = React.useState("#dashboard")
  const {md} = Grid.useBreakpoint()

  const history = useHistory()
  
  const account = React.useMemo(() => <Card
  headStyle={{padding: 12, textAlign: "center", borderBottom: "1px solid #e4e9f0"}} bodyStyle={{padding: 0}}
  title={"User 1"}>
  <Menu>
    <Menu.Item icon={<ProfileOutlined/>}>Profile</Menu.Item>
  </Menu>
  </Card>, [])

  const menus = React.useMemo(()=><React.Fragment>
  <Menu.SubMenu key={"menu-1"} title={"Menu 1"} icon={<AccountBookOutlined size={75}/>}>
    <Menu.Item key={"/sub-menu-1"}>Sub Menu 1</Menu.Item>
    <Menu.Item key={"/sub-menu-2"}>Sub Menu 2</Menu.Item>
  </Menu.SubMenu>
  <Menu.SubMenu key={"menu-2"} title={"Menu 2"} icon={<AccountBookOutlined size={75}/>}>
    <Menu.Item key={"/sub-menu-3"}>Sub Menu 1</Menu.Item>
    <Menu.Item key={"/sub-menu-4"}>Sub Menu 2</Menu.Item>
  </Menu.SubMenu>
  <Menu.Item key={"/wq5508"} icon={<BookOutlined size={75}/>}>WQ5508</Menu.Item>
  <Menu.Item key={"/government-coverage"} icon={<BookOutlined size={75}/>}>Government Coverage</Menu.Item>
  <Menu.Item key={"/data-collection"} icon={<BookOutlined size={75}/>}>IRB Data Collection</Menu.Item>
  </React.Fragment>, [])


  return <React.Fragment>
  <ViewPortContext.Provider value={{isMobileView: !md}}>
    <Layout style={{height: '100%'}}>

    <ResponsiveMenuContext.Provider value={{collapsed,setCollapsed}}>
      <ResponsiveMenu>
      {md && <div className={"ant-layout-header"} style={{backgroundColor: "transparent", padding: 0}}>
        <img src={collapsed ? compactImage : fullImage} className={"ant-layout-header"}
         style={{backgroundColor: "transparent", padding: 0}} alt={"logo"}/>
      </div>}

      <div className={'scroll-panel'} style={{height: 'calc(100% - 64px)'}}>
        <PerfectScrollbar component={"div"} options={{swipeEasing: true, wheelSpeed: 0.25}}>
        <Menu
        mode={"inline"}
        onSelect={(e)=>{
          history.push(e.key)
          setView(e.key)}}
        selectedKeys={[view]}
        defaultOpenKeys={["orders-menu", "invoices-menu", "reports-menu"]}
        >
        {menus}
        </Menu>
        </PerfectScrollbar>
      </div>
      </ResponsiveMenu>
    </ResponsiveMenuContext.Provider>
    <Layout>
      <Layout.Header style={{
      backgroundColor: "white",
      borderBottom: "1px solid #e4e9f0",
      display: "flex",
      alignItems: "center",
      paddingLeft: 16
      }}>
      <Button className={"custom-text-btn"} size={"large"} icon={<MenuOutlined size={75}/>}
        type={"link"} onClick={() => setCollapsed(!collapsed)}/>

      {/* {md && <Menu mode={"horizontal"} onSelect={(e)=>{
        history.push(e.key)
        setView(e.key)
        }} selectedKeys={[view]}>{menus}</Menu>} */}
      <div style={{flexGrow: 1, height: '100%'}}/>
      <Menu mode={"horizontal"}>
        <Menu.SubMenu title={<Avatar>JI</Avatar>}>
        <Menu.Item>Sign Out</Menu.Item>
        </Menu.SubMenu>
      </Menu>
      </Layout.Header>

      <Layout.Content style={{backgroundColor: "white",padding: 12}} className={'scroll-panel'}>
      <Route path="/government-coverage">
      <GovernmentCoverage/>
      </Route>
      <Route path="/wq5508">
      <WQ5508/>
      </Route>
      <Route path="/data-collection">
      <IRBDataCollection/>
      </Route>
      </Layout.Content>

      <Layout.Footer style={{backgroundColor: "white", borderTop: "1px solid #e4e9f0"}}>

      </Layout.Footer>
    </Layout>
    </Layout>
  </ViewPortContext.Provider>
  </React.Fragment>
}

--#

--% /smartapp01/api/web/src/assets/img 900x900.png
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ub9gNxJCAEAaEsLOIiF0z08KJx/nvMJOEO2KDf/3W9xbsAcJIQAgDQlhZ5EQ1gMthUSvxtCd47mvoBkJYfU+/PDDsa+99pqneOedd4ata+3atRP1g3/mmWf6P/aKE044wTv//PO9Z599Nve23X///d43vvGNxjJGjhzp///HHnus0v376KOPRixevNjfvlNOOaWxPsU555zjT5z83nvvPRj33T/84Q9LwmPx/vvvz0haR9Yxk+XLl3vXXHON95WvfKWx/uOOO87f56eeeqryc/ryyy/7lV97nhRa/xVXXOG98soriesM90VRdv06pnfffbd33nnn+fsZXX9aWQnX/fbbb5de/6uvvurNmDHDO+uss7wvf/nLjfWrDFx00UWeyoTOW9nlh9v45ptvxm7jM888459bletw3ToWc+bMyb1PL7zwgn+sdH2Fy9D51H59/PHHh5Td9iidqwceeMC/Rk4++eSma1LXyE033eStWrWq9LnQNREer6Rj/vjjj/vHy16j+m/tf9FyaMuv4rDDDmskKDr30b+nXdtl6b6je4u93rV/Kndp31u5cmXmsSpC9+usshrS9Wq3d/z48ZnbK7pO7fG89tprG8f78MMPH3a8y1zXuhZ0/0y6nxX57Unb/rjrSmVf64iWTW2PfiPyrEPXmK4je3y1jIkTJ7Z0n81CSyHRa7Hh379DMojhSAirFzxB90M/WPZvkyZN8vbbb7/G36Px6U9/2v/BS0qKZPbs2d6hhx6augxVgF966aWW9lOVKW3vAQcckLiuMPbZZx+/8hOtMKkyHH7m4osvTtyetGO2bNky/5h89rOfTd3nk046yVu6dGnL53bRokV+ZUPLTNvnz3zmM36ipM/b7ytRj3y2EB1DHUsd07T1a/tUDlQektav/ShaKX766ae9ESNGZO6/4gtf+IJfISu6j0EFrrEMW6FTYqXt/tSnPpW43i9+8YveQw89lLheVVCPOeaY1DJz4IEHevfcc0/L10iec6XYa6+9/HJcpuIdXBN+RFvoVP5UDtPW/bnPfc775je/massxJTfzEi7tstQGdA5Tlqf/pZ0HJU0hp9T8tPqtpx66qmJ9ya7vYccckjq9iY9qNM5sS2weaJIq6HKuNafdj0NBPeTgw8+2Js5c2bhY2a3P2jd9L3++uv+AyWV/aT1fv7zn/cuu+yy1Ac0l19+eeo1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AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACH/j8oQAwbu56jDAAAAABJRU5ErkJggg==
--#

--% /smartapp01/api/web/src/assets/img.png
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
--#

--% /smartapp01/api/web/src/components/IRBDataCollection.tsx
import React from "react";
import {  
  // Button, 
  Card, 
  Checkbox,
  // Col, 
  // DatePicker, 
  // Divider, 
  // Select, 
  // Space, 
  Table, 
  // Tag,
  Typography, 

  notification, 
} from "antd";
import {visualize, update} from '../api/index'
// import moment from "moment";
export interface IRBDataCollectionProps {
}

interface IRBDataCollectionRow {
  id: number,
  IRBCode: string,
  PrimaryCoverage: string,
  Government: number
}

const updateNotification = (field:string, status : number, rowsAffected : Array<number> = []) => {
  if(status===200 && rowsAffected.length === 1){
  return notification["success"]({
  message: "Successfully updated",
  description:
    `${field} field was successfully updated`
  })
  }
  else{
  return notification["error"]({
    message: "Unsuccessful",
    description:
    `${field} field update was unsuccessful`
  })
  }
}

const TableName: string = 'IRB_Data_Collection';

export const IRBDataCollection : React.FunctionComponent<IRBDataCollectionProps> = (props) => {
  const [source, setSource] = React.useState([]);

  const updateEntry = async (id:number, key: string, val: any) => {
  const data = {
    id        : id, 
    tableName : TableName,
    key       : key,
    val       : val
  }
  return await update(data)
  }

  const load = async ()=>{
    const {data:{rows=[]}} = await visualize(TableName)
    setSource(rows)
  }

  React.useEffect(()=>{
  load();
  },[])

  return <React.Fragment>
  <Card style={{ width: "88vw" }}>
    <Table dataSource={source} pagination={{ position: ['bottomCenter'] }} size={`small`} scroll={{y: 'calc(85vh - 90px)', x: 'max-content' }}>
    

    <Table.Column dataIndex={'IRBCode'} width={"40%"} title={'IRBCode'} render={(value, row: IRBDataCollectionRow, index) => {
      return <Typography.Text>{row.IRBCode}</Typography.Text>
    }} />

    <Table.Column dataIndex={'id'} width={"20%"} title={'id'} render={(value, row: IRBDataCollectionRow, index) => {
      return <Typography.Text>{row.id}</Typography.Text>
    }} />

    <Table.Column dataIndex={'Government'} title={'Flag'} render={(value, row : IRBDataCollectionRow, index) => {
      return <Checkbox 
      checked={row.Government ? true : false} 
      onChange={async (e)=>{
        const {status, data : {rowsAffected}} = await updateEntry(row.id, 'Government', e.target.checked? 1 : null)
        updateNotification('Government', status, rowsAffected)
        load()
      }}/>

    }} />

    </Table>
  </Card>

  </React.Fragment>
}

--#

--% /smartapp01/api/web/src/components/GovernmentCoverage.tsx
import React from "react";
import {Table, Card, Button, Select, Typography, DatePicker, Tag, Col, Space, Divider, notification, Checkbox} from "antd";
import {visualize, update} from '../api/index'
// import moment from "moment";
export interface GovernmentCoverageProps {
}

interface GovernmentCoverageRow {
  id: number,
  PrimaryCoverage: string,
  Government: number
}

const updateNotification = (field:string, status : number, rowsAffected : Array<number> = []) => {
  if(status===200 && rowsAffected.length === 1){
  return notification["success"]({
  message: "Successfully updated",
  description:
  `${field} field was successfully updated`
  })
  }
  else{
  return notification["error"]({
  message: "Unsuccessful",
  description:
  `${field} field update was unsuccessful`
  })
  }
}

export const GovernmentCoverage : React.FunctionComponent<GovernmentCoverageProps> = (props) => {
  const [source, setSource] = React.useState([]);

  const updateEntry = async (id:number, key: string, val: any) => {
  const data = {
    id : id, 
    tableName : 'Billing_Coverage_Government_New',
    key: key,
    val : val
  }
  return await update(data)
  }

  const load = async ()=>{
  const {data:{rows=[]}} = await visualize('Billing_Coverage_Government_New')
  setSource(rows)
  }

  React.useEffect(()=>{
  load();
  },[])

  return <React.Fragment>
  <Card style={{ width: "88vw" }}>
  <Table dataSource={source} pagination={{ position: ['bottomCenter'] }} size={`small`} scroll={{y: 'calc(85vh - 90px)', x: 'max-content' }}>
  <Table.Column 
  dataIndex={'id'}
  width={"70%"} 
  title={'Primary Coverage'} 
  render={(value, row: GovernmentCoverageRow, index) => {
    return <Typography.Text>{row.PrimaryCoverage}</Typography.Text>
  }} />

  <Table.Column 
  dataIndex={'Government'}
  title={'Government'} 
  render={(value, row : GovernmentCoverageRow, index) => {
    return <Checkbox 
    checked={row.Government ? true : false} 
    onChange={async (e)=>{
    const {status, data : {rowsAffected}} = await updateEntry(row.id, 'Government', e.target.checked? 1 : null)
    updateNotification('Government', status, rowsAffected)
    load()
    }}/>
  }} />
  </Table>
  </Card>

  </React.Fragment>
}

--#

--% /smartapp01/api/web/src/components/WQ5508.tsx
import React from "react";
import {Table, Card, Button, Select, Typography, DatePicker, Tag, Col, Space, notification, Input, Checkbox} from "antd";
import {visualize, update} from '../api/index'
import moment from "moment";
export interface WQ5508Props {
}

const dateFormat = 'YYYY/MM/DD';

interface WQ5508Row {
  'id': number,
  'Done': number,
  'Pending': number,
  'Notes': string,
  'Patient MRN': string,
  'Patient' : string,
  'Svc Date' : string,
  'Research IRB' : string,
  'Sess Amount' : number,
  'CPT Codes' : string,
  'Study Type': string,
  'Primary Coverage' : string,
  'Days Until Timely Filing' : number,
  'Aging Days' : number,
  'WQ File Date' : string,
  'Username' : string,
  'GovernmentFlag': number,
  'DataCollectionFlag' : number,
  'IRBFoundFlag' : number,
  'ManagerFlag' : number,
  'DateTimeStamp': string
}

const updateNotification = (field:string, status : number, rowsAffected : Array<number> = []) => {
  if(status===200 && rowsAffected.length === 1){
  return notification["success"]({
    message: "Successfully updated",
    description:
    `${field} field was successfully updated`
  })
  }
  else{
  return notification["error"]({
    message: "Unsuccessful",
    description:
    `${field} field update was unsuccessful`
  })
  }
}

export const WQ5508 : React.FunctionComponent<WQ5508Props> = (props) => {
  const [source, setSource] = React.useState([]);

  const updateEntry = async (id:number, key: string, val:any) => {
  const data = {
    id : id, 
    tableName : 'WQ5508_CONSOLIDATED',
    key : key,
    val : val
  }
  return await update(data)
  }

  const load = async ()=>{
    const {data:{rows=[]}} = await visualize('WQ5508_CONSOLIDATED')
    setSource(rows)
  }

  React.useEffect(()=>{
  load();
  },[])

  return <React.Fragment>
    <Card style={{ width: "90vw" }}>
    <Table dataSource={source} pagination={{ position: ['bottomCenter'] }} size={`small`} scroll={{y: 'calc(85vh - 90px)', x: 'calc(85vw - 90px)' }}>
    <Table.Column dataIndex={'Done'} title={'Done'} render={(value, row : WQ5508Row, index) => {
      return <Checkbox checked={row['Done'] ? true : false} onChange={async (e)=>{
      const {status, data : {rowsAffected}} = await updateEntry(row.id, 'Done', e.target.checked? 1 : null)
      await updateEntry(row.id, 'DateTimeStamp', new Date())
      updateNotification('Done', status, rowsAffected)
      load()
      }}/>
    }} />
    <Table.Column dataIndex={'Pending'} title={'Pending'} render={(value, row : WQ5508Row, index) => {
      return <Checkbox checked={row['Pending'] ? true : false} onChange={async (e)=>{
      const {status, data : {rowsAffected}} = await updateEntry(row.id, 'Pending', e.target.checked? 1 : null)
      updateNotification('Pending', status, rowsAffected)
      load()
      }}/>
    }} />
    <Table.Column dataIndex={'Notes'}  title={'Notes'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{value}</Typography.Text>
    }} />
    <Table.Column dataIndex={'Patient MRN'}  title={'Patient MRN'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{value}</Typography.Text>
    }} />
    <Table.Column dataIndex={'Patient'}  title={'Patient'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{value}</Typography.Text>
    }} />
    <Table.Column dataIndex={'Svc Date'}  title={'Svc Date'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{new Date(value).toString()}</Typography.Text>

      return <DatePicker defaultValue={moment(value, dateFormat)} format={dateFormat} disabled={false} onChange={async (date, dateString)=>{
      const {status, data : {rowsAffected}} = await updateEntry(row.id, 'Svc Date', dateString)
      updateNotification('Svc Date', status, rowsAffected)
      load()
      }}/>
    }} />
    <Table.Column dataIndex={'Research IRB'}  title={'Research IRB'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{value}</Typography.Text>
    }} />
    <Table.Column dataIndex={'Sess Amount'}  title={'Sess Amount'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{value}</Typography.Text>
    }} />
    <Table.Column dataIndex={'CPT Codes'}  title={'CPT Codes'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{value}</Typography.Text>
    }} />
    <Table.Column dataIndex={'Study Type'}  title={'Study Type'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{value}</Typography.Text>
       return <Select defaultValue={value} style={{ width: 120 }} onChange={async (e)=>{
      const {status, data : {rowsAffected}} = await updateEntry(row.id, 'Study Type', e)
      updateNotification('Study Type', status, rowsAffected)
      load()
       }}>
      <Select.Option value="Diagnostic">Diagnostic</Select.Option>
      <Select.Option value="Prophylactic">Prophylactic</Select.Option>
      <Select.Option value="Therapeutic">Therapeutic</Select.Option>
       </Select>
    }} />
    <Table.Column dataIndex={'Primary Coverage'}  title={'Primary Coverage'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{value}</Typography.Text>
    }} />
    <Table.Column dataIndex={'Days Until Timely Filing'}  title={'Days - Timely Filing'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{value}</Typography.Text>
    }} />
    <Table.Column dataIndex={'Aging Days'}  title={'Aging Days'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{value}</Typography.Text>
    }} />
    <Table.Column dataIndex={'WQ File Date'}  title={'WQ File Date'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{new Date(value).toString()}</Typography.Text>
      return <DatePicker defaultValue={moment(value, dateFormat)} format={dateFormat}  disabled={false} onChange={async (date, dateString)=>{
      const {status, data : {rowsAffected}} = await updateEntry(row.id, 'WQ File Date', dateString)
      updateNotification('WQ File Date', status, rowsAffected)
      load()
      }}/>
    }} />
    <Table.Column dataIndex={'Username'}  title={'Username'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{value}</Typography.Text>
    }} />
    <Table.Column dataIndex={'GovernmentFlag'} title={'GovernmentFlag'}  render={(value, row : WQ5508Row, index) => {
      return <Checkbox checked={value ? true : false} onChange={async (e)=>{
      const {status, data : {rowsAffected}} = await updateEntry(row.id, 'GovernmentFlag', e.target.checked? 1 : null)
      updateNotification('GovernmentFlag', status, rowsAffected)
      load()
      }}/>
    }} />
    <Table.Column dataIndex={'DataCollectionFlag'} title={'DataCollectionFlag'}  render={(value, row : WQ5508Row, index) => {
      return <Checkbox checked={value ? true : false} onChange={async (e)=>{
      const {status, data : {rowsAffected}} = await updateEntry(row.id, 'DataCollectionFlag', e.target.checked? 1 : null)
      updateNotification('DataCollectionFlag', status, rowsAffected)
      load()
      }}/>
    }} />
    <Table.Column dataIndex={'IRBFoundFlag'} title={'IRBFoundFlag'}  render={(value, row : WQ5508Row, index) => {
      return <Checkbox checked={value ? true : false} onChange={async (e)=>{
      const {status, data : {rowsAffected}} = await updateEntry(row.id, 'IRBFoundFlag', e.target.checked? 1 : null)
      updateNotification('IRBFoundFlag', status, rowsAffected)
      load()
      }}/>
    }} />
    <Table.Column dataIndex={'ManagerFlag'} title={'ManagerFlag'}  render={(value, row : WQ5508Row, index) => {
      return <Checkbox checked={value ? true : false} onChange={async (e)=>{
      const {status, data : {rowsAffected}} = await updateEntry(row.id, 'ManagerFlag', e.target.checked? 1 : null)
      updateNotification('ManagerFlag', status, rowsAffected)
      load()
      }}/>
    }} />
    <Table.Column dataIndex={'DateTimeStamp'}  title={'DateTimeStamp'}  render={(value, row: WQ5508Row, index) => {
      return <Typography.Text>{new Date(value).toString()}</Typography.Text>
      return <DatePicker defaultValue={moment(value, dateFormat)} format={dateFormat} disabled={false} onChange={async (date, dateString)=>{
      const {status, data : {rowsAffected}} = await updateEntry(row.id, 'DateTimeStamp', dateString)
      updateNotification('DateTimeStamp', status, rowsAffected)
      load()
      }}/>
    }} />

    </Table>
    </Card>
  </React.Fragment>
}

--#

--% /smartapp01/api/web/src/api/index.ts
import axios from "axios"
import moment from "moment";

if(process.env.REACT_APP_SERVER_URL){
  axios.defaults.baseURL = process.env.REACT_APP_SERVER_URL;
}

axios.interceptors.request.use((cfg)=>{
  return cfg;
})

axios.interceptors.response.use((cfg)=>{
  return cfg;
})

export const visualize = async (tableName:string)=>{
  return await axios.get(`/api/visualize/${tableName}`)
}

interface Data2Params {
  id: number
  tableName: string
  key: string
  val: any
}

export const update = async (data2: Data2Params)=>{
  return await axios({
  url: `/api/update`,
  method: 'POST',
  responseType: 'json',
  data: data2
  });
}


--#

--% /smartapp01/auth/package.json
{
  "name": "auth",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
  "test": "mocha",
  "coverage": "nyc mocha",
  "start": "moleculer-runner ./src"
  },
  "keywords": [],
  "author": "sptr",
  "license": "ISC",
  "dependencies": {
  "moleculer": "^0.14.13",
  "nats": "^1.4.9"
  },
  "devDependencies": {
  "chai": "^4.2.0",
  "chai-as-promised": "^7.1.1",
  "mocha": "^8.0.1",
  "nock": "^13.0.4",
  "nyc": "^15.1.0",
  "sinon": "^9.0.3"
  }
}

--#

--% /smartapp01/auth/.env

--#

--% /smartapp01/auth/.dockerignore
node_modules
--#

--% /smartapp01/auth/Dockerfile
FROM node:12-alpine

ENV NODE_ENV=production

RUN mkdir /app
WORKDIR /app

COPY package.json .

RUN npm install --production

COPY . .

CMD ["npm", "start"]
--#

--% /smartapp01/auth/src/auth.service.js

module.exports = {
  name: "auth",
  actions:{
  token:{
    async handler(ctx){
    return 401;
    }
  }
  }
}

--#

--% /smartapp01/auth/test/auth.service.test.js
const { ServiceBroker, Context } = require("moleculer");
const assert = require('assert');
const schema = require('../src/auth.service')
const sinon = require('sinon')
const chai = require('chai')
const expect = chai.expect
chai.use(require('chai-as-promised'))

describe("Authentication Actions",()=> {
  let broker = new ServiceBroker({logger: false});
  let service = broker.createService(schema);

  before(() => broker.start());
  after(() => broker.stop());

  it('should fetch token', async function () {

  const res = await broker.call('auth.token') || {};
  expect(res).eq(401)

  });
});

--#

--% /smartapp01/visualize/package.json
{
  "name": "visualize",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
  "test": "mocha",
  "coverage": "nyc mocha",
  "start": "moleculer-runner ./src"
  },
  "keywords": [],
  "author": "sptr",
  "license": "ISC",
  "dependencies": {
  "moleculer": "^0.14.13",
  "nats": "^1.4.9",
  "sequelize": "^6.6.5",
  "tedious": "^11.0.9",
  "mssql" : "^7.1.3"
  },
  "devDependencies": {
  "chai": "^4.2.0",
  "chai-as-promised": "^7.1.1",
  "mocha": "^8.0.1",
  "nock": "^13.0.4",
  "nyc": "^15.1.0",
  "sinon": "^9.0.3"
  }
}

--#

--% /smartapp01/visualize/.env

--#

--% /smartapp01/visualize/.dockerignore
node_modules
--#

--% /smartapp01/visualize/Dockerfile
FROM node:12-alpine

ENV NODE_ENV=production

RUN mkdir /app
WORKDIR /app

COPY package.json .

RUN npm install --production

COPY . .

CMD ["npm", "start"]
--#

--% /smartapp01/visualize/src/load.js
const { Sequelize } = require('sequelize');
var sql = require("mssql");

let dbConfig = {
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  server: process.env.DB_HOST,
  database: process.env.DB_DATABASE,
  port: parseInt(process.env.DB_PORT),
  options: { encrypt: false }
};


const sequelize = new Sequelize('TestDB', 'SA', 'MoonPie1', {
  host: 'localhost',
  dialect:'mssql'
  });

async function loadJSON({tableName, page:{from, size = 100} = {},orderBy,filter = []}){
  const {data : rows} = require('./data/data')
  const outgoingData = {
  rows 
  }

  return outgoingData
}

async function load_data(tableName){
  try{
  const res = await sql.connect(dbConfig)        
  const {recordset} = await sql.query(`select * from ${tableName}`)
  return {rows:recordset}
  }
  catch(err){
  return err
  }
}

module.exports = {
  load_data
}

--#

--% /smartapp01/visualize/src/visualize.service.js

module.exports = {
  name: "visualize",
  actions:{
  load:{
    params:{
    tableName: "string"
    },
    async handler(ctx){
    return this.load_data(ctx.params.tableName)
    }
  }
  },
  created(){
  const {load_data} = require('./load')
  this.load_data = load_data.bind(this)
  }
}

--#

--% /smartapp01/visualize/src/data/data.js
const data = [
  {
  "UID": 1537504855,
  "primary_coverage": "*LA CARE MCL CMMNTY FAM CARE",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 2138663502,
  "primary_coverage": "*CIGNA POS GRTR NEWPORT PHYS",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 434201408,
  "primary_coverage": "*BLUE SHIELD MCR GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1171126358,
  "primary_coverage": "*BLUE SHIELD HMO REGAL MG CAP",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1560360744,
  "primary_coverage": "BLUE CROSS OF CALIFORNIA EPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 771244835,
  "primary_coverage": "OUT OF STATE BS PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1181510274,
  "primary_coverage": "*SCAN MCR EMPIRE PHYS MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1824027568,
  "primary_coverage": "WRITERS GUILD OF AMERICA",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1388533909,
  "primary_coverage": "*BC OF CA PRIMECARE/NAMM",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1372265719,
  "primary_coverage": "*BS COVCA SILV GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 183643417,
  "primary_coverage": "GENERIC COMMERCIAL PLAN",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 218175239,
  "primary_coverage": "BLUE CROSS OF CALIFORNIA POS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1127224574,
  "primary_coverage": "*HLTH NET ELECT REGAL MG CAP",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 717060577,
  "primary_coverage": "*IEHP MCL PHYS HEALTHWAYS",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1400148003,
  "primary_coverage": "TRICARE WEST REGION",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 730213833,
  "primary_coverage": "BC COVCA PPO SILVER",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1227586970,
  "primary_coverage": "URN BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1147323347,
  "primary_coverage": "CCS RIVERSIDE",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1442148398,
  "primary_coverage": "*IEHP MCL HORIZON VALLEY",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1538100975,
  "primary_coverage": "BCBS FEDERAL EMPLOYEE PROGRAM",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 444943960,
  "primary_coverage": "KAISER SOUTHERN MEDICARE HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 2104544917,
  "primary_coverage": "*SECURE HORIZONS MCR CEDARS HLTH ASSOC",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1916401506,
  "primary_coverage": "*LA CARE MCL GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1491411420,
  "primary_coverage": "TRICARE PRIME",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 600320165,
  "primary_coverage": "GEHA - ASA",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1728425355,
  "primary_coverage": "CIGNA OPEN ACCESS PLUS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 2095459458,
  "primary_coverage": "BC COVCA PPO GOLD",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 871264926,
  "primary_coverage": "GOLD COAST MCL HEALTH PLAN DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 275562133,
  "primary_coverage": "*SECURE HORIZONS MCR AXMINSTER MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 816072237,
  "primary_coverage": "CAREMORE MCR HEALTH PLAN DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 488595671,
  "primary_coverage": "BLUE SHIELD PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1396303610,
  "primary_coverage": "CIGNA PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 476274903,
  "primary_coverage": "BLUE SHIELD EPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 156147313,
  "primary_coverage": "*LA CARE MCL HEALTHCARE LA IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 2142270678,
  "primary_coverage": "*HLTH NET MCR ST JUDE HERITAGE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 116786235,
  "primary_coverage": "BCCTP",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1555519842,
  "primary_coverage": "LA COUNTY FIREFIGHTERS LOCAL 1014",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1217023299,
  "primary_coverage": "LA CARE MEDI-CAL HMO DIRECT",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 580522855,
  "primary_coverage": "*CIGNA HMO BEAVER MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 251614032,
  "primary_coverage": "*IEHP MCL ALPHA CARE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1684460796,
  "primary_coverage": "*BLUE SHIELD PROMISE MCL HEALTHCARE LA IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1788066700,
  "primary_coverage": "*IEHP MCL INLAND FACULTY MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1360695274,
  "primary_coverage": "AETNA BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 765207896,
  "primary_coverage": "*SCAN MCR PRIMECARE/NAMM",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1537921777,
  "primary_coverage": "*BLUE SHIELD MCR ALAMITOS",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1095235732,
  "primary_coverage": "*BLUE SHIELD MCR PRIMECARE/NAMM",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1568758937,
  "primary_coverage": "CCS VENTURA",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 482569787,
  "primary_coverage": "BLUE SHIELD BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 2000388457,
  "primary_coverage": "CCS LOS ANGELES",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1243982196,
  "primary_coverage": "KAISER COVCA HMO GOLD DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1408917668,
  "primary_coverage": "KAISER SOUTHERN CALIFORNIA BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1542275121,
  "primary_coverage": "*BC OF CA POS HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 53795751,
  "primary_coverage": "*PAC HMO PRIMECARE INLAND VALLEY CAP",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 423949474,
  "primary_coverage": "NATIONAL MARROW DONOR PROGRAM BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 128402595,
  "primary_coverage": "*PAC HMO GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 651762858,
  "primary_coverage": "*BLUE SHIELD HMO GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1778275139,
  "primary_coverage": "*BLUE CROSS MCR GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 682720398,
  "primary_coverage": "*EASY CHOICE MCR REGAL MED GROUP FFS",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 106869151,
  "primary_coverage": "HEALTHCARE PARTNERS EMPLOYEES",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 2117314283,
  "primary_coverage": "KAISER MEDI-CAL HMO DIRECT",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1355190238,
  "primary_coverage": "AETNA POS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 592431495,
  "primary_coverage": "*SECURE HORIZONS MCR ST JOSEPH IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 763287496,
  "primary_coverage": "MERITAIN HEALTH",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 892919568,
  "primary_coverage": "*HLTH NET ALLIED PACIFIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1632643614,
  "primary_coverage": "CIGNA GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1584050311,
  "primary_coverage": "CCS MEDI-CAL",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 244675029,
  "primary_coverage": "*BLUE SHIELD PROMISE MCL CAL CARE IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1388899533,
  "primary_coverage": "MEDICARE PART A+B",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 39687950,
  "primary_coverage": "IEHP MEDICONNECT DUAL DIRECT",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 598302723,
  "primary_coverage": "*SCAN MCR HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1869443488,
  "primary_coverage": "GENERIC BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1635133987,
  "primary_coverage": "AETNA GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 2103445477,
  "primary_coverage": "*CIGNA HMO GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 87538195,
  "primary_coverage": "*BLUE SHIELD MCR PRIMECARE CAP IV",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1051190868,
  "primary_coverage": "KAISER COVCA HMO BRONZE DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1022821363,
  "primary_coverage": "*BS COVCA PLAT ALLIED PACIFIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 500728315,
  "primary_coverage": "UNITED HEALTHCARE OXFORD",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1879913767,
  "primary_coverage": "AETNA REPLACEMENT MCR PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1917878129,
  "primary_coverage": "CIGNA BMT - TN",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1897391354,
  "primary_coverage": "MEDICARE RAILROAD",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1071924003,
  "primary_coverage": "OUT OF STATE BC EPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1334293434,
  "primary_coverage": "BLUE CROSS MCR REPLACEMENT PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 218351422,
  "primary_coverage": "BLUE CROSS OF CALIFORNIA BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1533324086,
  "primary_coverage": "CAL OPTIMA MCL DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1617069156,
  "primary_coverage": "UNITED HEALTH CARE MCR REPLACEMENT PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1436033849,
  "primary_coverage": "MEDI-CAL",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1217871477,
  "primary_coverage": "*BLUE SHIELD HMO AXMINSTER MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 676379035,
  "primary_coverage": "*BLUE SHIELD HMO ST JOSEPH IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1513681355,
  "primary_coverage": "*BLUE SHIELD HMO RMG INTERCOMMUNITY",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1527862477,
  "primary_coverage": "HUMANA GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1501874099,
  "primary_coverage": "*AETNA HMO HCP CAP MTHDST",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1814933728,
  "primary_coverage": "*CAL OPTIMA MCL MONARCH FAMILY HEALTHCARE",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 862012406,
  "primary_coverage": "KAISER SOUTHERN CALIFORNIA HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 862943734,
  "primary_coverage": "KAISER NORTHERN CALIFORNIA HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 240655867,
  "primary_coverage": "MEDICARE PART B",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1042036906,
  "primary_coverage": "*BS COVCA SILV MEMORIALCARE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1396303906,
  "primary_coverage": "CIGNA POS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 712550447,
  "primary_coverage": "CCS TULARE",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1168702954,
  "primary_coverage": "BDCT GENERIC BMT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 997924970,
  "primary_coverage": "*BC OF CA GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 414550640,
  "primary_coverage": "BLUE CROSS GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 981219044,
  "primary_coverage": "UMR",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 56626789,
  "primary_coverage": "*AETNA HMO GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 2023103327,
  "primary_coverage": "BS COVCA PPO PLATINUM",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1597654292,
  "primary_coverage": "*BLUE SHIELD HMO GLOBAL CARE",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1147204803,
  "primary_coverage": "MOTION PICTURE SCREEN ACTORS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 306198724,
  "primary_coverage": "*BLUE SHIELD POS HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1917877197,
  "primary_coverage": "CIGNA BMT - PA",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 6362666,
  "primary_coverage": "*LA CARE MCL ALTAMED MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1493703328,
  "primary_coverage": "*BC OF CA SANSUM MC",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 43161578,
  "primary_coverage": "DELTA HEALTH SYSTEMS",
  "CurrentCoverage": "",
  "government": 0
  },
  {
  "UID": 711690761,
  "primary_coverage": "BLUE SHIELD HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 298989248,
  "primary_coverage": "OUT OF STATE MCR BS PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1682004932,
  "primary_coverage": "*BLUE SHIELD MCR HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 2046971352,
  "primary_coverage": "BLUE SHIELD MEDICARE HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1963951790,
  "primary_coverage": "CENCAL MEDI-CAL HMO",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 2024789996,
  "primary_coverage": "SIERRA HEALTH AND LIFE",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 471534270,
  "primary_coverage": "CIGNA SENIOR HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1050166051,
  "primary_coverage": "OUT OF STATE BC PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 527829327,
  "primary_coverage": "PINNACLE GROUP CLAIMS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 801710251,
  "primary_coverage": "OPERATING ENGINEERS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1887275435,
  "primary_coverage": "IEHP MEDI-CAL HMO DIRECT",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 523550920,
  "primary_coverage": "*LA CARE MEDI DUAL APPLECARE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 712052554,
  "primary_coverage": "CAL PERS PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 971034193,
  "primary_coverage": "KAISER COVCA HMO SILVER DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1138159113,
  "primary_coverage": "*SECURE HORIZONS MCR PRIMECARE CAP IV",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 607864312,
  "primary_coverage": "*MOLINA MCL INLAND FACULTY MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 587122935,
  "primary_coverage": "BLUE CROSS OF CALIFORNIA PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 289352998,
  "primary_coverage": "*MOLINA COVCA SILV VANTAGE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 625014119,
  "primary_coverage": "UNITED HEALTHCARE GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1734969266,
  "primary_coverage": "*BLUE SHIELD PROMISE MEDI DUAL HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 426872091,
  "primary_coverage": "BCBS NEVADA MEDICAID",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1355186438,
  "primary_coverage": "AETNA PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1199975883,
  "primary_coverage": "BS COVCA PPO SILVER",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 9,
  "primary_coverage": null,
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1192903551,
  "primary_coverage": "*LA CARE MCL DHS",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1419698406,
  "primary_coverage": "TRISTAR RISK MANAGEMENT POLICE",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1406057435,
  "primary_coverage": "BS COVCA PPO BRONZE",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 569317289,
  "primary_coverage": "SELF INSURED SCHOOLS CA PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1373142263,
  "primary_coverage": "*BC COVCA SILV GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 828779650,
  "primary_coverage": "BS COVCA PPO GOLD",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 307502581,
  "primary_coverage": "*BC OF CA HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 2100745759,
  "primary_coverage": "*BLUE SHIELD HMO PRIMECARE CAP IV",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1606417776,
  "primary_coverage": "WORKERS COMPENSATION GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1171675772,
  "primary_coverage": "UNITED HEALTHCARE PPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1521972295,
  "primary_coverage": "PHCS GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 552860996,
  "primary_coverage": "SCREEN ACTORS GUILD",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1113994192,
  "primary_coverage": "*BLUE CROSS MCL ACCOUNTABLE IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 791709537,
  "primary_coverage": "KAISER HAWAII HMO DIRECT",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1227325046,
  "primary_coverage": "URN CRS",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 653876433,
  "primary_coverage": "*HLTH NET MCL OMNICARE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 826788476,
  "primary_coverage": "*SECURE HORIZONS MCR HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 398681715,
  "primary_coverage": "MULTIPLAN GENERIC",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 1950441493,
  "primary_coverage": "*BC OF CA APPLECARE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1797743489,
  "primary_coverage": "*AETNA HMO MEMORIALCARE MG",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 1480920405,
  "primary_coverage": "*SECURE HORIZONS MCR GENERIC IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 66621630,
  "primary_coverage": "KAISER SOUTHERN CALIFORNIA EPO",
  "CurrentCoverage": "",
  "government": null
  },
  {
  "UID": 914518814,
  "primary_coverage": "*SCAN MCR PRIMECARE CAP IV",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 331857060,
  "primary_coverage": "*PAC HMO HCP IPA",
  "CurrentCoverage": "",
  "government": 1
  },
  {
  "UID": 834153197,
  "primary_coverage": "*BLUE SHIELD HMO PRIMECARE/NAMM",
  "CurrentCoverage": "",
  "government": 1
  }
]

module.exports = {
  data
}
--#

--% /smartapp01/visualize/test/visualize.service.test.js
const { ServiceBroker, Context } = require("moleculer");
const assert = require('assert');
const schema = require('../src/visualize.service')
const sinon = require('sinon')
const chai = require('chai')
const expect = chai.expect
chai.use(require('chai-as-promised'))

describe("Visualization Actions",()=> {
  let broker = new ServiceBroker({logger: false});
  let service = broker.createService(schema);

  before(() => broker.start());
  after(() => broker.stop());

  afterEach(()=>{

  })

  describe("Load Page data", ()=>{
  before(()=>{

  })
  it('should load data for the table', async function () {
    const res = await broker.call('visualize.load', {tableName: 'hello'});
    console.log(res)
  });
  })

});

--#

--% /smartapp01/migrations/V2__create_table.sql
CREATE TABLE [dbo].[WQ5508_CONSOLIDATED](
  [id] [int] IDENTITY(1,1) NOT NULL,
  [Done] [bit] NULL,
  [Pending] [bit] NULL,
  [Notes] [nvarchar](max) NULL,
  [Patient MRN] [nvarchar](255) NULL,
  [Patient] [nvarchar](255) NULL,
  [Svc Date] [datetime] NULL,
  [Research IRB] [nvarchar](255) NULL,
  [Sess Amount] [float] NULL,
  [CPT Codes] [nvarchar](255) NULL,
  [Study Type] [nvarchar](255) NULL,
  [Primary Coverage] [nvarchar](255) NULL,
  [Days Until Timely Filing] [float] NULL,
  [Aging Days] [float] NULL,
  [WQ File Date] [datetime2](7) NULL,
  [Username] [nvarchar](255) NULL,
  [GovernmentFlag] [bit] NULL,
  [DataCollectionFlag] [bit] NULL,
  [IRBFoundFlag] [bit] NULL,
  [ManagerFlag] [bit] NULL,
  [DateTimeStamp] [datetime2](7) NULL,
  CONSTRAINT PK__WQ5508 PRIMARY KEY (id)
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]

INSERT INTO WQ5508_CONSOLIDATED ([Done], [Pending], [Notes], [Patient MRN], [Patient], [Svc Date], [Research IRB], [Sess Amount], [CPT Codes], [Study Type], [Primary Coverage], [Days Until Timely Filing], [Aging Days], [WQ File Date], [Username], [GovernmentFlag], [DataCollectionFlag], [IRBFoundFlag], [ManagerFlag], [DateTimeStamp] ) VALUES
  (1, 1, 'Sample Note', '2398792', 'John Smith', '2020-02-02', '234235', 122.4, '443223', 'Therapeutic', 'TRICARE PRIME', 23, 5, '2020-02-05', 'johnsmith', 1, 1, 1, 1,'2020-05-08');
--#

--% /smartapp01/migrations/V3__create_irbdatacollection.sql
CREATE TABLE [IRB_Data_Collection](
  [id] [int] IDENTITY(1,1) NOT NULL,
  UID varchar(255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  [IRBCode] [nvarchar](5) NULL,
  [Government] [bit] NULL,
  -- [New] [bit] NOT NULL,
  [LastUpdated] [datetime] DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT PK__billing_irb_data_collection PRIMARY KEY (id)
) ON [PRIMARY]

INSERT INTO IRB_Data_Collection 
(UID, IRBCode, Government) 
VALUES
  (N'1', N'123', 0),
  (N'2', N'1141', 0),
  (N'3', N'5024', 0),
  (N'4', N'6129', 0),
  (N'5', N'6229', 0),
  (N'6', N'8242', 0),
  (N'7', N'10232', 0),
  (N'8', N'11005', 0),
  (N'9', N'11103', 0),
  (N'10', N'11122', 0),

  (N'11', N'11255', 0),
  (N'12', N'12358', 0),
  (N'13', N'13188', 0),
  (N'14', N'13278', 0),
  (N'15', N'13318', 0),
  (N'16', N'13477', 0),
  (N'17', N'14063', 0),
  (N'18', N'14098', 0),
  (N'19', N'14227', 0),
  (N'20', N'14259', 0),

  (N'21', N'14266', 0),
  (N'22', N'14274', 0),
  (N'23', N'14337', 0),
  (N'24', N'14344', 0),
  (N'25', N'15089', 0),
  (N'26', N'15130', 0),
  (N'27', N'15147', 0),
  (N'28', N'15158', 0),
  (N'29', N'15161', 0),
  (N'30', N'15185', 0),

  (N'31', N'15317', 0),
  (N'32', N'15341', 0),
  (N'33', N'15417', 0),
  (N'34', N'15447', 0),
  (N'35', N'16008', 0),
  (N'36', N'16072', 0),
  (N'37', N'16088', 0),
  (N'38', N'16117', 0),
  (N'39', N'16190', 0),
  (N'40', N'16298', 0),

  (N'41', N'16309', 0),
  (N'42', N'16323', 0),
  (N'43', N'16334', 0),
  (N'44', N'16441', 0),
  (N'45', N'17024', 0),
  (N'46', N'17072', 0),
  (N'47', N'17089', 0),
  (N'48', N'17154', 0),
  (N'49', N'17162', 0),
  (N'50', N'17185', 0),

  (N'51', N'17200', 0),
  (N'52', N'17211', 0),
  (N'53', N'17305', 0),
  (N'54', N'17343', 0),
  (N'55', N'17346', 0),
  (N'56', N'17361', 0),
  (N'57', N'17370', 0),
  (N'58', N'17375', 0),
  (N'59', N'17482', 0),
  (N'60', N'17503', 0),

  (N'61', N'17507', 0),
  (N'62', N'18082', 0),
  (N'63', N'18201', 0),
  (N'64', N'18209', 0),
  (N'65', N'18267', 0),
  (N'66', N'18295', 0),
  (N'67', N'18306', 0),
  (N'68', N'18387', 0),
  (N'69', N'18520', 0),
  (N'70', N'19127', 0),

  (N'71', N'19222', 0),
  (N'72', N'19249', 0),
  (N'73', N'19264', 0),
  (N'74', N'19477', 0),
  (N'75', N'19503', 0),
  (N'76', N'19543', 0),
  (N'77', N'20126', 0);

--#

--% /smartapp01/migrations/V1__create_initial_tables.sql
CREATE TABLE [Billing_Coverage_Government_New](
  [id] 							[int] IDENTITY(1,1) NOT NULL,
  UID 							varchar(255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
  [PrimaryCoverage] [nvarchar](500) NULL,
  [Government] 			[bit] NULL,
  [New] 						[bit] NOT NULL,
  [LastUpdated] 		[datetime] NOT NULL,
  CONSTRAINT 				PK__billing_cov_gov PRIMARY KEY (id)
) ON [PRIMARY]

INSERT INTO Billing_Coverage_Government_New (UID,PrimaryCoverage,Government, New, LastUpdated) VALUES
  (N'1537504855',N'LA CARE MCL CMMNTY FAM CARE', 1 ,1, '2020-04-02'),
  (N'1537504855',N'DSOIJUSA SAJSDJ', 0 ,0, '2020-05-02');

--#

--% /smartapp01/migrations/Dockerfile
FROM flyway/flyway:latest

COPY ./*.sql /flyway/sql/


--#

