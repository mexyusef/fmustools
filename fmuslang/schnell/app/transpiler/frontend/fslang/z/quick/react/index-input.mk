--% index/fmus
.,d
	%__TEMPLATE_CLIENT_PORT=__NILAI_CLIENT_PORT__
	?pick
		@project: crajs, webpack react-js*
			?pick
				wp5react,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/z/quick/react/wp5-reactjs.mk=index/fmus*)
				wp5react-ts,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/z/quick/react/wp5-reactts.mk=index/fmus*)
				sanity,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/z/quick/react/sanity.mk=index/fmus*)
		@pages*
			?pick
				@login page*
				@register page*
		@components*
			?pick
				@sidebar*
				@header*
					?pick
						@navbar*
						@searchbar*
						@profile dropdown*
						@hamburger*
				@rightbar*
		@UI/UX*
			?pick
				@antd*
					?pick
						@form*
						@table*
						@notification/alert*
						@modal*
						@drawer*
				@reactstrap*
				@react-bootstrap*
				@mui4*
				@mui5*
				@tailwind*
				@chakra-ui*
				@styled-component*
		@charts/graphs: line, area, bar, pie, donut*
			?pick
				@bizcharts*
				@echarts*
				@highcharts*
				@recharts*
		@communication*
			?pick
				@websocket*
				@socket.io*
				@pubsub*
				@webrtc*
		@configuration*
			?pick
				@babel json*
				@babel js*
				@eslint json*
				@eslint js*
				@prettier json*
				@prettier js*
				@lerna*
				@post-css*
				@swc*
		@context*
		@hook*
		@store*
		@function component*
		@class component*
		@useEffect*
		@useState*
--#
