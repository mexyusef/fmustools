--% program/fmus
__REPLACE_WITH_PROJECT_DIR_OR_INPUT__,d(/mk)
	%__TEMPLATE_TABLENAME=item
	%__TEMPLATE_SERVER_PORT__=9000
	%__TEMPLATE_URL_PREFIX=/api
__TEMPLATE_DB_INIT
__TEMPLATE_APP_INIT
	migrations,d(/mk)
__TEMPLATE_SERVER_APP_CONTENT
	fly.sh,f(e=__FILE__=flyway.sh)
	# $*chmod a+x *.sh
--#

--% flyway.sh
/home/usef/flyway-7.11.3/flyway -X -url=jdbc:postgresql://__TEMPLATE_DBHOST:__TEMPLATE_DBPORT/__TEMPLATE_DBNAME -user=__TEMPLATE_DBUSER -password=__TEMPLATE_DBPASS -locations=filesystem:./migrations -validateOnMigrate=false migrate
--#
