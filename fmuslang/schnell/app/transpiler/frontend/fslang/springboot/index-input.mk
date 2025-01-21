--% index/fmus
springboot-pg,d(/mk)
  %utama=__FILE__
  %__TEMPLATE_SERVER_PORT__=__NILAI_SERVER_PORT__
  %__TEMPLATE_PACKAGENAME_ROOTPROJECT__=sbgql1
  %__TEMPLATE_PACKAGENAME_BASEDOT__=de.fulgent
  %__TEMPLATE_PACKAGENAME_FULLBYSLASH__=de/fulgent/sbgql1
  %__TEMPLATE_PACKAGENAME_FULLBYDOT__=de.fulgent.sbgql1
__TEMPLATE_DB_INIT
__TEMPLATE_APP_INIT
  #sbgql1.fmus,f(e=utama=/springbooter/sbgql1.fmus)
  .gitignore,f(e=utama=/springbooter/.gitignore)
  HELP.md,f(e=utama=/springbooter/HELP.md)
  gradlew.bat,f(e=utama=/springbooter/gradlew.bat)
  README.md,f(e=utama=/springbooter/README.md)
  build.gradle,f(e=utama=/springbooter/build.gradle)
  wrapme.sh,f(e=utama=/springbooter/wrapme.sh)
  run.sh,f(e=utama=/springbooter/run.sh)
  run.bat,f(e=utama=/springbooter/run.bat)
  settings.gradle,f(e=utama=/springbooter/settings.gradle)
  gradlew,f(e=utama=/springbooter/gradlew)
  $*chmod a+x *.sh
  src,d(/mk)
    test,d(/mk)
      java,d(/mk)
        de,d(/mk)
          fulgent,d(/mk)
            sbgql1,d(/mk)
              FulgentApplicationTests.java,f(e=utama=/springbooter/src/test/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/FulgentApplicationTests.java)
    main,d(/mk)
      resources,d(/mk)
        application.yml,f(e=utama=/springbooter/src/main/resources/application.yml)
        data.sql,f(e=utama=/springbooter/src/main/resources/data.sql)
        schema.sql,f(e=utama=/springbooter/src/main/resources/schema.sql)
        mybatis-config.xml,f(e=utama=/springbooter/src/main/resources/mybatis-config.xml)
        mapper,d(/mk)
          AttendeeMapper.xml,f(e=utama=/springbooter/src/main/resources/mapper/AttendeeMapper.xml)
__TEMPLATE_APP_XMLMAPPER_ENTRY
        graphql,d(/mk)
          schema.gql,f(e=utama=/springbooter/src/main/resources/graphql/schema.gql)
      java,d(/mk)
        de,d(/mk)
          fulgent,d(/mk)
            sbgql1,d(/mk)
              ServletInitializer.java,f(e=utama=/springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/ServletInitializer.java)
              FulgentApplication.java,f(e=utama=/springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/FulgentApplication.java)
              BaseController.java,f(e=utama=/springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/BaseController.java)
              apps,d(/mk)
                attendee,d(/mk)
                  Attendee.java,f(e=utama=/springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/Attendee.java)
                  AttendeeController.java,f(e=utama=/springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeController.java)
                  AttendeeInput.java,f(e=utama=/springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeInput.java)
                  AttendeeRepository.java,f(e=utama=/springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeRepository.java)
                  AttendeeService.java,f(e=utama=/springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeService.java)
                  AttendeeQuery.java,f(e=utama=/springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeQuery.java)
                  AttendeeMapper.java,f(e=utama=/springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeMapper.java)
                  AttendeeMutation.java,f(e=utama=/springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeMutation.java)
__TEMPLATE_SERVER_APP_CONTENT
  gradle,d(/mk)
    wrapper,d(/mk)
      gradle-wrapper.properties,f(e=utama=/springbooter/gradle/wrapper/gradle-wrapper.properties)

  #$*qterminal 2>/dev/null &
--#

--% /springbooter/__TEMPLATE_PACKAGENAME_ROOTPROJECT__.fmus
urutan:
dari paling low level
repo -> service -> resolver -> schema.gql

/////////////////////////////////////////////////////////////////////

{
  findAttendeeByName(name:"ia") {
    name
  }
}

{
  findAttendeeById(id:3) {
    id
    name
  }  
}

{
  allAttendees {
    id
    name
  }
}

mutation {
  updateAttendee(id:3, attendee:{name:"wieke vlc"}) {
    name
  }
}

mutation {
  createAttendee(attendee:{name:"katy croatia"}) {
    id
    name
  }
}

mutation {
  createAttendee(attendee: {
    name: "clara fuentes"
  }) {
    name
  }
}
/////////////////////////////////////////////////////////////////////

skrg masalahnya apa?
create dan update masih pake field...belum pake create input ...

**$*tree .
.

    │   │               ├── DemoApplication.java
    │   │               └── ServletInitializer.java
    │   └── resources
    │       ├── application.properties
    │       ├── static
    │       └── templates

**src,d
  main,d
    resources,d
      mybatis-config.xml,f(t=)

      schema.sql,f(t=)
      data.sql,f(t=)
      graphql,d(/mk)
        schema.gql,f(t=)
      application.yml,f(t=)

**src,d
  main,d
    java/de/fulgent/sbgql1,d
      apps/attendee,d
        AttendeeMapper.java,f(n=package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee;)

term
**$*pwd
/springbooter

--#

--% /springbooter/.gitignore
HELP.md
.gradle
build/
!gradle/wrapper/gradle-wrapper.jar
!**/src/main/**/build/
!**/src/test/**/build/

### STS ###
.apt_generated
.classpath
.factorypath
.project
.settings
.springBeans
.sts4-cache
bin/
!**/src/main/**/bin/
!**/src/test/**/bin/

### IntelliJ IDEA ###
.idea
*.iws
*.iml
*.ipr
out/
!**/src/main/**/out/
!**/src/test/**/out/

### NetBeans ###
/nbproject/private/
/nbbuild/
/dist/
/nbdist/
/.nb-gradle/

### VS Code ###
.vscode/

--#

--% /springbooter/HELP.md
# Getting Started

### Reference Documentation
For further reference, please consider the following sections:

* [Official Gradle documentation](https://docs.gradle.org)
* [Spring Boot Gradle Plugin Reference Guide](https://docs.spring.io/spring-boot/docs/2.5.2/gradle-plugin/reference/html/)
* [Create an OCI image](https://docs.spring.io/spring-boot/docs/2.5.2/gradle-plugin/reference/html/#build-image)
* [MyBatis Framework](https://mybatis.org/spring-boot-starter/mybatis-spring-boot-autoconfigure/)
* [WebSocket](https://docs.spring.io/spring-boot/docs/2.5.2/reference/htmlsingle/#boot-features-websockets)
* [Spring Web](https://docs.spring.io/spring-boot/docs/2.5.2/reference/htmlsingle/#boot-features-developing-web-applications)
* [Spring Data JPA](https://docs.spring.io/spring-boot/docs/2.5.2/reference/htmlsingle/#boot-features-jpa-and-spring-data)

### Guides
The following guides illustrate how to use some features concretely:

* [MyBatis Quick Start](https://github.com/mybatis/spring-boot-starter/wiki/Quick-Start)
* [Using WebSocket to build an interactive web application](https://spring.io/guides/gs/messaging-stomp-websocket/)
* [Building a RESTful Web Service](https://spring.io/guides/gs/rest-service/)
* [Serving Web Content with Spring MVC](https://spring.io/guides/gs/serving-web-content/)
* [Building REST services with Spring](https://spring.io/guides/tutorials/bookmarks/)
* [Accessing Data with JPA](https://spring.io/guides/gs/accessing-data-jpa/)

### Additional Links
These additional references should also help you:

* [Gradle Build Scans – insights for your project's build](https://scans.gradle.com#gradle)


--#

--% /springbooter/gradlew.bat
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

--% /springbooter/README.md
rest
controller -> mapper java -> mapper xml
                          -> ibatis select/delete
graphql
schema -> resolver -> service -> jpa repository


--#

--% /springbooter/build.gradle
plugins {
  id 'org.springframework.boot' version '2.5.2'
  id 'io.spring.dependency-management' version '1.0.11.RELEASE'
  id 'java'
  id 'war'
}

group = '__TEMPLATE_PACKAGENAME_BASEDOT__'
version = '0.0.1-SNAPSHOT'
sourceCompatibility = '1.8'

configurations {
  compileOnly {
    extendsFrom annotationProcessor
  }
}

repositories {
  mavenCentral()
}

dependencies {
  implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
  implementation 'org.springframework.boot:spring-boot-starter-web'
  implementation 'org.springframework.boot:spring-boot-starter-websocket'
  implementation 'org.mybatis.spring.boot:mybatis-spring-boot-starter:2.2.0'

  implementation 'com.graphql-java:graphql-java:11.0'
  implementation 'com.graphql-java:graphql-java-tools:5.2.4'
  implementation 'com.graphql-java:graphql-java-servlet:6.1.3'
  implementation 'com.graphql-java:graphiql-spring-boot-starter:5.0.2'

  compileOnly 'org.projectlombok:lombok'
  runtimeOnly 'org.hsqldb:hsqldb'
  runtimeOnly 'org.postgresql:postgresql'
  annotationProcessor 'org.projectlombok:lombok'

  providedRuntime 'org.springframework.boot:spring-boot-starter-tomcat'
  testImplementation 'org.springframework.boot:spring-boot-starter-test'

  // https://mvnrepository.com/artifact/org.xerial/sqlite-jdbc
  implementation group: 'org.xerial', name: 'sqlite-jdbc', version: '3.36.0.3'
}

test {
  useJUnitPlatform()
}

--#

--% /springbooter/wrapme.sh
gradle wrapper
--#

--% /springbooter/run.sh
clear && ./gradlew bootRun
--#

--% /springbooter/run.bat
gradle bootRun
--#

--% /springbooter/settings.gradle
rootProject.name = '__TEMPLATE_PACKAGENAME_ROOTPROJECT__'

--#

--% /springbooter/gradlew
#!/usr/bin/env sh

#
# Copyright 2015 the original author or authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

##############################################################################
##
##  Gradle start up script for UN*X
##
##############################################################################

# Attempt to set APP_HOME
# Resolve links: $0 may be a link
PRG="$0"
# Need this for relative symlinks.
while [ -h "$PRG" ] ; do
    ls=`ls -ld "$PRG"`
    link=`expr "$ls" : '.*-> \(.*\)$'`
    if expr "$link" : '/.*' > /dev/null; then
        PRG="$link"
    else
        PRG=`dirname "$PRG"`"/$link"
    fi
done
SAVED="`pwd`"
cd "`dirname \"$PRG\"`/" >/dev/null
APP_HOME="`pwd -P`"
cd "$SAVED" >/dev/null

APP_NAME="Gradle"
APP_BASE_NAME=`basename "$0"`

# Add default JVM options here. You can also use JAVA_OPTS and GRADLE_OPTS to pass JVM options to this script.
DEFAULT_JVM_OPTS='"-Xmx64m" "-Xms64m"'

# Use the maximum available, or set MAX_FD != -1 to use that value.
MAX_FD="maximum"

warn () {
    echo "$*"
}

die () {
    echo
    echo "$*"
    echo
    exit 1
}

# OS specific support (must be 'true' or 'false').
cygwin=false
msys=false
darwin=false
nonstop=false
case "`uname`" in
  CYGWIN* )
    cygwin=true
    ;;
  Darwin* )
    darwin=true
    ;;
  MINGW* )
    msys=true
    ;;
  NONSTOP* )
    nonstop=true
    ;;
esac

CLASSPATH=$APP_HOME/gradle/wrapper/gradle-wrapper.jar


# Determine the Java command to use to start the JVM.
if [ -n "$JAVA_HOME" ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
        # IBM's JDK on AIX uses strange locations for the executables
        JAVACMD="$JAVA_HOME/jre/sh/java"
    else
        JAVACMD="$JAVA_HOME/bin/java"
    fi
    if [ ! -x "$JAVACMD" ] ; then
        die "ERROR: JAVA_HOME is set to an invalid directory: $JAVA_HOME

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
    fi
else
    JAVACMD="java"
    which java >/dev/null 2>&1 || die "ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.

Please set the JAVA_HOME variable in your environment to match the
location of your Java installation."
fi

# Increase the maximum file descriptors if we can.
if [ "$cygwin" = "false" -a "$darwin" = "false" -a "$nonstop" = "false" ] ; then
    MAX_FD_LIMIT=`ulimit -H -n`
    if [ $? -eq 0 ] ; then
        if [ "$MAX_FD" = "maximum" -o "$MAX_FD" = "max" ] ; then
            MAX_FD="$MAX_FD_LIMIT"
        fi
        ulimit -n $MAX_FD
        if [ $? -ne 0 ] ; then
            warn "Could not set maximum file descriptor limit: $MAX_FD"
        fi
    else
        warn "Could not query maximum file descriptor limit: $MAX_FD_LIMIT"
    fi
fi

# For Darwin, add options to specify how the application appears in the dock
if $darwin; then
    GRADLE_OPTS="$GRADLE_OPTS \"-Xdock:name=$APP_NAME\" \"-Xdock:icon=$APP_HOME/media/gradle.icns\""
fi

# For Cygwin or MSYS, switch paths to Windows format before running java
if [ "$cygwin" = "true" -o "$msys" = "true" ] ; then
    APP_HOME=`cygpath --path --mixed "$APP_HOME"`
    CLASSPATH=`cygpath --path --mixed "$CLASSPATH"`

    JAVACMD=`cygpath --unix "$JAVACMD"`

    # We build the pattern for arguments to be converted via cygpath
    ROOTDIRSRAW=`find -L / -maxdepth 1 -mindepth 1 -type d 2>/dev/null`
    SEP=""
    for dir in $ROOTDIRSRAW ; do
        ROOTDIRS="$ROOTDIRS$SEP$dir"
        SEP="|"
    done
    OURCYGPATTERN="(^($ROOTDIRS))"
    # Add a user-defined pattern to the cygpath arguments
    if [ "$GRADLE_CYGPATTERN" != "" ] ; then
        OURCYGPATTERN="$OURCYGPATTERN|($GRADLE_CYGPATTERN)"
    fi
    # Now convert the arguments - kludge to limit ourselves to /bin/sh
    i=0
    for arg in "$@" ; do
        CHECK=`echo "$arg"|egrep -c "$OURCYGPATTERN" -`
        CHECK2=`echo "$arg"|egrep -c "^-"`                                 ### Determine if an option

        if [ $CHECK -ne 0 ] && [ $CHECK2 -eq 0 ] ; then                    ### Added a condition
            eval `echo args$i`=`cygpath --path --ignore --mixed "$arg"`
        else
            eval `echo args$i`="\"$arg\""
        fi
        i=`expr $i + 1`
    done
    case $i in
        0) set -- ;;
        1) set -- "$args0" ;;
        2) set -- "$args0" "$args1" ;;
        3) set -- "$args0" "$args1" "$args2" ;;
        4) set -- "$args0" "$args1" "$args2" "$args3" ;;
        5) set -- "$args0" "$args1" "$args2" "$args3" "$args4" ;;
        6) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" ;;
        7) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" ;;
        8) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" "$args7" ;;
        9) set -- "$args0" "$args1" "$args2" "$args3" "$args4" "$args5" "$args6" "$args7" "$args8" ;;
    esac
fi

# Escape application args
save () {
    for i do printf %s\\n "$i" | sed "s/'/'\\\\''/g;1s/^/'/;\$s/\$/' \\\\/" ; done
    echo " "
}
APP_ARGS=`save "$@"`

# Collect all arguments for the java command, following the shell quoting and substitution rules
eval set -- $DEFAULT_JVM_OPTS $JAVA_OPTS $GRADLE_OPTS "\"-Dorg.gradle.appname=$APP_BASE_NAME\"" -classpath "\"$CLASSPATH\"" org.gradle.wrapper.GradleWrapperMain "$APP_ARGS"

exec "$JAVACMD" "$@"

--#

--% /springbooter/src/test/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/FulgentApplicationTests.java
package __TEMPLATE_PACKAGENAME_FULLBYDOT__;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class FulgentApplicationTests {

  @Test
  void contextLoads() {
  }

}

--#

--% /springbooter/src/main/resources/application.yml
server:
  port: __TEMPLATE_SERVER_PORT__

spring:
  datasource:
    # url: jdbc:sqlite:__TEMPLATE_DBNAME.db?date_string_format=yyyy-MM-dd HH:mm:ss
    # url: jdbc:sqlite:__TEMPLATE_DBNAME.db    
    # driver-class-name: org.sqlite.JDBC
    url: jdbc:postgresql://__TEMPLATE_DBHOST:__TEMPLATE_DBPORT/__TEMPLATE_DBNAME
    username: __TEMPLATE_DBUSER
    password: __TEMPLATE_DBPASS
    testWhileIdle: true
    validationQuery: SELECT 1
    initialization-mode: always
    # initialize: true

  jpa:
    properties:
      hibernate:
        dialect: org.hibernate.dialect.PostgreSQLDialect
        # hbm2ddl.auto: validate
        # dialect: org.hibernate.dialect.SQLiteDialect
    # hibernate:
      # ddl-auto: create-drop
      # ddl-auto: update

    show-sql: true
    # database-platform: com.sakr.sqlite.config.SQLDialect

mybatis:
  config-location: classpath:mybatis-config.xml

  logging:
    level:
      root: WARN
      __TEMPLATE_PACKAGENAME_FULLBYDOT__.db.mapper: TRACE

--#

--% /springbooter/src/main/resources/data.sql
select 1;
--#

--% /springbooter/src/main/resources/schema.sql
-- create table attendee (
--   id serial primary key,
--   name varchar(100)
-- );
select 1;
--#

--% /springbooter/src/main/resources/mybatis-config.xml
<?xml version="1.0" encoding="UTF-8" ?>

<!DOCTYPE configuration
  PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-config.dtd">

<configuration>

  <typeAliases>
    
    <typeAlias alias="attendee" type="__TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.Attendee" />
__TEMPLATE_APP_XML_TYPEALIASES__
  </typeAliases>

  <mappers>
    <mapper resource="mapper/AttendeeMapper.xml"/>
__TEMPLATE_APP_XML_MAPPERS__
  </mappers>

</configuration>

--#

--% /springbooter/src/main/resources/mapper/AttendeeMapper.xml
<?xml version="1.0" encoding="UTF-8" ?>

<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-mapper.dtd">

<mapper namespace="__TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.AttendeeMapper">

  <select id="selectAttendeeById" resultType="Attendee">
    select * from attendee where id = #{id}
  </select>

  <select id="findAll" resultMap="attendeeResultMap">
    select * from attendee
  </select>

  <resultMap id="attendeeResultMap" type="__TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.Attendee">
    <result property="id" column="id" />
    <result property="name" column="name" />
    <!-- <result property="state" column="state" />
    <result property="country" column="country" /> -->
  </resultMap>

  <insert id="insert">
    insert into attendee(
      name
      <!-- , state, country -->
    )
    values(
      #{attendee.name}
      <!-- ,
      #{attendee.state},
      #{attendee.country} -->
    )
  </insert>

  <update id="updateAttendee">
    update attendee
      <set>
        <if test="attendee.name != null">name=#{attendee.name},</if>
        <!-- <if test="attendee.state != null">state=#{attendee.state},</if>
        <if test="attendee.country != null">country=#{attendee.country},</if> -->
      </set>
    where id=#{id}
  </update>


</mapper>

--#

--% /springbooter/src/main/resources/graphql/schema.gql
type Attendee {
 id: ID!
 name: String!
}

__TEMPLATE_APP_TYPEDEFS__

type Query {
  allAttendees: [Attendee]
  findAttendeeById(id: ID): Attendee
  findAttendeeByName(name: String): [Attendee]
__TEMPLATE_APP_QUERYTYPES__
}

input AttendeeInput {
  id: ID
  name: String
}

__TEMPLATE_APP_INPUTTYPES__

type Mutation {
  createAttendee(attendee: AttendeeInput): Attendee
  deleteAttendee(id: ID): String
  updateAttendee(id: ID, attendee: AttendeeInput): Attendee
__TEMPLATE_APP_MUTATIONTYPES__
}

schema {
  query: Query
  mutation: Mutation
}
--#

--% /springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/ServletInitializer.java
package __TEMPLATE_PACKAGENAME_FULLBYDOT__;

import org.springframework.boot.builder.SpringApplicationBuilder;
import org.springframework.boot.web.servlet.support.SpringBootServletInitializer;

public class ServletInitializer extends SpringBootServletInitializer {

  @Override
  protected SpringApplicationBuilder configure(SpringApplicationBuilder application) {
    return application.sources(FulgentApplication.class);
  }

}

--#

--% /springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/FulgentApplication.java
package __TEMPLATE_PACKAGENAME_FULLBYDOT__;

import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.AttendeeService;
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.AttendeeRepository;
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.AttendeeQuery;
import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.AttendeeMutation;
__TEMPLATE_ROOTAPP_IMPORTS__

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import com.coxautodev.graphql.tools.SchemaParser;

import graphql.schema.GraphQLSchema;
import graphql.servlet.SimpleGraphQLHttpServlet;

import org.springframework.boot.web.servlet.ServletRegistrationBean;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;


@SpringBootApplication
public class FulgentApplication {

  public static void main(String[] args) {
    SpringApplication.run(FulgentApplication.class, args);
  }

  @Autowired
  private AttendeeService attendeeService;

__TEMPLATE_ROOTAPP_AUTOWIRED__

  @Bean
  public ServletRegistrationBean<SimpleGraphQLHttpServlet> graphQLServlet() {
    return new ServletRegistrationBean<SimpleGraphQLHttpServlet>(
      SimpleGraphQLHttpServlet
      .newBuilder(
        buildSchema(
          attendeeService__TEMPLATE_ROOTAPP_SERVICEPARAMS__
        )
      )
      .build(),
      "/graphql"
    );
  }

  private static GraphQLSchema buildSchema(
    AttendeeService attendeeService__TEMPLATE_ROOTAPP_BUILDSCHEMAPARAMS__
  ) {
    return SchemaParser
    .newParser()
    .file("graphql/schema.gql")
    .resolvers( 
      new AttendeeQuery(attendeeService),
      new AttendeeMutation(attendeeService)__TEMPLATE_ROOTAPP_RESOLVERPARAMS__
    )
    .build()
    .makeExecutableSchema();
  }

}

--#

--% /springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/BaseController.java
package __TEMPLATE_PACKAGENAME_FULLBYDOT__;
// ResponseBean.java
// =================
import lombok.extern.slf4j.Slf4j;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
class ResponseBean<T> {
  private String msg;
  private Integer code;
  private T data;
}

// BaseController.java
// ===================


@Slf4j
@RestController
public class BaseController {

  @GetMapping("/")
  public ResponseBean index() {
    log.info("Alive!");
    return new ResponseBean("Alive", 200, "Fulgent Server");
  }
  
}
--#

--% /springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/Attendee.java
package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee;

// import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import lombok.Data;

import javax.persistence.Entity;
import javax.persistence.Table;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;


@Entity
@Data
@Table(name = "attendee")
public class Attendee {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  private String name;

}

--#

--% /springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeController.java
package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee;

import java.util.List;

import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import lombok.Getter;
import lombok.Setter;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.PathVariable;


@AllArgsConstructor
@RestController
@RequestMapping("/attendee")
public class AttendeeController {

  private AttendeeMapper attendeeMapper;

  // http://localhost:__TEMPLATE_SERVER_PORT__/attendee
  @GetMapping(produces = {MediaType.APPLICATION_JSON_VALUE})
  public List<Attendee> getAll() {
    return attendeeMapper.findAll();
  }

  // http://localhost:__TEMPLATE_SERVER_PORT__/attendee/3
  // @GetMapping(path="{id}", produces = {MediaType.APPLICATION_JSON_VALUE})
  @GetMapping("{id}")
  public Attendee getById(@PathVariable("id") long id) {
    return attendeeMapper.findById(id);
  }

  // http://localhost:__TEMPLATE_SERVER_PORT__/attendee/name/gaia
  @GetMapping("/name/{name}")
  public Attendee getById(@PathVariable("name") String name) {
    return attendeeMapper.findByName(name);
  }

  @PostMapping
  public List<Attendee> createAttendee(
    @RequestBody
    Attendee attendee
  ) {
    attendeeMapper.insert(attendee);
    return attendeeMapper.findAll();
  }

  @PutMapping("{id}")
  public Attendee delete(
    @PathVariable("id") long id,
    @RequestBody Attendee attendee
  ) {
    attendeeMapper.updateAttendee(id, attendee);
    return attendeeMapper.findById(id);
  }

  @DeleteMapping("{id}")
  public List<Attendee> delete(@PathVariable("id") long id) {
    attendeeMapper.delete(id);
    return attendeeMapper.findAll();
  }

}

--#

--% /springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeInput.java
package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee;

import lombok.Data;

@Data
public class AttendeeInput {

  private Long id;
  private String name;

}

--#

--% /springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeRepository.java
package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee;

import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

import org.springframework.data.jpa.repository.Query;

// https://stackoverflow.com/questions/33153271/how-do-you-create-a-spring-jpa-repository-findby-query-using-a-property-that-con
// Query
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
// import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;

@Repository
public interface AttendeeRepository extends JpaRepository<Attendee, Long> {

  // @Select("select id, name from attendee where id = #{id}")
  // Attendee findById(@Param("id") Long id);

  // https://stackoverflow.com/questions/25362540/like-query-in-spring-jparepository
  // https://stackoverflow.com/questions/7491291/how-can-i-use-like-in-sql-queries-with-mybatis-safely-and-db-agnostic

  // @Query("select id, name from attendee where name like %?1%")
  // @Query("select id, name from attendee where name like %:name%")

  // Select gak bisa pake like spt Query
  // concat('%',concat(#{name}, '%'))
  // @Select("select id, name from attendee where name like #{name}")
  // @Select("select id, name from attendee where name like concat('%',concat(#{name}, '%'))")
  // @Select("select id, name from attendee where name like '%' || #{name} || '%'")
  // List<Attendee> findByName(@Param("name") String name);

  List<Attendee> findByNameIgnoreCaseContaining(@Param("name") String name);

}

--#

--% /springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeService.java
package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;


@Service
public class AttendeeService {

  @Autowired
  private AttendeeRepository attendeeRepository;

  public List<Attendee> findAll() {
    return attendeeRepository.findAll();
  }

  public Attendee findById(Long id) {
    return attendeeRepository.findById(id).orElse(null);
  }

  public List<Attendee> findByName(String name) {
    // return attendeeRepository.findByName(name);
    return attendeeRepository.findByNameIgnoreCaseContaining(name);
  }

  public Attendee save(Attendee attendee) {
    return attendeeRepository.save(attendee);
  }

  public void delete(Long id) {
    attendeeRepository.deleteById(id);
  }

}

--#

--% /springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeQuery.java
package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee;

// import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.Attendee;
// import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.AttendeeService;

import com.coxautodev.graphql.tools.GraphQLQueryResolver;

import java.util.List;

import lombok.RequiredArgsConstructor;


@RequiredArgsConstructor
public class AttendeeQuery implements GraphQLQueryResolver {

  //private final AttendeeService attendeeService;
  private AttendeeService attendeeService;
  
  //public AttendeeQuery(AttendeeService attendeeService) {
  //  this.attendeeService = attendeeService;
  //}

  public List<Attendee> findAttendeeByName(String name) {
    return attendeeService.findByName(name);
  }

  public Attendee findAttendeeById(Long id) {
    return attendeeService.findById(id);
  }

  public List<Attendee> allAttendees() {
    return attendeeService.findAll();
  }

}

--#

--% /springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeMapper.java
package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee;

import java.util.List;

import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;
// import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Update;
import org.apache.ibatis.annotations.Delete;

import org.springframework.stereotype.Repository;


@Mapper
@Repository
public interface AttendeeMapper {

  @Select("select * from attendee where name = #{name}")
  Attendee findByName(@Param("name") String name);

  @Select("select * from attendee where id = #{id}")
  Attendee findById(@Param("id") long id);
  
  List<Attendee> findAll();

  void insert(@Param("attendee") Attendee attendee);

  // @Update("update attendee set name=#{attendee.name},state=#{attendee.state},country=#{attendee.country} where id=#{id}")
  void updateAttendee(@Param("id") long id, Attendee attendee);

  @Delete("delete from attendee where id=#{id}")
  void delete(@Param("id") long id);

}

--#

--% /springbooter/src/main/java/__TEMPLATE_PACKAGENAME_FULLBYSLASH__/apps/attendee/AttendeeMutation.java
package __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee;

// import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.Attendee;
// import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.AttendeeInput;
// import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.AttendeeService;
// import __TEMPLATE_PACKAGENAME_FULLBYDOT__.apps.attendee.AttendeeRepository;

import com.coxautodev.graphql.tools.GraphQLMutationResolver;

import java.util.List;
import java.util.Optional;

import lombok.RequiredArgsConstructor;


@RequiredArgsConstructor
public class AttendeeMutation implements GraphQLMutationResolver {

  private AttendeeService attendeeService;
  // private final AttendeeRepository attendeeRepository;
  
  //public AttendeeMutation(AttendeeService attendeeService) {
  //  this.attendeeService = attendeeService;
  //}

  public Attendee createAttendee(AttendeeInput _attendee) {
    Attendee attendee = new Attendee();
    attendee.setName(_attendee.getName());
    return attendeeService.save(attendee);
  }

  public String deleteAttendee(Long id) {
    attendeeService.delete(id);
    return "Attendee deleted";
  }

  public Attendee updateAttendee(Long id, AttendeeInput _attendee) {
    // Attendee attendee = attendeeRepository.findById(id).orElse(null);
    Attendee attendee = attendeeService.findById(id);
    attendee.setName(_attendee.getName());
    // attendeeRepository.save(attendee);
    attendeeService.save(attendee);    
    return attendee;
  }

}

--#

--% /springbooter/gradle/wrapper/gradle-wrapper.properties
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-7.0.2-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists

--#
