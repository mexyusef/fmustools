--% /np/docker-compose.yml
version: '3'
services:
  database:
    image: 'mongo'
    # container_name: 'mymongocontainer'
    environment:
      - MONGO_INITDB_DATABASE=tempdb
      - MONGO_INITDB_ROOT_USERNAME=usef
      - MONGO_INITDB_ROOT_PASSWORD=rahasia
    ports:
      - '27017-27019:27017-27019'
  client:
    image: 'mongoclient/mongoclient'
    environment:
      - MONGO_URL=mongodb://usef:rahasia@database:27017/
    ports:
      - '7001:3000'
    depends_on:
      - database
  mongo-express:
    image: mongo-express
    restart: always
    ports:
      - 7002:8081
    depends_on:
      - database
    environment:
      ME_CONFIG_MONGODB_ADMINUSERNAME: usef
      ME_CONFIG_MONGODB_ADMINPASSWORD: rahasia
      ME_CONFIG_MONGODB_URL: mongodb://usef:rahasia@database:27017/
--#
