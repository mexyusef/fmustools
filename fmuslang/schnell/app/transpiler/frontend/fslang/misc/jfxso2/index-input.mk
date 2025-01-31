--% run.sh
./gradlew run
--#

--% run.bat
gradlew run
--#

--% index/fmus
jfxso2,d(/mk)
	%utama=__FILE__
	build.gradle,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/build.gradle)
	gradlew,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/gradlew)
	gradlew.bat,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/gradlew.bat)
	settings.gradle,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/settings.gradle)
	run.sh,f(e=__FILE__=run.sh)
	run.bat,f(e=__FILE__=run.bat)
	$*chmod a+x run.sh
	.gradle,d(/mk)
		6.3,d(/mk)
			gc.properties,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.3/gc.properties)
			executionHistory,d(/mk)
				executionHistory.lock,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.3/executionHistory/executionHistory.lock)
			fileChanges,d(/mk)
			fileContent,d(/mk)
				fileContent.lock,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.3/fileContent/fileContent.lock)
			fileHashes,d(/mk)
				fileHashes.lock,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.3/fileHashes/fileHashes.lock)
			javaCompile,d(/mk)
				javaCompile.lock,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.3/javaCompile/javaCompile.lock)
			vcsMetadata-1,d(/mk)
		6.5,d(/mk)
			gc.properties,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.5/gc.properties)
			executionHistory,d(/mk)
				executionHistory.lock,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.5/executionHistory/executionHistory.lock)
			fileChanges,d(/mk)
			fileHashes,d(/mk)
				fileHashes.lock,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.5/fileHashes/fileHashes.lock)
			vcsMetadata-1,d(/mk)
		6.6.1,d(/mk)
			gc.properties,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.6.1/gc.properties)
			executionHistory,d(/mk)
				executionHistory.lock,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.6.1/executionHistory/executionHistory.lock)
			fileChanges,d(/mk)
			fileContent,d(/mk)
				fileContent.lock,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.6.1/fileContent/fileContent.lock)
			fileHashes,d(/mk)
				fileHashes.lock,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.6.1/fileHashes/fileHashes.lock)
			javaCompile,d(/mk)
				javaCompile.lock,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.6.1/javaCompile/javaCompile.lock)
			vcsMetadata-1,d(/mk)
		buildOutputCleanup,d(/mk)
			buildOutputCleanup.lock,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/buildOutputCleanup/buildOutputCleanup.lock)
			cache.properties,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/buildOutputCleanup/cache.properties)
		checksums,d(/mk)
			checksums.lock,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/checksums/checksums.lock)
		configuration-cache,d(/mk)
			gc.properties,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/configuration-cache/gc.properties)
		vcs-1,d(/mk)
			gc.properties,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/.gradle/vcs-1/gc.properties)
	gradle,d(/mk)
		wrapper,d(/mk)
			gradle-wrapper.jar,f(b64=utama=F:/jualan/dahsyat/sfx/stackoverlow/gradle/wrapper/gradle-wrapper.jar)
			gradle-wrapper.properties,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/gradle/wrapper/gradle-wrapper.properties)
	src,d(/mk)
		main,d(/mk)
			java,d(/mk)
				be,d(/mk)
					fulgent,d(/mk)
						fxapp,d(/mk)
							Program.java,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/src/main/java/be/fulgent/fxapp/Program.java)
							Question.java,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/src/main/java/be/fulgent/fxapp/Question.java)
							Startup.java,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/src/main/java/be/fulgent/fxapp/Startup.java)
			resources,d(/mk)
				gaya.css,f(e=utama=F:/jualan/dahsyat/sfx/stackoverlow/src/main/resources/gaya.css)
		test,d(/mk)
			java,d(/mk)
			resources,d(/mk)
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/build.gradle
plugins {
	id 'java'
	id 'application'
	id 'org.openjfx.javafxplugin' version '0.0.9'
}

group 'org.example'
version '1.0-SNAPSHOT'

repositories {
	mavenCentral()
	jcenter()
}

dependencies {
	testCompile group: 'junit', name: 'junit', version: '4.12'

	implementation 'com.google.guava:guava:29.0-jre'
	implementation 'org.glassfish:javax.json:1.1'
	implementation 'com.gluonhq:connect:1.4.3'
	implementation "jakarta.xml.bind:jakarta.xml.bind-api:2.3.2"
	implementation "org.glassfish.jaxb:jaxb-runtime:2.3.2"
	implementation 'org.json:json:20201115'
	implementation 'org.jsoup:jsoup:1.13.1'
}


def packagename = 'be.fulgent.fxapp'
// ternyata . di-esc bukan \. tapi \\.
def packagefolder = packagename.replaceAll('\\.','/')

application {
//    mainClassName = "${packagename}.Program"
	 mainClassName = "${packagename}.Startup"
}

javafx {
	modules = [ 'javafx.controls', 'javafx.fxml', 'javafx.graphics', 'javafx.web' ]
}

//sourceSets {
//    main {
//        //output.resourcesDir = "$buildDir/classes/java/$name/${packagename}"
//        //output.resourcesDir = "build/classes/java/$name/$packagename"
//        //output.resourcesDir = "build/classes/java/$name/${packagename.replaceAll('.','/')}"
//        output.resourcesDir = "build/classes/java/$name/$packagefolder"
//    }
//}

--#

--% F:/jualan/dahsyat/sfx/stackoverlow/gradlew
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

--% F:/jualan/dahsyat/sfx/stackoverlow/gradlew.bat
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
if "%ERRORLEVEL%" == "0" goto init

echo.
echo ERROR: JAVA_HOME is not set and no 'java' command could be found in your PATH.
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:findJavaFromJavaHome
set JAVA_HOME=%JAVA_HOME:"=%
set JAVA_EXE=%JAVA_HOME%/bin/java.exe

if exist "%JAVA_EXE%" goto init

echo.
echo ERROR: JAVA_HOME is set to an invalid directory: %JAVA_HOME%
echo.
echo Please set the JAVA_HOME variable in your environment to match the
echo location of your Java installation.

goto fail

:init
@rem Get command-line arguments, handling Windows variants

if not "%OS%" == "Windows_NT" goto win9xME_args

:win9xME_args
@rem Slurp the command line arguments.
set CMD_LINE_ARGS=
set _SKIP=2

:win9xME_args_slurp
if "x%~1" == "x" goto execute

set CMD_LINE_ARGS=%*

:execute
@rem Setup the command line

set CLASSPATH=%APP_HOME%\gradle\wrapper\gradle-wrapper.jar


@rem Execute Gradle
"%JAVA_EXE%" %DEFAULT_JVM_OPTS% %JAVA_OPTS% %GRADLE_OPTS% "-Dorg.gradle.appname=%APP_BASE_NAME%" -classpath "%CLASSPATH%" org.gradle.wrapper.GradleWrapperMain %CMD_LINE_ARGS%

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

--% F:/jualan/dahsyat/sfx/stackoverlow/settings.gradle
rootProject.name = 'stackoverlow'


--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.3/gc.properties

--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.3/executionHistory/executionHistory.lock
A41VoDhG5oLkAAAAAAAAAAQ=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.3/fileContent/fileContent.lock
A4W2Rdq5HH0+AAAAAAAAAAA=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.3/fileHashes/fileHashes.lock
AzRJ+oIZWSjgAAAAAAAAAAo=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.3/javaCompile/javaCompile.lock
A3ZKZjRFP6AcAAAAAAAAJDI=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.5/gc.properties

--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.5/executionHistory/executionHistory.lock
A7KRRlK1idb+AAAAAAAAAAM=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.5/fileHashes/fileHashes.lock
A/IJQEaz8gtcAAAAAAAAAAY=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.6.1/gc.properties

--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.6.1/executionHistory/executionHistory.lock
A23jxVvQaEQgAAAAAAAAAJA=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.6.1/fileContent/fileContent.lock
AxuHSV2g5wvGAAAAAAAAAAA=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.6.1/fileHashes/fileHashes.lock
AwFkzg9ilQ+hAAAAAAAAANM=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/6.6.1/javaCompile/javaCompile.lock
AzxM6094KNFMAAAAAAAABCo=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/buildOutputCleanup/buildOutputCleanup.lock
A4L74Oti5vadAAAAAAAAAP0=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/buildOutputCleanup/cache.properties
#Mon Jan 31 22:39:44 ICT 2022
gradle.version=6.3

--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/checksums/checksums.lock
A/KmGM2THGfMAAAAAAAAApM=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/configuration-cache/gc.properties

--#

--% F:/jualan/dahsyat/sfx/stackoverlow/.gradle/vcs-1/gc.properties

--#

--% F:/jualan/dahsyat/sfx/stackoverlow/gradle/wrapper/gradle-wrapper.jar
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Z3JhZGxlL2NsaS9Db21tYW5kTGluZUNvbnZlcnRlci5jbGFzc1BLAQIUAwoAAAgIAAAAQQBTZgrVAgYAAGcOAAAmAAAAAAAAAAAAAACkgdF+AABvcmcvZ3JhZGxlL2NsaS9Db21tYW5kTGluZU9wdGlvbi5jbGFzc1BLAQIUAwoAAAgIAAAAQQD87YqvpQAAAOUAAAAoAAAAAAAAAAAAAACkgReFAABvcmcvZ3JhZGxlL2NsaS9Db21tYW5kTGluZVBhcnNlciQxLmNsYXNzUEsBAhQDCgAACAgAAABBACQVZntLAwAAvwkAADsAAAAAAAAAAAAAAKSBAoYAAG9yZy9ncmFkbGUvY2xpL0NvbW1hbmRMaW5lUGFyc2VyJEFmdGVyRmlyc3RTdWJDb21tYW5kLmNsYXNzUEsBAhQDCgAACAgAAABBAKUZRKOiAgAAJgcAADMAAAAAAAAAAAAAAKSBpokAAG9yZy9ncmFkbGUvY2xpL0NvbW1hbmRMaW5lUGFyc2VyJEFmdGVyT3B0aW9ucy5jbGFzc1BLAQIUAwoAAAgIAAAAQQCMi00T/AMAAHULAAA8AAAAAAAAAAAAAACkgZmMAABvcmcvZ3JhZGxlL2NsaS9Db21tYW5kTGluZVBhcnNlciRCZWZvcmVGaXJzdFN1YkNvbW1hbmQuY2xhc3NQSwECFAMKAAAICAAAAEEAtCqrWk0CAADvBAAARgAAAAAAAAAAAAAApIHvkAAAb3JnL2dyYWRsZS9jbGkvQ29tbWFuZExpbmVQYXJzZXIkQ2FzZUluc2Vuc2l0aXZlU3RyaW5nQ29tcGFyYXRvci5jbGFzc1BLAQIUAwoAAAgIAAAAQQB87FLO0AYAACYRAAA9AAAAAAAAAAAAAACkgaCTAABvcmcvZ3JhZGxlL2NsaS9Db21tYW5kTGluZVBhcnNlciRLbm93bk9wdGlvblBhcnNlclN0YXRlLmNsYXNzUEsBAhQDCgAACAgAAABBACTEvqKlAgAA9AYAADwAAAAAAAAAAAAAAKSBy5oAAG9yZy9ncmFkbGUvY2xpL0NvbW1hbmRMaW5lUGFyc2VyJE1pc3NpbmdPcHRpb25BcmdTdGF0ZS5jbGFzc1BLAQIUAwoAAAgIAAAAQQBUBEs+qgIAAMQGAAA9AAAAAAAAAAAAAACkgcqdAABvcmcvZ3JhZGxlL2NsaS9Db21tYW5kTGluZVBhcnNlciRPcHRpb25Bd2FyZVBhcnNlclN0YXRlLmNsYXNzUEsBAhQDCgAACAgAAABBAJgl4My7AgAAqgYAADcAAAAAAAAAAAAAAKSBz6AAAG9yZy9ncmFkbGUvY2xpL0NvbW1hbmRMaW5lUGFyc2VyJE9wdGlvbkNvbXBhcmF0b3IuY2xhc3NQSwECFAMKAAAICAAAAEEA5GZDmKcBAACjAwAAOAAAAAAAAAAAAAAApIHfowAAb3JnL2dyYWRsZS9jbGkvQ29tbWFuZExpbmVQYXJzZXIkT3B0aW9uUGFyc2VyU3RhdGUuY2xhc3NQSwECFAMKAAAICAAAAEEAosb3RasCAAC2BQAAMwAAAAAAAAAAAAAApIHcpQAAb3JnL2dyYWRsZS9jbGkvQ29tbWFuZExpbmVQYXJzZXIkT3B0aW9uU3RyaW5nLmNsYXNzUEsBAhQDCgAACAgAAABBAGdBcbKUAgAAeAUAAD0AAAAAAAAAAAAAAKSB2KgAAG9yZy9ncmFkbGUvY2xpL0NvbW1hbmRMaW5lUGFyc2VyJE9wdGlvblN0cmluZ0NvbXBhcmF0b3IuY2xhc3NQSwECFAMKAAAICAAAAEEAYE1+VQQCAAC4BAAAMgAAAAAAAAAAAAAApIHHqwAAb3JnL2dyYWRsZS9jbGkvQ29tbWFuZExpbmVQYXJzZXIkUGFyc2VyU3RhdGUuY2xhc3NQSwECFAMKAAAICAAAAEEAcM1YDd0CAABrBwAAPwAAAAAAAAAAAAAApIEbrgAAb3JnL2dyYWRsZS9jbGkvQ29tbWFuZExpbmVQYXJzZXIkVW5rbm93bk9wdGlvblBhcnNlclN0YXRlLmNsYXNzUEsBAhQDCgAACAgAAABBABCjPQcWEgAAbCkAACYAAAAAAAAAAAAAAKSBVbEAAG9yZy9ncmFkbGUvY2xpL0NvbW1hbmRMaW5lUGFyc2VyLmNsYXNzUEsBAhQDCgAACAgAAABBABqL5T7JBwAAABIAACYAAAAAAAAAAAAAAKSBr8MAAG9yZy9ncmFkbGUvY2xpL1BhcnNlZENvbW1hbmRMaW5lLmNsYXNzUEsBAhQDCgAACAgAAABBAHnfBXTaAgAARQUAACwAAAAAAAAAAAAAAKSBvMsAAG9yZy9ncmFkbGUvY2xpL1BhcnNlZENvbW1hbmRMaW5lT3B0aW9uLmNsYXNzUEsBAhQDCgAACAgAAABBAFx2xkJ8AQAACwMAADoAAAAAAAAAAAAAAKSB4M4AAG9yZy9ncmFkbGUvY2xpL1Byb2plY3RQcm9wZXJ0aWVzQ29tbWFuZExpbmVDb252ZXJ0ZXIuY2xhc3NQSwECFAMKAAAICAAAAEEACs84PXwBAAD8AgAAOQAAAAAAAAAAAAAApIG00AAAb3JnL2dyYWRsZS9jbGkvU3lzdGVtUHJvcGVydGllc0NvbW1hbmRMaW5lQ29udmVydGVyLmNsYXNzUEsBAhQDCgAACAgAAABBAP3YP6IVAAAAEwAAAB8AAAAAAAAAAAAAAKSBh9IAAGdyYWRsZS1jbGktY2xhc3NwYXRoLnByb3BlcnRpZXNQSwECFAMKAAAICAAAAEEAAAAAAAIAAAAAAAAAJQAAAAAAAAAAAAAApIHZ0gAAZ3JhZGxlLWNsaS1wYXJhbWV0ZXItbmFtZXMucHJvcGVydGllc1BLBQYAAAAANgA2AOoSAAAe0wAAAAA=
--#

--% F:/jualan/dahsyat/sfx/stackoverlow/gradle/wrapper/gradle-wrapper.properties
distributionBase=GRADLE_USER_HOME
distributionPath=wrapper/dists
distributionUrl=https\://services.gradle.org/distributions/gradle-6.3-bin.zip
zipStoreBase=GRADLE_USER_HOME
zipStorePath=wrapper/dists

--#

--% F:/jualan/dahsyat/sfx/stackoverlow/src/main/java/be/fulgent/fxapp/Program.java
package be.fulgent.fxapp;

import org.jsoup.Jsoup;
import org.jsoup.helper.Validate;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

//https://jsoup.org/cookbook/extracting-data/example-list-links

public class Program {
	public void Main() throws Exception {
		String url1 = "http://news.ycombinator.com/";
		String url2 = "https://stackoverflow.com/questions";
//        String[] args = Arrays.asList(url1).toArray(new String[0]);
//        Main(args);

		StackOverflow(url2);
	}

	public void StackOverflow(String url) throws Exception {
		Document doc = Jsoup.connect(url).get();

		int counter = 1;
		Elements divQuestion = doc.select("div.question-summary");
		for (Element question: divQuestion) {
			Element divTags = question.select("div.tags").first();
			Elements elemTags = divTags.select("a.post-tag");
			List<String> listTags = elemTags
				.stream()
				.map(elem -> elem.text())
				.collect(Collectors.toList());
			String tags = String.join(", ", listTags);

			Element user = question.select("div.user-details a").first();
			String username = user.text();

			Element waktos1 = question.selectFirst("div.user-action-time span");
			String waktos2 = waktos1.attr("title");
			String waktos3 = waktos1.text();
			String waktos = waktos2 + " " + waktos3;

			Element link = question.select("a.question-hyperlink").first();

			print("* %d. %s\n\t%s\n\t%s\n\t%s\n\t\t%s\n\n",
					counter,
					link.text(),
					tags,
					username,
					waktos,
					link.attr("abs:href")
			);

			counter += 1;
		}

	}

	public void Main(String[] args) throws Exception {
		Validate.isTrue(args.length == 1, "usage: supply url to fetch");
		String url = args[0];
		print("Fetching %s...", url);

		Document doc = Jsoup.connect(url).get();
		Elements links = doc.select("a[href]");
		Elements media = doc.select("[src]");
		Elements imports = doc.select("link[href]");

		print("\nMedia: (%d)", media.size());
		for (Element src : media) {
			if (src.normalName().equals("img"))
				print(" * %s: <%s> %sx%s (%s)",
						src.tagName(), src.attr("abs:src"), src.attr("width"), src.attr("height"),
						trim(src.attr("alt"), 20));
			else
				print(" * %s: <%s>", src.tagName(), src.attr("abs:src"));
		}

		print("\nImports: (%d)", imports.size());
		for (Element link : imports) {
			print(" * %s <%s> (%s)", link.tagName(),link.attr("abs:href"), link.attr("rel"));
		}

		print("\nLinks: (%d)", links.size());
		for (Element link : links) {
			print(" * a: <%s>  (%s)", link.attr("abs:href"), trim(link.text(), 35));
		}
	}

	public static void main(String[] args) throws IOException {
		Program p = new Program();
		try {
			if (args.length > 0)
				p.Main(args);
			else
				p.Main();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	private static void print(String msg, Object... args) {
		System.out.println(String.format(msg, args));
	}

	private static String trim(String s, int width) {
		if (s.length() > width)
			return s.substring(0, width-1) + ".";
		else
			return s;
	}

}

--#

--% F:/jualan/dahsyat/sfx/stackoverlow/src/main/java/be/fulgent/fxapp/Question.java
package be.fulgent.fxapp;


import java.text.SimpleDateFormat;
import java.util.Date;
import javafx.beans.property.SimpleStringProperty;
import javafx.beans.property.StringProperty;
import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;


@XmlAccessorType(XmlAccessType.PROPERTY)
public class Question {

	static final SimpleDateFormat sdf = new SimpleDateFormat ("dd-MM-YY");

	private StringProperty ownerProperty = new SimpleStringProperty();
	private String question;
//    private long timestamp;
	private String waktos;

	private String alamat;
	private String tags;


	public String getAlamat() {
		return alamat;
	}

	public void setAlamat(String alamat) {
		this.alamat = alamat;
	}

	public String getTags() {
		return tags;
	}

	public void setTags(String tags) {
		this.tags = tags;
	}


	public Question (String o, String q, String w, String a, String t) {
		this.ownerProperty.set(o);
		this.question = q;
		this.waktos = w;
		this.alamat = a;
		this.tags = t;
	}

	public String getOwner() {
		return ownerProperty.get();
	}

	public void setOwner(String owner) {
		this.ownerProperty.set(owner);
	}

	public String getQuestion() {
		return question;
	}

	public void setQuestion(String question) {
		this.question = question;
	}

	public String getWaktos() {
		return waktos;
	}

	public void setWaktos(String waktos) {
		this.waktos = waktos;
	}

}


--#

--% F:/jualan/dahsyat/sfx/stackoverlow/src/main/java/be/fulgent/fxapp/Startup.java
package be.fulgent.fxapp;


import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;
import javafx.application.Application;
import static javafx.application.Application.launch;
import javafx.beans.InvalidationListener;
import javafx.beans.Observable;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.concurrent.Service;
import javafx.concurrent.Worker;
import javafx.scene.Scene;
import javafx.geometry.Rectangle2D;
import javafx.scene.control.TableRow;
import javafx.stage.Screen;

import javafx.scene.control.TableCell;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.util.Callback;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.Reader;
import java.nio.charset.Charset;

import java.net.URL;
import java.net.URLConnection;
import java.net.MalformedURLException;
import java.util.List;
import java.util.stream.Collectors;
import java.util.zip.GZIPInputStream;
//import javafx.collections.FXCollections;
//import javafx.collections.ObservableList;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import javafx.scene.web.WebView;
import javafx.scene.input.Clipboard;
import javafx.scene.input.ClipboardContent;


public class Startup extends Application {

	static final SimpleDateFormat sdf = new SimpleDateFormat("dd-MM-YY");
	static final String soUrl = "http://api.stackexchange.com/2.2/search?order=desc&sort=activity&tagged=javafx&site=stackoverflow";
	final String stackOverflow = "https://stackoverflow.com/questions";
	final int Pages = 5;
	double lebar, tinggi;
	final Clipboard clipboard = Clipboard.getSystemClipboard();

	public static void main(String[] args) {
		launch(args);
	}


	public void copyClipboard(String nilai) {
		ClipboardContent content = new ClipboardContent();
//        content.putString("Some text");
//        content.putHtml("<b>Some</b> text");
		content.putString(nilai);
		clipboard.setContent(content);
	}
	@Override
	public void start(Stage primaryStage) throws Exception {
		TableView<Question> tableView = new TableView<>();


		tableView.setItems(getObservableList());
//        tableView.setItems(getObservableList2());


		TableColumn<Question, String> dateColumn = new TableColumn<>("Date");
		TableColumn<Question, String> ownerColumn = new TableColumn<>("Owner");
		TableColumn<Question, String> questionColumn = new TableColumn<>("Question");

		TableColumn<Question, String> tagsColumn = new TableColumn<>("Tags");
		TableColumn<Question, String> linkColumn = new TableColumn<>("Url");

//        dateColumn.setCellValueFactory(new PropertyValueFactory<>("timestampString"));
		dateColumn.setCellValueFactory(new PropertyValueFactory<>("waktos"));
		ownerColumn.setCellValueFactory(new PropertyValueFactory<>("owner"));
		questionColumn.setCellValueFactory(new PropertyValueFactory<>("question"));

		tagsColumn.setCellValueFactory(new PropertyValueFactory<>("tags"));
		linkColumn.setCellValueFactory(new PropertyValueFactory<>("alamat"));

		questionColumn.setPrefWidth(800);
		tableView.getColumns().addAll(questionColumn, tagsColumn, dateColumn, ownerColumn, linkColumn);

		tableView.setRowFactory(tv -> {
			final TableRow<Question> row = new TableRow<>();
//            row.hoverProperty().addListener(observable -> {
//                final Question item = row.getItem();
//                if (row.isHover() && item != null) {
//                    processHover(item);
//                }
//            });
//            if (! row.isEmpty()
//            && event.getButton()==MouseButton.PRIMARY
//            && event.getClickCount() == 2) {
			row.setOnMouseClicked(event -> {
				final Question item = row.getItem();
				if (event.getClickCount()==1 && !row.isEmpty()) {
					processClick(primaryStage, item);
				}
			});
			return row;
		});

		StackPane root = new StackPane();
		root.getChildren().add(tableView);



		Scene scene = new Scene(root, 1200, 768);

//        https://stackoverflow.com/questions/18700478/set-row-height-in-javafx-tableview
		scene.getStylesheets().add("gaya.css");

		primaryStage.setTitle("Wieke's StackOverflow Table");
		primaryStage.setScene(scene);

//        http://www.java2s.com/Code/Java/JavaFX/GetScreensize.htm
		Rectangle2D primaryScreenBounds = Screen.getPrimary().getVisualBounds();
		primaryStage.setWidth(primaryScreenBounds.getWidth());
		lebar = primaryScreenBounds.getWidth();
		tinggi = primaryScreenBounds.getHeight();

		primaryStage.show();
	}

	private void processClick(Stage primaryStage, Question item) {
//        System.out.println("Aku harus buka ini: " + item.getAlamat());
		copyClipboard(item.getAlamat());

//        Label secondLabel = new Label("I'm a Label on new Window");
		WebView internet = new WebView();
		internet.getEngine().load(item.getAlamat());

		StackPane secondaryLayout = new StackPane();
		secondaryLayout.getChildren().add(internet);

		Scene secondScene = new Scene(secondaryLayout, lebar/2, tinggi);

		// New window (Stage)
		Stage newWindow = new Stage();
		newWindow.setTitle("Second Stage");
		newWindow.setScene(secondScene);

		// Set position of second window, related to primary window.
		newWindow.setX(primaryStage.getX() + (lebar/2));
		newWindow.setY(primaryStage.getY() + 0);

		newWindow.show();
	}

	public void addQuestions(String url, ObservableList<Question> answer) throws IOException {

		Document doc = Jsoup.connect(url).get();
		Elements divQuestion = doc.select("div.question-summary");
		for (Element question: divQuestion) {
			Element divTags = question.select("div.tags").first();
			Elements elemTags = divTags.select("a.post-tag");
			List<String> listTags = elemTags
					.stream()
					.map(elem -> elem.text())
					.collect(Collectors.toList());
			String tags = String.join(", ", listTags);

			Element user = question.select("div.user-details a").first();
			String username = user.text();

			Element waktos1 = question.selectFirst("div.user-action-time span");
			String waktos2 = waktos1.attr("title");
			String waktos3 = waktos1.text();
			String waktos = waktos2 + " " + waktos3;

			Element link = question.select("a.question-hyperlink").first();

			Question q = new Question(username, link.text(), waktos, link.attr("abs:href"), tags);
			answer.add(q);
		}
	}

	ObservableList<Question> getObservableList() throws IOException {
		ObservableList<Question> answer = FXCollections.observableArrayList();

		for (int i=1; i<=Pages; i++) {
			String url = stackOverflow;
			if (i > 1) url += "?tab=newest&page=" + i;
			addQuestions(url, answer);
		}

		return answer;
	}

	ObservableList<Question> getObservableList2() throws IOException {
		ObservableList<Question> answer = FXCollections.observableArrayList();

		try {
			System.out.println("Oprekking: " + soUrl);
			URL so = new URL(soUrl);
			URLConnection conn = so.openConnection();
			InputStream is = conn.getInputStream();
			GZIPInputStream gis = new GZIPInputStream(is);
			BufferedReader br = new BufferedReader(
					new InputStreamReader(
							gis
					)
			);
			String inputLine;
			System.out.println("Sblm baca BR");
			while ((inputLine = br.readLine()) != null) {
				JSONObject job = new JSONObject(inputLine);
				System.out.println("Terima: " + job.toString());
			}
			System.out.println("Stlh baca BR");
		} catch(Exception e) {

		}

		return answer;
	}
}

--#

--% F:/jualan/dahsyat/sfx/stackoverlow/src/main/resources/gaya.css
.table-row-cell {
	-fx-cell-size: 50px;
}

// https://stackoverflow.com/questions/39512621/change-javafx-tableview-font-size/39514062

.table-view .table-cell{
	-fx-font-weight:bold;
	-fx-font-size:18px;
	/* -fx-text-fill:orange; */
}

//Style of each column header in the tableView
.table-view .column-header {
	 -fx-background-color: transparent;
}

//Style of each column header's background in the tableView
.table-view .column-header-background{
	-fx-background-color: linear-gradient(#131313 0.0%, #424141 100.0%);
}

//Style of each entire row in the table view when is hovered
.table-row-cell:hover {
	-fx-background-color:orange;
}

//Style of each entire row in the table view when is getting focused
.table-row-cell:focused {
	-fx-background-color:purple;
}
--#

