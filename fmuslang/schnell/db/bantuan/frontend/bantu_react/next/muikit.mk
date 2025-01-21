
--% index/fm.us
__TEMPLATE_PROJECT_DIR__,d
  %utama=__FILE__
  %__TEMPLATE_SERVER_PORT__=9600
	__TEMPLATE_MTS_DIR__,d(/mk)
		# assets,d(/cpa=/home/usef/tmp/nextjs-material-kit/assets)
		components,d(/cpa=/home/usef/tmp/nextjs-material-kit/components)
		# layouts,d(/cpa=/home/usef/tmp/nextjs-material-kit/layouts)
		pages,d(/cpa=/home/usef/tmp/nextjs-material-kit/pages)
		pages-sections,d(/cpa=/home/usef/tmp/nextjs-material-kit/pages-sections)
		public,d(/cpa=/home/usef/tmp/nextjs-material-kit/public)
		styles,d(/cpa=/home/usef/tmp/nextjs-material-kit/styles)
		next.config.js,f(F=/home/usef/tmp/nextjs-material-kit/next.config.js)
		package.json,f(F=/home/usef/tmp/nextjs-material-kit/package.json)
		routes.js,f(F=/home/usef/tmp/nextjs-material-kit/routes.js)
		run.sh,f(e=utama=/run.sh)
		yarner.sh,f(e=utama=/yarner.sh)
		$*chmod a+x *.sh
		$*ln -s /home/usef/tmp/node_modules .
		$*qterminal 2>/dev/null &

--#

--% /yarner.sh
yarn install
--#

--% /run.sh
yarn dev -- -p __TEMPLATE_SERVER_PORT__
--#

--% rujukan
/home/usef/tmp/nextjs-material-kit/
--#
