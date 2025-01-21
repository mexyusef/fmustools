--% index/fmus
fs-micronaut-mg,d(/mk)
	%utama=__FILE__
	.gitignore,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/.gitignore)
	build.gradle,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/build.gradle)
	docker-compose.yml,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/docker-compose.yml)
	gradle.properties,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/gradle.properties)
	gradlew.bat,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/gradlew.bat)
	micronaut-cli.yml,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/micronaut-cli.yml)
	README.md,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/README.md)
	run.sh,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/run.sh)
	settings.gradle,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/settings.gradle)
	.gradle,d(/mk)
		7.2,d(/mk)
			gc.properties,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/7.2/gc.properties)
			dependencies-accessors,d(/mk)
				dependencies-accessors.lock,f(b64=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/7.2/dependencies-accessors/dependencies-accessors.lock)
				gc.properties,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/7.2/dependencies-accessors/gc.properties)
			executionHistory,d(/mk)
				executionHistory.lock,f(b64=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/7.2/executionHistory/executionHistory.lock)
			fileChanges,d(/mk)
			fileHashes,d(/mk)
				fileHashes.lock,f(b64=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/7.2/fileHashes/fileHashes.lock)
			vcsMetadata-1,d(/mk)
		buildOutputCleanup,d(/mk)
			buildOutputCleanup.lock,f(b64=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/buildOutputCleanup/buildOutputCleanup.lock)
			cache.properties,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/buildOutputCleanup/cache.properties)
		checksums,d(/mk)
			checksums.lock,f(b64=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/checksums/checksums.lock)
		vcs-1,d(/mk)
			gc.properties,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/vcs-1/gc.properties)
	src,d(/mk)
		main,d(/mk)
			java,d(/mk)
				example,d(/mk)
					micronaut,d(/mk)
						Application.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/java/example/micronaut/Application.java)
						Fruit.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/java/example/micronaut/Fruit.java)
						FruitController.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/java/example/micronaut/FruitController.java)
						FruitRepository.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/java/example/micronaut/FruitRepository.java)
						MongoDbConfiguration.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/java/example/micronaut/MongoDbConfiguration.java)
						MongoDbFruitRepository.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/java/example/micronaut/MongoDbFruitRepository.java)
			resources,d(/mk)
				application.yml,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/resources/application.yml)
				logback.xml,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/resources/logback.xml)
		test,d(/mk)
			java,d(/mk)
				example,d(/mk)
					micronaut,d(/mk)
						FruitClient.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/test/java/example/micronaut/FruitClient.java)
						FruitControllerTest.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/test/java/example/micronaut/FruitControllerTest.java)
						FruitControllerValidationTest.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/test/java/example/micronaut/FruitControllerValidationTest.java)
						MicronautguideTest.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/test/java/example/micronaut/MicronautguideTest.java)
						MongoDbUtils.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-micronaut/src/test/java/example/micronaut/MongoDbUtils.java)
--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/.gitignore
Thumbs.db
.DS_Store
.gradle
build/
target/
out/
.idea
*.iml
*.ipr
*.iws
.project
.settings
.classpath
.factorypath

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/build.gradle
plugins {
    id("com.github.johnrengelman.shadow") version "7.1.0"
    id("io.micronaut.application") version "3.0.0"
}

version = "0.1"
group = "example.micronaut"

repositories {
    mavenCentral()
}

micronaut {
    runtime("netty")
    testRuntime("junit5")
    processing {
        incremental(true)
        annotations("example.micronaut.*")
    }
}

dependencies {
    annotationProcessor("io.micronaut:micronaut-http-validation")
    implementation("io.micronaut:micronaut-http-client")
    implementation("io.micronaut:micronaut-runtime")
    implementation("io.micronaut.mongodb:micronaut-mongo-reactive")
    implementation("io.micronaut.reactor:micronaut-reactor")
    implementation("io.micronaut.reactor:micronaut-reactor-http-client")
    implementation("javax.annotation:javax.annotation-api")
    runtimeOnly("ch.qos.logback:logback-classic")
    testImplementation("org.testcontainers:junit-jupiter")
    testImplementation("org.testcontainers:mongodb")
    testImplementation("org.testcontainers:testcontainers")
    implementation("io.micronaut:micronaut-validation")

}


application {
    mainClass.set("example.micronaut.Application")
}
java {
    sourceCompatibility = JavaVersion.toVersion("11")
    targetCompatibility = JavaVersion.toVersion("11")
}


--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/docker-compose.yml
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

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/gradle.properties
micronautVersion=3.2.0
org.gradle.java.installations.auto-download=false
org.gradle.java.installations.auto-detect=false
org.gradle.java.installations.fromEnv=JAVA_HOME

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/gradlew.bat
@rem
@rem Copyright 2015 the original author or authors.
@rem
@rem Licensed under the Apache License, Version 2.0 (the "License");
@rem you may not use this file except in compliance with the License.
@rem You may obtain a copy of the License at
@rem
@rem      https://www.apache.org/licenses/LICENSE-2.0
@rem
@rem Unless required by applicable law or agreed to in writing, software
@rem distributed under the License is distributed on an "AS IS" BASIS,
@rem WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
@rem See the License for the specific language governing permissions and
@rem limitations under the License.
@rem

@if "%DEBUG%" == "" @echo off
@rem ##########################################################################
@rem
@rem  Gradle startup script for Windows
@rem
@rem ##########################################################################

@rem Set local scope for the variables with windows NT shell
if "%OS%"=="Windows_NT" setlocal

set DIRNAME=%~dp0
if "%DIRNAME%" == "" set DIRNAME=.
set APP_BASE_NAME=%~n0
set APP_HOME=%DIRNAME%

@rem Resolve any "." and ".." in APP_HOME to make it shorter.
for %%i in ("%APP_HOME%") do set APP_HOME=%%~fi

@rem Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
set DEFAULT_JVM_OPTS="-Xmx64m" "-Xms64m"

@rem Find java.exe
if defined JAVA_HOME goto findJavaFromJavaHome

set JAVA_EXE=java.exe
%JAVA_EXE% -version >NUL 2>&1
if "%ERRORLEVEL%" == "0" goto execute

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto execute

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\gradle\wrapper\gradle-wrapper.jar


@rem Execute Gradle
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %GRADLE_OPTS% "-Dorg.gradle.appname=%APP_BASE_NAME%" -classpath "%CLASSPATH%" org.gradle.wrapper.GradleWrapperMain %*

:end
@rem End local scope for the variables with windows NT shell
if "%ERRORLEVEL%"=="0" goto mainEnd

:fail
rem Set variable GRADLE_EXIT_CONSOLE if you need the _script_ return code instead of
rem the _cmd.exe /c_ return code!
if  not "" == "%GRADLE_EXIT_CONSOLE%" exit 1
exit /b 1

:mainEnd
if "%OS%"=="Windows_NT" endlocal

:omega

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/micronaut-cli.yml
applicationType: default
defaultPackage: example.micronaut
testFramework: junit
sourceLanguage: java
buildTool: gradle
features: [annotation-api, app-name, gradle, http-client, java, java-application, junit, logback, mongo-reactive, netty-server, reactor, reactor-http-client, readme, shade, testcontainers, yaml]

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/README.md
## Micronaut 3.2.0 Documentation

- [User Guide](https://docs.micronaut.io/3.2.0/guide/index.html)
- [API Reference](https://docs.micronaut.io/3.2.0/api/index.html)
- [Configuration Reference](https://docs.micronaut.io/3.2.0/guide/configurationreference.html)
- [Micronaut Guides](https://guides.micronaut.io/index.html)
---

## Feature reactor documentation

- [Micronaut Reactor documentation](https://micronaut-projects.github.io/micronaut-reactor/snapshot/guide/index.html)

## Feature http-client documentation

- [Micronaut HTTP Client documentation](https://docs.micronaut.io/latest/guide/index.html#httpClient)

## Feature mongo-reactive documentation

- [Micronaut MongoDB Reactive Driver documentation](https://micronaut-projects.github.io/micronaut-mongodb/latest/guide/index.html)

- [https://docs.mongodb.com](https://docs.mongodb.com)

## Feature testcontainers documentation

- [https://www.testcontainers.org/](https://www.testcontainers.org/)

http://localhost:9300/fruits

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/run.sh
./gradlew run
--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/settings.gradle

rootProject.name="micronautguide"

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/7.2/gc.properties

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/7.2/dependencies-accessors/dependencies-accessors.lock
A8XDQiNAtjxwAAAAAAAAAAADAADdA0aE1BZeb4MAAAQ0MTcxAAA=
--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/7.2/dependencies-accessors/gc.properties

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/7.2/executionHistory/executionHistory.lock
AyMnOte6CtBuAAAAAAAAAA4DAADdAytJ74D1IsW+AAQ0MTcxAAA=
--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/7.2/fileHashes/fileHashes.lock
A91PAsEIrF6eAAAAAAAAAGIDAADdA9jaHxiyPP/qAAQ0MTcxAAA=
--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/buildOutputCleanup/buildOutputCleanup.lock
Aw0HAMYgTGKCAAAAAAAAADsDAADdA8JkKi8KvqAjAAQ0MTcxAAA=
--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/buildOutputCleanup/cache.properties
#Sun Nov 28 21:59:04 ICT 2021
gradle.version=7.2

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/checksums/checksums.lock
A9UQN7gj0e/vAAAAAAAAAvYDAADdA5mwKZv7xUnwAAQ0MTcxAAA=
--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/.gradle/vcs-1/gc.properties

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/java/example/micronaut/Application.java
package example.micronaut;

import io.micronaut.runtime.Micronaut;

public class Application {

    public static void main(String[] args) {
        Micronaut.run(Application.class, args);
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/java/example/micronaut/Fruit.java
package example.micronaut;

import io.micronaut.core.annotation.Creator;
import io.micronaut.core.annotation.Introspected;
import io.micronaut.core.annotation.NonNull;
import io.micronaut.core.annotation.Nullable;
import org.bson.codecs.pojo.annotations.BsonCreator;
import org.bson.codecs.pojo.annotations.BsonProperty;

import javax.validation.constraints.NotBlank;

@Introspected // <1>
public class Fruit {

    @NonNull
    @NotBlank // <2>
    @BsonProperty("name") // <3>
    private final String name;

    @Nullable
    @BsonProperty("description") // <3>
    private String description;

    public Fruit(@NonNull String name) {
        this(name, null);
    }

    @Creator // <4>
    @BsonCreator// <3>
    public Fruit(@NonNull @BsonProperty("name") String name,  // <3>
                 @Nullable @BsonProperty("description") String description) {  // <3>
        this.name = name;
        this.description = description;
    }

    @NonNull
    public String getName() {
        return name;
    }

    @Nullable
    public String getDescription() {
        return description;
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/java/example/micronaut/FruitController.java
package example.micronaut;

import io.micronaut.core.annotation.NonNull;
import io.micronaut.http.HttpStatus;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Post;
import io.micronaut.http.annotation.Status;
import io.micronaut.http.client.HttpClient;
import io.micronaut.scheduling.TaskExecutors;
import io.micronaut.scheduling.annotation.ExecuteOn;
import org.reactivestreams.Publisher;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import javax.validation.Valid;
import javax.validation.constraints.NotNull;
import java.util.List;

@Controller("/fruits") // <1>
public class FruitController {

    private final FruitRepository fruitService;

    public FruitController(FruitRepository fruitService) {  // <2>
        this.fruitService = fruitService;
    }

    @Get  // <3>
    public Publisher<Fruit> list() {
        return fruitService.list();
    }

    @Post // <4>
    public Mono<HttpStatus> save(@NonNull @NotNull @Valid Fruit fruit) { // <5>
        return fruitService.save(fruit) // <6>
                .map(added -> (added) ? HttpStatus.CREATED : HttpStatus.CONFLICT);
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/java/example/micronaut/FruitRepository.java
package example.micronaut;

import io.micronaut.core.annotation.NonNull;
import org.reactivestreams.Publisher;
import reactor.core.publisher.Mono;

import javax.validation.Valid;
import javax.validation.constraints.NotNull;

public interface FruitRepository {
    @NonNull
    Publisher<Fruit> list();

    Mono<Boolean> save(@NonNull @NotNull @Valid Fruit fruit); // <1>
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/java/example/micronaut/MongoDbConfiguration.java
package example.micronaut;

import io.micronaut.context.annotation.ConfigurationProperties;
import io.micronaut.core.annotation.NonNull;
import io.micronaut.core.naming.Named;

@ConfigurationProperties("db") // <1>
public interface MongoDbConfiguration extends Named {
    @NonNull
    String getCollection();
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/java/example/micronaut/MongoDbFruitRepository.java
package example.micronaut;

import com.mongodb.client.result.InsertOneResult;
import com.mongodb.reactivestreams.client.MongoClient;
import com.mongodb.reactivestreams.client.MongoCollection;
import io.micronaut.core.annotation.NonNull;
import jakarta.inject.Singleton;
import org.reactivestreams.Publisher;
import reactor.core.publisher.Mono;

import javax.validation.Valid;
import javax.validation.constraints.NotNull;

@Singleton // <1>
public class MongoDbFruitRepository implements FruitRepository {

    private final MongoDbConfiguration mongoConf;
    private final MongoClient mongoClient;

    public MongoDbFruitRepository(MongoDbConfiguration mongoConf,  // <2>
                                  MongoClient mongoClient) {  // <3>
        this.mongoConf = mongoConf;
        this.mongoClient = mongoClient;
    }

    @Override
    public Mono<Boolean> save(@NonNull @NotNull @Valid Fruit fruit){
        return Mono.from(getCollection().insertOne(fruit)) // <4>
                .map(insertOneResult -> Boolean.TRUE)
                .onErrorReturn(Boolean.FALSE);
    }

    @Override
    @NonNull
    public Publisher<Fruit> list() {
        return getCollection().find(); // <4>
    }
    
    @NonNull
    private MongoCollection<Fruit> getCollection(){
        return mongoClient.getDatabase(mongoConf.getName())
                .getCollection(mongoConf.getCollection(), Fruit.class);
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/resources/application.yml
micronaut:
  application:
    name: micronautguide
  server:
      port: 9300
---
#tag::mongodb[]
mongodb:
  uri: mongodb://${MONGO_USER:usef}:${MONGO_PASS:rahasia}@${MONGO_HOST:localhost}:${MONGO_PORT:27017}
#end::mongodb[]
---
#tag::db[]
db:
  name: 'fruit'
  collection: 'fruit'
#end::db[]

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/main/resources/logback.xml
<configuration>

    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <withJansi>true</withJansi>
        <!-- encoders are assigned the type
             ch.qos.logback.classic.encoder.PatternLayoutEncoder by default -->
        <encoder>
            <pattern>%cyan(%d{HH:mm:ss.SSS}) %gray([%thread]) %highlight(%-5level) %magenta(%logger{36}) - %msg%n</pattern>
        </encoder>
    </appender>

    <root level="info">
        <appender-ref ref="STDOUT" />
    </root>
</configuration>

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/test/java/example/micronaut/FruitClient.java
package example.micronaut;

import io.micronaut.core.annotation.NonNull;
import io.micronaut.http.HttpStatus;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Post;
import io.micronaut.http.client.annotation.Client;
import javax.validation.Valid;
import javax.validation.constraints.NotNull;
import java.util.List;

@Client("/fruits")
public interface FruitClient {

    @Post
    @NonNull
    HttpStatus save(@NonNull @NotNull @Valid Fruit fruit);

    @NonNull
    @Get
    List<Fruit> findAll();
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/test/java/example/micronaut/FruitControllerTest.java
package example.micronaut;

import io.micronaut.http.HttpStatus;
import io.micronaut.test.extensions.junit5.annotation.MicronautTest;
import io.micronaut.test.support.TestPropertyProvider;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.TestInstance;
import org.junit.jupiter.api.TestInstance.Lifecycle;

@MicronautTest
@TestInstance(Lifecycle.PER_CLASS)
public class FruitControllerTest implements TestPropertyProvider {

    @Test
    void fruitsEndpointInteractsWithMongo(FruitClient fruitClient) {
        List<Fruit> fruits = fruitClient.findAll();
        assertTrue(fruits.isEmpty());

        HttpStatus status = fruitClient.save(new Fruit("banana"));

        assertEquals(HttpStatus.CREATED, status);
        fruits = fruitClient.findAll();
        assertFalse(fruits.isEmpty());
        assertEquals("banana", fruits.get(0).getName());
        assertNull(fruits.get(0).getDescription());

        status = fruitClient.save(new Fruit("Apple", "Keeps the doctor away"));
        assertEquals(HttpStatus.CREATED, status);
        fruits = fruitClient.findAll();
        assertTrue(fruits.stream()
                .filter(f -> f.getDescription() != null && f.getDescription().equals("Keeps the doctor away"))
                .findFirst()
                .isPresent());
    }

    @AfterAll
    static void cleanup() {
        MongoDbUtils.closeMongoDb();
    }

    @Override
    public Map<String, String> getProperties() {
        MongoDbUtils.startMongoDb();
        return Collections.singletonMap("mongodb.uri", MongoDbUtils.getMongoDbUri());
    }
}
--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/test/java/example/micronaut/FruitControllerValidationTest.java
package example.micronaut;

import io.micronaut.context.annotation.Property;
import io.micronaut.context.annotation.Replaces;
import io.micronaut.context.annotation.Requires;
import io.micronaut.core.async.publisher.Publishers;
import io.micronaut.http.HttpRequest;
import static io.micronaut.http.HttpStatus.BAD_REQUEST;

import io.micronaut.http.HttpStatus;
import io.micronaut.http.client.HttpClient;
import io.micronaut.http.client.annotation.Client;
import io.micronaut.http.client.exceptions.HttpClientResponseException;
import io.micronaut.test.extensions.junit5.annotation.MicronautTest;
import jakarta.inject.Inject;
import jakarta.inject.Singleton;
import org.junit.jupiter.api.Test;
import org.reactivestreams.Publisher;
import reactor.core.publisher.Mono;

import java.util.Collections;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

@Property(name = "spec.name", value = "FruitControllerValidationTest")
@MicronautTest
public class FruitControllerValidationTest {
    @Inject
    @Client("/")
    HttpClient httpClient;

    @Test
    public void testFruitIsValidated() {
        HttpClientResponseException e = assertThrows(HttpClientResponseException.class, () ->
                httpClient.toBlocking().exchange(HttpRequest.POST("/fruits",new Fruit("", "Hola"))));
        assertEquals(HttpStatus.BAD_REQUEST, e.getStatus());
    }

    @Requires(property = "spec.name", value = "FruitControllerValidationTest")
    @Singleton
    @Replaces(FruitRepository.class)
    static class MockFruitRepository implements FruitRepository {
        @Override
        public Publisher<Fruit> list() {
            return Publishers.empty();
        }

        @Override
        public Mono<Boolean> save(Fruit fruit) {
            return Mono.just(Boolean.FALSE);
        }


    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/test/java/example/micronaut/MicronautguideTest.java
package example.micronaut;

import io.micronaut.runtime.EmbeddedApplication;
import io.micronaut.test.extensions.junit5.annotation.MicronautTest;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.Assertions;

import jakarta.inject.Inject;

@MicronautTest
class MicronautguideTest {

    @Inject
    EmbeddedApplication<?> application;

    @Test
    void testItWorks() {
        Assertions.assertTrue(application.isRunning());
    }

}

--#

--% C:/tmp/hapus/fl1/myjava/pake-micronaut/src/test/java/example/micronaut/MongoDbUtils.java
package example.micronaut;

import org.testcontainers.containers.MongoDBContainer;
import org.testcontainers.utility.DockerImageName;

public class MongoDbUtils {
    static MongoDBContainer mongoDBContainer;

    public static void startMongoDb() {
        if (mongoDBContainer == null) {
            mongoDBContainer = new MongoDBContainer(DockerImageName.parse("mongo:4.0.10"))
                    .withExposedPorts(27017);
        }
        if (!mongoDBContainer.isRunning()) {
            mongoDBContainer.start();
        }
    }

    public static String getMongoDbUri() {
        if (mongoDBContainer == null || !mongoDBContainer.isRunning()) {
            startMongoDb();
        }
        return mongoDBContainer.getReplicaSetUrl();
    }

    public static void closeMongoDb() {
        if (mongoDBContainer != null) {
            mongoDBContainer.close();
        }
    }
}
--#

