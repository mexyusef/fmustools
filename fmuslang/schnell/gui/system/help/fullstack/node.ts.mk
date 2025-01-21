--% appseed, api-server-nodejs
├── media
    - api.postman_collection.json
├── node_modules
├── src
└── tests
src
- index.ts
├── config
    - config.ts
    - passport.ts
    - safeRoutes.ts
├── migrations
├── models
    - users.ts
    activeSession.ts
├── routes
    - users.ts
└── server
    - index.ts
    - server.ts

>> pnpm gagal, yarn sukses

- Stack: Node JS/ Express / TypeORM / SQLite3
- API:
   - Sign UP: `/api/users/register`
   POST api/users/register
   Content-Type: application/json   
   {
       "username":"test",
       "password":"pass", 
       "email":"test@appseed.us"
   }
   - Sign IN: `/api/users/login`
   POST /api/users/login
   Content-Type: application/json   
   {
       "password":"pass", 
       "email":"test@appseed.us"
   }
   - Logout: `/api/users/logout`
   POST api/users/logout
   Content-Type: application/json
   authorization: JWT_TOKEN (returned by Login request)   
   {
       "token":"JWT_TOKEN"
   }
   - Check Session: `/api/users/checkSession`
   - Edit User: `/api/users/edit`
- Data persistence
  - TypeORM / SQLite3
  - Db migrations are in `src/migrations` folder
  - Added new config `ormconfig.json`
sumber:
https://github.com/app-generator/api-server-nodej
https://github.com/app-generator/api-server-nodejs-pro
https://docs.appseed.us/boilerplate-code/api-server/node-js

$ yarn typeorm migration:generate -n your_migration_name
$ yarn typeorm migration:run
$ yarn test
--#
