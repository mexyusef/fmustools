--% index/fmus
__PWD,d
	?pick
		@python*
			?pick
				@pyqt5 project*
				@wxpython project*
				@tkinter project*
				@webscraping - beautifulsoup*
				@webscraping - scrapy*
				@webscraping - xpath*
				@grpc - python*
				@kafka - python*
				@mqtt - python*
				@network/tcp/udp - python*
				@packaging: setup.py/easy_install*
				@concurrent: asyncio, eventloop setup*
				@quick repl - quickrepl dan langtemplate*
					.,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/z/quick/backend/../../../misc/quickrepl/index.mk=index/fmus*)
					.,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/z/quick/backend/../../../misc/langtemplate/index.mk=index/fmus*)
		@typescript*
			?pick
				@deno project*
				@react ts project*
				@webscraping - puppeteer*
		@javascript*
			?pick
				@node/express project*
				@npm package setup*
				@chrome extension setup*
				@firefox extension setup*
				@react project*
				@webscraping - puppeteer*
		@java*
			?pick
				@webscraping - jsoup*
				@gradle project*
					mygradle,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/z/quick/backend__/java-gradle.fmus=index/fmus*)
					mymaven,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/z/quick/backend__/java-maven.fmus=index/fmus*)
				@maven project*
				@springboot project*
		@kotlin*
			?pick
				@android project*
				@springboot project*
		@scala*
			?pick
				@play*
				@akka*
		@clojure*
		@go*
			?pick
				@webscraping - colly*
				@webassembly - go*
				@grpc - go*
		@rust*
			?pick
				@webassembly - rust*
				@grpc - rust*
		@c++*
			?pick
				@webassembly - c++*
				@create repl/cli*
				@cmake cpp sederhana di sini dg preloaded simple C++ program...*
					.,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/z/quick/backend__/cpp-cmake-boost.fmus=index/fmus*)
				@cmake cpp sederhana di sini dg user entry program lewat nano...*
					.,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/z/quick/backend__/cpp-cmake-boost-userentry.fmus=index/fmus*)
		@c#*
		@dart*
		@elm*
		@erlang*
		@elixir*
		@haskell*
		@by topics: parser, cli/repl, webasm, webscrape, websocket, webrtc, tcp/udp, gui, gql, gql+rest, rest, tdd*
			?pick
				@parser/parsing*
				@cli/repl*
				@webassembly*
				@web scraping*
				@web socket/socket.io*
				@web rtc*
				@komunikasi tcp/udp*
				@simple gui*
				@graphql*
				@hybrid rest - graphql*
				@rest*
				@tdd*
				@data science/engineering*
				@create package*
					?pick
						@python package*
						@js/ts package*
						@java library*
						@go package*
						@rust package*
--#
