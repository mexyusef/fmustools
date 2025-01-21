--% index/fmus
quarkus,d(/mk)
	%utama=__FILE__
	.dockerignore,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/.dockerignore)
	.gitignore,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/.gitignore)
	comp.sh,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/comp.sh)
	docker-compose.yml,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/docker-compose.yml)
	mvnw,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/mvnw)
	mvnw.cmd,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/mvnw.cmd)
	pom.xml,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/pom.xml)
	README.md,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/README.md)
	run.sh,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/run.sh)
	work.fmus,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/work.fmus)
	.mvn,d(/mk)
		wrapper,d(/mk)
			maven-wrapper.jar,f(b64=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/.mvn/wrapper/maven-wrapper.jar)
			maven-wrapper.properties,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/.mvn/wrapper/maven-wrapper.properties)
			MavenWrapperDownloader.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/.mvn/wrapper/MavenWrapperDownloader.java)
	src,d(/mk)
		main,d(/mk)
			docker,d(/mk)
				Dockerfile.jvm,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/docker/Dockerfile.jvm)
				Dockerfile.legacy-jar,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/docker/Dockerfile.legacy-jar)
				Dockerfile.native,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/docker/Dockerfile.native)
				Dockerfile.native-distroless,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/docker/Dockerfile.native-distroless)
			java,d(/mk)
				apps,d(/mk)
					comment,d(/mk)
						Comment.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/java/apps/comment/Comment.java)
						ReactiveCommentResource.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/java/apps/comment/ReactiveCommentResource.java)
						UpdateComment.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/java/apps/comment/UpdateComment.java)
					post,d(/mk)
						Post.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/java/apps/post/Post.java)
						ReactivePostResource.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/java/apps/post/ReactivePostResource.java)
						UpdatePost.java,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/java/apps/post/UpdatePost.java)
				main,d(/mk)
			resources,d(/mk)
				application.properties,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/resources/application.properties)
				META-INF,d(/mk)
					resources,d(/mk)
						index.html,f(e=utama=C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/resources/META-INF/resources/index.html)
--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/.dockerignore
*
!target/*-runner
!target/*-runner.jar
!target/lib/*
!target/quarkus-app/*
--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/.gitignore
#Maven
target/
pom.xml.tag
pom.xml.releaseBackup
pom.xml.versionsBackup
release.properties

# Eclipse
.project
.classpath
.settings/
bin/

# IntelliJ
.idea
*.ipr
*.iml
*.iws

# NetBeans
nb-configuration.xml

# Visual Studio Code
.vscode
.factorypath

# OSX
.DS_Store

# Vim
*.swp
*.swo

# patch
*.orig
*.rej

# Local environment
.env

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/comp.sh
./mvnw compile

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/docker-compose.yml
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

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/mvnw
#!/bin/sh
# ----------------------------------------------------------------------------
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# Maven Start Up Batch script
#
# Required ENV vars:
# ------------------
#   JAVA_HOME - location of a JDK home dir
#
# Optional ENV vars
# -----------------
#   M2_HOME - location of maven2's installed home dir
#   MAVEN_OPTS - parameters passed to the Java VM when running Maven
#     e.g. to debug Maven itself, use
#       set MAVEN_OPTS=-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=y,address=8000
#   MAVEN_SKIP_RC - flag to disable loading of mavenrc files
# ----------------------------------------------------------------------------

if [ -z "$MAVEN_SKIP_RC" ] ; then

  if [ -f /etc/mavenrc ] ; then
    . /etc/mavenrc
  fi

  if [ -f "$HOME/.mavenrc" ] ; then
    . "$HOME/.mavenrc"
  fi

fi

# OS specific support.  $var _must_ be set to either true or false.
cygwin=false;
darwin=false;
mingw=false
case "`uname`" in
  CYGWIN*) cygwin=true ;;
  MINGW*) mingw=true;;
  Darwin*) darwin=true
    # Use /usr/libexec/java_home if available, otherwise fall back to /Library/Java/Home
    # See https://developer.apple.com/library/mac/qa/qa1170/_index.html
    if [ -z "$JAVA_HOME" ]; then
      if [ -x "/usr/libexec/java_home" ]; then
        export JAVA_HOME="`/usr/libexec/java_home`"
      else
        export JAVA_HOME="/Library/Java/Home"
      fi
    fi
    ;;
esac

if [ -z "$JAVA_HOME" ] ; then
  if [ -r /etc/gentoo-release ] ; then
    JAVA_HOME=`java-config --jre-home`
  fi
fi

if [ -z "$M2_HOME" ] ; then
  ## resolve links - $0 may be a link to maven's home
  PRG="$0"

  # need this for relative symlinks
  while [ -h "$PRG" ] ; do
    ls=`ls -ld "$PRG"`
    link=`expr "$ls" : '.*-> \(.*\)$'`
    if expr "$link" : '/.*' > /dev/null; then
      PRG="$link"
    else
      PRG="`dirname "$PRG"`/$link"
    fi
  done

  saveddir=`pwd`

  M2_HOME=`dirname "$PRG"`/..

  # make it fully qualified
  M2_HOME=`cd "$M2_HOME" && pwd`

  cd "$saveddir"
  # echo Using m2 at $M2_HOME
fi

# For Cygwin, ensure paths are in UNIX format before anything is touched
if $cygwin ; then
  [ -n "$M2_HOME" ] &&
    M2_HOME=`cygpath --unix "$M2_HOME"`
  [ -n "$JAVA_HOME" ] &&
    JAVA_HOME=`cygpath --unix "$JAVA_HOME"`
  [ -n "$CLASSPATH" ] &&
    CLASSPATH=`cygpath --path --unix "$CLASSPATH"`
fi

# For Mingw, ensure paths are in UNIX format before anything is touched
if $mingw ; then
  [ -n "$M2_HOME" ] &&
    M2_HOME="`(cd "$M2_HOME"; pwd)`"
  [ -n "$JAVA_HOME" ] &&
    JAVA_HOME="`(cd "$JAVA_HOME"; pwd)`"
fi

if [ -z "$JAVA_HOME" ]; then
  javaExecutable="`which javac`"
  if [ -n "$javaExecutable" ] && ! [ "`expr \"$javaExecutable\" : '\([^ ]*\)'`" = "no" ]; then
    # readlink(1) is not available as standard on Solaris 10.
    readLink=`which readlink`
    if [ ! `expr "$readLink" : '\([^ ]*\)'` = "no" ]; then
      if $darwin ; then
        javaHome="`dirname \"$javaExecutable\"`"
        javaExecutable="`cd \"$javaHome\" && pwd -P`/javac"
      else
        javaExecutable="`readlink -f \"$javaExecutable\"`"
      fi
      javaHome="`dirname \"$javaExecutable\"`"
      javaHome=`expr "$javaHome" : '\(.*\)/bin'`
      JAVA_HOME="$javaHome"
      export JAVA_HOME
    fi
  fi
fi

if [ -z "$JAVACMD" ] ; then
  if [ -n "$JAVA_HOME"  ] ; then
    if [ -x "$JAVA_HOME/jre/sh/java" ] ; then
      # IBM's JDK on AIX uses strange locations for the executables
      JAVACMD="$JAVA_HOME/jre/sh/java"
    else
      JAVACMD="$JAVA_HOME/bin/java"
    fi
  else
    JAVACMD="`which java`"
  fi
fi

if [ ! -x "$JAVACMD" ] ; then
  echo "Error: JAVA_HOME is not defined correctly." >&2
  echo "  We cannot execute $JAVACMD" >&2
  exit 1
fi

if [ -z "$JAVA_HOME" ] ; then
  echo "Warning: JAVA_HOME environment variable is not set."
fi

CLASSWORLDS_LAUNCHER=org.codehaus.plexus.classworlds.launcher.Launcher

# traverses directory structure from process work directory to filesystem root
# first directory with .mvn subdirectory is considered project base directory
find_maven_basedir() {

  if [ -z "$1" ]
  then
    echo "Path not specified to find_maven_basedir"
    return 1
  fi

  basedir="$1"
  wdir="$1"
  while [ "$wdir" != '/' ] ; do
    if [ -d "$wdir"/.mvn ] ; then
      basedir=$wdir
      break
    fi
    # workaround for JBEAP-8937 (on Solaris 10/Sparc)
    if [ -d "${wdir}" ]; then
      wdir=`cd "$wdir/.."; pwd`
    fi
    # end of workaround
  done
  echo "${basedir}"
}

# concatenates all lines of a file
concat_lines() {
  if [ -f "$1" ]; then
    echo "$(tr -s '\n' ' ' < "$1")"
  fi
}

BASE_DIR=`find_maven_basedir "$(pwd)"`
if [ -z "$BASE_DIR" ]; then
  exit 1;
fi

##########################################################################################
# Extension to allow automatically downloading the maven-wrapper.jar from Maven-central
# This allows using the maven wrapper in projects that prohibit checking in binary data.
##########################################################################################
if [ -r "$BASE_DIR/.mvn/wrapper/maven-wrapper.jar" ]; then
    if [ "$MVNW_VERBOSE" = true ]; then
      echo "Found .mvn/wrapper/maven-wrapper.jar"
    fi
else
    if [ "$MVNW_VERBOSE" = true ]; then
      echo "Couldn't find .mvn/wrapper/maven-wrapper.jar, downloading it ..."
    fi
    if [ -n "$MVNW_REPOURL" ]; then
      jarUrl="$MVNW_REPOURL/io/takari/maven-wrapper/0.5.6/maven-wrapper-0.5.6.jar"
    else
      jarUrl="https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.5.6/maven-wrapper-0.5.6.jar"
    fi
    while IFS="=" read key value; do
      case "$key" in (wrapperUrl) jarUrl="$value"; break ;;
      esac
    done < "$BASE_DIR/.mvn/wrapper/maven-wrapper.properties"
    if [ "$MVNW_VERBOSE" = true ]; then
      echo "Downloading from: $jarUrl"
    fi
    wrapperJarPath="$BASE_DIR/.mvn/wrapper/maven-wrapper.jar"
    if $cygwin; then
      wrapperJarPath=`cygpath --path --windows "$wrapperJarPath"`
    fi

    if command -v wget > /dev/null; then
        if [ "$MVNW_VERBOSE" = true ]; then
          echo "Found wget ... using wget"
        fi
        if [ -z "$MVNW_USERNAME" ] || [ -z "$MVNW_PASSWORD" ]; then
            wget "$jarUrl" -O "$wrapperJarPath"
        else
            wget --http-user=$MVNW_USERNAME --http-password=$MVNW_PASSWORD "$jarUrl" -O "$wrapperJarPath"
        fi
    elif command -v curl > /dev/null; then
        if [ "$MVNW_VERBOSE" = true ]; then
          echo "Found curl ... using curl"
        fi
        if [ -z "$MVNW_USERNAME" ] || [ -z "$MVNW_PASSWORD" ]; then
            curl -o "$wrapperJarPath" "$jarUrl" -f
        else
            curl --user $MVNW_USERNAME:$MVNW_PASSWORD -o "$wrapperJarPath" "$jarUrl" -f
        fi

    else
        if [ "$MVNW_VERBOSE" = true ]; then
          echo "Falling back to using Java to download"
        fi
        javaClass="$BASE_DIR/.mvn/wrapper/MavenWrapperDownloader.java"
        # For Cygwin, switch paths to Windows format before running javac
        if $cygwin; then
          javaClass=`cygpath --path --windows "$javaClass"`
        fi
        if [ -e "$javaClass" ]; then
            if [ ! -e "$BASE_DIR/.mvn/wrapper/MavenWrapperDownloader.class" ]; then
                if [ "$MVNW_VERBOSE" = true ]; then
                  echo " - Compiling MavenWrapperDownloader.java ..."
                fi
                # Compiling the Java class
                ("$JAVA_HOME/bin/javac" "$javaClass")
            fi
            if [ -e "$BASE_DIR/.mvn/wrapper/MavenWrapperDownloader.class" ]; then
                # Running the downloader
                if [ "$MVNW_VERBOSE" = true ]; then
                  echo " - Running MavenWrapperDownloader.java ..."
                fi
                ("$JAVA_HOME/bin/java" -cp .mvn/wrapper MavenWrapperDownloader "$MAVEN_PROJECTBASEDIR")
            fi
        fi
    fi
fi
##########################################################################################
# End of extension
##########################################################################################

export MAVEN_PROJECTBASEDIR=${MAVEN_BASEDIR:-"$BASE_DIR"}
if [ "$MVNW_VERBOSE" = true ]; then
  echo $MAVEN_PROJECTBASEDIR
fi
MAVEN_OPTS="$(concat_lines "$MAVEN_PROJECTBASEDIR/.mvn/jvm.config") $MAVEN_OPTS"

# For Cygwin, switch paths to Windows format before running java
if $cygwin; then
  [ -n "$M2_HOME" ] &&
    M2_HOME=`cygpath --path --windows "$M2_HOME"`
  [ -n "$JAVA_HOME" ] &&
    JAVA_HOME=`cygpath --path --windows "$JAVA_HOME"`
  [ -n "$CLASSPATH" ] &&
    CLASSPATH=`cygpath --path --windows "$CLASSPATH"`
  [ -n "$MAVEN_PROJECTBASEDIR" ] &&
    MAVEN_PROJECTBASEDIR=`cygpath --path --windows "$MAVEN_PROJECTBASEDIR"`
fi

# Provide a "standardized" way to retrieve the CLI args that will
# work with both Windows and non-Windows executions.
MAVEN_CMD_LINE_ARGS="$MAVEN_CONFIG $@"
export MAVEN_CMD_LINE_ARGS

WRAPPER_LAUNCHER=org.apache.maven.wrapper.MavenWrapperMain

exec "$JAVACMD" \
  $MAVEN_OPTS \
  -classpath "$MAVEN_PROJECTBASEDIR/.mvn/wrapper/maven-wrapper.jar" \
  "-Dmaven.home=${M2_HOME}" "-Dmaven.multiModuleProjectDirectory=${MAVEN_PROJECTBASEDIR}" \
  ${WRAPPER_LAUNCHER} $MAVEN_CONFIG "$@"

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/mvnw.cmd
@REM ----------------------------------------------------------------------------
@REM Licensed to the Apache Software Foundation (ASF) under one
@REM or more contributor license agreements.  See the NOTICE file
@REM distributed with this work for additional information
@REM regarding copyright ownership.  The ASF licenses this file
@REM to you under the Apache License, Version 2.0 (the
@REM "License"); you may not use this file except in compliance
@REM with the License.  You may obtain a copy of the License at
@REM
@REM    https://www.apache.org/licenses/LICENSE-2.0
@REM
@REM Unless required by applicable law or agreed to in writing,
@REM software distributed under the License is distributed on an
@REM "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
@REM KIND, either express or implied.  See the License for the
@REM specific language governing permissions and limitations
@REM under the License.
@REM ----------------------------------------------------------------------------

@REM ----------------------------------------------------------------------------
@REM Maven Start Up Batch script
@REM
@REM Required ENV vars:
@REM JAVA_HOME - location of a JDK home dir
@REM
@REM Optional ENV vars
@REM M2_HOME - location of maven2's installed home dir
@REM MAVEN_BATCH_ECHO - set to 'on' to enable the echoing of the batch commands
@REM MAVEN_BATCH_PAUSE - set to 'on' to wait for a keystroke before ending
@REM MAVEN_OPTS - parameters passed to the Java VM when running Maven
@REM     e.g. to debug Maven itself, use
@REM set MAVEN_OPTS=-Xdebug -Xrunjdwp:transport=dt_socket,server=y,suspend=y,address=8000
@REM MAVEN_SKIP_RC - flag to disable loading of mavenrc files
@REM ----------------------------------------------------------------------------

@REM Begin all REM lines with '@' in case MAVEN_BATCH_ECHO is 'on'
@echo off
@REM set title of command window
title %0
@REM enable echoing by setting MAVEN_BATCH_ECHO to 'on'
@if "%MAVEN_BATCH_ECHO%" == "on"  echo %MAVEN_BATCH_ECHO%

@REM set %HOME% to equivalent of $HOME
if "%HOME%" == "" (set "HOME=%HOMEDRIVE%%HOMEPATH%")

@REM Execute a user defined script before this one
if not "%MAVEN_SKIP_RC%" == "" goto skipRcPre
@REM check for pre script, once with legacy .bat ending and once with .cmd ending
if exist "%HOME%\mavenrc_pre.bat" call "%HOME%\mavenrc_pre.bat"
if exist "%HOME%\mavenrc_pre.cmd" call "%HOME%\mavenrc_pre.cmd"
:skipRcPre

@setlocal

set ERROR_CODE=0

@REM To isolate internal variables from possible post scripts, we use another setlocal
@setlocal

@REM ==== START VALIDATION ====
if not "%JAVA_HOME%" == "" goto OkJHome

echo.
echo Error: JAVA_HOME not found in your environment. >&2
echo Please set the JAVA_HOME variable in your environment to match the >&2
echo location of your Java installation. >&2
echo.
goto error

:OkJHome
if exist "%JAVA_HOME%\bin\java.exe" goto init

echo.
echo Error: JAVA_HOME is set to an invalid directory. >&2
echo JAVA_HOME = "%JAVA_HOME%" >&2
echo Please set the JAVA_HOME variable in your environment to match the >&2
echo location of your Java installation. >&2
echo.
goto error

@REM ==== END VALIDATION ====

:init

@REM Find the project base dir, i.e. the directory that contains the folder ".mvn".
@REM Fallback to current working directory if not found.

set MAVEN_PROJECTBASEDIR=%MAVEN_BASEDIR%
IF NOT "%MAVEN_PROJECTBASEDIR%"=="" goto endDetectBaseDir

set EXEC_DIR=%CD%
set WDIR=%EXEC_DIR%
:findBaseDir
IF EXIST "%WDIR%"\.mvn goto baseDirFound
cd ..
IF "%WDIR%"=="%CD%" goto baseDirNotFound
set WDIR=%CD%
goto findBaseDir

:baseDirFound
set MAVEN_PROJECTBASEDIR=%WDIR%
cd "%EXEC_DIR%"
goto endDetectBaseDir

:baseDirNotFound
set MAVEN_PROJECTBASEDIR=%EXEC_DIR%
cd "%EXEC_DIR%"

:endDetectBaseDir

IF NOT EXIST "%MAVEN_PROJECTBASEDIR%\.mvn\jvm.config" goto endReadAdditionalConfig

@setlocal EnableExtensions EnableDelayedExpansion
for /F "usebackq delims=" %%a in ("%MAVEN_PROJECTBASEDIR%\.mvn\jvm.config") do set JVM_CONFIG_MAVEN_PROPS=!JVM_CONFIG_MAVEN_PROPS! %%a
@endlocal & set JVM_CONFIG_MAVEN_PROPS=%JVM_CONFIG_MAVEN_PROPS%

:endReadAdditionalConfig

SET MAVEN_JAVA_EXE="%JAVA_HOME%\bin\java.exe"
set WRAPPER_JAR="%MAVEN_PROJECTBASEDIR%\.mvn\wrapper\maven-wrapper.jar"
set WRAPPER_LAUNCHER=org.apache.maven.wrapper.MavenWrapperMain

set DOWNLOAD_URL="https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.5.6/maven-wrapper-0.5.6.jar"

FOR /F "tokens=1,2 delims==" %%A IN ("%MAVEN_PROJECTBASEDIR%\.mvn\wrapper\maven-wrapper.properties") DO (
    IF "%%A"=="wrapperUrl" SET DOWNLOAD_URL=%%B
)

@REM Extension to allow automatically downloading the maven-wrapper.jar from Maven-central
@REM This allows using the maven wrapper in projects that prohibit checking in binary data.
if exist %WRAPPER_JAR% (
    if "%MVNW_VERBOSE%" == "true" (
        echo Found %WRAPPER_JAR%
    )
) else (
    if not "%MVNW_REPOURL%" == "" (
        SET DOWNLOAD_URL="%MVNW_REPOURL%/io/takari/maven-wrapper/0.5.6/maven-wrapper-0.5.6.jar"
    )
    if "%MVNW_VERBOSE%" == "true" (
        echo Couldn't find %WRAPPER_JAR%, downloading it ...
        echo Downloading from: %DOWNLOAD_URL%
    )

    powershell -Command "&{"^
		"$webclient = new-object System.Net.WebClient;"^
		"if (-not ([string]::IsNullOrEmpty('%MVNW_USERNAME%') -and [string]::IsNullOrEmpty('%MVNW_PASSWORD%'))) {"^
		"$webclient.Credentials = new-object System.Net.NetworkCredential('%MVNW_USERNAME%', '%MVNW_PASSWORD%');"^
		"}"^
		"[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12; $webclient.DownloadFile('%DOWNLOAD_URL%', '%WRAPPER_JAR%')"^
		"}"
    if "%MVNW_VERBOSE%" == "true" (
        echo Finished downloading %WRAPPER_JAR%
    )
)
@REM End of extension

@REM Provide a "standardized" way to retrieve the CLI args that will
@REM work with both Windows and non-Windows executions.
set MAVEN_CMD_LINE_ARGS=%*

%MAVEN_JAVA_EXE% %JVM_CONFIG_MAVEN_PROPS% %MAVEN_OPTS% %MAVEN_DEBUG_OPTS% -classpath %WRAPPER_JAR% "-Dmaven.multiModuleProjectDirectory=%MAVEN_PROJECTBASEDIR%" %WRAPPER_LAUNCHER% %MAVEN_CONFIG% %*
if ERRORLEVEL 1 goto error
goto end

:error
set ERROR_CODE=1

:end
@endlocal & set ERROR_CODE=%ERROR_CODE%

if not "%MAVEN_SKIP_RC%" == "" goto skipRcPost
@REM check for post script, once with legacy .bat ending and once with .cmd ending
if exist "%HOME%\mavenrc_post.bat" call "%HOME%\mavenrc_post.bat"
if exist "%HOME%\mavenrc_post.cmd" call "%HOME%\mavenrc_post.cmd"
:skipRcPost

@REM pause the script if MAVEN_BATCH_PAUSE is set to 'on'
if "%MAVEN_BATCH_PAUSE%" == "on" pause

if "%MAVEN_TERMINATE_CMD%" == "on" exit %ERROR_CODE%

exit /B %ERROR_CODE%

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/pom.xml
<?xml version="1.0"?>
<project xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 https://maven.apache.org/xsd/maven-4.0.0.xsd"
         xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
    <modelVersion>4.0.0</modelVersion>
    <groupId>org.dvddhln</groupId>
    <artifactId>quarkus-crud-reactive-mongodb</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <properties>
        <compiler-plugin.version>3.8.1</compiler-plugin.version>
        <maven.compiler.parameters>true</maven.compiler.parameters>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
        <quarkus-plugin.version>2.0.0.Final</quarkus-plugin.version>
        <quarkus.platform.artifact-id>quarkus-bom</quarkus.platform.artifact-id>
        <quarkus.platform.group-id>io.quarkus</quarkus.platform.group-id>
        <quarkus.platform.version>2.0.0.Final</quarkus.platform.version>
        <surefire-plugin.version>3.0.0-M5</surefire-plugin.version>
    </properties>
    <dependencyManagement>
        <dependencies>
            <dependency>
                <groupId>${quarkus.platform.group-id}</groupId>
                <artifactId>${quarkus.platform.artifact-id}</artifactId>
                <version>${quarkus.platform.version}</version>
                <type>pom</type>
                <scope>import</scope>
            </dependency>
        </dependencies>
    </dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>io.quarkus</groupId>
            <artifactId>quarkus-mongodb-panache</artifactId>
        </dependency>
        <dependency>
            <groupId>io.quarkus</groupId>
            <artifactId>quarkus-resteasy-reactive-jsonb</artifactId>
        </dependency>
        <dependency>
            <groupId>io.quarkus</groupId>
            <artifactId>quarkus-junit5</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>io.quarkus</groupId>
            <artifactId>quarkus-panache-mock</artifactId>
            <scope>test</scope>
        </dependency>
        <dependency>
            <groupId>org.projectlombok</groupId>
            <artifactId>lombok</artifactId>
            <version>1.18.18</version>
        </dependency>
        <dependency>
            <groupId>io.rest-assured</groupId>
            <artifactId>rest-assured</artifactId>
            <scope>test</scope>
        </dependency>
    </dependencies>
    <build>
        <plugins>
            <plugin>
                <groupId>io.quarkus</groupId>
                <artifactId>quarkus-maven-plugin</artifactId>
                <version>${quarkus-plugin.version}</version>
                <extensions>true</extensions>
                <executions>
                    <execution>
                        <goals>
                            <goal>build</goal>
                            <goal>generate-code</goal>
                            <goal>generate-code-tests</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            <plugin>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>${compiler-plugin.version}</version>
                <configuration>
                    <parameters>${maven.compiler.parameters}</parameters>
                </configuration>
            </plugin>
            <plugin>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>${surefire-plugin.version}</version>
                <configuration>
                    <systemPropertyVariables>
                        <java.util.logging.manager>org.jboss.logmanager.LogManager</java.util.logging.manager>
                        <maven.home>${maven.home}</maven.home>
                    </systemPropertyVariables>
                </configuration>
            </plugin>
        </plugins>
    </build>
    <profiles>
        <profile>
            <id>native</id>
            <activation>
                <property>
                    <name>native</name>
                </property>
            </activation>
            <build>
                <plugins>
                    <plugin>
                        <artifactId>maven-failsafe-plugin</artifactId>
                        <version>${surefire-plugin.version}</version>
                        <executions>
                            <execution>
                                <goals>
                                    <goal>integration-test</goal>
                                    <goal>verify</goal>
                                </goals>
                                <configuration>
                                    <systemPropertyVariables>
                                        <native.image.path>
                                            ${project.build.directory}/${project.build.finalName}-runner
                                        </native.image.path>
                                        <java.util.logging.manager>org.jboss.logmanager.LogManager
                                        </java.util.logging.manager>
                                        <maven.home>${maven.home}</maven.home>
                                    </systemPropertyVariables>
                                </configuration>
                            </execution>
                        </executions>
                    </plugin>
                </plugins>
            </build>
            <properties>
                <quarkus.package.type>native</quarkus.package.type>
            </properties>
        </profile>
    </profiles>
</project>

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/README.md
# quarkus-crud-reactive-mongodb project

This project uses Quarkus, the Supersonic Subatomic Java Framework.

This project demonstrates the usage of MongoDB with Panache on top with reactive endpoints by
 creating entities and managing relations between and their corresponding operations in a blog crud
like fashion.

This project is presented in the following article.

[Creating a Reactive CRUD blog app with MongoDB, Quarkus and Panache](https://dvddhln.medium.com/creating-a-reactive-crud-blog-app-with-mongodb-quarkus-and-panache-54d659cf8dcb)


## Run mongodb in Docker container

    docker run -ti --rm -p 27017:27017 mongo:4.0

## Running the application in dev mode

You can run your application in dev mode that enables live coding using:
```shell script
./mvnw compile quarkus:dev
```

### Example Response

    {
    "id": "60dc9301971c0d514f62792e",
    "author": "John Doe",
    "comments": [
        {
            "id": "60dc930f971c0d514f62792f",
            "content": "22323232",
            "creationDate": "2021-06-30T17:51:43.781"
        },
        {
            "id": "60dc9310971c0d514f627930",
            "content": "22323232",
            "creationDate": "2021-06-30T17:51:44.815"
        },
        {
            "id": "60dc9311971c0d514f627931",
            "content": "1337",
            "creationDate": "2021-06-30T17:51:45.659"
        }
    ],
    "content": "This is some sample content",
    "creationDate": "2021-06-30T17:51:29.812",
    "title": "A new title"
    }

## GET All Posts 

    $ curl "localhost:8080/posts"

## GET All Posts by author and title

    $ curl "localhost:8080/posts/search?author=David&title=My Post"

## GET All Posts by date

    $ curl "localhost:8080/posts/search?dateFrom=2021-06-17T00:00:00.000Z&dateTo=2022-06-17T00:00:00.000Z"

## GET All Posts by multiple authors

    $ curl "localhost:8080/posts/search2?authors=John Doe&authors=Grace Kelly"


## Create POST

    $ curl -X POST "localhost:8080/posts"
    
    {
    "title":"My Post",
    "author":"John Doe"
    }

## Add comment to post

    $ curl -X PUT "localhost:8080/posts/60db336deb401c61ad7c559c"
    
    {
        "content":"This is a comment"
    }
    
## Delete post by id

    $ curl -X DELETE "localhost:8080/posts/60db4b085d2d613300cc136b"

## GET All Comments

    $ curl GET "localhost:8080/comments"

## Update comment

    $ curl -X PUT "localhost:8080/comments/60dc741f971c0d514f627904"

    {
        "content":"This is an update comment"
    }

## Delete comment 
    
    $ curl -X DELETE "localhost:8080/comments/60dc741f971c0d514f627904"

http://localhost:9400/posts
http://localhost:9400/comments

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/run.sh
./mvnw quarkus:dev

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/work.fmus
**run.sh,f(t=)
  $*chmod a+x run.sh
src,d(/mk)
  main,d(/mk)
    docker,d(/mk)
    java,d(/mk)
    resources,d(/mk)
--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/.mvn/wrapper/maven-wrapper.jar
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Zy9hcGFjaGUvbWF2ZW4vd3JhcHBlci9Cb290c3RyYXBNYWluU3RhcnRlci5jbGFzc1BLAQIUAxQACAgIAAEAIQA17EOiEgIAAOUDAAAyAAAAAAAAAAAAAAC0ATsJAABvcmcvYXBhY2hlL21hdmVuL3dyYXBwZXIvRGVmYXVsdERvd25sb2FkZXIkMS5jbGFzc1BLAQIUAxQACAgIAAEAIQDLG18KCQIAAHAEAABTAAAAAAAAAAAAAAC0Aa0LAABvcmcvYXBhY2hlL21hdmVuL3dyYXBwZXIvRGVmYXVsdERvd25sb2FkZXIkU3lzdGVtUHJvcGVydGllc1Byb3h5QXV0aGVudGljYXRvci5jbGFzc1BLAQIUAxQACAgIAAEAIQBDNYSPcAwAAGYYAAAwAAAAAAAAAAAAAAC0ATcOAABvcmcvYXBhY2hlL21hdmVuL3dyYXBwZXIvRGVmYXVsdERvd25sb2FkZXIuY2xhc3NQSwECFAMUAAgICAABACEAhHH3ErAAAADjAAAAKQAAAAAAAAAAAAAAtAEFGwAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL0Rvd25sb2FkZXIuY2xhc3NQSwECFAMUAAgICAABACEA5aFbB9wPAACIHwAAKAAAAAAAAAAAAAAAtAEMHAAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL0luc3RhbGxlci5jbGFzc1BLAQIUAxQACAgIAAEAIQCEJyvj/AEAAG0DAAAlAAAAAAAAAAAAAAC0AT4sAABvcmcvYXBhY2hlL21hdmVuL3dyYXBwZXIvTG9nZ2VyLmNsYXNzUEsBAhQDFAAICAgAAQAhABFwc71dCwAAyxgAAC8AAAAAAAAAAAAAALQBjS4AAG9yZy9hcGFjaGUvbWF2ZW4vd3JhcHBlci9NYXZlbldyYXBwZXJNYWluLmNsYXNzUEsBAhQDFAAICAgAAQAhABxvz0m7AQAAdAMAAD4AAAAAAAAAAAAAALQBRzoAAG9yZy9hcGFjaGUvbWF2ZW4vd3JhcHBlci9QYXRoQXNzZW1ibGVyJExvY2FsRGlzdHJpYnV0aW9uLmNsYXNzUEsBAhQDFAAICAgAAQAhAId8K58/BwAA3g4AACwAAAAAAAAAAAAAALQBbjwAAG9yZy9hcGFjaGUvbWF2ZW4vd3JhcHBlci9QYXRoQXNzZW1ibGVyLmNsYXNzUEsBAhQDFAAICAgAAQAhAHsCYC3oBAAA1wkAADYAAAAAAAAAAAAAALQBB0QAAG9yZy9hcGFjaGUvbWF2ZW4vd3JhcHBlci9TeXN0ZW1Qcm9wZXJ0aWVzSGFuZGxlci5jbGFzc1BLAQIUAxQACAgIAAEAIQC6AT9hmAMAACgJAAAzAAAAAAAAAAAAAAC0AVNJAABvcmcvYXBhY2hlL21hdmVuL3dyYXBwZXIvV3JhcHBlckNvbmZpZ3VyYXRpb24uY2xhc3NQSwECFAMUAAgICAABACEA+MejOZEIAAAsEwAALgAAAAAAAAAAAAAAtAFMTQAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL1dyYXBwZXJFeGVjdXRvci5jbGFzc1BLAQIUABQACAgIAAAAIQAAAAAAAgAAAAAAAAAdAAAAAAAAAAAAAAAAADlWAABvcmcvYXBhY2hlL21hdmVuL3dyYXBwZXIvY2xpL1BLAQIUAxQACAgIAAEAIQDwZFF2/QIAAFQIAAA/AAAAAAAAAAAAAAC0AYZWAABvcmcvYXBhY2hlL21hdmVuL3dyYXBwZXIvY2xpL0Fic3RyYWN0Q29tbWFuZExpbmVDb252ZXJ0ZXIuY2xhc3NQSwECFAMUAAgICAABACEAaucgRq4EAADODAAASQAAAAAAAAAAAAAAtAHwWQAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL2NsaS9BYnN0cmFjdFByb3BlcnRpZXNDb21tYW5kTGluZUNvbnZlcnRlci5jbGFzc1BLAQIUAxQACAgIAAEAIQD7bTaUVAEAAGcCAAA/AAAAAAAAAAAAAAC0ARVfAABvcmcvYXBhY2hlL21hdmVuL3dyYXBwZXIvY2xpL0NvbW1hbmRMaW5lQXJndW1lbnRFeGNlcHRpb24uY2xhc3NQSwECFAMUAAgICAABACEAPTiflEwBAAC7AwAANwAAAAAAAAAAAAAAtAHWYAAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL2NsaS9Db21tYW5kTGluZUNvbnZlcnRlci5jbGFzc1BLAQIUAxQACAgIAAEAIQA2V7BLEQUAAJ4LAAA0AAAAAAAAAAAAAAC0AYdiAABvcmcvYXBhY2hlL21hdmVuL3dyYXBwZXIvY2xpL0NvbW1hbmRMaW5lT3B0aW9uLmNsYXNzUEsBAhQDFAAICAgAAQAhAOa/y2stAwAAJQsAAEkAAAAAAAAAAAAAALQB+mcAAG9yZy9hcGFjaGUvbWF2ZW4vd3JhcHBlci9jbGkvQ29tbWFuZExpbmVQYXJzZXIkQWZ0ZXJGaXJzdFN1YkNvbW1hbmQuY2xhc3NQSwECFAMUAAgICAABACEAGxtbJ5MCAADBBwAAQQAAAAAAAAAAAAAAtAGeawAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL2NsaS9Db21tYW5kTGluZVBhcnNlciRBZnRlck9wdGlvbnMuY2xhc3NQSwECFAMUAAgICAABACEA7BT6390DAAAADQAASgAAAAAAAAAAAAAAtAGgbgAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL2NsaS9Db21tYW5kTGluZVBhcnNlciRCZWZvcmVGaXJzdFN1YkNvbW1hbmQuY2xhc3NQSwECFAMUAAgICAABACEA4KT7RyoCAACvBAAAVAAAAAAAAAAAAAAAtAH1cgAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL2NsaS9Db21tYW5kTGluZVBhcnNlciRDYXNlSW5zZW5zaXRpdmVTdHJpbmdDb21wYXJhdG9yLmNsYXNzUEsBAhQDFAAICAgAAQAhAEZ7KTZOBwAATRQAAEsAAAAAAAAAAAAAALQBoXUAAG9yZy9hcGFjaGUvbWF2ZW4vd3JhcHBlci9jbGkvQ29tbWFuZExpbmVQYXJzZXIkS25vd25PcHRpb25QYXJzZXJTdGF0ZS5jbGFzc1BLAQIUAxQACAgIAAEAIQAKgarvmgIAAEkHAABKAAAAAAAAAAAAAAC0AWh9AABvcmcvYXBhY2hlL21hdmVuL3dyYXBwZXIvY2xpL0NvbW1hbmRMaW5lUGFyc2VyJE1pc3NpbmdPcHRpb25BcmdTdGF0ZS5jbGFzc1BLAQIUAxQACAgIAAEAIQC70D2GqgIAAKcHAABLAAAAAAAAAAAAAAC0AXqAAABvcmcvYXBhY2hlL21hdmVuL3dyYXBwZXIvY2xpL0NvbW1hbmRMaW5lUGFyc2VyJE9wdGlvbkF3YXJlUGFyc2VyU3RhdGUuY2xhc3NQSwECFAMUAAgICAABACEASwKWF80CAACBBwAARQAAAAAAAAAAAAAAtAGdgwAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL2NsaS9Db21tYW5kTGluZVBhcnNlciRPcHRpb25Db21wYXJhdG9yLmNsYXNzUEsBAhQDFAAICAgAAQAhAAqgldKUAQAApQMAAEYAAAAAAAAAAAAAALQB3YYAAG9yZy9hcGFjaGUvbWF2ZW4vd3JhcHBlci9jbGkvQ29tbWFuZExpbmVQYXJzZXIkT3B0aW9uUGFyc2VyU3RhdGUuY2xhc3NQSwECFAMUAAgICAABACEAFqQY03YCAABmBQAAQQAAAAAAAAAAAAAAtAHliAAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL2NsaS9Db21tYW5kTGluZVBhcnNlciRPcHRpb25TdHJpbmcuY2xhc3NQSwECFAMUAAgICAABACEAN6TneX8CAACJBQAASwAAAAAAAAAAAAAAtAHKiwAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL2NsaS9Db21tYW5kTGluZVBhcnNlciRPcHRpb25TdHJpbmdDb21wYXJhdG9yLmNsYXNzUEsBAhQDFAAICAgAAQAhAPt0U4PsAQAAsAQAAEAAAAAAAAAAAAAAALQBwo4AAG9yZy9hcGFjaGUvbWF2ZW4vd3JhcHBlci9jbGkvQ29tbWFuZExpbmVQYXJzZXIkUGFyc2VyU3RhdGUuY2xhc3NQSwECFAMUAAgICAABACEATzzq0ccCAADVBwAATQAAAAAAAAAAAAAAtAEckQAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL2NsaS9Db21tYW5kTGluZVBhcnNlciRVbmtub3duT3B0aW9uUGFyc2VyU3RhdGUuY2xhc3NQSwECFAMUAAgICAABACEANdj7/LIQAAC0KAAANAAAAAAAAAAAAAAAtAFelAAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL2NsaS9Db21tYW5kTGluZVBhcnNlci5jbGFzc1BLAQIUAxQACAgIAAEAIQCIIedA6wYAAHoQAAA0AAAAAAAAAAAAAAC0AXKlAABvcmcvYXBhY2hlL21hdmVuL3dyYXBwZXIvY2xpL1BhcnNlZENvbW1hbmRMaW5lLmNsYXNzUEsBAhQDFAAICAgAAQAhAOA9IUPXAgAAQAUAADoAAAAAAAAAAAAAALQBv6wAAG9yZy9hcGFjaGUvbWF2ZW4vd3JhcHBlci9jbGkvUGFyc2VkQ29tbWFuZExpbmVPcHRpb24uY2xhc3NQSwECFAMUAAgICAABACEA70Jth4gBAAA1AwAASAAAAAAAAAAAAAAAtAH+rwAAb3JnL2FwYWNoZS9tYXZlbi93cmFwcGVyL2NsaS9Qcm9qZWN0UHJvcGVydGllc0NvbW1hbmRMaW5lQ29udmVydGVyLmNsYXNzUEsBAhQDFAAICAgAAQAhAK926rKJAQAAJgMAAEcAAAAAAAAAAAAAALQB/LEAAG9yZy9hcGFjaGUvbWF2ZW4vd3JhcHBlci9jbGkvU3lzdGVtUHJvcGVydGllc0NvbW1hbmRMaW5lQ29udmVydGVyLmNsYXNzUEsFBgAAAAAvAC8ABhIAAPqzAAAAAA==
--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/.mvn/wrapper/maven-wrapper.properties
distributionUrl=https://repo.maven.apache.org/maven2/org/apache/maven/apache-maven/3.8.1/apache-maven-3.8.1-bin.zip
wrapperUrl=https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/0.5.6/maven-wrapper-0.5.6.jar

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/.mvn/wrapper/MavenWrapperDownloader.java
/*
 * Copyright 2007-present the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
import java.net.*;
import java.io.*;
import java.nio.channels.*;
import java.util.Properties;

public class MavenWrapperDownloader {

    private static final String WRAPPER_VERSION = "0.5.6";
    /**
     * Default URL to download the maven-wrapper.jar from, if no 'downloadUrl' is provided.
     */
    private static final String DEFAULT_DOWNLOAD_URL = "https://repo.maven.apache.org/maven2/io/takari/maven-wrapper/"
        + WRAPPER_VERSION + "/maven-wrapper-" + WRAPPER_VERSION + ".jar";

    /**
     * Path to the maven-wrapper.properties file, which might contain a downloadUrl property to
     * use instead of the default one.
     */
    private static final String MAVEN_WRAPPER_PROPERTIES_PATH =
            ".mvn/wrapper/maven-wrapper.properties";

    /**
     * Path where the maven-wrapper.jar will be saved to.
     */
    private static final String MAVEN_WRAPPER_JAR_PATH =
            ".mvn/wrapper/maven-wrapper.jar";

    /**
     * Name of the property which should be used to override the default download url for the wrapper.
     */
    private static final String PROPERTY_NAME_WRAPPER_URL = "wrapperUrl";

    public static void main(String args[]) {
        System.out.println("- Downloader started");
        File baseDirectory = new File(args[0]);
        System.out.println("- Using base directory: " + baseDirectory.getAbsolutePath());

        // If the maven-wrapper.properties exists, read it and check if it contains a custom
        // wrapperUrl parameter.
        File mavenWrapperPropertyFile = new File(baseDirectory, MAVEN_WRAPPER_PROPERTIES_PATH);
        String url = DEFAULT_DOWNLOAD_URL;
        if(mavenWrapperPropertyFile.exists()) {
            FileInputStream mavenWrapperPropertyFileInputStream = null;
            try {
                mavenWrapperPropertyFileInputStream = new FileInputStream(mavenWrapperPropertyFile);
                Properties mavenWrapperProperties = new Properties();
                mavenWrapperProperties.load(mavenWrapperPropertyFileInputStream);
                url = mavenWrapperProperties.getProperty(PROPERTY_NAME_WRAPPER_URL, url);
            } catch (IOException e) {
                System.out.println("- ERROR loading '" + MAVEN_WRAPPER_PROPERTIES_PATH + "'");
            } finally {
                try {
                    if(mavenWrapperPropertyFileInputStream != null) {
                        mavenWrapperPropertyFileInputStream.close();
                    }
                } catch (IOException e) {
                    // Ignore ...
                }
            }
        }
        System.out.println("- Downloading from: " + url);

        File outputFile = new File(baseDirectory.getAbsolutePath(), MAVEN_WRAPPER_JAR_PATH);
        if(!outputFile.getParentFile().exists()) {
            if(!outputFile.getParentFile().mkdirs()) {
                System.out.println(
                        "- ERROR creating output directory '" + outputFile.getParentFile().getAbsolutePath() + "'");
            }
        }
        System.out.println("- Downloading to: " + outputFile.getAbsolutePath());
        try {
            downloadFileFromURL(url, outputFile);
            System.out.println("Done");
            System.exit(0);
        } catch (Throwable e) {
            System.out.println("- Error downloading");
            e.printStackTrace();
            System.exit(1);
        }
    }

    private static void downloadFileFromURL(String urlString, File destination) throws Exception {
        if (System.getenv("MVNW_USERNAME") != null && System.getenv("MVNW_PASSWORD") != null) {
            String username = System.getenv("MVNW_USERNAME");
            char[] password = System.getenv("MVNW_PASSWORD").toCharArray();
            Authenticator.setDefault(new Authenticator() {
                @Override
                protected PasswordAuthentication getPasswordAuthentication() {
                    return new PasswordAuthentication(username, password);
                }
            });
        }
        URL website = new URL(urlString);
        ReadableByteChannel rbc;
        rbc = Channels.newChannel(website.openStream());
        FileOutputStream fos = new FileOutputStream(destination);
        fos.getChannel().transferFrom(rbc, 0, Long.MAX_VALUE);
        fos.close();
        rbc.close();
    }

}

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/docker/Dockerfile.jvm
####
# This Dockerfile is used in order to build a container that runs the Quarkus application in JVM mode
#
# Before building the container image run:
#
# ./mvnw package
#
# Then, build the image with:
#
# docker build -f src/main/docker/Dockerfile.jvm -t quarkus/quarkus-crud-reactive-mongodb-jvm .
#
# Then run the container using:
#
# docker run -i --rm -p 8080:8080 quarkus/quarkus-crud-reactive-mongodb-jvm
#
# If you want to include the debug port into your docker image
# you will have to expose the debug port (default 5005) like this :  EXPOSE 8080 5005
#
# Then run the container using :
#
# docker run -i --rm -p 8080:8080 -p 5005:5005 -e JAVA_ENABLE_DEBUG="true" quarkus/quarkus-crud-reactive-mongodb-jvm
#
###
FROM registry.access.redhat.com/ubi8/ubi-minimal:8.3 

ARG JAVA_PACKAGE=java-11-openjdk-headless
ARG RUN_JAVA_VERSION=1.3.8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en'
# Install java and the run-java script
# Also set up permissions for user `1001`
RUN microdnf install curl ca-certificates ${JAVA_PACKAGE} \
    && microdnf update \
    && microdnf clean all \
    && mkdir /deployments \
    && chown 1001 /deployments \
    && chmod "g+rwX" /deployments \
    && chown 1001:root /deployments \
    && curl https://repo1.maven.org/maven2/io/fabric8/run-java-sh/${RUN_JAVA_VERSION}/run-java-sh-${RUN_JAVA_VERSION}-sh.sh -o /deployments/run-java.sh \
    && chown 1001 /deployments/run-java.sh \
    && chmod 540 /deployments/run-java.sh \
    && echo "securerandom.source=file:/dev/urandom" >> /etc/alternatives/jre/conf/security/java.security

# Configure the JAVA_OPTIONS, you can add -XshowSettings:vm to also display the heap size.
ENV JAVA_OPTIONS="-Dquarkus.http.host=0.0.0.0 -Djava.util.logging.manager=org.jboss.logmanager.LogManager"
# We make four distinct layers so if there are application changes the library layers can be re-used
COPY --chown=1001 target/quarkus-app/lib/ /deployments/lib/
COPY --chown=1001 target/quarkus-app/*.jar /deployments/
COPY --chown=1001 target/quarkus-app/app/ /deployments/app/
COPY --chown=1001 target/quarkus-app/quarkus/ /deployments/quarkus/

EXPOSE 8080
USER 1001

ENTRYPOINT [ "/deployments/run-java.sh" ]

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/docker/Dockerfile.legacy-jar
####
# This Dockerfile is used in order to build a container that runs the Quarkus application in JVM mode
#
# Before building the container image run:
#
# ./mvnw package -Dquarkus.package.type=legacy-jar
#
# Then, build the image with:
#
# docker build -f src/main/docker/Dockerfile.legacy-jar -t quarkus/quarkus-crud-reactive-mongodb-legacy-jar .
#
# Then run the container using:
#
# docker run -i --rm -p 8080:8080 quarkus/quarkus-crud-reactive-mongodb-legacy-jar
#
# If you want to include the debug port into your docker image
# you will have to expose the debug port (default 5005) like this :  EXPOSE 8080 5005
#
# Then run the container using :
#
# docker run -i --rm -p 8080:8080 -p 5005:5005 -e JAVA_ENABLE_DEBUG="true" quarkus/quarkus-crud-reactive-mongodb-legacy-jar
#
###
FROM registry.access.redhat.com/ubi8/ubi-minimal:8.3 

ARG JAVA_PACKAGE=java-11-openjdk-headless
ARG RUN_JAVA_VERSION=1.3.8
ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en'
# Install java and the run-java script
# Also set up permissions for user `1001`
RUN microdnf install curl ca-certificates ${JAVA_PACKAGE} \
    && microdnf update \
    && microdnf clean all \
    && mkdir /deployments \
    && chown 1001 /deployments \
    && chmod "g+rwX" /deployments \
    && chown 1001:root /deployments \
    && curl https://repo1.maven.org/maven2/io/fabric8/run-java-sh/${RUN_JAVA_VERSION}/run-java-sh-${RUN_JAVA_VERSION}-sh.sh -o /deployments/run-java.sh \
    && chown 1001 /deployments/run-java.sh \
    && chmod 540 /deployments/run-java.sh \
    && echo "securerandom.source=file:/dev/urandom" >> /etc/alternatives/jre/conf/security/java.security

# Configure the JAVA_OPTIONS, you can add -XshowSettings:vm to also display the heap size.
ENV JAVA_OPTIONS="-Dquarkus.http.host=0.0.0.0 -Djava.util.logging.manager=org.jboss.logmanager.LogManager"
COPY target/lib/* /deployments/lib/
COPY target/*-runner.jar /deployments/app.jar

EXPOSE 8080
USER 1001

ENTRYPOINT [ "/deployments/run-java.sh" ]

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/docker/Dockerfile.native
####
# This Dockerfile is used in order to build a container that runs the Quarkus application in native (no JVM) mode
#
# Before building the container image run:
#
# ./mvnw package -Pnative
#
# Then, build the image with:
#
# docker build -f src/main/docker/Dockerfile.native -t quarkus/quarkus-crud-reactive-mongodb .
#
# Then run the container using:
#
# docker run -i --rm -p 8080:8080 quarkus/quarkus-crud-reactive-mongodb
#
###
FROM registry.access.redhat.com/ubi8/ubi-minimal:8.3
WORKDIR /work/
RUN chown 1001 /work \
    && chmod "g+rwX" /work \
    && chown 1001:root /work
COPY --chown=1001:root target/*-runner /work/application

EXPOSE 8080
USER 1001

CMD ["./application", "-Dquarkus.http.host=0.0.0.0"]

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/docker/Dockerfile.native-distroless
####
# This Dockerfile is used in order to build a distroless container that runs the Quarkus application in native (no JVM) mode
#
# Before building the container image run:
#
# ./mvnw package -Pnative
#
# Then, build the image with:
#
# docker build -f src/main/docker/Dockerfile.native-distroless -t quarkus/quarkus-crud-reactive-mongodb .
#
# Then run the container using:
#
# docker run -i --rm -p 8080:8080 quarkus/quarkus-crud-reactive-mongodb
#
###
FROM quay.io/quarkus/quarkus-distroless-image:1.0
COPY target/*-runner /application

EXPOSE 8080
USER nonroot

CMD ["./application", "-Dquarkus.http.host=0.0.0.0"]

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/java/apps/comment/Comment.java
package apps.comment;

// import boundary.request.UpdateComment;
import apps.post.UpdatePost;
import apps.post.Post;

import io.quarkus.mongodb.panache.reactive.ReactivePanacheMongoEntity;
import io.smallrye.mutiny.Multi;
import io.smallrye.mutiny.Uni;
import org.bson.types.ObjectId;

import javax.json.bind.annotation.JsonbTransient;
import javax.ws.rs.NotFoundException;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Optional;


public class Comment extends ReactivePanacheMongoEntity {

    public String title;
    public String content;
    public LocalDateTime creationDate;
    @JsonbTransient
    public String postId;

    public static Uni<Comment> updateComment(String id, UpdateComment updateComment) {
        Uni<Comment> commentUni = findById(new ObjectId(id));

        return commentUni.call(comment -> {

            comment.content = updateComment.getContent();

            Uni<Post> uni = Post.findById(new ObjectId(comment.postId));
            return uni.call(posts -> {
                if (posts != null) {
                    Optional<Comment> com = posts.comments.stream()
                            .filter(comment1 -> comment1.equals(comment)).findFirst();
                    if (com.isPresent()) {
                        com.get().content = updateComment.getContent();
                    }
                }
                return Uni.createFrom().item(comment);
            }).chain(post -> post.persistOrUpdate());
        }).chain(comment -> {
            if (comment == null) {
                throw new NotFoundException();
            }
            return comment.persistOrUpdate();
        });


    }

    public static Uni<Void> deleteComment(String commentId) {
        Uni<Comment> commentUni = findById(new ObjectId(commentId));

        return commentUni.call(comment -> {

            Uni<Post> uni = Post.findById(new ObjectId(comment.postId));
            return uni.call(posts -> {
                if (posts != null) {
                    posts.comments.remove(comment);
                }
                return Uni.createFrom().item(comment);
            }).chain(post -> post.persistOrUpdate());
        }).chain(comment -> {
            if (comment == null) {
                throw new NotFoundException();
            }
            return comment.delete();
        });
    }

    public static Multi<Comment> streamAllComments() {
        return streamAll();
    }

    public static Multi<Comment> streamAllCommentsByPostId(String postId) {
        return stream("postId", postId);
    }


    @Override
    public boolean equals(Object c) {
        if (c == null) return false;
        Comment comp = ((Comment) c);
        return comp.id.equals(id);
    }
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/java/apps/comment/ReactiveCommentResource.java
package apps.comment;

// import boundary.request.UpdateComment;
import apps.post.UpdatePost;
// import entity.Comment;
import apps.post.Post;

import io.smallrye.mutiny.Multi;
import io.smallrye.mutiny.Uni;
import org.bson.types.ObjectId;

import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;

@Path("/comments")
public class ReactiveCommentResource {


    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Multi<Comment> list() {
        return Comment.streamAllComments();
    }

    @GET
    @Path("/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Uni<Comment> getComment(@PathParam("id") String id) {
        return Comment.findById(new ObjectId(id));
    }

    @DELETE
    @Path("/{id}")
    public Uni<Void> deleteComment(@PathParam("id") String id) {
        return Comment.deleteComment(id);
    }

    @PUT
    @Path("/{id}")
    @Consumes(MediaType.APPLICATION_JSON)
    public Uni<Comment> update(@PathParam("id") String id, UpdateComment updateComment) {
        return Comment.updateComment(id, updateComment);
    }

}
--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/java/apps/comment/UpdateComment.java
package apps.comment;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class UpdateComment {

    String content;
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/java/apps/post/Post.java
package apps.post;

// import boundary.request.UpdatePost;
import apps.comment.Comment;

import io.quarkus.mongodb.panache.reactive.ReactivePanacheMongoEntity;
import io.smallrye.mutiny.Multi;
import io.smallrye.mutiny.Uni;
import org.bson.types.ObjectId;

import javax.ws.rs.NotFoundException;
import java.time.LocalDateTime;
import java.util.List;


public class Post extends ReactivePanacheMongoEntity {

    public String title;
    public String content;
    public String author;
    public LocalDateTime creationDate;
    public List<Comment> comments;


    public static Uni<Post> updatePost(String id, UpdatePost updatePost) {
        Uni<Post> postUni = Post.findById(new ObjectId(id));
        return postUni
                .onItem().transform(post -> {
                    post.content = updatePost.getContent();
                    post.title = updatePost.getTitle();
                    return post;
                }).call(post -> post.persistOrUpdate());
    }


    public static Uni<Post> addCommentToPost(Comment comment, String postId) {
        Uni<Post> postUni = findById(new ObjectId(postId));

        return postUni.onItem().transform(post -> {

            if (post.comments == null) {
                post.comments = List.of(comment);
            } else {
                post.comments.add(comment);
            }
            comment.creationDate = LocalDateTime.now();
            comment.postId = postId;
            return post;
        }).call(post -> comment.persist().chain(() -> post.persistOrUpdate()));
    }

    public static Uni<Void> deletePost(String postId) {
        Uni<Post> postUni = findById(new ObjectId(postId));
        Multi<Comment> commentsUni = Comment.streamAllCommentsByPostId(postId);

        return postUni.call(post -> commentsUni.onItem().call(comment -> comment.delete())
                .collect().asList()).chain(post -> {
            if (post == null) {
                throw new NotFoundException();
            }
            return post.delete();
        });
    }

    public static Multi<Post> streamAllPosts() {
        return streamAll();
    }

}

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/java/apps/post/ReactivePostResource.java
package apps.post;

// import boundary.request.UpdatePost;
import apps.comment.Comment;
// import entity.Post;

import io.smallrye.mutiny.Multi;
import io.smallrye.mutiny.Uni;
import org.bson.Document;
import org.bson.types.ObjectId;

import javax.ws.rs.Consumes;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.PathParam;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.net.URI;
import java.time.LocalDateTime;
import java.time.ZonedDateTime;
import java.util.List;

@Path("/posts")
public class ReactivePostResource {


    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public Multi<Post> list() {
        return Post.streamAllPosts();
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    public Uni<Response> addPost(Post post) {
        post.creationDate = LocalDateTime.now();
        return post.<Post>persist().map(v ->
                Response.created(URI.create("/posts/" + v.id.toString()))
                        .entity(post).build());
    }

    @PUT
    @Path("/{id}")
    @Consumes(MediaType.APPLICATION_JSON)
    public Uni<Post> update(@PathParam("id") String id, UpdatePost updatePost) {
        return Post.updatePost(id, updatePost);
    }

    @GET
    @Path("/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Uni<Post> getPost(@PathParam("id") String id) {
        return Post.findById(new ObjectId(id));
    }

    @DELETE
    @Path("/{id}")
    public Uni<Void> deletePost(@PathParam("id") String id) {
        return Post.deletePost(id);
    }

    @GET
    @Path("/search")
    public Uni<List<Post>> search(@QueryParam("author") String author, @QueryParam("title") String title,
                                  @QueryParam("dateFrom") String dateFrom, @QueryParam("dateTo") String dateTo) {
        if (author != null) {
            return Post.find("{'author': ?1,'title': ?2}", author, title).list();
        }
        return Post
                .find("{'creationDate': {$gte: ?1}, 'creationDate': {$lte: ?2}}", ZonedDateTime.parse(dateFrom).toLocalDateTime(),
                        ZonedDateTime.parse(dateTo).toLocalDateTime()).list();
    }

    @GET
    @Path("/search2")
    public Uni<List<Post>> searchCustomQueries(@QueryParam("authors") List<String> authors) {

        // using Document
        return Post.find(new Document("author", new Document("$in", authors))).list();

        // using a raw JSON query
        //Post.find("{'$or': {'author':John Doe, 'author':Grace Kelly}}");
        //Post.find("{'author': {'$in': [John Doe, Grace Kelly]}}");

        // using Panache QL
        //Post.find("author in (John Doe,Grace Kelly)");

    }

    @PUT
    @Path("/{id}/comment")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Uni<Response> addCommentToPost(@PathParam("id") String id, Comment comment) {
        return Post.addCommentToPost(comment, id).map(v -> Response.accepted(v).build());
    }

}
--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/java/apps/post/UpdatePost.java
package apps.post;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public class UpdatePost {

    String title;
    String content;
}

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/resources/application.properties
quarkus.mongodb.connection-string = mongodb://usef:rahasia@localhost:27017
quarkus.mongodb.database = myquarkus
quarkus.http.host=0.0.0.0
quarkus.http.port=9400

--#

--% C:/tmp/hapus/fl1/myjava/pake-quarkus/src/main/resources/META-INF/resources/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>quarkus-crud-reactive-mongodb - 1.0.0-SNAPSHOT</title>
    <style>
        h1, h2, h3, h4, h5, h6 {
            margin-bottom: 0.5rem;
            font-weight: 400;
            line-height: 1.5;
        }

        h1 {
            font-size: 2.5rem;
        }

        h2 {
            font-size: 2rem
        }

        h3 {
            font-size: 1.75rem

        }

        h4 {
            font-size: 1.5rem
        }

        h5 {
            font-size: 1.25rem
        }

        h6 {
            font-size: 1rem
        }

        .lead {
            font-weight: 300;
            font-size: 2rem;
        }

        .banner {
            font-size: 2.7rem;
            margin: 0;
            padding: 2rem 1rem;
            background-color: #0d1c2c;
            color: white;
        }

        body {
            margin: 0;
            font-family: -apple-system, system-ui, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji";
        }

        code {
            font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
            font-size: 87.5%;
            color: #e83e8c;
            word-break: break-word;
        }

        .left-column {
            padding: .75rem;
            max-width: 75%;
            min-width: 55%;
        }

        .right-column {
            padding: .75rem;
            max-width: 25%;
        }

        .container {
            display: flex;
            width: 100%;
        }

        li {
            margin: 0.75rem;
        }

        .right-section {
            margin-left: 1rem;
            padding-left: 0.5rem;
        }

        .right-section h3 {
            padding-top: 0;
            font-weight: 200;
        }

        .right-section ul {
            border-left: 0.3rem solid #71aeef;
            list-style-type: none;
            padding-left: 0;
        }

        .example-code {
            border-left: 0.3rem solid #71aeef;
            padding-left: 10px;
        }

        .example-code h3 {
            font-weight: 200;
        }
    </style>
</head>
<body>

<div class="banner lead">
    Your new Cloud-Native application is ready!
</div>

<div class="container">
    <div class="left-column">
        <p class="lead"> Congratulations, you have created a new Quarkus cloud application.</p>

        <h2>What is this page?</h2>

        <p>This page is served by Quarkus. The source is in
            <code>src/main/resources/META-INF/resources/index.html</code>.</p>

        <h2>What are your next steps?</h2>

        <p>If not already done, run the application in <em>dev mode</em> using: <code>./mvnw compile quarkus:dev</code>.
        </p>
        <ul>
            <li>Your static assets are located in <code>src/main/resources/META-INF/resources</code>.</li>
            <li>Configure your application in <code>src/main/resources/application.properties</code>.</li>
            <li>Quarkus now ships with a <a href="/q/dev/">Dev UI</a> (available in dev mode only)</li>
            <li>Play with the getting started example code located in <code>src/main/java</code>:</li>
        </ul>
                <div class="example-code">
            <h3>RESTEasy JAX-RS example</h3>
            <p>REST is easy peasy with this Hello World RESTEasy resource.</p>
            <p><code>@Path: <a href="/hello-resteasy" class="path-link" target="_blank">/hello-resteasy</a></code></p>
            <p><a href="https://quarkus.io/guides/getting-started#the-jax-rs-resources" class="guide-link" target="_blank">Related guide section...</a></p>
        </div>

    </div>
    <div class="right-column">
        <div class="right-section">
            <h3>Application</h3>
            <ul>
                <li>GroupId: <code>org.dvddhln</code></li>
                <li>ArtifactId: <code>quarkus-crud-reactive-mongodb</code></li>
                <li>Version: <code>1.0.0-SNAPSHOT</code></li>
                <li>Quarkus Version: <code>1.13.7.Final</code></li>
            </ul>
        </div>
        <div class="right-section">
            <h3>Do you like Quarkus?</h3>
            <ul>
                <li>Go give it a star on <a href="https://github.com/quarkusio/quarkus">GitHub</a>.</li>
            </ul>
        </div>
        <div class="right-section">
            <h3>More reading</h3>
            <ul>
                <li><a href="https://quarkus.io/guides/maven-tooling.html" target="_blank">Setup your IDE</a></li>
                <li><a href="https://quarkus.io/guides/getting-started.html" target="_blank">Getting started</a></li>
                <li><a href="https://quarkus.io/guides/" target="_blank">All guides</a></li>
                <li><a href="https://quarkus.io" target="_blank">Quarkus Web Site</a></li>
            </ul>
        </div>
    </div>
</div>
</body>
</html>
--#

