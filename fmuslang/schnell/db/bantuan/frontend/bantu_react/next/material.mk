
--% index/fm.us
__TEMPLATE_PROJECT_DIR__,d
  %utama=__FILE__
  %__TEMPLATE_SERVER_PORT__=9600
	__TEMPLATE_MTS_DIR__,d(/mk)
		assets,d(/cpa=/home/usef/tmp/nextjs-material-dashboard/assets)
		components,d(/cpa=/home/usef/tmp/nextjs-material-dashboard/components)
		layouts,d(/cpa=/home/usef/tmp/nextjs-material-dashboard/layouts)
		pages,d(/cpa=/home/usef/tmp/nextjs-material-dashboard/pages)
		variables,d(/cpa=/home/usef/tmp/nextjs-material-dashboard/variables)
		next.config.js,f(F=/home/usef/tmp/nextjs-material-dashboard/next.config.js)
		package.json,f(F=/home/usef/tmp/nextjs-material-dashboard/package.json)
		routes.js,f(F=/home/usef/tmp/nextjs-material-dashboard/routes.js)
		run.sh,f(e=utama=/run.sh)
		yarner.sh,f(e=utama=/yarner.sh)
		$*chmod a+x *.sh
		$*ln -s /home/usef/tmp/node_modules .
		$*qterminal 2>/dev/null &
	
--#

--% /yarn.adder.sh
next-compose-plugins
--#

--% /yarner.sh
yarn install
--#

--% /run.sh
yarn dev -- -p __TEMPLATE_SERVER_PORT__
--#

--% rujukan
/home/usef/tmp/nextjs-material-dashboard/
--#
