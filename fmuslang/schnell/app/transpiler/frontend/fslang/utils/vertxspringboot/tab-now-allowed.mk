--% C:/work/sample/vertx-springboot-realworld-example-app/src/main/resources/application.yml
spring:
  datasource:
    url: jdbc:h2:mem:testdb;DB_CLOSE_ON_EXIT=FALSE;DB_CLOSE_DELAY=-1
    username: sa
    password:
  autoconfigure:
    exclude:
      - org.springframework.boot.autoconfigure.http.HttpMessageConvertersAutoConfiguration
vertx:
  server:
    port: 8080
    context_path: "/api"
  jwt:
    algorithm: "HS256"
    secret: "secret"
  database:
    url: ${spring.datasource.url}
    driver_class: "org.h2.Driver"
    max_pool_size: 30
    user: ${spring.datasource.username}
    password: ${spring.datasource.password}
--#

--% C:/work/sample/vertx-springboot-realworld-example-app/src/test/resources/application.yml
spring:
  datasource:
    url: jdbc:h2:mem:testdb;DB_CLOSE_ON_EXIT=FALSE;DB_CLOSE_DELAY=-1
    username: sa
    password:
  autoconfigure:
    exclude:
      - org.springframework.boot.autoconfigure.http.HttpMessageConvertersAutoConfiguration
vertx:
  server:
    port: 8081
    context_path: "/api"
  jwt:
    algorithm: "HS256"
    secret: "secret"
  database:
    url: ${spring.datasource.url}
    driver_class: "org.h2.Driver"
    max_pool_size: 30
    user: ${spring.datasource.username}
    password: ${spring.datasource.password}
--#
