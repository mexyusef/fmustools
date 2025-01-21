--% index/fmus
.,d
	%__TEMPLATE_CLIENT_PORT=__NILAI_CLIENT_PORT__
	?pick
		@antlr*
			?pick
				@antlr-go*
				@antlr-python*
					pyantlr,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/z/quick/parser__/pyantlr.fmus=index/fmus*)
				@antlr-javascript*
				@antlr-java*
		@javascript: ... apa namanya lupa*
		@python: lark, antlr*
			pyantlr,d(/load=ULIBPY_BASEDIR/app/transpiler/frontend/fslang/z/quick/parser__/pyantlr.fmus=index/fmus*)
		@python: pyparsing*
--#
