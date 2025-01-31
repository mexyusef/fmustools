--% index/fmus
fsdw,d(/mk)
	%utama=__FILE__
	config.yml,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/config.yml)
	dependency-reduced-pom.xml,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/dependency-reduced-pom.xml)
	docker-compose.yml,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/docker-compose.yml)
	pom.xml,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/pom.xml)
	README.md,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/README.md)
	run.sh,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/run.sh)
	work.fmus,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/work.fmus)
	src,d(/mk)
		main,d(/mk)
			java,d(/mk)
				de,d(/mk)
					fulgent,d(/mk)
						DropWizzApplication.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/DropWizzApplication.java)
						DropWizzConfiguration.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/DropWizzConfiguration.java)
						apps,d(/mk)
							category,d(/mk)
							order,d(/mk)
							product,d(/mk)
								Product.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/apps/product/Product.java)
								ProductClient.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/apps/product/ProductClient.java)
								ProductDAO.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/apps/product/ProductDAO.java)
								ProductMapper.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/apps/product/ProductMapper.java)
								ProductResource.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/apps/product/ProductResource.java)
							user,d(/mk)
						main,d(/mk)
							Credentials.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/Credentials.java)
							DropwizardMongoDBHealthCheck.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/DropwizardMongoDBHealthCheck.java)
							MongoDBConnection.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/MongoDBConnection.java)
							MongoDBFactoryConnection.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/MongoDBFactoryConnection.java)
							MongoDBManaged.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/MongoDBManaged.java)
							ObjectIdSerializer.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/ObjectIdSerializer.java)
							PasswordSerializer.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/PasswordSerializer.java)
							Response.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/Response.java)
							Seed.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/Seed.java)
			resources,d(/mk)
				banner.txt,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/resources/banner.txt)
				assets,d(/mk)
		test,d(/mk)
			java,d(/mk)
				de,d(/mk)
					fulgent,d(/mk)
						api,d(/mk)
						client,d(/mk)
						core,d(/mk)
						db,d(/mk)
						resources,d(/mk)
			resources,d(/mk)
				fixtures,d(/mk)
--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/config.yml
server:
  maxThreads: 512
  applicationContextPath: /dw
  applicationConnectors:
    - type: http
      port: 9100
  adminConnectors:
    - type: http
      port: 9101

logging:
  level: INFO
  loggers:
    com.demo: INFO

mongoDBConnection:
  credentials:
    username: "usef"
    password: "rahasia"
  seeds:
    - host: "localhost"
      port: 27017
  database: "tempdb_draft"
  authenticator: "admin"

swagger:
  basePath: /dw
  resourcePackage: de.fulgent.apps
  scan: true
  info:
    version: "1.0.0"
    title: "Donuts API CRUD"
    description: "A simple API used for expose CRUD operation on MongoDB collection"
    termsOfService: "http://swagger.io/terms/"
    contact:
      name: "Donuts API "
    license:
      name: "Usef"

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/dependency-reduced-pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">
  <modelVersion>4.0.0</modelVersion>
  <groupId>fulgent</groupId>
  <artifactId>coba2</artifactId>
  <name>DropWizz</name>
  <version>1.0-SNAPSHOT</version>
  <build>
    <plugins>
      <plugin>
        <artifactId>maven-shade-plugin</artifactId>
        <version>3.2.4</version>
        <executions>
          <execution>
            <phase>package</phase>
            <goals>
              <goal>shade</goal>
            </goals>
          </execution>
        </executions>
        <configuration>
          <createDependencyReducedPom>true</createDependencyReducedPom>
          <transformers>
            <transformer />
            <transformer>
              <mainClass>${mainClass}</mainClass>
            </transformer>
          </transformers>
          <filters>
            <filter>
              <artifact>*:*</artifact>
              <excludes>
                <exclude>META-INF/*.SF</exclude>
                <exclude>META-INF/*.DSA</exclude>
                <exclude>META-INF/*.RSA</exclude>
              </excludes>
            </filter>
          </filters>
        </configuration>
      </plugin>
      <plugin>
        <artifactId>maven-jar-plugin</artifactId>
        <version>3.2.0</version>
        <configuration>
          <archive>
            <manifest>
              <addClasspath>true</addClasspath>
              <mainClass>${mainClass}</mainClass>
            </manifest>
          </archive>
        </configuration>
      </plugin>
      <plugin>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.1</version>
        <configuration>
          <source>1.8</source>
          <target>1.8</target>
        </configuration>
      </plugin>
      <plugin>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>2.22.2</version>
      </plugin>
      <plugin>
        <artifactId>maven-source-plugin</artifactId>
        <version>3.2.1</version>
        <executions>
          <execution>
            <id>attach-sources</id>
            <goals>
              <goal>jar</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
      <plugin>
        <artifactId>maven-javadoc-plugin</artifactId>
        <version>3.3.0</version>
        <executions>
          <execution>
            <id>attach-javadocs</id>
            <goals>
              <goal>jar</goal>
            </goals>
          </execution>
        </executions>
      </plugin>
    </plugins>
  </build>
  <profiles>
    <profile>
      <id>java11+</id>
      <properties>
        <maven.javadoc.skip>true</maven.javadoc.skip>
      </properties>
    </profile>
  </profiles>
  <dependencies>
    <dependency>
      <groupId>io.dropwizard</groupId>
      <artifactId>dropwizard-testing</artifactId>
      <version>1.3.5</version>
      <scope>test</scope>
      <exclusions>
        <exclusion>
          <artifactId>junit</artifactId>
          <groupId>junit</groupId>
        </exclusion>
        <exclusion>
          <artifactId>objenesis</artifactId>
          <groupId>org.objenesis</groupId>
        </exclusion>
        <exclusion>
          <artifactId>assertj-core</artifactId>
          <groupId>org.assertj</groupId>
        </exclusion>
        <exclusion>
          <artifactId>jersey-test-framework-provider-inmemory</artifactId>
          <groupId>org.glassfish.jersey.test-framework.providers</groupId>
        </exclusion>
      </exclusions>
    </dependency>
    <dependency>
      <groupId>org.mockito</groupId>
      <artifactId>mockito-core</artifactId>
      <version>2.23.0</version>
      <scope>test</scope>
      <exclusions>
        <exclusion>
          <artifactId>byte-buddy</artifactId>
          <groupId>net.bytebuddy</groupId>
        </exclusion>
        <exclusion>
          <artifactId>byte-buddy-agent</artifactId>
          <groupId>net.bytebuddy</groupId>
        </exclusion>
        <exclusion>
          <artifactId>objenesis</artifactId>
          <groupId>org.objenesis</groupId>
        </exclusion>
      </exclusions>
    </dependency>
  </dependencies>
  <reporting>
    <plugins>
      <plugin>
        <artifactId>maven-project-info-reports-plugin</artifactId>
        <version>3.1.2</version>
        <configuration>
          <dependencyLocationsEnabled>false</dependencyLocationsEnabled>
          <dependencyDetailsEnabled>false</dependencyDetailsEnabled>
        </configuration>
      </plugin>
      <plugin>
        <artifactId>maven-javadoc-plugin</artifactId>
        <version>3.3.0</version>
      </plugin>
    </plugins>
  </reporting>
  <dependencyManagement>
    <dependencies>
      <dependency>
        <groupId>io.dropwizard</groupId>
        <artifactId>dropwizard-bom</artifactId>
        <version>${dropwizard.version}</version>
        <type>pom</type>
        <scope>import</scope>
      </dependency>
    </dependencies>
  </dependencyManagement>
  <properties>
    <dropwizard.version>1.3.5</dropwizard.version>
    <mainClass>de.fulgent.DropWizzApplication</mainClass>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <mongodb.version>3.8.2</mongodb.version>
    <mockito.core.version>2.23.0</mockito.core.version>
    <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
    <dropwizard.swagger.version>1.0.6-1</dropwizard.swagger.version>
  </properties>
</project>

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/docker-compose.yml
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
  phppgadmin:
    image: docker.io/bitnami/phppgadmin:7
    ports:
      - '7001:8080'
      - '7002:8443'
    depends_on:
      - db
--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/pom.xml
<?xml version="1.0" encoding="UTF-8"?>
<project
        xmlns="http://maven.apache.org/POM/4.0.0"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">

    <modelVersion>4.0.0</modelVersion>

    <groupId>fulgent</groupId>
    <artifactId>coba2</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>jar</packaging>

    <name>DropWizz</name>

    <properties>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <!-- <dropwizard.version>2.0.25</dropwizard.version> -->
        <dropwizard.version>1.3.5</dropwizard.version>
        <mainClass>de.fulgent.DropWizzApplication</mainClass>

        <dropwizard.swagger.version>1.0.6-1</dropwizard.swagger.version>
        <mockito.core.version>2.23.0</mockito.core.version>
        <mongodb.version>3.8.2</mongodb.version>
    </properties>

    <dependencyManagement>
        <dependencies>

            <dependency>
                <groupId>io.dropwizard</groupId>
                <artifactId>dropwizard-bom</artifactId>
                <version>${dropwizard.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>

        </dependencies>

    </dependencyManagement>

    <dependencies>
        <dependency>
            <groupId>io.dropwizard</groupId>
            <artifactId>dropwizard-core</artifactId>
        </dependency>
        <dependency>
            <groupId>com.fasterxml.jackson.core</groupId>
            <artifactId>jackson-annotations</artifactId>
        </dependency>
        <!-- <dependency>
            <groupId>jakarta.validation</groupId>
            <artifactId>jakarta.validation-api</artifactId>
        </dependency> -->
        <!-- <dependency>
            <groupId>org.hibernate.validator</groupId>
            <artifactId>hibernate-validator</artifactId>
        </dependency> -->



        <dependency>
            <groupId>org.glassfish.jaxb</groupId>
            <artifactId>jaxb-runtime</artifactId>
            <version>2.3.2</version>
        </dependency>
        <dependency>
            <groupId>jakarta.xml.bind</groupId>
            <artifactId>jakarta.xml.bind-api</artifactId>
            <version>2.3.2</version>
        </dependency>
        <dependency>
            <groupId>org.mongodb</groupId>
            <artifactId>mongodb-driver-sync</artifactId>
            <version>${mongodb.version}</version>
        </dependency>

        <dependency>
            <groupId>com.smoketurner</groupId>
            <artifactId>dropwizard-swagger</artifactId>
            <version>${dropwizard.swagger.version}</version>
        </dependency>
        <dependency>
            <groupId>io.dropwizard</groupId>
            <artifactId>dropwizard-testing</artifactId>
            <scope>test</scope>
        </dependency>

        <dependency>
            <groupId>org.mockito</groupId>
            <artifactId>mockito-core</artifactId>
            <version>${mockito.core.version}</version>
            <scope>test</scope>
        </dependency>

    </dependencies>

    <build>
        <plugins>
            <plugin>
                <artifactId>maven-shade-plugin</artifactId>
                <version>3.2.4</version>
                <configuration>
                    <createDependencyReducedPom>true</createDependencyReducedPom>
                    <transformers>
                        <transformer implementation="org.apache.maven.plugins.shade.resource.ServicesResourceTransformer"/>
                        <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
                            <mainClass>${mainClass}</mainClass>
                        </transformer>
                    </transformers>
                    <!-- exclude signed Manifests -->
                    <filters>
                        <filter>
                            <artifact>*:*</artifact>
                            <excludes>
                                <exclude>META-INF/*.SF</exclude>
                                <exclude>META-INF/*.DSA</exclude>
                                <exclude>META-INF/*.RSA</exclude>
                            </excludes>
                        </filter>
                    </filters>
                </configuration>
                <executions>
                    <execution>
                        <phase>package</phase>
                        <goals>
                            <goal>shade</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <artifactId>maven-jar-plugin</artifactId>
                <version>3.2.0</version>
                <configuration>
                    <archive>
                        <manifest>
                            <addClasspath>true</addClasspath>
                            <mainClass>${mainClass}</mainClass>
                        </manifest>
                    </archive>
                </configuration>
            </plugin>
            <plugin>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.8.1</version>
                <configuration>
                    <source>1.8</source>
                    <target>1.8</target>
                </configuration>
            </plugin>
            <plugin>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>2.22.2</version>
            </plugin>
            <plugin>
                <artifactId>maven-source-plugin</artifactId>
                <version>3.2.1</version>
                <executions>
                    <execution>
                        <id>attach-sources</id>
                        <goals>
                            <goal>jar</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <artifactId>maven-javadoc-plugin</artifactId>
                <version>3.3.0</version>
                <executions>
                    <execution>
                        <id>attach-javadocs</id>
                        <goals>
                            <goal>jar</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

    <reporting>
        <plugins>
            <plugin>
                <artifactId>maven-project-info-reports-plugin</artifactId>
                <version>3.1.2</version>
                <configuration>
                    <dependencyLocationsEnabled>false</dependencyLocationsEnabled>
                    <dependencyDetailsEnabled>false</dependencyDetailsEnabled>
                </configuration>
            </plugin>
            <plugin>
                <artifactId>maven-javadoc-plugin</artifactId>
                <version>3.3.0</version>
            </plugin>
        </plugins>
    </reporting>
    <profiles>
        <profile>
            <id>java11+</id>
            <activation>
                <jdk>[11,)</jdk>
            </activation>
            <properties>
                <!--
                Workaround for "javadoc: error - The code being documented uses modules but the packages
                defined in https://docs.oracle.com/javase/8/docs/api/ are in the unnamed module."
                -->
                <maven.javadoc.skip>true</maven.javadoc.skip>
            </properties>
        </profile>
    </profiles>
</project>

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/README.md
# DropWizz

How to start the DropWizz application
---

1. Run `mvn clean install` to build your application
1. Start application with `java -jar target/coba2-1.0-SNAPSHOT.jar server config.yml`
1. To check that your application is running enter url `http://localhost:8080`

Health Check
---

To see your applications health enter url `http://localhost:8081/healthcheck`

localhost:9100/dw
localhost:9100/dw/products
--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/run.sh
export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:/bin/java::")
mvn clean install && java -jar target/coba2-1.0-SNAPSHOT.jar server config.yml

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/work.fmus
*~localhost:9222/users/update_password p json {identitas=Wiranto,password=rahasia}
*~http://172.21.117.18:9000/dw/products p json {identitas=Wiranto,password=rahasia}

*~http://172.21.117.18:9000/dw/products


de.fulgent.apps.product.ProductResource: Persist a product in collection with the information: Product{id=null, price=24.0, flavor='coklat'}
*~http://172.21.117.18:9000/dw/products p json {price=24,flavor=coklat}

*~http://172.21.117.18:9000/dw/products p json {price=24,flavor=coklat}

*~http://172.21.117.18:9000/dw/products p json {price=12,flavor=hitam}
--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/DropWizzApplication.java
package de.fulgent;

import de.fulgent.main.*;
import de.fulgent.apps.product.*;

import io.dropwizard.Application;
import io.dropwizard.setup.Bootstrap;
import io.dropwizard.setup.Environment;

import io.federecio.dropwizard.swagger.SwaggerBundle;
import io.federecio.dropwizard.swagger.SwaggerBundleConfiguration;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class DropWizzApplication extends Application<DropWizzConfiguration> {

    private static final Logger LOGGER = LoggerFactory.getLogger(DropWizzApplication.class);

    public static void main(final String[] args) throws Exception {
        LOGGER.info("Start application.");
        new DropWizzApplication().run(args);
    }

    @Override
    public String getName() {
        return "DropWizz";
    }

    @Override
    public void initialize(final Bootstrap<DropWizzConfiguration> bootstrap) {
        // TODO: application initialization
        bootstrap.addBundle(new SwaggerBundle<DropWizzConfiguration>() {
            @Override
            protected SwaggerBundleConfiguration getSwaggerBundleConfiguration(
                final DropWizzConfiguration dropWizzConfiguration
            ) {
                return dropWizzConfiguration.getSwaggerBundleConfiguration();
            }
        });
    }

    @Override
    public void run(final DropWizzConfiguration configuration,
                    final Environment environment) {
        // TODO: implement application
        final MongoDBFactoryConnection mongoDBManagerConn = new MongoDBFactoryConnection(configuration.getMongoDBConnection());
        final MongoDBManaged mongoDBManaged = new MongoDBManaged(mongoDBManagerConn.getClient());
        final ProductDAO productDAO = new ProductDAO(mongoDBManagerConn.getClient()
            .getDatabase(configuration.getMongoDBConnection().getDatabase())
            .getCollection("products"));

        environment
            .lifecycle()
            .manage(mongoDBManaged);
        environment
            .jersey()
            .register(
                new ProductResource(productDAO)
            );
        environment.healthChecks().register("DropwizardMongoDBHealthCheck",
            new DropwizardMongoDBHealthCheck(mongoDBManagerConn.getClient()));
    }

}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/DropWizzConfiguration.java
package de.fulgent;

import de.fulgent.main.*;

import io.dropwizard.Configuration;
import com.fasterxml.jackson.annotation.JsonProperty;
import org.hibernate.validator.constraints.*;
import javax.validation.constraints.*;

import io.federecio.dropwizard.swagger.SwaggerBundleConfiguration;

public class DropWizzConfiguration extends Configuration {
    // TODO: implement service configuration
    private MongoDBConnection mongoDBConnection;

    @JsonProperty("swagger")
    private SwaggerBundleConfiguration swaggerBundleConfiguration;

    public MongoDBConnection getMongoDBConnection() {
        return mongoDBConnection;
    }

    public void setMongoDBConnection(final MongoDBConnection mongoDBConnection) {
        this.mongoDBConnection = mongoDBConnection;
    }

    public SwaggerBundleConfiguration getSwaggerBundleConfiguration() {
        return swaggerBundleConfiguration;
    }

    public void setSwaggerBundleConfiguration(final SwaggerBundleConfiguration swaggerBundleConfiguration) {
        this.swaggerBundleConfiguration = swaggerBundleConfiguration;
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/apps/product/Product.java
package de.fulgent.apps.product;

import javax.validation.constraints.NotNull;
import java.io.Serializable;
import java.util.Objects;

import org.bson.types.ObjectId;

import de.fulgent.main.ObjectIdSerializer;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;

public class Product implements Serializable {

    /** The id.*/
    @JsonSerialize(using = ObjectIdSerializer.class)
    private ObjectId id;

    /** The price. */
    @NotNull
    private double price;

    /** The principal flavor.*/
    @NotNull
    private String flavor;

    /**
     * Constructor.
     */
    public Product() {
    }

    @Override
    public boolean equals(final Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        final Product product = (Product) o;
        return Double.compare(product.price, price) == 0 &&
                Objects.equals(id, product.id) &&
                Objects.equals(flavor, product.flavor);
    }

    @Override
    public int hashCode() {
        return Objects.hash(id, price, flavor);
    }

    /**
     * Gets the id.
     *
     * @return the value id.
     */
    public ObjectId getId() {
        return id;
    }

    /**
     * Sets the id.
     *
     * @param id value.
     */
    public void setId(final ObjectId id) {
        this.id = id;
    }

    /**
     * Gets the price.
     *
     * @return the value price.
     */
    public double getPrice() {
        return price;
    }

    /**
     * Sets the price.
     *
     * @param price value.
     */
    public void setPrice(double price) {
        this.price = price;
    }

    /**
     * Gets the flavor.
     *
     * @return the value flavor.
     */
    public String getFlavor() {
        return flavor;
    }

    /**
     * Sets the flavor.
     *
     * @param flavor value.
     */
    public void setFlavor(String flavor) {
        this.flavor = flavor;
    }

    @Override
    public String toString() {
        return "Product{"
                + "id=" + id
                + ", price=" + price
                + ", flavor='" + flavor + '\''
                + '}';
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/apps/product/ProductClient.java
package de.fulgent.apps.product;

import java.util.Arrays;
import java.util.List;
import javax.ws.rs.client.Client;
import javax.ws.rs.client.Entity;
import javax.ws.rs.client.Invocation;
import javax.ws.rs.client.WebTarget;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

/**
 * This class serve the purpose of client jersey for this API.
 *
 * @author Rich Lopez
 * @version 1.0.0
 * @since 1.0.0
 */
public class ProductClient {

    /**
     * Client to connect.
     */
    private Client client;

    /**
     * Base of URL to connect.
     */
    private String basePath;

    /**
     * Constructor.
     *
     * @param client   the client jersey.
     * @param basePath the base path.
     */
    public ProductClient(final Client client, final String basePath) {
        this.client = client;
        this.basePath = basePath;
    }

    /**
     * Get all {@link Product} objects.
     *
     * @return A list of {@link Product} in other case null.
     */
    public List<Product> all() {
        final WebTarget webTarget = client.target(basePath);
        final Invocation.Builder builder = webTarget.request();
        final Response response = builder.accept(MediaType.APPLICATION_JSON).get();

        if (Response.Status.OK.getStatusCode() == response.getStatus()) {
            return Arrays.asList(response.readEntity(Product[].class));
        }
        return null;
    }

    /**
     * Get a {@link Product} object.
     *
     * @param id the identifier
     * @return A object {@link Product} or null in case not found.
     */
    public Product getOne(final String id) {
        final WebTarget webTarget = client.target(basePath).path("/").path(id);
        final Invocation.Builder builder = webTarget.request();
        final Response response = builder.accept(MediaType.APPLICATION_JSON).get();

        if (Response.Status.OK.getStatusCode() == response.getStatus()) {
            return response.readEntity(Product.class);
        }
        return null;
    }

    /**
     * Persist a object of type {@link Product}.
     *
     * @param product the product.
     * @throws Exception when can not save.
     */
    public void save(final Product product) throws Exception {
        final WebTarget webTarget = client.target(basePath);
        final Invocation.Builder builder = webTarget.request();
        final Response response = builder.accept(MediaType.APPLICATION_JSON)
                .post(Entity.entity(product, MediaType.APPLICATION_JSON));

        if (Response.Status.NO_CONTENT.getStatusCode() != response.getStatus()) {
            throw new Exception("Can not save Product.");
        }
    }

    /**
     * Update the information about a {@link Product}.
     *
     * @param id    the identifier.
     * @param product the product information.
     * @throws Exception when can not update the Dounut object.
     */
    public void update(final String id, Product product) throws Exception {
        final WebTarget webTarget = client.target(basePath).path("/").path(id);
        final Invocation.Builder builder = webTarget.request();
        final Response response = builder.accept(MediaType.APPLICATION_JSON)
                .put(Entity.entity(product, MediaType.APPLICATION_JSON));

        if (Response.Status.NO_CONTENT.getStatusCode() != response.getStatus()) {
            throw new Exception("Can not save Product.");
        }
    }

    /**
     * Delete a {@link Product} the product object.
     *
     * @param id the identifier of Product.
     */
    public void delete(final String id) throws Exception {
        final WebTarget webTarget = client.target(basePath).path("/").path(id);
        final Invocation.Builder builder = webTarget.request();
        final Response response = builder.accept(MediaType.APPLICATION_JSON)
                .delete();

        if (Response.Status.NO_CONTENT.getStatusCode() != response.getStatus()) {
            throw new Exception("Can not save Product.");
        }
    }

}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/apps/product/ProductDAO.java
package de.fulgent.apps.product;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

import com.mongodb.client.MongoCollection;
import com.mongodb.client.MongoCursor;
import org.bson.Document;
import org.bson.types.ObjectId;

/**
 * Data Access Object for objects of type {@link Product}.
 *
 * @version 1.0.0
 * @author Rich Lopez
 * @since 1.0.0
 */
public class ProductDAO {

    /**
     * The collection of Products
     */
    final MongoCollection<Document> productCollection;

    /**
     * Constructor.
     *
     * @param productCollection the collection of products.
     */
    public ProductDAO(final MongoCollection<Document> productCollection) {
        this.productCollection = productCollection;
    }

    /**
     * Find all products.
     *
     * @return the products.
     */
    public List<Product> getAll() {
        final MongoCursor<Document> products = productCollection.find().iterator();
        final List<Product> productsFind = new ArrayList<>();
        try {
            while (products.hasNext()) {
                final Document product = products.next();
                productsFind.add(ProductMapper.map(product));
            }
        } finally {
            products.close();
        }
        return productsFind;
    }

    /**
     * Get one document find in other case return null.
     *
     * @param id the identifier for find.
     * @return the Product find.
     */
    public Product getOne(final ObjectId id) {
        final Optional<Document> productFind = Optional.ofNullable(productCollection.find(new Document("_id", id)).first());
        return productFind.isPresent() ? ProductMapper.map(productFind.get()) : null;
    }

    public void save(final Product product){
        final Document saveProduct =new Document("price", product.getPrice())
                                      .append("flavor", product.getFlavor());
        productCollection.insertOne(saveProduct);
    }


    /**
     * Update a register.
     *
     * @param id the identifier.
     * @param product the object to update.
     */
    public void update(final ObjectId id, final Product product) {
        productCollection.updateOne(new Document("_id", id),
                new Document("$set", new Document("price", product.getPrice())
                        .append("flavor", product.getFlavor()))
        );
    }

    /**
     * Delete a register.
     * @param id    the identifier.
     */
    public void delete(final ObjectId id){
        productCollection.deleteOne(new Document("_id", id));
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/apps/product/ProductMapper.java
package de.fulgent.apps.product;

import org.bson.Document;

/**
 * Mapper class for Products objects.
 *
 * @author Rich Lopez
 * @version 1.0.0
 * @since 1.0.0
 */
public class ProductMapper {

    /**
     * Map objects {@link Document} to {@link Product}.
     *
     * @param productDocument the information document.
     * @return A object {@link Product}.
     */
    public static Product map(final Document productDocument) {
        final Product product = new Product();
        product.setId(productDocument.getObjectId("_id"));
        product.setFlavor(productDocument.getString("flavor"));
        product.setPrice(productDocument.getDouble("price"));
        return product;
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/apps/product/ProductResource.java
package de.fulgent.apps.product;

import java.util.List;

import javax.validation.constraints.NotNull;
import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

import org.bson.types.ObjectId;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiParam;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Api(value = "products",
     description = "Products REST API for handle Products CRUD operations on products collection.",
     tags = {"products"})
@Path("/products")
@Produces(MediaType.APPLICATION_JSON)
public class ProductResource {

    /**
     * Logger class.
     */
    private static final Logger LOGGER = LoggerFactory.getLogger(ProductResource.class);

    /**
     * DAO product.
     */
    private ProductDAO productDAO;

    /**
     * Constructor.
     *
     * @param productDAO the dao product.
     */
    public ProductResource(final ProductDAO productDAO) {
        this.productDAO = productDAO;
    }

    /**
     * Get all {@link Product} objects.
     *
     * @return A object {@link Response} with the information of result this method.
     */
    @ApiResponses(value = {
            @ApiResponse(code = 200, message = "Operation success."),
            @ApiResponse(code = 404, message = "Products not found")
    })
    @GET
    public Response all() {
        LOGGER.info("List all Products.");
        final List<Product> productsFind = productDAO.getAll();
        if (productsFind.isEmpty()) {
            return Response.accepted(new de.fulgent.main.Response("Products not found."))
                    .status(Response.Status.NOT_FOUND)
                    .build();
        }
        return Response.ok(productsFind).build();
    }

    /**
     * Get a {@link Product} by identifier.
     *
     * @param id the identifier.
     * @return A object {@link Response} with the information of result this method.
     */
    @ApiResponses(value = {
            @ApiResponse(code = 200, message = "Operation success."),
            @ApiResponse(code = 404, message = "Products not found")
    })
    @GET
    @Path("/{id}")
    public Response getOne(@ApiParam(value = "id") @PathParam("id") @NotNull final ObjectId id) {
        LOGGER.info("Find the product by identifier : " + id.toString());
        final Product product = productDAO.getOne(id);
        if (product != null) {
            return Response.ok(product).build();
        }
        return Response.accepted(new de.fulgent.main.Response("Product not found.")).build();
    }

    /**
     * Persis a {@link Product} object in a collection.
     *
     * @param product The objecto to persist.
     * @return A object {@link Response} with the information of result this method.
     */
    @ApiResponses(value = {
            @ApiResponse(code = 200, message = "Operation success.")
    })
    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Response save(@ApiParam(value = "Product") @NotNull final Product product) {
        LOGGER.info("Persist a product in collection with the information: {}", product);
        productDAO.save(product);
        return Response.status(Response.Status.CREATED).build();
    }

    /**
     * Update the information of a {@link Product}.
     *
     * @param id    The identifier.
     * @param product the product information.
     * @return A object {@link Response} with the information of result this method.
     */
    @ApiResponses(value = {
            @ApiResponse(code = 200, message = "Operation success.")
    })
    @PUT
    @Path("/{id}")
    public Response update(@ApiParam(value = "id") @PathParam("id") @NotNull final ObjectId id,
                           @ApiParam(value = "Product") @NotNull final Product product) {
        LOGGER.info("Update the information of a product : {} ", product);
        productDAO.update(id, product);
        return Response.ok().build();
    }

    /**
     * Delete a {@link Product} object.
      * @param id   the identifier.
     * @return  A object {@link Response} with the information of result this method.
     */
    @ApiResponses(value = {
            @ApiResponse(code = 200, message = "Operation success.")
    })
    @DELETE
    @Path("/{id}")
    public Response delete(@ApiParam(value = "id") @PathParam("id") @NotNull final ObjectId id) {
        LOGGER.info("Delete a product from collection with identifier: " + id.toString());
        productDAO.delete(id);
        return Response.ok().build();
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/Credentials.java
package de.fulgent.main;

import java.util.Arrays;
import java.util.Objects;

import com.fasterxml.jackson.databind.annotation.JsonSerialize;

public class Credentials {

    /** The user name.*/
    private String username;

    /** The password.*/
    @JsonSerialize(using = PasswordSerializer.class)
    private char[] password;

    /**
     * Constructor.
     */
    public Credentials() {
    }

    @Override
    public boolean equals(final Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        final Credentials that = (Credentials) o;
        return Objects.equals(username, that.username) &&
                Arrays.equals(password, that.password);
    }

    @Override
    public int hashCode() {
        int result = Objects.hash(username);
        result = 31 * result + Arrays.hashCode(password);
        return result;
    }

    /**
     * Gets the user name.
     * @return  the user name.
     */
    public String getUsername() {
        return username;
    }

    /**
     * Sets the user name.
     * @param username  the user name.
     */
    public void setUsername(final String username) {
        this.username = username;
    }

    /**
     * Gets the user name.
     * @return  the user name.
     */
    public char[] getPassword() {
        return password;
    }

    /**
     * Sets the password.
     * @param password  the password.
     */
    public void setPassword(final char[] password) {
        this.password = password;
    }

    @Override
    public String toString() {
        return "Credentials{"
                + "username='" + username + '\''
                + ", password=" + Arrays.toString(password)
                + '}';
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/DropwizardMongoDBHealthCheck.java
package de.fulgent.main;

import org.bson.Document;

import com.codahale.metrics.health.HealthCheck;
import com.mongodb.client.MongoClient;

/**
 * This class handle the MongoDB Health Check.
 *
 * @author Rich Lopez
 * @version 1.0.0
 * @since 1.0.0
 */
public class DropwizardMongoDBHealthCheck extends HealthCheck {

    /**
     * A client of MongoDB.
     */
    private MongoClient mongoClient;

    /**
     * Constructor.
     *
     * @param mongoClient the mongo client.
     */
    public DropwizardMongoDBHealthCheck(final MongoClient mongoClient) {
        this.mongoClient = mongoClient;
    }

    @Override
    protected Result check() {
        try {
            final Document document = mongoClient.getDatabase("products").runCommand(new Document("buildInfo", 1));
            if (document == null) {
                return Result.unhealthy("Can not perform operation buildInfo in Database.");
            }
        } catch (final Exception e) {
            return Result.unhealthy("Can not get the information from database.");
        }
        return Result.healthy();
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/MongoDBConnection.java
package de.fulgent.main;

import java.util.List;

/**
 * This has the configuration for connect to MongoDB database.
 *
 * @version 1.0.0
 * @author Rich Lopez
 * @since 1.0.0
 */
public class MongoDBConnection {

    /**
     * The credentials user and password.
     */
    private Credentials credentials;

    /**
     * The lis of seeds.
     */
    private List<Seed> seeds;

    /**
     * The db.
     */
    private String database;

    private String authenticator;

    /**
     * Gets the credentials.
     *
     * @return the value credentials.
     */
    public Credentials getCredentials() {
        return credentials;
    }

    /**
     * Sets the credentials.
     *
     * @param credentials value.
     */
    public void setCredentials(final Credentials credentials) {
        this.credentials = credentials;
    }

    /**
     * Gets the seeds.
     *
     * @return the value seeds.
     */
    public List<Seed> getSeeds() {
        return seeds;
    }

    /**
     * Sets the seeds.
     *
     * @param seeds value.
     */
    public void setSeeds(final List<Seed> seeds) {
        this.seeds = seeds;
    }

    /**
     * Gets the database.
     *
     * @return the value database.
     */
    public String getDatabase() {
        return database;
    }

    /**
     * Sets the database.
     *
     * @param database value.
     */
    public void setDatabase(final String database) {
        this.database = database;
    }


    public String getAuthenticator() {
        return authenticator;
    }
    public void setAuthenticator(final String authenticator) {
        this.authenticator = authenticator;
    }

    @Override
    public String toString() {
        return "MongoDBConnection{"
                + "credentials=" + credentials
                + ", seeds=" + seeds
                + ", database='" + database + '\''
                + '}';
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/MongoDBFactoryConnection.java
package de.fulgent.main;

import java.util.List;
import java.util.stream.Collectors;

import com.mongodb.MongoClientSettings;
import com.mongodb.MongoCredential;
import com.mongodb.ServerAddress;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoClients;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * This class has the porpuse of create a MongoDB client with their configuration.
 *
 * @author Rich Lopez
 * @version 1.0.0
 * @since 1.0.0
 */
public class MongoDBFactoryConnection {

    /**
     * Logger class.
     */
    private static final Logger LOGGER = LoggerFactory.getLogger(MongoDBFactoryConnection.class);

    /**
     * The configuration for connect to MongoDB Server.
     */
    private MongoDBConnection mongoDBConnection;

    /**
     * Constructor.
     *
     * @param mongoDBConnection the mongoDB connection data.
     */
    public MongoDBFactoryConnection(final MongoDBConnection mongoDBConnection) {
        this.mongoDBConnection = mongoDBConnection;
    }

    /**
     * Gets the connection to MongoDB.
     *
     * @return the mongo Client.
     */
    public MongoClient getClient() {
        LOGGER.info("Creating mongoDB client.");
        final Credentials configCredentials = mongoDBConnection.getCredentials();

        final MongoCredential credentials = MongoCredential.createCredential(
                configCredentials.getUsername(),
                // mongoDBConnection.getDatabase(),
                mongoDBConnection.getAuthenticator(),
                configCredentials.getPassword());

        final MongoClient client = MongoClients.create(
                MongoClientSettings.builder()
                        .credential(credentials)
                        .applyToClusterSettings(builder -> builder.hosts(getServers()))
                        .build()
        );

        return client;
    }

    /**
     * Map the object {@link Seed} to objects {@link ServerAddress} that contain the information of servers.
     *
     * @return the list of servers.
     */
    private List<ServerAddress> getServers() {
        final List<Seed> seeds = mongoDBConnection.getSeeds();
        return seeds.stream()
                .map(seed -> {
                    final ServerAddress serverAddress = new ServerAddress(seed.getHost(), seed.getPort());
                    return serverAddress;
                })
                .collect(Collectors.toList());
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/MongoDBManaged.java
package de.fulgent.main;

import com.mongodb.client.MongoClient;
import io.dropwizard.lifecycle.Managed;

/**
 * This is used for manage the connection to MongoDB.
 * @version 1.0.0
 * @since 1.0.0
 * @author Rich Lopez 
 */
public class MongoDBManaged implements Managed {

    /**
     * The mongoDB client.
     */
    private MongoClient mongoClient;

    /**
     * Constructor.
     * @param mongoClient   the mongoDB client.
     */
    public MongoDBManaged(final MongoClient mongoClient) {
        this.mongoClient = mongoClient;
    }

    @Override
    public void start() throws Exception {
    }

    @Override
    public void stop() throws Exception {
        mongoClient.close();
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/ObjectIdSerializer.java
package de.fulgent.main;

import java.io.IOException;

import org.bson.types.ObjectId;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.databind.JsonSerializer;
import com.fasterxml.jackson.databind.SerializerProvider;


/**
 * Serializer for ObjectId to String.
 *
 * @author Rich Lopez
 * @version 1.0.0
 * @since 1.0.0
 */
public class ObjectIdSerializer extends JsonSerializer<ObjectId> {
    @Override
    public void serialize(final ObjectId objectId, final JsonGenerator jsonGenerator,
                          final SerializerProvider serializerProvider) throws IOException {
        jsonGenerator.writeString(objectId.toString());
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/PasswordSerializer.java
package de.fulgent.main;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.databind.JsonSerializer;
import com.fasterxml.jackson.databind.SerializerProvider;

import java.io.IOException;

/**
 * Serializer for String to char[].
 *
 * @author Rich Lopez
 * @version 1.0.0
 * @since 1.0.0
 */
public class PasswordSerializer extends JsonSerializer<String> {
    @Override
    public void serialize(final String input, final JsonGenerator jsonGenerator,
                          final SerializerProvider serializerProvider) throws IOException {
        jsonGenerator.writeString(input.toCharArray(), 0, input.toCharArray().length);
    }

    @Override
    public Class<String> handledType() {
        return String.class;
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/Response.java
package de.fulgent.main;

import java.util.Objects;

/**
 * The class used for response message.
 * @version 1.0.0
 * @since 1.0.0
 * @author Rich Lopez 
 */
public class Response {

    /**
     * The message.
     */
    private String message;

    /**
     * Constructor.
     */
    public Response() {
    }

    /**
     * Constructor.
     * @param message the message.
     */
    public Response(final String message) {
        this.message = message;
    }

    @Override
    public boolean equals(final Object o) {
        if (this == o) {
            return true;
        }
        if (o == null || getClass() != o.getClass()) return false;
        final Response response = (Response) o;
        return Objects.equals(message, response.message);
    }

    @Override
    public int hashCode() {
        return Objects.hash(message);
    }

    /**
     * Gets the message.
     *
     * @return the value message.
     */
    public String getMessage() {
        return message;
    }

    /**
     * Sets the message.
     *
     * @param message value.
     */
    public void setMessage(final String message) {
        this.message = message;
    }

    @Override
    public String toString() {
        return "Response{"
                + "message='" + message + '\''
                + '}';
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/java/de/fulgent/main/Seed.java
package de.fulgent.main;

import java.util.Objects;

/**
 * This class is used for represent a server of MongoDB.
 * @version 1.0.0
 * @since 1.0.0
 * @author Rich Lopez
 */
public class Seed {

    /** The host.*/
    private String host;

    /** The port.*/
    private int port;

    /**
     * Constructor.
     */
    public Seed() {
    }

    @Override
    public boolean equals(final Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        final Seed seed = (Seed) o;
        return port == seed.port &&
                Objects.equals(host, seed.host);
    }

    @Override
    public int hashCode() {
        return Objects.hash(host, port);
    }

    /**
     * Gets the host.
     * @return  the host.
     */
    public String getHost() {
        return host;
    }

    /**
     * Sets the host.
     * @param host  the host.
     */
    public void setHost(final String host) {
        this.host = host;
    }

    /**
     * Gets the port.
     * @return  the port.
     */
    public int getPort() {
        return port;
    }

    /**
     * Sets the port.
     * @param port  the
     */
    public void setPort(final int port) {
        this.port = port;
    }

    @Override
    public String toString() {
        return "Seed{" +
                "host='" + host + '\'' +
                ", port=" + port +
                '}';
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-dropwizard/src/main/resources/banner.txt
================================================================================

                              Jatuhkan Wijar

================================================================================
--#
