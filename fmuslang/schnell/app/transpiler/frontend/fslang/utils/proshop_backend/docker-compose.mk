
--% docker-compose.yml
version: '3'
services:
  db:
    image: postgres
    environment:
      - POSTGRES_DB=tempdb
      - POSTGRES_USER=usef
      - POSTGRES_PASSWORD=rahasia
    ports:
      - "5432:5432"
  phppgadmin:
    image: docker.io/bitnami/phppgadmin:7
    ports:
      - '7001:8080'
      - '7002:8443'
    depends_on:
      - db
--#
