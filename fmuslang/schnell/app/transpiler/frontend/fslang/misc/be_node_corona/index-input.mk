--% index/fmus
be-node-corona,d(/mk)
  backend,d(/load=__FILE__=index_under_pwd*)
  frontend,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/misc/be_node_corona/react-corona.fmus=index/fmus*)
--#

--% index_under_pwd
.,d(/mk)
	%utama=__FILE__
	.env,f(e=utama=C:/tmp/hapus/nda01/.env)
	config.inc.php,f(e=utama=C:/tmp/hapus/nda01/config.inc.php)
	docker-compose.yml,f(e=utama=C:/tmp/hapus/nda01/docker-compose.yml)
	package.json,f(e=utama=C:/tmp/hapus/nda01/package.json)
	webpack-antd.js,f(e=utama=C:/tmp/hapus/nda01/webpack-antd.js)
	webpack-node-pg.js,f(e=utama=C:/tmp/hapus/nda01/webpack-node-pg.js)
	# $*ln -s /mnt/c/node_modules/node-antd-pg/node_modules .
	node-postgres,d(/mk)
		.babelrc,f(e=utama=C:/tmp/hapus/nda01/node-postgres/.babelrc)
		.eslintrc.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/.eslintrc.js)
		.gitignore,f(e=utama=C:/tmp/hapus/nda01/node-postgres/.gitignore)
		README.md,f(e=utama=C:/tmp/hapus/nda01/node-postgres/README.md)
		work.fmus,f(e=utama=C:/tmp/hapus/nda01/node-postgres/work.fmus)
		src,d(/mk)
			config.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/config.js)
			apps,d(/mk)
				index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/index.js)
				building,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/building/extender.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/building/models/index.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/building/models/postgres.js)
				corona,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/corona/extender.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/corona/models/index.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/corona/models/postgres.js)
				equipment,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/equipment/extender.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/equipment/models/index.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/equipment/models/postgres.js)
				floor,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/floor/extender.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/floor/models/index.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/floor/models/postgres.js)
				location,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/location/extender.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/location/models/index.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/location/models/postgres.js)
				measurement,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/measurement/extender.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/measurement/models/index.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/measurement/models/postgres.js)
				news,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/news/extender.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/news/models/index.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/news/models/postgres.js)
				point,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/point/extender.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/point/models/index.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/point/models/postgres.js)
				room,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/room/extender.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/room/models/index.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/room/models/postgres.js)
				sensor,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/sensor/extender.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/sensor/models/index.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/sensor/models/postgres.js)
				system,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/system/extender.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/system/models/index.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/system/models/postgres.js)
				todo,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/todo/extender.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/todo/models/index.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/todo/models/postgres.js)
				user,d(/mk)
					extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/user/extender.js)
					auth,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/user/auth/index.js)
						jwt.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/user/auth/jwt.js)
						kripto.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/user/auth/kripto.js)
						provider.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/user/auth/provider.js)
						token.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/user/auth/token.js)
						token_mongo.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/user/auth/token_mongo.js)
					models,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/user/models/index.js)
						mongo.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/user/models/mongo.js)
						postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/apps/user/models/postgres.js)
			core,d(/mk)
				app.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/app.js)
				crud-mongoose.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/crud-mongoose.js)
				crud.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/crud.js)
				extender.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/extender.js)
				db,d(/mk)
					index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/db/index.js)
					mongo.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/db/mongo.js)
					postgres.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/db/postgres.js)
				middlewares,d(/mk)
					auth.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/auth.js)
					body.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/body.js)
					cors.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/cors.js)
					index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/index.js)
					morgan.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/morgan.js)
					session.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/session.js)
					uploader.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/uploader.js)
				routes,d(/mk)
					index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/routes/index.js)
					api,d(/mk)
						auth.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/routes/api/auth.js)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/routes/api/index.js)
						users.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/routes/api/users.js)
					dummy,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/routes/dummy/index.js)
					extension,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/routes/extension/index.js)
					generic,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/core/routes/generic/index.js)
				utils,d(/mk)
			public,d(/mk)
			server,d(/mk)
				server-dev.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/server/server-dev.js)
				server-prod.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/src/server/server-prod.js)
		__mocks__,d(/mk)
			fileMock.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/__mocks__/fileMock.js)
			styleMock.js,f(e=utama=C:/tmp/hapus/nda01/node-postgres/__mocks__/styleMock.js)
	react-antd,d(/mk)
		.babelrc,f(e=utama=C:/tmp/hapus/nda01/react-antd/.babelrc)
		.env,f(e=utama=C:/tmp/hapus/nda01/react-antd/.env)
		.eslintrc.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/.eslintrc.js)
		config.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/config.js)
		index.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/index.css)
		index.html,f(e=utama=C:/tmp/hapus/nda01/react-antd/index.html)
		index.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/index.js)
		README.md,f(e=utama=C:/tmp/hapus/nda01/react-antd/README.md)
		assets,d(/mk)
			building.json,f(e=utama=C:/tmp/hapus/nda01/react-antd/assets/building.json)
			equipment.json,f(e=utama=C:/tmp/hapus/nda01/react-antd/assets/equipment.json)
			favicon.ico,f(b64=utama=C:/tmp/hapus/nda01/react-antd/assets/favicon.ico)
			floor.json,f(e=utama=C:/tmp/hapus/nda01/react-antd/assets/floor.json)
			location.json,f(e=utama=C:/tmp/hapus/nda01/react-antd/assets/location.json)
			measurement.json,f(e=utama=C:/tmp/hapus/nda01/react-antd/assets/measurement.json)
			menu.json,f(e=utama=C:/tmp/hapus/nda01/react-antd/assets/menu.json)
			news.json,f(e=utama=C:/tmp/hapus/nda01/react-antd/assets/news.json)
			point.json,f(e=utama=C:/tmp/hapus/nda01/react-antd/assets/point.json)
			room.json,f(e=utama=C:/tmp/hapus/nda01/react-antd/assets/room.json)
			sensor.json,f(e=utama=C:/tmp/hapus/nda01/react-antd/assets/sensor.json)
			system.json,f(e=utama=C:/tmp/hapus/nda01/react-antd/assets/system.json)
		components,d(/mk)
			App,d(/mk)
				index.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/App/index.js)
				style.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/App/style.css)
			common,d(/mk)
				BoModule,d(/mk)
					BoModule.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/common/BoModule/BoModule.css)
					BoModule.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/common/BoModule/BoModule.js)
				Table,d(/mk)
					SimpleTable.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/common/Table/SimpleTable.js)
				TabPage,d(/mk)
					index.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/common/TabPage/index.js)
					style.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/common/TabPage/style.css)
			context,d(/mk)
				SessionContext.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/context/SessionContext.js)
				SessionProvider.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/context/SessionProvider.js)
				ToolbarContext.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/context/ToolbarContext.js)
			Layout,d(/mk)
				BaseLayout.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Layout/BaseLayout.css)
				BaseLayout.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Layout/BaseLayout.js)
				Floating,d(/mk)
					index.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Layout/Floating/index.js)
					style.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Layout/Floating/style.css)
				Footer,d(/mk)
				Header,d(/mk)
					index.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Layout/Header/index.js)
					style.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Layout/Header/style.css)
				Sidebar,d(/mk)
					index.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Layout/Sidebar/index.js)
					style.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Layout/Sidebar/style.css)
			Login,d(/mk)
				index.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Login/index.js)
				login.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Login/login.css)
			Menu,d(/mk)
				index.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Menu/index.js)
				MainMenu.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Menu/MainMenu.css)
				MainMenu.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Menu/MainMenu.js)
				Shortcut.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Menu/Shortcut.js)
			modules,d(/mk)
				Building,d(/mk)
					Building.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Building/Building.js)
					CreateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Building/CreateForm.js)
					FormProvider.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Building/FormProvider.js)
					FormWrapper.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Building/FormWrapper.js)
					List.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Building/List.js)
					Modal.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Building/Modal.js)
					UpdateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Building/UpdateForm.js)
				Dashboard,d(/mk)
					capitals.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/capitals.js)
					charts_helper.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/charts_helper.js)
					chart_options.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/chart_options.js)
					Dashboard.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Dashboard.js)
					DashboardBizcharts.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/DashboardBizcharts.js)
					DashboardEcharts.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/DashboardEcharts.js)
					DashboardHicharts.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/DashboardHicharts.js)
					DashboardRecharts.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/DashboardRecharts.js)
					MyBar.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/MyBar.js)
					MyDonut.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/MyDonut.js)
					MyGauge.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/MyGauge.js)
					MyPie.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/MyPie.js)
					patterns.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/patterns.js)
					README.md,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/README.md)
					Speedy.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Speedy.js)
					useAxios.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/useAxios.js)
					GridMap,d(/mk)
						index.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/index.js)
						MapItem.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/MapItem.css)
						MapItem.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/MapItem.js)
						old-index.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/old-index.js)
						old-MapItem.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/old-MapItem.js)
						working-index.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/working-index.js)
						fs,d(/mk)
							fullscreen.png,f(b64=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/fs/fullscreen.png)
							fullscreen@2x.png,f(b64=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/fs/fullscreen@2x.png)
							leaflet.fullscreen.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/fs/leaflet.fullscreen.css)
							Leaflet.fullscreen.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/fs/Leaflet.fullscreen.js)
					Recharter,d(/mk)
						graph-types.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/graph-types.js)
						GraphBlock.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/GraphBlock.js)
						GridDashboard.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/GridDashboard.js)
						layoutConfig.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/layoutConfig.js)
						stateData.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/stateData.js)
						styles.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/styles.css)
						Title.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/Title.js)
						TypeItem.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/TypeItem.js)
				Equipment,d(/mk)
					CreateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/CreateForm.js)
					Equipment.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/Equipment.js)
					FormProvider.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/FormProvider.js)
					FormWrapper.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/FormWrapper.js)
					List.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/List.js)
					Modal.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/Modal.js)
					UpdateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/UpdateForm.js)
				Floor,d(/mk)
					CreateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Floor/CreateForm.js)
					Floor.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Floor/Floor.js)
					FormProvider.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Floor/FormProvider.js)
					FormWrapper.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Floor/FormWrapper.js)
					List.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Floor/List.js)
					Modal.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Floor/Modal.js)
					UpdateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Floor/UpdateForm.js)
				Location,d(/mk)
					CreateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Location/CreateForm.js)
					FormProvider.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Location/FormProvider.js)
					FormWrapper.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Location/FormWrapper.js)
					List.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Location/List.js)
					Location.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Location/Location.js)
					Modal.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Location/Modal.js)
					UpdateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Location/UpdateForm.js)
				Measurement,d(/mk)
					CreateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/CreateForm.js)
					FormProvider.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/FormProvider.js)
					FormWrapper.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/FormWrapper.js)
					List.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/List.js)
					Measurement.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/Measurement.js)
					Modal.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/Modal.js)
					UpdateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/UpdateForm.js)
				News,d(/mk)
					CreateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/News/CreateForm.js)
					FormProvider.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/News/FormProvider.js)
					FormWrapper.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/News/FormWrapper.js)
					List.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/News/List.js)
					Modal.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/News/Modal.js)
					News.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/News/News.js)
					UpdateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/News/UpdateForm.js)
				Point,d(/mk)
					CreateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Point/CreateForm.js)
					FormProvider.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Point/FormProvider.js)
					FormWrapper.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Point/FormWrapper.js)
					List.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Point/List.js)
					Modal.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Point/Modal.js)
					Point.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Point/Point.js)
					UpdateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Point/UpdateForm.js)
				Room,d(/mk)
					CreateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Room/CreateForm.js)
					FormProvider.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Room/FormProvider.js)
					FormWrapper.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Room/FormWrapper.js)
					List.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Room/List.js)
					Modal.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Room/Modal.js)
					Room.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Room/Room.js)
					UpdateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Room/UpdateForm.js)
				Sensor,d(/mk)
					CreateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/CreateForm.js)
					FormProvider.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/FormProvider.js)
					FormWrapper.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/FormWrapper.js)
					List.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/List.js)
					Modal.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/Modal.js)
					Sensor.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/Sensor.js)
					UpdateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/UpdateForm.js)
				System,d(/mk)
					CreateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/System/CreateForm.js)
					FormProvider.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/System/FormProvider.js)
					FormWrapper.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/System/FormWrapper.js)
					List.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/System/List.js)
					Modal.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/System/Modal.js)
					System.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/System/System.js)
					UpdateForm.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/modules/System/UpdateForm.js)
			Route,d(/mk)
				AuthenticatedRoute.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Route/AuthenticatedRoute.js)
				Routes.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Route/Routes.js)
			Setting,d(/mk)
				Settings_Popup.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/components/Setting/Settings_Popup.js)
		utils,d(/mk)
			authUtils.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/utils/authUtils.js)
			loader.css,f(e=utama=C:/tmp/hapus/nda01/react-antd/utils/loader.css)
			loader.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/utils/loader.js)
			requester.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/utils/requester.js)
			useAxios.js,f(e=utama=C:/tmp/hapus/nda01/react-antd/utils/useAxios.js)
--#

--% C:/tmp/hapus/nda01/.env
CHOKIDAR_USEPOLLING=true
HOST=localhost
PORT=9101
TIMEOUT=1000
#mongo or postgres
DB_CHOICE=postgres
DB_SCHEMA=public
DB_SYNC=1

SESSION_SECRET=K1nG.5up3rM4rk3t!
JWT_SECRET=Qu33n.5up3rM4rk3t!
NODE_ENV=development
# NODE_ENV=production

JWT_EXPIRED_SECONDS_PRODUCTION=10
# 3*60*60 = 3 jam
JWT_EXPIRED_SECONDS_DEVELOPMENT=10800
#JWT_EXPIRED_SECONDS_DEVELOPMENT=60

MONGO_DB=tempdb
MONGO_HOST=localhost
MONGO_PORT=5432
MONGO_USER=usef
MONGO_PASS=rahasia

POSTGRES_DB=tempdb
POSTGRES_USER=usef
POSTGRES_PASS=rahasia
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

--#

--% C:/tmp/hapus/nda01/config.inc.php
<?php

	/**
	 * Central phpPgAdmin configuration.  As a user you may modify the
	 * settings here for your particular configuration.
	 *
	 * $Id: config.inc.php-dist,v 1.55 2008/02/18 21:10:31 xzilla Exp $
	 */

	// An example server.  Create as many of these as you wish,
	// indexed from zero upwards.

	// Display name for the server on the login screen
	$conf['servers'][0]['desc'] = 'PostgreSQL';

	// Hostname or IP address for server.  Use '' for UNIX domain socket.
	// use 'localhost' for TCP/IP connection on this computer
	// $conf['servers'][0]['host'] = 'postgresql';
	$conf['servers'][0]['host'] = '172.21.37.176';

	// Database port on server (5432 is the PostgreSQL default)
	$conf['servers'][0]['port'] = 5432;

	// Database SSL mode
	// Possible options: disable, allow, prefer, require
	// To require SSL on older servers use option: legacy
	// To ignore the SSL mode, use option: unspecified
	$conf['servers'][0]['sslmode'] = 'allow';

	// Change the default database only if you cannot connect to template1.
	// For a PostgreSQL 8.1+ server, you can set this to 'postgres'.
	$conf['servers'][0]['defaultdb'] = 'template1';

	// Specify the path to the database dump utilities for this server.
	// You can set these to '' if no dumper is available.
	$conf['servers'][0]['pg_dump_path'] = '/opt/bitnami/postgresql/bin/pg_dump';
	$conf['servers'][0]['pg_dumpall_path'] = '/opt/bitnami/postgresql/bin/pg_dumpall';

	// Example for a second server (PostgreSQL for Windows)
	//$conf['servers'][1]['desc'] = 'Test Server';
	//$conf['servers'][1]['host'] = '127.0.0.1';
	//$conf['servers'][1]['port'] = 5432;
	//$conf['servers'][1]['sslmode'] = 'allow';
	//$conf['servers'][1]['defaultdb'] = 'template1';
	//$conf['servers'][1]['pg_dump_path'] = 'C:\\Program Files\\PostgreSQL\\8.0\\bin\\pg_dump.exe';
	//$conf['servers'][1]['pg_dumpall_path'] = 'C:\\Program Files\\PostgreSQL\\8.0\\bin\\pg_dumpall.exe';


	/* Groups definition */
	/* Groups allow administrators to logicaly group servers together under
	 * group nodes in the left browser tree
	 *
	 * The group '0' description
	 */
	//$conf['srv_groups'][0]['desc'] = 'group one';

	/* Add here servers indexes belonging to the group '0' separated by comma */
	//$conf['srv_groups'][0]['servers'] = '0,1,2';

	/* A server can belong to multi groups. Here server 1 is referenced in both
	 * 'group one' and 'group two'*/
	//$conf['srv_groups'][1]['desc'] = 'group two';
	//$conf['srv_groups'][1]['servers'] = '3,1';

	/* A group can be nested in one or more existing groups using the 'parents'
	 * parameter. Here the group 'group three' contains only one server and will
	 * appear as a subgroup in both 'group one' and 'group two':
	 */
	//$conf['srv_groups'][2]['desc'] = 'group three';
	//$conf['srv_groups'][2]['servers'] = '4';
	//$conf['srv_groups'][2]['parents'] = '0,1';

	/* Warning: Only groups with no parents appears at the root of the tree. */

	/* You can apply specific theme depending on servers, users and databases
	 * The priority order is :
	 *   * the theme defined for a server
	 *   * the theme defined for a database apply over the server one
	 *   * the theme defined for a user apply over the database one
	 */
	/* Example for servers */
	//$conf['servers'][0]['theme']['default'] = 'default';
	/* Example for users */
	//$conf['servers'][0]['theme']['user']['specific_user'] = 'default';
	/* Example for databases */
	//$conf['servers'][0]['theme']['db']['specific_db'] = 'default';

	// Default language. E.g.: 'english', 'polish', etc.  See lang/ directory
	// for all possibilities. If you specify 'auto' (the default) it will use
	// your browser preference.
	$conf['default_lang'] = 'auto';

	// AutoComplete uses AJAX interaction to list foreign key values
	// on insert fields. It currently only works on single column
	// foreign keys. You can choose one of the following values:
	// 'default on' enables AutoComplete and turns it on by default.
	// 'default off' enables AutoComplete but turns it off by default.
	// 'disable' disables AutoComplete.
	$conf['autocomplete'] = 'default on';

	// If extra login security is true, then logins via phpPgAdmin with no
	// password or certain usernames (pgsql, postgres, root, administrator)
	// will be denied. Only set this false once you have read the FAQ and
	// understand how to change PostgreSQL's pg_hba.conf to enable
	// passworded local connections.
	$conf['extra_login_security'] = false;

	// Only show owned databases?
	// Note: This will simply hide other databases in the list - this does
	// not in any way prevent your users from seeing other database by
	// other means. (e.g. Run 'SELECT * FROM pg_database' in the SQL area.)
	$conf['owned_only'] = false;

	// Display comments on objects?  Comments are a good way of documenting
	// a database, but they do take up space in the interface.
	$conf['show_comments'] = true;

	// Display "advanced" objects? Setting this to true will show
	// aggregates, types, operators, operator classes, conversions,
	// languages and casts in phpPgAdmin. These objects are rarely
	// administered and can clutter the interface.
	$conf['show_advanced'] = false;

	// Display "system" objects?
	$conf['show_system'] = false;

	// Minimum length users can set their password to.
	$conf['min_password_length'] = 1;

	// Width of the left frame in pixels (object browser)
	$conf['left_width'] = 200;

	// Which look & feel theme to use
	$conf['theme'] = 'default';

	// Show OIDs when browsing tables?
	// Only supported in versions <=11
	$conf['show_oids'] = false;

	// Max rows to show on a page when browsing record sets
	$conf['max_rows'] = 30;

	// Max chars of each field to display by default in browse mode
	$conf['max_chars'] = 50;

	// Send XHTML strict headers?
	$conf['use_xhtml_strict'] = false;

	// Base URL for PostgreSQL documentation.
	// '%s', if present, will be replaced with the PostgreSQL version
	// (e.g. 8.4 )
	$conf['help_base'] = 'http://www.postgresql.org/docs/%s/interactive/';

	// Configuration for ajax scripts
	// Time in seconds. If set to 0, refreshing data using ajax will be disabled (locks and activity pages)
	$conf['ajax_refresh'] = 3;

	/** Plugins management
	 * Add plugin names to the following array to activate them
	 * Example:
	 *   $conf['plugins'] = array(
	 *     'Example',
	 *     'Slony'
	 *   );
	 */
	$conf['plugins'] = array();

	/*****************************************
	 * Don't modify anything below this line *
	 *****************************************/

	$conf['version'] = 19;

?>

--#

--% C:/tmp/hapus/nda01/docker-compose.yml
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

--% C:/tmp/hapus/nda01/package.json
{
  "name": "np",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "scripts": {
    "test": "jest",
    "coverage": "jest --coverage",
    "antd": "webpack serve --mode development --config webpack-antd",
    "client": "webpack serve --mode development --config webpack-antd --open",
    "buildServer": "rm -rf dist && webpack --mode development --config webpack-node-pg",
    "server": "npm run buildServer && npm run start",
    "mulai": "npm run buildServer && npm run start",
    "go": "npm run buildServer && npm run start",
    "start": "node ./dist/server.js"
  },
  "dependencies": {
    "antd": "^4.15.5",
    "axios": "^0.21.1",
    "bcrypt": "^5.0.1",
    "bizcharts": "^4.1.15",
    "echarts": "^5.2.2",
    "echarts-for-react": "^3.0.2",
    "express": "^4.17.1",
    "font-awesome": "^4.7.0",
    "highcharts": "^9.3.2",
    "highcharts-react-official": "^3.1.0",
    "jsonwebtoken": "^8.5.1",
    "leaflet": "^1.7.1",
    "leaflet-geosearch": "^3.6.0",
    "leaflet-search": "^3.0.2",
    "leaflet.locatecontrol": "^0.76.0",
    "mongoose": "^5.12.9",
    "mongoose-unique-validator": "^2.0.3",
    "passport": "^0.5.2",
    "passport-facebook": "^3.0.0",
    "passport-github2": "^0.1.12",
    "passport-google-oauth20": "^2.0.0",
    "passport-local": "^1.0.0",
    "passport-twitter": "^1.0.4",
    "pg": "^8.6.0",
    "pg-hstore": "^2.3.3",
    "pubsub-js": "^1.9.3",
    "puppeteer": "^13.0.0",
    "rand-token": "^1.0.1",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-full-screen": "^1.1.0",
    "react-fullscreen-crossbrowser": "^1.1.0",
    "react-grid-layout": "^1.3.0",
    "react-hot-loader": "^4.13.0",
    "react-leaflet": "^3.2.3",
    "react-leaflet-search": "^2.0.1",
    "react-loader-spinner": "^4.0.0",
    "react-router-dom": "^5.2.0",
    "recharts": "^2.1.8",
    "uid-generator": "^2.0.0"
  },
  "devDependencies": {
    "@babel/core": "^7.14.2",
    "@babel/plugin-proposal-class-properties": "^7.13.0",
    "@babel/plugin-transform-runtime": "^7.14.2",
    "@babel/preset-env": "^7.14.2",
    "@babel/preset-react": "^7.13.13",
    "@babel/runtime": "^7.14.0",
    "@webpack-cli/serve": "^1.4.0",
    "babel-core": "^6.26.3",
    "babel-eslint": "^10.1.0",
    "babel-jest": "^26.6.3",
    "babel-loader": "^8.2.2",
    "babel-plugin-transform-runtime": "^6.23.0",
    "babel-polyfill": "^6.26.0",
    "cors": "^2.8.5",
    "css-loader": "^5.2.4",
    "dotenv": "^9.0.2",
    "dotenv-webpack": "^7.0.2",
    "eslint": "^7.26.0",
    "eslint-loader": "^4.0.2",
    "express-fileupload": "^1.2.1",
    "express-session": "^1.17.1",
    "file-loader": "^6.2.0",
    "fs": "^0.0.1-security",
    "helmet": "^4.6.0",
    "html-loader": "^2.1.2",
    "html-webpack-plugin": "^5.3.1",
    "jest": "^26.6.3",
    "mini-css-extract-plugin": "^1.6.0",
    "morgan": "^1.10.0",
    "optimize-css-assets-webpack-plugin": "^5.0.4",
    "sequelize": "^6.12.1",
    "sequelize-cli": "^6.3.0",
    "style-loader": "^2.0.0",
    "uglifyjs-webpack-plugin": "^2.2.0",
    "url-loader": "^4.1.1",
    "webpack": "^5.37.0",
    "webpack-cli": "^4.7.0",
    "webpack-dev-middleware": "^4.2.0",
    "webpack-dev-server": "^3.11.2",
    "webpack-hot-middleware": "^2.25.0",
    "webpack-node-externals": "^3.0.0"
  }
}

--#

--% C:/tmp/hapus/nda01/webpack-antd.js
const path = require('path');
const webpack = require('webpack');
const HtmlWebPackPlugin = require('html-webpack-plugin');
// const Dotenv = require('dotenv-webpack');

const sourcedir = 'react-antd'

module.exports = {
  entry: {
    main: [
      // 'babel-polyfill',
      // 'webpack-hot-middleware/client?path=/__webpack_hmr&timeout=20000', 
      // './src/index.js',
      `./${sourcedir}/index.js`
    ]
  },
  output: {
    path: path.join(__dirname, 'dist'),
    publicPath: '/',
    filename: '[name].js'
  },

  mode: 'development',
  // https://stackoverflow.com/questions/51946848/webpack-nodejs-module-not-found-error-cant-resolve-fs
  target: 'web',
  // target: 'node',

  // configuration.devtool should match pattern "^(inline-|hidden-|eval-)?(nosources-)?(cheap-(module-)?)?source-map$"
  // devtool: '#source-map',

  devServer: {
    contentBase: path.resolve(process.cwd(), 'dist'),
    hot: true,
    host: '0.0.0.0',
    port: 9001,
    historyApiFallback: true,
  },

  module: {
    rules: [
      {
        enforce: "pre",
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "eslint-loader",
        options: {
          emitWarning: true,
          failOnError: false,
          failOnWarning: false
        }
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: "babel-loader",
      },
      {
        // Loads the javacript into html template provided.
        // Entry point is set below in HtmlWebPackPlugin in Plugins 
        test: /\.html$/,
        use: [
          {
            loader: "html-loader",
            //options: { minimize: true }
          }
        ]
      },
      { 
        test: /\.css$/,
        use: [ 'style-loader', 'css-loader' ]
      },

      {
        test: /\.(ico|eot|svg|otf|ttf|woff|woff2)$/,
        use: 'file-loader',
      },

      {
       test: /\.(png|svg|jpg|gif)$/,
       use: ['file-loader']
      }

    ]
  },

  resolve: {
    modules: [sourcedir, 'node_modules'],
    extensions: ['.js'],
    alias: {
      '@': path.resolve(process.cwd(), sourcedir, 'components'),
      'assets': path.resolve(process.cwd(), sourcedir, 'assets'),
      'modules': path.resolve(process.cwd(), sourcedir, 'components', 'modules'),
      'context': path.resolve(process.cwd(), sourcedir, 'components', 'context'),
      'common': path.resolve(process.cwd(), sourcedir, 'components', 'common'),
      'utils': path.resolve(process.cwd(), sourcedir, 'utils'),
      '#': path.resolve(process.cwd(), sourcedir),
    },
  },

  plugins: [
    // https://stackoverflow.com/questions/41359504/webpack-bundle-js-uncaught-referenceerror-process-is-not-defined
    new webpack.ProvidePlugin({
      process: 'process/browser',
    }),
    new HtmlWebPackPlugin({
      template: path.resolve(process.cwd(), sourcedir, 'index.html'),
      filename: "./index.html",
      favicon: path.resolve(process.cwd(), sourcedir, 'assets', 'favicon.ico'),
      // excludeChunks: [ 'server' ]
    }),
    // new Dotenv(),
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin()
  ],
}


--#

--% C:/tmp/hapus/nda01/webpack-node-pg.js

const path = require('path');
const webpack = require('webpack');
const nodeExternals = require('webpack-node-externals');


const sourcedir = 'node-postgres/src'

module.exports = (env = undefined, argv = {mode: 'development'}) => {
  const SERVER_PATH = (argv.mode === 'production') ?
    `./${sourcedir}/server/server-prod.js` :
    `./${sourcedir}/server/server-dev.js`

  return ({
    entry: {
      server: SERVER_PATH,
    },
    output: {
      path: path.join(__dirname, 'dist'),
      publicPath: '/',
      filename: '[name].js'
    },
    mode: argv.mode,

    target: 'node',

    node: {
      // Need this when working with express, otherwise the build fails
      __dirname: false,   // if you don't put this is, __dirname
      __filename: false,  // and __filename return blank or /
    },
    externals: [nodeExternals()], // Need this to avoid error when working with Express

    resolve: {
      modules: [sourcedir, 'node_modules'],
      extensions: ['.js'],
      alias: {
        S: path.resolve(process.cwd(), sourcedir),
        C: path.resolve(process.cwd(), sourcedir, 'core'),
        A: path.resolve(process.cwd(), sourcedir, 'apps'),
        AU: path.resolve(process.cwd(), sourcedir, 'apps/user'),
        D: path.resolve(process.cwd(), sourcedir, 'core/db'),
        M: path.resolve(process.cwd(), sourcedir, 'core/middlewares'),
        R: path.resolve(process.cwd(), sourcedir, 'core/routes'),
        U: path.resolve(process.cwd(), sourcedir, 'core/utils'),
      },
    },

    module: {
      rules: [
        // {
        //   enforce: "pre",
        //   test: /\.js$/,
        //   exclude: /node_modules/,
        //   loader: "eslint-loader",
        //   options: {
        //     emitWarning: true,
        //     failOnError: false,
        //     failOnWarning: false
        //   }
        // },
        {
          // Transpiles ES6-8 into ES5
          test: /\.js$/,
          exclude: /node_modules/,
          use: {
            loader: "babel-loader"
          }
        },
        {
          // Loads the javacript into html template provided.
          // Entry point is set below in HtmlWebPackPlugin in Plugins 
          test: /\.html$/,
          use: [
            {
              loader: "html-loader",
              //options: { minimize: true }
            }
          ]
        },
        { 
          test: /\.css$/,
          use: [ 'style-loader', 'css-loader' ]
        },
        {
         test: /\.(png|svg|jpg|gif)$/,
         use: ['file-loader']
        }
      ]
    },

    plugins: [
      new webpack.HotModuleReplacementPlugin(),
      new webpack.NoEmitOnErrorsPlugin()
    ],

  })
}



--#

--% C:/tmp/hapus/nda01/node-postgres/.babelrc
{
  "presets": [
    "@babel/preset-env"
  ],
  "plugins": [
    ["@babel/transform-runtime"]
  ]
}


--#

--% C:/tmp/hapus/nda01/node-postgres/.eslintrc.js
module.exports = {
  "extends": [
    "eslint:recommended",
  ],
  "parser": "babel-eslint",
  "rules": {
    "no-unused-vars": "off",
    "no-undef": "off",
    "no-console": "off",
    "no-empty": "off",
  }
};



--#

--% C:/tmp/hapus/nda01/node-postgres/.gitignore
node_modules
.DS_Store
dist

Coverage
coverage


--#

--% C:/tmp/hapus/nda01/node-postgres/README.md
TODO:

0) yarn add sequelize sequelize-cli
1)
npx sequelize init
config/config.json:
{
  "development": {
    "username": "usef",
    "password": "rahasia",
    "database": "hapuslah",
    "host": "localhost",
    "port": 9022,
    "dialect": "postgresql"
  },
  "test": {
    "username": "usef",
    "password": "rahasia",
    "database": "hapuslah",
    "host": "localhost",
    "port": 9022,
    "dialect": "postgresql"
  },
  "production": {
    "username": "usef",
    "password": "rahasia",
    "database": "hapuslah",
    "host": "localhost",
    "port": 9022,
    "dialect": "postgresql"
  }
}

2)
npx sequelize-cli seed:generate --name <nama model sesuai nama database biar enak>
npx sequelize-cli seed:generate --name __NAMATABLE__

3)
gunakan:
createdAt: new Date(),
updatedAt: new Date()

modify dg content:
'use strict';

module.exports = {
  up: async (queryInterface, Sequelize) => {
    await queryInterface.bulkInsert(
      '__NAMATABLE__', 
      [
        {
          name: 'John Doe',
          rating: 2,
          comment: 'sebuah text comment',
        },
      ],
      {}
    );
  },
  down: async (queryInterface, Sequelize) => {
  }
};
4) run migration
npx sequelize-cli db:seed:all

# create table manual
docker exec -it pg psql -U usef insurance_development -c "create table insurances(id serial primary key,coverage varchar(255),government boolean);"

# select/check table
docker exec -it pg psql -U usef insurance_development -c "select * from insurances;"
docker exec -it pg psql -U usef insurance_development -c "SELECT id, coverage, government FROM insurances AS insurances;"

switching postgres <-> mongo

  apps/index.js
    comment out "khusus mongo"

  apps/user/models/index.js
    ganti import

  apps/task/models/index.js
    ganti import

  core/db/index.js
    ganti import

  core/routes/generic/index.js
    ganti import
      import Cruder from 'C/crud';
      // import Cruder from 'C/crud-mongoose';

  apps/user/auth/jwt.js
    ganti import
      import Token from './token';
      // import Token from './token_mongo';

  apps/user/auth/provider
    mungkin logic nya hrs diubah, ngikutin node ecommerce???


--#

--% C:/tmp/hapus/nda01/node-postgres/work.fmus
ganti password

/api/users/update_password

*~localhost:9000/items p json {user=name}
*~localhost:9001/rest/books p raw <{allBooks{isn;title}}>
*~localhost:9222/users/update_password p json {identitas=Wiranto,password=rahasia}

*~localhost:9222/users/update_password p json {identitas=Wiranto,password=rahasia}

    const {
      email,
      password
    } = await req.body;

http://172.23.28.134:9101/login

*~172.23.28.134:9101/api/users/update_password p json {email=gaia@gmail.com,password=rahasia}

{"id":2,"email":"gaia@gmail.com","password":"$2b$10$LOLYLNWAPgC54mOBUCVcf.ph7ixFG32i6/ltqyZDEH2HtGYNXTsN2"}

    id_user: {
      type: INTEGER,
      allowNull: false
    },
    refresh_expired_time: {
      type: 'TIMESTAMP',
      allowNull: false
    },
    refresh_token: {
      type: STRING,
      allowNull: false
    }, 
create table tokens(id_user INTEGER NOT NULL,refresh_expired_time DATE,refresh_token VARCHAR(500));

tempdb=# create table tokens(id_user INTEGER NOT NULL,refresh_expired_time DATE,refresh_token VARCHAR(500));
CREATE TABLE

--#

--% C:/tmp/hapus/nda01/node-postgres/src/config.js
module.exports = {
  secret: process.env.NODE_ENV === 'production' 
  ? process.env.JWT_SECRET 
  : 'jangan tatap mataku'
};

--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/index.js

import Sensor from './sensor/models';
import System from './system/models';
import Measurement from './measurement/models';
import Equipment from './equipment/models';
import Room from './room/models';
import Floor from './floor/models';
import Location from './location/models';
import Point from './point/models';
import Building from './building/models';
import News from './news/models';
import User from './user/models';
import ExtenderSensor from './sensor/extender.js';
import ExtenderSystem from './system/extender.js';
import ExtenderMeasurement from './measurement/extender.js';
import ExtenderEquipment from './equipment/extender.js';
import ExtenderRoom from './room/extender.js';
import ExtenderFloor from './floor/extender.js';
import ExtenderLocation from './location/extender.js';
import ExtenderPoint from './point/extender.js';
import ExtenderBuilding from './building/extender.js';
import ExtenderNews from './news/extender.js';
import ExtenderUser from './user/extender.js';

import Corona from './corona/models';
import Todo from './todo/models';
import ExtenderCorona from './corona/extender.js';
import ExtenderTodo from './todo/extender.js';

// khusus mongo
// dummy utk aktivasi mongo connect = Log
// import dbConnect from 'D';
// export const LogModel = dbConnect.model("Log", new dbConnect.Schema({ content: String, },));

const AppModels = {
  base: {
    'sensor': Sensor,
    'system': System,
    'measurement': Measurement,
    'equipment': Equipment,
    'room': Room,
    'floor': Floor,
    'location': Location,
    'point': Point,
    'building': Building,
    'news': News,
    'user': User,
    'corona': Corona,
    'todo': Todo,
  },
  extenders: [    
    ExtenderSensor,
    ExtenderSystem,
    ExtenderMeasurement,
    ExtenderEquipment,
    ExtenderRoom,
    ExtenderFloor,
    ExtenderLocation,
    ExtenderPoint,
    ExtenderBuilding,
    ExtenderNews,
    ExtenderUser,
    ExtenderCorona,
    ExtenderTodo,
  ]
};

export default AppModels;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/building/extender.js

const ExtensionRouter = Router => Router
  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  // .post("/current-admin", ExtenderObj.currentUser)
  // .post("/api/users/login", AuthProvider.login)
  // .post("/api/users/register", AuthProvider.register)
  // .post("/api/users/update_password", AuthProvider.updatePassword)
  ;
export default ExtensionRouter;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/building/models/index.js

// import Building from './mongo';
import Building from './postgres';

export default Building;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/building/models/postgres.js
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = 'buildings';

const fieldsMap = {
    id: { type: INTEGER, primaryKey: true },
    name: { type: STRING, maxlength: [255, "Value too Long"] },
    building_id: { type: STRING, maxlength: [255, "Value too Long"] },
    location_text: { type: STRING, maxlength: [500, "Value too Long"] },
    lalo: DECIMAL,
    description: { type: STRING, maxlength: [500, "Value too Long"] },
    notes: { type: STRING, maxlength: [1000, "Value too Long"] }
	};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const Building = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default Building;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/corona/extender.js
// import Sequelize from 'sequelize';
import puppeteer from 'puppeteer';
import Corona from './models';
import { checkAuthToken } from '../../core/middlewares/auth';


const newload = async ({params: {country}}, res) => {

  const alamat = `https://www.worldometers.info/coronavirus/country/${country}/`;

  puppeteer.launch({
    headless: true,
  })
  .then(async browser => {

    const page = await browser.newPage();
    await page.goto(alamat);
    await page.waitForSelector('body');

    console.log(`
      siap2 evaluate! ${alamat}
    `);

    var kembalian = await page.evaluate(() => {

      // get first date
      let first_date = document.body.querySelector(`div.news_date`);      
      let first_date_string = undefined;
      let tanggals = [];
      const gmt_killer = '00:00:00 GMT';

      if (first_date !== null) {
        // January 2 etc
        first_date_string = first_date.innerText + `, 2022 ${gmt_killer}`;
        let tanggal_pertama = new Date ( Date.parse(first_date_string) );

        tanggals = Array.from({length:7}, (_,idx) => {
          let tgl = new Date();
          tgl.setDate(tanggal_pertama.getDate()-idx);
          return tgl.toLocaleDateString();
        });

      }

      // let today = new Date();
      // today = new Date(today.setMinutes(today.getMinutes() - today.getTimezoneOffset()));
      // let tahun = today.getFullYear();
      // let bulan = today.getMonth() + 1;
      // let tanggal = today.getDate();
      // let hari_ini_adakah = document.body.querySelector(`#newsdate${tahun}-${bulan}-${tanggal}`);

      // Array.from hasilkan tanggal dari sekarang turun ke 7 hari lalu
      // maka tanggal terbaru punya id lebih kecil dari hari2 sampai 7 hr lalu
      // jk kita query dg sort id DESC maka peroleh yesterdays dulu dari 7hrll di awal, baru terakhir today
      // if (hari_ini_adakah === null) {
      //   // mulai dari kemarin, krn tanggal skrg belum ada
      //   tanggals = Array.from({length:7}, (_,idx) => {
      //     let tgl = new Date();
      //     tgl = new Date(tgl.setMinutes(tgl.getMinutes() - tgl.getTimezoneOffset()));
      //     // tgl.setDate(tgl.getDate()-idx-1);
      //     tgl.setDate(tgl.getDate()-idx);
      //     // tgl.setDate(tgl.getDate()-6+idx);
      //     return tgl.toLocaleDateString();
      //   });
      // } else {
      //   // mulai dari hari ini
      //   tanggals = Array.from({length:7}, (_,idx) => {
      //     let tgl = new Date();
      //     tgl = new Date(tgl.setMinutes(tgl.getMinutes() - tgl.getTimezoneOffset()));
      //     // tgl.setDate(tgl.getDate()-idx);
      //     tgl.setDate(tgl.getDate()-idx+1);
      //     // tgl.setDate(tgl.getDate()-6+1+idx);
      //     return tgl.toLocaleDateString();
      //   });
      // }


      let posts = document.body.querySelectorAll('.news_body');
      let maincounter = document.body.querySelectorAll('.maincounter-number');
      
      console.log(`
        temukan news_body di page?
        [${JSON.stringify(posts)}]
      `);

      let createItems = [];

      posts.forEach((item, index) => {
        let totalcases=0, totaldeaths=0, totalrecovered=0, istoday=false;
        if (index === 0) {
          totalcases = maincounter[0].innerText.replace(/,/g,'').trim();
          totaldeaths = maincounter[1].innerText.replace(/,/g,'').trim();
          totalrecovered = maincounter[2].innerText.replace(/,/g,'').trim();
          istoday = true;
        }
        let content = item.querySelector('.news_li').innerText;
        // 136 new cases and 8 new deaths
        let result =/([,\d]+) new cases and ([,\d]+) new deaths/. exec(content);
        if (result === null) {
          // '  3,957 new cases in Australia [source] [source] [source] [source] [source]'
          result = /([,\d]+) new cases/. exec(content);
          if (result === null) {
            result = [0,0]; // 0 cases, 0 deaths
          } else {
            result[1] = Number(String(result[1]).replace(/,/g,'').trim());
            result[2] = 0; // 0 deaths
          }
        } else {
          result[1] = Number(String(result[1]).replace(/,/g,'').trim());
          result[2] = Number(String(result[2]).replace(/,/g,'').trim());
        }
        createItems.push({
          cases: result[1], // spy postgres gak complain koma di angka
          deaths: result[2],
          date: tanggals[index],
          totalcases,
          totaldeaths,
          totalrecovered,
          istoday,
        });  
      });
      var items = { "posts": createItems };
      return items;
    });

    await browser.close();

    console.log(`stlh page evaluate yg mungkin gagal:`, kembalian);
    let terbangun = [];
    kembalian.posts.forEach((item, index) => {
      /**
        cek jk found where dimana date sama, maka update
        https://stackoverflow.com/questions/18304504/create-or-update-sequelize/41248216
       */
      const gmt_killer = '00:00:00 GMT';
      const data = {
        country,
        cases: item.cases,
        deaths: item.deaths,
        totalcases: item.totalcases,
        totaldeaths: item.totaldeaths,
        totalrecovered: item.totalrecovered,
        date: item.date + `, ${gmt_killer}`, // agar gak korting tanggal via waktu
        istoday: item.istoday,
      };
      const object = Corona.build(data);        
      console.log(`terbangun object build dg (cek tanggal di source dan hasil):
      source = ${JSON.stringify(data)}
      hasil = ${JSON.stringify(object)}
      jenis hasil = ${typeof object}
      `);
      
      terbangun.push(object)
    });

    console.log(`
      telah build, tinggal save sebanyak: ${terbangun.length}
    `);

    terbangun.forEach(async (item, index) => {
      console.log(`terbangun object save ${index} of ${terbangun.length}`);
      try {
        // await item.save();
        const ada = await Corona.findOne({
          order: [
            ['id', 'DESC'],
          ],
          where: {
            date: item.date,
            country: item.country,
          }
        });

        // delete item['id'];
        let tanpa_id = Object.fromEntries(Object.entries(item.dataValues).filter(([k, v]) => k !== 'id'));
        console.log(`antara update atau create: ${ada}
        ***********************************************
        item utk update/create, dg id: ${JSON.stringify(item)}
        ***********************************************
        item utk update/create, tanpa id: ${JSON.stringify(tanpa_id)}
        ***********************************************
        `);
        if (ada !== null) {            
          // const hasilupdate = await ada.update(item, {
          // https://stackoverflow.com/questions/38524938/sequelize-update-record-and-return-result
          const hasilupdate = await Corona.update(tanpa_id, {
            where: {
              date: item.date,
              country: item.country,
            },
            returning:true,
          });
          console.log(`updating...hasilnya adlh: ${JSON.stringify(hasilupdate)}`);
        } else {
          console.log(`creating...`);
          await item.save();
        }
      } catch (err) {
        console.log(`gagal pada ${index} => ${JSON.stringify(err)}
        `);
      }  
    });

    console.log(`
      corona #4: END.
    `);

    // res.json({'status': 'ok'});
    res.json(kembalian);
  
  }).catch(function(error) {
    console.error(error);
    res.json({'status': 'error'});
  });
  
}

const seven_day_data = async (req, res) => {
  const negara = req.params.country || 'indonesia';
  try {
    const options = {
      // utk latest 7 pentingkan id dulu
      // utk latest 1 pentingkan date dulu
      order: [
        ['date', 'DESC'], // butuh tanggal 1 duluan, tp ini dapat tanggal besar duluan, nanti kita reverse
        // ['date', 'ASC'],
        ['id', 'DESC'],
      ],
      limit: 7,
      where: {
        country: negara,
      }
    }
    const data = await Corona.findAll(options);
    
    console.log(`
      operasi "tujuh"
      opsi: ${options}
      hasil sblm reverse: 
      ${JSON.stringify(data, null, 2)}
    `);

    return res.json({
      result: data.reverse(),
      // total,
    });
  } catch(err) {
    console.error(err);
    res.json({'status': 'error'});
  }
}

const bernegara = async (negara) => {
  const options = {
    order: [ ['date', 'DESC'], ['id', 'DESC'], ],
    limit: 7,
    where: { country: negara, }
  }
  const data = await Corona.findAll(options);
  console.log(`bernegara: 
    ${negara} => ${data}`);
  return data.reverse();
}

const seven_day_data_several = async (req, res) => {
  
  // negaras = indonesia,australia
  let negaras_string = req.params.countries || 'indonesia';
  // // let negaras = (req.params.countries || 'indonesia').split(',').map(s=>s.trim());
  // negaras = negaras.split(',').map(s=>s.trim());
  let negaras = negaras_string.split(',').map(s=>s.trim());
  // let negaras = req.params.countries.split(',');
  console.log(`
    seven_day_data_several

    ini teh naon sih:
    ${typeof (negaras_string.split(',').map(s=>s.trim()))}

    request params: ${JSON.stringify(req.params)} 
    request params countries: ${req.params.countries} bertipe ${typeof req.params.countries}
    negaras: ${negaras} bertipe ${typeof negaras}, ${Array.isArray(negaras)}
  `);
  
  try {
    // negaras.forEach(async (negara) => {
    //   const options = {
    //     order: [ ['date', 'DESC'], ['id', 'DESC'], ],
    //     limit: 7,
    //     where: { country: negara, }
    //   }
    //   const data = await Corona.findAll(options);
    //   console.log(`${negara} => ${data}`);
    //   result.push (data.reverse());
    // });

    let result = await Promise.all( negaras.map(async (negara, index) => {
        const options = {
          order: [ ['date', 'DESC'], ['id', 'DESC'], ],
          limit: 7,
          where: { country: negara, }
        }
        const data = await Corona.findAll(options);
        console.log(`${negara} => ${data}`);
        return data.reverse();
      })
    );


    // negaras.forEach(async (negara) => {
    //   const options = {
    //     order: [ ['date', 'DESC'], ['id', 'DESC'], ],
    //     limit: 7,
    //     where: { country: negara, }
    //   }
    //   const data = await Corona.findAll(options);
    //   console.log(`${negara} => ${data}`);
    //   result.push (data.reverse());
    // });

    console.log(`
      hasil:
      ${JSON.stringify(result, null, 2)}
    `);

    return res.json({
      result
    });
  } catch(err) {
    console.error(err);
    res.json({'status': 'error'});
  }
}

const Extender = () => ({

  /**
   * 
   * @param {*} req 
   * @param {*} res 
   * @returns
   * 
   * {"result":
   * {"id":20,"country":"indonesia","cases":204,"deaths":5,"totalcases":4261412,"totaldeaths":144047,"totalrecovered":4112706,"date":"2021-12-23","istoday":true}
   * } 
   */
  today: async (req, res) => {
    const negara = req.params.country || 'indonesia';
    try {
      const options = {
        order: [
          ['date', 'DESC'],
          ['id', 'DESC'],
        ],
        where: {
          istoday: true,
          country: negara,
        },
        // limit: 1,
      }
      const data = await Corona.findOne(options);
      
      console.log(`
        today operation:
        opsi findOne: ${JSON.stringify(options)}
        hasil: ${JSON.stringify(data)}
      `);

      return res.json({
        result: data,
        // total,
      });
    } catch(err) {
      console.error(err);
      res.json({'status': 'error'});
    }
  },

  tujuh: seven_day_data,
  tujuhs: seven_day_data_several,
  load: newload,

  old_load: async ({params: {country}}, res) => {

    const alamat = `https://www.worldometers.info/coronavirus/country/${country}/`;

    puppeteer.launch({
      headless: true,
    })
    .then(async browser => {

      const page = await browser.newPage();
      await page.goto(alamat);
      await page.waitForSelector('body');

      console.log(`
        siap2 evaluate! ${alamat}
      `);

      var kembalian = await page.evaluate(() => {
        let today = new Date();
        today = new Date(today.setMinutes(today.getMinutes() - today.getTimezoneOffset()));
        let tahun = today.getFullYear();
        let bulan = today.getMonth() + 1;
        let tanggal = today.getDate();
        let hari_ini_adakah = document.body.querySelector(`#newsdate${tahun}-${bulan}-${tanggal}`);
        let tanggals = [];
        // Array.from hasilkan tanggal dari sekarang turun ke 7 hari lalu
        // maka tanggal terbaru punya id lebih kecil dari hari2 sampai 7 hr lalu
        // jk kita query dg sort id DESC maka peroleh yesterdays dulu dari 7hrll di awal, baru terakhir today
        if (hari_ini_adakah === null) {
          // mulai dari kemarin, krn tanggal skrg belum ada
          tanggals = Array.from({length:7}, (_,idx) => {
            let tgl = new Date();
            tgl = new Date(tgl.setMinutes(tgl.getMinutes() - tgl.getTimezoneOffset()));
            // tgl.setDate(tgl.getDate()-idx-1);
            tgl.setDate(tgl.getDate()-idx);
            // tgl.setDate(tgl.getDate()-6+idx);
            return tgl.toLocaleDateString();
          });
        } else {
          // mulai dari hari ini
          tanggals = Array.from({length:7}, (_,idx) => {
            let tgl = new Date();
            tgl = new Date(tgl.setMinutes(tgl.getMinutes() - tgl.getTimezoneOffset()));
            // tgl.setDate(tgl.getDate()-idx);
            tgl.setDate(tgl.getDate()-idx+1);
            // tgl.setDate(tgl.getDate()-6+1+idx);
            return tgl.toLocaleDateString();
          });
        }
        let posts = document.body.querySelectorAll('.news_body');
        let maincounter = document.body.querySelectorAll('.maincounter-number');
        
        console.log(`
          temukan news_body di page?
          [${JSON.stringify(posts)}]
        `);

        createItems = [];
        posts.forEach((item, index) => {
          let totalcases=0, totaldeaths=0, totalrecovered=0, istoday=false;
          if (index === 0) {
            totalcases = maincounter[0].innerText.replace(/,/g,'').trim();
            totaldeaths = maincounter[1].innerText.replace(/,/g,'').trim();
            totalrecovered = maincounter[2].innerText.replace(/,/g,'').trim();
            istoday = true;
          }
          let content = item.querySelector('.news_li').innerText;
          // 136 new cases and 8 new deaths
          let result =/([,\d]+) new cases and ([,\d]+) new deaths/. exec(content);
          if (result === null) {
            // '  3,957 new cases in Australia [source] [source] [source] [source] [source]'
            result = /([,\d]+) new cases/. exec(content);
            if (result === null) {
              result = [0,0]; // 0 cases, 0 deaths
            } else {
              result[1] = Number(String(result[1]).replace(/,/g,'').trim());
              result[2] = 0; // 0 deaths
            }
          } else {
            result[1] = Number(String(result[1]).replace(/,/g,'').trim());
            result[2] = Number(String(result[2]).replace(/,/g,'').trim());
          }
          createItems.push({
            cases: result[1], // spy postgres gak complain koma di angka
            deaths: result[2],
            date: tanggals[index],
            totalcases,
            totaldeaths,
            totalrecovered,
            istoday,
          });  
        });
        var items = { "posts": createItems };
        return items;
      });

      await browser.close();

      console.log(`stlh page evaluate yg mungkin gagal:`, kembalian);
      let terbangun = [];
      kembalian.posts.forEach((item, index) => {
        /**
          cek jk found where dimana date sama, maka update
          https://stackoverflow.com/questions/18304504/create-or-update-sequelize/41248216
         */
        const data = {
          country,
          cases: item.cases,
          deaths: item.deaths,
          totalcases: item.totalcases,
          totaldeaths: item.totaldeaths,
          totalrecovered: item.totalrecovered,
          date: item.date,
          istoday: item.istoday,
        };
        const object = Corona.build(data);        
        console.log(`terbangun object build dg:
        source = ${JSON.stringify(data)}
        hasil = ${JSON.stringify(object)}
        jenis hasil = ${typeof object}
        `);
        
        terbangun.push(object)
      });

      console.log(`
        telah build, tinggal save sebanyak: ${terbangun.length}
      `);

      terbangun.forEach(async (item, index) => {
        console.log(`terbangun object save ${index} of ${terbangun.length}`);
        try {
          // await item.save();
          const ada = await Corona.findOne({
            order: [
              ['id', 'DESC'],
            ],
            where: {
              date: item.date,
              country: item.country,
            }
          });

          // delete item['id'];
          let tanpa_id = Object.fromEntries(Object.entries(item.dataValues).filter(([k, v]) => k !== 'id'));
          console.log(`antara update atau create: ${ada}
          ***********************************************
          item utk update/create, dg id: ${JSON.stringify(item)}
          ***********************************************
          item utk update/create, tanpa id: ${JSON.stringify(tanpa_id)}
          ***********************************************
          `);
          if (ada !== null) {            
            // const hasilupdate = await ada.update(item, {
            // https://stackoverflow.com/questions/38524938/sequelize-update-record-and-return-result
            const hasilupdate = await Corona.update(tanpa_id, {
              where: {
                date: item.date,
                country: item.country,
              },
              returning:true,
            });
            console.log(`updating...hasilnya adlh: ${JSON.stringify(hasilupdate)}`);
          } else {
            console.log(`creating...`);
            await item.save();
          }
        } catch (err) {
          console.log(`gagal pada ${index} => ${JSON.stringify(err)}
          `);
        }  
      });
  
      console.log(`
        corona #4: END.
      `);

      // res.json({'status': 'ok'});
      res.json(kembalian);
    
    }).catch(function(error) {
      console.error(error);
      res.json({'status': 'error'});
    });
    
  },

  countries: async (req, res) => {
    try {
      const data = await Corona.findAll();
      const result = data;
      const uniques = [...new Set(result.map(i=>i.country))];
      res.json(uniques);
    } catch(err) {
      console.error(err);
      res.json({'status': 'error'});
    }
  },


});

const ExtenderObj = Extender();

const ExtensionRouter = Router => Router
  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  // .post("/current-admin", ExtenderObj.currentUser)
  // .post("/api/users/login", AuthProvider.login)
  // .post("/api/users/register", AuthProvider.register)

  // http://172.23.24.240:9101/corona/load/indonesia
  .get("/corona/load/:country", ExtenderObj.load)
  // http://172.23.24.240:9101/corona/latest/7/indonesia
  .get("/corona/latest/tujuh/:country?", ExtenderObj.tujuh)
  .get("/corona/latest/7/:country?", ExtenderObj.tujuh)

  .get("/corona/jamesbond/:countries", ExtenderObj.tujuhs)
  // http://172.23.24.240:9101/corona/today/indonesia
  .get("/corona/latest/today/:country?", ExtenderObj.today)
  .get("/corona/latest/0/:country?", ExtenderObj.today)
  // http://172.23.24.240:9101/corona/latest/countries
  .get("/corona/latest/countries", ExtenderObj.countries)
  .use(checkAuthToken)
  .get("/auth/latest", ExtenderObj.countries)
  ;

export default ExtensionRouter;

--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/corona/models/index.js

// import Corona from './mongo';
import Corona from './postgres';

export default Corona;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/corona/models/postgres.js
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = 'coronas';

const fieldsMap = {
	// id: { type: INTEGER, primaryKey: true },
	country: STRING,
	cases: INTEGER,
	deaths: INTEGER,
	totalcases: INTEGER,
	totaldeaths: INTEGER,
	totalrecovered: INTEGER,
	date: DATE,
	istoday: { type: BOOLEAN, default: false },
};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const Corona = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default Corona;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/equipment/extender.js

const ExtensionRouter = Router => Router
  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  // .post("/current-admin", ExtenderObj.currentUser)
  // .post("/api/users/login", AuthProvider.login)
  // .post("/api/users/register", AuthProvider.register)
  // .post("/api/users/update_password", AuthProvider.updatePassword)
  ;
export default ExtensionRouter;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/equipment/models/index.js

// import Equipment from './mongo';
import Equipment from './postgres';

export default Equipment;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/equipment/models/postgres.js
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = 'equipments';

const fieldsMap = {
    id: { type: INTEGER, primaryKey: true },
    name: { type: STRING, maxlength: [255, "Value too Long"] }
	};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const Equipment = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default Equipment;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/floor/extender.js

const ExtensionRouter = Router => Router
  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  // .post("/current-admin", ExtenderObj.currentUser)
  // .post("/api/users/login", AuthProvider.login)
  // .post("/api/users/register", AuthProvider.register)
  // .post("/api/users/update_password", AuthProvider.updatePassword)
  ;
export default ExtensionRouter;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/floor/models/index.js

// import Floor from './mongo';
import Floor from './postgres';

export default Floor;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/floor/models/postgres.js
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = 'floors';

const fieldsMap = {
    id: { type: INTEGER, primaryKey: true },
    name: { type: STRING, maxlength: [255, "Value too Long"] }
	};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const Floor = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default Floor;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/location/extender.js

const ExtensionRouter = Router => Router
  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  // .post("/current-admin", ExtenderObj.currentUser)
  // .post("/api/users/login", AuthProvider.login)
  // .post("/api/users/register", AuthProvider.register)
  // .post("/api/users/update_password", AuthProvider.updatePassword)
  ;
export default ExtensionRouter;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/location/models/index.js

// import Location from './mongo';
import Location from './postgres';

export default Location;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/location/models/postgres.js
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = 'locations';

const fieldsMap = {
    id: { type: INTEGER, primaryKey: true },
    name: { type: STRING, maxlength: [255, "Value too Long"] }
	};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const Location = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default Location;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/measurement/extender.js

const ExtensionRouter = Router => Router
  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  // .post("/current-admin", ExtenderObj.currentUser)
  // .post("/api/users/login", AuthProvider.login)
  // .post("/api/users/register", AuthProvider.register)
  // .post("/api/users/update_password", AuthProvider.updatePassword)
  ;
export default ExtensionRouter;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/measurement/models/index.js

// import Measurement from './mongo';
import Measurement from './postgres';

export default Measurement;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/measurement/models/postgres.js
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = 'measurements';

const fieldsMap = {
    id: { type: INTEGER, primaryKey: true },
    name: { type: STRING, maxlength: [255, "Value too Long"] }
	};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const Measurement = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default Measurement;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/news/extender.js
import Sequelize from 'sequelize';
import puppeteer from 'puppeteer';
import News from './models';

const Extender = () => ({

  dmau: async (req, res) => {

    console.log(`
    news #1: siap2 launch
    `);

    const browser = await puppeteer.launch({
      headless: true, 
      args: ['--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3312.0 Safari/537.36"']
    });

    console.log(`
    news #2: siap2 get dmau
    `);

    const page = await browser.newPage();
    const alamat = 'https://www.dailymail.co.uk/auhome/index.html';
    await page.goto(alamat);
    await page.waitForSelector('body');

    console.log(`
    news #3: siap2 parse story wrapper
    `);

    var kembalian = await page.evaluate(() => {
      let posts = document.body.querySelectorAll('div[class*="article"][itemprop="itemListElement"]');
      postItems = [];
      posts.forEach((item) => {
        // let title = '';
        // let summary = '';
        // let link = '';
        // let content = '';

        pertama = item.querySelector('div[class="articletext"]>div>p') || {innerText:''};
        kedua = item.querySelector('div[class="articletext-holder"]>p') || {innerText:''};
        normal = item.querySelector('div[class="articletext"]>p') || {innerText:''};
        excerpt_pertama = pertama.innerText;
        excerpt_kedua = kedua.innerText;
        excerpt_normal = normal.innerText;
        let text = 'KOSONG';
        if (excerpt_pertama.length !== 0) text = excerpt_pertama;
        else if (excerpt_kedua.length !== 0) text = excerpt_kedua;
        else if (excerpt_normal.length !== 0) text = excerpt_normal;

        // gambar1 = item.querySelector('div[class="articletext"]>a>img').dataset.src || {length:0};
        gambar2 = item.querySelector('a>img').dataset.src || {length:0};
        let gambars = [];
        // if (gambar1.length > 0) gambars.push(gambar1);
        // else 

        // "code":"22P02","detail":"Array value must start with \"{\" or dimension information."
        if (gambar2.length > 0) gambars.push(gambar2);


        // https://lerner.co.il/2014/05/19/learning-love-postgresql-arrays/
        gambars = gambars.toString()
        // gambars = '{' + gambars.toString() + '}'
        // gambars = '{' + gambars.toString().replace('"', '').replace("'",'') + '}'
        // https://medium.com/@olesiag/how-to-insert-into-postgresql-array-using-sequelize-and-express-31a2dae05c51
        // gambars = '{${[' + gambars.toString() + ']}}'
        // gambars = 'ARRAY[' + gambars.toString() + ']'
        

        postItems.push({
          title: item.querySelector('h2>a').innerText,
          link: item.querySelector('h2>a').href,
          summary: text,
          content: 'KOSONG',
          // https://github.com/sequelize/sequelize/issues/3819
          // images: ['satu', 'dua', 'tiga']
          images: gambars,
          // images: 'ARRAY[]',
          // images: '[]',
          // images: '{}',
        });

      });

      var items = { "posts": postItems };
      return items;
    });

    await browser.close();

    let max_id = await News.findAll({
      raw: true,
      attributes: [
        Sequelize.fn('max', Sequelize.col('id'))
      ]
    });
    if (max_id.length == 1) {
      max_id = max_id[0].max;
    }

    // sebelum save, ketemu max_id: [{"max":12}]
    console.log(`
      sebelum save, ketemu max_id: ${JSON.stringify(max_id)}
    `);

    let terbangun = [];
    kembalian.posts.forEach((item, index) => {
      const iden = (Number(max_id)+index+1).toString();
      const data = {
        id: iden,
        title: item.title,
        link: item.link,
        summary: item.summary,
        content: item.content,
        images: item.images,
        tags: 'dmau',
      };
      const object = News.build(data);
      console.log(`terbangun object build ${JSON.stringify(data)}`);
      terbangun.push(object);
    });

    console.log(`
      telah build, tinggal save sebanyak: ${terbangun.length}
    `);

    terbangun.forEach(async (item, index) => {
      console.log(`terbangun object save ${index}`);
      try {
        await item.save();
      } catch (err) {
        console.log(`
          gagal pada ${index}:
          ${JSON.stringify(err)}
        `);
      }

    });

    console.log(`
    news #4: END.
    `);

    res.json(kembalian);

  },

  nytimes: async (req, res) => {

    console.log(`
    news #1: siap2 launch
    `);

    const browser = await puppeteer.launch({
      headless: true, 
      args: ['--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3312.0 Safari/537.36"']
    });
    // .then(async browser => {

    console.log(`
    news #2: siap2 get nytimes
    `);
    
    const page = await browser.newPage();
    const alamat = "https://www.nytimes.com/";
    await page.goto(alamat);
    await page.waitForSelector('body');

    console.log(`
    news #3: siap2 parse story wrapper
    `);
  
    var kembalian = await page.evaluate(() => {
      let posts = document.body.querySelectorAll('.story-wrapper');
      postItems = [];
      posts.forEach((item) => {
        let title = '';
        let summary = '';
        let link = '';
        let content = '';
        try {
          // title = item.querySelector('h2').innerText;
          title = item.querySelector('a>div>h3').innerText;
          if (title!='') {
            // summary = item.querySelector('p').innerText;
            summary = item.querySelector('a>div>p').innerText;
            link = item.querySelector('a').href;

            postItems.push({
              title: title, link: link, summary: summary,
              content,
            });
          }

          // console.log(`
          // iterate item...
          // terima:
          // title = ${title}
          // link = ${link}
          // summary = ${summary}
          // `);
        } catch(e) {}

      });
      var items = { "posts": postItems };
      return items;
    });
  
    await browser.close();

    let max_id = await News.findAll({
      raw: true,
      attributes: [
        Sequelize.fn('max', Sequelize.col('id'))
      ]
    });

    let terbangun = [];
    kembalian.posts.forEach((item, index) => {
      const object = News.build({
        id: max_id+index+1,
        title: item.title,
        link: item.link,
        summary: item.summary,
        content: '',
        images: [],
        tags: 'nytimes',
      });
      // await object.save();
      terbangun.push(object)
    });
    
    console.log(`
      telah build, tinggal save sebanyak: ${terbangun.length}
    `);

    terbangun.forEach(async (item, index) => {
      console.log(`terbangun object save ${index}`);
      try {
        await item.save();
      } catch (err) {
        console.log(`
          gagal pada ${index}:
          ${JSON.stringify(err)}
        `);
      }

    });

    // News.bulkCreate(kembalian)
    // .then(() => {
    //   console.log(`
    //   setelah bulkCreate dan sebelum findAll
    //   `);
    //   // Notice: There are no arguments here, as of right now you'll have to...
    //   return News.findAll();
    // })
    // .then(berita => {
    //   // ... in order to get the array of user objects
    //   console.log(`
    //   ini setelah bulkCreate dan findAll selesai...
    //   `);
    //   console.log(berita);
    // })
    // .catch(err => {
    //   console.log(`
    //   GAGAL bulkCreate!
    //   ${JSON.stringify(err)}
    //   `);
    // })
    // ;

    console.log(`
    news #4: END.
    `);

    res.json(kembalian);

  },

});
const ExtenderObj = Extender();

const ExtensionRouter = Router => Router
  // http://172.23.24.240:9101/nytimes
  .get("/nytimes", ExtenderObj.nytimes)
  // http://172.23.24.240:9101/dmau
  .get("/dmau", ExtenderObj.dmau)
  // .post("/current-admin", ExtenderObj.currentUser)
  // .post("/api/users/login", AuthProvider.login)
  // .post("/api/users/register", AuthProvider.register)
  // .post("/api/users/update_password", AuthProvider.updatePassword)
  ;
export default ExtensionRouter;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/news/models/index.js

// import News from './mongo';
import News from './postgres';

export default News;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/news/models/postgres.js
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = 'newss';

const fieldsMap = {
	id: { type: INTEGER, primaryKey: true, autoIncrement: true, },
	title: { type: STRING, maxlength: [1000, "Value too Long"] },
	link: { type: STRING, maxlength: [500, "Value too Long"] },
	summary: STRING,
	content: TEXT,
	tags: STRING,
	// images: { type: ARRAY(TEXT) },
	// images: TEXT,
	images: STRING,
};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const News = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default News;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/point/extender.js

const ExtensionRouter = Router => Router
  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  // .post("/current-admin", ExtenderObj.currentUser)
  // .post("/api/users/login", AuthProvider.login)
  // .post("/api/users/register", AuthProvider.register)
  // .post("/api/users/update_password", AuthProvider.updatePassword)
  ;
export default ExtensionRouter;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/point/models/index.js

// import Point from './mongo';
import Point from './postgres';

export default Point;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/point/models/postgres.js
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = 'points';

const fieldsMap = {
    id: { type: INTEGER, primaryKey: true },
    name: { type: STRING, maxlength: [255, "Value too Long"] }
	};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const Point = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default Point;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/room/extender.js

const ExtensionRouter = Router => Router
  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  // .post("/current-admin", ExtenderObj.currentUser)
  // .post("/api/users/login", AuthProvider.login)
  // .post("/api/users/register", AuthProvider.register)
  // .post("/api/users/update_password", AuthProvider.updatePassword)
  ;
export default ExtensionRouter;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/room/models/index.js

// import Room from './mongo';
import Room from './postgres';

export default Room;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/room/models/postgres.js
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = 'rooms';

const fieldsMap = {
	id: { type: INTEGER, primaryKey: true },
	name: { type: STRING, maxlength: [255, "Value too Long"] }
};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const Room = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default Room;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/sensor/extender.js

const ExtensionRouter = Router => Router
  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  // .post("/current-admin", ExtenderObj.currentUser)
  // .post("/api/users/login", AuthProvider.login)
  // .post("/api/users/register", AuthProvider.register)
  // .post("/api/users/update_password", AuthProvider.updatePassword)
  ;
export default ExtensionRouter;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/sensor/models/index.js

// import Sensor from './mongo';
import Sensor from './postgres';

export default Sensor;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/sensor/models/postgres.js
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';
/**
 * crud create: error SequelizeDatabaseError: 
 * column "building" of relation "sensors" does not exist, 
 * data: {"smart_building":"smartie-001","sensor_id":"sense-001","building":"1","min_value":"0","max_value":"100","yellow":"60","red":"80","interval":"1000","stopper":"counter","stop":"1"}.
 * 
 */
import Building from 'A/building/models';

const tableName = 'sensors';

const fieldsMap = {
  id: { type: INTEGER, primaryKey: true, autoIncrement: true, },
  building_id: { type: STRING, allowNull: false, references: Building, },
  smart_building: { type: STRING, default: 'SB_0001', maxlength: [255, "Value too Long"] },
  sensor_id: { type: STRING, maxlength: [255, "Value too Long"] },
  min_value: { type: INTEGER, default: '0' },
  max_value: { type: INTEGER, default: '100' },
  yellow: { type: INTEGER, default: '60' },
  red: { type: INTEGER, default: '80' },
  interval: { type: INTEGER, default: '1' },
  stopper: { type: STRING, default: "counter", maxlength: [20, "Value too Long"], enum: ['epoch', 'counter'] },
  stop: { type: INTEGER, default: '0 ' }
};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const Sensor = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default Sensor;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/system/extender.js

const ExtensionRouter = Router => Router
  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  // .post("/current-admin", ExtenderObj.currentUser)
  // .post("/api/users/login", AuthProvider.login)
  // .post("/api/users/register", AuthProvider.register)
  // .post("/api/users/update_password", AuthProvider.updatePassword)
  ;
export default ExtensionRouter;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/system/models/index.js

// import System from './mongo';
import System from './postgres';

export default System;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/system/models/postgres.js
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = 'systems';

const fieldsMap = {
    id: { type: INTEGER, primaryKey: true },
    name: { type: STRING, maxlength: [255, "Value too Long"] }
	};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const System = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default System;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/todo/extender.js
import Todo from './models';

const Extender = () => ({
  metadata: async (req, res) => {
    try {
      
      const all = await Todo.findAll();
      console.log(`
      all todos:
      ${JSON.stringify(all)}
      `);
      const result = all;
      const unique = [...new Set(result.map(i=>i.category))]
      const data = unique.map(kategori => {
        let group_data = result.filter(i => i.category===kategori)
        return {
          [kategori]: group_data.map(r => ({done:r.done, content:r.content}))
        }
      });

      res.json(data);

    } catch(err) {
      console.error(err);
      res.json({'status': 'error'});
    }
  },
});
const ExtenderObj = Extender();
const ExtensionRouter = Router => Router
  
  .get("/ext/todo", ExtenderObj.metadata)

  ;
export default ExtensionRouter;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/todo/models/index.js

// import Todo from './mongo';
import Todo from './postgres';

export default Todo;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/todo/models/postgres.js
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = 'todos';

const fieldsMap = {
	id: { type: INTEGER, primaryKey: true },
	done: { type: BOOLEAN, default: 'false' },
	content: { type: STRING, maxlength: [5000, "Value too Long"] },
	category: STRING
};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const Todo = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default Todo;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/user/extender.js

import AuthProvider from './auth/provider';
import jwt_default_object from './auth/jwt';

const {
  // doGenToken,
  // generateToken,
  refreshToken,
  // decodeToken,
} = jwt_default_object;

const Extender = () => ({
  
//   createOrUpdateUser: async (req, res) => {
//     const { name, picture, email } = req.user;
  
//     const user = await User.findOneAndUpdate(
//       { email },
//       { name: email.split("@")[0], picture },
//       { new: true }
//     );
//     if (user) {
//       console.log("USER UPDATED", user);
//       res.json(user);
//     } else {
//       const newUser = await new User({
//         email,
//         name: email.split("@")[0],
//         picture,
//       }).save();
//       console.log("USER CREATED", newUser);
//       res.json(newUser);
//     }
//   },

  refresh_token: async (req, res, next) => {
    try {
      const { refresh_token } = req.body;
      if (!refresh_token) {
        return next(new Error("refresh_token can't be empty"));
      }
      const newToken = await refreshToken(refresh_token);
      const clientData = {
        response: "ok",
        data: newToken,
      };
      console.log(`
        refresh token send the following data to client:
        ${JSON.stringify(clientData)}
      `);
      return res.json(clientData);
    } catch (err) {
      if (err.message == "notvalid") {
        res.status(401).json({
          response: "nok",
          data: "Refresh token tidak valid.",
        });
        return;
      }
  
      return next(err);
    }
  },

});

const ExtenderObj = Extender();

const ExtensionRouter = Router => Router
  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  .post("/api/users/refresh_token", ExtenderObj.refresh_token)

  .post("/api/users/login", AuthProvider.login)
  .post("/api/users/register", AuthProvider.register)
  .post("/api/users/update_password", AuthProvider.updatePassword)
  ;

export default ExtensionRouter;

--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/user/auth/index.js
import Kripto from './kripto';
const Enkripsi = new Kripto('bcrypt');

export default Enkripsi;

--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/user/auth/jwt.js
const jwt = require('jsonwebtoken');
const moment = require('moment');
const randToken = require('rand-token');
const UIDGenerator = require('uid-generator');

import Token from './token';
// import Token from './token_mongo';

const doGenToken = () => {
  // Default is a 128-bit UID encoded in base58
  const uidgen = new UIDGenerator(256);
  return uidgen.generateSync();
}

const generateToken = async (userId, email=null, phone=null, role=null) => {
  let refreshToken = randToken.uid(64);
  let age = Number(process.env.NODE_ENV == 'production' ? process.env.JWT_EXPIRED_SECONDS_PRODUCTION : process.env.JWT_EXPIRED_SECONDS_DEVELOPMENT);
  // let age = 3 * 60 * 60
  let expTime = Date.now() / 1000 + age;
  
  // refresh token
  let oldToken = await Token.findOne({ where: { id_user: userId } });
  if (!oldToken) {
    
    const tokenExpiry = moment().add(7, "days");
    console.log(`

      creating new token: ${refreshToken} utk user ${userId} dg expiry: ${tokenExpiry}

    `);
    await Token.build({
      id_user: userId,
      refresh_token: refreshToken,
      refresh_expired_time: tokenExpiry,
    })
    .save();
    ;
  } else {
    console.log(`

      updating old token: ${refreshToken}

    `);
    await oldToken.update({
      refresh_token: refreshToken,
      refresh_expired_time: moment().add(7, "days"),
    });
  }

  // access token
  let jwt_internal_data = { id_user: userId, };

  if (email !== null && phone !== null && role !== null) {
    jwt_internal_data = { 
      id_user: userId, 
      email, 
      phone, 
      role 
    };
  }

  let jwt_data = {
    exp: expTime,
    data: jwt_internal_data,
  };

  let jwt_key = process.env.JWT_SECRET;
  let jwt_algo = { algorithm: "HS256" };
  const accessToken = jwt.sign( jwt_data, jwt_key, jwt_algo );
  
  return { accessToken, refreshToken, expTime }
}

const refreshToken = async (refresh_token) => {
  let authToken = await Token.findOne({ where: {refresh_token} });
  if (authToken) {
    if (moment(authToken.expired_time) < moment()) {
      throw new Error("refresh token already expired.");
    } else {
      let newToken = await generateToken(authToken.id_user);
      return newToken;
    }
  } else {
    throw new Error("auth token not valid.");
  }
}

const decodeToken = token => {
  try {
    return jwt.verify(token, process.env.JWT_SECRET);
  } catch (err) {
    throw err;
  }
}

export default {
  doGenToken,
  generateToken,
  refreshToken,
  decodeToken,
};

--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/user/auth/kripto.js
import bcrypt from 'bcrypt';
import crypto from 'crypto';

class Kripto {
  constructor(which_encryption = 'md5') {
    this.encrypt = this.hash_md5
    if (which_encryption == 'sha') {
      this.encrypt = this.hmac_sha256;
    } else if (which_encryption == 'bcrypt') {
      this.encrypt = this.hash_bcrypt;
      this.check = this.check_bcrypt;
    }
  }

  hash_md5 = (password) => crypto
    .createHash("md5")
    .update(password)
    .digest("hex");

  hmac_sha256 = (password) => crypto
    .createHmac("sha256", process.env.APP_SECRET)
    .update(password)
    .digest("hex");

  hmac_sha256_longer = (password) => crypto
    .createHmac("sha256", process.env.APP_SECRET)
    .update(password)
    .digest("hext").toString("hex");

  hash_bcrypt = async (password) => {
    const hashed = await bcrypt.hash(password, bcrypt.genSaltSync(+process.env.SALT_ROUNDS));
    return hashed;
  }

  check_bcrypt = async (suppliedPlainPassword, internallySavedHashedPassword) => {
    console.log(suppliedPlainPassword, '>>>>', await this.hash_bcrypt(suppliedPlainPassword), '>>>', internallySavedHashedPassword);
    const compare = await bcrypt.compare(suppliedPlainPassword, internallySavedHashedPassword);
    return compare;
  }
}

export default Kripto;

--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/user/auth/provider.js
import User from 'AU/models';
import Kripto from './kripto';
import jwt_default_object from './jwt';

const Enkripsi = new Kripto('bcrypt');

const {
  doGenToken,
  generateToken,
  refreshToken,
  decodeToken,
} = jwt_default_object;

const login = async (req, res, next) => {
  const process = async () => {

    // loginAxios(
    //   { 
    //     data: {
    //       username: values.username,
    //       password: values.password,
    //     }
    //   },
    console.log(`
      login #1
    `);

    const {
      email,
      password
    } = req.body;

    console.log(`
      login #2, terima
      user: ${email}
      pass: ${password}
    `);

    if (email == null || email == undefined || password === null || password === undefined)
      res.status(512).send({
        status: 'Error',
        message: 'Login not found',
      });

    // let pengguna_attributes = [ 'id', 'email', 'phone', 'role', 'username', 'password' ];
    let pengguna_attributes = [ 'id', 'email', 'username', 'password' ];
    let pengguna_where = { email };
    const pengguna = await User.findOne({
      attributes: pengguna_attributes,
      where: pengguna_where,
    });

    if (pengguna) {

      let check = await Enkripsi.check(password, pengguna.password);

      if (!check) {
        console.log(`gagal cek login ${email} dengan password ${password}.`);
        res.status(512).send({
            status: 'Error',
            message: 'Login not found',
        });
      }

      const jwt_token = await 
        generateToken(
          pengguna.id, 
          // pengguna.username, 
          // pengguna.name, 
          pengguna.email, 
          // pengguna.phone, 
          // pengguna.role
        );
      let response = {
        response: 'ok',
        data: {
          jwt: jwt_token,
          token: doGenToken(),
          email: pengguna.email,
          username: pengguna.username,
          // phone: pengguna.phone,
          // role: pengguna.role,
        },
      };
      console.log(`login ${email}, user ${pengguna}, successful: ${JSON.stringify(response)}`);
      res.json(response);
    }

  }

  try {
    process();
  } catch (err) {
    console.log(`Login processing error: ${err}.`);
    return next(err);
  }
};

const register = async (req, res, next) => {
  try {
    const {
      email,
      password,
      ...sisa
    } = req.body;

    const pengguna = User.build({
      email,
      password: Enkripsi.encrypt(password),
      ...sisa
    });

    const result = await pengguna.save();
    res.json(result);
  } catch (e) {
    return next(e);
  }
};

const updatePassword = async (req, res, next) => {
  try {
    const {
      email,
      password
    } = await req.body;

    console.log(`updatePassword, email: ${email}, password = ${password}.`);

    const pengguna = await User.findOne({
      attributes: ['id', 'email', 'password'],
      where: {
          email,
      }
    });

    if (pengguna && password !== '') {
      // ternyata ini [object Promise]
      let hasil_enkripsi = await Enkripsi.encrypt(password);
      console.log(`updatePassword, email: ${email}, password = ${password} => ${hasil_enkripsi}.`);
      pengguna.password = hasil_enkripsi;
      const result = await pengguna.save();
      res.json(result);
    } else {
      console.log(`update ${email} not found.`);
      res.status(512).send({
        status: 'Error',
        message: 'Email not found',
      });
    }

  } catch (err) {
    return next(err);
  }
};

export default {
  login,
  register,
  updatePassword,
};


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/user/auth/token.js
import { default as dbConnect } from 'D';

const {
  // DATE,
  INTEGER,
  STRING,  
} = require('sequelize');

const tableName = 'tokens';

const Token = dbConnect.define(
  
  tableName,

  {
    id_user: {
      type: INTEGER,
      allowNull: false
    },
    refresh_expired_time: {
      type: 'TIMESTAMP',
      allowNull: false
    },
    refresh_token: {
      type: STRING,
      allowNull: false
    },    
  },

  {
    freezeTableName: true,
    schema: process.env.DB_SCHEMA,
    timestamps: false
  }
  
)

Token.removeAttribute('id');

export default Token;

--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/user/auth/token_mongo.js
import mongoose from 'mongoose';

const fieldsMap = {
  id_user: { type: mongoose.Schema.Types.ObjectId, ref: 'User' },
  refresh_token: String,
  refresh_expired_time: Date,
}

const optionsMap = {
  timestamps: true
}

const TokenSchema = new mongoose.Schema(  
  fieldsMap,
  optionsMap
)

export default mongoose.model('Token', TokenSchema);


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/user/models/index.js
// import User from './mongo';
import User from './postgres';

export default User;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/user/models/mongo.js
import mongoose from 'mongoose';
// const { ObjectId } = mongoose.Schema;

const userSchema = new mongoose.Schema(
  {

    created_at: Date,
    email: { type: String, required: true, },
    firstname: String,
    lastname: String,
    password: String,
    phone: String,
    role: String,
    username: String,

    // name: String,
    // address: String,

    // email: {
    //   type: String,
    //   required: true,
    //   index: true,
    // },
    // role: {
    //   type: String,
    //   default: "subscriber",
    // },
    // cart: {
    //   type: Array,
    //   default: [],
    // },    
    // wishlist: [
    // 	{ type: mongoose.Schema.Types.ObjectId, ref: "Product" }
    // ],
  },
  { 
    timestamps: true
  }
);

export default mongoose.model("User", userSchema);


--#

--% C:/tmp/hapus/nda01/node-postgres/src/apps/user/models/postgres.js
import { default as dbConnect } from 'D';
import { 
  BIGINT, 
  BOOLEAN, 
  DATE,
  DECIMAL,
  DOUBLE, 
  ENUM, 
  FLOAT, 
  INTEGER, 
  STRING, 
  TEXT, 
  UUID, 
  UUIDV1, 
  UUIDV4,
} from 'sequelize';

const tableName = 'users';
const fieldsMap = {
  
  created_at: DATE,
  email: {
    type: STRING,
    allowNull: false,
  },
  firstname: STRING,
  lastname: STRING,
  password: STRING,
  phone: STRING,
  role: STRING,
  username: STRING,	
};

const optionsMap = {
  freezeTableName: true,
  schema: process.env.DB_SCHEMA,
  timestamps: false,
};

const User = dbConnect.define(
  tableName,
  fieldsMap,
  optionsMap,
);

// if (parseInt(process.env.DB_SYNC)===1) {
//   console.log(`\n\nDO SYNC'ing database...`);
//   dbConnect.sync({force: true});
// } else {
//   console.log(`\n\nnot synching database...`);
// }

export default User;

--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/app.js
// const express = require('express');
import express from 'express';
// import { setModel } from 'D';
import { devMiddlewares } from 'M';
import routes from 'R';
function setupApp(app) {
  app.use(express.json());
  app.use('/static', express.static('public'));

  // const { setModel } = require('D');
  // setModel(app);

  app.get('/', (_, res) => res.send(`dari dalam setupApp dg resolve!`));

  // const { devMiddlewares } = require('M');
  devMiddlewares(app);

  // app.use(require('R'));
  app.use(routes);
}

// module.exports = (app) => {
//   setupApp(app);
// }
const App = (app) => setupApp(app);
export default App;



--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/crud-mongoose.js
export default function(Model) {
  return {

    create: async ({body}, res, _) => {
      try {
        console.log(`crud create: start body: ${JSON.stringify(body)}`);
        const object = Model.build(body);
        const data = await object.save();
        return res.json(data);
      } catch(err) {
        console.log(`crud create: error ${err}, data: ${JSON.stringify(body)}.`);
        return res.status(422).json({ 
          message: 'Invalid request', 
          error: err,
          data: body
        });
      }
    },

    all: async (req, res)  => {
      try {
        // const options = {
        //   order: [ ['id', 'DESC'] ],
        // }
        // const data = await Model.findAll(options);
        const data = await Model.find({}).exec();
        const total = await Model.countDocuments().exec();
        return res.json({
          result: data,
          total,
        });
      } catch(err) {
        console.log(`CRUD/read/list error: [${err}]`);
      }
    },

    read: async ({params: {id}}, res)  => {
      try {
        const options = {
          where: {id}
        }
        const data = await Model.findOne(options);
        return res.json(data);
      } catch(err) {
      }
    },

    update: async ({body, params: {id}}, res, next)  => {
      try {
        const options = {
          where: {id}
        }
        const data = await Model.update(body, options);
        return res.json(data);
      } catch(err) {
        console.log(`crud update: error ${err}, data: ${JSON.stringify(body)}, id: ${id}`);
        return res.status(422).json({ 
          message: 'Invalid request',
          error: err,
          data: body 
        });
      }
    },

    destroy: async ({params: {id}}, res, next) => {
      try {
        const options = {
          where: {id}
        }
        const data = await Model.destroy(options);
        return res.json(data);
      } catch(err) {
        next(err);
      }
    },
    
  }

}



--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/crud.js
import { default as dbConnect } from 'D';
import Enkripsi from 'AU/auth';

export default function(Model) {
  return {
    create: async ({body}, res, _) => {
      try {
        console.log(`crud create: start body: ${JSON.stringify(body)}`);

        if (Model === dbConnect.models.users && body.hasOwnProperty('password')) {
          const encrypted = await Enkripsi.encrypt(body.password);
          console.log(`\n   *** changing pass from ${body.password} to ${encrypted}\n`);
          body.password = encrypted;
        }

        const object = Model.build(body);
        const data = await object.save();
        return res.json(data);
      } catch(err) {
        console.log(`crud create: error ${err}, data: ${JSON.stringify(body)}.`);
        return res.status(422).json({ 
          message: 'Invalid request', 
          error: err,
          data: body
        });
      }
    },
    all: async (req, res)  => {
      try {
        // const options = {
        //   order: [ ['id', 'DESC'] ],
        // }
        // const data = await Model.findAll(options);
        const data = await Model.findAll();
        const total = await Model.count();
        return res.json({
          result: data,
          total,
        });
      } catch(err) {
      }
    },
    read: async ({params: {id}}, res)  => {
      try {
        const options = {
          where: {id}
        }
        const data = await Model.findOne(options);
        return res.json(data);
      } catch(err) {
      }
    },
    update: async ({body, params: {id}}, res, next)  => {
      try {
        const options = {
          where: {id}
        }
        const data = await Model.update(body, options);
        return res.json(data);
      } catch(err) {
        console.log(`crud update: error ${err}, data: ${JSON.stringify(body)}, id: ${id}`);
        return res.status(422).json({ 
          message: 'Invalid request',
          error: err,
          data: body 
        });
      }
    },
    destroy: async ({params: {id}}, res, next) => {
      try {
        const options = {
          where: {id}
        }
        const data = await Model.destroy(options);
        return res.json(data);
      } catch(err) {
        next(err);
      }
    },
  }
}


--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/extender.js
// module.exports = () => ({
export default () => ({
  getFunc1: async(req, res, next) => res.json({
    'message': 'get-func1',
  }),
  
  getFunc2: async(req, res, next) => res.json({
    'message': 'get-func2',
  }),
  
  postFunc1: async(req, res, next) => res.json({
    'message': 'post-func1',
  }),

  postFunc2: async(req, res, next) => res.json({
    'message': 'post-func2',
  }),
});




--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/db/index.js
// import sequelize from './mongo';
import sequelize from './postgres';

export default sequelize;

--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/db/mongo.js
import mongoose from 'mongoose';

function connectionString(tryCount=1) {
  const dbHost = process.env.MONGO_HOST;

  const user_pass = `${process.env.MONGO_USER}:${process.env.MONGO_PASS}`;
  const host_port = `${dbHost}:${process.env.MONGO_PORT}`;
  const dbName = process.env.MONGO_DB || 'admin';
  
  const connstring = `mongodb://${user_pass}@${host_port}/${dbName}?authSource=admin`;
  console.log(`
    #${tryCount} Mongo Konek ke:
    ${connstring}
  `);
  return connstring;
}

mongoose.set('debug', true);

if (process.env.hasOwnProperty('MONGO_PORT')) {
  mongoose.connect(
    connectionString(),
    { 
      useNewUrlParser: true, 
      useUnifiedTopology: true 
    }
  );
} else {
  // tunggu sampai env populated
  // populating environment variables could take some times
  
  const timeout = 2000;
  console.log(`tunggu selama ${timeout} untuk koneksi ke mongo.`);
  setTimeout(function() {
  
    mongoose.connect(
      connectionString(2),
      { 
        useCreateIndex: true,
        useFindAndModify: false,
        useNewUrlParser: true, 
        useUnifiedTopology: true,
      }
    );

  }, timeout);

}

export default mongoose;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/db/postgres.js
import Sequelize from 'sequelize';

// let sequelize;
let sequelize = new Sequelize(`postgres://usef:rahasia@localhost:5432/tempdb`);

function otentikasi() {

  const dbname = process.env.POSTGRES_DB;
  const dbuser = process.env.POSTGRES_USER;
  const dbpass = process.env.POSTGRES_PASS;
  const dbhost = process.env.POSTGRES_HOST;
  const dbport = process.env.POSTGRES_PORT;
  
  const connstring = `postgres://${dbuser}:${dbpass}@${dbhost}:${dbport}/${dbname}`;
  
  sequelize = new Sequelize(connstring);
  // const sequelize = new Sequelize(`postgres://${process.env.POSTGRES_USER}:${process.env.POSTGRES_PASS}@${process.env.POSTGRES_HOST}:${process.env.POSTGRES_PORT}/${process.env.POSTGRES_DB}`);
  // const sequelize = new Sequelize(`postgres://usef:rahasia@gisel.ddns.net:9022/hapuslah`);
  console.log(`\n\n\n******* koneksi ke ${connstring}.`);

  sequelize
  .authenticate()
  .then(() => {
    console.log(`${__filename} => Succeed connect to ${dbhost}:${dbport}/${dbname} as ${dbuser}`);
  })
  .catch(err => {
    console.log(`${__filename} => Failed connect to ${dbhost}:${dbport}/${dbname} as ${dbuser} => ${JSON.stringify(err)}.`);	
  });
}

// tunggu sampai env populated
// populating environment variables could take some times
const timeout = 2000;
setTimeout(function() {

  otentikasi();

}, timeout);

export default sequelize;


--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/auth.js
import default_object from "../../apps/user/auth/jwt";
const { decodeToken } = default_object;

export const checkAuthToken = (req, res, next) => {
  let authToken =
    req.headers.authentication ||
    req.headers.Authentication ||
    req.headers.Authorization ||
    req.headers.authorization;

  if (!authToken) {
    if (!!req.query.jwtToken) {
      authToken = "Bearer " + req.query.jwtToken;
      delete req.query.jwtToken;
    }
  }

  if (!authToken) {
    // return next(new Error("Unauthenticated. Token tidak ditemukan"));
    return res.status(401).json({
      response: "nok",
      error: "Unauthenticated. Token tidak ditemukan",
    });
  }
  let tokens = authToken.split(" ");
  // TODO: add other authorization, not only bearer
  if (tokens.length != 2 || tokens[0] != "Bearer") {
    // next(new Error("Format token tidak valid"));
    return res.status(401).json({
      response: "nok",
      error: "Format token tidak valid",
    });
  } else {
    // TODO: handle other role, not only bearer
    try {
      let decoded = decodeToken(tokens[1]);
      req.idUser = decoded.data.id_user;
      req.user = decoded.data;
      next();
    } catch (e) {
      if (e.name == "TokenExpiredError") {
        return res.status(400).json({
          response: "nok",
          error: e.message,
        });
      } else {
        return res.status(401).json({
          response: "nok",
          error: e.message,
        });
      }
    }
  }
};

export const checkPermission = (permission) => (req, res, next) => {
  const { user } = req;
  if (!user) {
    throw new Error("Not Authorized");
  }

  const { role } = user;

  if (!role || !role.length || role !== permission) {
    throw new Error("You have no permission");
  }

  next();
};

export const handleAuth = (router) => {
  router.use(this.checkAuthToken);
};

--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/body.js
const bodyParser = require('body-parser');

const bodyParserMiddleware = (app) => {	
  app.use(bodyParser.json());
  app.use(bodyParser.urlencoded({
      extended: true
  }));
}

module.exports = bodyParserMiddleware;



--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/cors.js
const cors = require('cors');

const corsMiddleware = (app) => {
  
  if (process.env.NODE_ENV === 'production') {
    app.use(cors({
      // origin: process.env.CORS_ORIGIN.split(','),
      origin: '*',
      methods: process.env.CORS_METHOD.split(','),
      allowedHeaders: process.env.CORS_ALLOWED_HEADERS.split(','),
      exposedHeaders: ['File-Name'],
      maxAge: parseInt(process.env.CORS_MAX_AGE),
      credentials: process.env.CORS_CREDENTIALS === 'true',
    }));
  } else {
    app.use(cors({
      origin: '*',
      exposedHeaders: ['File-Name'],
    }));
  }
}

module.exports = corsMiddleware;



--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/index.js
const bodyParserMiddleware = require('./body');
const corsMiddleware = require('./cors');
const fileUploader = require('./uploader');
const morganMiddleware = require('./morgan');
const sessionMiddleware = require('./session');

const devMiddlewares = app => {

  const activeMiddlewares = [
    bodyParserMiddleware,
    corsMiddleware,
    fileUploader,
    // helmetMiddleware,
    morganMiddleware,
    sessionMiddleware,
  ];

  for (let _middleware of activeMiddlewares) {
    _middleware(app);
  }
}

module.exports = {
  devMiddlewares,
};





--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/morgan.js
const helmet = require('helmet');
const morgan = require('morgan');

// hidePoweredBy does not take options. Remove the property to silence this warning.
const helmetMiddleware = (app) => {
  
  app.use(helmet({
    hidePoweredBy: {
      setTo: process.env.POWERED_BY,
    },
  }));
}


const morganMiddleware = (app) => {	
  app.use(morgan('dev'));
}

module.exports = morganMiddleware;



--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/session.js
const session = require('express-session');

// express-session deprecated req.secret; 
// provide secret option backend/node2/middlewares/index.js:50:11
const sessionMiddleware = (app) => {
  
  app.use(session({
    name: app.appName,
    secret: process.env.SESSION_SECRET,
    resave: true,
    saveUninitialized: true,
    rolling: true,
    captcha: null,
    user: null,
    cookie: {
      httpOnly: false,
      secure: false,
      maxAge: 2000000,
    },
  }));
}

module.exports = sessionMiddleware;




--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/middlewares/uploader.js
const fileUpload = require('express-fileupload');

const fileUploader = (app) => {	
  app.use(fileUpload());
}

module.exports = fileUploader;




--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/routes/index.js
const express = require('express');
import GenericRouter from './generic';
// import DummyRouter from './dummy';
// import ExtensionRouter from './extension';
import AppModels from 'A';

const router = express.Router();

// server:port/model      GET
// server:port/model/:id  GET
// server:port/model      POST
// server:port/model/:id  PATCH
// server:port/model/:id  DELETE
router.use('/', GenericRouter(express));

AppModels.extenders.forEach(Extender => {
  // console.log(`jenis data extender adlh: ${typeof(Extender)}`);
  // router.use('/', Extender(router));
  router.use('/', Extender(express.Router()));
});

// const helloRouter = require('./dummy')(express);
// console.log(`pake dummy`);
// const helloRouter = DummyRouter(express);
// router.use('/', helloRouter);

// router.use('/ext', require('./extension')(helloRouter));
// router.use('/ext', ExtensionRouter(helloRouter));

export default router;

--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/routes/api/auth.js
var jwt = require('express-jwt');
var secret = require('S/config').secret;

function getTokenFromHeader(req){
  if (req.headers.authorization && 
      req.headers.authorization.split(' ')[0] === 'Token' ||
      req.headers.authorization && 
      req.headers.authorization.split(' ')[0] === 'Bearer') {
    return req.headers.authorization.split(' ')[1];
  }

  return null;
}

var auth = {
  required: jwt({
    secret: secret,
    userProperty: 'payload',
    getToken: getTokenFromHeader
  }),
  optional: jwt({
    secret: secret,
    userProperty: 'payload',
    credentialsRequired: false,
    getToken: getTokenFromHeader
  })
};

module.exports = auth;




--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/routes/api/index.js
const router = require('express').Router();

router.use('/', require('./users'));
// router.use('/profiles', require('./profiles'));
// router.use('/articles', require('./articles'));
// router.use('/tags', require('./tags'));

router.use(function(err, req, res, next){
  if(err.name === 'ValidationError'){
    return res.status(422).json({
      errors: Object.keys(err.errors).reduce(function(errors, key){
        errors[key] = err.errors[key].message;
        return errors;
      }, {})
    });
  }

  return next(err);
});

// module.exports = router;
export default router;




--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/routes/api/users.js
var mongoose = require('mongoose');
var router = require('express').Router();
var passport = require('passport');
var User = mongoose.model('User');
var auth = require('./auth');

router.get('/user', auth.required, function(req, res, next){
  User.findById(req.payload.id).then(function(user){
    if(!user){ return res.sendStatus(401); }

    return res.json({user: user.toAuthJSON()});
  }).catch(next);
});

router.put('/user', auth.required, function(req, res, next){
  User.findById(req.payload.id).then(function(user){
    if(!user){ return res.sendStatus(401); }

    // only update fields that were actually passed...
    if(typeof req.body.user.username !== 'undefined'){
      user.username = req.body.user.username;
    }
    if(typeof req.body.user.email !== 'undefined'){
      user.email = req.body.user.email;
    }
    if(typeof req.body.user.bio !== 'undefined'){
      user.bio = req.body.user.bio;
    }
    if(typeof req.body.user.image !== 'undefined'){
      user.image = req.body.user.image;
    }
    if(typeof req.body.user.password !== 'undefined'){
      user.setPassword(req.body.user.password);
    }

    return user.save().then(function(){
      return res.json({user: user.toAuthJSON()});
    });
  }).catch(next);
});

router.post('/users/login', function(req, res, next){
  if(!req.body.user.email){
    return res.status(422).json({errors: {email: "can't be blank"}});
  }

  if(!req.body.user.password){
    return res.status(422).json({errors: {password: "can't be blank"}});
  }

  passport.authenticate('local', {session: false}, function(err, user, info){
    if(err){ return next(err); }

    if(user){
      user.token = user.generateJWT();
      return res.json({user: user.toAuthJSON()});
    } else {
      return res.status(422).json(info);
    }
  })(req, res, next);
});

router.post('/users', function(req, res, next){
  var user = new User();

  user.username = req.body.user.username;
  user.email = req.body.user.email;
  user.setPassword(req.body.user.password);

  user.save().then(function(){
    return res.json({user: user.toAuthJSON()});
  }).catch(next);
});

module.exports = router;

--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/routes/dummy/index.js
const waktu = new Date();

const greetingService = (req, res) => res.json({
  'status'		: 'ok',
  'day'				: waktu.toLocaleDateString(),
  'time'			: waktu.toLocaleTimeString(),
  'message'		: `Hello, ${req.params.name || "World"}!`,
});

// module.exports = (express) => express
const DummyRouter = (express) => express
  .Router()
  .get('/hello', greetingService)
  .get('/hello/:name', greetingService);

export default DummyRouter;



--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/routes/extension/index.js
// const Extender = require('C/extender')();
import Extender from 'C/extender';
const ExtenderObj = Extender();

const ExtensionRouter = Router => Router

  .get('/func1', ExtenderObj.getFunc1)
  .post('/func1', ExtenderObj.postFunc1)

  .get('/func2', ExtenderObj.getFunc2)
  .post('/func2', ExtenderObj.postFunc2);

// module.exports = RouterExtender;
export default ExtensionRouter;




--#

--% C:/tmp/hapus/nda01/node-postgres/src/core/routes/generic/index.js
import Cruder from 'C/crud';
// import Cruder from 'C/crud-mongoose';

import AppModels from 'A';

const GenericRouter = (express, Controller) => {
  // const router = express.Router();
  // return router;
  return express.Router()	
    .post("/", Controller.create)
    .get("/", Controller.all)
    .get("/:id", Controller.read)
    .patch("/:id", Controller.update)
    .delete("/:id", Controller.destroy)	
}

// module.exports = (express) => {
export default function (express) {
  const router = new express.Router();
  // router.use(`/task`, GenericRouter(express, Cruder(Task)));
  // router.use(`/user`, GenericRouter(express, Cruder(User)));
  Object.entries(AppModels.base).forEach(([k,v]) => {
    router.use(`/${k}`, GenericRouter(express, Cruder(v)));
  });

  return router;
}

--#

--% C:/tmp/hapus/nda01/node-postgres/src/server/server-dev.js
import express from 'express';
import webpack from 'webpack';
import webpackDevMiddleware from 'webpack-dev-middleware';
import webpackHotMiddleware from 'webpack-hot-middleware';
// import config from '../../webpack.dev.config.js';
import config_func from 'S/../../webpack-node-pg';
import App from 'C/app';

import dotenv from 'dotenv';
dotenv.config();

const config = config_func();

const app = express();
const compiler = webpack(config);

app.use(webpackDevMiddleware(compiler, {
  publicPath: config.output.publicPath
}));

app.use(webpackHotMiddleware(compiler));

App(app);

// const PORT = process.env.PORT || 8080
// app.listen(PORT, () => {
//   console.log(`App listening to ${PORT}....`)
//   console.log('Press Ctrl+C to quit.')
// })
// tunggu 2 detik
const timeout = process.env.TIMEOUT || 2000;
setTimeout(function() {
  const PORT = process.env.PORT || 8080;
  app.listen(PORT, '0.0.0.0', () => {
    console.log(`App listening to ${PORT}....`)
    console.log('Press Ctrl+C to quit.')
  });
}, timeout);



--#

--% C:/tmp/hapus/nda01/node-postgres/src/server/server-prod.js
import path from 'path'
import express from 'express'

const app = express(),
            DIST_DIR = __dirname,
            HTML_FILE = path.join(DIST_DIR, 'index.html')


app.use(express.static(DIST_DIR))

app.get('*', (req, res) => {
  res.sendFile(HTML_FILE)
})

const PORT = process.env.PORT || 8080
app.listen(PORT, () => {
  console.log(`App listening to ${PORT}....`)
  console.log('Press Ctrl+C to quit.')
})



--#

--% C:/tmp/hapus/nda01/node-postgres/__mocks__/fileMock.js
module.exports = 'test-file-stub';



--#

--% C:/tmp/hapus/nda01/node-postgres/__mocks__/styleMock.js
module.exports = {};



--#

--% C:/tmp/hapus/nda01/react-antd/.babelrc
{
  "presets": [
    "@babel/preset-env",
    "@babel/preset-react"
  ],
  "plugins": [
    "react-hot-loader/babel",
    "@babel/plugin-proposal-class-properties",
    ["@babel/transform-runtime"]
  ]
}




--#

--% C:/tmp/hapus/nda01/react-antd/.env
HOST=localhost
PORT=9000

SALT_ROUNDS=14
#mongo or postgres
DB_CHOICE=postgres
DB_SCHEMA=public
SESSION_SECRET=K1nG.5up3rM4rk3t!
SESSION_NAME=anynameisgood
JWT_SECRET=Qu33n.5up3rM4rk3t!

NODE_ENV=development
REACT_APP_ENV=development

MONGO_DB=hapuslah
MONGO_HOST=gisel.ddns.net
MONGO_PORT=27017
MONGO_USER=usef
MONGO_PASS=rahasia

POSTGRES_DB=hapuslah
POSTGRES_USER=usef
POSTGRES_PASS=rahasia
POSTGRES_HOST=gisel.ddns.net
POSTGRES_PORT=9022

--#

--% C:/tmp/hapus/nda01/react-antd/.eslintrc.js
module.exports = {
  "extends": [
    "eslint:recommended",
  ],
  "parser": "babel-eslint",
  "rules": {
    "no-unused-vars": "off",
    "no-undef": "off",
    "no-console": "off",
    "no-case-declarations": "off",
    "no-prototype-builtins": "off",

    "no-unexpected-multiline": "off",
  }
};



--#

--% C:/tmp/hapus/nda01/react-antd/config.js
const config = {

  authentication: {
    storage: {
      access_token: 'fulgent-token-access',
      refesh_token: 'fulgent-token-refresh',
      expiry_token: 'fulgent-token-expiry',
      user: 'fulgent-user',
    },
    path: {
      after_token_expired: '/login',
      refresh: 'api/users/refresh_token',
    },
  },
  
  backend: {
    // host: 'localhost',
    host: '172.21.37.176',
    port: 9101,

    paths: {
      login: {        
        // path: 'user/login',
        path: 'api/users/login',
        method: 'POST',
      },
      logout: {
        path: 'api/users/logout',
        method: 'POST',
      },
      register: {
        path: 'api/users/register',
        method: 'POST',
      },
      forgot: {
        path: 'api/users/forgot',
        method: 'POST',
      },
      update: {
        path: 'api/users/update_password',
        method: 'POST',
      },
    },
  },

};

config.server = () => `http://${config.backend.host}:${config.backend.port}`;
config.serverPath = (path) => {
  let fullpath = path;
  if (path && !path.startsWith('/')) fullpath = '/' + fullpath;
  return `http://${config.backend.host}:${config.backend.port}${fullpath}`;
}

export default config;

--#

--% C:/tmp/hapus/nda01/react-antd/index.css
@import '~antd/dist/antd.css';
/* @import '~antd/dist/antd.dark.css'; */
/* @import '~antd/dist/antd.compact.css'; */
@import url('https://fonts.googleapis.com/css?family=Roboto:300,400,500&display=swap');

:root {
  --left-distance: 15%;
  --left-sidebar-percent: -15%; /* negative dari left-distance */
}

* {
  margin: 0;
  padding: 0;
}

body {
  height: 100%;
  margin: 0;
  font-family: "Helvetica Neue", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
    
}

body::after {
  content: "";
  background-size: cover;
  opacity: 0.2;

  top: 0;
  left: 0;
  bottom: 0;
  right: 0;

  position: fixed;
  z-index: -1;   
}

--#

--% C:/tmp/hapus/nda01/react-antd/index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Fullstack Template | Fulgent</title>
  <link
      rel="stylesheet"
      href="https://unpkg.com/leaflet@1.6.0/dist/leaflet.css"
      integrity="sha512-xwE/Az9zrjBIphAcBb3F6JVqxf46+CDLwfLMHloNu6KEQCAWi6HcDUbeOfBIptF7tcCzusKFjFw2yuvEpDL9wQ=="
      crossorigin=""
    />

</head>
<body>
  <div id="app"></div>
</body>
</html>


--#

--% C:/tmp/hapus/nda01/react-antd/index.js
import React from 'react';
import ReactDOM from 'react-dom';

import './index.css';
import 'font-awesome/css/font-awesome.min.css';
// import { App } from './components/App';
import App from './components/App';

ReactDOM.render(<App />, document.querySelector('#app'));



--#

--% C:/tmp/hapus/nda01/react-antd/README.md
cara kerja per modul

misal:

Sensor
  import ReadList from './List';
  import FormWrapper from './FormWrapper';
  const [drawerVisible, setDrawerVisible] = useState(false);
  const [modal_bomodule_content, set_modal_bomodule_content] = useState({});
  const show_update = (data) => {
    set_modal_bomodule_content(data);
    setDrawerVisible(true);
  }
  TabPage
    FormWrapper
    ReadList
      component: <ReadList show_update={show_update} />
CreateForm
UpdateForm
FormProvider
FormWrapper
List
  props
    {
      show_update,
      recordTransformer = record => record,
    }
Modal

const request = _req.createService("/auth", false);
request
  .post(this.state.form)
  .then(({ data }) => {})
  .catch((err) => {})
  .finally(() => {
    setLoading(false);
  })

const upload = _req.createService("/file/upload");
const dataRaw = await upload.upload(formData);
const { data } = await dataRaw.json();


--#

--% C:/tmp/hapus/nda01/react-antd/assets/building.json
{
  "headers": [
    "",
    "id",

    "name",
    "building_id",
    "location_text",
    "lalo",
    "description",
    "notes",


    "delete"
  ],
  "widths": {
    "show": 50,
    "id": 30,
    "hapus": 30,
    "normal": 150
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/assets/equipment.json
{
  "headers": [
    "",
    "id",

    "name",


    "delete"
  ],
  "widths": {
    "show": 50,
    "id": 30,
    "hapus": 30,
    "normal": 150
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/assets/favicon.ico
AAABAAMAEBAAAAEAIABoBAAANgAAACAgAAABACAAKBEAAJ4EAAAwMAAAAQAgAGgmAADGFQAAKAAAABAAAAAgAAAAAQAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPr59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//nw7//69fP/+vn3//r59//6+ff/+vn3//r59//50tX/+vn3//nLz//6+ff/+s3R//mttP/5r7f/+vn3//nP0//5yc3/+brA//r39f/65OX/+amx//mxuf/65OT/+cfL//r19P/5vsT/+vn3//nEyf/6+ff/+aav//r59//5u8H/+cHG//nLz//51df/+cTI//r59//5wMb/+d7f//m7wf/5lJ//+vTz//r59//5yMz/+vn3//nJzf/6+ff/+cvP//rY2v/51Nf/+c7S//nHzP/6+ff/+d/g//ni4//5x8v/+c7S//nLz//6+ff/+bnA//r59//5u8H/+vn3//m1vP/5usD/+trc//nFyv/5wMX/+vLx//m7wf/6+Pb/+cfL//r59//509b/+vn3//rp6f/5rLT/+uvr//r59//5uL7/+cHG//nIzf/5uL//+vf2//mzuf/619n/+vn3//nHy//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+tfZ//nV2P/5s7r/+dPW//r59//6+ff/+vn3//r59//66ur/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3/9rFzP9m1eT/+urq//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59/+a8vn/R7bM//j59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/7vj3/917i//61Nb/+vn3//r59//6+ff/+vn3//r59//5ztL/+aOs//m7wf/6+ff/+cbL//mttf/5rLT/+vn3//r59//5pq//+dDT//r59//64OL/+amx//mstP/64uP/+vXz//r59//5sbj/+vn3//nFyf/6+ff/+aqy//r59//66en/+amy//mirP/6+ff/+cTJ//r59//5xMn/+d7f//ri4//5qLD/+trc//r59//5x8z/+vn3//nJzf/6+ff/+dTX//nCx//5xMn/+t7g//nHzP/6+ff/+d7f//nj5P/5vML/+uzs//nO0v/6+ff/+bi+//r29f/5usD/+vn3//nM0P/53uD/+dfZ//nV2P/5wsf/+u7u//m4v//6+Pf/+vf1//mwuP/65OX/+vn3//rr6//5r7b/+vLw//r59//50dT/+vn3//rp6f/66en/+vj2//m2vf/63N7/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAACAAAABAAAAAAQAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPr59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+Pb/+ejo//no6P/66en/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+cHH//r59//6+ff/+vn3//m9w//6+ff/+vn3//r59//64eL/+XGB//l8iv/67e3/+cPI//r59//6+ff/+vn3//nN0f/5j5v/+aev//l9i//68vD/+vn3//r59//6+ff/+vn3//mlrv/4Znf/+bi///rh4v/62tz/+vn3//r59//5laD/+vn3//r59//67u7/+YqW//r59//6+ff/+vLx//lqe//65eX/+uHi//h1hP/5maP/+vn3//r59//64OH/+Zei//r29f/6+ff/+u3t//mMmf/68/H/+vn3//r59//5pa7/+aSt//r29P/5oar/+YyY//nDyP/6+ff/+vn3//mVoP/6+ff/+vn3//mRnP/65eb/+vn3//r59//5naf/+uLj//r59//6+ff/+tTX//hQZP/6+ff/+vn3//mnsP/67Oz/+ZKd//iSnv/5oKr/+vDv//mutf/6+ff/+vf1//mJlf/6+ff/+vn3//r59//5YHL/+cPI//r59//6+ff/+ZWg//r59//66+r/+YmW//r59//6+ff/+vn3//mXov/6+ff/+vn3//r59//6+ff/+XyK//r59//6+ff/+bO6//mosP/66ur/+vf1//rd3v/5wMb/+bO6//r59//50NP/+cDF//r59//6+ff/+vn3//mwuP/5w8j/+vn3//r59//5c4L/+uPj//mKl//65+f/+vn3//r59//6+ff/+Zij//r59//6+ff/+vn3//r59//5maP/+vn3//r59//5t77/+cjM//mUn//69PP/+vn3//m2vP/5tbz/+vn3//m3vf/52tz/+vn3//r59//6+ff/+czQ//nEyP/6+ff/+vn3//mIlf/4YnT/+YKP//r59//6+ff/+vn3//r59//5laD/+vn3//r59//6+ff/+vn3//mZo//6+ff/+vn3//mzuv/6+ff/+t/g//r59//65+j/+brA//mSnf/6+ff/+cLI//nLz//6+ff/+vn3//r59//5vsT/+dTW//r59//6+ff/+ZWg//rs7P/4aXr/+ubm//r59//6+ff/+vn3//mOmv/68fD/+vn3//r59//67Oz/+Zql//r59//6+ff/+YuX//rk5f/66ur/+uTl//mWof/64eL/+Zij//rh4v/67+7/+ZGc//r59//6+ff/+vn3//mRnP/69vT/+vn3//r59//5laD/+vn3//rq6v/4ZXb/+unp//r59//6+ff/+t/g//mIlf/6+ff/+vj2//l7if/66ur/+vn3//r59//60dX/+ZSf//mDkP/5lqH/+vn3//r59//5p7D/+vX0//r59//5iZX/+t7g//r59//509b/+ZGc//r59//6+ff/+vn3//mVoP/6+ff/+vn3//rp6f/4c4L/+vn3//r59//6+ff/+brA//ljdf/4XW//+cLH//r59//6+ff/+vn3//mqsv/5s7r/+ZCc//nFyv/6ztL/+vn3//lgcv/69/X/+vn3//rz8v/5doT/+GN0//l1hP/69fP/+vn3//r59//6+ff/+ZWg//r59//6+ff/+vn3//r49//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+u3s//mWoP/53+D/+dDT//mvt//5rLT/+ZKe//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//5laD/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6wcb/+u7t//nd3//50dT/+bm///rX2f/5laD/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//mVoP/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//m0u//6+ff/+ba8//ry8P/5nKb/+aCq//nEyf/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+b7E//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+cDF/9nd4f+Xl6r/vvX4//rn5//60NP/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//69/X/nICW/xbf9P8s6/z/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59/8q6/z/MsPZ/wzp/f/y+Pf/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3/0vt+/+bXnj/Q87h//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/yvb4/7BfeP/VgJH/+tTX//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+Gl5//mjrP/5iZX/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+u7t//mJlv/4aHn/+ba8//r59//6+ff/+vn3//r59//5yM3/+GJ0//lzg//66ur/+bm///r59//6+ff/+vn3//r59//5j5v/+tPW//nCx//66Oj/+vn3//r59//6+ff/+vj2//mLmP/4YnT/+aKr//rc3v/61Nf/+vn3//r59//4Wm3/+ba9//nk5f/5d4b/+sbL//r59//6+ff/+uLj//h3hv/69fP/+uvq//h0hP/5mKP/+vn3//r59//6+ff/+vn3//m8wv/5eoj/+tnb//m8wv/6+ff/+vn3//r59//5mKP/+b3D//r59//5uL7/+XyK//nDyP/6+ff/+vn3//rp6f/6+ff/+vn3//nn5//5h5T/+vn3//r59//5kJz/+vLx//r59//6+ff/+s/S//hfcf/6+ff/+vn3//r59//69vT/+Y+b//mBj//5pK3/+bG5//r59//6+ff/+vXz//mNmf/6+ff/+vn3//r59//5anv/+cPI//r59//6+ff/+vn3//r59//6+ff/+a61//mosf/6+ff/+vn3//mYov/6+ff/+vn3//r59//6+ff/+ICO//r59//6+ff/+vn3//m7wf/67Oz/+aix//mDkf/5sbn/+vn3//r59//5y8//+cXK//r59//6+ff/+vn3//m1vP/5w8j/+vn3//r59//6+ff/+ay0//hkdf/5gY7/+vf2//r59//6+ff/+Zij//r59//6+ff/+vn3//r59//4mKL/+vn3//r59//6+ff/+bG5//nO0f/4kJz/+Y+b//rT1v/619n/+vn3//m3vf/52tz/+vn3//r59//6+ff/+czQ//nEyf/6+ff/+vn3//mfqP/5mqT/+vX0//r59//6+ff/+vn3//r59//5lJ//+vn3//r59//6+ff/+vn3//mZo//6+ff/+vn3//r59//5r7f/+bC3//r59//5zND/+uHi//mxuf/6+ff/+cbL//nHy//6+ff/+vn3//r59//5usD/+dfZ//r59//6+ff/+HiH//r59//6+ff/+vn3//r49v/6+ff/+vn3//mKlv/69PL/+vn3//r59//619r/+a21//r59//6+ff/+crO//re3//5tLv/+vn3//r29P/5uL//+bG5//r59//68vH/+YuY//r59//6+ff/+vn3//mNmf/69/b/+vn3//r59//5h5T/+cfM//r39f/5g5H/+cbL//r59//6+ff/+tze//mFkv/6+Pb/+u/v//lwf//69vT/+vn3//r59//5r7f/+trc//nT1v/6+ff/+vn3//m0u//5usD/+vDv//r59//5kp7/+c/S//r59//5wcf/+Zul//r59//6+ff/+vn3//ry8P/5eIb/+Fhr//mlrv/6+ff/+vn3//r59//6+ff/+cDG//hldv/5ZHb/+tzd//r59//6+ff/+vn3//mwt//5tbz/+vj2//r59//6+ff/+brA//rw7//5wcb/+vn3//r39f/5hZL/+GN0//mGk//6+Pb/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+u/u//rv7v/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59/8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAADAAAABgAAAAAQAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPr59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vb1//nd3v/53d7/+d3e//nd3//67ez/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//67+//+tja//r59//6+ff/+vn3//r59//69fT/+tPW//r59//6+ff/+vn3//r59//6+ff/+uvr//rCx//5pa7/+s3R//rz8f/67Oz/+tze//r59//6+ff/+vn3//r59//6+ff/+cDG//hXav/4cYD/+HGA//hneP/5l6L/+vj2//r59//6+ff/+vn3//r59//6+ff/+vn3//rk5P/5trz/+aav//rZ2//69fP/+uXm//rf4P/6+ff/+vn3//r59//509b/+YeU//r59//6+ff/+vn3//r59//6xcr/+X2L//r59//6+ff/+vn3//r59//64eL/+W19//lkdv/5fYv/+Wt7//mIlf/5w8j/+Zei//r59//6+ff/+vn3//r59//61dj/+YSR//rX2f/6+ff/+vn3//rq6v/5l6L/+dHU//r59//6+ff/+vn3//r59//6+ff/+tPW//hbbv/5bn7/+X2L//hpev/5qrL/+bG5//mgqf/6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//rz8v/5h5T/+szQ//r59//6+ff/+vn3//r19P/5ipf/+Z+p//ru7v/6+Pb/+u3s//mXov/5bX3/+ZWg//r59//6+ff/+vn3//rr6//5laD/+tLV//r39v/6+ff/+vn3//r49v/63+D/+G+A//ro6P/6+ff/+vn3//r59//67u3/+FJl//q9wv/68vH/+vj2//rg4f/4dYT/+Y+a//mfqf/6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//rV2P/5go//+u7t//r59//6+ff/+vn3//rd3v/5hJH/+uzs//r59//6+ff/+vn3//rm5//5TGH/+X2L//r59//6+ff/+vn3//rM0P/5sLf/+vLx//rO0f/5vsT/+b3D//rKzv/67ez/+uLj//mBjv/6+Pb/+vn3//r59//5qrL/+Z2n//r59//6+ff/+vn3//r59//6xMn/+CQ9//mfqf/6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//mEkf/5tbv/+vn3//r59//6+ff/+vn3//m+w//5o6z/+vn3//r59//6+ff/+vn3//r39v/5jZr/+YKQ//r59//6+ff/+vn3//mTn//66Oj/+Zyn//mRnf/5pa7/+aWu//mXov/5pa7/+vLx//mbpf/64uP/+vn3//rz8v/5kp3/+tvc//r59//6+ff/+vn3//r59//69fT/+E9j//mfqf/6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+tLU//hXav/68vH/+vn3//r59//6+ff/+vn3//mWof/5y8//+vn3//r59//6+ff/+vn3//r59//5t73/+Y+a//r59//6+ff/+vn3//mGlP/64eH/+Zmk//rx8P/65eX/+vj2//r19P/5q7P/+uLj//rQ0//5wcb/+vn3//rp6f/5mKP/+unp//r59//6+ff/+vn3//r59//6+ff/+Y+a//mfqf/6+ff/+vn3//r59//50tX/+Wp7//rt7P/68/L/+F1v//nHzP/6+ff/+vn3//r59//6+ff/+vn3//mAjv/5293/+vn3//r59//6+ff/+vn3//r59//5ys7/+Zag//r59//6+ff/+vn3//iMmP/5y8//+c/T//mXo//5p7D/+vb1//r59//5tbz/+uLj//ri4//5tbz/+vn3//rj5P/5mqP/+u/u//r59//6+ff/+vn3//r59//6+ff/+a21//mgqf/6+ff/+vn3//r59//50tX/+D9V//lufv/5n6n/+HaG//r59//6+ff/+vn3//r59//6+ff/+vn3//l/jf/52tz/+vn3//r59//6+ff/+vn3//r59//5yc3/+Zul//r59//6+ff/+vn3//mJlv/67Oz/+vHw//mPm//6+Pb/+vn3//r59//5s7r/+uLj//rb3f/5usD/+vn3//rj5P/5l6H/+u7t//r59//6+ff/+vn3//r59//6+ff/+auz//mnr//6+ff/+vn3//r59//50tX/+X+N//mWoP/4KEH/+szQ//r59//6+ff/+vn3//r59//6+ff/+vn3//mTnv/5x8v/+vn3//r59//6+ff/+vn3//r59//5t73/+bG4//r59//6+ff/+vn3//mFkv/69/b/+vn3//rq6v/6+ff/+vn3//rv7v/5o63/+ubn//mFkv/5s7r/+vn3//ro6f/5lJ//+ujo//r59//6+ff/+vn3//r59//6+ff/+Y6a//nEyf/6+ff/+vn3//r59//50tX/+YaT//ry8f/5gpD/+YmW//rv7v/6+ff/+vn3//r59//6+ff/+vn3//m8wv/5nab/+vj2//r59//6+ff/+vn3//r49v/5laD/+tHV//r59//6+ff/+vn3//mkrf/5xMn/+vPy//ry8f/68vH/+vHw//l5h//5q7P/+tTX//mBj//5pa7/+vLx//rz8v/5jZn/+tbY//r59//6+ff/+vn3//r59//69fT/+Fls//rw7//6+ff/+vn3//r59//50tX/+YaT//r59//66+v/+XyK//l0g//65+f/+vn3//r59//6+ff/+vn3//rf4P/5fYv/+unp//r59//6+ff/+vn3//rj5P/5g5D/+uXm//r59//6+ff/+vn3//m1vP/5jJj/+aav//nEyf/5maT/+cbL//rZ2//69/X/+uXm//rV2P/5rLT/+vPy//r59//5rrX/+Y+a//r59//6+ff/+vn3//r59//5vsT/+YGP//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vHw//mLmP/5eYf/+vDv//r59//6+ff/+vn3//r29P/5kp3/+ZOe//r59//6+ff/+vf1//h1hP/5oar/+vf2//r59//6+ff/+vn3//rx8P/5xsv/+YCO//l3hv/5pa3/+X+N//r59//6+ff/+vn3//rAxv/5usD/+vn3//r59//68O//+F1v//mwt//6+ff/+vn3//ri5P/5Z3j/+tTW//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//rw7//5eYj/+Y6a//r59//6+ff/+vn3//r59//67+7/+WFy//lcbv/5gY7/+Epf//lufv/68/L/+vn3//r59//6+ff/+vn3//mXof/5Z3j/+sjM//l8iv/5s7r/+Zym//rN0f/6+ff/+vn3//mHlP/5pa7/+vn3//r59//6+ff/+ujo//hKXv/5a3z/+X+N//hEWv/5n6j/+vf1//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//r59//66en/+auz//r59//6+ff/+vn3//r59//6+ff/+vLx//mzuv/5l6L/+ba9//r19P/6+ff/+vn3//r59//6+ff/+vn3//r39f/68O//+YeT//rW2f/5tLv/+uTl//mCj//66en/+dze//hneP/5sLj/+vj2//r59//6+ff/+vn3//ro6P/5qLH/+Zei//rFyv/69vX/+vn3//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//ry8f/5maP/+rG4//rx8P/5tr3/+urq//mcpv/5xsr/+Y+b//hrfP/66en/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//rN0f/6n6j/+vPy//rx8P/5tr3/+uvq//mkrv/55+f/+Z2n//hbbf/68O//+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//ro6P/60tX/+vn3//rq6v/5s7r/+vHw//mkrf/56en/+u/v//lygv/69vT/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//50tX/+YaT//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//rg4v/5s7v/+vn3//rg4f/5rbT/+vj2//mep//5gY7/+E5i//m3vv/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//62dv/+Zah//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//ri4//5rrX/5/Ly/8iir/+0xc//7/j3//ru7f/5pa7/+tDU//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//69vT/+u3t//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//rx8P/1o63/rYWZ/2WSqv8W5/r/lvL5//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//UzNP/UbTJ/xHk+P8M6f3/K+v8//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59/+i8/n/Fur9/xXg9P8V4PT/DOn9/+/49//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59/+o8/n/Ger9/2yLo/9SpLv/F+X5//P59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//O9vj/Jev8/51cdv98fJX/VePx//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//5+ff/fPH6/65Tbv+jZX3/17/I//rl5f/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/9fn3/91tgP/lfIz/9k9j//ljdP/69vT/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//lufv/5foz/+s3R//mBjv/6yMz/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vPy//rW2f/5srn/+a+2//rZ2//69PP/+vn3//r59//6+ff/+vn3//r59//6+Pb/+t/g//mWof/5g5D/+r3D//rx8P/52tz/+tnb//r59//6+ff/+vn3//r59//6+ff/+vn3//mXov/5laD/+ufn//rj5P/5rbX/+vb0//r59//6+ff/+vn3//r59//6+ff/+vn3//rX2f/5k5//+YKQ//rDyf/68fD/+tnb//rQ0//6+ff/+vn3//r59//66+v/+X+N//hFWv/4ZHX/+GZ4//hPY//5pa7/+vX0//r59//6+ff/+vn3//r59//5yc7/+Ftt//mAjv/5lqH/+XSD//mDkf/5rrb/+bC3//r59//6+ff/+vn3//r59//6+ff/+vn3//rKzv/5hZL/+t7f//rv7//5tLv/+uzr//r59//6+ff/+vn3//r59//6+ff/+sHG//lVaP/5hJL/+Zei//lxgf/5m6X/+a+2//mfqf/6+ff/+vn3//r59//5qbL/+Etg//ra3P/68O//+vHw//rLz//5Y3X/+uHi//r59//6+ff/+vn3//rs7P/5e4n/+cLH//r39f/6+ff/+vHw//mZo//5V2r/+a61//r59//6+ff/+vn3//r59//6+ff/+vn3//rp6f/4a3z/+Fdq//m8wv/5sbn/+uLj//r59//6+ff/+vn3//r59//65eb/+FFk//rS1f/69/X/+vn3//rr6//5fYv/+XuJ//mfqf/6+ff/+vn3//r59//65eX/+ujp//r59//6+ff/+vn3//ry8f/4dIT/+tPW//r59//6+ff/+vn3//rO0v/5i5j/+vX0//r59//6+ff/+vn3//rl5f/5QVf/+Zul//r59//6+ff/+vn3//r59//6+ff/+vf2//m6wP/5jZj/+WJz//hjdf/5ub//+tbY//r59//6+ff/+vn3//r59//5oKr/+a+3//r59//6+ff/+vn3//r59//60dT/+CI8//mfqf/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//rx8P/4coH/+tTX//r59//6+ff/+vn3//meqP/5vsP/+vn3//r59//6+ff/+vn3//r39f/5go//+Z+p//r59//6+ff/+vn3//r59//6+ff/+sbK//mUn//64+T/+VZp//l/jf/50tb/+Z+p//r59//6+ff/+vn3//ry8f/5k57/+t7g//r59//6+ff/+vn3//r59//6+Pb/+Vps//mfqf/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//rLz//4W23/+uPk//r59//6+ff/+vn3//h2hf/54uP/+vn3//r59//6+ff/+vn3//r59//5qLD/+amx//r59//6+ff/+vn3//r59//6+ff/+YuX//ry8f/6+Pb/+XuJ//hhc//5xsv/+YOQ//r59//6+ff/+vn3//ro6P/5maP/+urq//r59//6+ff/+vn3//r59//6+ff/+ZWh//mfqf/6+ff/+vn3//r59//6+ff/+vn3//rm5v/5vML/+XqI//g5T//5sLf/+vj2//r59//6+ff/+vn3//hjdP/68fD/+vn3//r59//6+ff/+vn3//r59//5t77/+a+2//r59//6+ff/+vn3//r59//68/L/+YyY//r08v/50dT/+ba9//mLl//5tLv/+aew//rU1v/6+ff/+vn3//rj5P/5maP/+u/u//r59//6+ff/+vn3//r59//6+ff/+a62//mgqf/6+ff/+vn3//r59//6+ff/+svP//hZbP/5anv/+Zqk//rX2f/6+ff/+vn3//r59//6+ff/+vn3//hmd//67Oz/+vn3//r59//6+ff/+vn3//r59//5s7r/+be+//r59//6+ff/+vn3//r59//5ys7/+b3D//nIzP/5jJj/+aSt//rX2v/5tLv/+ufn//mTnv/6+ff/+vn3//rk5P/5lqH/+u3t//r59//6+ff/+vn3//r59//6+ff/+aix//mqs//6+ff/+vn3//r59//68vH/+EVa//m1vP/67+//+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//l+jP/51tj/+vn3//r59//6+ff/+vn3//r59//5n6n/+s/S//r59//6+ff/+vn3//r59//5sbj/+t/g//mXov/66+r/+vn3//rt7P/5tLv/+u7t//mGk//69vT/+vn3//rq6v/5k57/+ubm//r59//6+ff/+vn3//r59//6+ff/+YaT//nLz//6+ff/+vn3//r59//519n/+E5i//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//mstP/5pq7/+vj2//r59//6+ff/+vn3//rz8v/5j5v/+tvd//r59//6+ff/+vn3//ru7f/5r7f/+uzr//mGk//6+ff/+vn3//r39f/5tbz/+uTl//m3vv/50dT/+vn3//r19P/5jJj/+tDU//r59//6+ff/+vn3//r59//68vH/+FVo//r19P/6+ff/+vn3//r59//53d7/+EZc//r19P/6+ff/+vn3//rv7v/5trz/+uzs//r59//6+ff/+vn3//rb3f/5fIr/+urq//r59//6+ff/+vn3//rO0f/5iJT/+u/u//r59//6+ff/+vn3//rh4v/5sLf/+ujp//mWoP/6+ff/+vn3//r59//5tLz/+uLj//re3//5tLv/+vn3//r59//5ucD/+XyL//r39f/6+ff/+vn3//r49v/5r7b/+ZGd//r59//6+ff/+vn3//r59//69vT/+FVo//mAjv/68PD/+vPx//mGk//5aHn/+u3t//r59//6+ff/+vn3//r19P/5kZ3/+YiV//r49v/6+ff/+t/g//hOYv/5wsf/+vn3//r59//6+ff/+vn3//nBx//5xsv/+ba9//nKzf/6+ff/+vn3//r59//5xMn/+c3Q//rm5v/5sbj/+vTz//r59//68/L/+XOD//mLmP/69vT/+vn3//rQ1P/5YnT/+tzd//r59//6+ff/+vn3//r59//6+ff/+uXl//hIXf/4LET/+CdA//hKXv/61tn/+vn3//r59//6+ff/+vn3//r59//68O//+Wt8//hFWv/4XG//+DJJ//mosP/6+ff/+vn3//r59//6+ff/+vn3//mIlP/68vH/+YqW//r29P/6+ff/+vn3//r59//65eb/+aSu//r08//5tLv/+ufn//r59//6+ff/+vTz//hidP/4TGD/+Fxv//g5UP/6t77/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//ry8P/5ztL/+c3Q//ry8P/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vf1//nHy//5srn/+tnb//r59//6+ff/+vn3//r59//6+ff/+vn3//qstP/6+ff/+q+3//r59//6+ff/+vn3//r59//6+Pb/+srO//r59//6293/+u/u//r59//6+ff/+vn3//rz8f/5w8j/+bG5//rc3v/6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//rz8v/6+ff/+vPy//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3//r59//6+ff/+vn3/wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==
--#

--% C:/tmp/hapus/nda01/react-antd/assets/floor.json
{
  "headers": [
    "",
    "id",

    "name",


    "delete"
  ],
  "widths": {
    "show": 50,
    "id": 30,
    "hapus": 30,
    "normal": 150
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/assets/location.json
{
  "headers": [
    "",
    "id",

    "name",


    "delete"
  ],
  "widths": {
    "show": 50,
    "id": 30,
    "hapus": 30,
    "normal": 150
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/assets/measurement.json
{
  "headers": [
    "",
    "id",

    "name",


    "delete"
  ],
  "widths": {
    "show": 50,
    "id": 30,
    "hapus": 30,
    "normal": 150
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/assets/menu.json
[
  {
    "label": "Contoh Menu Lengkap",
    "children": [
      {
        "label": "Master",
        "children": [
          {
            "label": "Sub General",
            "children": [
              {
                "label": "Company"
              },
              {
                "label": "Fund",
                "link": "fund"
              },
              {
                "label": "Master Value",
                "link": "master-value"
              },
              {
                "label": "Activity"
              }
            ]
          },
          {
            "label": "Sub Accounting",
            "children": [
              {
                "label": "Account",
                "link": "account"
              },
              {
                "label": "Company Account Trading"
              }
            ]
          },
          {
            "label": "Sub Customer Service",
            "children": [
              {
                "label": "Black List Name"
              },
              {
                "label": "High Risk Monitoring",
                "link": "highriskmonitoring"
              }
            ]
          },
          {
            "label": "Sub Transaction",
            "children": [
              {
                "label": "AUM",
                "link": "aum"
              },
              {
                "label": "Sector",
                "link": "sector"
              }
            ]
          }
        ]
      },
      {
        "label": "Users",
        "link": "user"
      },
      {
        "label": "Security Setup",
        "link": "securitysetup"
      }
    ]
  },


  {
    "label": "Sensor",
    "children": [
      { "label": "Create", "link": "sensor" },
      { "label": "Read", "link": "sensor-list" },
      { "label": "Update", "link": "sensor" },
      { "label": "Delete", "link": "sensor" }
    ]
  },


  {
    "label": "System",
    "children": [
      { "label": "Create", "link": "system" },
      { "label": "Read", "link": "system" },
      { "label": "Update", "link": "system" },
      { "label": "Delete", "link": "system" }
    ]
  },


  {
    "label": "Measurement",
    "children": [
      { "label": "Create", "link": "measurement" },
      { "label": "Read", "link": "measurement" },
      { "label": "Update", "link": "measurement" },
      { "label": "Delete", "link": "measurement" }
    ]
  },


  {
    "label": "Equipment",
    "children": [
      { "label": "Create", "link": "equipment" },
      { "label": "Read", "link": "equipment" },
      { "label": "Update", "link": "equipment" },
      { "label": "Delete", "link": "equipment" }
    ]
  },


  {
    "label": "Room",
    "children": [
      { "label": "Create", "link": "room" },
      { "label": "Read", "link": "room" },
      { "label": "Update", "link": "room" },
      { "label": "Delete", "link": "room" }
    ]
  },


  {
    "label": "Floor",
    "children": [
      { "label": "Create", "link": "floor" },
      { "label": "Read", "link": "floor" },
      { "label": "Update", "link": "floor" },
      { "label": "Delete", "link": "floor" }
    ]
  },


  {
    "label": "Location",
    "children": [
      { "label": "Create", "link": "location" },
      { "label": "Read", "link": "location" },
      { "label": "Update", "link": "location" },
      { "label": "Delete", "link": "location" }
    ]
  },


  {
    "label": "Point",
    "children": [
      { "label": "Create", "link": "point" },
      { "label": "Read", "link": "point" },
      { "label": "Update", "link": "point" },
      { "label": "Delete", "link": "point" }
    ]
  },


  {
    "label": "Building",
    "children": [
      { "label": "Create", "link": "building" },
      { "label": "Read", "link": "building" },
      { "label": "Update", "link": "building" },
      { "label": "Delete", "link": "building" }
    ]
  },


  {
    "label": "News",
    "children": [
      { "label": "Create", "link": "news" },
      { "label": "Read", "link": "news-list" },
      { "label": "Update", "link": "news" },
      { "label": "Delete", "link": "news" }
    ]
  },


  {
    "label": "Dashboard",
    "link": "dashboard"
  }

]


--#

--% C:/tmp/hapus/nda01/react-antd/assets/news.json
{
  "headers": [
    "",
    "id",

    "title",
    "link",
    "summary",
    "content",
    "tags",
    "images",


    "delete"
  ],
  "widths": {
    "show": 50,
    "id": 30,
    "hapus": 30,
    "normal": 150
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/assets/point.json
{
  "headers": [
    "",
    "id",

    "name",


    "delete"
  ],
  "widths": {
    "show": 50,
    "id": 30,
    "hapus": 30,
    "normal": 150
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/assets/room.json
{
  "headers": [
    "",
    "id",

    "name",


    "delete"
  ],
  "widths": {
    "show": 50,
    "id": 30,
    "hapus": 30,
    "normal": 150
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/assets/sensor.json
{
  "headers": [
    "",
    "id",

    "building",
    "smart_building",
    "sensor_id",
    "min_value",
    "max_value",
    "yellow",
    "red",
    "interval",
    "stopper",
    "stop",


    "delete"
  ],
  "widths": {
    "show": 50,
    "id": 30,
    "hapus": 30,
    "normal": 150
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/assets/system.json
{
  "headers": [
    "",
    "id",

    "name",


    "delete"
  ],
  "widths": {
    "show": 50,
    "id": 30,
    "hapus": 30,
    "normal": 150
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/components/App/index.js
import React, { Suspense, useEffect, useState } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import { hot } from 'react-hot-loader/root';

const LoginForm = React.lazy(() => import('../Login'));
import BaseLayout from '../Layout/BaseLayout';

import SessionProvider from 'context/SessionProvider';
import ToolbarContext from 'context/ToolbarContext';

import classNames from 'classnames';
import './style.css'
import AuthenticatedRoute from '../Route/AuthenticatedRoute';

const GlobalError = ({ message = 'Terjadi Kesalahan Pada Aplikasi' }) => (
  <div
    className={classNames([
      'd-flex',
      'flex-grow-1',
      'align-items-center',
      'align-content-center',
      'justify-content-center',
      'global-error',
    ])}>
  <div>{message}</div>
  </div>
)

const NotFound = () => <GlobalError message="Error 404 Not Found" />;

const FullPage = ({ message = 'Now Loading.' }) => (
  <div
      className={classNames([
        'd-flex',
        'flex-grow-1',
        'align-items-center',
        'align-content-center',
        'justify-content-center',
        'global-error',
      ])}>
      <div className="spinner-border" role="status" />
      <div>{message}</div>
  </div>
);

const App = () => {

  // useEffect(() => {
  //   SocketHandler()
  // }, []);

  const [Toolbar, setToolbar] = useState(null);

  return <SessionProvider>

    <ToolbarContext.Provider value={{
      ToolbarComponent: Toolbar,
      setToolbar,
    }}>

      <Router>
        <Suspense fallback={<FullPage />}>
          <Switch>
            <Route path="/login" exact component={LoginForm} />
            <AuthenticatedRoute path="/" component={BaseLayout} />
            <Route path="/404" exact component={NotFound} />
            <Route component={NotFound} />
          </Switch>
        </Suspense>
      </Router>

    </ToolbarContext.Provider>

  </SessionProvider>;
}

export default hot(App);

--#

--% C:/tmp/hapus/nda01/react-antd/components/App/style.css
.global-error {
  height: 100%;
}


--#

--% C:/tmp/hapus/nda01/react-antd/components/common/BoModule/BoModule.css
.custom-filter-dropdown {
  padding: 8px;
  border-radius: 6px;
  background: #fff;
  box-shadow: 0 1px 6px rgba(0, 0, 0, .2);
}

.custom-filter-dropdown input {
  width: 130px;
  margin-right: 8px;
}



--#

--% C:/tmp/hapus/nda01/react-antd/components/common/BoModule/BoModule.js
import React, { useEffect, useState } from 'react';

import { 
  Button, Drawer, Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,
  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';

import './BoModule.css';

function column_sorter(a, b, column) {
  // console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`)
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    return b[column].toLowerCase() > a[column].toLowerCase();
      
  return b[column] > a[column];
}

const BoModule = ({  
  json_data,  
  ContentComponent = null,
  close_is_reload = false,
  cacheImage = false,
  isPending = false,
  modal_title = '',
  module_title = 'Module',
  paymentReference = false,
  resource_path,
  selectionCallback = () => {},
  recordTransformer = record => record
}) => {

  const [drawerVisible, setDrawerVisible] = useState(false);
  const [table_data, set_table_data] = useState([]);
  const [filter_table_data, set_filter_table_data] = useState(null);
  const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

  const [api, contextHolder] = notification.useNotification()
  const openError = (judul, isi, placement='topRight') => {
    api.error({
      message: judul,
      description: isi,
      placement,
    });
  }
  const openSuccess = (judul, isi, placement='topRight') => {
    api.success({
      message: judul,
      description: isi,
      placement,
    });
  }

  const handleDelete = record => {
    const key = record.key;
    const table_data_temp = [...table_data].filter(item => item.key !== key);
    let column_primary = 'id';
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    }

    console.log(`berhasil hapus ${kunci}`);

    // else if (record.hasOwnProperty('orderno')) {
    //   kunci = record.orderno;
    //   column_primary = 'orderno';
    // }
    // else {
    //   console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
    //   return;
    // }

    // let _deleteUrl = `${resource_path}/${kunci}`;
    // if (delete_url_mapper.hasOwnProperty(resource_path)) {
    //   if (column_primary !== 'id') // bo/module/kv/column/kunci
    //     _deleteUrl = `${delete_url_mapper[resource_path]}/${column_primary}/${kunci}`
    //   else // bo/module/kunci
    //     _deleteUrl = `${delete_url_mapper[resource_path]}/${kunci}`
    // }
    // setDeleteUrl(_deleteUrl);
    
    // console.log(`hapus table key ${key} dari ${JSON.stringify(record)} 
    //     => resource_path: ${resource_path}
    //     => hapus: ${_deleteUrl}, jumlah baris dari ${table_data.length} ke ${table_data_temp.length}`);
    
    // if (deleteUrl === _deleteUrl) {
    //   console.log(`deleting ${deleteUrl}`);
    //   deleteResource({},
    //     () => {
    //       console.log(`berhasil hapus ${kunci}`);
    //       set_table_data(table_data_temp);
    //       getResourceData({}, successHandler);
    //       openSuccess('Berhasil', `Berhasil hapus id ${kunci}`);
    //     },
    //     err => {
    //       console.log(`gagal hapus ${kunci}`);
    //       openError('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
    //     }
    //   );
    // } else {
    //   console.log(`NOT+RE deleting ${deleteUrl} as ${_deleteUrl}`);
    //   deleteResource(
    //     {
    //       url: useUrlBuilder(_deleteUrl)
    //     },
    //     () => {
    //       console.log(`berhasil hapus ${kunci}`);
    //       set_table_data(table_data_temp);
    //       getResourceData({}, successHandler);
    //       openSuccess('Berhasil', `Berhasil hapus ${column_primary} ${kunci}`);
    //     },
    //     err => {
    //       console.log(`gagal hapus ${kunci}`);
    //       openError('Gagal hapus...', `Tidak berhasil hapus ${column_primary} ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
    //     }
    //   );
    // }   
  }

  const table_header = json_data.headers.map((column, index) => {

    if (column === "") {
      return {
        title: "Show",
        fixed: 'left',
        width: 100,
        render: data => <Button onClick={() => {
          set_modal_bomodule_content(data);
          setDrawerVisible(true);
        }}>Show </Button>,
      };

    } else if (column === "delete") {
      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: 60,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {
      
      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? 75 : 150,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  // const modalSelectionHandler = (selections) => {
  //   set_modal_bomodule_selected(selections)
  //   // set_modal_bomodule(true)
  //   // selection bisa kosong jk dia unselect
  //   if (selectionCallback !== undefined) {            
  //     // kirim id dari record, bukan index selection
  //     let id_list = []
  //     selections.forEach(index => {
  //       let ketemu = table_data.find(record => record.key == index);
  //       if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
  //         id_list .push(ketemu.id + "," + ketemu.id_user);
  //       else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
  //         id_list .push(ketemu.orderno + "," + ketemu.customerno);
  //     })
  //     if (id_list.length > 0) {
  //       selectionCallback(id_list);
  //       console.log(`selection ${id_list}`);
  //     }
  //   }
  //   console.log(`bomodule selected: ${selections}, ${typeof(selections)}, siap masuk cc: ${modal_bomodule_selected}.`)
  // }

  function searchTable(value) {
    let saring = table_data.filter(o =>
      Object.keys(o).some(k =>
        String(o[k])
          .toLowerCase()
          .includes(value.toLowerCase())
      )
    )
    set_filter_table_data(saring);
  }

  const getResourceData = useAxios({ url: resource_path, });
  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  }

  useEffect(() => {
    getResourceData({}, successHandler);
  }, []);

  return <>
    <Table
      size="small"
      columns={[
        {
          title: '',
          key: 1,
          dataIndex: 'action',
          width: '50px',
          render: () => <Button icon={<ReloadOutlined />} 
            onClick={() => {
            set_filter_table_data(table_data)
            getResourceData({}, successHandler)
            }}>
              Reload
            </Button>
        },

        {
          title: '',
          key: 2,
          dataIndex: 'action',
          width: '200px',
          render: () => <Input.Search 
            style={{ margin: "0 20px 0 0" }}
            placeholder="Cari lalu tekan Enter..."
            enterButton
            onSearch={searchTable}
            />
        },
      ]}
      dataSource={[{key:0}]}
      pagination={false}
      />

    <SimpleTable 
      header={table_header} 
      body={filter_table_data === null ? table_data : filter_table_data} 
      selectCallback={modalSelectionHandler} />

    {contextHolder}
  </>;
}

export default BoModule;



--#

--% C:/tmp/hapus/nda01/react-antd/components/common/Table/SimpleTable.js
import React, { useState } from 'react';
import { Table } from 'antd';

const SimpleTable = ({
  header,
  body,
  selectCallback = null,
  tableSelection = true,
}) => {

  const [selectedRows, setSelectedRows] = useState([])

  // ini peroleh semua yg terselect
  const rowSelection = {
    selectedRows,
    onChange: (pilihan) => {
      setSelectedRows(pilihan)
      // console.log(`#1 selection now: ${selectedRows} dg ${pilihan}`)
      if (selectCallback) selectCallback(pilihan)
    }
  }

  const modifySelection = (record) => {
    // selectedRows.length > 0 ? [...selectedRows] : []
    const newrows = [...selectedRows]; 
    if (newrows.indexOf(record.key) >= 0) {
      newrows.splice(newrows.indexOf(record.key), 1);
    } else {
      newrows.push(record.key);
    }
    setSelectedRows(newrows);
    console.log(`#2 selection now: ${selectedRows} dg ${newrows}`);
  }
  
  // ini row yg diklik (1 saja)
  const onRowSelection = (record) => ({
      onClick: () => {
        // console.log(`something is being clicked ${JSON.stringify(record)}`)
        modifySelection(record);
        // console.log(`selected: ${selectedRows}`)
      }
  })

  if (tableSelection) {
    return <Table
      bordered      
      columns={header}
      dataSource={body}
      rowSelection={rowSelection}
      size='small'
      scroll={{ x: 1500, y: 300 }}
      // scroll={{ y: 240 }}
      // components={components}
      // pagination={{ position: ['topLeft', 'bottomRight'], pageSize: 10 }}
      pagination={{ position: ['topLeft', 'bottomRight'] }}
      // pagination={{ position: 'both', pageSize: 10 }}
      
      // onRow={onRowSelection}
    >
    </Table>;
  } else {
    return (<Table columns={header} dataSource={body} />);
  }
}

export default SimpleTable;



--#

--% C:/tmp/hapus/nda01/react-antd/components/common/TabPage/index.js
import React, { useState } from 'react';
import { 
  Tabs 
} from 'antd';


const TabPage = ({
  tabs_data,
  // tabpos = 'left',
  // tabpos = 'bottom',
  tabpos = 'top',
}) => {
  return (
    <div className="card-container">
      <Tabs type="card" tabPosition={tabpos}>
        {tabs_data.map(
          (tab_page, index) => {
            let icon_title = tab_page.icon ? <span>{tab_page.icon} {tab_page.title}</span> : tab_page.title
            return <Tabs.TabPane tab={icon_title} key={index}>
              {tab_page.component}
            </Tabs.TabPane>
          }
        )}
      </Tabs>
    </div>
  );
}

export default TabPage;



--#

--% C:/tmp/hapus/nda01/react-antd/components/common/TabPage/style.css
.card-container p {
  margin: 0;
}

/* .card-container>.ant-tabs-card .ant-tabs-content {
  height: 120px;
  margin-top: -16px;
}

.card-container>.ant-tabs-card .ant-tabs-content>.ant-tabs-tabpane {
  background: #fff;
  padding: 16px;
}

.card-container>.ant-tabs-card>.ant-tabs-nav::before {
  display: none;
}

.card-container>.ant-tabs-card .ant-tabs-tab,
[data-theme='compact'] .card-container>.ant-tabs-card .ant-tabs-tab {
  border-color: transparent;
  background: transparent;
}

.card-container>.ant-tabs-card .ant-tabs-tab-active,
[data-theme='compact'] .card-container>.ant-tabs-card .ant-tabs-tab-active {
  border-color: #fff;
  background: #fff;
}

#components-tabs-demo-card-top .code-box-demo {
  background: #f5f5f5;
  overflow: hidden;
  padding: 24px;
}

[data-theme='compact'] .card-container>.ant-tabs-card .ant-tabs-content {
  height: 120px;
  margin-top: -8px;
}

[data-theme='dark'] .card-container>.ant-tabs-card .ant-tabs-tab {
  border-color: transparent;
  background: transparent;
}

[data-theme='dark'] #components-tabs-demo-card-top .code-box-demo {
  background: #000;
}

[data-theme='dark'] .card-container>.ant-tabs-card .ant-tabs-content>.ant-tabs-tabpane {
  background: #141414;
}

[data-theme='dark'] .card-container>.ant-tabs-card .ant-tabs-tab-active {
  border-color: #141414;
  background: #141414;
} */



--#

--% C:/tmp/hapus/nda01/react-antd/components/context/SessionContext.js
import React from 'react';

const SessionContext = React.createContext({
  authenticated: false,
  token: null,

  email: null,
  username: null,
  phone: null,
  role: null,

  data: [],
  setSession: (stateobj) => {},
  sessionLogout: () => {},
});

export default SessionContext;



--#

--% C:/tmp/hapus/nda01/react-antd/components/context/SessionProvider.js
import React, { useState, useEffect } from 'react';
import { hot } from 'react-hot-loader/root';
import SessionContext from './SessionContext';

const sessionName = process.env.SESSION_NAME || 'default-session-name';

const SessionProvider = ({ children }) => {

  // ini bikin token yg sdh ada, masuk di initial state
  // sewaktu nilai lain null/false
  // maka, AuthenticatedRoute hrs berbasis authenticated instead of token
  const initializedToken = localStorage.getItem(sessionName) || null;
  const [state, setState] = useState({
    authenticated: false,
    token: initializedToken,

    username: null,
    email: null,
    role: null,
    phone: null,
  });

  useEffect(() => {
    if (state.token !== initializedToken) {
      localStorage.setItem(sessionName, state.token);
    }
  }, [state.token]);

  const sessionLogout = () => {
    
    localStorage.removeItem(sessionName);
    let terhapus = localStorage.getItem(sessionName);
    console.log(`logging out locally...pastikan sudah null [${terhapus}].`);
    // setState({ token: null, });
    setState({});

  };

  return (
  <SessionContext.Provider
    value={{
      ...state,
      setSession: setState,
      sessionLogout,
    }}>
    {children}
  </SessionContext.Provider>
  );
};

export default hot(SessionProvider);



--#

--% C:/tmp/hapus/nda01/react-antd/components/context/ToolbarContext.js
import React from 'react';

const ToolbarContext = React.createContext({
});

export default ToolbarContext;



--#

--% C:/tmp/hapus/nda01/react-antd/components/Layout/BaseLayout.css
.main-section {
  background-color: #e1e1e1;
  box-shadow: -3px -3px 7px #fffff7, 3px 3px 5px rgba(90,100,120,.2);
  
  margin-top: 50px;
  
  margin-left: var(--left-mainbar-percent);
  transition: all .5s ease;

  width: 100%;
  height: 100%;
  border: 1px solid red;
  

  padding: 15px;
}

.main-section.geser {
  margin-left: calc(var(--left-mainbar-percent) + var(--left-distance));
}



--#

--% C:/tmp/hapus/nda01/react-antd/components/Layout/BaseLayout.js
import React, { Fragment, useEffect, useState } from 'react';
import { hot } from 'react-hot-loader/root';
import { Route, Switch, withRouter } from 'react-router-dom';
import MainRoutes from '@/Route/Routes';
import './BaseLayout.css';
import Sidebar from './Sidebar';
import Header from './Header';
import Floating from './Floating';

const BaseLayout = ({ history, children }) => {

  const [show_menu, set_show_menu] = useState(false);

  function toggle_menu() {
    set_show_menu(!show_menu);
  }

  useEffect(function() {
    history.push('/dashboard');
  }, []);

  return <Fragment>

    <Header />

    <Sidebar active_classname={show_menu ? 'layout-sidebar active' : 'layout-sidebar'} toggler={toggle_menu} />
    
    <main className={'main-section' + (show_menu?' geser':'')}>
      
      {children}

      {MainRoutes.map(
        (item, index) => {
          return (<Route key={index} path={item.path} component={item.component} />)
        }
      )}

    </main>

    <Floating active_classname={show_menu ? 'layout-floating active' : 'layout-floating'} onClick={toggle_menu} />

  </Fragment>;
}

export default hot(withRouter(BaseLayout));



--#

--% C:/tmp/hapus/nda01/react-antd/components/Layout/Floating/index.js
import React, { useContext } from 'react';
import { Button, Tooltip } from 'antd';
import { SketchOutlined } from '@ant-design/icons';

import './style.css';

export default ({
  active_classname,
  onClick
}) => {
  return (<div className={active_classname}>
    <Tooltip title="Toggle sidebar menu">
      <Button type="primary" shape="circle" icon={<SketchOutlined />} onClick={onClick} />
    </Tooltip>
  </div>);
}



--#

--% C:/tmp/hapus/nda01/react-antd/components/Layout/Floating/style.css
.layout-floating {
  position: fixed;
  bottom: 0px;
  left: 15px;
  width: 50px;
  height: 50px;
  transition: left .2s ease;
  z-index: 11;
}

.layout-floating.active {
  left: calc(15px + var(--left-distance));
}



--#

--% C:/tmp/hapus/nda01/react-antd/components/Layout/Header/index.js
import React, { useContext } from 'react';
import { 
    PageHeader,
    Popover,
    Statistic,
    Tooltip,
} from 'antd';
import { Menu, Dropdown, Button } from 'antd';

import SessionContext from 'context/SessionContext';
import ToolbarContext from 'context/ToolbarContext';
import Settings_Popup from '@/Setting/Settings_Popup';
import './style.css';

// import { useHistory } from 'react-router-dom';
// import { useHistory } from 'react-router';
import { withRouter } from 'react-router-dom';

const Header = ({
  history,
}) => {

  const session = useContext(SessionContext);
  const toolbar = useContext(ToolbarContext);

  function clearSession() {
    session.sessionLogout();
    // clean up forage
    // forageHousekeeping();
    console.log(`Header => Session cleared...`);
    history.push('/');
  }

  function printSession() {
    console.log(`${JSON.stringify(session)}`);
  }

  const DropdownChoice = (<Menu>
    <Menu.Item key="1">
      {
        <>
        <h1>{session.username}</h1>
        <br/>
        <h4>{session.email}</h4>
        <br/>
        <h4>{session.phone}</h4>
        <br/>
        <h4>{session.role}</h4>
        </>
      }
    </Menu.Item>
  </Menu>);

  let UserDropdown = () => (<Dropdown overlay={DropdownChoice} placement="bottomRight">
    <i className='fa fa-user kiri'></i>
  </Dropdown>);

  const Settings = () => (<Popover placement="bottom" title={<span>Settings</span>} content={Settings_Popup} trigger="click">
    <Tooltip title='Setting' key="5"><i className='fa fa-cogs kiri'></i></Tooltip>
  </Popover>);

  return (<PageHeader
    className="layout-header"
    // onBack={() => null}
    title="Judul"
    subTitle="Subjudul"
    avatar={{ src: 'favicon.ico', shape: 'square' }}

    extra={[
      <Tooltip title='Pencarian' key="1"><i className='fa fa-search kiri'></i></Tooltip>,
      <Tooltip title='Notifikasi umum' key="2"><i className='fa fa-bell kiri' onClick={printSession}></i></Tooltip>,
      <UserDropdown key="3"/>,
      <Settings key="5"/>,
      <Tooltip title='Klik untuk logout' key="4"><i className='fa fa-sign-out kanan' onClick={clearSession}></i></Tooltip>,
    ]}
>
    {toolbar.ToolbarComponent}

    {/* <Clock />
    <Calendar /> */}

  </PageHeader>);
}

export default withRouter(Header);


--#

--% C:/tmp/hapus/nda01/react-antd/components/Layout/Header/style.css
.layout-header {
  background-color: rgba(141, 128, 235, 0.8);
  padding: 5px;

  font-size: .8rem;
}

.tombol {
  position: absolute;
  right: 0;
  padding: 10px;
}

.kiri, .kanan {
  margin: 5px;
  padding: 5px;
  transform: scale(1.5);
}

.kanan:hover, .kiri:hover {
  filter: hue-rotate(90deg);
}



--#

--% C:/tmp/hapus/nda01/react-antd/components/Layout/Sidebar/index.js

import React, { useContext } from 'react'
import classNames from 'classnames'
import './style.css'
import { Menu } from '@/Menu';

export default ({
    active_classname,
    toggler,
}) => {
  return (<div className={active_classname}>
    <Menu toggler={toggler} />
  </div>);
}



--#

--% C:/tmp/hapus/nda01/react-antd/components/Layout/Sidebar/style.css
.layout-sidebar {
  position: fixed;
  top: 0;
  bottom: 0;
  left: var(--left-sidebar-percent);
  width: var(--left-distance);
  box-shadow: -3px -3px 7px #fffff7, 3px 3px 5px rgba(90,100,120,.2);
  transition: left .2s ease;
  z-index: 10;
}

.layout-sidebar.active {
  left: calc(var(--left-sidebar-percent) + var(--left-distance));
}



--#

--% C:/tmp/hapus/nda01/react-antd/components/Login/index.js
import React, { Suspense, useContext, useEffect, useRef, useState } from 'react';
import { 
  Button, 
  Checkbox,
  Form, 
  Input,   
  notification,
} from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';
import SessionContext from '../context/SessionContext';
import './login.css';

import useAxios from '#/utils/useAxios';
import { registerRefreshJob } from '#/utils/authUtils';
import config from '#/config';

const LoginForm = (props) => {

  const session = useContext(SessionContext);

  const [api, contextHolder] = notification.useNotification();
  const openNotification = (judul, isi, placement='bottomRight') => {
    api.error({
      message: judul,
      description: isi,
      placement,
    });
  };

  const loginAxios = useAxios(config.backend.paths.login);
  // const mounted = useRef();

  useEffect(
    function() {
      // if (!mounted.current) {
      //   if (props.history) {
      //     if (session.authenticated) {
      //       console.log('User is authenticated...');
      //       props.history.push('/');
      //     }
      //   }
      // }

      if (session.authenticated) {
        console.log('User is authenticated...');
        props.history.push('/');
      }

    },
    [session]
    // []
  );

  const onFinish = values => {

    console.log(`Data utk login: ${JSON.stringify(values)}`);

    loginAxios(
      { 
        data: {
          email: values.email,
          password: values.password,
        }
      },

      response => {
        // apps/user/auth/provider/login
        // data: {
        //   jwt: { accessToken, refreshToken, expTime },
        //   token: doGenToken(),
        //   email: pengguna.email,
        //   username: pengguna.username,
        //   // phone: pengguna.phone,
        //   // role: pengguna.role,
        // },
        const { token: mainToken, jwt: jwt_data, ...responseData } = response.data;

        const { accessToken, refreshToken, expTime } = jwt_data;        
        localStorage.setItem(config.authentication.storage.access_token, accessToken);
        localStorage.setItem(config.authentication.storage.refesh_token, refreshToken);
        localStorage.setItem(config.authentication.storage.expiry_token, expTime);

        console.log(`
          berhasil login, kita lihat data localStorage
          original exptime: ${expTime}
          nilai epoch expiry: ${localStorage.getItem(config.authentication.storage.expiry_token)}
          epoch expiry: ${
            new Date(localStorage.getItem(config.authentication.storage.expiry_token)*1000).toLocaleString()
          }
          berapa lama lagi tuh?
        `);
        delete response.data.jwt;
        localStorage.setItem(config.authentication.storage.user, JSON.stringify(response.data));

        let sessionData = {
          authenticated: true,
          token: mainToken && mainToken !== "" ? mainToken : accessToken,
          ...responseData
        }
        session.setSession(sessionData);
        console.log(`sukses login: ${JSON.stringify(sessionData)}`);
        // props.history.push('/');
        registerRefreshJob();
      },

      error => {
        let isi = JSON.stringify(error);
        console.log(`gagal login: ${isi}`);
        openNotification(`gagal login`, isi);
      },

    );
  };

  return (<div className="login-container-div">
    <Form
      name="normal_login"
      className="login-form"
      initialValues={{
        remember: true,
      }}
      onFinish={onFinish}>

      <Form.Item
        name="email"
        rules={[
          {
            required: true,
            message: 'Please input your Email!',
          },
        ]}>

        <Input 
          prefix={<UserOutlined className="site-form-item-icon" />} 
          placeholder="Email" />

      </Form.Item>

      <Form.Item
        name="password"
        rules={[
          {
            required: true,
            message: 'Please input your Password!',
          },
        ]}>

        <Input
          prefix={<LockOutlined className="site-form-item-icon" />}
          type="password"
          placeholder="Password"
        />

      </Form.Item>

      <Form.Item>
        
        <Form.Item name="remember" valuePropName="checked" noStyle><Checkbox>Remember me</Checkbox></Form.Item>
        <a className="login-form-forgot" href="">Forgot password</a>

      </Form.Item>

      <Form.Item>
        
        <Button type="primary" htmlType="submit" className="login-form-button">Log in</Button>
        {' '} Or <a href="">register now!</a>

      </Form.Item>

    </Form>

    {contextHolder}

  </div>);
}

export default LoginForm;



--#

--% C:/tmp/hapus/nda01/react-antd/components/Login/login.css

.login-container-div {
  width: 400px;
  height: 250px;

  margin: 150px auto;
  padding: 15px;

  background-color: rgba(33, 3, 248, .5);
  border-radius: 10px;

  box-shadow: 10px 15px 18px #888888;
}


--#

--% C:/tmp/hapus/nda01/react-antd/components/Menu/index.js
export { default as Menu } from './MainMenu';



--#

--% C:/tmp/hapus/nda01/react-antd/components/Menu/MainMenu.css
.menu-component {
  width: 100%;
  font-size: .5rem;
}


--#

--% C:/tmp/hapus/nda01/react-antd/components/Menu/MainMenu.js
import React, { useEffect, useState } from 'react';

// import { useHistory } from 'react-router-dom';
// import { useHistory } from 'react-router';
import { withRouter } from 'react-router-dom';

import { Switch, Menu, Button } from 'antd';
import {
  AppstoreOutlined,
  MenuUnfoldOutlined,
  MenuFoldOutlined,
  PieChartOutlined,
  DesktopOutlined,
  ContainerOutlined,
  MailOutlined,
} from '@ant-design/icons';

import MenuJson from 'assets/menu.json';
import './MainMenu.css';


const { SubMenu } = Menu;

const MainMenu = ({
  history,
  toggler,
  rootMenu=null,
}) => {
  // let history = useHistory();
  // const [theme, setTheme] = useState('dark')
  // const toggleTheme = (value) => setTheme(value ? 'dark' : 'light');

  function handleClick(e) {
    // console.log('click ', e, 'atau: props.link nya', e.item.props.link);
    if (e.item.props.link !== undefined) {
      history.push('/' + e.item.props.link);
      toggler();
    }
  }

  let counter=0;
  let CreateMenu = (parent, level=0) => {
    return parent.map( (item, index) => {
      // console.log(`oprek ${JSON.stringify(item)} level=${level} key=${level}-${index}-${counter}`)
      counter +=1;
      if (item.hasOwnProperty("children")) {
        return <SubMenu key={`${level}-${index}-${counter}`} icon={<AppstoreOutlined />} title={item.label}>
            
          {CreateMenu(item.children, level+1)}

        </SubMenu>
      } else {
        return <Menu.Item key={`${level}-${index}-${counter}`} icon={<PieChartOutlined />} link={item.link}>{item.label}</Menu.Item>;
      }
    });
  }

  let NewReturn = () => (
    <div className="menu-component">
      <Menu
        defaultSelectedKeys={['1']}
        defaultOpenKeys={['1-0-0']}        
        // theme={theme}
        // mode="inline"
        // inlineCollapsed={this.state.collapsed}
        // onClick={this.handleClick}
        onClick={handleClick}
      >

      {CreateMenu(rootMenu ? rootMenu : MenuJson)}

      </Menu>
    </div>
  );
  return <NewReturn />;
}

// export default MainMenu;
export default withRouter(MainMenu);



--#

--% C:/tmp/hapus/nda01/react-antd/components/Menu/Shortcut.js



--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Building/Building.js

import React, { useEffect, useState } from 'react';

import {
	Button,
	DatePicker,
	Divider,
	Drawer,
	Input, InputNumber ,
	Modal,
	Popover,
	Select,
	Space,
} from 'antd';
import {
	DesktopOutlined,
	DownOutlined, 
	UserOutlined,
	// HomeOutlined,
	// SettingFilled,
	// SmileOutlined,
	FileExcelOutlined,
	FilePdfOutlined,
	ReloadOutlined,
	ReloadFilled, 
	DeleteOutlined,
	DeleteFilled,
} from '@ant-design/icons';

import ToolbarContext from 'context/ToolbarContext';
import TabPage from 'common/TabPage';

import ReadList from './List';
import FormWrapper from './FormWrapper';

const Building = () => {
	const { setToolbar } = React.useContext(ToolbarContext);
	const [lokasiTab, setLokasiTab] = useState('top');
	const [drawerVisible, setDrawerVisible] = useState(false);
	// diisi oleh List wkt 'Show'
	const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

	const show_update = (data) => {
		set_modal_bomodule_content(data);
		setDrawerVisible(true);
	}

	let Toolbar = () => (<Space>
		<h1>Building</h1>
		<Button type="primary" 
			onClick = {				
				() => {
					set_modal_bomodule_content({});
					setDrawerVisible(true);
				}
			}>Create new</Button>
		{/* <Button type="default" disabled onClick={generateBlotter2}>Blotter Subscription</Button> */}
		{/* <Popover placement="bottom" title={<span>Pilih nasabah dan tanggal Blotter subscription</span>} content={Blotter_Popup} trigger="click"> */}
		{/* <Button disabled type="primary">Blotter Subscription</Button> */}
		{/* </Popover> */}			
	</Space>);

	useEffect(function() {
		setToolbar(<Toolbar />)
	}, []);

	return <>
		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'Create',
						icon: <DesktopOutlined />,
						component: <FormWrapper />
					},
					{
						title: 'Read',
						icon: <DesktopOutlined />,
						component: <ReadList show_update={show_update} />
					},
				]
			} />

		<Drawer
      title="Add Record"
      placement='right'      
      onClose={() => setDrawerVisible(false)}
      visible={drawerVisible}
      width={800}
      // closable={false}
      >

			<FormWrapper
				data_raw={modal_bomodule_content}
				onClose={() => setDrawerVisible(false)}
				/>

		</Drawer>
	
	</>;
};

export default Building;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Building/CreateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
// import moment from 'moment';

const CreateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit CreateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  // useEffect(() => {
  // }, [initialFormValues]);

  return <Form name='create_form' 
      // size='small'
      form={form_konek_provider}
      className='create_form'
    >
    <Row gutter={[8, 16]}>
      <Col span='24'>
        
        {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>



<Form.Item name='building_id' label="Building_Id">
  <Input />
</Form.Item>



<Form.Item name='location_text' label="Location_Text">
  <Input />
</Form.Item>



<Form.Item name='lalo' label="Lalo">
  <Input />
</Form.Item>



<Form.Item name='description' label="Description">
  <Input />
</Form.Item>



<Form.Item name='notes' label="Notes">
  <Input />
</Form.Item>


      </Col>
    </Row>

  </Form>;
}

export default CreateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Building/FormProvider.js

import React, { useEffect, useState } from 'react';

import {
  Button,
  Checkbox,
  Form,
  notification,
} from 'antd';

import useAxios from 'utils/useAxios';
import UpdateForm from './UpdateForm';
import CreateForm from './CreateForm';
import PubSub from 'pubsub-js';

const FormProvider = ({
  onClose,
  data_raw = {},
  submit_form = (values) => console.log(`submit FormProvider`),
}) => {

  const updateRecord = useAxios({ method: 'PATCH', });
  const createRecord = useAxios({ method: 'POST', path: 'building',  });
  const is_updating = Object.keys(data_raw).length > 0;

  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  return <Form.Provider onFormFinish={(name, {values, forms}) => {

    if (is_updating) {
      const { update_form } = forms;
      let updated_values = update_form.getFieldsValue();
      let diffs = {};
      for (let key in updated_values) {
        if (updated_values.hasOwnProperty(key)) {
          if (updated_values[key] !== data_raw[key]) {
            diffs[key] = updated_values[key];
          }
        }      
      }
      console.log(`update diffs: ${JSON.stringify(diffs)}`);
      let values_has_changed = Object.keys(diffs).length > 0;
      if (values_has_changed) {
        updateRecord(
          {
            // url: useUrlBuilder(`bo/bo_marketholiday/${updated_values.id}`),
            path: `building/${updated_values.id}`,
            data: diffs
          },

          response => {
            console.log(`sukses updateRecord => ${JSON.stringify(response)}`);
            berhasil(`sukses updateRecord [${JSON.stringify(response)}]`);
            PubSub.publish('<<Update:Record>>', response);
          },

          err => {
            console.log(`gagal updateRecord => ${JSON.stringify(err)}.`);
            gagal(`gagal updateRecord [${JSON.stringify(err)}]`);
          }
        );
      }

    } else {
      const { create_form } = forms;
      let created_values = create_form.getFieldsValue();
      console.log(`created values from onformfinish: ${JSON.stringify(values)} vs getfieldsvalue ${JSON.stringify(created_values)}`);
      createRecord(
        {
          data: created_values
        },

        response => {
          console.log(`sukses createRecord => ${JSON.stringify(response)}`);
          berhasil(`sukses createRecord.`);
          PubSub.publish('<<Create:Record>>', response);
        },

        err => {
          console.log(`gagal createRecord => ${JSON.stringify(err)}.`);
          gagal(`gagal createRecord.`);
        }
      );

    }      

    onClose();

  }}>

    {is_updating ? <UpdateForm initialFormValues={data_raw} /> : <CreateForm />}

    <Form name="fundordertabs-form-body" onFinish={(values) => {}}>
      <Form.Item>
        <Button type='primary' htmlType="submit">Submit</Button>
      </Form.Item>
    </Form>

  </Form.Provider>;

}

export default FormProvider;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Building/FormWrapper.js

import React, { useEffect, useState } from 'react'
import FormProvider from './FormProvider'

const FormWrapper = ({
    onClose=()=>{},
    data_raw={},
    data_selected={},
}) => {
  return <>    
    <FormProvider 
      data_raw={data_raw} 
      onClose={onClose} />
  </>;
}

export default FormWrapper;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Building/List.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';
import PubSub from 'pubsub-js';

import useAxios from 'utils/useAxios';
import SimpleTable from 'common/Table/SimpleTable';
import JsonData from 'assets/building.json';

function column_sorter(a, b, column) {
  console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`);
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    // return b[column][0].toLowerCase() > a[column][0].toLowerCase();
    return 0;
      
  return b[column] > a[column];
}

const List = ({
  show_update,
  recordTransformer = record => record,
}) => {

  const resource_path = 'building';
  const deleteRecord = useAxios({ method: 'DELETE', });
  const [table_data, set_table_data] = useState([]);
  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  const getResourceData = useAxios({ path: resource_path, });  

  const update_table_data = (topic_channel, data) => {
    getResourceData({}, successHandler);
  };

  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  };

  const wrapAsync = () => {
    PubSub.subscribe('<<Create:Record>>', update_table_data);
    PubSub.subscribe('<<Update:Record>>', update_table_data);
    PubSub.subscribe('<<Delete:Record>>', update_table_data);
  }

  useEffect(() => {
    wrapAsync();
    getResourceData({}, successHandler);
  }, []);

  const handleDelete = record => {
    const key = record.key;
    console.log(`deleting ${key} dari record ${JSON.stringify(record)}.`);
    // const table_data_temp = [...table_data].filter(item => item.key !== key);
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    } else {
      console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
      return;
    }

    deleteRecord(
      {
        path: `${resource_path}/${kunci}`,
      },
      response => {
        console.log(`berhasil hapus ${kunci}`);
        PubSub.publish('<<Delete:Record>>', response);
        berhasil('Berhasil', `Berhasil hapus id ${kunci}`);
      },
      err => {
        console.log(`gagal hapus ${kunci}`);
        gagal('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
      }
    );
  }

  const table_header = JsonData.headers.map((column, index) => {

    if (column === "") {

      return {
        title: "Show",
        fixed: 'left',
        width: JsonData.widths.show,
        render: data => <Button onClick={() => {
          console.log(`Show data ${JSON.stringify(data)}`);
          show_update(data);
        }}>Show </Button>,
      };

    } else if (column === "delete") {

      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: JsonData.widths.hapus,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {

      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? JsonData.widths.id : JsonData.widths.normal,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  const modalSelectionHandler = (selections) => {
    // set_modal_bomodule_selected(selections);
    // if (selectionCallback !== undefined) {            
    //   // kirim id dari record, bukan index selection
    //   let id_list = []
    //   selections.forEach(index => {
    //     let ketemu = table_data.find(record => record.key == index)                
    //     // if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
    //     //   id_list .push(ketemu.id + "," + ketemu.id_user);
    //     // else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
    //     //   id_list .push(ketemu.orderno + "," + ketemu.customerno);
    //   })
    //   if (id_list.length > 0) {
    //     selectionCallback(id_list);
    //     console.log(`selection ${id_list}`);
    //   }
    // }
    console.log(`SimpleTable selectCallback: ${selections}, ${typeof(selections)}.`);
  }

	return <>

    <SimpleTable 
      header={table_header}
      body={table_data} 
      selectCallback={modalSelectionHandler} />

  </>;
};

export default List;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Building/Modal.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, 
  Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';


const BoComponentModalDefaultContent = ({
  data_selected,
  data_raw
}) => (<>
      Daftar terselect default isi-selected: {JSON.stringify(data_selected)}
      <hr />
      Isi show (data raw): {JSON.stringify(data_raw)}
  </>
);

const BoComponentModal = ({
  Content,
  modal_title,
  modal_bomodule_visible,
  modal_bomodule_selected,
  modal_bomodule_content,
  set_modal_bomodule,
}) => (<Modal visible={modal_bomodule_visible} title={modal_title}
    onOk={(e) => set_modal_bomodule(false)}
    onCancel={(e) => set_modal_bomodule(false)}
  >

    {<Content
      data_selected={modal_bomodule_selected}
      data_raw={modal_bomodule_content}
    />}

  </Modal>
);

export default {
  BoComponentModalDefaultContent,
  BoComponentModal,
};


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Building/UpdateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
import moment from 'moment';

const UpdateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit UpdateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  useEffect(() => {
    const {
      date,
      ...bukan_tanggal
    } = initialFormValues

    form_konek_provider.setFieldsValue({
      date: moment(date),
      ...bukan_tanggal
    });

  }, [initialFormValues]);

  return <Form name='update_form' 
      // size='small'
      form={form_konek_provider}
      className='update_form'
    >
      <Row gutter={[8, 16]}>
        <Col span='24'>
          
          {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>



<Form.Item name='building_id' label="Building_Id">
  <Input />
</Form.Item>



<Form.Item name='location_text' label="Location_Text">
  <Input />
</Form.Item>



<Form.Item name='lalo' label="Lalo">
  <Input />
</Form.Item>



<Form.Item name='description' label="Description">
  <Input />
</Form.Item>



<Form.Item name='notes' label="Notes">
  <Input />
</Form.Item>


        </Col>
      </Row>

    </Form>;
}

export default UpdateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/capitals.js
// https://www.jasom.net/list-of-capital-cities-with-latitude-and-longitude/

const capital_data = `
Abkhazia,Sukhumi,43.001525,41.023415
Afghanistan,Kabul,34.575503,69.240073
Aland Islands,Mariehamn,60.1,19.933333
Albania,Tirana,41.327546,19.818698
Algeria,Algiers,36.752887,3.042048
American Samoa,Pago Pago,-14.275632,-170.702036
Andorra,Andorra la Vella,42.506317,1.521835
Angola,Luanda,-8.839988,13.289437
Anguilla,The Valley,18.214813,-63.057441
Antarctica,South Pole,-90,0
Antigua and Barbuda,St. John's,17.12741,-61.846772
Argentina,Buenos Aires,-34.603684,-58.381559
Armenia,Yerevan,40.179186,44.499103
Aruba,Oranjestad,12.509204,-70.008631
Australia,Canberra,-35.282,149.128684
Austria,Vienna,48.208174,16.373819
Azerbaijan,Baku,40.409262,49.867092
Bahamas,Nassau,25.047984,-77.355413
Bahrain,Manama,26.228516,50.58605
Bangladesh,Dhaka,23.810332,90.412518
Barbados,Bridgetown,13.113222,-59.598809
Belarus,Minsk,53.90454,27.561524
Belgium,Brussels,50.85034,4.35171
Belize,Belmopan,17.251011,-88.75902
Benin,Porto-Novo,6.496857,2.628852
Bermuda,Hamilton,32.294816,-64.781375
Bhutan,Thimphu,27.472792,89.639286
Bolivia,La Paz,-16.489689,-68.119294
Bosnia and Herzegovina,Sarajevo,43.856259,18.413076
Botswana,Gaborone,-24.628208,25.923147
Bouvet Island,Bouvet Island,-54.43,3.38
Brazil,BrasÃ­lia,-15.794229,-47.882166
British Indian Ocean Territory,Camp Justice,21.3419,55.4778
British Virgin Islands,Road Town,18.428612,-64.618466
Brunei,Bandar Seri Begawan,4.903052,114.939821
Bulgaria,Sofia,42.697708,23.321868
Burkina Faso,Ouagadougou,12.371428,-1.51966
Burundi,Bujumbura,-3.361378,29.359878
Cambodia,Phnom Penh,11.544873,104.892167
Cameroon,YaoundÃ©,3.848033,11.502075
Canada,Ottawa,45.42153,-75.697193
Cape Verde,Praia,14.93305,-23.513327
Cayman Islands,George Town,19.286932,-81.367439
Central African Republic,Bangui,4.394674,18.55819
Chad,N'Djamena,12.134846,15.055742
Chile,Santiago,-33.44889,-70.669265
China,Beijing,39.904211,116.407395
Christmas Island,Flying Fish Cove,-10.420686,105.679379
Cocos (Keeling) Islands,West Island,-12.188834,96.829316
Colombia,BogotÃ¡,4.710989,-74.072092
Comoros,Moroni,-11.717216,43.247315
Congo (DRC),Kinshasa,-4.441931,15.266293
Congo (Republic),Brazzaville,-4.26336,15.242885
Cook Islands,Avarua,-21.212901,-159.782306
Costa Rica,San JosÃ©,9.928069,-84.090725
CÃ´te d'Ivoire,Yamoussoukro,6.827623,-5.289343
Croatia,Zagreb ,45.815011,15.981919
Cuba,Havana,23.05407,-82.345189
CuraÃ§ao,Willemstad,12.122422,-68.882423
Cyprus,Nicosia,35.185566,33.382276
Czech Republic,Prague,50.075538,14.4378
Denmark,Copenhagen,55.676097,12.568337
Djibouti,Djibouti,11.572077,43.145647
Dominica,Roseau,15.309168,-61.379355
Dominican Republic,Santo Domingo,18.486058,-69.931212
Ecuador,Quito,-0.180653,-78.467838
Egypt,Cairo,30.04442,31.235712
El Salvador,San Salvador,13.69294,-89.218191
Equatorial Guinea,Malabo,3.750412,8.737104
Eritrea,Asmara,15.322877,38.925052
Estonia,Tallinn,59.436961,24.753575
Ethiopia,Addis Ababa,8.980603,38.757761
Falkland Islands (Islas Malvinas),Stanley,-51.697713,-57.851663
Faroe Islands,TÃ³rshavn,62.007864,-6.790982
Fiji,Suva,-18.124809,178.450079
Finland,Helsinki,60.173324,24.941025
France,Paris,48.856614,2.352222
French Guiana,Cayenne,4.92242,-52.313453
French Polynesia,Papeete,-17.551625,-149.558476
French Southern Territories,Saint-Pierre ,-21.3419,55.4778
Gabon,Libreville,0.416198,9.467268
Gambia,Banjul,13.454876,-16.579032
Georgia,Tbilisi,41.715138,44.827096
Germany,Berlin,52.520007,13.404954
Ghana,Accra,5.603717,-0.186964
Gibraltar,Gibraltar,36.140773,-5.353599
Greece,Athens,37.983917,23.72936
Greenland,Nuuk,64.18141,-51.694138
Grenada,St. George's,12.056098,-61.7488
Guadeloupe,Basse-Terre,16.014453,-61.706411
Guam,HagÃ¥tÃ±a,13.470891,144.751278
Guatemala,Guatemala City,14.634915,-90.506882
Guernsey,St. Peter Port,49.455443,-2.536871
Guinea,Conakry,9.641185,-13.578401
Guinea-Bissau,Bissau,11.881655,-15.617794
Guyana,Georgetown,6.801279,-58.155125
Haiti,Port-au-Prince,18.594395,-72.307433
Honduras,Tegucigalpa,14.072275,-87.192136
Hong Kong,Hong Kong,22.396428,114.109497
Hungary,Budapest,47.497912,19.040235
Iceland,ReykjavÃ­k,64.126521,-21.817439
India,New Delhi,28.613939,77.209021
Indonesia,Jakarta,-6.208763,106.845599
Iran,Tehran,35.689198,51.388974
Iraq,Baghdad,33.312806,44.361488
Ireland,Dublin,53.349805,-6.26031
Isle of Man,Douglas,54.152337,-4.486123
Israel,Tel Aviv,32.0853,34.781768
Italy,Rome,41.902784,12.496366
Jamaica,Kingston,18.042327,-76.802893
Japan,Tokyo,35.709026,139.731992
Jersey,St. Helier,49.186823,-2.106568
Jordan,Amman,31.956578,35.945695
Kazakhstan,Astana,51.160523,71.470356
Kenya,Nairobi,-1.292066,36.821946
Kiribati,Tarawa Atoll,1.451817,172.971662
Kosovo,Pristina,42.662914,21.165503
Kuwait,Kuwait City,29.375859,47.977405
Kyrgyzstan,Bishkek,42.874621,74.569762
Laos,Vientiane,17.975706,102.633104
Latvia,Riga,56.949649,24.105186
Lebanon,Beirut,33.888629,35.495479
Lesotho,Maseru,-29.363219,27.51436
Liberia,Monrovia,6.290743,-10.760524
Libya,Tripoli,32.887209,13.191338
Liechtenstein,Vaduz,47.14103,9.520928
Lithuania,Vilnius,54.687156,25.279651
Luxembourg,Luxembourg,49.611621,6.131935
Macau,Macau,22.166667,113.55
Macedonia (FYROM),Skopje,41.997346,21.427996
Madagascar,Antananarivo,-18.87919,47.507905
Malawi,Lilongwe,-13.962612,33.774119
Malaysia,Kuala Lumpur,3.139003,101.686855
Maldives,MalÃ©,4.175496,73.509347
Mali,Bamako,12.639232,-8.002889
Malta,Valletta,35.898909,14.514553
Marshall Islands,Majuro,7.116421,171.185774
Martinique,Fort-de-France,14.616065,-61.05878
Mauritania,Nouakchott,18.07353,-15.958237
Mauritius,Port Louis,-20.166896,57.502332
Mayotte,Mamoudzou,-12.780949,45.227872
Mexico,Mexico City,19.432608,-99.133208
Micronesia,Palikir,6.914712,158.161027
Moldova,Chisinau,47.010453,28.86381
Monaco,Monaco,43.737411,7.420816
Mongolia,Ulaanbaatar,47.886399,106.905744
Montenegro,Podgorica,42.43042,19.259364
Montserrat,Plymouth,16.706523,-62.215738
Morocco,Rabat,33.97159,-6.849813
Mozambique,Maputo,-25.891968,32.605135
Myanmar (Burma),Naypyidaw,19.763306,96.07851
Nagorno-Karabakh Republic,Stepanakert,39.826385,46.763595
Namibia,Windhoek,-22.560881,17.065755
Nauru,Yaren,-0.546686,166.921091
Nepal,Kathmandu,27.717245,85.323961
Netherlands,Amsterdam,52.370216,4.895168
Netherlands Antilles,Willemstad ,12.1091242,-68.9316546
New Caledonia,NoumÃ©a,-22.255823,166.450524
New Zealand,Wellington,-41.28646,174.776236
Nicaragua,Managua,12.114993,-86.236174
Niger,Niamey,13.511596,2.125385
Nigeria,Abuja,9.076479,7.398574
Niue,Alofi,-19.055371,-169.917871
Norfolk Island,Kingston,-29.056394,167.959588
North Korea,Pyongyang,39.039219,125.762524
Northern Cyprus,Nicosia,35.185566,33.382276
Northern Mariana Islands,Saipan,15.177801,145.750967
Norway,Oslo,59.913869,10.752245
Oman,Muscat,23.58589,58.405923
Pakistan,Islamabad,33.729388,73.093146
Palau,Ngerulmud,7.500384,134.624289
Palestine,Ramallah,31.9073509,35.5354719
Panama,Panama City,9.101179,-79.402864
Papua New Guinea,Port Moresby,-9.4438,147.180267
Paraguay,Asuncion,-25.26374,-57.575926
Peru,Lima,-12.046374,-77.042793
Philippines,Manila,14.599512,120.98422
Pitcairn Islands,Adamstown,-25.06629,-130.100464
Poland,Warsaw,52.229676,21.012229
Portugal,Lisbon,38.722252,-9.139337
Puerto Rico,San Juan,18.466334,-66.105722
Qatar,Doha,25.285447,51.53104
RÃ©union,Saint-Denis,-20.882057,55.450675
Romania,Bucharest,44.426767,26.102538
Russia,Moscow,55.755826,37.6173
Rwanda,Kigali,-1.957875,30.112735
Saint Pierre and Miquelon,St. Pierre,46.775846,-56.180636
Saint Vincent and the Grenadines,Kingstown,13.160025,-61.224816
Samoa,Apia,-13.850696,-171.751355
San Marino,San Marino,43.935591,12.447281
SÃ£o TomÃ© and PrÃ­ncipe,SÃ£o TomÃ©,0.330192,6.733343
Saudi Arabia,Riyadh,24.749403,46.902838
Senegal,Dakar,14.764504,-17.366029
Serbia,Belgrade,44.786568,20.448922
Seychelles,Victoria,-4.619143,55.451315
Sierra Leone,Freetown,8.465677,-13.231722
Singapore,Singapore,1.280095,103.850949
Slovakia,Bratislava,48.145892,17.107137
Slovenia,Ljubljana,46.056947,14.505751
Solomon Islands,Honiara,-9.445638,159.9729
Somalia,Mogadishu,2.046934,45.318162
South Africa,Pretoria,-25.747868,28.229271
South Georgia and the South Sandwich Islands,King Edward Point,-54.28325,-36.493735
South Korea,Seoul,37.566535,126.977969
South Ossetia,Tskhinvali,42.22146,43.964405
South Sudan,Juba,4.859363,31.57125
Spain,Madrid,40.416775,-3.70379
Sri Lanka,Sri Jayawardenepura Kotte,6.89407,79.902478
St. BarthÃ©lemy,Gustavia,17.896435,-62.852201
St. Kitts and Nevis,Basseterre,17.302606,-62.717692
St. Lucia,Castries,14.010109,-60.987469
St. Martin,Marigot,18.067519,-63.082466
Sudan,Khartoum,15.500654,32.559899
Suriname,Paramaribo,5.852036,-55.203828
Svalbard and Jan Mayen,Longyearbyen ,78.062,22.055
Swaziland,Mbabane,-26.305448,31.136672
Sweden,Stockholm,59.329323,18.068581
Switzerland,Bern,46.947974,7.447447
Syria,Damascus,33.513807,36.276528
Taiwan,Taipei,25.032969,121.565418
Tajikistan,Dushanbe,38.559772,68.787038
Tanzania,Dodoma,-6.162959,35.751607
Thailand,Bangkok,13.756331,100.501765
Timor-Leste,Dili,-8.556856,125.560314
Togo,LomÃ©,6.172497,1.231362
Tokelau,Nukunonu,-9.2005,-171.848
Tonga,NukuÊ»alofa,-21.139342,-175.204947
Transnistria,Tiraspol,46.848185,29.596805
Trinidad and Tobago,Port of Spain,10.654901,-61.501926
Tristan da Cunha,Edinburgh of the Seven Seas,-37.068042,-12.311315
Tunisia,Tunis,36.806495,10.181532
Turkey,Ankara,39.933364,32.859742
Turkmenistan,Ashgabat,37.960077,58.326063
Turks and Caicos Islands,Cockburn Town,21.467458,-71.13891
Tuvalu,Funafuti,-8.520066,179.198128
U.S. Virgin Islands,Charlotte Amalie,18.3419,-64.930701
Uganda,Kampala,0.347596,32.58252
Ukraine,Kiev,50.4501,30.5234
United Arab Emirates,Abu Dhabi,24.299174,54.697277
United Kingdom,London,51.507351,-0.127758
United States,Washington,38.907192,-77.036871
Uruguay,Montevideo,-34.901113,-56.164531
Uzbekistan,Tashkent,41.299496,69.240073
Vanuatu,Port Vila,-17.733251,168.327325
Vatican City,Vatican City,41.902179,12.453601
Venezuela,Caracas,10.480594,-66.903606
Vietnam,Hanoi,21.027764,105.83416
Wallis and Futuna,Mata-Utu,-13.282509,-176.176447
Western Sahara,El AaiÃºn,27.125287,-13.1625
Yemen,Sana'a,15.369445,44.191007
Zambia,Lusaka,-15.387526,28.322817
Zimbabwe,Harare,-17.825166,31.03351
`

export default capital_data;

export const capitals = {
  'australia': [-35.282,149.128684],
  'brazil': [-15.794229,-47.882166],
  'france': [48.856614,2.352222],
  'germany': [52.520007,13.404954],
  'india': [28.613939,77.209021],
  'indonesia': [-6.208763,106.845599],
  'italy': [41.902784,12.496366],
  'japan': [35.709026,139.731992],
  'russia': [55.755826,37.6173],
  'taiwan': [25.032969,121.565418],
  'thailand': [13.756331,100.501765],
  'uk': [51.507351,-0.127758],
  'us': [38.907192,-77.036871],
  'viet-nam': [21.027764,105.83416],
}


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/charts_helper.js


export const create_tooltip = () => {
    return {
        trigger: 'axis'
    }
}

export const create_legend = (var_list) => {
    return {
        legend: var_list
    }
}

export const create_toolbox = () => {
    return {
        show : true,
        feature : {
            magicType : {show: true, type: ['line', 'bar']},
            restore : {show: true},
            saveAsImage : {show: true}
        }
    }
}

export const create_toolbox1 = () => {
    return {
        show : true,
        feature : {
            magicType : {show: true, type: ['bar']},
            // restore : {show: true},
            // saveAsImage : {show: true}
        }
    }
}

export const create_toolbox2 = () => {
    return {
        show : true,
        feature : {
            magicType : {show: true, type: ['line', 'bar']},
            // restore : {show: true},
            // saveAsImage : {show: true}
        }
    }
}

export const create_toolbox3 = () => {
    return {
        show : true,
        feature : {
            magicType : {show: true, type: ['line', 'bar']},
            // restore : {show: true},
            // saveAsImage : {show: true}
        }
    }
}

export const create_toolbox4 = () => {
    return {
        show : true,
        feature : {
            // magicType : {show: true, type: ['line', 'bar']},
            // restore : {show: true},
            saveAsImage : {show: true}
        }
    }
}

export const create_color = (clr1="#55ce63", clr2="#009efb") => {
    return [clr1, clr2]
}

export const create_xaxis = (data_list=['Jan','Feb','Mar','Apr','May','Jun','July','Aug','Sept','Oct','Nov','Dec']) => {
    return [
        {
            type: 'category',
            data: data_list
        }
    ]
}

export const markpoint_max_min = [
    {type : 'max', name: 'Max'},
    {type : 'min', name: 'Min'}
]

export const create_series_item = (item_name, item_data, markpoint_data=[], chart_type='line', smooth=false, area=false) => {

    let conditional = {
        name: item_name,
        type: chart_type,
        data: item_data,
        markPoint: {
            data: markpoint_data
        },
        markLine: {
            data : [
                {type : 'average', name: 'Average'}
            ]
        }
    }
    if (area) conditional.areaStyle = {};
    if (smooth) conditional.smooth = true;
    return conditional;
}

export const charter = (title, subtitle, tt, lg, tb, clr, x, srs) => {
    return {
        title: {
            text: title,
            subtext: subtitle
        },
        tooltip: tt,
        legend: lg,
        toolbox: tb,
        color: clr,
        calculable: true,
        xAxis: x,
        yAxis: [{type:'value'}],
        series: srs,
    }
}

export const echarts = (tt, lg, tb, clr, x, srs) => {
    return {
        tooltip: tt,
        legend: lg,
        toolbox: tb,
        color: clr,
        calculable: true,
        xAxis: x,
        yAxis: [{type:'value'}],
        series: srs,
    }
}

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/chart_options.js
import { piePatternSrc, bgPatternSrc } from './patterns';

let piePatternImg = new Image();
piePatternImg.src = piePatternSrc;

let bgPatternImg = new Image();
bgPatternImg.src = bgPatternSrc;

const patternItemStyle = {
  normal: {
    opacity: 0.7,
    color: {
      image: piePatternImg,
      repeat: 'repeat'
    },
    borderWidth: 3,
    borderColor: '#235894'
  }
}

export const createOptions = (name_value_pairs, title, subtitle) => {
  return {
    title: {
      text: title,
      subtext: subtitle,
      right: 'center'
    },
    tooltip: {
      trigger: 'item',
      formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
      bottom: 10,
      right: 'center',
      data: name_value_pairs.map(item=>item.name)
    },
    series: [{
      name: title,
      type: 'pie',
      radius : '65%',
      center: ['50%', '50%'],
      selectedMode: 'single',
      itemStyle: {
        emphasis: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      },
      data: name_value_pairs
    }]
  }
}

export const createOptions2 = (name_value_pairs, nama_series) => {
  return {
    tooltip : {
      trigger: 'item',
      formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
      orient : 'vertical',
      x : 'left',
      data: name_value_pairs.map(item=>item.name)
    },
    toolbox: {
      show : true,
      feature : {
        dataView : {show: true, readOnly: false},
        magicType : {
          show: true,
          type: ['pie', 'funnel'],
          option: {
            funnel: {
              x: '25%',
              width: '50%',
              funnelAlign: 'center',
              max: 1548
            }
          }
        },
        restore : {show: true},
        saveAsImage : {show: true}
      }
    },
    color: ["#f62d51", "#009efb", "#55ce63", "#ffbc34", "#2f3d4a"],
    calculable : true,
    series : [{
      name: nama_series,
      type: 'pie',
      radius : ['65%', '75%'],
      itemStyle : {
        normal : {
          label : {
            show : false
          },
          labelLine : {
            show : false
          }
        },
        emphasis : {
          label : {
            show : true,
            position : 'center',
            textStyle : {
              fontSize : '30',
              fontWeight : 'bold'
            }
          }
        }
      },
      data: name_value_pairs
      // data: [
      //     {name:'prabowo', value:30},
      //     {name:'jokowi', value:50},
      //     {name:'basuki', value:20}
      // ]
    }]
  }
}

export const createOptions3 = (name_value_pairs, nama_series) => {
  return {
    tooltip: {
      trigger: 'item',
      formatter: "{a} <br/>{b}: {c} ({d}%)"
    },
    legend: {
      orient: 'vertical',
      x: 'left',
      data: name_value_pairs.map(item=>item.name)
    },
    series: [{
      name: nama_series,
      type:'pie',
      radius: ['50%', '70%'],
      avoidLabelOverlap: false,
      label: {
        normal: {
          show: false,
          position: 'center'
        },
        emphasis: {
          show: true,
          textStyle: {
            fontSize: '30',
            fontWeight: 'bold'
          }
        }
      },
      labelLine: {
        normal: {
          show: false
        }
      },
      data: name_value_pairs
      // data: [
      //     {name:'prabowo', value:30},
      //     {name:'jokowi', value:50},
      //     {name:'basuki', value:20}
      // ]
    }]
  }
}

export const createOptions4 = (name_value_pairs, nama_series) => {
  return {
    backgroundColor: {
      image: bgPatternImg,
      repeat: 'repeat'
    },
    title: {
      text: nama_series,
      right: 'center',
      textStyle: {
        color: '#235894'
      }
    },
    tooltip: {},
    series: [{
      name: nama_series,
      type: 'pie',
      selectedMode: 'single',
      selectedOffset: 30,
      clockwise: true,
      label: {
        normal: {
          textStyle: {
            fontSize: 18,
            color: '#235894'
          }
        }
      },
      labelLine: {
        normal: {
          lineStyle: {
            color: '#235894'
          }
        }
      },
      data: name_value_pairs,
      // data: [
      //     {name:'prabowo', value:30},
      //     {name:'jokowi', value:50},
      //     {name:'basuki', value:20}
      // ],
      itemStyle: patternItemStyle
    }]
  }
}

export const createOptions5 = (name_value_pairs, nama_series) => {
  return {
    tooltip : {
      trigger: 'item',
      formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
      x : 'center',
      y : 'bottom',
      data: name_value_pairs.map(item=>item.name)
      // data: ['prabowo', 'jokowi', 'basuki']
    },
    toolbox: {
      show : true,
      feature : {

        dataView : {show: true, readOnly: false},
        magicType : {
          show: true,
          type: ['pie', 'funnel']
        },
        restore : {show: true},
        saveAsImage : {show: true}
      }
    },
    color: ["#f62d51", "#55ce63","#ffbc34", "#7460ee","#009efb", "#2f3d4a","#90a4ae"],
    calculable : true,
    series : [
      {
        name: nama_series,
        type: 'pie',
        radius : [20, 110],
        center : ['50%', 150],
        roseType : 'radius',
        width: '40%',       // for funnel
        max: 40,            // for funnel
        itemStyle : {
          normal : {
            label : {
              show : false
            },
            labelLine : {
              show : false
            }
          },
          emphasis : {
            label : {
              show : true
            },
            labelLine : {
              show : true
            }
          }
        },
        data: name_value_pairs
        // data: [
        //     {name:'prabowo', value:30},
        //     {name:'jokowi', value:50},
        //     {name:'basuki', value:20}
        // ]
      },
      // {
      //     name:'Area mode',
      //     type:'pie',
      //     radius : [30, 110],
      //     center : ['75%', 200],
      //     roseType : 'area',
      //     x: '50%',               // for funnel
      //     max: 40,                // for funnel
      //     sort : 'ascending',     // for funnel
      //     data: [
      //         {name:'prabowo', value:30},
      //         {name:'jokowi', value:50},
      //         {name:'basuki', value:20}
      //     ]
      // }
    ]
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Dashboard.js
import React, { useEffect, useState } from 'react';
import { hot } from 'react-hot-loader/root';
import {
  Button,
	Card,
	Col,
  DatePicker,
  Divider,
  Drawer,
  Input, InputNumber ,
  Modal,
  Popover,
	Row,
  Select,
  Space,
	Statistic,
	Table,
} from 'antd';
import {
	AppstoreOutlined,
	BankOutlined,
	CaretRightOutlined,
	ContainerOutlined,
	DeleteFilled,
	DeleteOutlined,
	DesktopOutlined,
	DislikeFilled,
	DislikeOutlined,
	DownOutlined,
	ExclamationCircleOutlined,
	FileAddOutlined,
	FileExcelOutlined,
	FilePdfOutlined,
	FundOutlined,
	HomeOutlined,
	InboxOutlined,
	LikeFilled,
	LikeOutlined,
	LockOutlined,
	MailOutlined,
	MenuFoldOutlined,
	MenuOutlined,
	MenuUnfoldOutlined,
	MinusCircleOutlined,
	MoneyCollectOutlined,
	PieChartOutlined,
	PlusOutlined,
	ReloadFilled,
	ReloadOutlined,
	SettingFilled,
	SettingOutlined,
	SketchOutlined,
	SmileOutlined,
	SolutionOutlined,
	UploadOutlined,
	UserOutlined, 	
} from '@ant-design/icons';
import TabPage from 'common/TabPage';
import ToolbarContext from 'context/ToolbarContext';
import DashboardEcharts from './DashboardEcharts';
import DashboardBizcharts from './DashboardBizcharts';
import DashboardHicharts from './DashboardHicharts';
import DashboardRecharts from './DashboardRecharts';

import GridMap from './GridMap';

import useAxios from './useAxios';
import MyLoader from '#/utils/loader';
import { capitals } from './capitals';

const Dashboard = () => {
  const { setToolbar } = React.useContext(ToolbarContext);
  const [lokasiTab, setLokasiTab] = useState('top');

  const [coronaData, setCoronaData] = useState({labels:[],cases:[],deaths:[]});
  const [latestData, setLatestData] = useState({
    totalcases:0,
    totaldeaths:0,
    totalrecovered:0,
  });
  const [isLoadingCountry, setLoadingCountry] = useState(false);
  const [isAddingCountry, setAddingCountry] = useState(false);
  const [isRefreshing, setRefreshing] = useState(false);
  const [jumlahData, setJumlahData] = useState(0);
  const [countries, setCountries] = useState(['indonesia']);
  const [country, setCountry] = useState('indonesia');
  const [newcountry, setNewCountry] = useState('');

	const [lalo, setLalo] = useState(capitals[country]);

  const getCoronaData = useAxios({ path: `corona/latest/7/${country}`, });
  const getLatestData = useAxios({ path: `corona/latest/0/${country}`, });
  const getCoronaCountries = useAxios({ path: 'corona/latest/countries', });
  const loadCountry = useAxios({ path: `corona/load/${country}`, });
  const loadCountryDynamic = useAxios({ path: `corona/load/${country}`, });

  const fetchCountryData = () => {
    getCoronaCountries({}, response => {
      setCountries(response.sort());
    });
  }

  const fetchCoronaData = () => {

    getCoronaData({}, response => {
      let result = response.result;
      let labels = result.map(item => item.date);
      // labels = labels.map(item => /(\d+)-(\d+)-(\d+)/.exec(item)[3]);
      let cases = result.map(item => item.cases);
      let deaths = result.map(item => item.deaths);

      setJumlahData(labels.length);

      setCoronaData({
        labels,
        cases,
        deaths,
      });
      // console.log(`
      //   peroleh data corona:
      //   ${JSON.stringify(result)}

      //   labels = ${labels}
      //   cases = ${cases}
      //   deaths = ${deaths}
      // `);
    });
  }

  const fetchTotalData = () => {
    getLatestData({}, response => {
      const {
        totalcases,
        totaldeaths,
        totalrecovered,
      } = response.result;
      setLatestData({
        totalcases,
        totaldeaths,
        totalrecovered,
      })
    });
  }

  useEffect(function() {
    fetchCountryData();
  }, []);

  useEffect(function() {

    fetchTotalData();

    fetchCoronaData();

		setLalo(capitals[country]);

		console.log(`new capital: ${capitals[country]}`);

  }, [country]);

  useEffect(function() {
    setToolbar(<Toolbar />)
  }, []);

	
  let Toolbar = () => (<Space>
    <h1>Dashboard</h1>

    <Button type="primary">Do something</Button>

  </Space>);

  return isLoadingCountry ?
  <MyLoader type="Grid"/>
  : isAddingCountry ?
  <MyLoader type="Audio"/>
  : isRefreshing ?
  <MyLoader type="BallTriangle"/>
  : (<>

		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'GridMap',
						icon: <DesktopOutlined />,
						component: <GridMap lalo={lalo} />
					},
				]
			} 
		/>

		<Card>
		<Row gutter={[8, 16]}>
      <Col span='8'>
        <Select showSearch
          value={country}
          // placeholder="Ketik untuk cari..."
          onChange={value=>setCountry(value)}
          style={{width: 120}}
        >
          {countries.map((item, index) => (
            <Select.Option key={index} disabled={item.disabled} value={item}>
              {item}
            </Select.Option>
            )
          )}
        </Select>
      </Col>
      <Col span='2'>
      <Button icon={<SketchOutlined />}
				disabled={isLoadingCountry}
				onClick={()=>{
				setLoadingCountry(true);
				loadCountry({}, response => {
					// setCountry(country);
					fetchCoronaData();
					fetchTotalData();
					setLoadingCountry(false);
				});
			}} type="primary">Load</Button>
      </Col>
      <Col span='8'>
        <Input 
          value={newcountry}
          onChange={e => setNewCountry(e.target.value)}
          placeholder="Type country to fetch"
          />
      </Col>
      <Col span='2'>
      <Button icon={<SketchOutlined />}
				disabled={isAddingCountry}
				onClick={()=>{
					if (newcountry.length > 0 && !countries.includes(newcountry)) {
						let newpath = `corona/load/${newcountry}`;
						console.log(`mari oprek negara ${newcountry} => ${newpath}`);
						setAddingCountry(true);
						loadCountryDynamic({ path: newpath }, response => {
								// ambil countries baru utk select input
							fetchCountryData();
							// set ke new country
							setCountry(newcountry); // akan initiate fetch country+total data?                    
							setAddingCountry(false);

							setNewCountry('');
						});
					}
				}} type="primary">Add</Button>
      </Col>
      <Col span='2'>
      <Button icon={<SketchOutlined />}
				disabled={isRefreshing}
				onClick={()=>{
					setRefreshing(true);
					fetchTotalData();
					fetchCoronaData();
					fetchCountryData();
					setRefreshing(false);
				}} type="primary">Refresh</Button>
      </Col>
    </Row>
		</Card>

		<Row gutter={[8, 16]}>
      <Col span='6'>
				<Card>
				<Statistic title="Cases" value={latestData.totalcases} prefix={<LikeOutlined />} />
				</Card>
			</Col>
			<Col span='6'>
				<Card>
				<Statistic title="Deaths" value={latestData.totaldeaths} prefix={<LikeOutlined />} />
				</Card>
			</Col>
			<Col span='6'>
				<Card>
				<Statistic title="Recovered" value={latestData.totalrecovered} prefix={<LikeOutlined />} />
				</Card>
			</Col>
			<Col span='6'>
				<Card>
				<Statistic title="Unaccounted" value={latestData.totalcases-(latestData.totaldeaths+latestData.totalrecovered)} prefix={<LikeOutlined />} />
				</Card>
			</Col>
		</Row>

		<Row gutter={[8, 16]}>
      <Col span='12'>
				<Table
					bordered
					columns={["No", "Tanggal", "Jumlah Kasus"].map((item,index)=>{
						return {
							key: index,
							dataIndex: index,
							title: item,
						}
					})}
					dataSource={jumlahData ?
						Array.from({length:jumlahData}, (_,nomor) => {
							return {
								key: nomor,
								0:nomor+1,
								1:coronaData.labels[nomor],
								2:coronaData.cases[nomor],
							}
						})
						: []}
					/>
			</Col>
      <Col span='12'>
				<Table
					bordered
					columns={["No", "Tanggal", "Jumlah Mati"].map((item,index)=>{
						return {
							key: index,
							dataIndex: index,
							title: item,
						}
					})}
					dataSource={jumlahData ?
						Array.from({length:jumlahData}, (_,nomor) => {
							return {
								key: nomor,
								0:nomor+1,
								1:coronaData.labels[nomor],
								2:coronaData.deaths[nomor],
							}
						})
						: []}
					/>
			</Col>
		</Row>

		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'ECharts',
						icon: <DesktopOutlined />,
						component: <DashboardEcharts 
							title1={country}
							// subtitle1={`Judul statistik untuk ${country}`}
							subtitle1={country}
							data={[
								{k:'Total cases',v:latestData.totalcases},
								{k:'Total deaths',v:latestData.totaldeaths},
								{k:'Total recovered',v:latestData.totalrecovered},
								{k:'Total unaccounted',v:latestData.totalcases-(latestData.totaldeaths+latestData.totalrecovered)},
							].map((item,idx)=>{
								return {
									name: item.k,
									value: item.v,
								}
							})}
							labels={coronaData.labels}
							series1={coronaData.cases}
							series2={coronaData.deaths}
							/>,
					},
					{
						title: 'HighCharts',
						icon: <DesktopOutlined />,
						component: <DashboardHicharts 
							title1={country}
							// subtitle1={`Judul statistik untuk ${country}`}
							subtitle1={country}
							total={[latestData.totalcases,latestData.totaldeaths,latestData.totalrecovered,latestData.totalcases-(latestData.totaldeaths+latestData.totalrecovered)]}
							data={[
								{k:'Total cases',v:latestData.totalcases},
								{k:'Total deaths',v:latestData.totaldeaths},
								{k:'Total recovered',v:latestData.totalrecovered},
								{k:'Total unaccounted',v:latestData.totalcases-(latestData.totaldeaths+latestData.totalrecovered)},
							].map((item,idx)=>{
								return {
									name: item.k,
									value: item.v,
								}
							})}
							data_percent={[
								{k:'Total cases',v:latestData.totalcases},
								{k:'Total deaths',v:latestData.totaldeaths},
								{k:'Total recovered',v:latestData.totalrecovered},
								{k:'Total unaccounted',v:latestData.totalcases-(latestData.totaldeaths+latestData.totalrecovered)},
							].map((elem,idx)=>{
								return {
									item: elem.k,
									percent: elem.v,
								}
							})}
							labels={coronaData.labels}
							series1={coronaData.cases.map((item,idx)=>{
								return {
									time: coronaData.labels[idx],
									value: item,
								}
							})}
							series2={coronaData.deaths.map((item,idx)=>{
								return {
									time: coronaData.labels[idx],
									value: item,
								}
							})}
							/>
					},
					{
						title: 'ReCharts',
						icon: <DesktopOutlined />,
						component: <DashboardRecharts 
							title1={country}
							// subtitle1={`Judul statistik untuk ${country}`}
							subtitle1={country}
							data={[
								{k:'Total cases',v:latestData.totalcases},
								{k:'Total deaths',v:latestData.totaldeaths},
								{k:'Total recovered',v:latestData.totalrecovered},
								{k:'Total unaccounted',v:latestData.totalcases-(latestData.totaldeaths+latestData.totalrecovered)},
							].map((item,idx)=>{
								return {
									name: item.k,
									value: item.v,
								}
							})}
							labels={coronaData.labels}
							series1={coronaData.cases.map((item,idx)=>{
								return {
									time: coronaData.labels[idx],
									value: item,
								}
							})}
							series2={coronaData.deaths.map((item,idx)=>{
								return {
									time: coronaData.labels[idx],
									value: item,
								}
							})}
							/>
					},
					{
						title: 'BizCharts',
						icon: <DesktopOutlined />,
						component: <DashboardBizcharts 
							title1={country}
							// subtitle1={`Judul statistik untuk ${country}`}
							subtitle1={country}
							total={[latestData.totalcases,latestData.totaldeaths,latestData.totalrecovered,latestData.totalcases-(latestData.totaldeaths+latestData.totalrecovered)]}
							data={[
								{k:'Total cases',v:latestData.totalcases},
								{k:'Total deaths',v:latestData.totaldeaths},
								{k:'Total recovered',v:latestData.totalrecovered},
								{k:'Total unaccounted',v:latestData.totalcases-(latestData.totaldeaths+latestData.totalrecovered)},
							].map((item,idx)=>{
								return {
									name: item.k,
									value: item.v,
								}
							})}
							data_percent={[
								{k:'Total cases',v:latestData.totalcases},
								{k:'Total deaths',v:latestData.totaldeaths},
								{k:'Total recovered',v:latestData.totalrecovered},
								{k:'Total unaccounted',v:latestData.totalcases-(latestData.totaldeaths+latestData.totalrecovered)},
							].map((elem,idx)=>{
								return {
									item: elem.k,
									percent: elem.v,
								}
							})}
							labels={coronaData.labels}
							series1={coronaData.cases.map((item,idx)=>{
								return {
									time: coronaData.labels[idx],
									value: item,
								}
							})}
							series2={coronaData.deaths.map((item,idx)=>{
								return {
									time: coronaData.labels[idx],
									value: item,
								}
							})}
							/>
					},
				]
			} 
		/>

  </>);
};

export default hot(Dashboard);

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/DashboardBizcharts.js

import React, { useEffect, useState } from 'react';
import { 
  Chart, 
  Line, 
  Point, 
  Tooltip, 
  getTheme,
} from "bizcharts";
import {
  G2,
  // Chart,
  // Tooltip,
  Interval,
} from "bizcharts";

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';

import Speedy from './Speedy';
import MyGauge from './MyGauge';
import MyPie from './MyPie';
import MyBar from './MyBar';
import MyDonut from './MyDonut';
const data = [
	{
		year: "1991",
		value: 3,
	},
	{
		year: "1992",
		value: 4,
	},
	{
		year: "1993",
		value: 3.5,
	},
	{
		year: "1994",
		value: 5,
	},
	{
		year: "1995",
		value: 4.9,
	},
	{
		year: "1996",
		value: 6,
	},
	{
		year: "1997",
		value: 7,
	},
	{
		year: "1998",
		value: 9,
	},
	{
		year: "1999",
		value: 13,
	},
];


const data2 = [
  { name: 'London', æœˆä»½: 'Jan.', æœˆå‡é™é›¨é‡: 18.9 },
  { name: 'London', æœˆä»½: 'Feb.', æœˆå‡é™é›¨é‡: 28.8 },
  { name: 'London', æœˆä»½: 'Mar.', æœˆå‡é™é›¨é‡: 39.3 },
  { name: 'London', æœˆä»½: 'Apr.', æœˆå‡é™é›¨é‡: 81.4 },
  { name: 'London', æœˆä»½: 'May', æœˆå‡é™é›¨é‡: 47 },
  { name: 'London', æœˆä»½: 'Jun.', æœˆå‡é™é›¨é‡: 20.3 },
  { name: 'London', æœˆä»½: 'Jul.', æœˆå‡é™é›¨é‡: 24 },
  { name: 'London', æœˆä»½: 'Aug.', æœˆå‡é™é›¨é‡: 35.6 },
  { name: 'Berlin', æœˆä»½: 'Jan.', æœˆå‡é™é›¨é‡: 12.4 },
  { name: 'Berlin', æœˆä»½: 'Feb.', æœˆå‡é™é›¨é‡: 23.2 },
  { name: 'Berlin', æœˆä»½: 'Mar.', æœˆå‡é™é›¨é‡: 34.5 },
  { name: 'Berlin', æœˆä»½: 'Apr.', æœˆå‡é™é›¨é‡: 99.7 },
  { name: 'Berlin', æœˆä»½: 'May', æœˆå‡é™é›¨é‡: 52.6 },
  { name: 'Berlin', æœˆä»½: 'Jun.', æœˆå‡é™é›¨é‡: 35.5 },
  { name: 'Berlin', æœˆä»½: 'Jul.', æœˆå‡é™é›¨é‡: 37.4 },
  { name: 'Berlin', æœˆä»½: 'Aug.', æœˆå‡é™é›¨é‡: 42.4 },
];

const DashboardBizcharts = ({title1,subtitle1,total,data, data_percent,labels, series1,series2}) => {
  return (<>
    <h1>DashboardBizcharts</h1>
    <span>
      <a href='https://bizcharts.net/product/BizCharts4/gallery'>
      https://bizcharts.net/product/BizCharts4/gallery
      </a>
    </span>

    <Row gutter={[8, 16]}>
      <Col span='8'>
        <Chart
          appendPadding={[10, 0, 0, 10]}
          autoFit
          height={500}
          data={series1}
          onLineClick={console.log}
          scale={{ 
            value: { min: 0, alias: 'Cases', type: 'linear-strict' }, 
            time: { range: [0, 1] } 
          }}
        >

          <Line position="time*value" />
          <Point position="time*value" />

          <Tooltip showCrosshairs follow={false} />
        </Chart>
      </Col>

      <Col span='8'>
        <MyPie data={data_percent} />
      </Col>

      <Col span='8'>
        <Speedy mati={total[1]} kasus={total[0]} />
      </Col>


    </Row>

    <Row gutter={[8, 16]}>
      <Col span='8'>
        {/* <Chart height={400} padding="auto" data={data2} autoFit>
          <Interval
            adjust={[
            {
                type: 'dodge',
                marginRatio: 0,
              },
            ]}
            color="name"
            position="posisi dimana?"
          />
        
          <Tooltip shared />
        </Chart> */}
        <MyGauge mati={total[1]} kasus={total[0]} />
      </Col>

      <Col span='8'>
        <MyBar data={series2} />
      </Col>

      <Col span='8'>
        <MyDonut type_value_data={data} />
      </Col>
      
    </Row>
  </>);
}

export default DashboardBizcharts;

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/DashboardEcharts.js
import React, { useEffect, useState } from 'react';
import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';

import ReactEcharts from 'echarts-for-react';
import { 
  createOptions, createOptions2, createOptions3, createOptions4, createOptions5 
} from './chart_options';
import {
  echarts,create_series_item,create_xaxis,create_color,create_toolbox,create_legend,create_tooltip
} from './charts_helper'

const name_value_pairs = [
  {name: 'pH', value: 10},
  {name: 'COD', value: 20},
  {name: 'TSS', value: 30},
  {name: 'Q', value: 40},
]

const node_data = {
  data_ph: 
  {
    int: [1,2,3,4,5,6,7,8,9,10,11,12,13,14],
    float: [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0,5.0,3.0,2.0,1.0],
  }, 
  data_cod: [], 
  data_tss: [], 
  data_q: []
}

const DashboardEcharts = ({title1,subtitle1,data, labels, series1,series2}) => {
  return (<>
    <h1>DashboardEcharts</h1>

    <Row gutter={[8, 16]}>
      <Col span='8'>
        <ReactEcharts 
          option={createOptions(data, title1, subtitle1)} />
      </Col>
      <Col span='8'>
        <ReactEcharts 
          option={createOptions2(data, title1)} />
      </Col>
      <Col span='8'>
        <ReactEcharts 
          option={createOptions3(data, title1)} />
      </Col>
    </Row>

    <Row gutter={[8, 16]}>
      <Col span='12'>
        <ReactEcharts 
          option={createOptions4(data, title1)} />
      </Col>
      <Col span='12'>
        <ReactEcharts 
          option={createOptions5(data, title1)} />
      </Col>
    </Row>

    <Row gutter={[8, 16]}>
      <Col span='12'>
        <ReactEcharts 
          option={echarts(
            create_tooltip(),
            create_legend('Cases'),
            create_toolbox(),
            ["#55ce63"],
            create_xaxis(labels),
            [
              create_series_item('Cases', series1, [])
            ]
          )} />
      </Col>
      <Col span='12'>
        <ReactEcharts 
          option={echarts(
            create_tooltip(),
            create_legend('Deaths'),
            create_toolbox(),
            ["#fb9e11"],
            create_xaxis(labels),
            [
              create_series_item('Deaths', series2, [], 'line', true)
            ]
          )} />
      </Col>
    </Row>

    <Row gutter={[8, 16]}>
      <Col span='12'>
        <ReactEcharts 
          option={echarts(
            create_tooltip(),
            create_legend('Cases'),
            create_toolbox(),
            ["#009efb"],
            create_xaxis(labels),
            [
              create_series_item('Cases', series1, [], 'line', false, true)
            ]
          )} />
      </Col>
      <Col span='12'>
        <ReactEcharts 
          option={echarts(
            create_tooltip(),
            create_legend('Deaths'),
            create_toolbox(),
            ["#f62d51"],
            create_xaxis(labels),
            [
              create_series_item('Deaths', series2, [], 'bar')
            ]
          )} />
      </Col>
    </Row>

  </>);
}

export default DashboardEcharts;

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/DashboardHicharts.js
import React, { useEffect, useState } from 'react';
import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
import Highcharts from 'highcharts';
import HighchartsReact from 'highcharts-react-official';

const options = (judul, data, type='spline') => ({
    xAxis: {
        // type: 'datetime',
        // tickPixelInterval: 10,
        // categories: input_data.map(item => item[0]),
        // https://stackoverflow.com/questions/19381530/highcharts-x-axis-labels-as-text
        // seriesData = [[label,value],[label,value]]
        type: 'category',
        labels: {
            enabled: true,
            // formatter: function() { return data[this.value][0];},
            // rotation: -45,
            // style: {
            //         fontSize: '13px',
            //         fontFamily: 'Verdana, sans-serif'
            //     },
            // }
        },
      },
    //   yAxis: {
    //     plotLines: [
    //       {
    //         color: '#FFFF00',
    //         width: 2,
    //         value: warning_value,
    //       },
    //       {
    //         color: '#FF0000',
    //         width: 2,
    //         value: danger_value,
    //       } 
    //     ],
    //   },
  chart: {
    type
  },
  title: {
    text: judul
  },
  series: [
    {
        // type: config.tipe_grafik,
        // color: config.warna,
        // name: elem.name,
        // data: config.init_data, // new Array(jumlah_datapoint).fill(0),
      data
    }
  ]
});

const DashboardHicharts = ({title1,subtitle1,total,data, data_percent,labels, series1,series2}) => {
  return (<>
    <h1>DashboardHicharts</h1>

    <Row gutter={[8, 16]}>
      <Col span='6'>
      <HighchartsReact highcharts={Highcharts} options={options(`Case ${title1}`,series1.map(item=>Object.values(item)))} />
      </Col>
      <Col span='6'>
      <HighchartsReact highcharts={Highcharts} options={options(`Case ${title1}`,series1.map(item=>Object.values(item)), 'line')} />
      </Col>
      <Col span='6'>
      <HighchartsReact highcharts={Highcharts} options={options(`Case ${title1}`,series1.map(item=>Object.values(item)), 'area')} />
      </Col>
      <Col span='6'>
      <HighchartsReact highcharts={Highcharts} options={options(`Case ${title1}`,series1.map(item=>Object.values(item)), 'bar')} />
      </Col>
    </Row>

    <Row gutter={[8, 16]}>
    <Col span='6'>
      <HighchartsReact highcharts={Highcharts} options={options(`Deaths ${title1}`,series2.map(item=>Object.values(item)), 'line')} />
      </Col>
      <Col span='6'>
      <HighchartsReact highcharts={Highcharts} options={options(`Deaths ${title1}`,series2.map(item=>Object.values(item)), 'column')} />
      </Col>
      <Col span='6'>
      <HighchartsReact highcharts={Highcharts} options={options(`Deaths ${title1}`,series2.map(item=>Object.values(item)), 'bar')} />
      </Col>
      <Col span='6'>
      <HighchartsReact highcharts={Highcharts} options={options(`Deaths ${title1}`,series2.map(item=>Object.values(item)), 'pie')} />
      </Col>
    </Row>

    <Row gutter={[8, 16]}>
      <Col span='8'>
        <HighchartsReact highcharts={Highcharts} options={options(`Case ${title1}`,series1.map(item=>Object.values(item)))} />
      </Col>

      <Col span='8'>
        <HighchartsReact highcharts={Highcharts} options={{
          chart: {
              type: 'bar'
          },
          title: {
              text: 'Historic World Population by Region'
          },
          subtitle: {
              text: 'Source: <a href="https://en.wikipedia.org/wiki/World_population">Wikipedia.org</a>'
          },
          xAxis: {
              categories: ['Africa', 'America', 'Asia', 'Europe', 'Oceania'],
              title: {
                  text: null
              }
          },
          yAxis: {
              min: 0,
              title: {
                  text: 'Population (millions)',
                  align: 'high'
              },
              labels: {
                  overflow: 'justify'
              }
          },
          tooltip: {
              valueSuffix: ' millions'
          },
          plotOptions: {
              bar: {
                  dataLabels: {
                      enabled: true
                  }
              }
          },
          legend: {
              layout: 'vertical',
              align: 'right',
              verticalAlign: 'top',
              x: -40,
              y: 80,
              floating: true,
              borderWidth: 1,
              backgroundColor:
                  Highcharts.defaultOptions.legend.backgroundColor || '#FFFFFF',
              shadow: true
          },
          credits: {
              enabled: false
          },
          series: [{
              name: 'Year 1800',
              data: [107, 31, 635, 203, 2]
          }, {
              name: 'Year 1900',
              data: [133, 156, 947, 408, 6]
          }, {
              name: 'Year 2000',
              data: [814, 841, 3714, 727, 31]
          }, {
              name: 'Year 2016',
              data: [1216, 1001, 4436, 738, 40]
          }]
      }} />
      </Col>
      <Col span='8'>
        <HighchartsReact highcharts={Highcharts} options={{
          chart: {
              type: 'column'
          },
          title: {
              text: 'Monthly Average Rainfall'
          },
          subtitle: {
              text: 'Source: WorldClimate.com'
          },
          xAxis: {
              categories: [
                  'Jan',
                  'Feb',
                  'Mar',
                  'Apr',
                  'May',
                  'Jun',
                  'Jul',
                  'Aug',
                  'Sep',
                  'Oct',
                  'Nov',
                  'Dec'
              ],
              crosshair: true
          },
          yAxis: {
              min: 0,
              title: {
                  text: 'Rainfall (mm)'
              }
          },
          tooltip: {
              headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
              pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                  '<td style="padding:0"><b>{point.y:.1f} mm</b></td></tr>',
              footerFormat: '</table>',
              shared: true,
              useHTML: true
          },
          plotOptions: {
              column: {
                  pointPadding: 0.2,
                  borderWidth: 0
              }
          },
          series: [{
              name: 'Tokyo',
              data: [49.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4]

          }, {
              name: 'New York',
              data: [83.6, 78.8, 98.5, 93.4, 106.0, 84.5, 105.0, 104.3, 91.2, 83.5, 106.6, 92.3]

          }, {
              name: 'London',
              data: [48.9, 38.8, 39.3, 41.4, 47.0, 48.3, 59.0, 59.6, 52.4, 65.2, 59.3, 51.2]

          }, {
              name: 'Berlin',
              data: [42.4, 33.2, 34.5, 39.7, 52.6, 75.5, 57.4, 60.4, 47.6, 39.1, 46.8, 51.1]

          }]
      }} />
      </Col>
    </Row>


    <Row gutter={[8, 16]}>
      <Col span='8'>
        <HighchartsReact highcharts={Highcharts} options={{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}} />
      </Col>

      <Col span='8'>
        <HighchartsReact highcharts={Highcharts} options={{

title: {
    text: 'Solar Employment Growth by Sector, 2010-2016'
},

subtitle: {
    text: 'Source: thesolarfoundation.com'
},

yAxis: {
    title: {
        text: 'Number of Employees'
    }
},

xAxis: {
    accessibility: {
        rangeDescription: 'Range: 2010 to 2017'
    }
},

legend: {
    layout: 'vertical',
    align: 'right',
    verticalAlign: 'middle'
},

plotOptions: {
    series: {
        label: {
            connectorAllowed: false
        },
        pointStart: 2010
    }
},

series: [{
    name: 'Installation',
    data: [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
}, {
    name: 'Manufacturing',
    data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
}, {
    name: 'Sales & Distribution',
    data: [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
}, {
    name: 'Project Development',
    data: [null, null, 7988, 12169, 15112, 22452, 34400, 34227]
}, {
    name: 'Other',
    data: [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
}],

responsive: {
    rules: [{
        condition: {
            maxWidth: 500
        },
        chartOptions: {
            legend: {
                layout: 'horizontal',
                align: 'center',
                verticalAlign: 'bottom'
            }
        }
    }]
}

}} />
      </Col>

      <Col span='8'>
        <HighchartsReact highcharts={Highcharts} options={{
    chart: {
        type: 'area'
    },
    accessibility: {
        description: 'Image description: An area chart compares the nuclear stockpiles of the USA and the USSR/Russia between 1945 and 2017. The number of nuclear weapons is plotted on the Y-axis and the years on the X-axis. The chart is interactive, and the year-on-year stockpile levels can be traced for each country. The US has a stockpile of 6 nuclear weapons at the dawn of the nuclear age in 1945. This number has gradually increased to 369 by 1950 when the USSR enters the arms race with 6 weapons. At this point, the US starts to rapidly build its stockpile culminating in 32,040 warheads by 1966 compared to the USSRâ€™s 7,089. From this peak in 1966, the US stockpile gradually decreases as the USSRâ€™s stockpile expands. By 1978 the USSR has closed the nuclear gap at 25,393. The USSR stockpile continues to grow until it reaches a peak of 45,000 in 1986 compared to the US arsenal of 24,401. From 1986, the nuclear stockpiles of both countries start to fall. By 2000, the numbers have fallen to 10,577 and 21,000 for the US and Russia, respectively. The decreases continue until 2017 at which point the US holds 4,018 weapons compared to Russiaâ€™s 4,500.'
    },
    title: {
        text: 'US and USSR nuclear stockpiles'
    },
    subtitle: {
        text: 'Sources: <a href="https://thebulletin.org/2006/july/global-nuclear-stockpiles-1945-2006">' +
            'thebulletin.org</a> &amp; <a href="https://www.armscontrol.org/factsheets/Nuclearweaponswhohaswhat">' +
            'armscontrol.org</a>'
    },
    xAxis: {
        allowDecimals: false,
        labels: {
            formatter: function () {
                return this.value; // clean, unformatted number for year
            }
        },
        accessibility: {
            rangeDescription: 'Range: 1940 to 2017.'
        }
    },
    yAxis: {
        title: {
            text: 'Nuclear weapon states'
        },
        labels: {
            formatter: function () {
                return this.value / 1000 + 'k';
            }
        }
    },
    tooltip: {
        pointFormat: '{series.name} had stockpiled <b>{point.y:,.0f}</b><br/>warheads in {point.x}'
    },
    plotOptions: {
        area: {
            pointStart: 1940,
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 2,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [{
        name: 'USA',
        data: [
            null, null, null, null, null, 6, 11, 32, 110, 235,
            369, 640, 1005, 1436, 2063, 3057, 4618, 6444, 9822, 15468,
            20434, 24126, 27387, 29459, 31056, 31982, 32040, 31233, 29224, 27342,
            26662, 26956, 27912, 28999, 28965, 27826, 25579, 25722, 24826, 24605,
            24304, 23464, 23708, 24099, 24357, 24237, 24401, 24344, 23586, 22380,
            21004, 17287, 14747, 13076, 12555, 12144, 11009, 10950, 10871, 10824,
            10577, 10527, 10475, 10421, 10358, 10295, 10104, 9914, 9620, 9326,
            5113, 5113, 4954, 4804, 4761, 4717, 4368, 4018
        ]
    }, {
        name: 'USSR/Russia',
        data: [null, null, null, null, null, null, null, null, null, null,
            5, 25, 50, 120, 150, 200, 426, 660, 869, 1060,
            1605, 2471, 3322, 4238, 5221, 6129, 7089, 8339, 9399, 10538,
            11643, 13092, 14478, 15915, 17385, 19055, 21205, 23044, 25393, 27935,
            30062, 32049, 33952, 35804, 37431, 39197, 45000, 43000, 41000, 39000,
            37000, 35000, 33000, 31000, 29000, 27000, 25000, 24000, 23000, 22000,
            21000, 20000, 19000, 18000, 18000, 17000, 16000, 15537, 14162, 12787,
            12600, 11400, 5500, 4512, 4502, 4502, 4500, 4500
        ]
    }]
}} />
      </Col>
    </Row>

  </>);
}

export default DashboardHicharts;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/DashboardRecharts.js

import React, { Component, useEffect, useState } from 'react';
import {   
  Area,
  AreaChart,  
  Bar,
  BarChart,
  Brush,
  CartesianGrid,
  ErrorBar,
  Label, 
  LabelList,
  Legend,
  Line,
  LineChart,  
  Pie,
  PieChart,
  ReferenceArea,
  ReferenceDot,
  ReferenceLine,
  ResponsiveContainer,
  Sector,
  Tooltip,
  XAxis,
  YAxis,
} from 'recharts';
import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
// https://ant.design/components/icon/

import { scalePow, scaleLog } from 'd3-scale';

import GridDashboard from './Recharter/GridDashboard';

import _ from 'lodash';

const scale = scaleLog().base(10).nice();

function changeNumberOfData(data) {
  if (Array.isArray(data)) {
    return data.map(changeNumberOfData);
  }

  if (typeof data === 'object') {
    return _.mapValues(data, val => {
      if (typeof val === 'number') {
        return Math.floor(val * Math.random() * 2);
      }

      return changeNumberOfData(val);
    });
  }

  return data;
}

class CustomLineDot extends Component {

  static displayName = 'CustomLineDotDemo';

  render() {
    const { cx, cy, stroke, payload } = this.props;

    if (cx !== +cx || cy !== +cy) { return null; }

    if (payload.value > 250) {
      return (
        <svg x={cx - 10} y={cy - 10} width={20} height={20} fill="red" viewBox="0 0 1024 1024">
          <path d="M512 1009.984c-274.912 0-497.76-222.848-497.76-497.76s222.848-497.76 497.76-497.76c274.912 0 497.76 222.848 497.76 497.76s-222.848 497.76-497.76 497.76zM340.768 295.936c-39.488 0-71.52 32.8-71.52 73.248s32.032 73.248 71.52 73.248c39.488 0 71.52-32.8 71.52-73.248s-32.032-73.248-71.52-73.248zM686.176 296.704c-39.488 0-71.52 32.8-71.52 73.248s32.032 73.248 71.52 73.248c39.488 0 71.52-32.8 71.52-73.248s-32.032-73.248-71.52-73.248zM772.928 555.392c-18.752-8.864-40.928-0.576-49.632 18.528-40.224 88.576-120.256 143.552-208.832 143.552-85.952 0-164.864-52.64-205.952-137.376-9.184-18.912-31.648-26.592-50.08-17.28-18.464 9.408-21.216 21.472-15.936 32.64 52.8 111.424 155.232 186.784 269.76 186.784 117.984 0 217.12-70.944 269.76-186.784 8.672-19.136 9.568-31.2-9.12-40.096z"/>
        </svg>
      );
    }

    return (
      <svg x={cx - 10} y={cy - 10} width={20} height={20} fill="green" viewBox="0 0 1024 1024">
        <path d="M517.12 53.248q95.232 0 179.2 36.352t145.92 98.304 98.304 145.92 36.352 179.2-36.352 179.2-98.304 145.92-145.92 98.304-179.2 36.352-179.2-36.352-145.92-98.304-98.304-145.92-36.352-179.2 36.352-179.2 98.304-145.92 145.92-98.304 179.2-36.352zM663.552 261.12q-15.36 0-28.16 6.656t-23.04 18.432-15.872 27.648-5.632 33.28q0 35.84 21.504 61.44t51.2 25.6 51.2-25.6 21.504-61.44q0-17.408-5.632-33.28t-15.872-27.648-23.04-18.432-28.16-6.656zM373.76 261.12q-29.696 0-50.688 25.088t-20.992 60.928 20.992 61.44 50.688 25.6 50.176-25.6 20.48-61.44-20.48-60.928-50.176-25.088zM520.192 602.112q-51.2 0-97.28 9.728t-82.944 27.648-62.464 41.472-35.84 51.2q-1.024 1.024-1.024 2.048-1.024 3.072-1.024 8.704t2.56 11.776 7.168 11.264 12.8 6.144q25.6-27.648 62.464-50.176 31.744-19.456 79.36-35.328t114.176-15.872q67.584 0 116.736 15.872t81.92 35.328q37.888 22.528 63.488 50.176 17.408-5.12 19.968-18.944t0.512-18.944-3.072-7.168-1.024-3.072q-26.624-55.296-100.352-88.576t-176.128-33.28z"/>
      </svg>
    );
  }
}

const data = [
  { name: 'Page A', uv: 1000, pv: 2400, amt: 2400, uvError: [75, 20] },
  { name: 'Page B', uv: 300, pv: 4567, amt: 2400, uvError: [90, 40] },
  { name: 'Page C', uv: 280, pv: 1398, amt: 2400, uvError: 40 },
  { name: 'Page D', uv: 200, pv: 9800, amt: 2400, uvError: 20 },
  { name: 'Page E', uv: 278, pv: null, amt: 2400, uvError: 28 },
  { name: 'Page F', uv: 189, pv: 4800, amt: 2400, uvError: [90, 20] },
  { name: 'Page G', uv: 189, pv: 4800, amt: 2400, uvError: [28, 40] },
  { name: 'Page H', uv: 189, pv: 4800, amt: 2400, uvError: 28 },
  { name: 'Page I', uv: 189, pv: 4800, amt: 2400, uvError: 28 },
  { name: 'Page J', uv: 189, pv: 4800, amt: 2400, uvError: [15, 60] },
];

const data01 = [
  { day: '05-01', weather: 'sunny' },
  { day: '05-02', weather: 'sunny' },
  { day: '05-03', weather: 'cloudy' },
  { day: '05-04', weather: 'rain' },
  { day: '05-05', weather: 'rain' },
  { day: '05-06', weather: 'cloudy' },
  { day: '05-07', weather: 'cloudy' },
  { day: '05-08', weather: 'sunny' },
  { day: '05-09', weather: 'sunny' },
];

const data02 = [
  { name: 'Page A', uv: 300, pv: 2600, amt: 3400 },
  { name: 'Page B', uv: 400, pv: 4367, amt: 6400 },
  { name: 'Page C', uv: 300, pv: 1398, amt: 2400 },
  { name: 'Page D', uv: 200, pv: 9800, amt: 2400 },
  { name: 'Page E', uv: 278, pv: 3908, amt: 2400 },
  { name: 'Page F', uv: 189, pv: 4800, amt: 2400 },
  { name: 'Page G', uv: 189, pv: 4800, amt: 2400 },
];

const data03 = [
  { date: 'Jan 04 2016', price: 105.35 },
  { date: 'Jan 05 2016', price: 102.71 },
  { date: 'Jan 06 2016', price: 100.7 },
  { date: 'Jan 07 2016', price: 96.45 },
  { date: 'Jan 08 2016', price: 96.96 },
  { date: 'Jan 11 2016', price: 98.53 },
  { date: 'Jan 12 2016', price: 99.96 },
  { date: 'Jan 13 2016', price: 97.39 },
  { date: 'Jan 14 2016', price: 99.52 },
  { date: 'Jan 15 2016', price: 97.13 },
  { date: 'Jan 19 2016', price: 96.66 },
  { date: 'Jan 20 2016', price: 96.79 },
  { date: 'Jan 21 2016', price: 96.3 },
  { date: 'Jan 22 2016', price: 101.42 },
  { date: 'Jan 25 2016', price: 99.44 },
  { date: 'Jan 26 2016', price: 99.99 },
  { date: 'Jan 27 2016', price: 93.42 },
  { date: 'Jan 28 2016', price: 94.09 },
  { date: 'Jan 29 2016', price: 97.34 },
  { date: 'Feb 01 2016', price: 96.43 },
  { date: 'Feb 02 2016', price: 94.48 },
  { date: 'Feb 03 2016', price: 96.35 },
  { date: 'Feb 04 2016', price: 96.6 },
  { date: 'Feb 05 2016', price: 94.02 },
  { date: 'Feb 08 2016', price: 95.01 },
  { date: 'Feb 09 2016', price: 94.99 },
  { date: 'Feb 10 2016', price: 94.27 },
  { date: 'Feb 11 2016', price: 93.7 },
  { date: 'Feb 12 2016', price: 93.99 },
  { date: 'Feb 16 2016', price: 96.64 },
  { date: 'Feb 17 2016', price: 98.12 },
  { date: 'Feb 18 2016', price: 96.26 },
  { date: 'Feb 19 2016', price: 96.04 },
  { date: 'Feb 22 2016', price: 96.88 },
  { date: 'Feb 23 2016', price: 94.69 },
  { date: 'Feb 24 2016', price: 96.1 },
  { date: 'Feb 25 2016', price: 96.76 },
  { date: 'Feb 26 2016', price: 96.91 },
  { date: 'Feb 29 2016', price: 96.69 },
  { date: 'Mar 01 2016', price: 100.53 },
  { date: 'Mar 02 2016', price: 100.75 },
  { date: 'Mar 03 2016', price: 101.5 },
  { date: 'Mar 04 2016', price: 103.01 },
  { date: 'Mar 07 2016', price: 101.87 },
  { date: 'Mar 08 2016', price: 101.03 },
  { date: 'Mar 09 2016', price: 101.12 },
  { date: 'Mar 10 2016', price: 101.17 },
  { date: 'Mar 11 2016', price: 102.26 },
  { date: 'Mar 14 2016', price: 102.52 },
  { date: 'Mar 15 2016', price: 104.58 },
  { date: 'Mar 16 2016', price: 105.97 },
  { date: 'Mar 17 2016', price: 105.8 },
  { date: 'Mar 18 2016', price: 105.92 },
  { date: 'Mar 21 2016', price: 105.91 },
  { date: 'Mar 22 2016', price: 106.72 },
  { date: 'Mar 23 2016', price: 106.13 },
  { date: 'Mar 24 2016', price: 105.67 },
  { date: 'Mar 28 2016', price: 105.19 },
  { date: 'Mar 29 2016', price: 107.68 },
  { date: 'Mar 30 2016', price: 109.56 },
  { date: 'Mar 31 2016', price: 108.99 },
  { date: 'Apr 01 2016', price: 109.99 },
  { date: 'Apr 04 2016', price: 111.12 },
  { date: 'Apr 05 2016', price: 109.81 },
  { date: 'Apr 06 2016', price: 110.96 },
  { date: 'Apr 07 2016', price: 108.54 },
  { date: 'Apr 08 2016', price: 108.66 },
  { date: 'Apr 11 2016', price: 109.02 },
  { date: 'Apr 12 2016', price: 110.44 },
  { date: 'Apr 13 2016', price: 112.04 },
  { date: 'Apr 14 2016', price: 112.1 },
  { date: 'Apr 15 2016', price: 109.85 },
  { date: 'Apr 18 2016', price: 107.48 },
  { date: 'Apr 19 2016', price: 106.91 },
  { date: 'Apr 20 2016', price: 107.13 },
  { date: 'Apr 21 2016', price: 105.97 },
  { date: 'Apr 22 2016', price: 105.68 },
  { date: 'Apr 25 2016', price: 105.08 },
  { date: 'Apr 26 2016', price: 104.35 },
  { date: 'Apr 27 2016', price: 97.82 },
  { date: 'Apr 28 2016', price: 94.83 },
  { date: 'Apr 29 2016', price: 93.74 },
  { date: 'May 02 2016', price: 93.64 },
  { date: 'May 03 2016', price: 95.18 },
  { date: 'May 04 2016', price: 94.19 },
  { date: 'May 05 2016', price: 93.24 },
  { date: 'May 06 2016', price: 92.72 },
  { date: 'May 09 2016', price: 92.79 },
  { date: 'May 10 2016', price: 93.42 },
  { date: 'May 11 2016', price: 92.51 },
  { date: 'May 12 2016', price: 90.34 },
  { date: 'May 13 2016', price: 90.52 },
  { date: 'May 16 2016', price: 93.88 },
  { date: 'May 17 2016', price: 93.49 },
  { date: 'May 18 2016', price: 94.56 },
  { date: 'May 19 2016', price: 94.2 },
  { date: 'May 20 2016', price: 95.22 },
  { date: 'May 23 2016', price: 96.43 },
  { date: 'May 24 2016', price: 97.9 },
  { date: 'May 25 2016', price: 99.62 },
  { date: 'May 26 2016', price: 100.41 },
  { date: 'May 27 2016', price: 100.35 },
  { date: 'May 31 2016', price: 99.86 },
  { date: 'Jun 01 2016', price: 98.46 },
  { date: 'Jun 02 2016', price: 97.72 },
  { date: 'Jun 03 2016', price: 97.92 },
  { date: 'Jun 06 2016', price: 98.63 },
  { date: 'Jun 07 2016', price: 99.03 },
  { date: 'Jun 08 2016', price: 98.94 },
  { date: 'Jun 09 2016', price: 99.65 },
  { date: 'Jun 10 2016', price: 98.83 },
  { date: 'Jun 13 2016', price: 97.34 },
  { date: 'Jun 14 2016', price: 97.46 },
  { date: 'Jun 15 2016', price: 97.14 },
  { date: 'Jun 16 2016', price: 97.55 },
  { date: 'Jun 17 2016', price: 95.33 },
  { date: 'Jun 20 2016', price: 95.1 },
  { date: 'Jun 21 2016', price: 95.91 },
  { date: 'Jun 22 2016', price: 95.55 },
  { date: 'Jun 23 2016', price: 96.1 },
  { date: 'Jun 24 2016', price: 93.4 },
  { date: 'Jun 27 2016', price: 92.04 },
  { date: 'Jun 28 2016', price: 93.59 },
  { date: 'Jun 29 2016', price: 94.4 },
  { date: 'Jun 30 2016', price: 95.6 },
  { date: 'Jul 01 2016', price: 95.89 },
  { date: 'Jul 05 2016', price: 94.99 },
  { date: 'Jul 06 2016', price: 95.53 },
  { date: 'Jul 07 2016', price: 95.94 },
  { date: 'Jul 08 2016', price: 96.68 },
  { date: 'Jul 11 2016', price: 96.98 },
  { date: 'Jul 12 2016', price: 97.42 },
  { date: 'Jul 13 2016', price: 96.87 },
  { date: 'Jul 14 2016', price: 98.79 },
  { date: 'Jul 15 2016', price: 98.78 },
  { date: 'Jul 18 2016', price: 99.83 },
  { date: 'Jul 19 2016', price: 99.87 },
  { date: 'Jul 20 2016', price: 99.96 },
  { date: 'Jul 21 2016', price: 99.43 },
  { date: 'Jul 22 2016', price: 98.66 },
  { date: 'Jul 25 2016', price: 97.34 },
  { date: 'Jul 26 2016', price: 96.67 },
  { date: 'Jul 27 2016', price: 102.95 },
  { date: 'Jul 28 2016', price: 104.34 },
  { date: 'Jul 29 2016', price: 104.21 },
  { date: 'Aug 01 2016', price: 106.05 },
  { date: 'Aug 02 2016', price: 104.48 },
  { date: 'Aug 03 2016', price: 105.79 },
  { date: 'Aug 04 2016', price: 105.87 },
  { date: 'Aug 05 2016', price: 107.48 },
  { date: 'Aug 08 2016', price: 108.37 },
  { date: 'Aug 09 2016', price: 108.81 },
  { date: 'Aug 10 2016', price: 108 },
  { date: 'Aug 11 2016', price: 107.93 },
  { date: 'Aug 12 2016', price: 108.18 },
  { date: 'Aug 15 2016', price: 109.48 },
  { date: 'Aug 16 2016', price: 109.38 },
  { date: 'Aug 17 2016', price: 109.22 },
  { date: 'Aug 18 2016', price: 109.08 },
  { date: 'Aug 19 2016', price: 109.36 },
  { date: 'Aug 22 2016', price: 108.51 },
  { date: 'Aug 23 2016', price: 108.85 },
  { date: 'Aug 24 2016', price: 108.03 },
  { date: 'Aug 25 2016', price: 107.57 },
  { date: 'Aug 26 2016', price: 106.94 },
  { date: 'Aug 29 2016', price: 106.82 },
  { date: 'Aug 30 2016', price: 106 },
  { date: 'Aug 31 2016', price: 106.1 },
  { date: 'Sept 01 2016', price: 106.73 },
  { date: 'Sept 02 2016', price: 107.73 },
  { date: 'Sept 06 2016', price: 107.7 },
  { date: 'Sept 07 2016', price: 108.36 },
  { date: 'Sept 08 2016', price: 105.52 },
  { date: 'Sept 09 2016', price: 103.13 },
  { date: 'Sept 12 2016', price: 105.44 },
  { date: 'Sept 13 2016', price: 107.95 },
  { date: 'Sept 14 2016', price: 111.77 },
  { date: 'Sept 15 2016', price: 115.57 },
  { date: 'Sept 16 2016', price: 114.92 },
  { date: 'Sept 19 2016', price: 113.58 },
  { date: 'Sept 20 2016', price: 113.57 },
  { date: 'Sept 21 2016', price: 113.55 },
  { date: 'Sept 22 2016', price: 114.62 },
  { date: 'Sept 23 2016', price: 112.71 },
  { date: 'Sept 26 2016', price: 112.88 },
  { date: 'Sept 27 2016', price: 113.09 },
  { date: 'Sept 28 2016', price: 113.95 },
  { date: 'Sept 29 2016', price: 112.18 },
  { date: 'Sept 30 2016', price: 113.05 },
  { date: 'Oct 03 2016', price: 112.52 },
  { date: 'Oct 04 2016', price: 113 },
  { date: 'Oct 05 2016', price: 113.05 },
  { date: 'Oct 06 2016', price: 113.89 },
  { date: 'Oct 07 2016', price: 114.06 },
  { date: 'Oct 10 2016', price: 116.05 },
  { date: 'Oct 11 2016', price: 116.3 },
  { date: 'Oct 12 2016', price: 117.34 },
  { date: 'Oct 13 2016', price: 116.98 },
  { date: 'Oct 14 2016', price: 117.63 },
  { date: 'Oct 17 2016', price: 117.55 },
  { date: 'Oct 18 2016', price: 117.47 },
  { date: 'Oct 19 2016', price: 117.12 },
  { date: 'Oct 20 2016', price: 117.06 },
  { date: 'Oct 21 2016', price: 116.6 },
  { date: 'Oct 24 2016', price: 117.65 },
  { date: 'Oct 25 2016', price: 118.25 },
  { date: 'Oct 26 2016', price: 115.59 },
  { date: 'Oct 27 2016', price: 114.48 },
  { date: 'Oct 28 2016', price: 113.72 },
  { date: 'Oct 31 2016', price: 113.54 },
  { date: 'Nov 01 2016', price: 111.49 },
  { date: 'Nov 02 2016', price: 111.59 },
  { date: 'Nov 03 2016', price: 109.83 },
  { date: 'Nov 04 2016', price: 108.84 },
  { date: 'Nov 07 2016', price: 110.41 },
  { date: 'Nov 08 2016', price: 111.06 },
  { date: 'Nov 09 2016', price: 110.88 },
  { date: 'Nov 10 2016', price: 107.79 },
  { date: 'Nov 11 2016', price: 108.43 },
  { date: 'Nov 14 2016', price: 105.71 },
  { date: 'Nov 15 2016', price: 107.11 },
  { date: 'Nov 16 2016', price: 109.99 },
  { date: 'Nov 17 2016', price: 109.95 },
  { date: 'Nov 18 2016', price: 110.06 },
  { date: 'Nov 21 2016', price: 111.73 },
  { date: 'Nov 22 2016', price: 111.8 },
  { date: 'Nov 23 2016', price: 111.23 },
  { date: 'Nov 25 2016', price: 111.79 },
  { date: 'Nov 28 2016', price: 111.57 },
  { date: 'Nov 29 2016', price: 111.46 },
  { date: 'Nov 30 2016', price: 110.52 },
  { date: 'Dec 01 2016', price: 109.49 },
  { date: 'Dec 02 2016', price: 109.9 },
  { date: 'Dec 05 2016', price: 109.11 },
  { date: 'Dec 06 2016', price: 109.95 },
  { date: 'Dec 07 2016', price: 111.03 },
  { date: 'Dec 08 2016', price: 112.12 },
  { date: 'Dec 09 2016', price: 113.95 },
  { date: 'Dec 12 2016', price: 113.3 },
  { date: 'Dec 13 2016', price: 115.19 },
  { date: 'Dec 14 2016', price: 115.19 },
  { date: 'Dec 15 2016', price: 115.82 },
  { date: 'Dec 16 2016', price: 115.97 },
  { date: 'Dec 19 2016', price: 116.64 },
  { date: 'Dec 20 2016', price: 116.95 },
  { date: 'Dec 21 2016', price: 117.06 },
  { date: 'Dec 22 2016', price: 116.29 },
  { date: 'Dec 23 2016', price: 116.52 },
  { date: 'Dec 27 2016', price: 117.26 },
  { date: 'Dec 28 2016', price: 116.76 },
  { date: 'Dec 29 2016', price: 116.73 },
  { date: 'Dec 30 2016', price: 115.82 },
];

const series = [
  { name: 'Series 1', data: [
    { category: 'A', value: Math.random() },
    { category: 'B', value: Math.random() },
    { category: 'C', value: Math.random() }
  ] },
  { name: 'Series 2', data: [
    { category: 'B', value: Math.random() },
    { category: 'C', value: Math.random() },
    { category: 'D', value: Math.random() }
  ] },
  { name: 'Series 3', data: [
    { category: 'C', value: Math.random() },
    { category: 'D', value: Math.random() },
    { category: 'E', value: Math.random() }
  ] },
];

const renderSpecialDot = (props) => {
  const { cx, cy, stroke, key } = props;

  if (cx === +cx && cy === +cy) {
    return <path d={`M${cx - 2},${cy - 2}h4v4h-4Z`} fill={stroke} key={key} />;
  }

  return null;
};


const renderActiveShape = (props) => {
	const RADIAN = Math.PI / 180;
	const {
		cx, cy, midAngle, innerRadius, outerRadius, startAngle, endAngle,
		fill, payload, percent, value,
	} = props;
	const sin = Math.sin(-RADIAN * midAngle);
	const cos = Math.cos(-RADIAN * midAngle);
	const sx = cx + (outerRadius + 10) * cos;
	const sy = cy + (outerRadius + 10) * sin;
	const mx = cx + (outerRadius + 30) * cos;
	const my = cy + (outerRadius + 30) * sin;
	const ex = mx + (cos >= 0 ? 1 : -1) * 22;
	const ey = my;
	const textAnchor = cos >= 0 ? 'start' : 'end';

	return (
		<g>
			<text x={cx} y={cy} dy={8} textAnchor="middle" fill={fill}>{payload.name}</text>
      <text x={cx} y={cy+20} dy={8} textAnchor="middle" fill={fill}>{payload.value}</text>
			<Sector
				cx={cx}
				cy={cy}
				innerRadius={innerRadius}
				outerRadius={outerRadius}
				startAngle={startAngle}
				endAngle={endAngle}
				fill={fill}
			/>
			<Sector
				cx={cx}
				cy={cy}
				startAngle={startAngle}
				endAngle={endAngle}
				innerRadius={outerRadius + 6}
				outerRadius={outerRadius + 10}
				fill={fill}
			/>
			<path d={`M${sx},${sy}L${mx},${my}L${ex},${ey}`} stroke={fill} fill="none" />
			<circle cx={ex} cy={ey} r={2} fill={fill} stroke="none" />
			<text x={ex + (cos >= 0 ? 1 : -1) * 12} y={ey} textAnchor={textAnchor} fill="#333">{`#: ${value}`}</text>
			<text x={ex + (cos >= 0 ? 1 : -1) * 12} y={ey} dy={18} textAnchor={textAnchor} fill="#999">
				{`(P: ${(percent * 100).toFixed(2)}%)`}
			</text>
		</g>
	);
};


const DashboardRecharts = ({title1,subtitle1,data, labels, series1,series2}) => {

  const width = 400;
  const height = 200;
  const COLORS = ['#0088FE', '#00C49F', '#FFBB28', '#FF8042'];
  const [pieindex, setPieindex] = useState(0);

  return (<>
    <h1>DashboardRecharts Y</h1>
    <Row gutter={[8, 16]}>
      <Col span='12'>
        <LineChart
          width={width}
          height={height}
          data={series1}
          margin={{ left: 10, right: 10 }}
        >
          <CartesianGrid strokeDasharray="3 3" strokeOpacity={0.1} />
          <XAxis dataKey="time" />
          <YAxis dataKey="value" mirror />
          <Line
            type="monotone"
            dataKey="value"
            stroke="#82ca9d"
            dot={false}
            isAnimationActive={false}
          />
        </LineChart>
      </Col>
      <Col span='12'>
      <AreaChart
          width={width}
          height={height}
          data={series2}
          margin={{ left: 10, right: 10 }}
        >
          <CartesianGrid strokeDasharray="3 3" strokeOpacity={0.1} />
          <XAxis dataKey="time" />
          <YAxis dataKey="value" mirror />
          <Area
            dataKey="value"
            fill="#82ca9d"
            stroke="#82ca9d"
            isAnimationActive={false}
          />
        </AreaChart>
      </Col>
    </Row>

    <Row gutter={[8, 16]}>
      <Col span='12'>
        <PieChart width={width} height={height}>
          <Pie
            data={series1}
            dataKey="value"
            nameKey="time"
            cx="50%"
            cy="50%"
            outerRadius={100}
            fill="#82ca9d"
            isAnimationActive={false}
          />
        </PieChart>
      </Col>
      <Col span='12'>
        <BarChart
          width={width}
          height={height}
          data={series2}
          margin={{ left: 10, right: 10 }}
        >
          <CartesianGrid strokeDasharray="3 3" strokeOpacity={0.1} />
          <XAxis dataKey="time" />
          <YAxis dataKey="value" mirror />
          <Bar dataKey="value" fill="#8884d8" isAnimationActive={false} />
        </BarChart>
      </Col>
    </Row>

    <Row gutter={[16, 16]}>
      <Col span='24'>
        <PieChart width={width+100} height={height+100} style={{margin:50}}>
          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            cx="50%"
            cy="50%"
            colors={ COLORS }
            outerRadius={100}
            innerRadius={80}
            onMouseEnter={(data,index)=>setPieindex(index)}
            activeShape={renderActiveShape}
            activeIndex={pieindex}
            hole={10}
            label
            // fill="#82ca9d"
            fill="#8884d8"
            isAnimationActive={false}
          />
        </PieChart>
      </Col>
    </Row>

    {/* <Row gutter={[8, 16]}>
      <Col span='8'>
      <LineChart width={400} height={400} data={data02} syncId="test">
            <CartesianGrid stroke="#f5f5f5" fill="#e6e6e6" />
            <Legend
              // onMouseEnter={this.handleLegendMouseEnter}
              // onMouseLeave={this.handleLegendMouseLeave}
            />
            <XAxis type="number" dataKey="pv" height={40} label={<div>Hello</div>}>
              <Label value="xè½´" position="insideBottom" />
            </XAxis>
            <YAxis type="number" unit="%" width={80}>
              <Label value="yè½´" position="insideLeft" angle={90} />
            </YAxis>
            <Tooltip trigger="click" />
            <Line
              key="uv"
              type="monotone"
              dataKey="uv"
              stroke="#ff7300"
              dot={renderSpecialDot}
              strokeOpacity={opacity}
              strokeDasharray="3 3"
            >
              <LabelList position="bottom" offset={10} dataKey="name" />
            </Line>
            <Brush dataKey="name" height={30} />
          </LineChart>
      </Col>
      <Col span='8'>
        <LineChart
            width={400} height={400} data={data01}
            margin={{ top: 20, right: 20, bottom: 20, left: 20 }}>
            <XAxis dataKey="day" />
            <YAxis type="category" domain={['cloudy', 'rain', 'sunny']} />
            <Tooltip />
            <Line type="stepAfter" dataKey="weather" stroke="#ff7300" />
          </LineChart>
      </Col>
      <Col span='8'>
      <LineChart
            width={400}
            height={400}
            data={data}
            margin={{ top: 20, right: 20, bottom: 20, left: 20 }}
            syncId="test"
          >
            <CartesianGrid stroke='#f5f5f5' verticalFill={['rgba(0, 0, 0, 0.2)', 'rgba(255, 255, 255, 0.3)']} horizontalFill={['#ccc', '#fff']} />
            <Legend />
            <XAxis dataKey="name" axisLine={{ stroke: 'red' }} />
            <YAxis scale={scale} domain={[0.01, 'auto']} ticks={[0.01, 0.1, 1, 10, 100, 1000]} />
            <Tooltip />
            <Line type='monotone' dataKey='uv' dot={<CustomLineDot/>} stroke='#ff7300' />
          </LineChart>
      </Col>
    </Row> */}



  </>);
}

export default DashboardRecharts;

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/MyBar.js
import React, { useEffect, useState } from 'react';
import { Chart, Interval, Tooltip } from 'bizcharts';

const data = [
  { year: '1951 å¹´', sales: 38 },
  { year: '1952 å¹´', sales: 52 },
  { year: '1956 å¹´', sales: 61 },
  { year: '1957 å¹´', sales: 45 },
  { year: '1958 å¹´', sales: 48 },
  { year: '1959 å¹´', sales: 38 },
  { year: '1960 å¹´', sales: 38 },
  { year: '1962 å¹´', sales: 38 },
];


function MyBar({data}) {
  return <Chart 
    height={400} 
    autoFit 
    data={data} 
    interactions={['active-region']} 
    padding={[30, 30, 30, 50]} >
    <Interval position="time*value" />
    <Tooltip shared />
  </Chart>
}
export default MyBar;

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/MyDonut.js
import React from "react";
import {
  Chart,
  registerShape,
  Geom,
  Axis,
  Tooltip,
  Interval,
  Interaction,
  Coordinate,
} from "bizcharts";

const data = [
  {
    type: "jenis 1",
    value: 20
  },
  {
    type: "jenis 2",
    value: 18
  },
  {
    type: "jenis 3",
    value: 32
  },
  {
    type: "jenis 4",
    value: 15
  },
  {
    type: "Other",
    value: 15
  }
];

const sliceNumber = 0.01;

registerShape("interval", "sliceShape", {
  draw(cfg, container) {
    const points = cfg.points;
    let path = [];
    path.push(["M", points[0].x, points[0].y]);
    path.push(["L", points[1].x, points[1].y - sliceNumber]);
    path.push(["L", points[2].x, points[2].y - sliceNumber]);
    path.push(["L", points[3].x, points[3].y]);
    path.push("Z");
    path = this.parsePath(path);
    return container.addShape("path", {
      attrs: {
        fill: cfg.color,
        path: path
      }
    });
  }
});
    

class MyDonut extends React.Component {
  render() {
    const { type_value_data } = this.props;
    return (
     <Chart data={type_value_data} height={500} autoFit >
        <Coordinate type="theta" radius={0.8} innerRadius={0.75} />
        <Axis visible={false} />
        <Tooltip showTitle={false} />
        <Interval
          adjust="stack"
          position="value"
          color="name"
          shape="sliceShape"
        />
        <Interaction type="element-single-selected" />
      </Chart>
       
    );
  }
}

export default MyDonut;
--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/MyGauge.js
import React, { useState, useEffect } from 'react';
import {
	Chart,
	Point,
	Area,
	Annotation,
	Axis,
	Coordinate,
	registerShape,
	registerAnimation,
} from 'bizcharts';

// registerShape('point', 'pointer', {
// 	draw(cfg, container) {

// 		const group = container.addGroup();

// 		const center = this.parsePoint({ x: 0, y: 0 });
// 		const start = this.parsePoint({ x: 0, y: 0.5 });


// 		const preAngle = this.preAngle || 0;

// 		const angle1 = Math.atan((start.y - center.y) / (start.x - center.x));
// 		const angle = (Math.PI - 2 * (angle1)) * cfg.points[0].x;

// 		this.preAngle = angle;

// 		return group;
// 	},
// });
function kFormatter(num) {
	return Math.abs(num) > 999999 ? Math.sign(num)*((Math.abs(num)/1000000).toFixed(1)) + 'M'
    : Math.abs(num) > 999 ? Math.sign(num)*((Math.abs(num)/1000).toFixed(1)) + 'K' : Math.sign(num)*Math.abs(num)
}

function MyGauge({mati, kasus}) {
	const [data, setData] = useState([{ value: mati }]);
	const startAngle = Math.PI / 2
	const endAngle = startAngle + Math.PI * 2;

  const scale = {
    value: {
      min: 0,
      // max: 1,
      max: kasus,
      // tickInterval: 0.1,
      tickInterval: kasus/10, // biar gak rame
      // formatter: v => v * 100
      formatter: v => kFormatter(v)
    }
  }

  const tinggi_chart=400;

	return (
		<Chart
			height={tinggi_chart}
			data={data}
			scale={scale}
			autoFit
		>
			<Coordinate
				type="polar"
				radius={0.75}
				startAngle={startAngle}
				endAngle={endAngle}
			/>
			<Axis
				name="value"
				line={null}
				// visible={false}
				label={{
					offset: -36,
					style: {
						fontSize: 18,
						textAlign: 'center',
						textBaseline: 'middle',
					},
				}}
				grid={null}
			/>
			<Point
				position="value*1"
				color="#1890FF"
				shape="pointer"
			/>
			<Annotation.Arc
				start={[0, 1]}
				end={[1, 1]}
				style={{
					stroke: '#CBCBCB',
					lineWidth: 18,
					lineDash: null,
					lineCap: 'round',
				}}
			/>
			<Annotation.Arc
				start={[0, 1]}
				// end={[data[0].value, 1]}
        end={[mati, 1]}
				style={{
					stroke: '#1890FF',
					lineCap: 'round',
					lineWidth: 18,
					lineDash: null,
				}}
			/>
			<Annotation.Text
				position={['50%', '60%']}
				// content={`${Math.round(data[0].value * 100)}%`}
        content={`${mati}/${kasus}\n ${(mati/kasus).toFixed(3)}%`}
				style={{
					fontSize: Math.round(tinggi_chart/25),
					fill: '#262626',
					textAlign: 'center',
				}}
			/>
		</Chart>
	)
}

export default MyGauge;

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/MyPie.js
import React from "react";
import {
	Chart,
	Interval,
	Tooltip,
	Axis,
	Coordinate,
	getTheme,
} from "bizcharts";

function MyPie({data}) {
	// const data = [
	// 	{ item: "item 1", percent: 0.4 },
	// 	{ item: "item 2", percent: 0.21 },
	// 	{ item: "item 3", percent: 0.17 },
	// 	{ item: "item 4", percent: 0.13 },
	// 	{ item: "item 5", percent: 0.09 },
	// ];
	const colors = data.reduce((pre, cur, idx) => {
		pre[cur.item] = getTheme().colors10[idx];
		return pre;
	}, {});

	const cols = {
		percent: {
			formatter: (val) => {
				// val = val * 100 + "%";
				return val;
			},
		},
	};

	return (
		<Chart height={400} data={data} scale={cols} interactions={['element-active']} autoFit>
			<Coordinate type="theta" radius={0.75} />
			<Tooltip showTitle={false} />
			<Axis visible={false} />
			<Interval
				position="percent"
				adjust="stack"
				color="item"
				style={{
					lineWidth: 1,
					stroke: "#fff",
				}}
				label={[
					"item",
					(item) => {
						return {
							offset: 20,
							content: (data) => {
								return `${data.item}\n ${data.percent}`;
							},
							style: {
								fill: colors[item],
							},
						};
					},
				]}
			/>
		</Chart>
	);
}

export default MyPie;

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/patterns.js

export const piePatternSrc = 'data:image/jpeg;base64,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';

export const bgPatternSrc = 'data:image/png;charset=utf-8;base64,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';
--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/README.md
https://github.com/recharts/recharts/tree/master/demo/component

https://github.com/recharts/recharts/blob/master/demo/component/BarChart.tsx

https://github.com/recharts/recharts/blob/master/demo/component/AreaChart.tsx

https://github.com/recharts/recharts/blob/master/demo/component/PieChart.tsx

https://codesandbox.io/examples/package/recharts

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Speedy.js
import React, { useState, useEffect } from 'react';
import {
	Chart,
	Point,
	Area,
	Annotation,
	Axis,
	Coordinate,
	registerShape,
	registerAnimation,
} from 'bizcharts';

function kFormatter(num) {
	return Math.abs(num) > 999999 ? Math.sign(num)*((Math.abs(num)/1000000).toFixed(1)) + 'M'
    : Math.abs(num) > 999 ? Math.sign(num)*((Math.abs(num)/1000).toFixed(1)) + 'K' : Math.sign(num)*Math.abs(num)
}

registerShape('point', 'pointer', {
	draw(cfg, container) {

		const group = container.addGroup();
		// console.log(cfg)
		const center = this.parsePoint({ x: 0, y: 0 });
		const start = this.parsePoint({ x: 0, y: 0 });

		const line = group.addShape('line', {
			attrs: {
				x1: center.x,
				y1: center.y,
				x2: cfg.x,
				y2: cfg.y,
				stroke: cfg.color,
				lineWidth: 5,
				lineCap: 'round',
			},
		});
		group.addShape('circle', {
			attrs: {
				x: center.x,
				y: center.y,
				r: 9.75,
				stroke: cfg.color,
				lineWidth: 4.5,
				fill: '#fff',
			},
		});

		const preAngle = this.preAngle || 0;

		const angle1 = Math.atan((start.y - center.y) / (start.x - center.x));
		const angle = (Math.PI - 2 * (angle1)) * cfg.points[0].x;

		
		if (group.cfg.animable) {
			group.animate((ratio) => {
				group.resetMatrix();
				group.rotateAtPoint(center.x, center.y, preAngle + (angle - preAngle) * ratio);
			}, 300);
		} else {
			group.rotateAtPoint(center.x, center.y, angle);
		}
		this.preAngle = angle;

		return group;
	},
});

registerAnimation('cust-animation', (shape) => {
	console.log('cust-animation', shape)
})


function Speedy({mati, kasus}) {
	const [data, setData] = useState([{ value: mati }]);

	const scale = {
		value: {
			min: 0,
			max: kasus,
			tickInterval: kasus/10, // biar gak rame
			formatter: v => kFormatter(v)
		}
	}
	
	useEffect(() => {
		setTimeout(() => {
			setData([{ value: mati }])
		}, 1000)
	}, [])
	return (
		<Chart
			height={500}
			data={data}
			scale={scale}
			autoFit
		>
			<Coordinate
				type="polar"
				radius={0.75}
				startAngle={(-12 / 10) * Math.PI}
				endAngle={(2 / 10) * Math.PI}
			/>
			<Axis name="1" />
			<Axis
				name="value"
				line={null}
				label={{
					offset: -36,
					style: {
						fontSize: 18,
						textAlign: 'center',
						textBaseline: 'middle',
					},
				}}
				subTickLine={{
					count: 4,
					length: -15,
				}}
				tickLine={{
					length: -24,
				}}
				grid={null}
			/>
			<Point
				position="value*1"
				color="#1890FF"
				shape="pointer"				
			/>
			<Annotation.Arc
				start={[0, 1]}
				end={[1, 1]}
				style={{
					stroke: '#CBCBCB',
					lineWidth: 18,
					lineDash: null,
				}}
			/>
			<Annotation.Arc
				start={[0, 1]}
				end={[mati, 1]}
				style={{
					stroke: '#1890FF',
					lineWidth: 18,
					lineDash: null,
				}}
			/>
			<Annotation.Text
				position={['50%', '50%']}
				content={`${mati}\n ${(mati/kasus).toFixed(3)}%`}
				style={{
					fontSize: 24,
					fill: '#262626',
					textAlign: 'center',
				}}
			/>
		</Chart>
	)
}

export default Speedy;
--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/useAxios.js
import React, { useState, useContext } from 'react';

import axios from 'axios';
import config from '#/config';

const initialState = {
  isFetching: false,
  isError: false,
  // statusCode: null,
  // code: null,
  // message: null,
  // details: null,
  data: null,
}

export default ({
  method = 'GET',
  path,
  headers = {},
}) => {

  const [state, setState] = useState(initialState);

  if (path === undefined) path = '';
  const url = `${config.server()}/${path}`;

  const originalArgs = {
    method,
    url,
    data: null,
    params: {},
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      ...headers,
    }
  }

  const sender = (newArgs={}, successCb=undefined, errorCb=undefined) => {

    let updatedArgs = {
      ...originalArgs,
      ...newArgs,
    };
    if (newArgs.hasOwnProperty('path')) {
      updatedArgs['url'] = `${config.server()}/${newArgs["path"]}`;
    }
    // console.log(`useAxios: sending request to => ${url}.`);

    setState({
      ...initialState,
      isFetching: true,
    });

    axios(updatedArgs)
    .then(response => {
      if (response.data) {
        
        setState(prevState => ({
          ...prevState,
          data: response.data,
        }));

        if (successCb) {
          successCb(response.data);
        }

      }
    })
    .catch(error => {
      console.log(`useAxios: catch error => ${JSON.stringify(error)}.`);
      
      setState(prevState => ({
        ...prevState,
        isError: true,
      }));

      if (errorCb) {
        errorCb(error);
      }

    })
    .then(() => {
      
      setState({
        ...initialState,
        isFetching: false,
      });

    });
  }
  
  return sender;
}


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/index.js
import React from "react";
import {
  Button,
	Card,
	Col,
  DatePicker,
  Divider,
  Drawer,
  Input,
  InputNumber,
  Modal,
  Popover,
	Row,
  Select,
  Space,
	Statistic,
	Table,
} from 'antd';
import { WidthProvider, Responsive } from "react-grid-layout";
import MapItem from './MapItem';
// import { FullScreen, useFullScreenHandle } from "react-full-screen";
// import {FullScreen} from "react-full-screen";
import {default as FullScreen} from 'react-fullscreen-crossbrowser';

const ResponsiveReactGridLayout = WidthProvider(Responsive);

const tinggi_baris = 225;
const total = 10;
const lebar = 5;
const tinggi = 2;

// const jumlah_datapoint = 10;
// const NEW_CHART = '<<new chart>>';

const NEW_MAP = '<<new map>>';
const default_layer = {
  'tile': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
  'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  'name': 'OpenStreetMap_Mapnik',
}

function ActionComponent(props) {
  return <Card title={props.title} extra={props.RemoveComponent} style={{ width: 300 }}>
    <Button onClick={()=>props.go_fullscreen()}>Full</Button>
  </Card>
}

function RemoveComponent(props) {
  const removeStyle = {
    width: '10px',
    position: "absolute",
    right: "2px",
    top: 0,
    cursor: "pointer"
  };

  return <span
    className="remove"
    style={removeStyle}
    onClick={props.remove}
    >
    x
  </span>
}

export default class GridMap extends React.Component {

  state = {
    items: ['pertama'].map(function(item, key, list) {
      let per_kolom = (total/lebar);
      let posx = (key * lebar) % total;
      let posy = ~~(key / per_kolom);
      
      console.log(key, item, per_kolom, posx, posy);

      return {
        i: key.toString(),
        x: posx,
        y: item === (list.length - 1) ? Infinity : posy,
        w: lebar,
        h: tinggi,
        // index: key,
        name: item,
        add: item === (list.length - 1),
        resizeHandles: ["sw", "se"],
      };
    }),
    // controls: {},

    is_fullscreen: false,
    viewmap: [],
    map_ids: [],

  }

  constructor(props) {
    super(props);
    // this.chartElements = {};
  }

  componentDidMount() {
    PubSub.subscribe(NEW_MAP, this.new_map);
  }

  goFullScreen = () => {
    this.setState({ is_fullscreen: true });
  };

  new_map = (topic, data) => {
    this.onAddItem('map', data);
  }

  onAddItem = (type, {name}) => {
    // if (type === 'chart') {
    //   if (!this.state.charttokens.hasOwnProperty(name)) {
    //     let charttoken = PubSub.subscribe('sensor:data:' + name, this.sensorDataHandler);
    //     this.setState({
    //       charttokens: {
    //         ...this.state.charttokens,
    //         [name]: charttoken,
    //       }
    //     })
    //   }
    // } else if (type === 'map') {      
    //   if (!this.state.maptoken) {
    //     let maptoken = PubSub.subscribe('map:data:' + name, this.mapDataHandler);
    //     this.setState({
    //       maptoken,
    //     })
    //   }
    // }

    // if (!this.state.maptoken) {
    //   let maptoken = PubSub.subscribe('map:data:' + name, this.mapDataHandler);
    //   this.setState({
    //     maptoken,
    //   })
    // }
    let poslast = this.state.items.length;
    // [{"i":"new:0","name":"SB_0001_sensor_temp","type":"chart","x":null,"y":null,"w":4,"h":2}].
    let posx = (poslast * lebar) % total;
    let new_item = {
      i: "new:" + poslast,
      name,
      type, // 'map'
      // x: Infinity,
      // yellow,
      // red,
      x: posx,
      y: Infinity,
      w: lebar,
      h: tinggi,
    };

    // this.setState({
    //   map_ids: this.state.map_ids.concat(map_id)
    // });
    this.setState({
      items: this.state.items.concat(new_item),
      map_ids: this.state.map_ids.concat(name),
    });

  }

  mapDataHandler = (topic, data) => {
    console.log(`new data/latlong map ${topic}: ${data}.`);
    let map_id = topic.split(':')[2];
    // kita pindah ke lokasi data atau search lokasi data
    // data = { command: search/goto/zoomto/reset, payload: ...}
  }

  onRemoveItem = (index) => {
    console.log("removing", index);
    let removeDom = this.state.items.filter(elem => elem.i === index);

    console.log(`hapus DOM: ${JSON.stringify(removeDom)}.`);

    if (removeDom.length === 1) {
      let item = removeDom[0];

      // console.log(`hapus ${item.name} dari ${Object.keys(this.chartElements)}.`);
      // delete this.chartElements[item.name];
      // console.log(`stlh hapus menjadi => ${Object.keys(this.chartElements)}.`);

      if (item.type === 'chart') { // sementara chart dulu, map menyusul
        // let older = this.state.viewsensor;
        // delete older[item.name];
        // this.setState({
        //   // viewsensor: older
        //   viewmap: this.state.viewsensor.filter(elem => elem.name !== item.name)
        // });
      }
      else if (item.type === 'map') {
        // let older = this.state.viewmap;
        // delete older[item.name];
        // this.setState({
        //   viewmap: older
        // });
        this.setState({
          viewmap: this.state.viewmap.filter(elem => elem.name !== item.name)
        });
      }
    }

    this.setState({
        items: this.state.items.filter(elem => elem.i !== index),
     });
  }

  addMap = () => {
    // let map_id = `${bangunan.name}-${bangunan.id}-${bangunan.location}`;
    // if (!this.state.viewmap.hasOwnProperty(map_id)) {
    //   PubSub.publish(NEW_MAP, {name: map_id});
    // }
    let map_id = this.state.items.length + 1;
    PubSub.publish(NEW_MAP, {name: map_id});
  }

  render() {

    const { lalo } = this.props;

    return (<>

      <Row gutter={[8, 16]}>
        <Col span='8'>
          <Button 
          type="primary"
          onClick={this.addMap}>Add Map</Button>
        </Col>
        {/* <Col span='8'>
          <HighchartsReact highcharts={Highcharts} options={options} />
        </Col>
        <Col span='8'>
          <HighchartsReact highcharts={Highcharts} options={options} />
        </Col> */}
      </Row>

      {/* <Row gutter={[8, 16]}>
        <Col span='8'>
        </Col>
      </Row> */}

      <Row gutter={[8, 16]}>
        <Col span='24'>
          <ResponsiveReactGridLayout
            className="layout"
            breakpoints={{lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0}}
            cols={{ lg: 12, md: 10, sm: 6, xs: 4, xxs: 2 }}
            rowHeight={tinggi_baris || 250}
            >

            {this.state.items.map((elem,idx) => {
              // return <h1 key={idx}>{elem.name}</h1>

              // // const fullscreen = useFullScreenHandle();
              // const fullscreen = undefined;
              // // const new_reference = React.createRef();
              // // global_references[elem.name] = React.useRef(new_reference);
              // // console.log(`******** refs: ${JSON.stringify(global_references)}.`);
              const ItemComponent = <div key={elem.i} data-grid={elem} style={{background: 'rgb(156, 243, 135)', border: '1px blue solid'}}>
                <Card>
                  <ActionComponent
                    go_fullscreen={this.goFullScreen}
                    name={elem.name}
                    title='Action'
                    RemoveComponent={<RemoveComponent remove={() => this.onRemoveItem(elem.i)}/>}/>

                  <FullScreen
                    enabled={this.state.is_fullscreen}
                    onChange={isFull => this.setState({ is_fullscreen: isFull })}
                  >
                    <h1>Please deh muncul...</h1>
                    <div style={{height:this.state.is_fullscreen?`100%`:`200px`}}>
                  <MapItem
                    capital={lalo}
                    elem={elem}                    
                    config={{
                      basemaps: {
                        'OpenStreetMap_Mapnik': default_layer,
                      },
                      center: lalo,
                      // fullscreen_handle: fullscreen,
                      tilelayers: default_layer,
                      zoom: 4,
                    }} />
                    </div>
                    <h1>Juga dari bawah...</h1>
                  </FullScreen>


                </Card>
              </div>;

              // // if (! this.state.controls.hasOwnProperty(elem.name)) {
              // //   // komponen baru blm ada di grid
              // //   // no state change in render!
              // //   // this.setState({
              // //   //   controls: {
              // //   //     ...this.state.controls,
              // //   //     [elem.name]: ItemComponent,
              // //   //   }
              // //   // });
              // //   return ItemComponent;
              // // } else {
              // //   // komponen sudah ditambahkan, sudah ada di grid
              // //   return this.state.controls[elem.name];
              // // }

              return ItemComponent;

            })}

          </ResponsiveReactGridLayout>
        </Col>
      </Row>

    </>);
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/MapItem.css
.leaflet-container {
  width: 100%;
  height: 100%;
}
--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/MapItem.js
import React, { 
  // Component, PureComponent,
  useCallback,
  useEffect,
  useMemo,
  useState,
} from "react";
import './MapItem.css';
import { 
  MapContainer, TileLayer, Marker, Popup,
  // useEventHandlers,
  useMapEvent,
  useMapEvents,
  useMap,
  Rectangle,
} from 'react-leaflet';
import { useEventHandlers } from '@react-leaflet/core'
// import Search from "react-leaflet-search";

// Classes used by Leaflet to position controls
const POSITION_CLASSES = {
  bottomleft: 'leaflet-bottom leaflet-left',
  bottomright: 'leaflet-bottom leaflet-right',
  topleft: 'leaflet-top leaflet-left',
  topright: 'leaflet-top leaflet-right',
}

const BOUNDS_STYLE = { weight: 1 }

function MinimapBounds({ parentMap, zoom }) {
  const minimap = useMap()

  // Clicking a point on the minimap sets the parent's map center
  const onClick = useCallback(
    (e) => {
      parentMap.setView(e.latlng, parentMap.getZoom())
    },
    [parentMap],
  )
  useMapEvent('click', onClick)

  // Keep track of bounds in state to trigger renders
  const [bounds, setBounds] = useState(parentMap.getBounds())
  const onChange = useCallback(() => {
    setBounds(parentMap.getBounds())
    // Update the minimap's view to match the parent map's center and zoom
    minimap.setView(parentMap.getCenter(), zoom)
  }, [minimap, parentMap, zoom])

  // Listen to events on the parent map
  const handlers = useMemo(() => ({ move: onChange, zoom: onChange }), [])
  useEventHandlers({ instance: parentMap }, handlers)

  return <Rectangle bounds={bounds} pathOptions={BOUNDS_STYLE} />
}

function MinimapControl({ position, zoom }) {
  const parentMap = useMap()
  const mapZoom = zoom || 0

  // Memoize the minimap so it's not affected by position changes
  const minimap = useMemo(
    () => (
      <MapContainer
        style={{ height: 80, width: 80 }}
        center={parentMap.getCenter()}
        zoom={mapZoom}
        dragging={false}
        doubleClickZoom={false}
        scrollWheelZoom={false}
        attributionControl={false}
        zoomControl={false}>
        <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
        <MinimapBounds parentMap={parentMap} zoom={mapZoom} />
      </MapContainer>
    ),
    [],
  )

  const positionClass =
    (position && POSITION_CLASSES[position]) || POSITION_CLASSES.topright
  return (
    <div className={positionClass}>
      <div className="leaflet-control leaflet-bar">{minimap}</div>
    </div>
  )
}

// https://react-leaflet.js.org/docs/example-events/

function LocationMarker() {
  const [position, setPosition] = useState(null)
  const map = useMapEvents({
    click() {
      map.locate()
    },
    locationfound(e) {
      setPosition(e.latlng)
      map.flyTo(e.latlng, map.getZoom())
    },
  })

  return position === null ? null : (
    <Marker position={position}>
      <Popup>You are here</Popup>
    </Marker>
  )
}

// https://stackoverflow.com/questions/67114692/how-to-set-view-of-map-for-new-location-using-latitute-and-longitude-with-react
// https://pastebin.com/d2h8hUr9
function ChangeView({ center, zoom }) {
  const map = useMap();
  map.setView(center, zoom);
  return null;
}

const MapItem = ({capital, elem, config}) => {

  function customPopup(SearchInfo) {
    return (
      <Popup>
        <div>
          <p>I am a custom popUp</p>
          <p>
            latitude and longitude from search component:{" "}
            {SearchInfo.latLng.toString().replace(",", " , ")}
          </p>
          <p>Info from search component: {SearchInfo.info}</p>
          <p>
            {SearchInfo.raw &&
              SearchInfo.raw.place_id &&
              JSON.stringify(SearchInfo.raw.place_id)}
          </p>
        </div>
      </Popup>
    );
  }

  const [map, setMap] = useState(null);

  useEffect(()=>{
    if (map !== null) {
      console.log(`MapItem heading to: ${capital}`);
      map.setView(capital, config.zoom);
    }
  }, [capital]);

  return (<MapContainer 
    // center={config.center}
    center={capital}
    zoom={config.zoom} 
    scrollWheelZoom={true}>
    <TileLayer
      attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
    />
    <ChangeView center={capital} zoom={config.zoom} /> 
    <MinimapControl position="topright" />
    <LocationMarker />
  </MapContainer>);

  // const displayMap = useMemo(
  //   () =>  (<MapContainer 
  //   // center={config.center}
  //   center={capital}
  //   zoom={config.zoom} 
  //   scrollWheelZoom={true}>
  //   <TileLayer
  //     attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  //     url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
  //   />
  //   <MinimapControl position="topright" />
  //   <LocationMarker />
  // </MapContainer>),
  // [capital]);

  // return (
  //   <>
  //     {/* {map ? <DisplayPosition map={map} /> : null} */}
  //     {displayMap}
  //   </>
  // );
}

export default MapItem;

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/old-index.js
import React from "react";
import {
  Button,
	Card,
	Col,
  DatePicker,
  Divider,
  Drawer,
  Input, InputNumber ,
  Modal,
  Popover,
	Row,
  Select,
  Space,
	Statistic,
	Table,
} from 'antd';
import { WidthProvider, Responsive } from "react-grid-layout";
import MapItem from './MapItem';
const ResponsiveReactGridLayout = WidthProvider(Responsive);

const tinggi_baris = 225;
const total = 10;
const lebar = 5;
const tinggi = 2;

// const jumlah_datapoint = 10;
// const NEW_CHART = '<<new chart>>';

const NEW_MAP = '<<new map>>';
const default_layer = {
  'tile': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
  'attrib': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  'name': 'OpenStreetMap_Mapnik',
}

function ActionComponent(props) {
  return <Card title={props.title} extra={props.RemoveComponent} style={{ width: 300 }}>
  </Card>
}

function RemoveComponent(props) {
  const removeStyle = {
    width: '10px',
    position: "absolute",
    right: "2px",
    top: 0,
    cursor: "pointer"
  };

  return <span
    className="remove"
    style={removeStyle}
    onClick={props.remove}
    >
    x
  </span>
}

export default class GridMap extends React.Component {

  state = {
    items: ['pertama'].map(function(item, key, list) {
      let per_kolom = (total/lebar);
      let posx = (key * lebar) % total;
      let posy = ~~(key / per_kolom);
      console.log(key, item, per_kolom, posx, posy);
      return {
        i: key.toString(),
        x: posx,
        y: item === (list.length - 1) ? Infinity : posy,
        w: lebar,
        h: tinggi,
        // index: key,
        name: item,
        add: item === (list.length - 1),
        resizeHandles: ["sw", "se"],
      };
    }),
    // controls: {},

    maptoken: null,
    // charttokens: {},
    // building_data: [],
    // viewsensor: {},
    // configsensor: {},
    // viewmap: {},
    viewmap: [],
    map_ids: [],

  }

  constructor(props) {
    super(props);
    // this.chartElements = {};
  }

  componentDidMount() {
    PubSub.subscribe(NEW_MAP, this.new_map);
  }

  // new_chart = (topic, data) => {
  //   this.onAddItem('chart', data);
  // }

  new_map = (topic, data) => {
    this.onAddItem('map', data);
  }

  onAddItem = (type, {name}) => {
    // if (type === 'chart') {
    //   if (!this.state.charttokens.hasOwnProperty(name)) {
    //     let charttoken = PubSub.subscribe('sensor:data:' + name, this.sensorDataHandler);
    //     this.setState({
    //       charttokens: {
    //         ...this.state.charttokens,
    //         [name]: charttoken,
    //       }
    //     })
    //   }
    // } else if (type === 'map') {      
    //   if (!this.state.maptoken) {
    //     let maptoken = PubSub.subscribe('map:data:' + name, this.mapDataHandler);
    //     this.setState({
    //       maptoken,
    //     })
    //   }
    // }

    // if (!this.state.maptoken) {
    //   let maptoken = PubSub.subscribe('map:data:' + name, this.mapDataHandler);
    //   this.setState({
    //     maptoken,
    //   })
    // }
    let poslast = this.state.items.length;
    // [{"i":"new:0","name":"SB_0001_sensor_temp","type":"chart","x":null,"y":null,"w":4,"h":2}].
    let posx = (poslast * lebar) % total;
    let new_item = {
      i: "new:" + poslast,
      name,
      type, // 'map'
      // x: Infinity,
      // yellow,
      // red,
      x: posx,
      y: Infinity,
      w: lebar,
      h: tinggi,
    };

    // this.setState({
    //   map_ids: this.state.map_ids.concat(map_id)
    // });
    this.setState({
      items: this.state.items.concat(new_item),
      map_ids: this.state.map_ids.concat(name),
    });

  }

  mapDataHandler = (topic, data) => {
    console.log(`new data/latlong map ${topic}: ${data}.`);
    let map_id = topic.split(':')[2];
    // kita pindah ke lokasi data atau search lokasi data
    // data = { command: search/goto/zoomto/reset, payload: ...}
  }

  onRemoveItem = (index) => {
    console.log("removing", index);
    let removeDom = this.state.items.filter(elem => elem.i === index);

    console.log(`hapus DOM: ${JSON.stringify(removeDom)}.`);

    if (removeDom.length === 1) {
      let item = removeDom[0];

      // console.log(`hapus ${item.name} dari ${Object.keys(this.chartElements)}.`);
      // delete this.chartElements[item.name];
      // console.log(`stlh hapus menjadi => ${Object.keys(this.chartElements)}.`);

      if (item.type === 'chart') { // sementara chart dulu, map menyusul
        // let older = this.state.viewsensor;
        // delete older[item.name];
        // this.setState({
        //   // viewsensor: older
        //   viewmap: this.state.viewsensor.filter(elem => elem.name !== item.name)
        // });
      }
      else if (item.type === 'map') {
        // let older = this.state.viewmap;
        // delete older[item.name];
        // this.setState({
        //   viewmap: older
        // });
        this.setState({
          viewmap: this.state.viewmap.filter(elem => elem.name !== item.name)
        });
      }
    }

    this.setState({
        items: this.state.items.filter(elem => elem.i !== index),
     });
  }

  addMap = () => {
    // let map_id = `${bangunan.name}-${bangunan.id}-${bangunan.location}`;
    // if (!this.state.viewmap.hasOwnProperty(map_id)) {
    //   PubSub.publish(NEW_MAP, {name: map_id});
    // }
    let map_id = this.state.items.length + 1;
    PubSub.publish(NEW_MAP, {name: map_id});
  }

  render() {
    return (<>

      <Row gutter={[8, 16]}>
        <Col span='8'>
          <Button 
          type="primary"
          onClick={this.addMap}>Add Map</Button>
        </Col>
        {/* <Col span='8'>
          <HighchartsReact highcharts={Highcharts} options={options} />
        </Col>
        <Col span='8'>
          <HighchartsReact highcharts={Highcharts} options={options} />
        </Col> */}
      </Row>

      {/* <Row gutter={[8, 16]}>
        <Col span='8'>
        </Col>
      </Row> */}

      <Row gutter={[8, 16]}>
        <Col span='24'>
          <ResponsiveReactGridLayout
            className="layout"
            breakpoints={{lg: 1200, md: 996, sm: 768, xs: 480, xxs: 0}}
            cols={{ lg: 12, md: 10, sm: 6, xs: 4, xxs: 2 }}
            rowHeight={tinggi_baris || 250}
            >

            {this.state.items.map((elem,idx) => {
              return <h1 key={idx}>{elem.name}</h1>

              // // const fullscreen = useFullScreenHandle();
              // const fullscreen = undefined;
              // // const new_reference = React.createRef();
              // // global_references[elem.name] = React.useRef(new_reference);
              // // console.log(`******** refs: ${JSON.stringify(global_references)}.`);
              // const ItemComponent = <div key={elem.i} data-grid={elem} style={{border: '1px red solid'}}>
              //   <Card>
              //     <ActionComponent
              //       fullscreen={fullscreen}
              //       name={elem.name}
              //       title='judul card action'
              //       RemoveComponent={<RemoveComponent remove={() => this.onRemoveItem(elem.i)}/>}/>

              //     <MapItem
              //       elem={elem}
              //       config={{
              //         basemaps: {
              //           'OpenStreetMap_Mapnik': default_layer,
              //         },
              //         center: [-0.2900057071240255, 100.62515258789062],
              //         fullscreen_handle: fullscreen,
              //         tilelayers: default_layer,
              //         zoom: 12,
              //       }} />
              //   </Card>
              // </div>;

              // // if (! this.state.controls.hasOwnProperty(elem.name)) {
              // //   // komponen baru blm ada di grid
              // //   // no state change in render!
              // //   // this.setState({
              // //   //   controls: {
              // //   //     ...this.state.controls,
              // //   //     [elem.name]: ItemComponent,
              // //   //   }
              // //   // });
              // //   return ItemComponent;
              // // } else {
              // //   // komponen sudah ditambahkan, sudah ada di grid
              // //   return this.state.controls[elem.name];
              // // }

              // return ItemComponent;

            })}

          </ResponsiveReactGridLayout>
        </Col>
      </Row>

    </>);
  }
}

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/old-MapItem.js
import React, { 
  // Component, PureComponent, 
  useEffect, useState 
} from "react";
// import { FullScreen, useFullScreenHandle } from "react-full-screen";

import L from 'leaflet';
import 'leaflet-search';
import 'leaflet.locatecontrol';
import 'leaflet-search/dist/leaflet-search.min.css'
import 'leaflet.locatecontrol/dist/L.Control.Locate.min.css'

import './fs/leaflet.fullscreen.css'
import './fs/Leaflet.fullscreen'

// import Highcharts from "highcharts";
// import HighchartsReact from "highcharts-react-official";
// const ReactHighcharts = require('react-highcharts');

export default function MapItem({ elem, config, }) {

  // const screen1 = useFullScreenHandle();
  // const zoom = 12;
  // const center = [-0.2900057071240255, 100.62515258789062];
  // let tilelayers = [];
  // let basemaps = {};

  useEffect( () => {

    console.log(`MapItem
    config: ${JSON.stringify(config, null, 2)}.
    dan elem: ${JSON.stringify(elem)}.
    `);
    
    const default_layer = L.tileLayer(config.tilelayers.tile, { 
        id: config.tilelayers.name,
        attribution: config.tilelayers.attrib ,
      }
    );
    let main_map = L.map(elem.name, {
      center: [config.center],
      zoom: config.zoom,
      layers: [default_layer],
    });
    
    let markerlayer = L.layerGroup();
    markerlayer.addTo(main_map);  
    
    let controllayer = L.control.layers({
      [config.tilelayers.name]: default_layer
    });
    controllayer.addTo(main_map);
    main_map.addControl(new L.Control.Fullscreen());

    // main_map.addControl( new L.Control.Search({
    //   url: 'https://nominatim.openstreetmap.org/search?format=json&q={s}',
    //   jsonpParam: 'json_callback',
    //   propertyName: 'display_name',
    //   propertyLoc: ['lat','lon'],
    //   marker: L.circleMarker([0,0], {radius:30}),
    //   autoCollapse: true,
    //   autoType: false,
    //   minLength: 2,

    //   moveToLocation: function(latlng, title, map) {
    //     // main_map.flyTo(latlng.lat, latlng.lng);
    //     console.log(`search control, apakah params null?
        
    //     latlng    = ${latlng}
    //     title     = ${title}
    //     map       = ${map}
        
    //     `);

    //     var zoom = map.getBoundsZoom(latlng.layer.getBounds());
    //     map.setView(latlng, zoom); // access the zoom
        
    //     //https://wiki.openstreetmap.org/wiki/Shortlink
    //     // var url = L.Util.template('http://osm.org/?mlat={lat}&amp;mlon={lon}#map={zoom}/{lat}/{lon}', {
    //     //   lat: latlng.lat,
    //     //   lon: latlng.lng,
    //     //   zoom: map.getZoom()
    //     // });
  
    //     // location.href = url;
    //   }

    // }) );

    main_map.addControl(L.control.locate({
      strings: {
          title: 'Tunjukkan lokasi saya'
      },
      locateOptions: {
          enableHighAccuracy: true
      }
    }));

    main_map.on('locationfound', function (e) {
      var radius = e.accuracy / 2;
      let center = e.latlng; // => flyTo...
      main_map.flyTo(center);
      console.log(`Akurasi ${radius / 1000} m.`);
      L.circle(e.latlng, radius).addTo(main_map);
    });
    
    main_map.locate({
      enableHighAccuracy: true,
      setView: true, 
      // watch: true, 
      maxZoom: config.zoom
    });

  }, [] )

  // return (<FullScreen handle={config.fullscreen_handle}>
  //   <div style={{width: '100%', minHeight: '200px',}} id={elem.name} />
  // </FullScreen>);
  return (
    <div style={{width: '100%', minHeight: '300px',}} id={elem.name} />
  );
}

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/working-index.js
import React from "react";
import _ from "lodash";
import RGL, { WidthProvider } from "react-grid-layout";
import 'react-grid-layout/css/styles.css';

const ReactGridLayout = WidthProvider(RGL);

/**
 * This layout demonstrates how to use the `onResize` handler to enforce a min/max width and height.
 *
 * In this grid, all elements are allowed a max width of 2 if the height < 3,
 * and a min width of 2 if the height >= 3.
 */
export default class GridMap extends React.PureComponent {
  static defaultProps = {
    isDraggable: true,
    isResizable: true,
    items: 20,
    rowHeight: 30,
    onLayoutChange: function() {},
    cols: 12
  };

  generateDOM() {
    // Generate items with properties from the layout, rather than pass the layout directly
    const layout = this.generateLayout();
    return _.map(layout, function(l) {
      return (
        <div key={l.i} data-grid={l} style={{ background: 'rgb(156, 243, 135)', border: '1px solid blue' }}>
          <span className="text">{l.i}</span>
        </div>
      );
    });
  }

  generateLayout() {
    const p = this.props;
    return _.map(new Array(p.items), function(item, i) {
      const w = _.random(1, 2);
      const h = _.random(1, 3);
      return {
        x: (i * 2) % 12,
        y: Math.floor(i / 6),
        w: w,
        h: h,
        i: i.toString()
      };
    });
  }

  onLayoutChange(layout) {
    this.props.onLayoutChange(layout);
  }

  onResize(layout, oldLayoutItem, layoutItem, placeholder) {
    // `oldLayoutItem` contains the state of the item before the resize.
    // You can modify `layoutItem` to enforce constraints.

    if (layoutItem.h < 3 && layoutItem.w > 2) {
      layoutItem.w = 2;
      placeholder.w = 2;
    }

    if (layoutItem.h >= 3 && layoutItem.w < 2) {
      layoutItem.w = 2;
      placeholder.w = 2;
    }
  }

  render() {
    return (
      <ReactGridLayout
        onLayoutChange={this.onLayoutChange}
        onResize={this.onResize}
        {...this.props}
      >
        {this.generateDOM()}
      </ReactGridLayout>
    );
  }
}

// if (process.env.STATIC_EXAMPLES === true) {
//   import("../test-hook.jsx").then(fn => fn.default(DynamicMinMaxLayout));
// }

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/fs/fullscreen.png
iVBORw0KGgoAAAANSUhEUgAAABoAAAA0CAYAAACU7CiIAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAACoSURBVFiF7ZZhDoAgCIWxdbF3suxkHM3+1FaOmNqyIr6fiHuJTyKklKgHQxcVF7rCKAUBiA5h5tCSR/T0iTakL9PWz05IZNEM3YSCt6BvCgFI2ps4Q9v3k9Ldgdrr8nrX9LYc7wwu5EIu9KCQT6rq+r8mVbV0ewBEIpqy8MzMsWR/8f+oxmES9u7olZPqLKQeYtqkWuy61V2xND/H3h35pNqMPTPYE1oAnZZStKN8jj8AAAAASUVORK5CYII=
--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/fs/fullscreen@2x.png
iVBORw0KGgoAAAANSUhEUgAAADQAAABoCAYAAAC+NNNnAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAbrwAAG68BXhqRHAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAEhSURBVHic7dpBDoIwFADRj/FiPRlwsh4NN5CoiVKg1Ukzb43ApKK1dliWJXpy+/cN1GYQnUF0BtEZRHcvPTCldGhKkXMefnm+TXcjZBBd8TP0rvQ9ffb1R5+xTXcjZBCdQXQG0Q2u+sAZRGcQnUF0p9cUrv4eanW97kbIIDqD6AyiO70ut7du1mrdbU93I2QQnWsKdAbRGURnEJ1BdAbRGURnEJ1BdAbRueeUziA695zSGURnEN3pT7lvUkpTRIw7h80556n2tauPUGFMRMS4HltV9f+HWs3RSnX3DBlEZxCdQXQt9pzOUfbFuh179Xovqo/QOp35eKNPmkx9mszl1hudWpx7T3fPkEF0BtG555TOIDr3nNIZRGcQnUF0BtE9AF5WX48h7QeZAAAAAElFTkSuQmCC
--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/fs/leaflet.fullscreen.css
.leaflet-control-fullscreen a {
  background:#fff url(fullscreen.png) no-repeat 0 0;
  background-size:26px 52px;
  }
  .leaflet-touch .leaflet-control-fullscreen a {
    background-position: 2px 2px;
    }
  .leaflet-fullscreen-on .leaflet-control-fullscreen a {
    background-position:0 -26px;
    }
  .leaflet-touch.leaflet-fullscreen-on .leaflet-control-fullscreen a {
    background-position: 2px -24px;
    }

/* Do not combine these two rules; IE will break. */
.leaflet-container:-webkit-full-screen {
  width:100%!important;
  height:100%!important;
  }
.leaflet-container.leaflet-fullscreen-on {
  width:100%!important;
  height:100%!important;
  }

.leaflet-pseudo-fullscreen {
  position:fixed!important;
  width:100%!important;
  height:100%!important;
  top:0!important;
  left:0!important;
  z-index:99999;
  }

@media
  (-webkit-min-device-pixel-ratio:2),
  (min-resolution:192dpi) {
    .leaflet-control-fullscreen a {
      background-image:url(fullscreen@2x.png);
    }
  }

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/GridMap/fs/Leaflet.fullscreen.js
(function (factory) {
    // if (typeof define === 'function' && define.amd) {
    //     // AMD
    //     define(['leaflet'], factory);
    // } else 
    if (typeof module !== 'undefined') {
        // Node/CommonJS
        module.exports = factory(require('leaflet'));
    } else {
        // Browser globals
        if (typeof window.L === 'undefined') {
            throw new Error('Leaflet must be loaded first');
        }
        factory(window.L);
    }
}(function (L) {
    L.Control.Fullscreen = L.Control.extend({
        options: {
            position: 'topleft',
            title: {
                'false': 'View Fullscreen',
                'true': 'Exit Fullscreen'
            }
        },

        onAdd: function (map) {
            var container = L.DomUtil.create('div', 'leaflet-control-fullscreen leaflet-bar leaflet-control');

            this.link = L.DomUtil.create('a', 'leaflet-control-fullscreen-button leaflet-bar-part', container);
            this.link.href = '#';

            this._map = map;
            this._map.on('fullscreenchange', this._toggleTitle, this);
            this._toggleTitle();

            L.DomEvent.on(this.link, 'click', this._click, this);

            return container;
        },

        _click: function (e) {
            L.DomEvent.stopPropagation(e);
            L.DomEvent.preventDefault(e);
            this._map.toggleFullscreen(this.options);
        },

        _toggleTitle: function() {
            this.link.title = this.options.title[this._map.isFullscreen()];
        }
    });

    L.Map.include({
        isFullscreen: function () {
            return this._isFullscreen || false;
        },

        toggleFullscreen: function (options) {
            var container = this.getContainer();
            if (this.isFullscreen()) {
                if (options && options.pseudoFullscreen) {
                    this._disablePseudoFullscreen(container);
                } else if (document.exitFullscreen) {
                    document.exitFullscreen();
                } else if (document.mozCancelFullScreen) {
                    document.mozCancelFullScreen();
                } else if (document.webkitCancelFullScreen) {
                    document.webkitCancelFullScreen();
                } else if (document.msExitFullscreen) {
                    document.msExitFullscreen();
                } else {
                    this._disablePseudoFullscreen(container);
                }
            } else {
                if (options && options.pseudoFullscreen) {
                    this._enablePseudoFullscreen(container);
                } else if (container.requestFullscreen) {
                    container.requestFullscreen();
                } else if (container.mozRequestFullScreen) {
                    container.mozRequestFullScreen();
                } else if (container.webkitRequestFullscreen) {
                    container.webkitRequestFullscreen(Element.ALLOW_KEYBOARD_INPUT);
                } else if (container.msRequestFullscreen) {
                    container.msRequestFullscreen();
                } else {
                    this._enablePseudoFullscreen(container);
                }
            }

        },

        _enablePseudoFullscreen: function (container) {
            L.DomUtil.addClass(container, 'leaflet-pseudo-fullscreen');
            this._setFullscreen(true);
            this.fire('fullscreenchange');
        },

        _disablePseudoFullscreen: function (container) {
            L.DomUtil.removeClass(container, 'leaflet-pseudo-fullscreen');
            this._setFullscreen(false);
            this.fire('fullscreenchange');
        },

        _setFullscreen: function(fullscreen) {
            this._isFullscreen = fullscreen;
            var container = this.getContainer();
            if (fullscreen) {
                L.DomUtil.addClass(container, 'leaflet-fullscreen-on');
            } else {
                L.DomUtil.removeClass(container, 'leaflet-fullscreen-on');
            }
            this.invalidateSize();
        },

        _onFullscreenChange: function (e) {
            var fullscreenElement =
                document.fullscreenElement ||
                document.mozFullScreenElement ||
                document.webkitFullscreenElement ||
                document.msFullscreenElement;

            if (fullscreenElement === this.getContainer() && !this._isFullscreen) {
                this._setFullscreen(true);
                this.fire('fullscreenchange');
            } else if (fullscreenElement !== this.getContainer() && this._isFullscreen) {
                this._setFullscreen(false);
                this.fire('fullscreenchange');
            }
        }
    });

    L.Map.mergeOptions({
        fullscreenControl: false
    });

    L.Map.addInitHook(function () {
        if (this.options.fullscreenControl) {
            this.fullscreenControl = new L.Control.Fullscreen(this.options.fullscreenControl);
            this.addControl(this.fullscreenControl);
        }

        var fullscreenchange;

        if ('onfullscreenchange' in document) {
            fullscreenchange = 'fullscreenchange';
        } else if ('onmozfullscreenchange' in document) {
            fullscreenchange = 'mozfullscreenchange';
        } else if ('onwebkitfullscreenchange' in document) {
            fullscreenchange = 'webkitfullscreenchange';
        } else if ('onmsfullscreenchange' in document) {
            fullscreenchange = 'MSFullscreenChange';
        }

        if (fullscreenchange) {
            var onFullscreenChange = L.bind(this._onFullscreenChange, this);

            this.whenReady(function () {
                L.DomEvent.on(document, fullscreenchange, onFullscreenChange);
            });

            this.on('unload', function () {
                L.DomEvent.off(document, fullscreenchange, onFullscreenChange);
            });
        }
    });

    L.control.fullscreen = function (options) {
        return new L.Control.Fullscreen(options);
    };
}));
--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/graph-types.js
export default [
  {
    label: "Line",
    value: "line"
  },
  {
    label: "Pie",
    value: "pie"
  },
  {
    label: "Area",
    value: "area"
  },
  {
    label: "Bar",
    value: "bar"
  }
];

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/GraphBlock.js
import React from "react";
// import PropTypes from "prop-types";
import {
  LineChart,
  Line,
  BarChart,
  Bar,
  AreaChart,
  Area,
  PieChart,
  Pie,
  CartesianGrid,
  XAxis,
  YAxis
} from "recharts";

const GraphBlock = ({ type, data, width=200, height=100 }) => {
  switch (type) {
    case "pie":
      return (
        <PieChart width={width} height={height}>
          <Pie
            data={data}
            dataKey="value"
            nameKey="time"
            cx="50%"
            cy="50%"
            outerRadius={100}
            fill="#82ca9d"
            isAnimationActive={false}
          />
        </PieChart>
      );
    case "line":
      return (
        <LineChart
          width={width}
          height={height}
          data={data}
          margin={{ left: 10, right: 10 }}
        >
          <CartesianGrid strokeDasharray="3 3" strokeOpacity={0.1} />
          <XAxis dataKey="time" />
          <YAxis dataKey="value" mirror />
          <Line
            type="monotone"
            dataKey="value"
            stroke="#82ca9d"
            dot={false}
            isAnimationActive={false}
          />
        </LineChart>
      );
    case "bar":
      return (
        <BarChart
          width={width}
          height={height}
          data={data}
          margin={{ left: 10, right: 10 }}
        >
          <CartesianGrid strokeDasharray="3 3" strokeOpacity={0.1} />
          <XAxis dataKey="time" />
          <YAxis dataKey="value" mirror />
          <Bar dataKey="value" fill="#82ca9d" isAnimationActive={false} />
        </BarChart>
      );
    case "area":
      return (
        <AreaChart
          width={width}
          height={height}
          data={data}
          margin={{ left: 10, right: 10 }}
        >
          <CartesianGrid strokeDasharray="3 3" strokeOpacity={0.1} />
          <XAxis dataKey="time" />
          <YAxis dataKey="value" mirror />
          <Area
            dataKey="value"
            fill="#82ca9d"
            stroke="#82ca9d"
            isAnimationActive={false}
          />
        </AreaChart>
      );
    default:
      return null;
  }
};

// GraphBlock.propTypes = {
//   type: PropTypes.string.isRequired,
//   data: PropTypes.array.isRequired,
//   width: PropTypes.number.isRequired,
//   height: PropTypes.number.isRequired
// };

export default GraphBlock;

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/GridDashboard.js
import React from "react";
import GraphBlock from "./GraphBlock";
import layout_config from './layoutConfig';
// import "./styles.css";

import { Responsive, WidthProvider } from "react-grid-layout";
const ResponsiveGridLayout = WidthProvider(Responsive);

const grid_data = [
  {
    type: "line",
    title: "Graph 1",
    data: [
      {
        time: "5:08 AM",
        value: 3738
      },
      {
        time: "4:52 PM",
        value: 2135
      },
      {
        time: "4:04 AM",
        value: 2649
      },
      {
        time: "10:17 AM",
        value: 560
      },
      {
        time: "11:39 AM",
        value: 3942
      },
      {
        time: "1:41 PM",
        value: 3421
      },
      {
        time: "6:39 AM",
        value: 2634
      },
      {
        time: "5:08 PM",
        value: 2298
      },
      {
        time: "2:46 AM",
        value: 2231
      },
      {
        time: "10:56 PM",
        value: 921
      },
      {
        time: "3:48 AM",
        value: 4047
      },
      {
        time: "4:30 AM",
        value: 4186
      },
      {
        time: "10:44 PM",
        value: 4350
      },
      {
        time: "12:41 AM",
        value: 3057
      },
      {
        time: "7:16 PM",
        value: 524
      },
      {
        time: "9:47 AM",
        value: 2924
      },
      {
        time: "5:43 PM",
        value: 173
      },
      {
        time: "12:13 AM",
        value: 1244
      },
      {
        time: "2:07 AM",
        value: 631
      },
      {
        time: "7:37 AM",
        value: 2216
      },
      {
        time: "10:00 AM",
        value: 3112
      },
      {
        time: "11:21 PM",
        value: 4318
      },
      {
        time: "10:38 PM",
        value: 1788
      },
      {
        time: "2:36 PM",
        value: 4382
      },
      {
        time: "1:48 AM",
        value: 142
      },
      {
        time: "8:12 AM",
        value: 423
      },
      {
        time: "6:01 AM",
        value: 260
      },
      {
        time: "9:05 AM",
        value: 1327
      },
      {
        time: "1:41 AM",
        value: 1347
      },
      {
        time: "9:08 AM",
        value: 3983
      },
      {
        time: "12:31 AM",
        value: 960
      },
      {
        time: "2:59 PM",
        value: 4989
      },
      {
        time: "9:43 AM",
        value: 2974
      },
      {
        time: "7:46 PM",
        value: 1896
      },
      {
        time: "1:02 PM",
        value: 111
      },
      {
        time: "10:33 AM",
        value: 1868
      },
      {
        time: "12:37 PM",
        value: 4486
      },
      {
        time: "11:30 AM",
        value: 4383
      },
      {
        time: "8:01 AM",
        value: 924
      },
      {
        time: "12:17 PM",
        value: 1679
      },
      {
        time: "9:03 AM",
        value: 4815
      },
      {
        time: "7:20 AM",
        value: 1916
      },
      {
        time: "9:52 PM",
        value: 1173
      },
      {
        time: "10:34 AM",
        value: 146
      },
      {
        time: "1:13 PM",
        value: 3722
      },
      {
        time: "4:38 AM",
        value: 1912
      },
      {
        time: "3:55 AM",
        value: 4101
      },
      {
        time: "1:55 PM",
        value: 3782
      },
      {
        time: "4:59 PM",
        value: 3795
      }
    ]
  },
  {
    type: "bar",
    title: "Graph 2",
    data: [
      {
        time: "11:01 PM",
        value: 2584
      },
      {
        time: "5:27 AM",
        value: 4601
      },
      {
        time: "12:25 AM",
        value: 2051
      },
      {
        time: "9:44 AM",
        value: 4797
      },
      {
        time: "3:08 PM",
        value: 1731
      },
      {
        time: "3:35 PM",
        value: 2966
      },
      {
        time: "6:54 AM",
        value: 3129
      },
      {
        time: "6:22 AM",
        value: 3152
      },
      {
        time: "1:00 PM",
        value: 1912
      },
      {
        time: "4:45 PM",
        value: 4969
      },
      {
        time: "6:22 AM",
        value: 3150
      },
      {
        time: "8:47 AM",
        value: 1891
      },
      {
        time: "10:51 AM",
        value: 2708
      },
      {
        time: "1:10 AM",
        value: 324
      },
      {
        time: "12:20 AM",
        value: 2374
      },
      {
        time: "8:51 AM",
        value: 2265
      },
      {
        time: "6:52 PM",
        value: 3601
      },
      {
        time: "6:03 AM",
        value: 4022
      },
      {
        time: "11:15 AM",
        value: 4140
      },
      {
        time: "10:57 PM",
        value: 373
      },
      {
        time: "9:30 AM",
        value: 2498
      },
      {
        time: "11:22 AM",
        value: 403
      },
      {
        time: "6:21 PM",
        value: 2825
      },
      {
        time: "9:27 AM",
        value: 1549
      },
      {
        time: "11:05 PM",
        value: 2476
      },
      {
        time: "5:33 PM",
        value: 458
      },
      {
        time: "8:25 PM",
        value: 983
      },
      {
        time: "5:38 PM",
        value: 3597
      },
      {
        time: "10:42 PM",
        value: 2107
      }
    ]
  },
  {
    type: "pie",
    title: "Graph 3",
    data: [
      {
        time: "8:09 AM",
        value: 4408
      },
      {
        time: "10:28 AM",
        value: 3644
      },
      {
        time: "8:11 PM",
        value: 4861
      },
      {
        time: "1:26 AM",
        value: 2394
      },
      {
        time: "6:55 PM",
        value: 2937
      },
      {
        time: "11:21 PM",
        value: 4806
      },
      {
        time: "8:10 PM",
        value: 3688
      },
      {
        time: "4:07 AM",
        value: 3182
      },
      {
        time: "9:26 PM",
        value: 1281
      },
      {
        time: "11:44 AM",
        value: 2058
      },
      {
        time: "3:19 PM",
        value: 939
      },
      {
        time: "9:03 PM",
        value: 2193
      },
      {
        time: "8:07 AM",
        value: 3201
      },
      {
        time: "7:05 PM",
        value: 2679
      },
      {
        time: "3:32 PM",
        value: 4651
      },
      {
        time: "2:36 AM",
        value: 3895
      },
      {
        time: "1:52 AM",
        value: 3914
      },
      {
        time: "12:52 AM",
        value: 4085
      },
      {
        time: "10:04 AM",
        value: 264
      },
      {
        time: "5:23 AM",
        value: 4148
      },
      {
        time: "2:57 PM",
        value: 4821
      },
      {
        time: "11:53 PM",
        value: 1106
      },
      {
        time: "2:51 AM",
        value: 3802
      },
      {
        time: "5:58 AM",
        value: 3507
      },
      {
        time: "12:03 AM",
        value: 2362
      },
      {
        time: "7:44 AM",
        value: 2392
      },
      {
        time: "2:11 PM",
        value: 3857
      },
      {
        time: "5:05 AM",
        value: 4673
      },
      {
        time: "1:17 PM",
        value: 4782
      },
      {
        time: "9:49 PM",
        value: 1162
      },
      {
        time: "12:37 AM",
        value: 2622
      },
      {
        time: "1:37 PM",
        value: 2993
      }
    ]
  },
  {
    type: "area",
    title: "Graph 4",
    data: [
      {
        time: "8:54 PM",
        value: 1690
      },
      {
        time: "10:50 AM",
        value: 2876
      },
      {
        time: "2:22 AM",
        value: 2779
      },
      {
        time: "11:11 AM",
        value: 4147
      },
      {
        time: "5:23 PM",
        value: 3179
      },
      {
        time: "5:16 AM",
        value: 3543
      },
      {
        time: "2:02 PM",
        value: 1362
      },
      {
        time: "6:06 AM",
        value: 478
      },
      {
        time: "11:06 PM",
        value: 1243
      },
      {
        time: "4:53 PM",
        value: 464
      },
      {
        time: "5:50 PM",
        value: 3688
      },
      {
        time: "6:02 PM",
        value: 1044
      },
      {
        time: "1:00 AM",
        value: 1582
      },
      {
        time: "2:46 AM",
        value: 1990
      },
      {
        time: "2:42 PM",
        value: 4452
      },
      {
        time: "10:03 AM",
        value: 186
      },
      {
        time: "8:17 AM",
        value: 613
      },
      {
        time: "3:50 PM",
        value: 167
      },
      {
        time: "8:03 AM",
        value: 4581
      },
      {
        time: "8:09 PM",
        value: 3458
      }
    ]
  },
  {
    type: "bar",
    title: "Graph 5",
    data: [
      {
        time: "10:28 AM",
        value: 1285
      },
      {
        time: "4:22 PM",
        value: 3740
      },
      {
        time: "1:31 AM",
        value: 549
      },
      {
        time: "8:48 PM",
        value: 2432
      },
      {
        time: "10:45 PM",
        value: 1029
      },
      {
        time: "5:50 AM",
        value: 2045
      },
      {
        time: "9:10 AM",
        value: 3103
      },
      {
        time: "9:48 PM",
        value: 2594
      },
      {
        time: "2:12 AM",
        value: 2298
      },
      {
        time: "8:46 PM",
        value: 2043
      },
      {
        time: "9:45 PM",
        value: 4216
      },
      {
        time: "3:27 PM",
        value: 1404
      },
      {
        time: "9:08 AM",
        value: 3618
      },
      {
        time: "12:03 PM",
        value: 1938
      },
      {
        time: "4:28 AM",
        value: 1550
      },
      {
        time: "5:05 AM",
        value: 1355
      },
      {
        time: "11:51 AM",
        value: 4740
      },
      {
        time: "9:11 PM",
        value: 3457
      },
      {
        time: "6:18 AM",
        value: 2099
      }
    ]
  },
  {
    type: "pie",
    title: "Graph 6",
    data: [
      {
        time: "12:47 AM",
        value: 4135
      },
      {
        time: "1:29 PM",
        value: 2915
      },
      {
        time: "4:47 AM",
        value: 119
      },
      {
        time: "6:53 PM",
        value: 4718
      },
      {
        time: "1:18 AM",
        value: 2424
      },
      {
        time: "9:46 PM",
        value: 4146
      },
      {
        time: "12:37 AM",
        value: 2801
      },
      {
        time: "2:05 AM",
        value: 1881
      },
      {
        time: "2:48 PM",
        value: 3905
      },
      {
        time: "11:37 PM",
        value: 4349
      },
      {
        time: "1:00 AM",
        value: 1127
      },
      {
        time: "7:58 PM",
        value: 3288
      },
      {
        time: "6:58 AM",
        value: 1381
      },
      {
        time: "11:06 AM",
        value: 1147
      },
      {
        time: "4:41 PM",
        value: 2030
      },
      {
        time: "11:53 PM",
        value: 1381
      },
      {
        time: "2:50 AM",
        value: 3040
      },
      {
        time: "7:47 PM",
        value: 2740
      },
      {
        time: "9:12 AM",
        value: 1190
      },
      {
        time: "10:30 AM",
        value: 3834
      },
      {
        time: "4:39 AM",
        value: 2334
      }
    ]
  },
  {
    type: "line",
    title: "Graph 7",
    data: [
      {
        time: "2:52 PM",
        value: 2262
      },
      {
        time: "1:39 PM",
        value: 4843
      },
      {
        time: "11:19 PM",
        value: 4611
      },
      {
        time: "2:08 PM",
        value: 4345
      },
      {
        time: "3:41 PM",
        value: 831
      },
      {
        time: "5:17 PM",
        value: 301
      },
      {
        time: "12:57 AM",
        value: 4583
      },
      {
        time: "3:01 PM",
        value: 3046
      },
      {
        time: "2:13 PM",
        value: 2290
      },
      {
        time: "4:49 PM",
        value: 1057
      },
      {
        time: "5:08 AM",
        value: 2263
      },
      {
        time: "4:11 PM",
        value: 783
      },
      {
        time: "11:24 AM",
        value: 477
      },
      {
        time: "11:11 AM",
        value: 701
      },
      {
        time: "10:12 AM",
        value: 3867
      },
      {
        time: "2:30 AM",
        value: 3013
      },
      {
        time: "11:34 PM",
        value: 3578
      },
      {
        time: "7:25 PM",
        value: 2078
      },
      {
        time: "5:03 AM",
        value: 4649
      },
      {
        time: "11:21 PM",
        value: 4262
      },
      {
        time: "1:17 PM",
        value: 4583
      },
      {
        time: "1:49 AM",
        value: 2856
      },
      {
        time: "4:07 PM",
        value: 290
      },
      {
        time: "3:49 AM",
        value: 1830
      },
      {
        time: "4:59 PM",
        value: 1907
      },
      {
        time: "7:45 AM",
        value: 982
      },
      {
        time: "7:10 PM",
        value: 993
      },
      {
        time: "7:35 AM",
        value: 1476
      },
      {
        time: "1:28 AM",
        value: 4153
      },
      {
        time: "10:00 AM",
        value: 1401
      },
      {
        time: "6:35 PM",
        value: 1841
      },
      {
        time: "1:48 PM",
        value: 4285
      },
      {
        time: "3:48 AM",
        value: 4013
      },
      {
        time: "6:36 AM",
        value: 3680
      },
      {
        time: "3:56 AM",
        value: 3649
      },
      {
        time: "8:08 AM",
        value: 2908
      },
      {
        time: "6:34 AM",
        value: 4972
      },
      {
        time: "2:24 AM",
        value: 3278
      },
      {
        time: "6:13 AM",
        value: 2608
      },
      {
        time: "4:16 AM",
        value: 630
      },
      {
        time: "11:56 PM",
        value: 1360
      },
      {
        time: "12:04 AM",
        value: 1715
      },
      {
        time: "12:05 PM",
        value: 3166
      },
      {
        time: "9:26 PM",
        value: 3279
      },
      {
        time: "8:33 AM",
        value: 3338
      }
    ]
  }
];

const GridDashboard = () => {
  const width = 400;
  const height = 200;
  return (
    <div className="dashboard">
      {/* <GridLayout /> */}

      {/* <ResponsiveGridLayout
        className="layout"
        layouts={layout_config}
        // onBreakpointChange={this.handleBreakPointChange}
        isDraggable
        isRearrangeable
        isResizable
        draggableHandle=".grid-item__title"
        breakpoints={{ lg: 1280, md: 992, sm: 767, xs: 480, xxs: 0 }}
        cols={{ lg: 12, md: 10, sm: 6, xs: 4, xxs: 2 }}
      > */}
        {grid_data.map((item,index) => (
          
          <GraphBlock key={index} type={item.type} data={item.data} width={width} height={height} />
          
          ))}
      {/* </ResponsiveGridLayout> */}
    </div>
  );
};

export default GridDashboard;

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/layoutConfig.js
const layout_config = {
  lg: [
    {
      w: 8,
      h: 2,
      x: 0,
      y: 0,
      i: "graph1"
    },
    {
      w: 4,
      h: 2,
      x: 8,
      y: 0,
      i: "graph2"
    },
    {
      w: 5,
      h: 2,
      x: 0,
      y: 0,
      i: "graph3"
    },
    {
      w: 3,
      h: 2,
      x: 5,
      y: 0,
      i: "graph4"
    },
    {
      w: 4,
      h: 2,
      x: 9,
      y: 2,
      i: "graph5"
    },
    {
      w: 3,
      h: 2,
      x: 3,
      y: 2,
      i: "graph6"
    },
    {
      w: 3,
      h: 2,
      x: 0,
      y: 2,
      i: "graph7"
    }
  ],
  md: [
    {
      w: 6,
      h: 2,
      x: 0,
      y: 0,
      i: "graph1"
    },
    {
      w: 4,
      h: 2,
      x: 6,
      y: 0,
      i: "graph2"
    },
    {
      w: 3,
      h: 2,
      x: 0,
      y: 0,
      i: "graph3"
    },
    {
      w: 3,
      h: 2,
      x: 3,
      y: 0,
      i: "graph4"
    },
    {
      w: 4,
      h: 2,
      x: 6,
      y: 2,
      i: "graph5"
    },
    {
      w: 3,
      h: 2,
      x: 3,
      y: 2,
      i: "graph6"
    },
    {
      w: 3,
      h: 2,
      x: 0,
      y: 2,
      i: "graph7"
    }
  ],
  sm: [
    {
      w: 6,
      h: 2,
      x: 0,
      y: 0,
      i: "graph1"
    },
    {
      w: 3,
      h: 2,
      x: 0,
      y: 0,
      i: "graph2"
    },
    {
      w: 3,
      h: 2,
      x: 3,
      y: 0,
      i: "graph3"
    },
    {
      w: 3,
      h: 2,
      x: 0,
      y: 0,
      i: "graph4"
    },
    {
      w: 3,
      h: 2,
      x: 3,
      y: 2,
      i: "graph5"
    },
    {
      w: 3,
      h: 2,
      x: 0,
      y: 2,
      i: "graph6"
    },
    {
      w: 3,
      h: 2,
      x: 3,
      y: 2,
      i: "graph7"
    }
  ],
  xs: [
    {
      w: 4,
      h: 2,
      x: 0,
      y: 0,
      i: "graph1"
    },
    {
      w: 4,
      h: 2,
      x: 0,
      y: 0,
      i: "graph2"
    },
    {
      w: 4,
      h: 2,
      x: 0,
      y: 0,
      i: "graph3"
    },
    {
      w: 4,
      h: 2,
      x: 0,
      y: 0,
      i: "graph4"
    },
    {
      w: 4,
      h: 2,
      x: 0,
      y: 2,
      i: "graph5"
    },
    {
      w: 4,
      h: 2,
      x: 0,
      y: 2,
      i: "graph6"
    },
    {
      w: 4,
      h: 2,
      x: 0,
      y: 2,
      i: "graph7"
    }
  ]
};

export default layout_config;
--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/stateData.js
const state_data = {
  graph1: {
    type: "line",
    title: "Graph 1",
    data: [
      {
        time: "5:08 AM",
        value: 3738
      },
      {
        time: "4:52 PM",
        value: 2135
      },
      {
        time: "4:04 AM",
        value: 2649
      },
      {
        time: "10:17 AM",
        value: 560
      },
      {
        time: "11:39 AM",
        value: 3942
      },
      {
        time: "1:41 PM",
        value: 3421
      },
      {
        time: "6:39 AM",
        value: 2634
      },
      {
        time: "5:08 PM",
        value: 2298
      },
      {
        time: "2:46 AM",
        value: 2231
      },
      {
        time: "10:56 PM",
        value: 921
      },
      {
        time: "3:48 AM",
        value: 4047
      },
      {
        time: "4:30 AM",
        value: 4186
      },
      {
        time: "10:44 PM",
        value: 4350
      },
      {
        time: "12:41 AM",
        value: 3057
      },
      {
        time: "7:16 PM",
        value: 524
      },
      {
        time: "9:47 AM",
        value: 2924
      },
      {
        time: "5:43 PM",
        value: 173
      },
      {
        time: "12:13 AM",
        value: 1244
      },
      {
        time: "2:07 AM",
        value: 631
      },
      {
        time: "7:37 AM",
        value: 2216
      },
      {
        time: "10:00 AM",
        value: 3112
      },
      {
        time: "11:21 PM",
        value: 4318
      },
      {
        time: "10:38 PM",
        value: 1788
      },
      {
        time: "2:36 PM",
        value: 4382
      },
      {
        time: "1:48 AM",
        value: 142
      },
      {
        time: "8:12 AM",
        value: 423
      },
      {
        time: "6:01 AM",
        value: 260
      },
      {
        time: "9:05 AM",
        value: 1327
      },
      {
        time: "1:41 AM",
        value: 1347
      },
      {
        time: "9:08 AM",
        value: 3983
      },
      {
        time: "12:31 AM",
        value: 960
      },
      {
        time: "2:59 PM",
        value: 4989
      },
      {
        time: "9:43 AM",
        value: 2974
      },
      {
        time: "7:46 PM",
        value: 1896
      },
      {
        time: "1:02 PM",
        value: 111
      },
      {
        time: "10:33 AM",
        value: 1868
      },
      {
        time: "12:37 PM",
        value: 4486
      },
      {
        time: "11:30 AM",
        value: 4383
      },
      {
        time: "8:01 AM",
        value: 924
      },
      {
        time: "12:17 PM",
        value: 1679
      },
      {
        time: "9:03 AM",
        value: 4815
      },
      {
        time: "7:20 AM",
        value: 1916
      },
      {
        time: "9:52 PM",
        value: 1173
      },
      {
        time: "10:34 AM",
        value: 146
      },
      {
        time: "1:13 PM",
        value: 3722
      },
      {
        time: "4:38 AM",
        value: 1912
      },
      {
        time: "3:55 AM",
        value: 4101
      },
      {
        time: "1:55 PM",
        value: 3782
      },
      {
        time: "4:59 PM",
        value: 3795
      }
    ]
  },
  graph2: {
    type: "bar",
    title: "Graph 2",
    data: [
      {
        time: "11:01 PM",
        value: 2584
      },
      {
        time: "5:27 AM",
        value: 4601
      },
      {
        time: "12:25 AM",
        value: 2051
      },
      {
        time: "9:44 AM",
        value: 4797
      },
      {
        time: "3:08 PM",
        value: 1731
      },
      {
        time: "3:35 PM",
        value: 2966
      },
      {
        time: "6:54 AM",
        value: 3129
      },
      {
        time: "6:22 AM",
        value: 3152
      },
      {
        time: "1:00 PM",
        value: 1912
      },
      {
        time: "4:45 PM",
        value: 4969
      },
      {
        time: "6:22 AM",
        value: 3150
      },
      {
        time: "8:47 AM",
        value: 1891
      },
      {
        time: "10:51 AM",
        value: 2708
      },
      {
        time: "1:10 AM",
        value: 324
      },
      {
        time: "12:20 AM",
        value: 2374
      },
      {
        time: "8:51 AM",
        value: 2265
      },
      {
        time: "6:52 PM",
        value: 3601
      },
      {
        time: "6:03 AM",
        value: 4022
      },
      {
        time: "11:15 AM",
        value: 4140
      },
      {
        time: "10:57 PM",
        value: 373
      },
      {
        time: "9:30 AM",
        value: 2498
      },
      {
        time: "11:22 AM",
        value: 403
      },
      {
        time: "6:21 PM",
        value: 2825
      },
      {
        time: "9:27 AM",
        value: 1549
      },
      {
        time: "11:05 PM",
        value: 2476
      },
      {
        time: "5:33 PM",
        value: 458
      },
      {
        time: "8:25 PM",
        value: 983
      },
      {
        time: "5:38 PM",
        value: 3597
      },
      {
        time: "10:42 PM",
        value: 2107
      }
    ]
  },
  graph3: {
    type: "pie",
    title: "Graph 3",
    data: [
      {
        time: "8:09 AM",
        value: 4408
      },
      {
        time: "10:28 AM",
        value: 3644
      },
      {
        time: "8:11 PM",
        value: 4861
      },
      {
        time: "1:26 AM",
        value: 2394
      },
      {
        time: "6:55 PM",
        value: 2937
      },
      {
        time: "11:21 PM",
        value: 4806
      },
      {
        time: "8:10 PM",
        value: 3688
      },
      {
        time: "4:07 AM",
        value: 3182
      },
      {
        time: "9:26 PM",
        value: 1281
      },
      {
        time: "11:44 AM",
        value: 2058
      },
      {
        time: "3:19 PM",
        value: 939
      },
      {
        time: "9:03 PM",
        value: 2193
      },
      {
        time: "8:07 AM",
        value: 3201
      },
      {
        time: "7:05 PM",
        value: 2679
      },
      {
        time: "3:32 PM",
        value: 4651
      },
      {
        time: "2:36 AM",
        value: 3895
      },
      {
        time: "1:52 AM",
        value: 3914
      },
      {
        time: "12:52 AM",
        value: 4085
      },
      {
        time: "10:04 AM",
        value: 264
      },
      {
        time: "5:23 AM",
        value: 4148
      },
      {
        time: "2:57 PM",
        value: 4821
      },
      {
        time: "11:53 PM",
        value: 1106
      },
      {
        time: "2:51 AM",
        value: 3802
      },
      {
        time: "5:58 AM",
        value: 3507
      },
      {
        time: "12:03 AM",
        value: 2362
      },
      {
        time: "7:44 AM",
        value: 2392
      },
      {
        time: "2:11 PM",
        value: 3857
      },
      {
        time: "5:05 AM",
        value: 4673
      },
      {
        time: "1:17 PM",
        value: 4782
      },
      {
        time: "9:49 PM",
        value: 1162
      },
      {
        time: "12:37 AM",
        value: 2622
      },
      {
        time: "1:37 PM",
        value: 2993
      }
    ]
  },
  graph4: {
    type: "area",
    title: "Graph 4",
    data: [
      {
        time: "8:54 PM",
        value: 1690
      },
      {
        time: "10:50 AM",
        value: 2876
      },
      {
        time: "2:22 AM",
        value: 2779
      },
      {
        time: "11:11 AM",
        value: 4147
      },
      {
        time: "5:23 PM",
        value: 3179
      },
      {
        time: "5:16 AM",
        value: 3543
      },
      {
        time: "2:02 PM",
        value: 1362
      },
      {
        time: "6:06 AM",
        value: 478
      },
      {
        time: "11:06 PM",
        value: 1243
      },
      {
        time: "4:53 PM",
        value: 464
      },
      {
        time: "5:50 PM",
        value: 3688
      },
      {
        time: "6:02 PM",
        value: 1044
      },
      {
        time: "1:00 AM",
        value: 1582
      },
      {
        time: "2:46 AM",
        value: 1990
      },
      {
        time: "2:42 PM",
        value: 4452
      },
      {
        time: "10:03 AM",
        value: 186
      },
      {
        time: "8:17 AM",
        value: 613
      },
      {
        time: "3:50 PM",
        value: 167
      },
      {
        time: "8:03 AM",
        value: 4581
      },
      {
        time: "8:09 PM",
        value: 3458
      }
    ]
  },
  graph5: {
    type: "bar",
    title: "Graph 5",
    data: [
      {
        time: "10:28 AM",
        value: 1285
      },
      {
        time: "4:22 PM",
        value: 3740
      },
      {
        time: "1:31 AM",
        value: 549
      },
      {
        time: "8:48 PM",
        value: 2432
      },
      {
        time: "10:45 PM",
        value: 1029
      },
      {
        time: "5:50 AM",
        value: 2045
      },
      {
        time: "9:10 AM",
        value: 3103
      },
      {
        time: "9:48 PM",
        value: 2594
      },
      {
        time: "2:12 AM",
        value: 2298
      },
      {
        time: "8:46 PM",
        value: 2043
      },
      {
        time: "9:45 PM",
        value: 4216
      },
      {
        time: "3:27 PM",
        value: 1404
      },
      {
        time: "9:08 AM",
        value: 3618
      },
      {
        time: "12:03 PM",
        value: 1938
      },
      {
        time: "4:28 AM",
        value: 1550
      },
      {
        time: "5:05 AM",
        value: 1355
      },
      {
        time: "11:51 AM",
        value: 4740
      },
      {
        time: "9:11 PM",
        value: 3457
      },
      {
        time: "6:18 AM",
        value: 2099
      }
    ]
  },
  graph6: {
    type: "pie",
    title: "Graph 6",
    data: [
      {
        time: "12:47 AM",
        value: 4135
      },
      {
        time: "1:29 PM",
        value: 2915
      },
      {
        time: "4:47 AM",
        value: 119
      },
      {
        time: "6:53 PM",
        value: 4718
      },
      {
        time: "1:18 AM",
        value: 2424
      },
      {
        time: "9:46 PM",
        value: 4146
      },
      {
        time: "12:37 AM",
        value: 2801
      },
      {
        time: "2:05 AM",
        value: 1881
      },
      {
        time: "2:48 PM",
        value: 3905
      },
      {
        time: "11:37 PM",
        value: 4349
      },
      {
        time: "1:00 AM",
        value: 1127
      },
      {
        time: "7:58 PM",
        value: 3288
      },
      {
        time: "6:58 AM",
        value: 1381
      },
      {
        time: "11:06 AM",
        value: 1147
      },
      {
        time: "4:41 PM",
        value: 2030
      },
      {
        time: "11:53 PM",
        value: 1381
      },
      {
        time: "2:50 AM",
        value: 3040
      },
      {
        time: "7:47 PM",
        value: 2740
      },
      {
        time: "9:12 AM",
        value: 1190
      },
      {
        time: "10:30 AM",
        value: 3834
      },
      {
        time: "4:39 AM",
        value: 2334
      }
    ]
  },
  graph7: {
    type: "line",
    title: "Graph 7",
    data: [
      {
        time: "2:52 PM",
        value: 2262
      },
      {
        time: "1:39 PM",
        value: 4843
      },
      {
        time: "11:19 PM",
        value: 4611
      },
      {
        time: "2:08 PM",
        value: 4345
      },
      {
        time: "3:41 PM",
        value: 831
      },
      {
        time: "5:17 PM",
        value: 301
      },
      {
        time: "12:57 AM",
        value: 4583
      },
      {
        time: "3:01 PM",
        value: 3046
      },
      {
        time: "2:13 PM",
        value: 2290
      },
      {
        time: "4:49 PM",
        value: 1057
      },
      {
        time: "5:08 AM",
        value: 2263
      },
      {
        time: "4:11 PM",
        value: 783
      },
      {
        time: "11:24 AM",
        value: 477
      },
      {
        time: "11:11 AM",
        value: 701
      },
      {
        time: "10:12 AM",
        value: 3867
      },
      {
        time: "2:30 AM",
        value: 3013
      },
      {
        time: "11:34 PM",
        value: 3578
      },
      {
        time: "7:25 PM",
        value: 2078
      },
      {
        time: "5:03 AM",
        value: 4649
      },
      {
        time: "11:21 PM",
        value: 4262
      },
      {
        time: "1:17 PM",
        value: 4583
      },
      {
        time: "1:49 AM",
        value: 2856
      },
      {
        time: "4:07 PM",
        value: 290
      },
      {
        time: "3:49 AM",
        value: 1830
      },
      {
        time: "4:59 PM",
        value: 1907
      },
      {
        time: "7:45 AM",
        value: 982
      },
      {
        time: "7:10 PM",
        value: 993
      },
      {
        time: "7:35 AM",
        value: 1476
      },
      {
        time: "1:28 AM",
        value: 4153
      },
      {
        time: "10:00 AM",
        value: 1401
      },
      {
        time: "6:35 PM",
        value: 1841
      },
      {
        time: "1:48 PM",
        value: 4285
      },
      {
        time: "3:48 AM",
        value: 4013
      },
      {
        time: "6:36 AM",
        value: 3680
      },
      {
        time: "3:56 AM",
        value: 3649
      },
      {
        time: "8:08 AM",
        value: 2908
      },
      {
        time: "6:34 AM",
        value: 4972
      },
      {
        time: "2:24 AM",
        value: 3278
      },
      {
        time: "6:13 AM",
        value: 2608
      },
      {
        time: "4:16 AM",
        value: 630
      },
      {
        time: "11:56 PM",
        value: 1360
      },
      {
        time: "12:04 AM",
        value: 1715
      },
      {
        time: "12:05 PM",
        value: 3166
      },
      {
        time: "9:26 PM",
        value: 3279
      },
      {
        time: "8:33 AM",
        value: 3338
      }
    ]
  }
}

export default state_data;

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/styles.css
body {
  font-family: sans-serif;
  background: #171819;
}

.grid-item {
  background: #212124;
  border: 1px solid #141414;
  display: flex;
  flex-direction: column;
}

.grid-item__title {
  font-size: 14px;
  color: #fff;
  padding: 4px 0;
  text-align: center;
}
.grid-item__title:hover {
  cursor: move;
}
.grid-item__title .panel {
  box-shadow: none;
  border: none;
}
.grid-item__title .panel:focus {
  outline: none;
}
.grid-item__title .panel-heading {
  padding: 3px 0;
  background: #171819;
  border: none;
  color: rgba(255, 255, 255, 0.7);
}
.grid-item__title .panel-body {
  padding: 0 0 0 15px;
  background: #171819;
  color: rgba(255, 255, 255, 0.7);
}

.grid-item__graph {
  flex: 1;
}

.type-item {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.7);
  padding: 3px 0;
}
.type-item:hover {
  color: #fff;
}

.type-item.selected {
  color: #fff;
}

.data-edit__error {
  color: rgba(255, 0, 0, 0.7);
  font-size: 12px;
  padding: 3px 0;
}

.recharts-text {
  font-size: 12px;
}

.detail__info {
  color: #fff;
  padding: 20px;
}

.detail__edit {
  padding: 20px;
}

.detail__info > div {
  padding: 5px 0;
}

label {
  color: #fff;
  display: block;
}
.dropdown > .btn-default,
.dropdown.open > .btn-default {
  background: #171819;
  border: 1px solid #141414;
  color: #fff;
}
.dropdown > .btn-default:hover,
.dropdown > .btn-default:focus .dropdown.open > .btn-default:hover,
.dropdown.open > .btn-default:focus {
  background: #171819;
  border: 1px solid #141414;
  color: #fff;
  outline: none;
}

.dropdown-menu {
  border: 1px solid #141414;
  background: #171819;
  color: #fff;
}
.dropdown-menu > li > a {
  color: rgba(255, 255, 255, 0.7);
}
.dropdown-menu > li > a:hover {
  background: #171819;
  color: #fff;
}

.react-grid-item > .react-resizable-handle::after {
  border-right-color: rgba(255, 255, 255, 0.5);
  border-bottom-color: rgba(255, 255, 255, 0.5);
}

.modal-body {
  padding: 0;
}

.data-edit {
  position: relative;
}
.data-edit__update {
  position: absolute;
  right: 20px;
  bottom: 20px;
  z-index: 10;
}

.detail-page__title,
.edit-page__title {
  position: fixed;
  top: 20px;
  left: 0;
  right: 0;
  color: #fff;
  text-align: center;
}

.go-back {
  position: fixed;
  right: 20px;
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  top: 20px;
  z-index: 10;
}

.go-back:hover {
  color: #fff;
  cursor: pointer;
}

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/Title.js
import React, { Component } from "react";
import PropTypes from "prop-types";
// import { DropdownButton, Panel, MenuItem } from "react-bootstrap";
import { Link } from "react-router-dom";

import TypeItem from "./TypeItem";

// import { setType } from "../actions/app-actions";

import graphTypes from "./graph-types";

class Title extends Component {
  // handleClick = value => {
  //   const { root } = this.props;
  //   this.props.setType({ key: root, value, item: "type" });
  // };

  render() {
    const { title, type, root } = this.props;
    return (
      <>
      {/* <DropdownButton id="title-dropdown" title={title}>
        <li>
          <Link to={`/${root}/view`}>View</Link>
        </li>
        <li>
          <Link to={`/${root}/layout`}>Layout</Link>
        </li>
        <li>
          <Link to={`/${root}/edit`}>Edit</Link>
        </li>
        <MenuItem>
          <Panel id="collapsible-type-panel" defaultExpanded>
            <Panel.Heading>
              <Panel.Title toggle>Type</Panel.Title>
            </Panel.Heading>
            <Panel.Collapse>
              <Panel.Body> */}

                {/* {graphTypes.map(({ label, value }) => {
                  return (
                    <TypeItem
                      key={value}
                      // onClick={this.handleClick}
                      type={type}
                      value={value}
                      label={label}
                    />
                  );
                })} */}

              {/* </Panel.Body>
            </Panel.Collapse>
          </Panel>
        </MenuItem>
      </DropdownButton> */}
      </>
    );
  }
}

Title.propTypes = {
  root: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  type: PropTypes.string.isRequired
};

// export default connect(null, { setType })(Title);
export default Title;

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Dashboard/Recharter/TypeItem.js
import React, { Component } from "react";
import PropTypes from "prop-types";

class TypeItem extends Component {
  handleClick = () => {
    const { onClick, value } = this.props;

    onClick(value);
  };
  render() {
    const { type, label, value } = this.props;
    return (
      <div
        className={`type-item ${value === type ? "selected" : ""}`}
        onClick={this.handleClick}
      >
        {label}
      </div>
    );
  }
}

TypeItem.propTypes = {
  type: PropTypes.string.isRequired,
  value: PropTypes.string.isRequired,
  label: PropTypes.string.isRequired,
  onClick: PropTypes.func.isRequired
};

export default TypeItem;

--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/CreateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
// import moment from 'moment';

const CreateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit CreateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  // useEffect(() => {
  // }, [initialFormValues]);

  return <Form name='create_form' 
      // size='small'
      form={form_konek_provider}
      className='create_form'
    >
    <Row gutter={[8, 16]}>
      <Col span='24'>
        
        {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


      </Col>
    </Row>

  </Form>;
}

export default CreateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/Equipment.js

import React, { useEffect, useState } from 'react';

import {
	Button,
	DatePicker,
	Divider,
	Drawer,
	Input, InputNumber ,
	Modal,
	Popover,
	Select,
	Space,
} from 'antd';
import {
	DesktopOutlined,
	DownOutlined, 
	UserOutlined,
	// HomeOutlined,
	// SettingFilled,
	// SmileOutlined,
	FileExcelOutlined,
	FilePdfOutlined,
	ReloadOutlined,
	ReloadFilled, 
	DeleteOutlined,
	DeleteFilled,
} from '@ant-design/icons';

import ToolbarContext from 'context/ToolbarContext';
import TabPage from 'common/TabPage';

import ReadList from './List';
import FormWrapper from './FormWrapper';

const Equipment = () => {
	const { setToolbar } = React.useContext(ToolbarContext);
	const [lokasiTab, setLokasiTab] = useState('top');
	const [drawerVisible, setDrawerVisible] = useState(false);
	// diisi oleh List wkt 'Show'
	const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

	const show_update = (data) => {
		set_modal_bomodule_content(data);
		setDrawerVisible(true);
	}

	let Toolbar = () => (<Space>
		<h1>Equipment</h1>
		<Button type="primary" 
			onClick = {				
				() => {
					set_modal_bomodule_content({});
					setDrawerVisible(true);
				}
			}>Create new</Button>
		{/* <Button type="default" disabled onClick={generateBlotter2}>Blotter Subscription</Button> */}
		{/* <Popover placement="bottom" title={<span>Pilih nasabah dan tanggal Blotter subscription</span>} content={Blotter_Popup} trigger="click"> */}
		{/* <Button disabled type="primary">Blotter Subscription</Button> */}
		{/* </Popover> */}			
	</Space>);

	useEffect(function() {
		setToolbar(<Toolbar />)
	}, []);

	return <>
		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'Create',
						icon: <DesktopOutlined />,
						component: <FormWrapper />
					},
					{
						title: 'Read',
						icon: <DesktopOutlined />,
						component: <ReadList show_update={show_update} />
					},
				]
			} />

		<Drawer
      title="Add Record"
      placement='right'      
      onClose={() => setDrawerVisible(false)}
      visible={drawerVisible}
      width={800}
      // closable={false}
      >

			<FormWrapper
				data_raw={modal_bomodule_content}
				onClose={() => setDrawerVisible(false)}
				/>

		</Drawer>
	
	</>;
};

export default Equipment;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/FormProvider.js

import React, { useEffect, useState } from 'react';

import {
  Button,
  Checkbox,
  Form,
  notification,
} from 'antd';

import useAxios from 'utils/useAxios';
import UpdateForm from './UpdateForm';
import CreateForm from './CreateForm';
import PubSub from 'pubsub-js';

const FormProvider = ({
  onClose,
  data_raw = {},
  submit_form = (values) => console.log(`submit FormProvider`),
}) => {

  const updateRecord = useAxios({ method: 'PATCH', });
  const createRecord = useAxios({ method: 'POST', path: 'equipment',  });
  const is_updating = Object.keys(data_raw).length > 0;

  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  return <Form.Provider onFormFinish={(name, {values, forms}) => {

    if (is_updating) {
      const { update_form } = forms;
      let updated_values = update_form.getFieldsValue();
      let diffs = {};
      for (let key in updated_values) {
        if (updated_values.hasOwnProperty(key)) {
          if (updated_values[key] !== data_raw[key]) {
            diffs[key] = updated_values[key];
          }
        }      
      }
      console.log(`update diffs: ${JSON.stringify(diffs)}`);
      let values_has_changed = Object.keys(diffs).length > 0;
      if (values_has_changed) {
        updateRecord(
          {
            // url: useUrlBuilder(`bo/bo_marketholiday/${updated_values.id}`),
            path: `equipment/${updated_values.id}`,
            data: diffs
          },

          response => {
            console.log(`sukses updateRecord => ${JSON.stringify(response)}`);
            berhasil(`sukses updateRecord [${JSON.stringify(response)}]`);
            PubSub.publish('<<Update:Record>>', response);
          },

          err => {
            console.log(`gagal updateRecord => ${JSON.stringify(err)}.`);
            gagal(`gagal updateRecord [${JSON.stringify(err)}]`);
          }
        );
      }

    } else {
      const { create_form } = forms;
      let created_values = create_form.getFieldsValue();
      console.log(`created values from onformfinish: ${JSON.stringify(values)} vs getfieldsvalue ${JSON.stringify(created_values)}`);
      createRecord(
        {
          data: created_values
        },

        response => {
          console.log(`sukses createRecord => ${JSON.stringify(response)}`);
          berhasil(`sukses createRecord.`);
          PubSub.publish('<<Create:Record>>', response);
        },

        err => {
          console.log(`gagal createRecord => ${JSON.stringify(err)}.`);
          gagal(`gagal createRecord.`);
        }
      );

    }      

    onClose();

  }}>

    {is_updating ? <UpdateForm initialFormValues={data_raw} /> : <CreateForm />}

    <Form name="fundordertabs-form-body" onFinish={(values) => {}}>
      <Form.Item>
        <Button type='primary' htmlType="submit">Submit</Button>
      </Form.Item>
    </Form>

  </Form.Provider>;

}

export default FormProvider;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/FormWrapper.js

import React, { useEffect, useState } from 'react'
import FormProvider from './FormProvider'

const FormWrapper = ({
    onClose=()=>{},
    data_raw={},
    data_selected={},
}) => {
  return <>    
    <FormProvider 
      data_raw={data_raw} 
      onClose={onClose} />
  </>;
}

export default FormWrapper;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/List.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';
import PubSub from 'pubsub-js';

import useAxios from 'utils/useAxios';
import SimpleTable from 'common/Table/SimpleTable';
import JsonData from 'assets/equipment.json';

function column_sorter(a, b, column) {
  console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`);
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    // return b[column][0].toLowerCase() > a[column][0].toLowerCase();
    return 0;
      
  return b[column] > a[column];
}

const List = ({
  show_update,
  recordTransformer = record => record,
}) => {

  const resource_path = 'equipment';
  const deleteRecord = useAxios({ method: 'DELETE', });
  const [table_data, set_table_data] = useState([]);
  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  const getResourceData = useAxios({ path: resource_path, });  

  const update_table_data = (topic_channel, data) => {
    getResourceData({}, successHandler);
  };

  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  };

  const wrapAsync = () => {
    PubSub.subscribe('<<Create:Record>>', update_table_data);
    PubSub.subscribe('<<Update:Record>>', update_table_data);
    PubSub.subscribe('<<Delete:Record>>', update_table_data);
  }

  useEffect(() => {
    wrapAsync();
    getResourceData({}, successHandler);
  }, []);

  const handleDelete = record => {
    const key = record.key;
    console.log(`deleting ${key} dari record ${JSON.stringify(record)}.`);
    // const table_data_temp = [...table_data].filter(item => item.key !== key);
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    } else {
      console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
      return;
    }

    deleteRecord(
      {
        path: `${resource_path}/${kunci}`,
      },
      response => {
        console.log(`berhasil hapus ${kunci}`);
        PubSub.publish('<<Delete:Record>>', response);
        berhasil('Berhasil', `Berhasil hapus id ${kunci}`);
      },
      err => {
        console.log(`gagal hapus ${kunci}`);
        gagal('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
      }
    );
  }

  const table_header = JsonData.headers.map((column, index) => {

    if (column === "") {

      return {
        title: "Show",
        fixed: 'left',
        width: JsonData.widths.show,
        render: data => <Button onClick={() => {
          console.log(`Show data ${JSON.stringify(data)}`);
          show_update(data);
        }}>Show </Button>,
      };

    } else if (column === "delete") {

      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: JsonData.widths.hapus,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {

      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? JsonData.widths.id : JsonData.widths.normal,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  const modalSelectionHandler = (selections) => {
    // set_modal_bomodule_selected(selections);
    // if (selectionCallback !== undefined) {            
    //   // kirim id dari record, bukan index selection
    //   let id_list = []
    //   selections.forEach(index => {
    //     let ketemu = table_data.find(record => record.key == index)                
    //     // if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
    //     //   id_list .push(ketemu.id + "," + ketemu.id_user);
    //     // else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
    //     //   id_list .push(ketemu.orderno + "," + ketemu.customerno);
    //   })
    //   if (id_list.length > 0) {
    //     selectionCallback(id_list);
    //     console.log(`selection ${id_list}`);
    //   }
    // }
    console.log(`SimpleTable selectCallback: ${selections}, ${typeof(selections)}.`);
  }

	return <>

    <SimpleTable 
      header={table_header}
      body={table_data} 
      selectCallback={modalSelectionHandler} />

  </>;
};

export default List;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/Modal.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, 
  Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';


const BoComponentModalDefaultContent = ({
  data_selected,
  data_raw
}) => (<>
      Daftar terselect default isi-selected: {JSON.stringify(data_selected)}
      <hr />
      Isi show (data raw): {JSON.stringify(data_raw)}
  </>
);

const BoComponentModal = ({
  Content,
  modal_title,
  modal_bomodule_visible,
  modal_bomodule_selected,
  modal_bomodule_content,
  set_modal_bomodule,
}) => (<Modal visible={modal_bomodule_visible} title={modal_title}
    onOk={(e) => set_modal_bomodule(false)}
    onCancel={(e) => set_modal_bomodule(false)}
  >

    {<Content
      data_selected={modal_bomodule_selected}
      data_raw={modal_bomodule_content}
    />}

  </Modal>
);

export default {
  BoComponentModalDefaultContent,
  BoComponentModal,
};


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Equipment/UpdateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
import moment from 'moment';

const UpdateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit UpdateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  useEffect(() => {
    const {
      date,
      ...bukan_tanggal
    } = initialFormValues

    form_konek_provider.setFieldsValue({
      date: moment(date),
      ...bukan_tanggal
    });

  }, [initialFormValues]);

  return <Form name='update_form' 
      // size='small'
      form={form_konek_provider}
      className='update_form'
    >
      <Row gutter={[8, 16]}>
        <Col span='24'>
          
          {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


        </Col>
      </Row>

    </Form>;
}

export default UpdateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Floor/CreateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
// import moment from 'moment';

const CreateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit CreateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  // useEffect(() => {
  // }, [initialFormValues]);

  return <Form name='create_form' 
      // size='small'
      form={form_konek_provider}
      className='create_form'
    >
    <Row gutter={[8, 16]}>
      <Col span='24'>
        
        {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


      </Col>
    </Row>

  </Form>;
}

export default CreateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Floor/Floor.js

import React, { useEffect, useState } from 'react';

import {
	Button,
	DatePicker,
	Divider,
	Drawer,
	Input, InputNumber ,
	Modal,
	Popover,
	Select,
	Space,
} from 'antd';
import {
	DesktopOutlined,
	DownOutlined, 
	UserOutlined,
	// HomeOutlined,
	// SettingFilled,
	// SmileOutlined,
	FileExcelOutlined,
	FilePdfOutlined,
	ReloadOutlined,
	ReloadFilled, 
	DeleteOutlined,
	DeleteFilled,
} from '@ant-design/icons';

import ToolbarContext from 'context/ToolbarContext';
import TabPage from 'common/TabPage';

import ReadList from './List';
import FormWrapper from './FormWrapper';

const Floor = () => {
	const { setToolbar } = React.useContext(ToolbarContext);
	const [lokasiTab, setLokasiTab] = useState('top');
	const [drawerVisible, setDrawerVisible] = useState(false);
	// diisi oleh List wkt 'Show'
	const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

	const show_update = (data) => {
		set_modal_bomodule_content(data);
		setDrawerVisible(true);
	}

	let Toolbar = () => (<Space>
		<h1>Floor</h1>
		<Button type="primary" 
			onClick = {				
				() => {
					set_modal_bomodule_content({});
					setDrawerVisible(true);
				}
			}>Create new</Button>
		{/* <Button type="default" disabled onClick={generateBlotter2}>Blotter Subscription</Button> */}
		{/* <Popover placement="bottom" title={<span>Pilih nasabah dan tanggal Blotter subscription</span>} content={Blotter_Popup} trigger="click"> */}
		{/* <Button disabled type="primary">Blotter Subscription</Button> */}
		{/* </Popover> */}			
	</Space>);

	useEffect(function() {
		setToolbar(<Toolbar />)
	}, []);

	return <>
		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'Create',
						icon: <DesktopOutlined />,
						component: <FormWrapper />
					},
					{
						title: 'Read',
						icon: <DesktopOutlined />,
						component: <ReadList show_update={show_update} />
					},
				]
			} />

		<Drawer
      title="Add Record"
      placement='right'      
      onClose={() => setDrawerVisible(false)}
      visible={drawerVisible}
      width={800}
      // closable={false}
      >

			<FormWrapper
				data_raw={modal_bomodule_content}
				onClose={() => setDrawerVisible(false)}
				/>

		</Drawer>
	
	</>;
};

export default Floor;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Floor/FormProvider.js

import React, { useEffect, useState } from 'react';

import {
  Button,
  Checkbox,
  Form,
  notification,
} from 'antd';

import useAxios from 'utils/useAxios';
import UpdateForm from './UpdateForm';
import CreateForm from './CreateForm';
import PubSub from 'pubsub-js';

const FormProvider = ({
  onClose,
  data_raw = {},
  submit_form = (values) => console.log(`submit FormProvider`),
}) => {

  const updateRecord = useAxios({ method: 'PATCH', });
  const createRecord = useAxios({ method: 'POST', path: 'floor',  });
  const is_updating = Object.keys(data_raw).length > 0;

  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  return <Form.Provider onFormFinish={(name, {values, forms}) => {

    if (is_updating) {
      const { update_form } = forms;
      let updated_values = update_form.getFieldsValue();
      let diffs = {};
      for (let key in updated_values) {
        if (updated_values.hasOwnProperty(key)) {
          if (updated_values[key] !== data_raw[key]) {
            diffs[key] = updated_values[key];
          }
        }      
      }
      console.log(`update diffs: ${JSON.stringify(diffs)}`);
      let values_has_changed = Object.keys(diffs).length > 0;
      if (values_has_changed) {
        updateRecord(
          {
            // url: useUrlBuilder(`bo/bo_marketholiday/${updated_values.id}`),
            path: `floor/${updated_values.id}`,
            data: diffs
          },

          response => {
            console.log(`sukses updateRecord => ${JSON.stringify(response)}`);
            berhasil(`sukses updateRecord [${JSON.stringify(response)}]`);
            PubSub.publish('<<Update:Record>>', response);
          },

          err => {
            console.log(`gagal updateRecord => ${JSON.stringify(err)}.`);
            gagal(`gagal updateRecord [${JSON.stringify(err)}]`);
          }
        );
      }

    } else {
      const { create_form } = forms;
      let created_values = create_form.getFieldsValue();
      console.log(`created values from onformfinish: ${JSON.stringify(values)} vs getfieldsvalue ${JSON.stringify(created_values)}`);
      createRecord(
        {
          data: created_values
        },

        response => {
          console.log(`sukses createRecord => ${JSON.stringify(response)}`);
          berhasil(`sukses createRecord.`);
          PubSub.publish('<<Create:Record>>', response);
        },

        err => {
          console.log(`gagal createRecord => ${JSON.stringify(err)}.`);
          gagal(`gagal createRecord.`);
        }
      );

    }      

    onClose();

  }}>

    {is_updating ? <UpdateForm initialFormValues={data_raw} /> : <CreateForm />}

    <Form name="fundordertabs-form-body" onFinish={(values) => {}}>
      <Form.Item>
        <Button type='primary' htmlType="submit">Submit</Button>
      </Form.Item>
    </Form>

  </Form.Provider>;

}

export default FormProvider;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Floor/FormWrapper.js

import React, { useEffect, useState } from 'react'
import FormProvider from './FormProvider'

const FormWrapper = ({
    onClose=()=>{},
    data_raw={},
    data_selected={},
}) => {
  return <>    
    <FormProvider 
      data_raw={data_raw} 
      onClose={onClose} />
  </>;
}

export default FormWrapper;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Floor/List.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';
import PubSub from 'pubsub-js';

import useAxios from 'utils/useAxios';
import SimpleTable from 'common/Table/SimpleTable';
import JsonData from 'assets/floor.json';

function column_sorter(a, b, column) {
  console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`);
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    // return b[column][0].toLowerCase() > a[column][0].toLowerCase();
    return 0;
      
  return b[column] > a[column];
}

const List = ({
  show_update,
  recordTransformer = record => record,
}) => {

  const resource_path = 'floor';
  const deleteRecord = useAxios({ method: 'DELETE', });
  const [table_data, set_table_data] = useState([]);
  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  const getResourceData = useAxios({ path: resource_path, });  

  const update_table_data = (topic_channel, data) => {
    getResourceData({}, successHandler);
  };

  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  };

  const wrapAsync = () => {
    PubSub.subscribe('<<Create:Record>>', update_table_data);
    PubSub.subscribe('<<Update:Record>>', update_table_data);
    PubSub.subscribe('<<Delete:Record>>', update_table_data);
  }

  useEffect(() => {
    wrapAsync();
    getResourceData({}, successHandler);
  }, []);

  const handleDelete = record => {
    const key = record.key;
    console.log(`deleting ${key} dari record ${JSON.stringify(record)}.`);
    // const table_data_temp = [...table_data].filter(item => item.key !== key);
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    } else {
      console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
      return;
    }

    deleteRecord(
      {
        path: `${resource_path}/${kunci}`,
      },
      response => {
        console.log(`berhasil hapus ${kunci}`);
        PubSub.publish('<<Delete:Record>>', response);
        berhasil('Berhasil', `Berhasil hapus id ${kunci}`);
      },
      err => {
        console.log(`gagal hapus ${kunci}`);
        gagal('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
      }
    );
  }

  const table_header = JsonData.headers.map((column, index) => {

    if (column === "") {

      return {
        title: "Show",
        fixed: 'left',
        width: JsonData.widths.show,
        render: data => <Button onClick={() => {
          console.log(`Show data ${JSON.stringify(data)}`);
          show_update(data);
        }}>Show </Button>,
      };

    } else if (column === "delete") {

      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: JsonData.widths.hapus,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {

      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? JsonData.widths.id : JsonData.widths.normal,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  const modalSelectionHandler = (selections) => {
    // set_modal_bomodule_selected(selections);
    // if (selectionCallback !== undefined) {            
    //   // kirim id dari record, bukan index selection
    //   let id_list = []
    //   selections.forEach(index => {
    //     let ketemu = table_data.find(record => record.key == index)                
    //     // if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
    //     //   id_list .push(ketemu.id + "," + ketemu.id_user);
    //     // else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
    //     //   id_list .push(ketemu.orderno + "," + ketemu.customerno);
    //   })
    //   if (id_list.length > 0) {
    //     selectionCallback(id_list);
    //     console.log(`selection ${id_list}`);
    //   }
    // }
    console.log(`SimpleTable selectCallback: ${selections}, ${typeof(selections)}.`);
  }

	return <>

    <SimpleTable 
      header={table_header}
      body={table_data} 
      selectCallback={modalSelectionHandler} />

  </>;
};

export default List;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Floor/Modal.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, 
  Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';


const BoComponentModalDefaultContent = ({
  data_selected,
  data_raw
}) => (<>
      Daftar terselect default isi-selected: {JSON.stringify(data_selected)}
      <hr />
      Isi show (data raw): {JSON.stringify(data_raw)}
  </>
);

const BoComponentModal = ({
  Content,
  modal_title,
  modal_bomodule_visible,
  modal_bomodule_selected,
  modal_bomodule_content,
  set_modal_bomodule,
}) => (<Modal visible={modal_bomodule_visible} title={modal_title}
    onOk={(e) => set_modal_bomodule(false)}
    onCancel={(e) => set_modal_bomodule(false)}
  >

    {<Content
      data_selected={modal_bomodule_selected}
      data_raw={modal_bomodule_content}
    />}

  </Modal>
);

export default {
  BoComponentModalDefaultContent,
  BoComponentModal,
};


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Floor/UpdateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
import moment from 'moment';

const UpdateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit UpdateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  useEffect(() => {
    const {
      date,
      ...bukan_tanggal
    } = initialFormValues

    form_konek_provider.setFieldsValue({
      date: moment(date),
      ...bukan_tanggal
    });

  }, [initialFormValues]);

  return <Form name='update_form' 
      // size='small'
      form={form_konek_provider}
      className='update_form'
    >
      <Row gutter={[8, 16]}>
        <Col span='24'>
          
          {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


        </Col>
      </Row>

    </Form>;
}

export default UpdateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Location/CreateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
// import moment from 'moment';

const CreateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit CreateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  // useEffect(() => {
  // }, [initialFormValues]);

  return <Form name='create_form' 
      // size='small'
      form={form_konek_provider}
      className='create_form'
    >
    <Row gutter={[8, 16]}>
      <Col span='24'>
        
        {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


      </Col>
    </Row>

  </Form>;
}

export default CreateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Location/FormProvider.js

import React, { useEffect, useState } from 'react';

import {
  Button,
  Checkbox,
  Form,
  notification,
} from 'antd';

import useAxios from 'utils/useAxios';
import UpdateForm from './UpdateForm';
import CreateForm from './CreateForm';
import PubSub from 'pubsub-js';

const FormProvider = ({
  onClose,
  data_raw = {},
  submit_form = (values) => console.log(`submit FormProvider`),
}) => {

  const updateRecord = useAxios({ method: 'PATCH', });
  const createRecord = useAxios({ method: 'POST', path: 'location',  });
  const is_updating = Object.keys(data_raw).length > 0;

  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  return <Form.Provider onFormFinish={(name, {values, forms}) => {

    if (is_updating) {
      const { update_form } = forms;
      let updated_values = update_form.getFieldsValue();
      let diffs = {};
      for (let key in updated_values) {
        if (updated_values.hasOwnProperty(key)) {
          if (updated_values[key] !== data_raw[key]) {
            diffs[key] = updated_values[key];
          }
        }      
      }
      console.log(`update diffs: ${JSON.stringify(diffs)}`);
      let values_has_changed = Object.keys(diffs).length > 0;
      if (values_has_changed) {
        updateRecord(
          {
            // url: useUrlBuilder(`bo/bo_marketholiday/${updated_values.id}`),
            path: `location/${updated_values.id}`,
            data: diffs
          },

          response => {
            console.log(`sukses updateRecord => ${JSON.stringify(response)}`);
            berhasil(`sukses updateRecord [${JSON.stringify(response)}]`);
            PubSub.publish('<<Update:Record>>', response);
          },

          err => {
            console.log(`gagal updateRecord => ${JSON.stringify(err)}.`);
            gagal(`gagal updateRecord [${JSON.stringify(err)}]`);
          }
        );
      }

    } else {
      const { create_form } = forms;
      let created_values = create_form.getFieldsValue();
      console.log(`created values from onformfinish: ${JSON.stringify(values)} vs getfieldsvalue ${JSON.stringify(created_values)}`);
      createRecord(
        {
          data: created_values
        },

        response => {
          console.log(`sukses createRecord => ${JSON.stringify(response)}`);
          berhasil(`sukses createRecord.`);
          PubSub.publish('<<Create:Record>>', response);
        },

        err => {
          console.log(`gagal createRecord => ${JSON.stringify(err)}.`);
          gagal(`gagal createRecord.`);
        }
      );

    }      

    onClose();

  }}>

    {is_updating ? <UpdateForm initialFormValues={data_raw} /> : <CreateForm />}

    <Form name="fundordertabs-form-body" onFinish={(values) => {}}>
      <Form.Item>
        <Button type='primary' htmlType="submit">Submit</Button>
      </Form.Item>
    </Form>

  </Form.Provider>;

}

export default FormProvider;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Location/FormWrapper.js

import React, { useEffect, useState } from 'react'
import FormProvider from './FormProvider'

const FormWrapper = ({
    onClose=()=>{},
    data_raw={},
    data_selected={},
}) => {
  return <>    
    <FormProvider 
      data_raw={data_raw} 
      onClose={onClose} />
  </>;
}

export default FormWrapper;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Location/List.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';
import PubSub from 'pubsub-js';

import useAxios from 'utils/useAxios';
import SimpleTable from 'common/Table/SimpleTable';
import JsonData from 'assets/location.json';

function column_sorter(a, b, column) {
  console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`);
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    // return b[column][0].toLowerCase() > a[column][0].toLowerCase();
    return 0;
      
  return b[column] > a[column];
}

const List = ({
  show_update,
  recordTransformer = record => record,
}) => {

  const resource_path = 'location';
  const deleteRecord = useAxios({ method: 'DELETE', });
  const [table_data, set_table_data] = useState([]);
  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  const getResourceData = useAxios({ path: resource_path, });  

  const update_table_data = (topic_channel, data) => {
    getResourceData({}, successHandler);
  };

  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  };

  const wrapAsync = () => {
    PubSub.subscribe('<<Create:Record>>', update_table_data);
    PubSub.subscribe('<<Update:Record>>', update_table_data);
    PubSub.subscribe('<<Delete:Record>>', update_table_data);
  }

  useEffect(() => {
    wrapAsync();
    getResourceData({}, successHandler);
  }, []);

  const handleDelete = record => {
    const key = record.key;
    console.log(`deleting ${key} dari record ${JSON.stringify(record)}.`);
    // const table_data_temp = [...table_data].filter(item => item.key !== key);
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    } else {
      console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
      return;
    }

    deleteRecord(
      {
        path: `${resource_path}/${kunci}`,
      },
      response => {
        console.log(`berhasil hapus ${kunci}`);
        PubSub.publish('<<Delete:Record>>', response);
        berhasil('Berhasil', `Berhasil hapus id ${kunci}`);
      },
      err => {
        console.log(`gagal hapus ${kunci}`);
        gagal('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
      }
    );
  }

  const table_header = JsonData.headers.map((column, index) => {

    if (column === "") {

      return {
        title: "Show",
        fixed: 'left',
        width: JsonData.widths.show,
        render: data => <Button onClick={() => {
          console.log(`Show data ${JSON.stringify(data)}`);
          show_update(data);
        }}>Show </Button>,
      };

    } else if (column === "delete") {

      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: JsonData.widths.hapus,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {

      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? JsonData.widths.id : JsonData.widths.normal,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  const modalSelectionHandler = (selections) => {
    // set_modal_bomodule_selected(selections);
    // if (selectionCallback !== undefined) {            
    //   // kirim id dari record, bukan index selection
    //   let id_list = []
    //   selections.forEach(index => {
    //     let ketemu = table_data.find(record => record.key == index)                
    //     // if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
    //     //   id_list .push(ketemu.id + "," + ketemu.id_user);
    //     // else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
    //     //   id_list .push(ketemu.orderno + "," + ketemu.customerno);
    //   })
    //   if (id_list.length > 0) {
    //     selectionCallback(id_list);
    //     console.log(`selection ${id_list}`);
    //   }
    // }
    console.log(`SimpleTable selectCallback: ${selections}, ${typeof(selections)}.`);
  }

	return <>

    <SimpleTable 
      header={table_header}
      body={table_data} 
      selectCallback={modalSelectionHandler} />

  </>;
};

export default List;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Location/Location.js

import React, { useEffect, useState } from 'react';

import {
	Button,
	DatePicker,
	Divider,
	Drawer,
	Input, InputNumber ,
	Modal,
	Popover,
	Select,
	Space,
} from 'antd';
import {
	DesktopOutlined,
	DownOutlined, 
	UserOutlined,
	// HomeOutlined,
	// SettingFilled,
	// SmileOutlined,
	FileExcelOutlined,
	FilePdfOutlined,
	ReloadOutlined,
	ReloadFilled, 
	DeleteOutlined,
	DeleteFilled,
} from '@ant-design/icons';

import ToolbarContext from 'context/ToolbarContext';
import TabPage from 'common/TabPage';

import ReadList from './List';
import FormWrapper from './FormWrapper';

const Location = () => {
	const { setToolbar } = React.useContext(ToolbarContext);
	const [lokasiTab, setLokasiTab] = useState('top');
	const [drawerVisible, setDrawerVisible] = useState(false);
	// diisi oleh List wkt 'Show'
	const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

	const show_update = (data) => {
		set_modal_bomodule_content(data);
		setDrawerVisible(true);
	}

	let Toolbar = () => (<Space>
		<h1>Location</h1>
		<Button type="primary" 
			onClick = {				
				() => {
					set_modal_bomodule_content({});
					setDrawerVisible(true);
				}
			}>Create new</Button>
		{/* <Button type="default" disabled onClick={generateBlotter2}>Blotter Subscription</Button> */}
		{/* <Popover placement="bottom" title={<span>Pilih nasabah dan tanggal Blotter subscription</span>} content={Blotter_Popup} trigger="click"> */}
		{/* <Button disabled type="primary">Blotter Subscription</Button> */}
		{/* </Popover> */}			
	</Space>);

	useEffect(function() {
		setToolbar(<Toolbar />)
	}, []);

	return <>
		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'Create',
						icon: <DesktopOutlined />,
						component: <FormWrapper />
					},
					{
						title: 'Read',
						icon: <DesktopOutlined />,
						component: <ReadList show_update={show_update} />
					},
				]
			} />

		<Drawer
      title="Add Record"
      placement='right'      
      onClose={() => setDrawerVisible(false)}
      visible={drawerVisible}
      width={800}
      // closable={false}
      >

			<FormWrapper
				data_raw={modal_bomodule_content}
				onClose={() => setDrawerVisible(false)}
				/>

		</Drawer>
	
	</>;
};

export default Location;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Location/Modal.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, 
  Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';


const BoComponentModalDefaultContent = ({
  data_selected,
  data_raw
}) => (<>
      Daftar terselect default isi-selected: {JSON.stringify(data_selected)}
      <hr />
      Isi show (data raw): {JSON.stringify(data_raw)}
  </>
);

const BoComponentModal = ({
  Content,
  modal_title,
  modal_bomodule_visible,
  modal_bomodule_selected,
  modal_bomodule_content,
  set_modal_bomodule,
}) => (<Modal visible={modal_bomodule_visible} title={modal_title}
    onOk={(e) => set_modal_bomodule(false)}
    onCancel={(e) => set_modal_bomodule(false)}
  >

    {<Content
      data_selected={modal_bomodule_selected}
      data_raw={modal_bomodule_content}
    />}

  </Modal>
);

export default {
  BoComponentModalDefaultContent,
  BoComponentModal,
};


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Location/UpdateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
import moment from 'moment';

const UpdateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit UpdateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  useEffect(() => {
    const {
      date,
      ...bukan_tanggal
    } = initialFormValues

    form_konek_provider.setFieldsValue({
      date: moment(date),
      ...bukan_tanggal
    });

  }, [initialFormValues]);

  return <Form name='update_form' 
      // size='small'
      form={form_konek_provider}
      className='update_form'
    >
      <Row gutter={[8, 16]}>
        <Col span='24'>
          
          {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


        </Col>
      </Row>

    </Form>;
}

export default UpdateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/CreateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
// import moment from 'moment';

const CreateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit CreateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  // useEffect(() => {
  // }, [initialFormValues]);

  return <Form name='create_form' 
      // size='small'
      form={form_konek_provider}
      className='create_form'
    >
    <Row gutter={[8, 16]}>
      <Col span='24'>
        
        {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


      </Col>
    </Row>

  </Form>;
}

export default CreateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/FormProvider.js

import React, { useEffect, useState } from 'react';

import {
  Button,
  Checkbox,
  Form,
  notification,
} from 'antd';

import useAxios from 'utils/useAxios';
import UpdateForm from './UpdateForm';
import CreateForm from './CreateForm';
import PubSub from 'pubsub-js';

const FormProvider = ({
  onClose,
  data_raw = {},
  submit_form = (values) => console.log(`submit FormProvider`),
}) => {

  const updateRecord = useAxios({ method: 'PATCH', });
  const createRecord = useAxios({ method: 'POST', path: 'measurement',  });
  const is_updating = Object.keys(data_raw).length > 0;

  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  return <Form.Provider onFormFinish={(name, {values, forms}) => {

    if (is_updating) {
      const { update_form } = forms;
      let updated_values = update_form.getFieldsValue();
      let diffs = {};
      for (let key in updated_values) {
        if (updated_values.hasOwnProperty(key)) {
          if (updated_values[key] !== data_raw[key]) {
            diffs[key] = updated_values[key];
          }
        }      
      }
      console.log(`update diffs: ${JSON.stringify(diffs)}`);
      let values_has_changed = Object.keys(diffs).length > 0;
      if (values_has_changed) {
        updateRecord(
          {
            // url: useUrlBuilder(`bo/bo_marketholiday/${updated_values.id}`),
            path: `measurement/${updated_values.id}`,
            data: diffs
          },

          response => {
            console.log(`sukses updateRecord => ${JSON.stringify(response)}`);
            berhasil(`sukses updateRecord [${JSON.stringify(response)}]`);
            PubSub.publish('<<Update:Record>>', response);
          },

          err => {
            console.log(`gagal updateRecord => ${JSON.stringify(err)}.`);
            gagal(`gagal updateRecord [${JSON.stringify(err)}]`);
          }
        );
      }

    } else {
      const { create_form } = forms;
      let created_values = create_form.getFieldsValue();
      console.log(`created values from onformfinish: ${JSON.stringify(values)} vs getfieldsvalue ${JSON.stringify(created_values)}`);
      createRecord(
        {
          data: created_values
        },

        response => {
          console.log(`sukses createRecord => ${JSON.stringify(response)}`);
          berhasil(`sukses createRecord.`);
          PubSub.publish('<<Create:Record>>', response);
        },

        err => {
          console.log(`gagal createRecord => ${JSON.stringify(err)}.`);
          gagal(`gagal createRecord.`);
        }
      );

    }      

    onClose();

  }}>

    {is_updating ? <UpdateForm initialFormValues={data_raw} /> : <CreateForm />}

    <Form name="fundordertabs-form-body" onFinish={(values) => {}}>
      <Form.Item>
        <Button type='primary' htmlType="submit">Submit</Button>
      </Form.Item>
    </Form>

  </Form.Provider>;

}

export default FormProvider;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/FormWrapper.js

import React, { useEffect, useState } from 'react'
import FormProvider from './FormProvider'

const FormWrapper = ({
    onClose=()=>{},
    data_raw={},
    data_selected={},
}) => {
  return <>    
    <FormProvider 
      data_raw={data_raw} 
      onClose={onClose} />
  </>;
}

export default FormWrapper;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/List.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';
import PubSub from 'pubsub-js';

import useAxios from 'utils/useAxios';
import SimpleTable from 'common/Table/SimpleTable';
import JsonData from 'assets/measurement.json';

function column_sorter(a, b, column) {
  console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`);
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    // return b[column][0].toLowerCase() > a[column][0].toLowerCase();
    return 0;
      
  return b[column] > a[column];
}

const List = ({
  show_update,
  recordTransformer = record => record,
}) => {

  const resource_path = 'measurement';
  const deleteRecord = useAxios({ method: 'DELETE', });
  const [table_data, set_table_data] = useState([]);
  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  const getResourceData = useAxios({ path: resource_path, });  

  const update_table_data = (topic_channel, data) => {
    getResourceData({}, successHandler);
  };

  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  };

  const wrapAsync = () => {
    PubSub.subscribe('<<Create:Record>>', update_table_data);
    PubSub.subscribe('<<Update:Record>>', update_table_data);
    PubSub.subscribe('<<Delete:Record>>', update_table_data);
  }

  useEffect(() => {
    wrapAsync();
    getResourceData({}, successHandler);
  }, []);

  const handleDelete = record => {
    const key = record.key;
    console.log(`deleting ${key} dari record ${JSON.stringify(record)}.`);
    // const table_data_temp = [...table_data].filter(item => item.key !== key);
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    } else {
      console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
      return;
    }

    deleteRecord(
      {
        path: `${resource_path}/${kunci}`,
      },
      response => {
        console.log(`berhasil hapus ${kunci}`);
        PubSub.publish('<<Delete:Record>>', response);
        berhasil('Berhasil', `Berhasil hapus id ${kunci}`);
      },
      err => {
        console.log(`gagal hapus ${kunci}`);
        gagal('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
      }
    );
  }

  const table_header = JsonData.headers.map((column, index) => {

    if (column === "") {

      return {
        title: "Show",
        fixed: 'left',
        width: JsonData.widths.show,
        render: data => <Button onClick={() => {
          console.log(`Show data ${JSON.stringify(data)}`);
          show_update(data);
        }}>Show </Button>,
      };

    } else if (column === "delete") {

      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: JsonData.widths.hapus,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {

      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? JsonData.widths.id : JsonData.widths.normal,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  const modalSelectionHandler = (selections) => {
    // set_modal_bomodule_selected(selections);
    // if (selectionCallback !== undefined) {            
    //   // kirim id dari record, bukan index selection
    //   let id_list = []
    //   selections.forEach(index => {
    //     let ketemu = table_data.find(record => record.key == index)                
    //     // if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
    //     //   id_list .push(ketemu.id + "," + ketemu.id_user);
    //     // else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
    //     //   id_list .push(ketemu.orderno + "," + ketemu.customerno);
    //   })
    //   if (id_list.length > 0) {
    //     selectionCallback(id_list);
    //     console.log(`selection ${id_list}`);
    //   }
    // }
    console.log(`SimpleTable selectCallback: ${selections}, ${typeof(selections)}.`);
  }

	return <>

    <SimpleTable 
      header={table_header}
      body={table_data} 
      selectCallback={modalSelectionHandler} />

  </>;
};

export default List;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/Measurement.js

import React, { useEffect, useState } from 'react';

import {
	Button,
	DatePicker,
	Divider,
	Drawer,
	Input, InputNumber ,
	Modal,
	Popover,
	Select,
	Space,
} from 'antd';
import {
	DesktopOutlined,
	DownOutlined, 
	UserOutlined,
	// HomeOutlined,
	// SettingFilled,
	// SmileOutlined,
	FileExcelOutlined,
	FilePdfOutlined,
	ReloadOutlined,
	ReloadFilled, 
	DeleteOutlined,
	DeleteFilled,
} from '@ant-design/icons';

import ToolbarContext from 'context/ToolbarContext';
import TabPage from 'common/TabPage';

import ReadList from './List';
import FormWrapper from './FormWrapper';

const Measurement = () => {
	const { setToolbar } = React.useContext(ToolbarContext);
	const [lokasiTab, setLokasiTab] = useState('top');
	const [drawerVisible, setDrawerVisible] = useState(false);
	// diisi oleh List wkt 'Show'
	const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

	const show_update = (data) => {
		set_modal_bomodule_content(data);
		setDrawerVisible(true);
	}

	let Toolbar = () => (<Space>
		<h1>Measurement</h1>
		<Button type="primary" 
			onClick = {				
				() => {
					set_modal_bomodule_content({});
					setDrawerVisible(true);
				}
			}>Create new</Button>
		{/* <Button type="default" disabled onClick={generateBlotter2}>Blotter Subscription</Button> */}
		{/* <Popover placement="bottom" title={<span>Pilih nasabah dan tanggal Blotter subscription</span>} content={Blotter_Popup} trigger="click"> */}
		{/* <Button disabled type="primary">Blotter Subscription</Button> */}
		{/* </Popover> */}			
	</Space>);

	useEffect(function() {
		setToolbar(<Toolbar />)
	}, []);

	return <>
		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'Create',
						icon: <DesktopOutlined />,
						component: <FormWrapper />
					},
					{
						title: 'Read',
						icon: <DesktopOutlined />,
						component: <ReadList show_update={show_update} />
					},
				]
			} />

		<Drawer
      title="Add Record"
      placement='right'      
      onClose={() => setDrawerVisible(false)}
      visible={drawerVisible}
      width={800}
      // closable={false}
      >

			<FormWrapper
				data_raw={modal_bomodule_content}
				onClose={() => setDrawerVisible(false)}
				/>

		</Drawer>
	
	</>;
};

export default Measurement;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/Modal.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, 
  Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';


const BoComponentModalDefaultContent = ({
  data_selected,
  data_raw
}) => (<>
      Daftar terselect default isi-selected: {JSON.stringify(data_selected)}
      <hr />
      Isi show (data raw): {JSON.stringify(data_raw)}
  </>
);

const BoComponentModal = ({
  Content,
  modal_title,
  modal_bomodule_visible,
  modal_bomodule_selected,
  modal_bomodule_content,
  set_modal_bomodule,
}) => (<Modal visible={modal_bomodule_visible} title={modal_title}
    onOk={(e) => set_modal_bomodule(false)}
    onCancel={(e) => set_modal_bomodule(false)}
  >

    {<Content
      data_selected={modal_bomodule_selected}
      data_raw={modal_bomodule_content}
    />}

  </Modal>
);

export default {
  BoComponentModalDefaultContent,
  BoComponentModal,
};


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Measurement/UpdateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
import moment from 'moment';

const UpdateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit UpdateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  useEffect(() => {
    const {
      date,
      ...bukan_tanggal
    } = initialFormValues

    form_konek_provider.setFieldsValue({
      date: moment(date),
      ...bukan_tanggal
    });

  }, [initialFormValues]);

  return <Form name='update_form' 
      // size='small'
      form={form_konek_provider}
      className='update_form'
    >
      <Row gutter={[8, 16]}>
        <Col span='24'>
          
          {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


        </Col>
      </Row>

    </Form>;
}

export default UpdateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/News/CreateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
// import moment from 'moment';

const CreateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit CreateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  // useEffect(() => {
  // }, [initialFormValues]);

  return <Form name='create_form' 
      // size='small'
      form={form_konek_provider}
      className='create_form'
    >
    <Row gutter={[8, 16]}>
      <Col span='24'>
        
        {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='title' label="Title">
  <Input />
</Form.Item>



<Form.Item name='link' label="Link">
  <Input />
</Form.Item>



<Form.Item name='summary' label="Summary">
  <Input />
</Form.Item>



<Form.Item name='content' label="Content">
  <Input />
</Form.Item>



<Form.Item name='tags' label="Tags">
  <Input />
</Form.Item>



<Form.Item name='images' label="Images">
  <Input />
</Form.Item>


      </Col>
    </Row>

  </Form>;
}

export default CreateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/News/FormProvider.js

import React, { useEffect, useState } from 'react';

import {
  Button,
  Checkbox,
  Form,
  notification,
} from 'antd';

import useAxios from 'utils/useAxios';
import UpdateForm from './UpdateForm';
import CreateForm from './CreateForm';
import PubSub from 'pubsub-js';

const FormProvider = ({
  onClose,
  data_raw = {},
  submit_form = (values) => console.log(`submit FormProvider`),
}) => {

  const updateRecord = useAxios({ method: 'PATCH', });
  const createRecord = useAxios({ method: 'POST', path: 'news',  });
  const is_updating = Object.keys(data_raw).length > 0;

  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  return <Form.Provider onFormFinish={(name, {values, forms}) => {

    if (is_updating) {
      const { update_form } = forms;
      let updated_values = update_form.getFieldsValue();
      let diffs = {};
      for (let key in updated_values) {
        if (updated_values.hasOwnProperty(key)) {
          if (updated_values[key] !== data_raw[key]) {
            diffs[key] = updated_values[key];
          }
        }      
      }
      console.log(`update diffs: ${JSON.stringify(diffs)}`);
      let values_has_changed = Object.keys(diffs).length > 0;
      if (values_has_changed) {
        updateRecord(
          {
            // url: useUrlBuilder(`bo/bo_marketholiday/${updated_values.id}`),
            path: `news/${updated_values.id}`,
            data: diffs
          },

          response => {
            console.log(`sukses updateRecord => ${JSON.stringify(response)}`);
            berhasil(`sukses updateRecord [${JSON.stringify(response)}]`);
            PubSub.publish('<<Update:Record>>', response);
          },

          err => {
            console.log(`gagal updateRecord => ${JSON.stringify(err)}.`);
            gagal(`gagal updateRecord [${JSON.stringify(err)}]`);
          }
        );
      }

    } else {
      const { create_form } = forms;
      let created_values = create_form.getFieldsValue();
      console.log(`created values from onformfinish: ${JSON.stringify(values)} vs getfieldsvalue ${JSON.stringify(created_values)}`);
      createRecord(
        {
          data: created_values
        },

        response => {
          console.log(`sukses createRecord => ${JSON.stringify(response)}`);
          berhasil(`sukses createRecord.`);
          PubSub.publish('<<Create:Record>>', response);
        },

        err => {
          console.log(`gagal createRecord => ${JSON.stringify(err)}.`);
          gagal(`gagal createRecord.`);
        }
      );

    }      

    onClose();

  }}>

    {is_updating ? <UpdateForm initialFormValues={data_raw} /> : <CreateForm />}

    <Form name="fundordertabs-form-body" onFinish={(values) => {}}>
      <Form.Item>
        <Button type='primary' htmlType="submit">Submit</Button>
      </Form.Item>
    </Form>

  </Form.Provider>;

}

export default FormProvider;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/News/FormWrapper.js

import React, { useEffect, useState } from 'react'
import FormProvider from './FormProvider'

const FormWrapper = ({
    onClose=()=>{},
    data_raw={},
    data_selected={},
}) => {
  return <>    
    <FormProvider 
      data_raw={data_raw} 
      onClose={onClose} />
  </>;
}

export default FormWrapper;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/News/List.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';
import PubSub from 'pubsub-js';

import useAxios from 'utils/useAxios';
import SimpleTable from 'common/Table/SimpleTable';
import JsonData from 'assets/news.json';

function column_sorter(a, b, column) {
  console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`);
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    // return b[column][0].toLowerCase() > a[column][0].toLowerCase();
    return 0;
      
  return b[column] > a[column];
}

const List = ({
  show_update,
  recordTransformer = record => record,
}) => {

  const resource_path = 'news';
  const deleteRecord = useAxios({ method: 'DELETE', });
  const [table_data, set_table_data] = useState([]);
  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  const getResourceData = useAxios({ path: resource_path, });  

  const update_table_data = (topic_channel, data) => {
    getResourceData({}, successHandler);
  };

  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  };

  const wrapAsync = () => {
    PubSub.subscribe('<<Create:Record>>', update_table_data);
    PubSub.subscribe('<<Update:Record>>', update_table_data);
    PubSub.subscribe('<<Delete:Record>>', update_table_data);
  }

  useEffect(() => {
    wrapAsync();
    getResourceData({}, successHandler);
  }, []);

  const handleDelete = record => {
    const key = record.key;
    console.log(`deleting ${key} dari record ${JSON.stringify(record)}.`);
    // const table_data_temp = [...table_data].filter(item => item.key !== key);
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    } else {
      console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
      return;
    }

    deleteRecord(
      {
        path: `${resource_path}/${kunci}`,
      },
      response => {
        console.log(`berhasil hapus ${kunci}`);
        PubSub.publish('<<Delete:Record>>', response);
        berhasil('Berhasil', `Berhasil hapus id ${kunci}`);
      },
      err => {
        console.log(`gagal hapus ${kunci}`);
        gagal('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
      }
    );
  }

  const table_header = JsonData.headers.map((column, index) => {

    if (column === "") {

      return {
        title: "Show",
        fixed: 'left',
        width: JsonData.widths.show,
        render: data => <Button onClick={() => {
          console.log(`Show data ${JSON.stringify(data)}`);
          show_update(data);
        }}>Show </Button>,
      };

    } else if (column === "delete") {

      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: JsonData.widths.hapus,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {

      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? JsonData.widths.id : JsonData.widths.normal,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  const modalSelectionHandler = (selections) => {
    // set_modal_bomodule_selected(selections);
    // if (selectionCallback !== undefined) {            
    //   // kirim id dari record, bukan index selection
    //   let id_list = []
    //   selections.forEach(index => {
    //     let ketemu = table_data.find(record => record.key == index)                
    //     // if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
    //     //   id_list .push(ketemu.id + "," + ketemu.id_user);
    //     // else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
    //     //   id_list .push(ketemu.orderno + "," + ketemu.customerno);
    //   })
    //   if (id_list.length > 0) {
    //     selectionCallback(id_list);
    //     console.log(`selection ${id_list}`);
    //   }
    // }
    console.log(`SimpleTable selectCallback: ${selections}, ${typeof(selections)}.`);
  }

	return <>

    <SimpleTable 
      header={table_header}
      body={table_data}
      selectCallback={modalSelectionHandler} />

  </>;
};

export default List;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/News/Modal.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, 
  Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';


const BoComponentModalDefaultContent = ({
  data_selected,
  data_raw
}) => (<>
      Daftar terselect default isi-selected: {JSON.stringify(data_selected)}
      <hr />
      Isi show (data raw): {JSON.stringify(data_raw)}
  </>
);

const BoComponentModal = ({
  Content,
  modal_title,
  modal_bomodule_visible,
  modal_bomodule_selected,
  modal_bomodule_content,
  set_modal_bomodule,
}) => (<Modal visible={modal_bomodule_visible} title={modal_title}
    onOk={(e) => set_modal_bomodule(false)}
    onCancel={(e) => set_modal_bomodule(false)}
  >

    {<Content
      data_selected={modal_bomodule_selected}
      data_raw={modal_bomodule_content}
    />}

  </Modal>
);

export default {
  BoComponentModalDefaultContent,
  BoComponentModal,
};


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/News/News.js

import React, { useEffect, useState } from 'react';

import {
	Button,
	DatePicker,
	Divider,
	Drawer,
	Input, InputNumber ,
	Modal,
	Popover,
	Select,
	Space,
} from 'antd';
import {
	DesktopOutlined,
	DownOutlined, 
	UserOutlined,
	// HomeOutlined,
	// SettingFilled,
	// SmileOutlined,
	FileExcelOutlined,
	FilePdfOutlined,
	ReloadOutlined,
	ReloadFilled, 
	DeleteOutlined,
	DeleteFilled,
} from '@ant-design/icons';

import ToolbarContext from 'context/ToolbarContext';
import TabPage from 'common/TabPage';
import GridMap from '../Dashboard/GridMap';
import ReadList from './List';
import FormWrapper from './FormWrapper';

const News = () => {
	const { setToolbar } = React.useContext(ToolbarContext);
	const [lokasiTab, setLokasiTab] = useState('top');
	const [drawerVisible, setDrawerVisible] = useState(false);
	// diisi oleh List wkt 'Show'
	const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

	const show_update = (data) => {
		set_modal_bomodule_content(data);
		setDrawerVisible(true);
	}

	let Toolbar = () => (<Space>
		<h1>News</h1>
		<Button type="primary" 
			onClick = {				
				() => {
					set_modal_bomodule_content({});
					setDrawerVisible(true);
				}
			}>Create new</Button>
		{/* <Button type="default" disabled onClick={generateBlotter2}>Blotter Subscription</Button> */}
		{/* <Popover placement="bottom" title={<span>Pilih nasabah dan tanggal Blotter subscription</span>} content={Blotter_Popup} trigger="click"> */}
		{/* <Button disabled type="primary">Blotter Subscription</Button> */}
		{/* </Popover> */}			
	</Space>);

	useEffect(function() {
		setToolbar(<Toolbar />)
	}, []);

	return <>
		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'GridMap',
						icon: <DesktopOutlined />,
						component: <GridMap />
					},
				]
			} 
		/>

		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'Create',
						icon: <DesktopOutlined />,
						component: <FormWrapper />
					},
					{
						title: 'Read',
						icon: <DesktopOutlined />,
						component: <ReadList show_update={show_update} />
					},
				]
			} />

		<Drawer
      title="Add Record"
      placement='right'      
      onClose={() => setDrawerVisible(false)}
      visible={drawerVisible}
      width={800}
      // closable={false}
      >

			<FormWrapper
				data_raw={modal_bomodule_content}
				onClose={() => setDrawerVisible(false)}
				/>

		</Drawer>
	
	</>;
};

export default News;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/News/UpdateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
import moment from 'moment';

const UpdateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit UpdateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  useEffect(() => {
    const {
      date,
      ...bukan_tanggal
    } = initialFormValues

    form_konek_provider.setFieldsValue({
      date: moment(date),
      ...bukan_tanggal
    });

  }, [initialFormValues]);

  return <Form name='update_form' 
      // size='small'
      form={form_konek_provider}
      className='update_form'
    >
      <Row gutter={[8, 16]}>
        <Col span='24'>
          
          {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='title' label="Title">
  <Input />
</Form.Item>



<Form.Item name='link' label="Link">
  <Input />
</Form.Item>



<Form.Item name='summary' label="Summary">
  <Input />
</Form.Item>



<Form.Item name='content' label="Content">
  <Input />
</Form.Item>



<Form.Item name='tags' label="Tags">
  <Input />
</Form.Item>



<Form.Item name='images' label="Images">
  <Input />
</Form.Item>


        </Col>
      </Row>

    </Form>;
}

export default UpdateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Point/CreateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
// import moment from 'moment';

const CreateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit CreateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  // useEffect(() => {
  // }, [initialFormValues]);

  return <Form name='create_form' 
      // size='small'
      form={form_konek_provider}
      className='create_form'
    >
    <Row gutter={[8, 16]}>
      <Col span='24'>
        
        {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


      </Col>
    </Row>

  </Form>;
}

export default CreateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Point/FormProvider.js

import React, { useEffect, useState } from 'react';

import {
  Button,
  Checkbox,
  Form,
  notification,
} from 'antd';

import useAxios from 'utils/useAxios';
import UpdateForm from './UpdateForm';
import CreateForm from './CreateForm';
import PubSub from 'pubsub-js';

const FormProvider = ({
  onClose,
  data_raw = {},
  submit_form = (values) => console.log(`submit FormProvider`),
}) => {

  const updateRecord = useAxios({ method: 'PATCH', });
  const createRecord = useAxios({ method: 'POST', path: 'point',  });
  const is_updating = Object.keys(data_raw).length > 0;

  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  return <Form.Provider onFormFinish={(name, {values, forms}) => {

    if (is_updating) {
      const { update_form } = forms;
      let updated_values = update_form.getFieldsValue();
      let diffs = {};
      for (let key in updated_values) {
        if (updated_values.hasOwnProperty(key)) {
          if (updated_values[key] !== data_raw[key]) {
            diffs[key] = updated_values[key];
          }
        }      
      }
      console.log(`update diffs: ${JSON.stringify(diffs)}`);
      let values_has_changed = Object.keys(diffs).length > 0;
      if (values_has_changed) {
        updateRecord(
          {
            // url: useUrlBuilder(`bo/bo_marketholiday/${updated_values.id}`),
            path: `point/${updated_values.id}`,
            data: diffs
          },

          response => {
            console.log(`sukses updateRecord => ${JSON.stringify(response)}`);
            berhasil(`sukses updateRecord [${JSON.stringify(response)}]`);
            PubSub.publish('<<Update:Record>>', response);
          },

          err => {
            console.log(`gagal updateRecord => ${JSON.stringify(err)}.`);
            gagal(`gagal updateRecord [${JSON.stringify(err)}]`);
          }
        );
      }

    } else {
      const { create_form } = forms;
      let created_values = create_form.getFieldsValue();
      console.log(`created values from onformfinish: ${JSON.stringify(values)} vs getfieldsvalue ${JSON.stringify(created_values)}`);
      createRecord(
        {
          data: created_values
        },

        response => {
          console.log(`sukses createRecord => ${JSON.stringify(response)}`);
          berhasil(`sukses createRecord.`);
          PubSub.publish('<<Create:Record>>', response);
        },

        err => {
          console.log(`gagal createRecord => ${JSON.stringify(err)}.`);
          gagal(`gagal createRecord.`);
        }
      );

    }      

    onClose();

  }}>

    {is_updating ? <UpdateForm initialFormValues={data_raw} /> : <CreateForm />}

    <Form name="fundordertabs-form-body" onFinish={(values) => {}}>
      <Form.Item>
        <Button type='primary' htmlType="submit">Submit</Button>
      </Form.Item>
    </Form>

  </Form.Provider>;

}

export default FormProvider;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Point/FormWrapper.js

import React, { useEffect, useState } from 'react'
import FormProvider from './FormProvider'

const FormWrapper = ({
    onClose=()=>{},
    data_raw={},
    data_selected={},
}) => {
  return <>    
    <FormProvider 
      data_raw={data_raw} 
      onClose={onClose} />
  </>;
}

export default FormWrapper;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Point/List.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';
import PubSub from 'pubsub-js';

import useAxios from 'utils/useAxios';
import SimpleTable from 'common/Table/SimpleTable';
import JsonData from 'assets/point.json';

function column_sorter(a, b, column) {
  console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`);
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    // return b[column][0].toLowerCase() > a[column][0].toLowerCase();
    return 0;
      
  return b[column] > a[column];
}

const List = ({
  show_update,
  recordTransformer = record => record,
}) => {

  const resource_path = 'point';
  const deleteRecord = useAxios({ method: 'DELETE', });
  const [table_data, set_table_data] = useState([]);
  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  const getResourceData = useAxios({ path: resource_path, });  

  const update_table_data = (topic_channel, data) => {
    getResourceData({}, successHandler);
  };

  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  };

  const wrapAsync = () => {
    PubSub.subscribe('<<Create:Record>>', update_table_data);
    PubSub.subscribe('<<Update:Record>>', update_table_data);
    PubSub.subscribe('<<Delete:Record>>', update_table_data);
  }

  useEffect(() => {
    wrapAsync();
    getResourceData({}, successHandler);
  }, []);

  const handleDelete = record => {
    const key = record.key;
    console.log(`deleting ${key} dari record ${JSON.stringify(record)}.`);
    // const table_data_temp = [...table_data].filter(item => item.key !== key);
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    } else {
      console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
      return;
    }

    deleteRecord(
      {
        path: `${resource_path}/${kunci}`,
      },
      response => {
        console.log(`berhasil hapus ${kunci}`);
        PubSub.publish('<<Delete:Record>>', response);
        berhasil('Berhasil', `Berhasil hapus id ${kunci}`);
      },
      err => {
        console.log(`gagal hapus ${kunci}`);
        gagal('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
      }
    );
  }

  const table_header = JsonData.headers.map((column, index) => {

    if (column === "") {

      return {
        title: "Show",
        fixed: 'left',
        width: JsonData.widths.show,
        render: data => <Button onClick={() => {
          console.log(`Show data ${JSON.stringify(data)}`);
          show_update(data);
        }}>Show </Button>,
      };

    } else if (column === "delete") {

      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: JsonData.widths.hapus,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {

      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? JsonData.widths.id : JsonData.widths.normal,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  const modalSelectionHandler = (selections) => {
    // set_modal_bomodule_selected(selections);
    // if (selectionCallback !== undefined) {            
    //   // kirim id dari record, bukan index selection
    //   let id_list = []
    //   selections.forEach(index => {
    //     let ketemu = table_data.find(record => record.key == index)                
    //     // if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
    //     //   id_list .push(ketemu.id + "," + ketemu.id_user);
    //     // else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
    //     //   id_list .push(ketemu.orderno + "," + ketemu.customerno);
    //   })
    //   if (id_list.length > 0) {
    //     selectionCallback(id_list);
    //     console.log(`selection ${id_list}`);
    //   }
    // }
    console.log(`SimpleTable selectCallback: ${selections}, ${typeof(selections)}.`);
  }

	return <>

    <SimpleTable 
      header={table_header}
      body={table_data} 
      selectCallback={modalSelectionHandler} />

  </>;
};

export default List;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Point/Modal.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, 
  Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';


const BoComponentModalDefaultContent = ({
  data_selected,
  data_raw
}) => (<>
      Daftar terselect default isi-selected: {JSON.stringify(data_selected)}
      <hr />
      Isi show (data raw): {JSON.stringify(data_raw)}
  </>
);

const BoComponentModal = ({
  Content,
  modal_title,
  modal_bomodule_visible,
  modal_bomodule_selected,
  modal_bomodule_content,
  set_modal_bomodule,
}) => (<Modal visible={modal_bomodule_visible} title={modal_title}
    onOk={(e) => set_modal_bomodule(false)}
    onCancel={(e) => set_modal_bomodule(false)}
  >

    {<Content
      data_selected={modal_bomodule_selected}
      data_raw={modal_bomodule_content}
    />}

  </Modal>
);

export default {
  BoComponentModalDefaultContent,
  BoComponentModal,
};


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Point/Point.js

import React, { useEffect, useState } from 'react';

import {
	Button,
	DatePicker,
	Divider,
	Drawer,
	Input, InputNumber ,
	Modal,
	Popover,
	Select,
	Space,
} from 'antd';
import {
	DesktopOutlined,
	DownOutlined, 
	UserOutlined,
	// HomeOutlined,
	// SettingFilled,
	// SmileOutlined,
	FileExcelOutlined,
	FilePdfOutlined,
	ReloadOutlined,
	ReloadFilled, 
	DeleteOutlined,
	DeleteFilled,
} from '@ant-design/icons';

import ToolbarContext from 'context/ToolbarContext';
import TabPage from 'common/TabPage';

import ReadList from './List';
import FormWrapper from './FormWrapper';

const Point = () => {
	const { setToolbar } = React.useContext(ToolbarContext);
	const [lokasiTab, setLokasiTab] = useState('top');
	const [drawerVisible, setDrawerVisible] = useState(false);
	// diisi oleh List wkt 'Show'
	const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

	const show_update = (data) => {
		set_modal_bomodule_content(data);
		setDrawerVisible(true);
	}

	let Toolbar = () => (<Space>
		<h1>Point</h1>
		<Button type="primary" 
			onClick = {				
				() => {
					set_modal_bomodule_content({});
					setDrawerVisible(true);
				}
			}>Create new</Button>
		{/* <Button type="default" disabled onClick={generateBlotter2}>Blotter Subscription</Button> */}
		{/* <Popover placement="bottom" title={<span>Pilih nasabah dan tanggal Blotter subscription</span>} content={Blotter_Popup} trigger="click"> */}
		{/* <Button disabled type="primary">Blotter Subscription</Button> */}
		{/* </Popover> */}			
	</Space>);

	useEffect(function() {
		setToolbar(<Toolbar />)
	}, []);

	return <>
		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'Create',
						icon: <DesktopOutlined />,
						component: <FormWrapper />
					},
					{
						title: 'Read',
						icon: <DesktopOutlined />,
						component: <ReadList show_update={show_update} />
					},
				]
			} />

		<Drawer
      title="Add Record"
      placement='right'      
      onClose={() => setDrawerVisible(false)}
      visible={drawerVisible}
      width={800}
      // closable={false}
      >

			<FormWrapper
				data_raw={modal_bomodule_content}
				onClose={() => setDrawerVisible(false)}
				/>

		</Drawer>
	
	</>;
};

export default Point;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Point/UpdateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
import moment from 'moment';

const UpdateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit UpdateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  useEffect(() => {
    const {
      date,
      ...bukan_tanggal
    } = initialFormValues

    form_konek_provider.setFieldsValue({
      date: moment(date),
      ...bukan_tanggal
    });

  }, [initialFormValues]);

  return <Form name='update_form' 
      // size='small'
      form={form_konek_provider}
      className='update_form'
    >
      <Row gutter={[8, 16]}>
        <Col span='24'>
          
          {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


        </Col>
      </Row>

    </Form>;
}

export default UpdateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Room/CreateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
// import moment from 'moment';

const CreateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit CreateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  // useEffect(() => {
  // }, [initialFormValues]);

  return <Form name='create_form' 
      // size='small'
      form={form_konek_provider}
      className='create_form'
    >
    <Row gutter={[8, 16]}>
      <Col span='24'>
        
        {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


      </Col>
    </Row>

  </Form>;
}

export default CreateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Room/FormProvider.js

import React, { useEffect, useState } from 'react';

import {
  Button,
  Checkbox,
  Form,
  notification,
} from 'antd';

import useAxios from 'utils/useAxios';
import UpdateForm from './UpdateForm';
import CreateForm from './CreateForm';
import PubSub from 'pubsub-js';

const FormProvider = ({
  onClose,
  data_raw = {},
  submit_form = (values) => console.log(`submit FormProvider`),
}) => {

  const updateRecord = useAxios({ method: 'PATCH', });
  const createRecord = useAxios({ method: 'POST', path: 'room',  });
  const is_updating = Object.keys(data_raw).length > 0;

  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  return <Form.Provider onFormFinish={(name, {values, forms}) => {

    if (is_updating) {
      const { update_form } = forms;
      let updated_values = update_form.getFieldsValue();
      let diffs = {};
      for (let key in updated_values) {
        if (updated_values.hasOwnProperty(key)) {
          if (updated_values[key] !== data_raw[key]) {
            diffs[key] = updated_values[key];
          }
        }      
      }
      console.log(`update diffs: ${JSON.stringify(diffs)}`);
      let values_has_changed = Object.keys(diffs).length > 0;
      if (values_has_changed) {
        updateRecord(
          {
            // url: useUrlBuilder(`bo/bo_marketholiday/${updated_values.id}`),
            path: `room/${updated_values.id}`,
            data: diffs
          },

          response => {
            console.log(`sukses updateRecord => ${JSON.stringify(response)}`);
            berhasil(`sukses updateRecord [${JSON.stringify(response)}]`);
            PubSub.publish('<<Update:Record>>', response);
          },

          err => {
            console.log(`gagal updateRecord => ${JSON.stringify(err)}.`);
            gagal(`gagal updateRecord [${JSON.stringify(err)}]`);
          }
        );
      }

    } else {
      const { create_form } = forms;
      let created_values = create_form.getFieldsValue();
      console.log(`created values from onformfinish: ${JSON.stringify(values)} vs getfieldsvalue ${JSON.stringify(created_values)}`);
      createRecord(
        {
          data: created_values
        },

        response => {
          console.log(`sukses createRecord => ${JSON.stringify(response)}`);
          berhasil(`sukses createRecord.`);
          PubSub.publish('<<Create:Record>>', response);
        },

        err => {
          console.log(`gagal createRecord => ${JSON.stringify(err)}.`);
          gagal(`gagal createRecord.`);
        }
      );

    }      

    onClose();

  }}>

    {is_updating ? <UpdateForm initialFormValues={data_raw} /> : <CreateForm />}

    <Form name="fundordertabs-form-body" onFinish={(values) => {}}>
      <Form.Item>
        <Button type='primary' htmlType="submit">Submit</Button>
      </Form.Item>
    </Form>

  </Form.Provider>;

}

export default FormProvider;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Room/FormWrapper.js

import React, { useEffect, useState } from 'react'
import FormProvider from './FormProvider'

const FormWrapper = ({
    onClose=()=>{},
    data_raw={},
    data_selected={},
}) => {
  return <>    
    <FormProvider 
      data_raw={data_raw} 
      onClose={onClose} />
  </>;
}

export default FormWrapper;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Room/List.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';
import PubSub from 'pubsub-js';

import useAxios from 'utils/useAxios';
import SimpleTable from 'common/Table/SimpleTable';
import JsonData from 'assets/room.json';

function column_sorter(a, b, column) {
  console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`);
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    // return b[column][0].toLowerCase() > a[column][0].toLowerCase();
    return 0;
      
  return b[column] > a[column];
}

const List = ({
  show_update,
  recordTransformer = record => record,
}) => {

  const resource_path = 'room';
  const deleteRecord = useAxios({ method: 'DELETE', });
  const [table_data, set_table_data] = useState([]);
  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  const getResourceData = useAxios({ path: resource_path, });  

  const update_table_data = (topic_channel, data) => {
    getResourceData({}, successHandler);
  };

  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  };

  const wrapAsync = () => {
    PubSub.subscribe('<<Create:Record>>', update_table_data);
    PubSub.subscribe('<<Update:Record>>', update_table_data);
    PubSub.subscribe('<<Delete:Record>>', update_table_data);
  }

  useEffect(() => {
    wrapAsync();
    getResourceData({}, successHandler);
  }, []);

  const handleDelete = record => {
    const key = record.key;
    console.log(`deleting ${key} dari record ${JSON.stringify(record)}.`);
    // const table_data_temp = [...table_data].filter(item => item.key !== key);
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    } else {
      console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
      return;
    }

    deleteRecord(
      {
        path: `${resource_path}/${kunci}`,
      },
      response => {
        console.log(`berhasil hapus ${kunci}`);
        PubSub.publish('<<Delete:Record>>', response);
        berhasil('Berhasil', `Berhasil hapus id ${kunci}`);
      },
      err => {
        console.log(`gagal hapus ${kunci}`);
        gagal('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
      }
    );
  }

  const table_header = JsonData.headers.map((column, index) => {

    if (column === "") {

      return {
        title: "Show",
        fixed: 'left',
        width: JsonData.widths.show,
        render: data => <Button onClick={() => {
          console.log(`Show data ${JSON.stringify(data)}`);
          show_update(data);
        }}>Show </Button>,
      };

    } else if (column === "delete") {

      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: JsonData.widths.hapus,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {

      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? JsonData.widths.id : JsonData.widths.normal,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  const modalSelectionHandler = (selections) => {
    // set_modal_bomodule_selected(selections);
    // if (selectionCallback !== undefined) {            
    //   // kirim id dari record, bukan index selection
    //   let id_list = []
    //   selections.forEach(index => {
    //     let ketemu = table_data.find(record => record.key == index)                
    //     // if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
    //     //   id_list .push(ketemu.id + "," + ketemu.id_user);
    //     // else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
    //     //   id_list .push(ketemu.orderno + "," + ketemu.customerno);
    //   })
    //   if (id_list.length > 0) {
    //     selectionCallback(id_list);
    //     console.log(`selection ${id_list}`);
    //   }
    // }
    console.log(`SimpleTable selectCallback: ${selections}, ${typeof(selections)}.`);
  }

	return <>

    <SimpleTable 
      header={table_header}
      body={table_data} 
      selectCallback={modalSelectionHandler} />

  </>;
};

export default List;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Room/Modal.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, 
  Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';


const BoComponentModalDefaultContent = ({
  data_selected,
  data_raw
}) => (<>
      Daftar terselect default isi-selected: {JSON.stringify(data_selected)}
      <hr />
      Isi show (data raw): {JSON.stringify(data_raw)}
  </>
);

const BoComponentModal = ({
  Content,
  modal_title,
  modal_bomodule_visible,
  modal_bomodule_selected,
  modal_bomodule_content,
  set_modal_bomodule,
}) => (<Modal visible={modal_bomodule_visible} title={modal_title}
    onOk={(e) => set_modal_bomodule(false)}
    onCancel={(e) => set_modal_bomodule(false)}
  >

    {<Content
      data_selected={modal_bomodule_selected}
      data_raw={modal_bomodule_content}
    />}

  </Modal>
);

export default {
  BoComponentModalDefaultContent,
  BoComponentModal,
};


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Room/Room.js

import React, { useEffect, useState } from 'react';

import {
	Button,
	DatePicker,
	Divider,
	Drawer,
	Input, InputNumber ,
	Modal,
	Popover,
	Select,
	Space,
} from 'antd';
import {
	DesktopOutlined,
	DownOutlined, 
	UserOutlined,
	// HomeOutlined,
	// SettingFilled,
	// SmileOutlined,
	FileExcelOutlined,
	FilePdfOutlined,
	ReloadOutlined,
	ReloadFilled, 
	DeleteOutlined,
	DeleteFilled,
} from '@ant-design/icons';

import ToolbarContext from 'context/ToolbarContext';
import TabPage from 'common/TabPage';

import ReadList from './List';
import FormWrapper from './FormWrapper';

const Room = () => {
	const { setToolbar } = React.useContext(ToolbarContext);
	const [lokasiTab, setLokasiTab] = useState('top');
	const [drawerVisible, setDrawerVisible] = useState(false);
	// diisi oleh List wkt 'Show'
	const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

	const show_update = (data) => {
		set_modal_bomodule_content(data);
		setDrawerVisible(true);
	}

	let Toolbar = () => (<Space>
		<h1>Room</h1>
		<Button type="primary" 
			onClick = {				
				() => {
					set_modal_bomodule_content({});
					setDrawerVisible(true);
				}
			}>Create new</Button>
		{/* <Button type="default" disabled onClick={generateBlotter2}>Blotter Subscription</Button> */}
		{/* <Popover placement="bottom" title={<span>Pilih nasabah dan tanggal Blotter subscription</span>} content={Blotter_Popup} trigger="click"> */}
		{/* <Button disabled type="primary">Blotter Subscription</Button> */}
		{/* </Popover> */}			
	</Space>);

	useEffect(function() {
		setToolbar(<Toolbar />)
	}, []);

	return <>
		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'Create',
						icon: <DesktopOutlined />,
						component: <FormWrapper />
					},
					{
						title: 'Read',
						icon: <DesktopOutlined />,
						component: <ReadList show_update={show_update} />
					},
				]
			} />

		<Drawer
      title="Add Record"
      placement='right'      
      onClose={() => setDrawerVisible(false)}
      visible={drawerVisible}
      width={800}
      // closable={false}
      >

			<FormWrapper
				data_raw={modal_bomodule_content}
				onClose={() => setDrawerVisible(false)}
				/>

		</Drawer>
	
	</>;
};

export default Room;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Room/UpdateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
import moment from 'moment';

const UpdateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit UpdateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  useEffect(() => {
    const {
      date,
      ...bukan_tanggal
    } = initialFormValues

    form_konek_provider.setFieldsValue({
      date: moment(date),
      ...bukan_tanggal
    });

  }, [initialFormValues]);

  return <Form name='update_form' 
      // size='small'
      form={form_konek_provider}
      className='update_form'
    >
      <Row gutter={[8, 16]}>
        <Col span='24'>
          
          {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


        </Col>
      </Row>

    </Form>;
}

export default UpdateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/CreateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
// import moment from 'moment';

const CreateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit CreateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  // useEffect(() => {
  // }, [initialFormValues]);

  return <Form name='create_form' 
      // size='small'
      form={form_konek_provider}
      className='create_form'
    >
    <Row gutter={[8, 16]}>
      <Col span='24'>
        
        {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


        {/* <Form.Item name='id' label="Id">
          <InputNumber />
        </Form.Item> */}



        <Form.Item name='smart_building' label="Smart_Building">
          <Input />
        </Form.Item>



        <Form.Item name='sensor_id' label="Sensor_Id">
          <Input />
        </Form.Item>



        <Form.Item name='min_value' label="Min_Value">
          <InputNumber />
        </Form.Item>



        <Form.Item name='max_value' label="Max_Value">
          <InputNumber />
        </Form.Item>



        <Form.Item name='yellow' label="Yellow">
          <InputNumber />
        </Form.Item>



        <Form.Item name='red' label="Red">
          <InputNumber />
        </Form.Item>



        <Form.Item name='interval' label="Interval">
          <InputNumber />
        </Form.Item>



        <Form.Item name='stopper' label='Stopper'><Select>
        {data.map((item, index) => {
        return <Select.Option key={index} value={item}>{item}</Select.Option>
        })}
        </Select>
        </Form.Item> 



        <Form.Item name='stop' label="Stop">
          <InputNumber />
        </Form.Item>


      </Col>
    </Row>

  </Form>;
}

export default CreateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/FormProvider.js

import React, { useEffect, useState } from 'react';

import {
  Button,
  Checkbox,
  Form,
  notification,
} from 'antd';

import useAxios from 'utils/useAxios';
import UpdateForm from './UpdateForm';
import CreateForm from './CreateForm';
import PubSub from 'pubsub-js';

const FormProvider = ({
  onClose,
  data_raw = {},
  submit_form = (values) => console.log(`submit FormProvider`),
}) => {

  const updateRecord = useAxios({ method: 'PATCH', });
  const createRecord = useAxios({ method: 'POST', path: 'sensor',  });
  const is_updating = Object.keys(data_raw).length > 0;

  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  return <Form.Provider onFormFinish={(name, {values, forms}) => {

    if (is_updating) {
      const { update_form } = forms;
      let updated_values = update_form.getFieldsValue();
      let diffs = {};
      for (let key in updated_values) {
        if (updated_values.hasOwnProperty(key)) {
          if (updated_values[key] !== data_raw[key]) {
            diffs[key] = updated_values[key];
          }
        }      
      }
      console.log(`update diffs: ${JSON.stringify(diffs)}`);
      let values_has_changed = Object.keys(diffs).length > 0;
      if (values_has_changed) {
        updateRecord(
          {
            // url: useUrlBuilder(`bo/bo_marketholiday/${updated_values.id}`),
            path: `sensor/${updated_values.id}`,
            data: diffs
          },

          response => {
            console.log(`sukses updateRecord => ${JSON.stringify(response)}`);
            berhasil(`sukses updateRecord [${JSON.stringify(response)}]`);
            PubSub.publish('<<Update:Record>>', response);
          },

          err => {
            console.log(`gagal updateRecord => ${JSON.stringify(err)}.`);
            gagal(`gagal updateRecord [${JSON.stringify(err)}]`);
          }
        );
      }

    } else {
      const { create_form } = forms;
      let created_values = create_form.getFieldsValue();
      console.log(`created values from onformfinish: ${JSON.stringify(values)} vs getfieldsvalue ${JSON.stringify(created_values)}`);
      createRecord(
        {
          data: created_values
        },

        response => {
          console.log(`sukses createRecord => ${JSON.stringify(response)}`);
          berhasil(`sukses createRecord.`);
          PubSub.publish('<<Create:Record>>', response);
        },

        err => {
          console.log(`gagal createRecord => ${JSON.stringify(err)}.`);
          gagal(`gagal createRecord.`);
        }
      );

    }

    onClose();

  }}>

    {is_updating ? <UpdateForm initialFormValues={data_raw} /> : <CreateForm />}

    <Form name="fundordertabs-form-body" onFinish={(values) => {}}>
      <Form.Item>
        <Button type='primary' htmlType="submit">Submit</Button>
      </Form.Item>
    </Form>

  </Form.Provider>;

}

export default FormProvider;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/FormWrapper.js

import React, { useEffect, useState } from 'react'
import FormProvider from './FormProvider'

const FormWrapper = ({
    onClose=()=>{},
    data_raw={},
    data_selected={},
}) => {
  return <>    
    <FormProvider 
      data_raw={data_raw} 
      onClose={onClose} />
  </>;
}

export default FormWrapper;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/List.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';
import PubSub from 'pubsub-js';

import useAxios from 'utils/useAxios';
import SimpleTable from 'common/Table/SimpleTable';
import JsonData from 'assets/sensor.json';

function column_sorter(a, b, column) {
  console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`);
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    // return b[column][0].toLowerCase() > a[column][0].toLowerCase();
    return 0;
      
  return b[column] > a[column];
}

const List = ({
  show_update=()=>{},
  recordTransformer = record => record,
}) => {

  const resource_path = 'sensor';
  const deleteRecord = useAxios({ method: 'DELETE', });
  const [table_data, set_table_data] = useState([]);
  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  const getResourceData = useAxios({ path: resource_path, });

  const update_table_data = (topic_channel, data) => {
    getResourceData({}, successHandler);
  };

  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  };

  const wrapAsync = () => {
    PubSub.subscribe('<<Create:Record>>', update_table_data);
    PubSub.subscribe('<<Update:Record>>', update_table_data);
    PubSub.subscribe('<<Delete:Record>>', update_table_data);
  }

  useEffect(() => {
    wrapAsync();
    getResourceData({}, successHandler);
  }, []);

  const handleDelete = record => {
    const key = record.key;
    console.log(`deleting ${key} dari record ${JSON.stringify(record)}.`);
    // const table_data_temp = [...table_data].filter(item => item.key !== key);
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    } else {
      console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
      return;
    }

    deleteRecord(
      {
        path: `${resource_path}/${kunci}`,
      },
      response => {
        console.log(`berhasil hapus ${kunci}`);
        PubSub.publish('<<Delete:Record>>', response);
        berhasil('Berhasil', `Berhasil hapus id ${kunci}`);
      },
      err => {
        console.log(`gagal hapus ${kunci}`);
        gagal('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
      }
    );
  }

  const table_header = JsonData.headers.map((column, index) => {

    if (column === "") {

      return {
        title: "Show",
        fixed: 'left',
        width: JsonData.widths.show,
        render: data => <Button onClick={() => {
          console.log(`Show data ${JSON.stringify(data)}`);
          show_update(data);
        }}>Show </Button>,
      };

    } else if (column === "delete") {

      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: JsonData.widths.hapus,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {

      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? JsonData.widths.id : JsonData.widths.normal,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  const modalSelectionHandler = (selections) => {
    // set_modal_bomodule_selected(selections);
    // if (selectionCallback !== undefined) {            
    //   // kirim id dari record, bukan index selection
    //   let id_list = []
    //   selections.forEach(index => {
    //     let ketemu = table_data.find(record => record.key == index)                
    //     // if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
    //     //   id_list .push(ketemu.id + "," + ketemu.id_user);
    //     // else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
    //     //   id_list .push(ketemu.orderno + "," + ketemu.customerno);
    //   })
    //   if (id_list.length > 0) {
    //     selectionCallback(id_list);
    //     console.log(`selection ${id_list}`);
    //   }
    // }
    console.log(`SimpleTable selectCallback: ${selections}, ${typeof(selections)}.`);
  }

	return <>

    <SimpleTable 
      header={table_header}
      body={table_data} 
      selectCallback={modalSelectionHandler} />

  </>;
};

export default List;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/Modal.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, 
  Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';


const BoComponentModalDefaultContent = ({
  data_selected,
  data_raw
}) => (<>
      Daftar terselect default isi-selected: {JSON.stringify(data_selected)}
      <hr />
      Isi show (data raw): {JSON.stringify(data_raw)}
  </>
);

const BoComponentModal = ({
  Content,
  modal_title,
  modal_bomodule_visible,
  modal_bomodule_selected,
  modal_bomodule_content,
  set_modal_bomodule,
}) => (<Modal visible={modal_bomodule_visible} title={modal_title}
    onOk={(e) => set_modal_bomodule(false)}
    onCancel={(e) => set_modal_bomodule(false)}
  >

    {<Content
      data_selected={modal_bomodule_selected}
      data_raw={modal_bomodule_content}
    />}

  </Modal>
);

export default {
  BoComponentModalDefaultContent,
  BoComponentModal,
};


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/Sensor.js

import React, { useEffect, useState } from 'react';

import {
	Button,
	DatePicker,
	Divider,
	Drawer,
	Input, InputNumber ,
	Modal,
	Popover,
	Select,
	Space,
} from 'antd';
import {
	DesktopOutlined,
	DownOutlined, 
	UserOutlined,
	// HomeOutlined,
	// SettingFilled,
	// SmileOutlined,
	FileExcelOutlined,
	FilePdfOutlined,
	ReloadOutlined,
	ReloadFilled, 
	DeleteOutlined,
	DeleteFilled,
} from '@ant-design/icons';

import ToolbarContext from 'context/ToolbarContext';
import TabPage from 'common/TabPage';

import ReadList from './List';
import FormWrapper from './FormWrapper';

const Sensor = () => {
	const { setToolbar } = React.useContext(ToolbarContext);
	const [lokasiTab, setLokasiTab] = useState('top');
	const [drawerVisible, setDrawerVisible] = useState(false);
	// diisi oleh List wkt 'Show'
	const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

	const show_update = (data) => {
		set_modal_bomodule_content(data);
		setDrawerVisible(true);
	}

	let Toolbar = () => (<Space>
		<h1>Sensor</h1>
		<Button type="primary" 
			onClick = {				
				() => {
					set_modal_bomodule_content({});
					setDrawerVisible(true);
				}
			}>Create new</Button>
		{/* <Button type="default" disabled onClick={generateBlotter2}>Blotter Subscription</Button> */}
		{/* <Popover placement="bottom" title={<span>Pilih nasabah dan tanggal Blotter subscription</span>} content={Blotter_Popup} trigger="click"> */}
		{/* <Button disabled type="primary">Blotter Subscription</Button> */}
		{/* </Popover> */}			
	</Space>);

	useEffect(function() {
		setToolbar(<Toolbar />)
	}, []);

	return <>
		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'Create',
						icon: <DesktopOutlined />,
						component: <FormWrapper />
					},
					{
						title: 'Read',
						icon: <DesktopOutlined />,
						component: <ReadList show_update={show_update} />
					},
				]
			} />

		<Drawer
      title="Add Record"
      placement='right'      
      onClose={() => setDrawerVisible(false)}
      visible={drawerVisible}
      width={800}
      // closable={false}
      >

			<FormWrapper
				data_raw={modal_bomodule_content}
				onClose={() => setDrawerVisible(false)}
				/>

		</Drawer>
	
	</>;
};

export default Sensor;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/Sensor/UpdateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
import moment from 'moment';

const UpdateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit UpdateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  useEffect(() => {
    const {
      date,
      ...bukan_tanggal
    } = initialFormValues

    form_konek_provider.setFieldsValue({
      date: moment(date),
      ...bukan_tanggal
    });

  }, [initialFormValues]);

  return <Form name='update_form' 
      // size='small'
      form={form_konek_provider}
      className='update_form'
    >
      <Row gutter={[8, 16]}>
        <Col span='24'>
          
          {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='smart_building' label="Smart_Building">
  <Input />
</Form.Item>



<Form.Item name='sensor_id' label="Sensor_Id">
  <Input />
</Form.Item>



<Form.Item name='min_value' label="Min_Value">
  <InputNumber />
</Form.Item>



<Form.Item name='max_value' label="Max_Value">
  <InputNumber />
</Form.Item>



<Form.Item name='yellow' label="Yellow">
  <InputNumber />
</Form.Item>



<Form.Item name='red' label="Red">
  <InputNumber />
</Form.Item>



<Form.Item name='interval' label="Interval">
  <InputNumber />
</Form.Item>



<Form.Item name='stopper' label="Stopper">
  <Input />
</Form.Item>



<Form.Item name='stop' label="Stop">
  <InputNumber />
</Form.Item>


        </Col>
      </Row>

    </Form>;
}

export default UpdateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/System/CreateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
// import moment from 'moment';

const CreateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit CreateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  // useEffect(() => {
  // }, [initialFormValues]);

  return <Form name='create_form' 
      // size='small'
      form={form_konek_provider}
      className='create_form'
    >
    <Row gutter={[8, 16]}>
      <Col span='24'>
        
        {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


      </Col>
    </Row>

  </Form>;
}

export default CreateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/System/FormProvider.js

import React, { useEffect, useState } from 'react';

import {
  Button,
  Checkbox,
  Form,
  notification,
} from 'antd';

import useAxios from 'utils/useAxios';
import UpdateForm from './UpdateForm';
import CreateForm from './CreateForm';
import PubSub from 'pubsub-js';

const FormProvider = ({
  onClose,
  data_raw = {},
  submit_form = (values) => console.log(`submit FormProvider`),
}) => {

  const updateRecord = useAxios({ method: 'PATCH', });
  const createRecord = useAxios({ method: 'POST', path: 'system',  });
  const is_updating = Object.keys(data_raw).length > 0;

  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  return <Form.Provider onFormFinish={(name, {values, forms}) => {

    if (is_updating) {
      const { update_form } = forms;
      let updated_values = update_form.getFieldsValue();
      let diffs = {};
      for (let key in updated_values) {
        if (updated_values.hasOwnProperty(key)) {
          if (updated_values[key] !== data_raw[key]) {
            diffs[key] = updated_values[key];
          }
        }      
      }
      console.log(`update diffs: ${JSON.stringify(diffs)}`);
      let values_has_changed = Object.keys(diffs).length > 0;
      if (values_has_changed) {
        updateRecord(
          {
            // url: useUrlBuilder(`bo/bo_marketholiday/${updated_values.id}`),
            path: `system/${updated_values.id}`,
            data: diffs
          },

          response => {
            console.log(`sukses updateRecord => ${JSON.stringify(response)}`);
            berhasil(`sukses updateRecord [${JSON.stringify(response)}]`);
            PubSub.publish('<<Update:Record>>', response);
          },

          err => {
            console.log(`gagal updateRecord => ${JSON.stringify(err)}.`);
            gagal(`gagal updateRecord [${JSON.stringify(err)}]`);
          }
        );
      }

    } else {
      const { create_form } = forms;
      let created_values = create_form.getFieldsValue();
      console.log(`created values from onformfinish: ${JSON.stringify(values)} vs getfieldsvalue ${JSON.stringify(created_values)}`);
      createRecord(
        {
          data: created_values
        },

        response => {
          console.log(`sukses createRecord => ${JSON.stringify(response)}`);
          berhasil(`sukses createRecord.`);
          PubSub.publish('<<Create:Record>>', response);
        },

        err => {
          console.log(`gagal createRecord => ${JSON.stringify(err)}.`);
          gagal(`gagal createRecord.`);
        }
      );

    }      

    onClose();

  }}>

    {is_updating ? <UpdateForm initialFormValues={data_raw} /> : <CreateForm />}

    <Form name="fundordertabs-form-body" onFinish={(values) => {}}>
      <Form.Item>
        <Button type='primary' htmlType="submit">Submit</Button>
      </Form.Item>
    </Form>

  </Form.Provider>;

}

export default FormProvider;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/System/FormWrapper.js

import React, { useEffect, useState } from 'react'
import FormProvider from './FormProvider'

const FormWrapper = ({
    onClose=()=>{},
    data_raw={},
    data_selected={},
}) => {
  return <>    
    <FormProvider 
      data_raw={data_raw} 
      onClose={onClose} />
  </>;
}

export default FormWrapper;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/System/List.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';

import {
  // DownOutlined, 
  // UserOutlined,
  // ReloadFilled, 
  // DeleteOutlined,
  // HomeOutlined,
  // SettingFilled,
  // SmileOutlined,
  
  FileAddOutlined,
  FileExcelOutlined,
  FilePdfOutlined,
  ReloadOutlined,
  DeleteFilled,
} from '@ant-design/icons';
import PubSub from 'pubsub-js';

import useAxios from 'utils/useAxios';
import SimpleTable from 'common/Table/SimpleTable';
import JsonData from 'assets/system.json';

function column_sorter(a, b, column) {
  console.log(`table sorting: ${column}, pertama ${a[column]}, kedua ${b[column]}.`);
  // return b[column] > a[column]
  // return b[column].localeCompare(a[column])
  // return a[column] - b[column]
  // return a[column] > b[column]
  if (b[column] === null || b[column] === '') // descend
    return -1;
  else if (a[column] === null || a[column] === '')
    return 1;
  else if (typeof(b[column]) === "string")
    // return b[column][0].toLowerCase() > a[column][0].toLowerCase();
    return 0;
      
  return b[column] > a[column];
}

const List = ({
  show_update,
  recordTransformer = record => record,
}) => {

  const resource_path = 'system';
  const deleteRecord = useAxios({ method: 'DELETE', });
  const [table_data, set_table_data] = useState([]);
  const gagal = pesan => notification['error']({
    message: "Error",
    description: pesan,
  });
  const berhasil = pesan => notification['success']({
    message: "Success",
    description: pesan,
  });

  const getResourceData = useAxios({ path: resource_path, });  

  const update_table_data = (topic_channel, data) => {
    getResourceData({}, successHandler);
  };

  const successHandler = response => {
    let data = response.result
      .map((record, index) => {
        record.key = index;
        return recordTransformer(record);
      });

    set_table_data(data);
  };

  const wrapAsync = () => {
    PubSub.subscribe('<<Create:Record>>', update_table_data);
    PubSub.subscribe('<<Update:Record>>', update_table_data);
    PubSub.subscribe('<<Delete:Record>>', update_table_data);
  }

  useEffect(() => {
    wrapAsync();
    getResourceData({}, successHandler);
  }, []);

  const handleDelete = record => {
    const key = record.key;
    console.log(`deleting ${key} dari record ${JSON.stringify(record)}.`);
    // const table_data_temp = [...table_data].filter(item => item.key !== key);
    let kunci;
    if (record.hasOwnProperty('id')) {
      kunci = record.id;
    } else {
      console.log(`Did not know how to identify this record to delete: ${JSON.stringify(record)}`);
      return;
    }

    deleteRecord(
      {
        path: `${resource_path}/${kunci}`,
      },
      response => {
        console.log(`berhasil hapus ${kunci}`);
        PubSub.publish('<<Delete:Record>>', response);
        berhasil('Berhasil', `Berhasil hapus id ${kunci}`);
      },
      err => {
        console.log(`gagal hapus ${kunci}`);
        gagal('Gagal hapus...', `Tidak berhasil hapus ${kunci}. Silahkan coba lagi. ${JSON.stringify(err)}`);
      }
    );
  }

  const table_header = JsonData.headers.map((column, index) => {

    if (column === "") {

      return {
        title: "Show",
        fixed: 'left',
        width: JsonData.widths.show,
        render: data => <Button onClick={() => {
          console.log(`Show data ${JSON.stringify(data)}`);
          show_update(data);
        }}>Show </Button>,
      };

    } else if (column === "delete") {

      return {
        title: 'Hapus',
        dataIndex: 'operation',
        fixed: 'right',
        width: JsonData.widths.hapus,
        render: (text, record) => table_data.length >= 1 ? (
          <Popconfirm title={`Yakin hapus ${record.id}?`} onConfirm={() => handleDelete(record)}>
            <DeleteFilled style={{ fontSize: '20px', color: '#f25', textAlign: 'center' }} />
          </Popconfirm>
        ) : null,
      };

    } else {

      let noFilter = {
        // kolom biasa, dataIndex sama dg nama kolom
        title: column,
        fixed: index == 1 ? 'left' : null,
        width: index == 1 ? JsonData.widths.id : JsonData.widths.normal,
        dataIndex: (column !== "" && column !== "cb") ? column : '0',
        // defaultSortOrder: 'descend',
        sortDirections: ['descend', 'ascend', 'descend'],
        sorter: (a, b) => column_sorter(a, b, column),
      }

      // let filteredColumn = column.replace('filter#', '')
      // let withFilter = {
      //   // kolom biasa, dataIndex sama dg nama kolom
      //   title: filteredColumn,
      //   fixed: index == 1 ? 'left' : null,
      //   width: index == 1 ? 75 : 150,
      //   dataIndex: (filteredColumn !== "" && filteredColumn !== "cb") ? filteredColumn : '0',
      //   // defaultSortOrder: 'descend',
      //   sortDirections: ['descend', 'ascend', 'descend'],
      //   sorter: (a, b) => column_sorter(a, b, filteredColumn),

      //   filterDropdown: (<div className="custom-filter-dropdown">
      //     <Input
      //       placeholder="Cari nilai..."
      //       value={filterText[index]}
      //       onChange={e => {
      //         let newText = [...filterText]
      //         newText[index] = e.target.value
      //         setFilterText(newText)
      //       }}
      //       onPressEnter={() => filterSearch(filteredColumn, index)}
      //     />
      //     <Button type="primary" onClick={() => filterSearch(filteredColumn, index)}>Cari</Button>
      //   </div>),
      //   filterDropdownVisible: filterVisible[index],
      //   onFilterDropdownVisibleChange: visible => setColumnVisible(visible, index),
      // };

      // let filterCondition = column.startsWith('filter#');
      // return filterCondition ? withFilter : noFilter;

      return noFilter;
    }

  });

  const modalSelectionHandler = (selections) => {
    // set_modal_bomodule_selected(selections);
    // if (selectionCallback !== undefined) {            
    //   // kirim id dari record, bukan index selection
    //   let id_list = []
    //   selections.forEach(index => {
    //     let ketemu = table_data.find(record => record.key == index)                
    //     // if (ketemu.hasOwnProperty('id') && ketemu.hasOwnProperty('id_user'))
    //     //   id_list .push(ketemu.id + "," + ketemu.id_user);
    //     // else if (ketemu.hasOwnProperty('orderno') && ketemu.hasOwnProperty('customerno'))
    //     //   id_list .push(ketemu.orderno + "," + ketemu.customerno);
    //   })
    //   if (id_list.length > 0) {
    //     selectionCallback(id_list);
    //     console.log(`selection ${id_list}`);
    //   }
    // }
    console.log(`SimpleTable selectCallback: ${selections}, ${typeof(selections)}.`);
  }

	return <>

    <SimpleTable 
      header={table_header}
      body={table_data} 
      selectCallback={modalSelectionHandler} />

  </>;
};

export default List;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/System/Modal.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Drawer, 
  Dropdown, 
  Input,
  Menu, 
  Modal,
  Popconfirm,
  Table,

  notification,
} from 'antd';


const BoComponentModalDefaultContent = ({
  data_selected,
  data_raw
}) => (<>
      Daftar terselect default isi-selected: {JSON.stringify(data_selected)}
      <hr />
      Isi show (data raw): {JSON.stringify(data_raw)}
  </>
);

const BoComponentModal = ({
  Content,
  modal_title,
  modal_bomodule_visible,
  modal_bomodule_selected,
  modal_bomodule_content,
  set_modal_bomodule,
}) => (<Modal visible={modal_bomodule_visible} title={modal_title}
    onOk={(e) => set_modal_bomodule(false)}
    onCancel={(e) => set_modal_bomodule(false)}
  >

    {<Content
      data_selected={modal_bomodule_selected}
      data_raw={modal_bomodule_content}
    />}

  </Modal>
);

export default {
  BoComponentModalDefaultContent,
  BoComponentModal,
};


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/System/System.js

import React, { useEffect, useState } from 'react';

import {
	Button,
	DatePicker,
	Divider,
	Drawer,
	Input, InputNumber ,
	Modal,
	Popover,
	Select,
	Space,
} from 'antd';
import {
	DesktopOutlined,
	DownOutlined, 
	UserOutlined,
	// HomeOutlined,
	// SettingFilled,
	// SmileOutlined,
	FileExcelOutlined,
	FilePdfOutlined,
	ReloadOutlined,
	ReloadFilled, 
	DeleteOutlined,
	DeleteFilled,
} from '@ant-design/icons';

import ToolbarContext from 'context/ToolbarContext';
import TabPage from 'common/TabPage';

import ReadList from './List';
import FormWrapper from './FormWrapper';

const System = () => {
	const { setToolbar } = React.useContext(ToolbarContext);
	const [lokasiTab, setLokasiTab] = useState('top');
	const [drawerVisible, setDrawerVisible] = useState(false);
	// diisi oleh List wkt 'Show'
	const [modal_bomodule_content, set_modal_bomodule_content] = useState({});

	const show_update = (data) => {
		set_modal_bomodule_content(data);
		setDrawerVisible(true);
	}

	let Toolbar = () => (<Space>
		<h1>System</h1>
		<Button type="primary" 
			onClick = {				
				() => {
					set_modal_bomodule_content({});
					setDrawerVisible(true);
				}
			}>Create new</Button>
		{/* <Button type="default" disabled onClick={generateBlotter2}>Blotter Subscription</Button> */}
		{/* <Popover placement="bottom" title={<span>Pilih nasabah dan tanggal Blotter subscription</span>} content={Blotter_Popup} trigger="click"> */}
		{/* <Button disabled type="primary">Blotter Subscription</Button> */}
		{/* </Popover> */}			
	</Space>);

	useEffect(function() {
		setToolbar(<Toolbar />)
	}, []);

	return <>
		<TabPage 
			tabpos={lokasiTab}
			tabs_data={
				[
					{
						title: 'Create',
						icon: <DesktopOutlined />,
						component: <FormWrapper />
					},
					{
						title: 'Read',
						icon: <DesktopOutlined />,
						component: <ReadList show_update={show_update} />
					},
				]
			} />

		<Drawer
      title="Add Record"
      placement='right'      
      onClose={() => setDrawerVisible(false)}
      visible={drawerVisible}
      width={800}
      // closable={false}
      >

			<FormWrapper
				data_raw={modal_bomodule_content}
				onClose={() => setDrawerVisible(false)}
				/>

		</Drawer>
	
	</>;
};

export default System;


--#

--% C:/tmp/hapus/nda01/react-antd/components/modules/System/UpdateForm.js

import React, { useEffect, useState } from 'react';

import { 
  Button, 
  Col, 
  DatePicker,
  Form, 
  Input, 
  InputNumber,
  Modal,
  Radio,
  Row,
  Select,
  Switch,
} from 'antd';
import moment from 'moment';

const UpdateForm = ({
  initialFormValues = {},
  formSubmit = () => console.log(`submit UpdateForm`),
}) => {
  
  const [form_konek_provider] = Form.useForm();

  useEffect(() => {
    const {
      date,
      ...bukan_tanggal
    } = initialFormValues

    form_konek_provider.setFieldsValue({
      date: moment(date),
      ...bukan_tanggal
    });

  }, [initialFormValues]);

  return <Form name='update_form' 
      // size='small'
      form={form_konek_provider}
      className='update_form'
    >
      <Row gutter={[8, 16]}>
        <Col span='24'>
          
          {/* <Form.Item name='id' label="ID">
          <Input disabled />
        </Form.Item> */}


<Form.Item name='id' label="Id">
  <InputNumber />
</Form.Item>



<Form.Item name='name' label="Name">
  <Input />
</Form.Item>


        </Col>
      </Row>

    </Form>;
}

export default UpdateForm;


--#

--% C:/tmp/hapus/nda01/react-antd/components/Route/AuthenticatedRoute.js
import React, { useContext } from 'react';
import {
  Route,
  Redirect
} from 'react-router-dom';

import SessionContext from '../context/SessionContext';

export default ({
  name,
  path,
  exact = false,
  component: Component,
  // roles = [],
}) => {

  const session = useContext(SessionContext);

  return (
    <Route
      path={path}
      name={name}
      exact={exact}
      render={(props) => 
        // session.authenticated
        session.token
          ? (<Component {...props} />)
          : (<Redirect
            to={{
              pathname: '/login',
              state: { from: props.location },
            }}
          />)
      }
    />
  );
};



--#

--% C:/tmp/hapus/nda01/react-antd/components/Route/Routes.js

import Dashboard from 'modules/Dashboard/Dashboard';

import Sensor from 'modules/Sensor/Sensor';
import SensorList from 'modules/Sensor/List';
import System from 'modules/System/System';
import Measurement from 'modules/Measurement/Measurement';
import Equipment from 'modules/Equipment/Equipment';
import Room from 'modules/Room/Room';
import Floor from 'modules/Floor/Floor';
import Location from 'modules/Location/Location';
import Point from 'modules/Point/Point';
import Building from 'modules/Building/Building';
import News from 'modules/News/News';
import NewsList from 'modules/News/List';

export default [

  { 
    name: 'Dashboard', 
    path: '/dashboard', 
    icon: 'group', 
    exact: true, 
    component: Dashboard, 
    roles: [], 
  },


  { 
    name: 'Sensor', 
    path: '/sensor', 
    icon: 'group', 
    exact: true, 
    component: Sensor, 
    roles: [], 
  },

  { 
    name: 'Sensor List', 
    path: '/sensor-list', 
    icon: 'group', 
    exact: true, 
    component: SensorList, 
    roles: [], 
  },

  { 
    name: 'System', 
    path: '/system', 
    icon: 'group', 
    exact: true, 
    component: System, 
    roles: [], 
  },


  { 
    name: 'Measurement', 
    path: '/measurement', 
    icon: 'group', 
    exact: true, 
    component: Measurement, 
    roles: [], 
  },


  { 
    name: 'Equipment', 
    path: '/equipment', 
    icon: 'group', 
    exact: true, 
    component: Equipment, 
    roles: [], 
  },


  { 
    name: 'Room', 
    path: '/room', 
    icon: 'group', 
    exact: true, 
    component: Room, 
    roles: [], 
  },


  { 
    name: 'Floor', 
    path: '/floor', 
    icon: 'group', 
    exact: true, 
    component: Floor, 
    roles: [], 
  },


  { 
    name: 'Location', 
    path: '/location', 
    icon: 'group', 
    exact: true, 
    component: Location, 
    roles: [], 
  },


  { 
    name: 'Point', 
    path: '/point', 
    icon: 'group', 
    exact: true, 
    component: Point, 
    roles: [], 
  },


  { 
    name: 'Building', 
    path: '/building', 
    icon: 'group', 
    exact: true, 
    component: Building, 
    roles: [], 
  },


  { 
    name: 'News', 
    path: '/news', 
    icon: 'group', 
    exact: true, 
    component: News, 
    roles: [], 
  },

  { 
    name: 'News List', 
    path: '/news-list', 
    icon: 'group', 
    exact: true, 
    component: NewsList, 
    roles: [], 
  },


];


--#

--% C:/tmp/hapus/nda01/react-antd/components/Setting/Settings_Popup.js
import React, { useEffect, useReducer, useState } from 'react';
import {
  Button,
  Collapse,
  DatePicker,
  Divider,
  Drawer,
  List,
  Modal,
  Popover,
  Select,
  Space,
} from 'antd';
import { ExclamationCircleOutlined } from '@ant-design/icons';
// import localForage from 'localforage';
// import { forage_cache_get, } from '@/utils/forage_cache';
// import DateAdder from '#c/Primitives/DateAdder/DateAdder';

const Settings_Popup = (props) => {
  
  // const [kycList, setKycList] = useState([]);

  // const sortByFirstName = (records) => {
  //   // return records.sort((a,b) => b.split('|')[1] - a.split('|')[1])
  //   records.sort();
  //   return records;
  // }

  // const skycTransformer = item => `${item.firstname.toLowerCase()} ${item.middlename.toLowerCase()} ${item.lastname.toLowerCase()} | ${item.email} | ${item.id_user} `;

  // const skycSetter = (items) => {
  //   let sorted = sortByFirstName(items)
  //   let unique = Array.from(new Set(sorted))
  //   setKycList(unique)
  // }

  // useEffect(() => {
  //   forage_cache_get(
  //     's_kyc', 
  //     skycTransformer,
  //     skycSetter
  //   );
  // }, []);

  function onChange(value, dateString) {
    console.log('Selected Time: ', value)
    // Formatted Selected Time:  2020-08-15 20:36:33
    console.log('Formatted Selected Time: ', dateString)
  }

  function onOk(value) {
    console.log('onOk: ', JSON.stringify(value)) // iso string
  }

  let Popuper = () => (<>
    <Select showSearch placeholder="Pilih nasabah" style={{ width: 450, marginBottom:'10px' }}>
      {/* {Array.from(new Set(kycList)).map( (item, index) => {
        let [fullname, email, uid] = item.split('|')
        return <Select.Option key={index} value={email.trim()}>{fullname} &lt;{email.trim()}&gt;, {uid.trim()}</Select.Option>
      })} */}
    </Select>
    <Divider dashed orientation='center'>Kirim Email Mutual Fund Activity</Divider>
    
    <DatePicker showTime onChange={onChange} onOk={onOk} size='small' style={{ marginTop:'10px'}}/>

    <Button type='primary' style={{ marginLeft: '20px', marginTop:'10px'}}>Set</Button>
  </>);

  let Container = () => (<Collapse accordion defaultActiveKey={['4']} style={{ width: 500 }}>

    {/* <Collapse.Panel header="Add date" key="4">
      <DateAdder />
    </Collapse.Panel> */}

    <Collapse.Panel header="Kirim email manual dan otomatis" key="1">
      <Popuper />
    </Collapse.Panel>

    <Collapse.Panel header="New BO User" key="2">
      <h1>Create BO User here</h1>
    </Collapse.Panel>

    {/* <Collapse.Panel header="Local Cache" key="3">
      <List
        size="small"
        bordered
        dataSource={kycList}
        renderItem={item => <List.Item>{item}</List.Item>}
        header={<div><Button onClick={() => {
          localForage.removeItem('bo/s_kyc/list')
          localForage.removeItem('bo/s_kyc/list/config')
          setKycList([])
        }}>Clear</Button></div>}
        footer={<div>Users cache used for selection</div>}
      >

      </List>
    </Collapse.Panel> */}

  </Collapse>);

  return <Container />;
}

export default Settings_Popup;



--#

--% C:/tmp/hapus/nda01/react-antd/utils/authUtils.js
import config from '#/config';

let refreshLoop;

/**
 * 
 * @returns seconds untuk setTimeout (perlu *1000 dulu utk jd ms)
 */
function getNextRefreshTime() {
  const expTime = Number(localStorage.getItem(config.authentication.storage.expiry_token));
  const nextRefreshTime = expTime - new Date().getTime() / 1000 - 1;
  console.log(`getNextRefreshTime:
    NEXT refresh: ${nextRefreshTime}
  `);
  return nextRefreshTime;
}

async function doRefreshToken(refresh_token = "") {
  try {
    if (!refresh_token) {
      refresh_token = localStorage.getItem(config.authentication.storage.refesh_token);
      if (!refresh_token) {
        throw new Error("Unauthenticated");
      }
    }
    const response = await fetch(config.serverPath(config.authentication.path.refresh), {
      headers: {
        "Content-Type": "application/json",
      },
      method: "POST",
      body: JSON.stringify({
        refresh_token,
      }),
    });
    const { data } = await response.json();
    console.log(`
      refresh token get the following data from server:
      ${JSON.stringify(data)}
    `);
    // alert(`
    //   refresh token get the following data from server:
    //   ${JSON.stringify(data)}
    // `);
    const { accessToken, refreshToken, expTime } = data;
    if (!refreshToken) {
      throw new Error("Failed to refresh token");
    }
    localStorage.setItem(config.authentication.storage.access_token, accessToken);
    localStorage.setItem(config.authentication.storage.refesh_token, refreshToken);
    localStorage.setItem(config.authentication.storage.expiry_token, expTime);

    registerRefreshJob();

    return true;
  } catch (e) {
    clearTimeout(refreshLoop);
    localStorage.clear();
    window.location = config.authentication.path.after_token_expired;
    return;
  }
}

export function registerRefreshJob() {
  const nextRefreshTime = getNextRefreshTime();

  if (nextRefreshTime < 0 && !!refreshLoop) {
    clearTimeout(refreshLoop);
    localStorage.clear();
    window.location = config.authentication.path.after_token_expired;
  }

  refreshLoop = setTimeout(async () => {
    await doRefreshToken();
  }, nextRefreshTime * 1000);
}

--#

--% C:/tmp/hapus/nda01/react-antd/utils/loader.css
/* https://stackoverflow.com/questions/60018959/blur-the-whole-page-except-a-div */

.container {
  width: 100%;
  height: 100%;
  min-height: 400px;
  top: 0;
  left: 0;
  z-index: 10000;
  position: absolute;
  background-color: black;
  opacity: 0.5;
}

.subcontainer {
  filter: blur(0.5rem);
}

.center {
  width: 100px;
  height: 100px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  /* background: #f00; */
  /* filter: blur(0); */
  /* filter: none; */
}

--#

--% C:/tmp/hapus/nda01/react-antd/utils/loader.js
import React, { useEffect, useState } from "react";
import Loader from "react-loader-spinner";
import "react-loader-spinner/dist/loader/css/react-spinner-loader.css";

import "./loader.css";

/**
 * https://github.com/mhnpd/react-loader-spinner
 * Audio
 * BallTriangle
 * Bars
 * Circles
 * Grid
 * Hearts
 * Oval
 * Puff
 * Rings
 * TailSpin
 * ThreeDots
 * 
 */

const MyLoader = (props) => {
  return (
    <div className="container">
      <Loader 
        className="center"
        type={props.type} color="#00BFFF" height={100} width={100} timeout={30000}/>
    </div>
  );
}

export default MyLoader;

--#

--% C:/tmp/hapus/nda01/react-antd/utils/requester.js
import config from '../config';

const network_timeout = 60 * 1000;

// let refreshLoop;

class Requester {

  constructor(prefixUrl, isPrivate = true) {
    this.url = config.serverPath(prefixUrl);
    this.isPrivate = isPrivate;
    this.request = {};
  }

  getAccessToken() {
    const token = localStorage.getItem(config.authentication.storage.access_token);
    if (!token) {
      throw new Error("Calling private service need access token");
    }
    return `Bearer ${token}`;
  }

  handleResponse(res) {
    if (res.status !== 200) {
      if (res.status === 401) {
        localStorage.clear();
        // window.location = "/app/login";
        window.location = config.authentication.path.after_token_expired;
        return;
      }
      return res.json();
    }
    if (res.headers.get("content-type")) {
      const contentType = res.headers.get("content-type").toLowerCase();

      if (contentType.includes("application/json")) {
        return res.json();
      }
    } else {
      return res.json();
    }
  }

  connect() {
    return new Promise((resolve, reject) => {
      // this.refreshTokenIfNecessary()
      //   .then(() => {
      let headers = {
        "Content-Type": "application/json",
      };
      if (this.isPrivate) {
        headers["Authentication"] = this.getAccessToken();
      }
      this.request.headers = headers;
      resolve(
        Promise.race([
          fetch(this.url, this.request)
            .then((response) => {
              return this.handleResponse(response);
            })
            .then((response) => {
              if (!response) {
                throw new Error({
                  response: "nok",
                  error: "Tidak dapat terhubung ke server.",
                });
              }
              if (response.response !== "ok") {
                if ((response.error || "").includes("jwt")) {
                  localStorage.clear();
                  // window.location = "/app/login";
                  window.location = config.authentication.path.after_token_expired;
                }
                throw response;
              }
              return response;
            })
            .catch((err) => {
              if (!process.env.REACT_APP_ENV) console.log(err);
              throw err;
            }),
          new Promise((_, reject) =>
            setTimeout(
              () =>
                reject({
                  response: "nok",
                  error: "Tidak dapat terhubung ke server.",
                }),
              network_timeout
            )
          ),
        ])
      );
      // })
      // .catch((err) => reject(err));
    });
  }

  get(data) {
    let query = [];
    this.request.method = "GET";
    for (let item in data) {
      if (data[item]) {
        query.push(item + "=" + encodeURIComponent(data[item]));
      }
    }
    this.url += "?" + query.join("&");
    return this.connect();
  }

  post(data) {
    this.request.method = "POST";
    this.request.body = JSON.stringify(data);
    return this.connect();
  }

  upload(data, isPrivate = true) {
    let headers = {};

    if (isPrivate) {
      headers.Authentication = this.getAccessToken();
    }

    return fetch(this.url, {
      method: "POST",
      headers,
      body: data,
    });
  }


  /**
   * 
   * @param {*} prefix 
   * @param {*} options 
   * @returns 
   * 
   * const upload = _req.createService("/file/upload");
   * const dataRaw = await upload.upload(formData);
   * const { data } = await dataRaw.json();
   */
  static createService(prefix, options) {
    return new Requester(prefix, options);
  }
}

export default Requester;

--#

--% C:/tmp/hapus/nda01/react-antd/utils/useAxios.js
import React, { useState, useContext } from 'react';

import axios from 'axios';
import config from '#/config';

const initialState = {
  isFetching: false,
  isError: false,
  // statusCode: null,
  // code: null,
  // message: null,
  // details: null,
  data: null,
}

export default ({
  method = 'GET',
  path,
  headers = {},
}) => {

  const [state, setState] = useState(initialState);

  if (path === undefined) path = '';
  const url = `${config.server()}/${path}`;

  const originalArgs = {
    method,
    url,
    data: null,
    params: {},
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
      ...headers,
    }
  }

  const sender = (newArgs={}, successCb=undefined, errorCb=undefined) => {    

    let updatedArgs = {
      ...originalArgs,
      ...newArgs,
    };
    if (newArgs.hasOwnProperty('path')) {
      updatedArgs['url'] = `${config.server()}/${newArgs["path"]}`;
    }
    console.log(`useAxios: sending request to => ${url}.`);

    setState({
      ...initialState,
      isFetching: true,
    });

    axios(updatedArgs)
    .then(response => {
      if (response.data) {
        
        setState(prevState => ({
          ...prevState,
          data: response.data,
        }));

        if (successCb) {
          successCb(response.data);
        }

      }
    })
    .catch(error => {
      console.log(`useAxios: catch error => ${JSON.stringify(error)}.`);
      
      setState(prevState => ({
        ...prevState,
        isError: true,
      }));

      if (errorCb) {
        errorCb(error);
      }

    })
    .then(() => {
      
      setState({
        ...initialState,
        isFetching: false,
      });

    });
  }
  
  return sender;
}


--#

