--% index/fm.us
__TEMPLATE_PROJECT_DIR__,d(/mk)
	%utama=__FILE__
	%__TEMPLATE_SERVER_PORT__=9505
	$*qterminal 2>/dev/null &

	.editorconfig,f(e=utama=/rts/.editorconfig)
	package.json,f(e=utama=/rts/package.json)
	.gitignore,f(e=utama=/rts/.gitignore)
	wallaby.conf.js,f(e=utama=/rts/wallaby.conf.js)
	tsconfig.json,f(e=utama=/rts/tsconfig.json)
	.eslintrc.js,f(e=utama=/rts/.eslintrc.js)
	README.md,f(e=utama=/rts/README.md)
	.commitlintrc.js,f(e=utama=/rts/.commitlintrc.js)
	.babelrc,f(e=utama=/rts/.babelrc)
	.dockerignore,f(e=utama=/rts/.dockerignore)
	Dockerfile,f(e=utama=/rts/Dockerfile)
	.gitattributes,f(e=utama=/rts/.gitattributes)
	yarn.add.sh,f(e=utama=/yarn.add.sh)
	run.sh,f(e=utama=/run.sh)
	$*chmod a+x *.sh
	$*ln -s ../node_modules .
	
	src,d(/mk)
		server.tsx,f(e=utama=/rts/src/server.tsx)
		index.html,f(e=utama=/rts/src/index.html)
		favicon.ico,f(b64=utama=/rts/src/favicon.ico)
		client.tsx,f(e=utama=/rts/src/client.tsx)
		app,d(/mk)
			helpers,d(/mk)
				setupCss.ts,f(e=utama=/rts/src/app/helpers/setupCss.ts)
				withInitialState.tsx,f(e=utama=/rts/src/app/helpers/withInitialState.tsx)
				JestBootstrap.ts,f(e=utama=/rts/src/app/helpers/JestBootstrap.ts)
				LanguageHelper.ts,f(e=utama=/rts/src/app/helpers/LanguageHelper.ts)
				LanguageHelper.test.ts,f(e=utama=/rts/src/app/helpers/LanguageHelper.test.ts)
			pages,d(/mk)
				StarsPage.test.tsx,f(e=utama=/rts/src/app/pages/StarsPage.test.tsx)
				StarsPage.tsx,f(e=utama=/rts/src/app/pages/StarsPage.tsx)
				CounterPage.test.tsx,f(e=utama=/rts/src/app/pages/CounterPage.test.tsx)
				AboutPage.tsx,f(e=utama=/rts/src/app/pages/AboutPage.tsx)
				AboutPage.test.tsx,f(e=utama=/rts/src/app/pages/AboutPage.test.tsx)
				HomePage.test.tsx,f(e=utama=/rts/src/app/pages/HomePage.test.tsx)
				CounterPage.tsx,f(e=utama=/rts/src/app/pages/CounterPage.tsx)
				HomePage.tsx,f(e=utama=/rts/src/app/pages/HomePage.tsx)
			sagas,d(/mk)
				StarsSaga.test.ts,f(e=utama=/rts/src/app/sagas/StarsSaga.test.ts)
				StarsSaga.ts,f(e=utama=/rts/src/app/sagas/StarsSaga.ts)
				SettingsSaga.ts,f(e=utama=/rts/src/app/sagas/SettingsSaga.ts)
				dummyApi.ts,f(e=utama=/rts/src/app/sagas/dummyApi.ts)
				BaseSaga.ts,f(e=utama=/rts/src/app/sagas/BaseSaga.ts)
				rootSaga.ts,f(e=utama=/rts/src/app/sagas/rootSaga.ts)
				SettingsSaga.test.ts,f(e=utama=/rts/src/app/sagas/SettingsSaga.test.ts)
			redux,d(/mk)
				rootReducer.ts,f(e=utama=/rts/src/app/redux/rootReducer.ts)
				configureStore.ts,f(e=utama=/rts/src/app/redux/configureStore.ts)
				IStore.ts,f(e=utama=/rts/src/app/redux/IStore.ts)
				modules,d(/mk)
					starsActionCreators.ts,f(e=utama=/rts/src/app/redux/modules/starsActionCreators.ts)
					counterActionCreators.ts,f(e=utama=/rts/src/app/redux/modules/counterActionCreators.ts)
					settingsActionCreators.ts,f(e=utama=/rts/src/app/redux/modules/settingsActionCreators.ts)
					counterModule.test.ts,f(e=utama=/rts/src/app/redux/modules/counterModule.test.ts)
					starsModule.ts,f(e=utama=/rts/src/app/redux/modules/starsModule.ts)
					settingsModule.test.ts,f(e=utama=/rts/src/app/redux/modules/settingsModule.test.ts)
					settingsModule.ts,f(e=utama=/rts/src/app/redux/modules/settingsModule.ts)
					baseModule.ts,f(e=utama=/rts/src/app/redux/modules/baseModule.ts)
					counterModule.ts,f(e=utama=/rts/src/app/redux/modules/counterModule.ts)
					starsModule.test.ts,f(e=utama=/rts/src/app/redux/modules/starsModule.test.ts)
				middlewares,d(/mk)
					sentryMiddleware.ts,f(e=utama=/rts/src/app/redux/middlewares/sentryMiddleware.ts)
			images,d(/mk)
				crazy.png,f(b64=utama=/rts/src/app/images/crazy.png)
			models,d(/mk)
				Translator.ts,f(e=utama=/rts/src/app/models/Translator.ts)
				TranslatorInterfaces.ts,f(e=utama=/rts/src/app/models/TranslatorInterfaces.ts)
			components,d(/mk)
				Button.stories.tsx,f(e=utama=/rts/src/app/components/Button.stories.tsx)
				Button.tsx,f(e=utama=/rts/src/app/components/Button.tsx)
			constants,d(/mk)
				FontSize.ts,f(e=utama=/rts/src/app/constants/FontSize.ts)
				Color.ts,f(e=utama=/rts/src/app/constants/Color.ts)
				index.ts,f(e=utama=/rts/src/app/constants/index.ts)
			containers,d(/mk)
				App.tsx,f(e=utama=/rts/src/app/containers/App.tsx)
				Header.tsx,f(e=utama=/rts/src/app/containers/Header.tsx)
				Html.tsx,f(e=utama=/rts/src/app/containers/Html.tsx)
				Header.test.tsx,f(e=utama=/rts/src/app/containers/Header.test.tsx)
				App.test.tsx,f(e=utama=/rts/src/app/containers/App.test.tsx)
			routes,d(/mk)
				configureRouter.ts,f(e=utama=/rts/src/app/routes/configureRouter.ts)
				routes.ts,f(e=utama=/rts/src/app/routes/routes.ts)
			selectors,d(/mk)
				translationsSelector.ts,f(e=utama=/rts/src/app/selectors/translationsSelector.ts)
	.storybook,d(/mk)
		webpack.config.js,f(e=utama=/rts/.storybook/webpack.config.js)
		presets.js,f(e=utama=/rts/.storybook/presets.js)
		config.js,f(e=utama=/rts/.storybook/config.js)
	config,d(/mk)
		main.js,f(e=utama=/rts/config/main.js)
		main.local.js,f(e=utama=/rts/config/main.local.js)
		index.js,f(e=utama=/rts/config/index.js)
		webpack,d(/mk)
			index.js,f(e=utama=/rts/config/webpack/index.js)
			dev.js,f(e=utama=/rts/config/webpack/dev.js)
			prod.js,f(e=utama=/rts/config/webpack/prod.js)
			server.js,f(e=utama=/rts/config/webpack/server.js)
		types,d(/mk)
			png.d.ts,f(e=utama=/rts/config/types/png.d.ts)
			dev.d.ts,f(e=utama=/rts/config/types/dev.d.ts)
			redux-router5.d.ts,f(e=utama=/rts/config/types/redux-router5.d.ts)
		utils,d(/mk)
			createIfDoesntExist.js,f(e=utama=/rts/config/utils/createIfDoesntExist.js)
			index.js,f(e=utama=/rts/config/utils/index.js)
			copySync.js,f(e=utama=/rts/config/utils/copySync.js)
			replaceWithProdScripts.js,f(e=utama=/rts/config/utils/replaceWithProdScripts.js)
			copySyncIfDoesntExist.js,f(e=utama=/rts/config/utils/copySyncIfDoesntExist.js)

	translations,d(/mk)
		en.json,f(e=utama=/rts/translations/en.json)
		de.json,f(e=utama=/rts/translations/de.json)
	__mocks__,d(/mk)
		.fs.ts,f(e=utama=/rts/__mocks__/.fs.ts)
		fileMock.js,f(e=utama=/rts/__mocks__/fileMock.js)
		fs.js,f(e=utama=/rts/__mocks__/fs.js)
--#

--% /run.sh
# ./node_modules/.bin/webpack serve --mode development --config __TEMPLATE_WEBPACK_NAME__
./node_modules/.bin/webpack serve --mode development --config node_modules/@medly/webpack-config
--#

--% /yarn.add.sh
yarn add @sentry/browser autobind-decorator chalk cross-fetch es6-promise express prop-types react react-dom react-helmet react-redux react-router5 redux redux-logger redux-router5 redux-saga reselect router5 router5-plugin-browser serialize-javascript serve-favicon typesafe-actions typestyle

yarn add --dev @babel/core @babel/plugin-proposal-class-properties @babel/plugin-proposal-decorators @babel/plugin-proposal-nullish-coalescing-operator @babel/plugin-proposal-object-rest-spread @babel/plugin-proposal-optional-chaining @babel/plugin-transform-runtime @babel/preset-env @babel/preset-react @babel/preset-typescript @commitlint/cli @commitlint/config-conventional @crazyfactory/tslint-rules @storybook/addon-docs @storybook/react @types/enzyme @types/express @types/jest @types/node @types/prop-types @types/react @types/react-dom @types/react-helmet @types/react-redux @types/serialize-javascript @types/storybook__react @typescript-eslint/eslint-plugin @typescript-eslint/eslint-plugin-tslint @typescript-eslint/parser babel-loader cross-env css-loader enzyme enzyme-adapter-react-16 eslint eslint-loader file-loader husky jest jest-enzyme mini-css-extract-plugin null-loader optimize-css-assets-webpack-plugin react-docgen-typescript-loader react-hot-loader rimraf style-loader terser-webpack-plugin ts-jest tslint tslint-microsoft-contrib tslint-react typescript url-loader webpack webpack-bundle-analyzer webpack-cli webpack-dev-middleware webpack-hot-middleware webpack-manifest-plugin
--#

--% /rts/.editorconfig
# EditorConfig helps developers define and maintain consistent
# coding styles between different editors and IDEs
# editorconfig.org

root = true

[*]

# Change these settings to your own preference
indent_style = space
indent_size = 2

# We recommend you to keep these unchanged
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true

[*.md]
trim_trailing_whitespace = false

--#

--% /rts/package.json
{
	"name": "RTS Mania",
	"description": "React, Typescript, and Sh*t.",
	"main": "build/server.js",
	"husky": {
		"hooks": {
			"commit-msg": "commitlint -E HUSKY_GIT_PARAMS",
			"pre-commit": "npm run lint",
			"pre-push": "npm run build && npm run build:prod && npm run test:no-cache"
		}
	},
	"scripts": {
		"type-check": "tsc",
		"type-check:watch": "npm run type-check -- --watch",
		"clean": "rimraf build && rimraf .jest/cache",
		"prebuild": "npm run clean -s",
		"build": "webpack --config config/webpack/index.js",
		"build:prod": "cross-env NODE_ENV=production npm run build && node ./config/utils/replaceWithProdScripts",
		"postbuild": "webpack --config config/webpack/server.js",
		"prestart": "npm run build -s",
		"start": "node build/server.js",
		"start:prod": "npm run build:prod && cross-env NODE_ENV=production node build/server.js",
		"test": "jest",
		"test:no-cache": "jest --no-cache",
		"test:watch": "jest --watch",
		"lint": "eslint \"src/**/**.ts*\"",
		"lint:fix": "npm run lint -s -- --fix",
		"doc": "start-storybook -p 6060"
	},

	"devDependencies": {
		"@babel/core": "^7.9.6",
		"@babel/plugin-proposal-class-properties": "^7.8.3",
		"@babel/plugin-proposal-decorators": "^7.8.3",
		"@babel/plugin-proposal-nullish-coalescing-operator": "^7.8.3",
		"@babel/plugin-proposal-object-rest-spread": "^7.9.6",
		"@babel/plugin-proposal-optional-chaining": "^7.9.0",
		"@babel/plugin-transform-runtime": "^7.9.6",
		"@babel/preset-env": "^7.9.6",
		"@babel/preset-react": "^7.9.4",
		"@babel/preset-typescript": "^7.9.0",
		"@commitlint/cli": "^8.3.5",
		"@commitlint/config-conventional": "^8.3.4",
		"@crazyfactory/tslint-rules": "^1.9.0",
		"@storybook/addon-docs": "^5.3.18",
		"@storybook/react": "^5.3.18",
		"@types/enzyme": "^3.10.5",
		"@types/express": "^4.17.6",
		"@types/jest": "^25.2.1",
		"@types/node": "^13.13.4",
		"@types/prop-types": "^15.7.3",
		"@types/react": "^16.9.34",
		"@types/react-dom": "^16.9.7",
		"@types/react-helmet": "^5.0.15",
		"@types/react-redux": "^7.1.8",
		"@types/serialize-javascript": "^1.5.0",
		"@types/storybook__react": "^5.2.1",
		"@typescript-eslint/eslint-plugin": "^2.33.0",
		"@typescript-eslint/eslint-plugin-tslint": "^2.33.0",
		"@typescript-eslint/parser": "^2.33.0",
		"babel-loader": "^8.1.0",
		"cross-env": "^7.0.2",
		"css-loader": "^3.5.3",
		"enzyme": "^3.11.0",
		"enzyme-adapter-react-16": "^1.15.2",
		"eslint": "^7.0.0",
		"eslint-loader": "^4.0.2",
		"file-loader": "^6.0.0",
		"husky": "^4.2.5",
		"jest": "^25.5.4",
		"jest-enzyme": "^7.1.2",
		"mini-css-extract-plugin": "^0.9.0",
		"null-loader": "^4.0.0",
		"optimize-css-assets-webpack-plugin": "^5.0.3",
		"react-docgen-typescript-loader": "^3.7.2",
		"react-hot-loader": "^4.12.21",
		"rimraf": "^3.0.2",
		"style-loader": "^1.2.1",
		"terser-webpack-plugin": "^3.0.1",
		"ts-jest": "^26.1.0",
		"tslint": "^6.1.2",
		"tslint-microsoft-contrib": "^6.2.0",
		"tslint-react": "^5.0.0",
		"typescript": "^3.9.2",
		"url-loader": "^4.1.0",
		"webpack": "^4.43.0",
		"webpack-bundle-analyzer": "^3.7.0",
		"webpack-cli": "^3.3.11",
		"webpack-dev-middleware": "^3.7.2",
		"webpack-hot-middleware": "^2.25.0",
		"webpack-manifest-plugin": "^2.2.0"
	},
	"dependencies": {
		"@sentry/browser": "^5.27.0",
		"autobind-decorator": "^2.4.0",
		"chalk": "^4.1.0",
		"cross-fetch": "^3.0.6",
		"es6-promise": "^4.2.8",
		"express": "^4.17.1",
		"prop-types": "^15.7.2",
		"react": "^16.14.0",
		"react-dom": "^16.14.0",
		"react-helmet": "^6.1.0",
		"react-redux": "^7.2.1",
		"react-router5": "^8.0.1",
		"redux": "^4.0.5",
		"redux-logger": "^3.0.6",
		"redux-router5": "^8.0.1",
		"redux-saga": "^1.1.3",
		"reselect": "^4.0.0",
		"router5": "^8.0.1",
		"router5-plugin-browser": "^8.0.1",
		"serialize-javascript": "^3.1.0",
		"serve-favicon": "^2.5.0",
		"typesafe-actions": "^5.1.0",
		"typestyle": "^2.1.0"
	},
	"jest": {
		"preset": "ts-jest",
		"cacheDirectory": "<rootDir>/.jest/cache",
		"collectCoverage": true,
		"coverageDirectory": "<rootDir>/coverage",
		"testRegex": "(/__tests__/.*|\\.(test|spec))\\.(ts|tsx|js)$",
		"moduleNameMapper": {
			"\\.(jpg|jpeg|png|gif|eot|otf|webp|svg|ttf|woff|woff2|mp4|webm|wav|mp3|m4a|aac|oga)$": "<rootDir>/__mocks__/fileMock.js"
		},
		"moduleFileExtensions": [
			"ts",
			"tsx",
			"js",
			"json"
		],
		"moduleDirectories": [
			"node_modules",
			"./"
		],
		"setupFilesAfterEnv": [
			"./src/app/helpers/JestBootstrap.ts"
		]
	}
}

--#

--% /rts/.gitignore
# Build Folder
build
config/main.local.js
# Logs
logs
*.log
npm-debug.log*

# Runtime data
pids
*.pid
*.seed

# Directory for instrumented libs generated by jscoverage/JSCover
lib-cov

# Coverage directory used by tools like istanbul
coverage

# node-waf configuration
.lock-wscript

# Compiled binary addons (http://nodejs.org/api/addons.html)
build/Release

# Dependency directory
node_modules

# Optional npm cache directory
.npm

# Optional REPL history
.node_repl_history

# OS X
.DS_STORE

# JetBrains
.idea/*
!.idea/runConfigurations/
!.idea/inspectionProfiles/
.awcache/
.jest/cache/

--#

--% /rts/wallaby.conf.js
module.exports = function(wallaby) {
	return {
		files: [
			'src/**/*.ts',
			'src/**/*.tsx',
			'__mocks__/**/*',
			'config/**/*',
			'!src/**/*.test.ts',
			'!src/**/*.test.tsx'
		],
		tests: [
			'src/**/*.test.ts',
			'src/**/*.test.tsx'
		],
		env: {
			type: 'node'
		},
		testFramework: 'jest'
	};
};

--#

--% /rts/tsconfig.json
{
	"compilerOptions": {
		"outDir": "build",
		"module": "commonjs",
		"target": "es5",
		"lib": ["es5", "scripthost", "dom", "es2015"],
		"sourceMap": true,
		"inlineSourceMap": false,
		"inlineSources": false,
		"experimentalDecorators": true,
		"noEmit": true,
		"noUnusedParameters": true,
		"noUnusedLocals": true,
		"jsx": "react",
		"moduleResolution": "node",
		"esModuleInterop": true
	},
	"exclude": [
		"node_modules",
		"build"
	]
}

--#

--% /rts/.eslintrc.js
const tslintRules = {
	"align": [
		true,
		"parameters",
		"arguments",
		"statements"
	],
	"chai-vague-errors": true,
	"comment-format": [
		true,
		"check-space"
	],
	"create-async-actions": true,
	"enum-sort-keys": true,
	"export-name": true,
	"function-constructor": true,
	"function-name": [
		true,
		{
			"method-regex": "^[a-z][\\w\\d]+$",
			"private-method-regex": "^[a-z][\\w\\d]+$",
			"static-method-regex": "^[a-z][\\w\\d]+$",
			"function-regex": "^[a-z][\\w\\d]+$"
		}
	],
	"hex-format": true,
	"import-spacing": true,
	"interface-sort-keys": false,
	"increment-decrement": true,
	"jquery-deferred-must-complete": true,
	"jsdoc-format": true,
	"jsx-boolean-value": true,
	"jsx-curly-spacing": [
		true,
		"never"
	],
	"jsx-equals-spacing": [
		true,
		"never"
	],
	"jsx-key": true,
	"jsx-no-bind": true,
	"jsx-no-lambda": true,
	"jsx-no-multiline-js": true,
	"jsx-no-string-ref": true,
	"jsx-self-close": true,
	"jsx-space-before-closing-tag": [
		true,
		"never"
	],
	"jsx-wrap-multiline": true,
	"max-func-body-length": [
		true,
		150,
		{
			"ignore-parameters-to-function-regex": "describe"
		}
	],
	"max-line-length": [
		true,
		120
	],
	"member-ordering": [
		true,
		{
			"order": [
				"public-static-field",
				"public-instance-field",
				"private-static-field",
				"private-instance-field",
				"public-constructor",
				"private-constructor",
				"public-instance-method",
				"protected-instance-method",
				"private-instance-method"
			],
			"alphabetize": true
		}
	],
	"mocha-avoid-only": true,
	"no-backbone-get-set-outside-model": true,
	"no-cookies": true,
	"no-delete-expression": true,
	"no-disable-auto-sanitization": true,
	"no-document-domain": true,
	"no-document-write": true,
	"no-dup-actions": true,
	"no-duplicate-imports": true,
	"no-duplicate-variable": true,
	"no-exec-script": true,
	"no-for-in": true,
	"no-function-expression": true,
	"no-http-string": true,
	"no-implicit-dependencies": [
		true,
		"dev"
	],
	"no-inner-html": true,
	"no-jquery-raw-elements": true,
	"no-reference-import": true,
	"no-shadowed-variable": true,
	"no-string-based-set-immediate": true,
	"no-string-based-set-interval": true,
	"no-string-based-set-timeout": true,
	"no-trailing-whitespace": true,
	"no-unnecessary-local-variable": true,
	"no-unnecessary-override": true,
	"no-unused-expression": true,
	"no-with-statement": true,
	"object-literal-sort-keys": true,
	"one-line": [
		true,
		"check-open-brace",
		"check-catch",
		"check-else",
		"check-whitespace"
	],
	"only-arrow-functions": [
		true,
		"allow-declarations",
		"allow-named-functions"
	],
	"ordered-imports": [
		true,
		{
			"import-sources-order": "case-insensitive",
			"module-source-path": "full",
			"named-imports-order": "case-insensitive"
		}
	],
	"prefer-array-literal": true,
	"prefer-conditional-expression": true,
	"promise-must-complete": true,
	"quotemark": [
		true,
		"double"
	],
	 // todo: Specifying excluded files as an option used to work until updating eslint and it's parsers.
	"react-no-dangerous-html": true,
	"react-this-binding-issue": true,
	"semicolon": [
		true,
		"always"
	],
	"space-within-parens": [
		true,
		0
	],
	"trailing-comma": [
		true,
		{
			"singleline": "never",
			"multiline": "never"
		}
	],
	"triple-equals": [
		true,
		"allow-null-check"
	],
	"typedef": [
		true,
		"call-signature",
		"parameter",
		"property-declaration",
		"member-variable-declaration"
	],
	"unnecessary-bind": true,
	"use-named-parameter": true,
	"variable-name": [
		true,
		"ban-keywords",
		"check-format",
		"allow-leading-underscore",
		"allow-pascal-case"
	],
	"whitespace": [
		true,
		"check-branch",
		"check-decl",
		"check-operator",
		"check-separator",
		"check-type"
	]
};

module.exports = {
	"env": {
		"browser": true,
		"node": true
	},
	"overrides": [
		{
			"files": ["*.stories.tsx"],
			"rules": {
				"@typescript-eslint/tslint/config": [
					"error",
					{
						"rulesDirectory": [
							"node_modules/tslint-react/rules",
							"node_modules/tslint-microsoft-contrib",
							"node_modules/@crazyfactory/tslint-rules/lib"
						],
						"rules": {
							...tslintRules,
							"export-name": false,
							"jsx-no-lambda": false,
							"react-this-binding-issue": false,
						}
					}
				]
			}
		}
	],
	"parser": "@typescript-eslint/parser",
	"parserOptions": {
		"project": "tsconfig.json",
		"sourceType": "module"
	},
	"plugins": [
		"@typescript-eslint",
		"@typescript-eslint/tslint"
	],
	"rules": {
		"@typescript-eslint/adjacent-overload-signatures": "error",
		"@typescript-eslint/array-type": "error",
		"@typescript-eslint/ban-types": "error",
		"@typescript-eslint/class-name-casing": "error",
		"@typescript-eslint/consistent-type-assertions": "error",
		"@typescript-eslint/explicit-member-accessibility": [
			"error",
			{
				"overrides": {
					"constructors": "off"
				}
			}
		],
		"@typescript-eslint/indent": ["error", 2],
		"@typescript-eslint/interface-name-prefix": [
			"error",
			{
				"prefixWithI": "always"
			}
		],
		"@typescript-eslint/member-ordering": "off",
		"@typescript-eslint/no-empty-function": "error",
		"@typescript-eslint/no-empty-interface": "error",
		"@typescript-eslint/no-explicit-any": "off",
		"@typescript-eslint/no-extraneous-class": "error",
		"@typescript-eslint/no-inferrable-types": "off",
		"@typescript-eslint/no-misused-new": "error",
		"@typescript-eslint/no-namespace": "off",
		"@typescript-eslint/no-parameter-properties": "off",
		"@typescript-eslint/no-require-imports": "off",
		"@typescript-eslint/no-this-alias": "error",
		"@typescript-eslint/no-use-before-declare": "off",
		"@typescript-eslint/no-var-requires": "off",
		"@typescript-eslint/prefer-for-of": "error",
		"@typescript-eslint/prefer-function-type": "error",
		"@typescript-eslint/prefer-namespace-keyword": "off",
		"@typescript-eslint/type-annotation-spacing": "error",
		"@typescript-eslint/unified-signatures": "error",
		"arrow-parens": [
			"error",
			"always"
		],
		"complexity": "off",
		"constructor-super": "error",
		"curly": "error",
		"default-case": "error",
		"dot-notation": "error",
		"eol-last": "off",
		"guard-for-in": "error",
		"max-classes-per-file": [
			"error",
			1
		],
		"member-ordering": "off",
		"new-parens": "error",
		"no-bitwise": "error",
		"no-caller": "error",
		"no-cond-assign": "error",
		"no-console": [
			"error",
			{
				"allow": [
					"error",
					"debug",
					"info",
					"time",
					"timeEnd",
					"trace",
					"warn"
				]
			}
		],
		"no-constant-condition": "error",
		"no-control-regex": "error",
		"no-debugger": "error",
		"no-duplicate-case": "error",
		"no-empty": "error",
		"no-empty-function": "off",
		"no-eval": "error",
		"no-extra-bind": "error",
		"no-extra-semi": "error",
		"no-fallthrough": "off",
		"no-invalid-regexp": "error",
		"no-invalid-this": "error",
		"no-multi-str": "off",
		"no-multiple-empty-lines": "error",
		"no-new-func": "error",
		"no-new-wrappers": "error",
		"no-octal": "error",
		"no-octal-escape": "error",
		"no-regex-spaces": "error",
		"no-return-await": "error",
		"no-sequences": "error",
		"no-sparse-arrays": "error",
		"no-template-curly-in-string": "error",
		"no-throw-literal": "error",
		"no-undef-init": "error",
		"no-unsafe-finally": "error",
		"no-unused-labels": "error",
		"no-var": "error",
		"object-shorthand": "error",
		"one-var": "off",
		"prefer-const": "error",
		"prefer-object-spread": "error",
		"quote-props": [
			"error",
			"consistent-as-needed"
		],
		"radix": "error",
		"space-before-function-paren": ["error", "never"],
		"use-isnan": "error",
		"valid-typeof": "off",
		"@typescript-eslint/tslint/config": [
			"error",
			{
				"rulesDirectory": [
					"node_modules/tslint-react/rules",
					"node_modules/tslint-microsoft-contrib",
					"node_modules/@crazyfactory/tslint-rules/lib"
				],
				"rules": tslintRules
			}
		]
	}
};

--#

--% /rts/README.md
# ts-react-boilerplate

[![Greenkeeper badge](https://badges.greenkeeper.io/crazyfactory/ts-react-boilerplate.svg?token=817c7964cfab1973415f903cc9bde50f4d9ea8d7fe44c1b0e722569f0c99438d)](https://greenkeeper.io/)
[![Build Status](https://travis-ci.org/crazyfactory/ts-react-boilerplate.svg?branch=master)](https://travis-ci.org/crazyfactory/ts-react-boilerplate)
[![Dependency Status](https://david-dm.org/crazyfactory/ts-react-boilerplate.svg)](https://david-dm.org/crazyfactory/ts-react-boilerplate)
[![devDependency Status](https://david-dm.org/crazyfactory/ts-react-boilerplate/dev-status.svg)](https://david-dm.org/crazyfactory/ts-react-boilerplate?type=dev)
[![GitHub issues](https://img.shields.io/github/issues/crazyfactory/ts-react-boilerplate.svg)](https://github.com/crazyfactory/ts-react-boilerplate/issues)
___

##### Based on [Vortigern](https://github.com/barbar/vortigern)

[![TypeScript](./.github/typescript.png)](https://www.typescriptlang.org/)
[![React](./.github/react.png)](https://github.com/facebook/react)
[![Redux](./.github/redux.png)](https://github.com/reactjs/redux)

## Libraries
This boilerplate uses the following libraries and tools:

#### Core
- [TypeScript](https://www.typescriptlang.org/)
- [React](https://github.com/facebook/react) & [React DOM](https://github.com/facebook/react) for views.
- [Router5](https://github.com/router5) handles in-app routing.
- [Redux](https://github.com/reactjs/redux) manages application state.
- [React Redux](https://github.com/reactjs/react-redux) to use React-Redux bindings.
- [React Router5](https://github.com/router5) & [Redux-Router5](https://github.com/router5) integrate router5 with react
and redux.

#### Utilities
- [Reselect](https://github.com/reduxjs/reselect/) computes derived data, allowing Redux to store the minimal possible
state.
- [Redux Saga](https://github.com/redux-saga/redux-saga) makes side effects (i.e. asynchronous things like data fetching
and impure things like accessing the browser cache) in React/Redux applications easier and better.
- [Isomorphic Fetch](https://github.com/matthew-andrews/isomorphic-fetch) with
[ES6-Promise](https://github.com/stefanpenner/es6-promise) for using fetch api on both client & server side.
- [React Helmet](https://github.com/nfl/react-helmet)
- [Sentry Browser](https://github.com/getsentry/sentry-javascript) captures exceptions during run time.
- [TypeStyle](https://github.com/typestyle/typestyle) makes css typesafe.

#### Build System
- [Webpack](https://github.com/webpack/webpack) for bundling.
	- [TS Loader](https://github.com/TypeStrong/ts-loader) as ts loader.
	- [React Hot Loader](https://github.com/gaearon/react-hot-loader) provides hot reload capability to our development
	server
	- [File Loader](https://github.com/webpack/file-loader)
	- [URL Loader](https://github.com/webpack/url-loader)
	- [Manifest Plugin](https://github.com/danethurber/webpack-manifest-plugin)
	- [TS Lint Loader](https://github.com/wbuchwalter/tslint-loader) for using tslint as preloader on build process.

#### Dev & Prod Server
- [Webpack Dev Middleware](https://github.com/webpack/webpack-dev-middleware)
- [Webpack Hot Middleware](https://github.com/webpack/webpack-hot-middleware)
- [Express](https://github.com/expressjs/express) for running server both on client and server side.
- [Serve Favicon](https://github.com/expressjs/serve-favicon) for serving favicon.

#### Developer Experience
- [ESLint](https://github.com/eslint/eslint) for linting.
- [Typescript ESLint](https://github.com/typescript-eslint/typescript-eslint) enables ESLint to support TypeScript.
- [Redux Logger](https://github.com/theaqua/redux-logger)
- [Redux DevTools](https://github.com/gaearon/redux-devtools)
- [Chalk](https://github.com/chalk/chalk) for colored terminal logs.

#### Testing
- [Jest](https://github.com/facebook/jest) as test runner.
- [TS Jest](https://github.com/kulshekhar/ts-jest) as Jest preprocessor
- [Enzyme](https://github.com/airbnb/enzyme) for rendering React Components.
- [Jest Enzyme](https://github.com/blainekasten/enzyme-matchers) for asserting React Components.

#### Doc
- [Storybook](https://github.com/storybookjs/storybook) - UI component dev & test: React and more.

## Directory Structure
```bash
.
├── build                       # Built, ready to serve app.
├── config                      # Root folder for configurations.
│   ├── types                   # Global type definitions, written by us.
│   ├── utils                   # Utils for config.
│   ├── webpack                 # Webpack configurations.
│   ├── index.js                # Combines main.js and main.local.js
│   ├── main.js                 # Default App configurations.
│   └── main.local.js           # Local App configurations.
├── node_modules                # Node Packages.
├── src                         # Source code.
│   ├── app                     # App folder.
│   │ ├── components            # Unconnected Components.
│   │ ├── constants             # Constants that are used throughout project like Color and FontSize
│   │ ├── containers            # Redux-Connected Components.
│   │ ├── helpers               # Helper Functions.
│   │ ├── images                # Images folder.
│   │ ├── models                # Models folder.
│   │ ├── pages                 # Page-like Components.
│   │ ├── redux                 # Redux related code aka data layer of the app.
│   │ │   ├── middlewares       # Redux middlewares.     
│   │ │   ├── modules           # Redux modules.     
│   │ │   ├── configureStore.ts # Redux store, contains global app state.
│   │ │   ├── IStore.ts         # Store shape.
│   │ │   └── rootReducer.ts    # Main reducers file to combine them.    
│   │ ├── routes                # Routes.
│   │ ├── sagas                 # Saga files.
│   │ └── selectors             # Redux selectors.
│   ├── vendor                  # Dealing with resources
│   ├── client.tsx              # Entry point for client side rendering.
│   ├── favicon.ico             # Favicon
│   ├── index.html              # html file for client side rendering
│   └── server.tsx              # Entry point for server side rendering.
├── translations                # For json translations.
├── .dockerignore               # Tells docker which files to ignore.
├── .editorconfig               # Configuration for editors.
├── .gitignore                  # Tells git which files to ignore.
├── .travis.yml                 # Travis file.
├── Dockerfile                  # Dockerfile.
├── LICENSE                     # License file
├── package.json                # Package configuration.
├── package-lock.json           # Package lock
├── README.md                   # This file
├── styleguide.config.js        # Config for doc
├── tsconfig.json               # TypeScript transpiler configuration.
└── tslint.json                 # Configures tslint.
```

## Installation

You can clone from this repository and use master

```bash
$ git clone https://github.com/crazyfactory/ts-react-boilerplate
$ cd ts-react-boilerplate
$ npm install
```

## Usage

All commands defaults to development environment. You can set `NODE_ENV` to `production` or use the shortcuts below.

```bash
# Running

$ npm start # This starts the app in development mode

# Starting it with the production build
$ NODE_ENV=production npm start # or
$ npm run start:prod

# Building 

$ npm build # This builds the app in development mode

# Commands below builds the production build
$ NODE_ENV=production npm build # or
$ npm run build:prod

# Testing
$ npm test

# Too see doc, run this command, and go to localhost:6060. Any component that has .md file with the same name will be
# doc-generated.
$ npm run doc
```

For Windows users, we recommend using the shortcuts instead of setting environment variables because they work a little
different on Windows.

#### Sentry
Create main.local.js in config folder and export an object that has `sentry` key like so:
```
module.exports = {
	sentry: {
		dsn: YOUR_DSN,
		release: YOUR_RELEASE_VERSION
	}
	
	// other configs
	...
}
```

## Credits

This boilerplate is based on [Vortigern](https://github.com/barbar/vortigern) and is heavily updated.
This boilerplate is released under the [MIT license](LICENSE).

___

## [Crazy Factory](https://www.crazy-factory.com/en-US/)

Crazy factory is an online shop which manufactures piercings, jewellery, mobile covers, etc. **All at factory prices!**

You can contact us at [dev@crazy-factory.com](mailto:dev@crazy-factory.com)

Be sure to check out available [jobs at Crazy](http://stackoverflow.com/jobs/companies/Crazy-Factory).

--#

--% /rts/.commitlintrc.js
module.exports = {
	extends: ['@commitlint/config-conventional'],
	rules: {
		'type-enum': [
			2,
			'always',
			[
				'build',
				'chore',
				'ci',
				'cleanup',
				'docs',
				'feat',
				'fix',
				'followup',
				'improve',
				'perf',
				'refactor',
				'revert',
				'style',
				'test',
				'unfeat'
			]
		]
	}
};

--#

--% /rts/.babelrc
{
	"presets": [
		"@babel/env",
		"@babel/typescript",
		"@babel/react"
	],
	"plugins": [
		["@babel/plugin-proposal-decorators", {"legacy": true}],
		["@babel/plugin-proposal-class-properties", {"loose":  true}],
		["@babel/plugin-proposal-private-methods", { "loose": true }],
		"@babel/plugin-proposal-nullish-coalescing-operator",
		"@babel/plugin-proposal-object-rest-spread",
		"@babel/plugin-proposal-optional-chaining",
		"@babel/plugin-transform-runtime"
	]
}

--#

--% /rts/.dockerignore
# Build Folder
build

# Logs
logs
*.log
npm-debug.log*

# Runtime data
pids
*.pid
*.seed

# Directory for instrumented libs generated by jscoverage/JSCover
lib-cov

# Coverage directory used by tools like istanbul
coverage

# node-waf configuration
.lock-wscript

# Compiled binary addons (http://nodejs.org/api/addons.html)
build/Release

# Dependency directory
node_modules

# Optional npm cache directory
.npm

# Optional REPL history
.node_repl_history

# OS X
.DS_STORE

# TypeScript
typings

# Git
.git
--#

--% /rts/Dockerfile
FROM mhart/alpine-node:latest

MAINTAINER Crazy Factory dev@crazy-factory.com

WORKDIR /app
ADD . .

RUN npm install

EXPOSE __TEMPLATE_SERVER_PORT__

CMD ["npm", "run", "start:prod"]

--#

--% /rts/.gitattributes
* text eol=lf

#
## These files are binary and should be left untouched
#

# (binary is a macro for -text -diff)
*.png binary
*.jpg binary
*.jpeg binary
*.gif binary
*.ico binary
*.mov binary
*.mp4 binary
*.mp3 binary
*.flv binary
*.fla binary
*.swf binary
*.gz binary
*.zip binary
*.7z binary
*.ttf binary
*.eot binary
*.woff binary
*.pyc binary
*.pdf binary

--#

--% /rts/src/server.tsx
import * as e6p from "es6-promise";
(e6p as any).polyfill();
import Chalk from "chalk";
import "cross-fetch/polyfill";
import express from "express";
import path from "path";
import * as React from "react";
import {renderToString} from "react-dom/server";
import {Provider} from "react-redux";
import {RouterProvider} from "react-router5";
import favicon from "serve-favicon";
import {config as appConfig} from "../config";
import {App} from "./app/containers/App";
import {Html} from "./app/containers/Html";
import {LanguageHelper} from "./app/helpers/LanguageHelper";
import {configureStore} from "./app/redux/configureStore";
import {IStore} from "./app/redux/IStore";
import {configureRouter} from "./app/routes/configureRouter";
import rootSaga from "./app/sagas/rootSaga";

const app = express();

if (process.env.NODE_ENV !== "production") {
	const webpack = require("webpack");
	const webpackConfig = require("../config/webpack/dev");
	const webpackCompiler = webpack(webpackConfig);

	app.use(require("webpack-dev-middleware")(webpackCompiler, {
		lazy: false,
		logLevel: "info",
		publicPath: webpackConfig.output.publicPath,
		stats: {colors: true}
	}));

	app.use(require("webpack-hot-middleware")(webpackCompiler));
}

app.use(favicon(path.join(__dirname, "public/favicon.ico")));

app.use("/public", express.static(path.join(__dirname, "public")));

app.get("/translations/:language", (req: express.Request, res: express.Response) => {
	const languageHelper = new LanguageHelper(req.params.language);
	res.json(languageHelper.getTranslations());
});

app.get("*", (req: express.Request, res: express.Response) => {
	if (!appConfig.ssr) {
		res.sendFile(path.resolve("./build/index.html"), {}, (error) => {
			if (error) {
				console.error(error.message);
			}
		});
		return;
	}

	const router = configureRouter();
	router.start(req.url, (error, routeState) => {
		if (error) {
			res.status(500).send(error.message);
			return;
		}

		const languageHelper = new LanguageHelper(req.headers["accept-language"] as string);
		const store = configureStore(router, {
			router: {
				previousRoute: null,
				route: routeState,
				transitionError: null,
				transitionRoute: null
			},
			settings: {
				error: "",
				language: "en",
				loaded: true,
				pending: false,
				translations: languageHelper.getTranslations()
			}
		});

		store.runSaga(rootSaga).toPromise().then(() => {
			// deep clone state because store will be changed during the second render in constructor
			const initialState = JSON.parse(JSON.stringify(store.getState()));

			// tslint:disable-next-line
			console.time("second render");

			// render again from the initial data
			const markup = renderToString(
				<Provider store={store} key="provider">
					<RouterProvider router={router}>
						<App/>
					</RouterProvider>
				</Provider>
			);

			// tslint:disable-next-line
			console.timeEnd("second render");

			res.status(200).send(renderHTML(markup, initialState));

		}).catch((err: any) => {
			console.error(err.message);
			res.status(500).send(err.message);
		});

		// tslint:disable-next-line
		console.time("first render");

		// first render to activate constructor to dispatch actions for loading initial data
		renderToString(
			<Provider store={store} key="provider">
				<RouterProvider router={router}>
					<App/>
				</RouterProvider>
			</Provider>
		);

		// tslint:disable-next-line
		console.timeEnd("first render");

		// dispatching END will cause the root saga to terminate after all fired tasks terminate
		store.close();
	});
});

app.listen(appConfig.port, appConfig.host, (err) => {
	if (err) {
		console.error(Chalk.bgRed(err));
	} else {
		console.info(Chalk.black.bgGreen(
			`\n\n💂  Listening at http://${appConfig.host}:${appConfig.port}\n`
		));
	}
});

function renderHTML(markup: string, initialState: Partial<IStore>): string {
	const manifest = require("../build/manifest.json");
	const html = renderToString(
		<Html markup={markup} manifest={manifest} initialState={initialState}/>
	);
	return `<!doctype html> ${html}`;
}

--#

--% /rts/src/index.html
<!--For client side rendering when ssr is false in config/main.js-->
<!DOCTYPE html>
<html lang="en">
<head>
</head>
<body>
	<div id="app"></div>
	<script src="/public/js/app.js"></script>
</body>
</html>

--#

--% /rts/src/favicon.ico
AAABAAEAICAAAAEAGACoDAAAFgAAACgAAAAgAAAAQAAAAAEAGAAAAAAAgAwAABMLAAATCwAAAAAAAAAAAAD////v1q3erUr3797////////////////////////////////////33rXepUrWjBDWjBDelBnelCHelBnWjBDWjBDWjBDWjBDWjBDWjBDWjBDWjBDWjBnenELv3sX////33rXWjAjmtWP/////////////////////////////////////////////9+/vxYzWjBDWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADWewDepVL/9/fenDrWhADv1qX////////////////////////////////////////////////////379bmrVrWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADWhAjWjBDWewDmvYTWjBDWhADv1q3////////////////////////////////////////////////////////////vzpTWjBDWhADWhADWhADWhADWhADWhADWhADelCnmvYTelCnWhADelDHWjBDWhADv1qX///////////////////////fvxYzmrVrmrVLmtWvv1rX/9+/////////////////33sXenDHWhADWhADWhADWhADWhADepUr35tbmvXvWhADWhADelCHWjBDWhADmvXv////////////////////mvXPWhADWhADWhADWhADWhADenDHvxYz/9+//////////////7+bepUrWhADWhADWjAjmvXP/9/fvzpzWhADWhADWhADelCHelBnWhADmrUr/////////////////7+belCHWhADWhADWhADWhADWhADWhADWhADenDHv1q3/////////////9+/mrVrelCn33rX////35sXWjAjWhADWhADWhADelCHelBnWhADWjBn3797////////////35s7WjBDWhADWhADWhADWhADWhADWhADWhADWhADWhADmvXP/9+//////////9+/3797/////9+benCnWhADWhADWhADWhADelCHejBnWhADWhADvzpT////////////379belBnWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADepUL3797/////////////9/fmrVLWhADWhADWhADWhADWhADelCHWjBDWhADWhADenDH///f///////////fepULWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADepTrmrVL35s7/////////9+/epUrWhADWhADWhADWhADWhADelCHWjBDWhADWhADWhADv1q3////////////vxYzWhADWhADWhADWhADWhADWhADWhADWhADWjBDvxYz////33r3epUL35tb/////////9+benDrWhADWhADWhADWhADenCnWjBDWhADWhADWhADenDH/9/f////////3797elBnWhADWhADWhADWhADWhADWhADenDr35sX////////////33r3mrVL3797////////379belBnWhADWhADWhADelCnWjBDWhADWhADWhADWhADvxZT////////////mvXPWhADWhADWhADWhADWhADmvXP/9+/////////////////////epUrepUr////////////33rXWjAjWhADWhADenDHWjBDWhADWhADWhADWhADelBn3797/////////9+/enDHWhADWhADelCn33rX////////////////////////v1qXWhAjWhADvxYz////////////mvXvWhADWhADelCnWjBDWhADWhADWhADWhADWhADmrVL////////3797enDrWhADmtWP/7+b////////////////////////35tbelBnWhADWhADWjAj35s7/////////9/fepTrWhADenCnWjBnWhADWhADWhADWhADWhADWhADvxYzvxYzWjAjWjBnvzpz/////////////////////////////9+/epULWhADWhADWhADWhADmrUr///f////////33r3WjAjelCnWjBDWhADWhADWhADWhADWhADWhADWhADWhADepUL379b////////////////////////////////mvXPWhADWhADWhADWhADWhADmrVL////////////////mtWPelCHWjBDWhADWhADWhADWhADWhADWhADWjAjvxYz///f////////////////////////////////v1q3WhAjWhADWhADWhADWhADWhADmtWv////////////////379bmrUrWjBDWhADWhADWhADWhADWhADenDH33r3////////////////////////////////////379belBnWhADWhADWhADWhADWhADWhADenDH///f/////////////////9+/WjBDWhADWhADWhADWhAjmvXP/9+//////////////////////////////////////9+/epULWhADWhADWhADWhADWhADWhADWhADWhADv1qX////////////////////WjBDWhADWhADelCH33rX////////////////////////////////////////////v1qXWhADWhADWhADWhADWhADWhADWhADWhADWhADelCH/7+b////////////////WjBDWhADWhADelBn379b/////////////////////////////////////////////9/fvxYTWjBDWhADWhADWhADWhADWhADWhADWhADWhADmrVL/9/f////////////WjBDWhADWhADWhADelCn3797////////////////////////////////////////////////35s7mrVLWhADWhADWhADWhADWhADWhADWhADWhADmtWP/9/f////////WjBDWhADWhADWhADWhADenDr/9+b////////////////////////////mvXv35s7////////////////33r3enDrWhADWhADWhADWhADWhADWhADWhADmrVL3797////WjBDWhADWhADWhADWhADWhADepUL/9+b////////////////////vxYzWhADelCH33rX////////////////33r3WhAjWhADWhADWhADWhADWhADWhADWhADelCHv1qXWjBDWhADWhADWhADWhADWhADWhADerUr/9+/////////////35s7WhAjWhADWhADWhAjmvXv/9/f/////////9/fenDrWhADWhADWhADWhADWhADWhADWhADWhADepTrWjBDWhADWhADWhADWhADWhADWhADWhADepUr/9+//////////9+/mvXPWhADWhADWhADWhADepUL33sX////////vxYTWhADWhADWhADWhADWhADWhADWhADWhADepULWjBDWhADWhADWhADWhADWhADWhADWhADWhADepUr37+b////////////vzpTWjBDWhADWhADWhADWjAjmtWv37973797ejBnWhADWhADWhADWhADWhADWhADWhADmrUrWjAjWhADWhADWhADWhADWhADWhADWhADWhADWhADenDH35tb////////////33r3elCnWhADWhADWhADWhADelCHvxYTepTrWhADWhADWhADWhADWhADWhADWhADmrVLelCHWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADelCH33r3////////////37+bmtWPWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADvxYTvzpzWhAjWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADWjAjvzpT////////////////v1qXelCnWhADWhADWhADWhADWhADWhADWhADWhADWhADWhADenDH/9+b////33rXerUrelCnelCHelCHelCHelCHelCHelCHelCHelCHejBnejBnmvXv///f/////////////7+bmvWvelBnWjBDWjBDWjBnWjBDWjBDWjBDelBnmrVr3797///8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==
--#

--% /rts/src/client.tsx
import * as e6p from "es6-promise";
(e6p as any).polyfill();
import "cross-fetch/polyfill";
import * as React from "react";
import * as ReactDOM from "react-dom";
import {Provider} from "react-redux";
import {RouterProvider} from "react-router5";
import {setStylesTarget} from "typestyle";
import {config as appConfig} from "../config";
import {App} from "./app/containers/App";
import {configureStore} from "./app/redux/configureStore";
import {setLanguage} from "./app/redux/modules/settingsActionCreators";
import {configureRouter} from "./app/routes/configureRouter";
import rootSaga from "./app/sagas/rootSaga";

const ReactHotLoader = appConfig.env !== "production"
	? require("react-hot-loader").AppContainer
	: ({ children }) => React.Children.only(children);

const renderOrHydrate = appConfig.ssr ? ReactDOM.hydrate : ReactDOM.render;

const router = configureRouter();
const store = configureStore(router, window.__INITIAL_STATE__);
let sagaTask = store.runSaga(rootSaga);
if (!appConfig.ssr) {
	store.dispatch(setLanguage.invoke("en"));
}
router.start();
renderOrHydrate(
	(
		<ReactHotLoader>
			<Provider store={store} key="provider">
				<RouterProvider router={router}>
					<App/>
				</RouterProvider>
			</Provider>
		</ReactHotLoader>
	),
	document.getElementById("app")
);

setStylesTarget(document.getElementById("styles-target"));

if ((module as any).hot) {
	(module as any).hot.accept("./app/containers/App", () => {
		const {App: NewApp} = require("./app/containers/App");
		renderOrHydrate(
			(
				<ReactHotLoader>
					<Provider store={store}>
						<RouterProvider router={router}>
							<NewApp/>
						</RouterProvider>
					</Provider>
				</ReactHotLoader>
			),
			document.getElementById("app")
		);
	});

	(module as any).hot.accept("./app/sagas/rootSaga", () => {
		sagaTask.cancel();
		sagaTask.toPromise().then(() => {
			sagaTask = store.runSaga(require("./app/sagas/rootSaga").default);
		});
	});
}

--#

--% /rts/src/app/helpers/setupCss.ts
import {cssRaw} from "typestyle";
import {Color} from "../constants/Color";
import {FontSize} from "../constants/FontSize";

export function setupCss(): void {
	cssRaw(`
	* {
		box-sizing: border-box;
	}

	html, body {
		font-family: Roboto;
		font-size: ${FontSize.MEDIUM};
		height: auto;
		margin: 0;
	}

	input[type="number"]::-webkit-outer-spin-button,
	input[type="number"]::-webkit-inner-spin-button {
		-webkit-appearance: none;
		margin: 0;
	}

	input[type="number"] {
		-moz-appearance: textfield;
	}

	img {
		image-rendering: -webkit-optimize-contrast;
	}

	a {
		color: ${Color.BLACK};
		text-decoration: none;
	}

	a:active, a:visited {
		color: ${Color.BLUE};
	}

	:focus {
		outline-color: ${Color.BLUE};
	}

	input, textarea, select, button {
		font-family: Roboto;
		font-size: ${FontSize.MEDIUM};
	}

	ul {
		list-style-type: none;
		padding: 0;
	}
`);
}

--#

--% /rts/src/app/helpers/withInitialState.tsx
import * as React from "react";

const Stage: React.FunctionComponent<{initialState: any}> = ({children, initialState}) => {
	const [state, setState] = React.useState(initialState);
	return (
		<div>{(children as any)(state, setState)}</div>
	);
};

const renderChildrenFn = (story, context) => (state, setState) => {
	const setCombinedState = (updatedState) => setState({...state, ...updatedState});
	return <div>{story({...context, state, setState: setCombinedState})}</div>;
};

export function withInitialState(initialState: any): (
	story: (...args: any) => JSX.Element,
	context: any
) => JSX.Element {
	return (story, context) => (
		<>
			<Stage initialState={initialState}>
				{renderChildrenFn(story, context)}
			</Stage>
			<div style={{backgroundColor: "#eee", marginTop: 30, maxWidth: 500, overflowX: "auto", padding: 10}}>
				initialState: {JSON.stringify(initialState)}
			</div>
		</>
	);
}

--#

--% /rts/src/app/helpers/JestBootstrap.ts
import * as Enzyme from "enzyme";
import Adapter from "enzyme-adapter-react-16";
import "jest-enzyme";

Enzyme.configure({adapter: new Adapter()});

(global as any).requestAnimationFrame = (callback: () => void) => {
	setTimeout(callback, 0);
};

(global as any).alert = jest.fn();

--#

--% /rts/src/app/helpers/LanguageHelper.ts
import fs from "fs";

export class LanguageHelper {
	private readonly preferredLanguage: string;

	constructor(private requestedLanguage: string) {
		this.preferredLanguage = this.requestedLanguage.split(",")[0];
	}

	public static getDefaultLanguage(): string {
		return "en";
	}

	public static isSupported(language: string): boolean {
		return LanguageHelper.getSupportedLanguages().indexOf(language) !== -1;
	}

	private static getLanguageFileLocation(language: string): string {
		return `${__dirname}/../translations/${language.toLowerCase()}.json`;
	}

	private static getSupportedLanguages(): string[] {
		return ["en", "de"];
	}

	private static getTranslations(language: string): object {
		return JSON.parse(fs.readFileSync(LanguageHelper.getLanguageFileLocation(language)).toString());
	}

	public getPreferredLanguage(): string {
		return this.preferredLanguage;
	}

	public getRequestedLanguage(): string {
		return this.requestedLanguage;
	}

	public getTranslations(): any {
		return LanguageHelper.getTranslations(
			LanguageHelper.isSupported(this.preferredLanguage) ? this.preferredLanguage : "en"
		);
	}
}

--#

--% /rts/src/app/helpers/LanguageHelper.test.ts
import {IFS} from "../../../__mocks__/.fs";

jest.mock("fs");
import {LanguageHelper} from "./LanguageHelper";

const languages: string[] = ["en, en", "en-GB, en;q=0.7", "de"];

describe("LanguageHelper", () => {

	describe("constructor", () => {
		it("accepts settings and we're able to get it", () => {
			const languageHelper = new LanguageHelper(languages[0]);
			expect(languageHelper.getRequestedLanguage()).toBe("en, en");
		});
	});

	describe("getPreferredLanguage()", () => {
		it("returns the most preferred settings", () => {
			const languageHelper = new LanguageHelper(languages[0]);
			expect(languageHelper.getPreferredLanguage()).toBe("en");
		});
	});

	describe("getDefaultLanguage()", () => {
		it("returns en", () => {
			expect(LanguageHelper.getDefaultLanguage()).toBe("en");
		});
	});

	describe("isSupported()", () => {
		it("returns true for en and de", () => {
			expect(LanguageHelper.isSupported("en")).toBeTruthy();
			expect(LanguageHelper.isSupported("de")).toBeTruthy();
			expect(LanguageHelper.isSupported("blah")).toBeFalsy();
		});
	});

	describe("getTranslations()", () => {
		let fs: IFS;

		beforeEach(() => {
			fs = require("fs");
		});

		it("returns settings data object for valid requested settings", () => {
			const languageHelper = new LanguageHelper("de");
			fs.__setFileContents("de.json", JSON.stringify({hello: "hallo"}));
			expect(languageHelper.getTranslations()).toEqual({hello: "hallo"});
		});

		it("returns default settings data object for invalid requested settings", () => {
			fs.__setFileContents("en.json", JSON.stringify({hello: "hello"}));
			const languageHelper = new LanguageHelper("invalid settings");
			expect(languageHelper.getTranslations()).toEqual({hello: "hello"});
		});
	});
});

--#

--% /rts/src/app/pages/StarsPage.test.tsx
import {shallow} from "enzyme";
import * as React from "react";
import {ISettingsState} from "../redux/modules/settingsModule";
import {loadStarsCount} from "../redux/modules/starsActionCreators";
import {IStarsState} from "../redux/modules/starsModule";
import {mapDispatchToProps, mapStateToProps, UnconnectedStarsPage} from "./StarsPage";

describe("<Stars />", () => {
	const translations = {
		fetchingStars: "Fetching Stars..."
	};

	it("maps state to props correctly", () => {
		const settings: ISettingsState = {
			error: "",
			language: "en",
			loaded: true,
			pending: false,
			translations: {"Fetching stars...": "Fetching Stars..."}
		};
		const stars: IStarsState = {
			count: 100,
			error: "",
			loaded: true,
			pending: false
		};
		const props = mapStateToProps({settings, stars});
		expect(props).toEqual({
			count: 100,
			error: "",
			loaded: true,
			pending: false,
			translations
		});
	});

	it("maps dispatch to props correctly", () => {
		const dispatch = jest.fn();
		const props = mapDispatchToProps(dispatch);
		expect(dispatch).not.toHaveBeenCalledWith(loadStarsCount.invoke(null));
		props.loadStarsCount();
		expect(dispatch).toHaveBeenCalledWith(loadStarsCount.invoke(null));
	});

	it("dispatches loadStars action before rendering if loaded is false", () => {
		const loadStars = jest.fn();
		expect(loadStars).not.toHaveBeenCalled();
		shallow(
			<UnconnectedStarsPage
				count={0}
				error={""}
				loaded={false}
				loadStarsCount={loadStars}
				pending={false}
				translations={translations}
			/>
		);
		expect(loadStars).toHaveBeenCalled();
	});

	it("does not dispatch loadStars action before rendering if loaded is true", () => {
		const loadStars = jest.fn();
		shallow(
			<UnconnectedStarsPage
				count={0}
				error={""}
				loaded={true}
				loadStarsCount={loadStars}
				pending={false}
				translations={translations}
			/>
		);
		expect(loadStars).not.toHaveBeenCalled();
	});

	it("shows fetching if pending is true", () => {
		const wrapper = shallow(
			<UnconnectedStarsPage
				count={0}
				error={""}
				loaded={false}
				loadStarsCount={jest.fn()}
				pending={true}
				translations={translations}
			/>
		);
		expect(wrapper.containsMatchingElement(<div>Fetching Stars...</div>)).toBeTruthy();
	});

	it("shows error if error is not empty", () => {
		const wrapper = shallow(
			<UnconnectedStarsPage
				count={0}
				error={"Error"}
				loaded={true}
				loadStarsCount={jest.fn()}
				pending={false}
				translations={translations}
			/>
		);
		expect(wrapper.containsMatchingElement(<div>Error</div>)).toBeTruthy();
	});

	it("shows stars count", () => {
		const count = 5;
		const wrapper = shallow(
			<UnconnectedStarsPage
				count={count}
				error={""}
				loaded={true}
				loadStarsCount={jest.fn()}
				pending={false}
				translations={translations}
			/>
		);
		expect(wrapper.containsMatchingElement(<div>{count}</div>)).toBeTruthy();
	});
});

--#

--% /rts/src/app/pages/StarsPage.tsx
import * as React from "react";
import {connect} from "react-redux";
import {Dispatch} from "redux";
import {createSelector} from "reselect";
import {Translator} from "../models/Translator";
import {ITranslator} from "../models/TranslatorInterfaces";
import {IStore} from "../redux/IStore";
import {loadStarsCount as loadStarsActionCreator} from "../redux/modules/starsActionCreators";
import {translationsSelector} from "../selectors/translationsSelector";

interface IStateToProps {
	count: number;
	error: string;
	loaded: boolean;
	pending: boolean;
	translations: {
		fetchingStars: string;
	};
}

interface IDispatchToProps {
	loadStarsCount: () => void;
}

interface IProps extends IStateToProps, IDispatchToProps {}

class StarsPage extends React.Component<IProps> {
	constructor(props: IStateToProps & IDispatchToProps) {
		super(props);
		if (!this.props.loaded) {
			this.props.loadStarsCount();
		}
	}

	public render(): JSX.Element {
		const {count, error, pending, translations} = this.props;
		if (pending) {
			return <div>{translations.fetchingStars}</div>;
		} else {
			return error ? <div>{error}</div> : <div>{count}</div>;
		}
	}
}

const componentTranslationsSelector = createSelector(
	translationsSelector,
	(translations) => {
		const translator: ITranslator = new Translator(translations);
		return {
			fetchingStars: translator.translate("Fetching stars...")
		};
	}
);

function mapStateToProps(state: Pick<IStore, "settings" | "stars">): IStateToProps {
	return {
		count: state.stars.count,
		error: state.stars.error,
		loaded: state.stars.loaded,
		pending: state.stars.pending,
		translations: componentTranslationsSelector(state)
	};
}

function mapDispatchToProps(dispatch: Dispatch): IDispatchToProps {
	return {
		loadStarsCount: () => dispatch(loadStarsActionCreator.invoke(null))
	};
}

const connected = connect(mapStateToProps, mapDispatchToProps)(StarsPage);
export {connected as StarsPage, mapDispatchToProps, mapStateToProps, StarsPage as UnconnectedStarsPage};

--#

--% /rts/src/app/pages/CounterPage.test.tsx
import {shallow} from "enzyme";
import * as React from "react";
import {
	decrement as decrementActionCreator,
	increment as incrementActionCreator
} from "../redux/modules/counterActionCreators";
import {ICounterState} from "../redux/modules/counterModule";
import {ISettingsState} from "../redux/modules/settingsModule";
import {mapDispatchToProps, mapStateToProps, UnconnectedCounterPage} from "./CounterPage";

describe("<Counter />", () => {
	const translations = {
		counter: "Counter",
		decrement: "Decrement",
		increment: "Increment"
	};

	it("maps state to props correctly", () => {
		const settings: ISettingsState = {
			error: "",
			language: "en",
			loaded: true,
			pending: false,
			translations: {Counter: "Counter", Decrement: "Decrement", Increment: "Increment"}
		};
		const counter: ICounterState = {
			count: 10,
			error: "",
			loaded: false,
			pending: false
		};
		const props = mapStateToProps({counter, settings});
		expect(props).toEqual({
			count: 10,
			translations
		});
	});

	it("map dispatch to props correctly", () => {
		const dispatch = jest.fn();
		const props = mapDispatchToProps(dispatch);

		expect(dispatch).not.toHaveBeenCalledWith(decrementActionCreator());
		props.decrement();
		expect(dispatch).toHaveBeenCalledWith(decrementActionCreator());

		expect(dispatch).not.toHaveBeenCalledWith(incrementActionCreator());
		props.increment();
		expect(dispatch).toHaveBeenCalledWith(incrementActionCreator());
	});

	it("calls increment() when increment button is clicked", () => {
		const spied = jest.fn();
		const wrapper = shallow(
			<UnconnectedCounterPage count={0} increment={spied} decrement={jest.fn()} translations={translations}/>
		);
		expect(wrapper.find({name: "incBtn"})).toBeDefined();
		expect(spied).not.toHaveBeenCalled();
		wrapper.find({name: "incBtn"}).simulate("click");
		expect(spied).toHaveBeenCalled();
	});

	it("calls decrement() when decrement button is clicked", () => {
		const spied = jest.fn();
		const wrapper = shallow(
			<UnconnectedCounterPage count={0} increment={jest.fn()} decrement={spied} translations={translations}/>
		);
		expect(wrapper.find({name: "decBtn"})).toBeDefined();
		expect(spied).not.toHaveBeenCalled();
		wrapper.find({name: "decBtn"}).simulate("click");
		expect(spied).toHaveBeenCalled();
	});
});

--#

--% /rts/src/app/pages/AboutPage.tsx
import * as React from "react";
import {connect} from "react-redux";
import {Dispatch} from "redux";
import {createSelector} from "reselect";
import {Button} from "../components/Button";
import {Translator} from "../models/Translator";
import {ITranslator} from "../models/TranslatorInterfaces";
import {IStore} from "../redux/IStore";
import {setLanguage as setLanguageActionCreator} from "../redux/modules/settingsActionCreators";
import {TLanguage} from "../redux/modules/settingsModule";
import {translationsSelector} from "../selectors/translationsSelector";

interface IStateToProps {
	language: string;
	translations: {
		aboutUs: string;
		change: string;
		currentLanguage: string;
	};
}

interface IDispatchToProps {
	setLanguage: (language: string) => void;
}

interface IProps extends IStateToProps, IDispatchToProps {}

class AboutPage extends React.Component<IProps> {
	constructor(props: IStateToProps & IDispatchToProps) {
		super(props);
		this.handleLanguageChange = this.handleLanguageChange.bind(this);
	}

	public render(): JSX.Element {
		const {language, translations} = this.props;
		return (
			<div>
				<h3>{translations.aboutUs}: {language}</h3>
				<Button onClick={this.handleLanguageChange}>
					{translations.change}
				</Button>
				<h4>{translations.currentLanguage}</h4>
			</div>
		);
	}

	private handleLanguageChange(): void {
		const language = this.props.language === "en" ? "de" : "en";
		this.props.setLanguage(language);
	}
}

const componentTranslationsSelector = createSelector(
	translationsSelector,
	(translations) => {
		const translator: ITranslator = new Translator(translations);
		return {
			aboutUs: translator.translate("About us"),
			change: translator.translate("Change language"),
			currentLanguage: translator.translate("Current language")
		};
	}
);

export const mapStateToProps = (state: Pick<IStore, "settings">): IStateToProps => ({
	language: state.settings.language,
	translations: componentTranslationsSelector(state)
});

export const mapDispatchToProps = (dispatch: Dispatch): IDispatchToProps => {
	return {
		setLanguage: (language: TLanguage) => dispatch(setLanguageActionCreator.invoke(language))
	};
};

const connected = connect(mapStateToProps, mapDispatchToProps)(AboutPage);
export {AboutPage as UnconnectedAboutPage, connected as AboutPage};

--#

--% /rts/src/app/pages/AboutPage.test.tsx
import {shallow} from "enzyme";
import * as React from "react";
import {Button} from "../components/Button";
import {setLanguage as setLanguageActionCreator} from "../redux/modules/settingsActionCreators";
import {ISettingsState} from "../redux/modules/settingsModule";
import {mapDispatchToProps, mapStateToProps, UnconnectedAboutPage} from "./AboutPage";

/* tslint:disable:no-empty jsx-no-lambda */
describe("<AboutPage />", () => {
	const translations = {
		aboutUs: "About Us",
		change: "Change",
		currentLanguage: "Current Language"
	};

	it("maps state to props correctly", () => {
		const settings: ISettingsState = {
			error: "",
			language: "en",
			loaded: true,
			pending: false,
			translations: {"About us": "About Us", "Change language": "Change", "Current language": "Current Language"}
		};
		const props = mapStateToProps({settings});
		expect(props.language).toBe("en");
		expect(props.translations).toEqual(translations);
	});

	it("maps dispatch to props correctly", () => {
		const dispatch = jest.fn();
		const props = mapDispatchToProps(dispatch);
		expect(dispatch).not.toHaveBeenCalledWith(setLanguageActionCreator.invoke("de"));
		props.setLanguage("de");
		expect(dispatch).toHaveBeenCalledWith(setLanguageActionCreator.invoke("de"));
	});

	it("calls setLanguage() to de", () => {
		const setLanguage = jest.fn();
		const wrapper = shallow(
			<UnconnectedAboutPage setLanguage={setLanguage} language="en" translations={translations}/>
		);
		expect(wrapper.find(Button)).toBeDefined();
		expect(setLanguage).not.toHaveBeenCalled();
		wrapper.find(Button).simulate("click");
		expect(setLanguage).toHaveBeenCalledWith("de");
	});

	it("calls setLanguage() to en", () => {
		const setLanguage = jest.fn();
		const wrapper = shallow(
			<UnconnectedAboutPage setLanguage={setLanguage} language="de" translations={translations}/>
		);
		expect(wrapper.find(Button)).toBeDefined();
		expect(setLanguage).not.toHaveBeenCalled();
		wrapper.find(Button).simulate("click");
		expect(setLanguage).toHaveBeenCalledWith("en");
	});
});

--#

--% /rts/src/app/pages/HomePage.test.tsx
import {shallow} from "enzyme";
import * as React from "react";
import {ISettingsState} from "../redux/modules/settingsModule";
import {mapStateToProps, UnconnectedHomePage} from "./HomePage";
describe("<HomePage />", () => {
	const translations = {
		hello: "Hello!"
	};

	it("maps state to props correctly", () => {
		const settings: ISettingsState = {
			error: "",
			language: "en",
			loaded: true,
			pending: false,
			translations: {Hello: "Hello!"}
		};
		const props = mapStateToProps({settings});
		expect(props).toEqual({
			translations: {
				hello: "Hello!"
			}
		});
	});

	it("says hello", () => {
		const wrapper = shallow(<UnconnectedHomePage translations={translations}/>);
		expect(wrapper.find("p")).toHaveText("Hello!");
	});
});

--#

--% /rts/src/app/pages/CounterPage.tsx
import * as React from "react";
import {connect} from "react-redux";
import {Dispatch} from "redux";
import {createSelector} from "reselect";
import {stylesheet} from "typestyle";
import {Button} from "../components/Button";
import {Translator} from "../models/Translator";
import {ITranslator} from "../models/TranslatorInterfaces";
import {IStore} from "../redux/IStore";
import {
	decrement as decrementActionCreator,
	increment as incrementActionCreator
} from "../redux/modules/counterActionCreators";
import {translationsSelector} from "../selectors/translationsSelector";

const classNames = stylesheet({
	moveRight: {
		marginLeft: "8px"
	}
});

interface IStateToProps {
	count: number;
	translations: {
		counter: string;
		decrement: string;
		increment: string;
	};
}

interface IDispatchToProps {
	decrement: () => void;
	increment: () => void;
}

export interface IProps extends IStateToProps, IDispatchToProps {}

class CounterPage extends React.Component<IProps> {
	public render(): JSX.Element {
		const {count, decrement, increment, translations} = this.props;
		return (
			<div>
				<h4>{translations.counter}</h4>
				<Button name="decBtn" onClick={decrement} disabled={count <= 0}>
					{translations.decrement}
				</Button>
				<Button className={classNames.moveRight} name="incBtn" onClick={increment}>
					{translations.increment}
				</Button>
				<p>{count}</p>
			</div>
		);
	}
}

const componentTranslationsSelector = createSelector(
	translationsSelector,
	(translations) => {
		const translator: ITranslator = new Translator(translations);
		return {
			counter: translator.translate("Counter"),
			decrement: translator.translate("Decrement"),
			increment: translator.translate("Increment")
		};
	}
);

function mapStateToProps(state: Pick<IStore, "counter" | "settings">): IStateToProps {
	return {
		count: state.counter.count,
		translations: componentTranslationsSelector(state)
	};
}

function mapDispatchToProps(dispatch: Dispatch): IDispatchToProps {
	return {
		decrement: () => dispatch(decrementActionCreator()),
		increment: () => dispatch(incrementActionCreator())
	};
}

const connected = connect(mapStateToProps, mapDispatchToProps)(CounterPage);

export {connected as CounterPage, CounterPage as UnconnectedCounterPage, mapDispatchToProps, mapStateToProps};

--#

--% /rts/src/app/pages/HomePage.tsx
import * as React from "react";
import {connect} from "react-redux";
import {createSelector} from "reselect";
import {stylesheet} from "typestyle";
import {Color} from "../constants/Color";
import crazyImage from "../images/crazy.png";
import {Translator} from "../models/Translator";
import {ITranslator} from "../models/TranslatorInterfaces";
import {IStore} from "../redux/IStore";
import {translationsSelector} from "../selectors/translationsSelector";

const classNames = stylesheet({
	container: {
		color: Color.BLUE,
		textAlign: "center"
	}
});

interface IStateToProps {
	translations: {
		hello: string;
	};
}

class HomePage extends React.Component<IStateToProps> {
	public render(): JSX.Element {
		const {translations} = this.props;
		return (
			<div className={classNames.container}>
				<a href={"https://www.crazy-factory.com"}>
					<img alt={"crazy logo"} src={crazyImage}/>
				</a>
				<p>{translations.hello}</p>
			</div>
		);
	}
}

const componentTranslationsSelector = createSelector(
	translationsSelector,
	(translations) => {
		const translator: ITranslator = new Translator(translations);
		return {
			hello: translator.translate("Hello")
		};
	}
);

function mapStateToProps(state: Pick<IStore, "settings">): IStateToProps {
	return {
		translations: componentTranslationsSelector(state)
	};
}

const connected = connect(mapStateToProps)(HomePage);
export {connected as HomePage, HomePage as UnconnectedHomePage, mapStateToProps};

--#

--% /rts/src/app/sagas/StarsSaga.test.ts
jest.mock("./dummyApi");
import {runSaga} from "redux-saga";
import {dummyApi} from "./dummyApi";
import {StarsSaga} from "./StarsSaga";

describe("StarsSaga", () => {
	describe("fetchStarsCount", () => {
		it("gets stars count and sets fulfilled", () => {
			expect.assertions(1);
			const dispatched = [];
			(dummyApi as any).getStarsCount.mockResolvedValue(10);
			return runSaga(
				{
					dispatch: (action) => dispatched.push(action)
				},
				(new StarsSaga()).fetchStarsCount
			).toPromise().then(() => {
				expect(dispatched).toEqual([
					{payload: null, type: "STARS/LOAD_STARS_COUNT_PENDING"},
					{payload: 10, type: "STARS/LOAD_STARS_COUNT_FULFILLED"}
				]);
			});
		});

		it("gets rejected and sets rejected", () => {
			expect.assertions(1);
			const dispatched = [];
			(dummyApi as any).getStarsCount.mockRejectedValue("Error");
			return runSaga(
				{
					dispatch: (action) => dispatched.push(action)
				},
				(new StarsSaga()).fetchStarsCount
			).toPromise().then(() => {
				expect(dispatched).toEqual([
					{payload: null, type: "STARS/LOAD_STARS_COUNT_PENDING"},
					{message: "Error", payload: null, type: "STARS/LOAD_STARS_COUNT_REJECTED"}
				]);
			});
		});
	});
});

--#

--% /rts/src/app/sagas/StarsSaga.ts
import autobind from "autobind-decorator";
import {call, CallEffect, ForkEffect, put, PutEffect, takeLatest} from "redux-saga/effects";
import {getType} from "typesafe-actions";
import {loadStarsCount} from "../redux/modules/starsActionCreators";
import {BaseSaga} from "./BaseSaga";
import {dummyApi} from "./dummyApi";

export class StarsSaga extends BaseSaga {
	@autobind
	public *fetchStarsCount(): IterableIterator<CallEffect | PutEffect<any>> {
		try {
			yield put(loadStarsCount.setPending(null));
			const count = yield call(dummyApi.getStarsCount);
			yield put(loadStarsCount.setFulfilled(count));
		} catch (e) {
			yield put(loadStarsCount.setRejected(null, e.toString()));
		}
	}

	protected *registerListeners(): IterableIterator<ForkEffect> {
		yield takeLatest(getType(loadStarsCount.invoke), this.fetchStarsCount);
	}
}

--#

--% /rts/src/app/sagas/SettingsSaga.ts
import autobind from "autobind-decorator";
import {call, CallEffect, ForkEffect, put, PutEffect, takeLatest} from "redux-saga/effects";
import {getType} from "typesafe-actions";
import {setLanguage} from "../redux/modules/settingsActionCreators";
import {BaseSaga} from "./BaseSaga";
import {dummyApi} from "./dummyApi";

export class SettingsSaga extends BaseSaga {
	@autobind
	public *fetchTranslations(
		action: ReturnType<typeof setLanguage.invoke>
	): IterableIterator<CallEffect | PutEffect<any>> {
		try {
			yield put(setLanguage.setPending(null));
			const translations = yield call(dummyApi.getTranslations, action.payload);
			yield put(setLanguage.setFulfilled(translations));
		} catch (e) {
			yield put(setLanguage.setRejected(null, e.toString()));
		}
	}

	protected *registerListeners(): IterableIterator<ForkEffect> {
		yield takeLatest(getType(setLanguage.invoke), this.fetchTranslations);
	}
}

--#

--% /rts/src/app/sagas/dummyApi.ts
import {ITranslations} from "../redux/modules/settingsModule";

// Don't forget to enable this in production!
// tslint:disable:no-http-string

export const dummyApi = {
	getStarsCount: (): Promise<number> => {
		return fetch("https://api.github.com/repos/crazyfactory/ts-react-boilerplate")
			.then((res) => res.json())
			.then((json) => json.stargazers_count);
	},
	getTranslations: (payload: string): Promise<ITranslations> => {
		return fetch(`http://localhost:__TEMPLATE_SERVER_PORT__/translations/${payload}`).then((res) => res.json());
	}
};

--#

--% /rts/src/app/sagas/BaseSaga.ts
import {fork, ForkEffect} from "redux-saga/effects";

export abstract class BaseSaga {
	constructor() {
		this.registerListeners = this.registerListeners.bind(this);
	}

	public watch(): ForkEffect {
		return fork(this.registerListeners);
	}

	protected abstract registerListeners(): IterableIterator<ForkEffect>;
}

--#

--% /rts/src/app/sagas/rootSaga.ts
import {all, AllEffect} from "redux-saga/effects";
import {SettingsSaga} from "./SettingsSaga";
import {StarsSaga} from "./StarsSaga";

export default function* rootSaga(): IterableIterator<AllEffect<any>> {
	yield all([
		(new SettingsSaga()).watch(),
		(new StarsSaga()).watch()
	]);
}

--#

--% /rts/src/app/sagas/SettingsSaga.test.ts
jest.mock("./dummyApi");
import {runSaga} from "redux-saga";
import {dummyApi} from "./dummyApi";
import {SettingsSaga} from "./SettingsSaga";

describe("SettingsSaga", () => {
	describe("fetchTranslations", () => {
		it("gets translations and sets fulfilled", () => {
			expect.assertions(1);
			const dispatched = [];
			(dummyApi as any).getTranslations.mockResolvedValue({"Translation Key": "Translation Value"});
			return runSaga(
				{
					dispatch: (action) => dispatched.push(action)
				},
				(new SettingsSaga()).fetchTranslations,
				{
					payload: "en",
					type: "SETTINGS/SET_LANGUAGE"
				}
			).toPromise().then(() => {
				expect(dispatched).toEqual([
					{payload: null, type: "SETTINGS/SET_LANGUAGE_PENDING"},
					{payload: {"Translation Key": "Translation Value"}, type: "SETTINGS/SET_LANGUAGE_FULFILLED"}
				]);
			});
		});

		it("gets rejected and sets rejected", () => {
			expect.assertions(1);
			const dispatched = [];
			(dummyApi as any).getTranslations.mockRejectedValue("Error");
			return runSaga(
				{
					dispatch: (action) => dispatched.push(action)
				},
				(new SettingsSaga()).fetchTranslations,
				{
					payload: "en",
					type: "SETTINGS/SET_LANGUAGE"
				}
			).toPromise().then(() => {
				expect(dispatched).toEqual([
					{payload: null, type: "SETTINGS/SET_LANGUAGE_PENDING"},
					{message: "Error", payload: null, type: "SETTINGS/SET_LANGUAGE_REJECTED"}
				]);
			});
		});
	});
});

--#

--% /rts/src/app/redux/rootReducer.ts
import {CombinedState, combineReducers, Reducer} from "redux";
import {router5Reducer} from "redux-router5";
import {IStore} from "./IStore";
import {counterReducer} from "./modules/counterModule";
import {settingsReducer} from "./modules/settingsModule";
import {starsReducer} from "./modules/starsModule";

const rootReducer: Reducer<CombinedState<IStore>> = combineReducers<IStore>({
	counter: counterReducer,
	router: router5Reducer,
	settings: settingsReducer,
	stars: starsReducer
});

export default rootReducer;

--#

--% /rts/src/app/redux/configureStore.ts
import {init} from "@sentry/browser";
import {applyMiddleware, compose, createStore, Middleware, Store} from "redux";
import {createLogger} from "redux-logger";
import {router5Middleware} from "redux-router5";
import createSagaMiddleware, {END, Task} from "redux-saga";
import {Router} from "router5";
import {config as appConfig} from "../../../config";
import {IStore} from "./IStore";
import {sentryMiddleware} from "./middlewares/sentryMiddleware";
import rootReducer from "./rootReducer";

interface IExtendedStore extends Store<Partial<IStore>> {
	close: () => void;
	runSaga: (rootSaga: any) => Task;
}

export function configureStore(router: Router, initialState?: Partial<IStore>): IExtendedStore {
	const sagaMiddleware = createSagaMiddleware();
	const middlewares: Middleware[] = [
		router5Middleware(router),
		sagaMiddleware
	];

	/** Add Only Dev. Middlewares */
	if (appConfig.env !== "production" && process.env.BROWSER) {
		const logger = createLogger();
		middlewares.push(logger);
	}

	if (appConfig.sentry && appConfig.sentry.dsn && process.env.BROWSER) {
		middlewares.unshift(sentryMiddleware);

		init({
			dsn: appConfig.sentry.dsn,
			...appConfig.sentry.options
		});
	}

	const composeEnhancers = (appConfig.env !== "production" &&
		typeof window === "object" &&
		(typeof window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ === "function") &&
		window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__({shouldHotReload: false})) || compose;

	const store = createStore(rootReducer, initialState, composeEnhancers(
		applyMiddleware(...middlewares)
	));

	if (appConfig.env === "development" && (module as any).hot) {
		(module as any).hot.accept("./rootReducer", () => {
			store.replaceReducer((require("./rootReducer").default));
		});
	}

	return {
		...store,
		close: () => store.dispatch(END),
		runSaga: sagaMiddleware.run
	};
}

--#

--% /rts/src/app/redux/IStore.ts
import {RouterState} from "redux-router5";
import {ICounterState} from "./modules/counterModule";
import {ISettingsState} from "./modules/settingsModule";
import {IStarsState} from "./modules/starsModule";

export interface IStore {
	counter: ICounterState;
	router: RouterState;
	settings: ISettingsState;
	stars: IStarsState;
}

--#

--% /rts/src/app/redux/modules/starsActionCreators.ts
import {createAsyncActions} from "./baseModule";

// tslint:disable-next-line:export-name
export const loadStarsCount = createAsyncActions(
	"STARS/LOAD_STARS_COUNT",
	"STARS/LOAD_STARS_COUNT_PENDING",
	"STARS/LOAD_STARS_COUNT_FULFILLED",
	"STARS/LOAD_STARS_COUNT_REJECTED"
)<null, null, number, null>();

--#

--% /rts/src/app/redux/modules/counterActionCreators.ts
import {createAction} from "typesafe-actions";

export const increment = createAction("COUNTER/INCREMENT")();
export const decrement = createAction("COUNTER/DECREMENT")();

--#

--% /rts/src/app/redux/modules/settingsActionCreators.ts
import {createAsyncActions} from "./baseModule";
import {ITranslations, TLanguage} from "./settingsModule";

// tslint:disable-next-line:export-name
export const setLanguage = createAsyncActions(
	"SETTINGS/SET_LANGUAGE",
	"SETTINGS/SET_LANGUAGE_PENDING",
	"SETTINGS/SET_LANGUAGE_FULFILLED",
	"SETTINGS/SET_LANGUAGE_REJECTED"
)<TLanguage, null, ITranslations, null>();

--#

--% /rts/src/app/redux/modules/counterModule.test.ts
import {decrement, increment} from "./counterActionCreators";
import {counterReducer, ICounterState} from "./counterModule";

describe("counterModule", () => {
	describe("reducer", () => {
		it("returns initial state when state and action type are undefined", () => {
			const initialState: ICounterState = {
				count: 0,
				error: "",
				loaded: false,
				pending: false
			};
			expect(counterReducer(undefined, {type: undefined})).toEqual(initialState);
		});

		it("handles action of type INCREMENT", () => {
			const state: ICounterState = {
				count: 0,
				error: "",
				loaded: false,
				pending: false
			};
			expect(counterReducer(state, increment())).toEqual({
				count: 1,
				error: "",
				loaded: false,
				pending: false
			});
		});

		it("handles action of type DECREMENT when count is more than 0", () => {
			const state: ICounterState = {
				count: 2,
				error: "",
				loaded: false,
				pending: false
			};
			expect(counterReducer(state, decrement())).toEqual({
				count: 1,
				error: "",
				loaded: false,
				pending: false
			});
		});

		it("handles action of type DECREMENT when count is 0", () => {
			const state: ICounterState = {
				count: 0,
				error: "",
				loaded: false,
				pending: false
			};
			expect(counterReducer(state, decrement())).toEqual({
				count: 0,
				error: "",
				loaded: false,
				pending: false
			});
		});

		it("handles actions with unknown type", () => {
			const state: ICounterState = {
				count: 10,
				error: "",
				loaded: false,
				pending: false
			};
			expect(counterReducer(state, {type: "unknown"} as any)).toBe(state);
		});
	});
});

--#

--% /rts/src/app/redux/modules/starsModule.ts
import {ActionType, getType} from "typesafe-actions";
import {IBaseState} from "./baseModule";
import * as starsActionCreators from "./starsActionCreators";

export interface IStarsState extends IBaseState {
	count: number;
}

const initialState: IStarsState = {
	count: 0,
	error: "",
	loaded: false,
	pending: false
};

export function starsReducer(
	state: IStarsState = initialState,
	action: ActionType<typeof starsActionCreators>
): IStarsState {
	switch (action.type) {
		case getType(starsActionCreators.loadStarsCount.setPending):
			return {
				...state,
				pending: true
			};
		case getType(starsActionCreators.loadStarsCount.setFulfilled):
			return {
				...state,
				count: action.payload,
				error: "",
				loaded: true,
				pending: false
			};
		case getType(starsActionCreators.loadStarsCount.setRejected):
			return {
				...state,
				error: action.message,
				loaded: true,
				pending: false
			};
		default:
			return state;
	}
}

--#

--% /rts/src/app/redux/modules/settingsModule.test.ts
import {setLanguage} from "./settingsActionCreators";
import {ISettingsState, settingsReducer} from "./settingsModule";

describe("settingsModule", () => {
	describe("reducer", () => {
		it("returns initial state when state and action type are undefined", () => {
			const initialState: ISettingsState = {
				error: "",
				language: "en",
				loaded: false,
				pending: false,
				translations: {}
			};
			expect(settingsReducer(undefined, {type: undefined})).toEqual(initialState);
		});

		it("handles invoke action", () => {
			const state: ISettingsState = {
				error: "",
				language: "en",
				loaded: false,
				pending: false,
				translations: {}
			};
			expect(settingsReducer(state, setLanguage.invoke("de"))).toEqual({
				error: "",
				language: "de",
				loaded: false,
				pending: false,
				translations: {}
			});
		});

		it("handles pending action", () => {
			const state: ISettingsState = {
				error: "",
				language: "en",
				loaded: false,
				pending: false,
				translations: {}
			};
			expect(settingsReducer(state, setLanguage.setPending(null))).toEqual({
				error: "",
				language: "en",
				loaded: false,
				pending: true,
				translations: {}
			});
		});

		it("handles fulfilled action", () => {
			const state: ISettingsState = {
				error: "",
				language: "de",
				loaded: false,
				pending: true,
				translations: {}
			};
			expect(settingsReducer(state, setLanguage.setFulfilled({Hello: "Hallo"}))).toEqual({
				error: "",
				language: "de",
				loaded: true,
				pending: false,
				translations: {Hello: "Hallo"}
			});
		});

		it("handles rejected action", () => {
			const state: ISettingsState = {
				error: "",
				language: "de",
				loaded: false,
				pending: true,
				translations: {}
			};
			expect(settingsReducer(state, setLanguage.setRejected(null, "Error"))).toEqual({
				error: "Error",
				language: "de",
				loaded: true,
				pending: false,
				translations: {}
			});
		});

		it("handles actions with unknown type", () => {
			const state: ISettingsState = {
				error: "",
				language: "en",
				loaded: false,
				pending: false,
				translations: {Hello: "Hallo"}
			};
			expect(settingsReducer(state, {type: "unknown"} as any)).toBe(state);
		});
	});
});

--#

--% /rts/src/app/redux/modules/settingsModule.ts
import {ActionType, getType} from "typesafe-actions";
import {IBaseState} from "./baseModule";
import * as settingsActionCreators from "./settingsActionCreators";

export type TLanguage = "en" | "de";

export interface ITranslations {
	[key: string]: string;
}

export interface ISettingsState extends IBaseState {
	language: TLanguage;
	translations: ITranslations;
}

const initialState: ISettingsState = {
	error: "",
	language: "en",
	loaded: false,
	pending: false,
	translations: {}
};

export function settingsReducer(
	state: ISettingsState = initialState,
	action: ActionType<typeof settingsActionCreators>
): ISettingsState {
	switch (action.type) {
		case getType(settingsActionCreators.setLanguage.invoke):
			return {
				...state,
				language: action.payload
			};
		case getType(settingsActionCreators.setLanguage.setPending):
			return {
				...state,
				pending: true
			};
		case getType(settingsActionCreators.setLanguage.setFulfilled):
			return {
				...state,
				error: "",
				loaded: true,
				pending: false,
				translations: action.payload
			};
		case getType(settingsActionCreators.setLanguage.setRejected):
			return {
				...state,
				error: action.message,
				loaded: true,
				pending: false
			};
		default:
			return state;
	}
}

--#

--% /rts/src/app/redux/modules/baseModule.ts
import {Action} from "redux";

export interface IAction<P, T = string, M = string> extends Action<T> {
	message?: M;
	payload?: P;
}

export interface IBaseState {
	error: string;
	loaded: boolean;
	pending: boolean;
}

export type TAsyncActionCreator<T extends string, P> = (payload: P) => IAction<P, T>;
export type TRejectedActionCreator<T extends string, P> = (payload: P, message: string) => IAction<P, T>;

export interface IAsyncActionsBuilder<
	T1 extends string,
	T2 extends string,
	T3 extends string,
	T4 extends string,
	P1,
	P2,
	P3,
	P4
> {
	invoke: TAsyncActionCreator<T1, P1>;
	setFulfilled: TAsyncActionCreator<T3, P3>;
	setPending: TAsyncActionCreator<T2, P2>;
	setRejected: TRejectedActionCreator<T4, P4>;
}

export type TGetAsyncAction<T1 extends string, T2 extends string, T3 extends string, T4 extends string> =
	<P1, P2, P3, P4>() => IAsyncActionsBuilder<T1, T2, T3, T4, P1, P2, P3, P4>;

export function createAsyncActions<T1 extends string, T2 extends string, T3 extends string, T4 extends string>(
	baseType: T1,
	pendingType: T2,
	fulfilledType: T3,
	rejectedType: T4
): TGetAsyncAction<T1, T2, T3, T4> {

	function builder<P1, P2, P3, P4>(): IAsyncActionsBuilder<T1, T2, T3, T4, P1, P2, P3, P4> {
		const invokeActionCreator = (payload: P1): IAction<P1, T1> => ({type: baseType, payload});
		invokeActionCreator.getType = () => baseType;

		const fulfilledActionCreator = (payload: P3): IAction<P3, T3> => ({type: fulfilledType, payload});
		fulfilledActionCreator.getType = () => fulfilledType;

		const pendingActionCreator = (payload: P2): IAction<P2, T2> => ({type: pendingType, payload});
		pendingActionCreator.getType = () => pendingType;

		const rejectedActionCreator = (payload: P4, message: string): IAction<P4, T4> => (
			{type: rejectedType, message, payload}
		);
		rejectedActionCreator.getType = () => rejectedType;

		return {
			invoke: invokeActionCreator,
			setFulfilled: fulfilledActionCreator,
			setPending: pendingActionCreator,
			setRejected: rejectedActionCreator
		};
	}

	// tslint:disable-next-line:prefer-object-spread
	return Object.assign(builder, {});
}

--#

--% /rts/src/app/redux/modules/counterModule.ts
import {ActionType, getType} from "typesafe-actions";
import {IBaseState} from "./baseModule";
import * as counterActionCreators from "./counterActionCreators";

export interface ICounterState extends IBaseState {
	count: number;
}

const initialState: ICounterState = {
	count: 0,
	error: "",
	loaded: false,
	pending: false
};

export function counterReducer(
	state: ICounterState = initialState,
	action: ActionType<typeof counterActionCreators>
): ICounterState {
	switch (action.type) {
		case getType(counterActionCreators.increment):
			return {
				...state,
				count: state.count + 1
			};
		case getType(counterActionCreators.decrement):
			return {
				...state,
				count: ((state.count - 1 > 0) ? state.count - 1 : 0)
			};
		default:
			return state;
	}
}

--#

--% /rts/src/app/redux/modules/starsModule.test.ts
import {loadStarsCount} from "./starsActionCreators";
import {IStarsState, starsReducer} from "./starsModule";

describe("starsModule", () => {
	describe("reducer", () => {
		it("returns initial state when state and action type are undefined", () => {
			const initialState: IStarsState = {
				count: 0,
				error: "",
				loaded: false,
				pending: false
			};
			expect(starsReducer(undefined, {type: undefined})).toEqual(initialState);
		});

		it("handles pending action", () => {
			const state: IStarsState = {
				count: 0,
				error: "",
				loaded: false,
				pending: false
			};
			expect(starsReducer(state, loadStarsCount.setPending(null))).toEqual({
				count: 0,
				error: "",
				loaded: false,
				pending: true
			});
		});

		it("handles fulfilled action", () => {
			const state: IStarsState = {
				count: 0,
				error: "",
				loaded: false,
				pending: true
			};
			expect(starsReducer(state, loadStarsCount.setFulfilled(10))).toEqual({
				count: 10,
				error: "",
				loaded: true,
				pending: false
			});
		});

		it("handles rejected action", () => {
			const state: IStarsState = {
				count: 0,
				error: "",
				loaded: false,
				pending: true
			};
			expect(starsReducer(state, loadStarsCount.setRejected(null, "Error"))).toEqual({
				count: 0,
				error: "Error",
				loaded: true,
				pending: false
			});
		});

		it("handles actions with unknown type", () => {
			const state: IStarsState = {
				count: 10,
				error: "",
				loaded: true,
				pending: false
			};
			expect(starsReducer(state, {type: "unknown"} as any)).toBe(state);
		});
	});
});

--#

--% /rts/src/app/redux/middlewares/sentryMiddleware.ts
import {addBreadcrumb} from "@sentry/browser";
import {Middleware, Store} from "redux";
import {IStore} from "../IStore";

export const sentryMiddleware: Middleware = (store: Store<IStore>) => (next) => (action) => {
	addBreadcrumb({
		category: "redux-action",
		data: {
			action,
			store: store.getState()
		},
		message: action.type
	});
	return next(action);
};

--#

--% /rts/src/app/images/crazy.png
iVBORw0KGgoAAAANSUhEUgAAATYAAABmCAMAAAB2m03YAAAABGdBTUEAALGPC/xhBQAAAAFzUkdCAK7OHOkAAAA/UExURQAAACo2OwCM0io2Oyo2Oyo2Oyo2Oyo2Oyo2Ox9Rayo2Oyo2OwCM0gCM0io2OwCM0gCM0gCM0gCM0io2OwCM0o7Th4kAAAATdFJOUwAg3/FJx4VqpA/eMSmkd0vCaofCVE4CAAALtUlEQVR42u2d24LyIA6AS6Hl1KP6/s+66owWQhKgVp1/d7kabavTz5AztGn+P/6V4Sfj5PksZWe0DQ/Yx/h37mU4LW1+zOmFK3LachrIL1LdORzGP4+I6ICUrjNG+/jiMxzq94g7I6Pf/ux+fjH5HN0B0E6XorEmF84tcWp7Qr9IdMm9GYtiewyngsun5LDmsAWU5f0sHSB9GdpcBu2SiJBduNMR0VQSAyM4bNENGvIgji34kQS4Xr1KbSyDtlTLaCJwXuICZVlsT4lqmlRWOxbbBDA5IH3vp5YwGNrqaxzBxfDYzp7+AMdi89vf0212wK/cP9YyavMu2rEynHguNLbnPSLHWGzB27fP8JgE77Og+9RaqTq0pLDJhAuNTVpa+3kWm4nEUgNVt38sJTff2n0TO1aIKjYDoaJzPLaH/lb0IQKbisTSJCpx57B7jEGBVsPELZyjEzCLFmCTjejB6bG0wEMENhuJpTvK/Rh3GIPTpWKccO/hJiM9eB1ji8zmr3Lrab2n9M9wYAJ3gTaziJHZN9pqH9e2qHNbIKkcNo1g6xM2BsEWTzcBrewUCJg/zP2oNqGYLbjGXLSKbFCnC2KbEGxTwmb7BCdxAhq6wj74DH2Y+1FrQpFJvQzs55Rh6xFsOsG2zcDORWoRDyNiD9cFX6jeiw2YUGSC3qFxzt+B2EJvtUPVlJVnGIZuIIN/wL4VW5uboI+USPsqNlMySUOf36COq0qNxfaWdwe5HxlsSy6eWAt8ZtzbVcAhMSUmIYCiDepLpHM0EFF9VIjAYxszam0scmNobDqDzcA8R3CB71H17pI5Ggi5OSpEYLGNvFprhzL4u7GFUYSGbpuYMA/EY4Hs80wHw/93YDvxoetamg3Yh+3cRTGrgFMwuDjwQHos7+u5BN7R2E7sebGFbd+ADXNpA7ct1HMCNTrSktkm9TZsKxvxnyriWhqbUNsQHLZH+lcGHD1CQaDJpiS2eDlDSWJbuSiszbvARdiSOgMhag+7FyUZBZI603hKWFHZu6OxrVxebqzz/V7E5iaLKPwpzFj2aMp8UyOWzLEfi23liltrXQFnfFnanqUtFd25S6THUhE+qEDY92A7McmSdqhKoiy2eR3bo0QT11O6pJygKJGamJTJYdhGJqO5VCU6QTW6CltvJNRGJkqXmaScYCiR8ge7Hxi2kSmnInI4LKVRRh2260sJsopdBKVPPBBJipRDy2BHYhu5ck15UR5TghCb9dsQKbYkuHLRUVgCpedoLIeueQO2paqa39aU8OvcXSSUj29dwXJCn4YVmAti3oCtrSkVLjW1rtewdfFhd5VPDUk4Wu3bQ0OEBFsNtfFSSS3Jt+WwgXyb4mMvgZSznkO+FVu5RzNfqqlVYwPZXU1ic4mXIT6JbSiuri4VtfgibH0eW09Xny349ETtvxPbfFRjF4H/RWzmzLWQWNY1eye24QitxuA3TFJ8ymPraGwaTGH/SWxUVFXZNUJ6fjXlZQSbo7H1OdfsvSahLbEJQ1W1iwgNc80MKTZLU7sZFMmGT+/FVqbfTnsUG/AgNJA+kcXmGWxd7J1I9zvUp7AVhQnLnikaY7mJjwMJVx5b3OZ1HdHlhuvv+gA2LDVU093FXRf58X3HOqwJNg1PD68X7tvYSizDXN7hG46eb/vjscEafmxh5PexxcnFOh+EvUqwbn4Gm+Gw6b+ArcAytKVN+CXiJn0Btg6ayqjz5m9gY9NujBeS4j6RrttGTTUF2CSM1KMWkj+CLWsZ1rI5ulyaHDfnmwJsNklChjbC/RVsRP2K90JaRAdC5w3ESLK3aGEOYvMJDkW2638VW8Yy2AJsFhNA3z+9BdlFKyN1MG4nhi9FePCeFxJ9djzzRxPy3ruwZSzDnMe2ELbVeqW0UkcUQ74z9oblhBdiU7vR/DcOcoKWWIY244C0/2vYTttKl7XKC0mN7WH/qriv2FB+Ry/CVSncLhVvxraE5bylwgtZU5sRGFFEaT9WBcH3FW1Hzt30vH+ryfGkK6YON0HxxVdVK4KDgQlSydkNWws4ZXNBC2MSFogNixFkWlBHKnYeZnZNZsHzluG1IICQW1ELSUXJrvfJQQfTXl3DG9BHqeVU6IUMiCSWYLMUzjS/GUcWWWzekU2GVAbvt8HJgX6SKYztcuZzyKR9Zyr9YS8V2DxejGIj2akEG7rKXAoW27mzIJ7xyeuczzrmXLiRn6Jl2DSzzpusj6o8NsGuzffsYmkFYrlomX0mqz3nXbiWnaJl2CZmWwHi1n96mjPYDLuI3LPpP7CuPn6Z8XDbfHA/YFZ0uFRhM8wuFoYr8/HYaC6Cxwayx6CVQmHYmGLLifNCKNwl2Dp6V4Fo8VmSSeexRUXAPknYCb7Mr6kFYBbBNnPROh7cL7RGLMTmqIRvnOeARWabweaiGW3P3Np80zF6U8Bl9mx0tBQG9zAaXS9ZbLLrultJ7sc/w24bcT4m8CG+Eb+VveiX+Bk+4pQSZxcrTfGPqcIXGsE25DK4I144pa9rUJNosjUGkbLWyOsm4Y415CfYRMMujTPxV/fhTyBSbGO+HJpahpmd2gXYFJZuVGWNIww22ENpoHuSWYipgpc+nt+MPbCFad8B2Iq2GluYxoWilGtT2okN2wkCLvu1ASodfyljKsey5blD5rICbMHP3EMmuV5CBpuuxJYsMt++Gy6zZyooZWnfAczs9VKPLdwejF7Vdyg2XSBtwQds287JlM2aL01BuYTU5ssObMGCFg89kA9iSxaZC6TqbxJsbUkBOe7pgtTYxCWJLVjwKKAH8k1sm9cxAZVLClt+86P1Lls5agXYwnAv2U/ng9i6xEb3qaWyCbamfI7+WIYVWAN7KcbWbXW9eMEj9EA+hc0rkxZYVeIXdYneH6taTbEotS3HFt5jlKJx4Bf/ELY0uZIExKEYksW6HVsI2ss+bOE+FQEmg2Prfsc1pHobtik1VnEakGwW2rOF4LoPW7RWz5C+E9eHcCg22ZP/skvozDV9zUSifNmFLVoZapic0iewOaMFHS2bBFtpvySb7d2FzYU/Zg/u/+PSFrelOLwXh6IwF7gftQVnCpskWnT9lyZpuK90jxeGKD2VwUb2OJzqsYno5mDl4wvYwvqPwqu3VEPfULNbpW23tG9bjc1HKQ0PEhwfwhb7bdsymtgF0RDbUtGKBEXt3i4yU14I4e7+Ni3Y6O0p3Yj5U9hiPabw9k8B6ayFPc3IqUOsHNfa4GqKb4ZZfXC7GW+2oY/FZrBMnkbXcpErQNdSAzpDIVwqsYFd5cFu6V8N5cFJfYKtsIV+ZPGu2JVZbOH2utch4znxbWx42y+9LG8ogQZyucueEoxji+PfTFPCfy/BhvmuYAvsdi1pF58TLySL7cyV3T+JTVdjI+rtD3Dtgnq32N7iJzhNc9iYCnH/17GRLeHDPM9FTVpRqGorsNH7VCQr5N9cuarHVrwnQ0lla42I5rDR+1TcDf4L2PwfxGZbdr/epRgbs0/FGanCT/ur8rnycgW2die2NReytqmNxrEx+1Tcbk4zzQyKxyYqmhnOddjGfdiyKfPTkBobHFvUenX124AN8GBSGizWadAIqAGP/3CgMecFbLZoWVqRLcCfoGBz2CSjvKb4uPRRW5BsMti6SHBhy9cr2H7lZjxU1Ii+BxSbhQkbaP+idL48530/gVubNJXxCrahdtu29VIzbA6bh3cMFbkqyIoR2KxjK1OvYKtc4lPz9Bw4+VFs6sxoHMkFX6bJYSOdG928jO3HKswv+mol6UwU2wQpWWgVic7kzuaxEWbaNAdgu7MomqWnyyvUcGx9ks9K5iG6W0VEjcSGP3THHoLtbhmHg5UaIsEoNpOk6mUym3xH999nsCHedI9Gwzuw3eSoPVjSkOeT6u2ZqtJgaaN0j8nHLcYr7KURTSm2xscCRz1Gdhe2q67nF8aPbc3gnoa7dzWpNp2T59sjcjX6r9JPILbXS+W9Oz0qHQeX/F4FXv5+8Tb+oYcb/8nxH6YT02ZUEQH4AAAAAElFTkSuQmCC
--#

--% /rts/src/app/models/Translator.ts
import {ITranslations} from "../redux/modules/settingsModule";
import {ITranslator} from "./TranslatorInterfaces";

export class Translator implements ITranslator {
	private readonly translations: ITranslations;

	constructor(translations: ITranslations) {
		this.translations = translations;
	}

	public translate(key: string): string {
		if (this.translations[key]) {
			return this.translations[key];
		}
		console.warn(`Translations: no key: "${key}" found`);
		return key;
	}
}

--#

--% /rts/src/app/models/TranslatorInterfaces.ts
export interface ITranslator {
	translate: (key: string) => string;
}
--#

--% /rts/src/app/components/Button.stories.tsx
import * as React from "react";
import {Color} from "../constants";
import {withInitialState} from "../helpers/withInitialState";
import {Button} from "./Button";

export default {
	component: Button,
	title: "Button"
};

export const Primary = () => <Button>Primary</Button>;
export const Secondary = () => <Button type={"secondary"}>Secondary</Button>;
export const Disabled = () => <Button disabled={true}>Disabled</Button>;
export const StyledButton = () => {
	const style = {
		backgroundColor: Color.BLACK,
		border: 0,
		borderRadius: 5,
		color: Color.BLUE
	};
	return (
		<Button style={style}>
			Styled
		</Button>
	);
};
export const SwitchableButton = ({state, setState}) => (
	<Button
		type={state.type}
		onClick={() => setState({type: state.type === "primary" ? "secondary" : "primary"})}
	>
		Click me!
	</Button>
);
SwitchableButton.story = {
	decorators: [withInitialState({type: "primary"})]
};

--#

--% /rts/src/app/components/Button.tsx
import * as React from "react";
import {classes, stylesheet} from "typestyle";
import {Color} from "../constants/Color";

const classNames = stylesheet({
	button: {
		outline: "none",
		padding: "10px 25px"
	},
	disabled: {
		backgroundColor: Color.GREY,
		border: "none",
		color: Color.WHITE,
		cursor: "not-allowed"
	},
	primary: {
		backgroundColor: Color.BLUE,
		border: `1px solid ${Color.BLUE}`,
		color: Color.WHITE,
		cursor: "pointer"
	},
	secondary: {
		backgroundColor: Color.WHITE,
		border: `1px solid ${Color.GREY}`,
		color: Color.GREY,
		cursor: "pointer"
	}
});

export type TButtonType = "primary" | "secondary";

interface IProps extends React.HTMLProps<HTMLButtonElement> {
	/**
	 * Either primary or secondary
	 */
	type?: TButtonType;
}

export class Button extends React.Component<IProps> {
	public static defaultProps: Partial<IProps> = {
		type: "primary"
	};

	public render(): JSX.Element {
		const {children, className, disabled, type, ...rest} = this.props;
		return (
			<button
				className={classes(classNames.button, disabled ? classNames.disabled : classNames[type], className)}
				disabled={disabled}
				{...rest}
			>
				{children}
			</button>
		);
	}
}

--#

--% /rts/src/app/constants/FontSize.ts
export enum FontSize {
	MEDIUM = "16px"
}

--#

--% /rts/src/app/constants/Color.ts
export enum Color {
	BLACK = "#000",
	BLUE = "#0095da",
	GREY = "#ccc",
	WHITE = "#fff"
}

--#

--% /rts/src/app/constants/index.ts
// easier import for doc
export {Color} from "./Color";
export {FontSize} from "./FontSize";

--#

--% /rts/src/app/containers/App.tsx
import * as React from "react";
import {Helmet} from "react-helmet";
import {connect} from "react-redux";
import {createRouteNodeSelector, RouterState} from "redux-router5";
import {createSelector} from "reselect";
import {State as IRouteState} from "router5";
import {stylesheet} from "typestyle";
import {config as appConfig} from "../../../config";
import {setupCss} from "../helpers/setupCss";
import {Translator} from "../models/Translator";
import {ITranslator} from "../models/TranslatorInterfaces";
import {AboutPage} from "../pages/AboutPage";
import {CounterPage} from "../pages/CounterPage";
import {HomePage} from "../pages/HomePage";
import {StarsPage} from "../pages/StarsPage";
import {IStore} from "../redux/IStore";
import {RoutePageMap} from "../routes/routes";
import {translationsSelector} from "../selectors/translationsSelector";
import {Header} from "./Header";

setupCss();

const classNames = stylesheet({
	container: {
		margin: 0,
		padding: 0,
		textAlign: "center"
	}
});

interface IStateToProps {
	route: IRouteState;
	translations: {
		notFound: string;
	};
}

class App extends React.Component<IStateToProps> {
	private components: RoutePageMap = {
		aboutPage: AboutPage,
		counterPage: CounterPage,
		homePage: HomePage,
		starsPage: StarsPage
	};
	public render(): JSX.Element {
		const {route, translations: {notFound}} = this.props;
		const segment = route ? route.name.split(".")[0] : undefined;
		return (
			<section className={classNames.container}>
				<Helmet {...appConfig.app.head}/>
				<Header/>
				{segment && this.components[segment] ? React.createElement(this.components[segment]) : <div>{notFound}</div>}
			</section>
		);
	}
}

const componentTranslationsSelector = createSelector(
	translationsSelector,
	(translations) => {
		const translator: ITranslator = new Translator(translations);
		return {
			notFound: translator.translate("Not found")
		};
	}
);

const mapStateToProps = (state: Pick<IStore, "router" | "settings">): IStateToProps & Partial<RouterState> => ({
	...createRouteNodeSelector("")(state),
	translations: componentTranslationsSelector(state)
});

const connected = connect(mapStateToProps)(App);

export {classNames, connected as App, App as UnconnectedApp, mapStateToProps};

--#

--% /rts/src/app/containers/Header.tsx
import * as React from "react";
import {connect} from "react-redux";
import {ConnectedLink} from "react-router5";
import {createSelector} from "reselect";
import {stylesheet} from "typestyle";
import {Translator} from "../models/Translator";
import {ITranslator} from "../models/TranslatorInterfaces";
import {IStore} from "../redux/IStore";
import {getRoutes} from "../routes/routes";
import {translationsSelector} from "../selectors/translationsSelector";

const classNames = stylesheet({
	activeLink: {
		textDecoration: "underline"
	},
	nav: {
		$nest: {
			ul: {
				$nest: {
					li: {
						display: "inline",
						padding: "5px"
					}
				},
				listStyleType: "none",
				padding: 0
			}
		}
	}
});

interface IStateToProps {
	translations: {
		aboutUs: string;
		counter: string;
		home: string;
		stars: string;
	};
}

class Header extends React.Component<IStateToProps> {
	public render(): JSX.Element {
		const {translations} = this.props;
		const routes = getRoutes();
		return (
			<nav className={classNames.nav}>
				<ul>
					<li>
						<ConnectedLink activeClassName={classNames.activeLink} routeName={routes.homePage.name}>
							{translations.home}
						</ConnectedLink>
					</li>
					<li>
						<ConnectedLink activeClassName={classNames.activeLink} routeName={routes.aboutPage.name}>
							{translations.aboutUs}
						</ConnectedLink>
					</li>
					<li>
						<ConnectedLink activeClassName={classNames.activeLink} routeName={routes.counterPage.name}>
							{translations.counter}
						</ConnectedLink>
					</li>
					<li>
						<ConnectedLink activeClassName={classNames.activeLink} routeName={routes.starsPage.name}>
							{translations.stars}
						</ConnectedLink>
					</li>
				</ul>
			</nav>
		);
	}
}

const componentTranslationsSelector = createSelector(
	translationsSelector,
	(translations) => {
		const translator: ITranslator = new Translator(translations);
		return {
			aboutUs: translator.translate("About us"),
			counter: translator.translate("Counter"),
			home: translator.translate("Home"),
			stars: translator.translate("Stars")
		};
	}
);

function mapStateToProps(state: Pick<IStore, "settings">): IStateToProps {
	return {
		translations: componentTranslationsSelector(state)
	};
}

const connected = connect(mapStateToProps)(Header);
export {connected as Header, Header as UnconnectedHeader, mapStateToProps};

--#

--% /rts/src/app/containers/Html.tsx
import autobind from "autobind-decorator";
import * as React from "react";
import {Helmet} from "react-helmet";
import serialize from "serialize-javascript";
import {getStyles} from "typestyle";
import {IStore} from "../redux/IStore";

interface IHtmlProps {
	initialState?: Partial<IStore>;
	manifest?: {[key: string]: string};
	markup?: string;
}

export class Html extends React.Component<IHtmlProps> {
	public render(): JSX.Element {
		const head = Helmet.renderStatic();
		const {markup, initialState} = this.props;

		// styles from typestyle
		const renderStyles = <style id="styles-target">{getStyles()}</style>;

		// styles from css files
		const links = this.getFileNames(".css").map(
			(href, i) => <link key={i} href={href} rel="stylesheet" type="text/css"/>
		);

		// scripts
		const scripts = this.getFileNames(".js").map((src, i) => <script src={src} key={i}/>);

		const initialStateScript = (
			// tslint:disable-next-line:react-no-dangerous-html
			<script
				dangerouslySetInnerHTML={{__html: `window.__INITIAL_STATE__=${serialize(initialState, {isJSON: true})};`}}
				charSet="UTF-8"
			/>
		);

		return (
			<html>
				<head>
					{head.base.toComponent()}
					{head.title.toComponent()}
					{head.meta.toComponent()}
					{head.link.toComponent()}
					{head.script.toComponent()}
					{renderStyles}
					{links}
					<link rel="shortcut icon" href="/favicon.ico"/>
				</head>
				<body>
					{/* tslint:disable-next-line:react-no-dangerous-html */}
					<main id="app" dangerouslySetInnerHTML={{__html: markup}}/>
					{initialStateScript}
					{scripts}
				</body>
			</html>
		);
	}

	@autobind
	private getFileNames(endsWith: string): string[] {
		const {manifest} = this.props;
		const scriptFileNames: string[] = [];
		Object.keys(manifest).forEach((key: string) => {
			if (manifest[key].endsWith(endsWith)) {
				scriptFileNames.push(manifest[key]);
			}
		});
		return scriptFileNames;
	}
}

--#

--% /rts/src/app/containers/Header.test.tsx
import {shallow} from "enzyme";
import * as React from "react";
import {ConnectedLink} from "react-router5";
import {ISettingsState} from "../redux/modules/settingsModule";
import {getRoutes} from "../routes/routes";
import {mapStateToProps, UnconnectedHeader} from "./Header";

describe("<Header />", () => {
	const translations = {
		aboutUs: "About Us",
		counter: "Counter",
		home: "Home",
		stars: "Stars"
	};

	it("maps state to props", () => {
		const settings: ISettingsState = {
			error: "",
			language: "en",
			loaded: true,
			pending: false,
			translations: {
				"About us": "About Us",
				"Counter": "Counter",
				"Home": "Home",
				"Stars": "Stars"
			}
		};
		const props = mapStateToProps({settings});
		expect(props).toEqual({
			translations
		});
	});

	it("contains links", () => {
		const wrapper = shallow(<UnconnectedHeader translations={translations}/>);
		const routes = getRoutes();
		expect(wrapper.containsMatchingElement(
			<ConnectedLink routeName={routes.homePage.name}>Home</ConnectedLink>)
		).toBeTruthy();
		expect(wrapper.containsMatchingElement(
			<ConnectedLink routeName={routes.aboutPage.name}>About Us</ConnectedLink>)
		).toBeTruthy();
		expect(wrapper.containsMatchingElement(
			<ConnectedLink routeName={routes.counterPage.name}>Counter</ConnectedLink>)
		).toBeTruthy();
		expect(wrapper.containsMatchingElement(
			<ConnectedLink routeName={routes.starsPage.name}>Stars</ConnectedLink>)
		).toBeTruthy();
	});
});

--#

--% /rts/src/app/containers/App.test.tsx
import {shallow} from "enzyme";
import * as React from "react";
import {State as IRouteState} from "router5";
import {HomePage} from "../pages/HomePage";
import {ISettingsState} from "../redux/modules/settingsModule";
import {getRoutes} from "../routes/routes";
import {classNames, mapStateToProps, UnconnectedApp} from "./App";

describe("<App />", () => {
	const routes = getRoutes();
	const route: IRouteState = {
		meta: {id: 1, params: {}, options: {}, redirected: false},
		name: routes.homePage.name,
		params: {},
		path: "/"
	};
	const routeUnavailable: IRouteState = {
		name: "unavailable",
		params: {},
		path: "/"
	};
	const settings: ISettingsState = {
		error: "",
		language: "en",
		loaded: true,
		pending: false,
		translations: {"Not found": "Not Found"}
	};
	const translations = {notFound: "Not Found"};

	it("maps state to props correctly", () => {
		const props = mapStateToProps({
			router: {route, previousRoute: route, transitionRoute: null, transitionError: null},
			settings
		});
		expect(props.route).toEqual(route);
		expect(props.translations).toEqual({notFound: "Not Found"});
	});

	it("renders with correct style", () => {
		const wrapper = shallow(<UnconnectedApp route={route} translations={translations}/>);
		expect(wrapper.find("section")).toHaveClassName(classNames.container);
	});

	it("renders HomePage", () => {
		const wrapper = shallow(<UnconnectedApp route={route} translations={translations}/>);
		expect(wrapper.find(HomePage).length).toBe(1);
	});

	it("renders Not Found when route is null", () => {
		const wrapper = shallow(<UnconnectedApp route={null} translations={translations}/>);
		expect(wrapper.find("div")).toHaveText("Not Found");
	});

	it("renders Not Found when segment is undefined", () => {
		const wrapper = shallow(<UnconnectedApp route={routeUnavailable} translations={translations}/>);
		expect(wrapper.find("div")).toHaveText("Not Found");
	});
});

--#

--% /rts/src/app/routes/configureRouter.ts
import createRouter, {Router} from "router5";
import browserPlugin from "router5-plugin-browser";
import {MiddlewareFactory} from "router5/dist/types/router";
import {getRoutes} from "./routes";

export function configureRouter(baseUrl: string = ""): Router {
	const routes = getRoutes(baseUrl);
	const router = createRouter(Object.keys(routes).map((key) => routes[key]));
	router.usePlugin(browserPlugin({useHash: false}));

	const middlewares: MiddlewareFactory[] = [];

	router.useMiddleware(...middlewares);

	return router;
}

--#

--% /rts/src/app/routes/routes.ts
import {ConnectedComponent} from "react-redux";
import {Action} from "redux";
import {actions} from "redux-router5";

interface IRoute {
	name: RoutablePages;
	path: string;
}
type RoutablePages = "homePage"
| "aboutPage"
| "counterPage"
| "starsPage";

type RouteConfig = Record<RoutablePages, Omit<IRoute, "name">>;
export type RoutePageMap = Record<RoutablePages, ConnectedComponent<any, any>>;
type RouteNavigate = Record<RoutablePages, (...params: any[]) => Action>;

const config: RouteConfig = {
	aboutPage: {path: "/about"},
	counterPage: {path: "/counter"},
	homePage: {path: "/"},
	starsPage: {path: "/stars"}
};

export function getRoutes(baseUrl: string = ""): Record<RoutablePages, IRoute> {
	return Object.keys(config)
		.map((key) => ({
			name: key,
			path: baseUrl + config[key].path
		}))
		.reduce((a, c) => ({...a, [c.name]: c}), {} as any);
}

function getNavigateAction<T extends {[key: string]: any}>(routeName: RoutablePages, params?: T): Action {
	return actions.navigateTo(routeName, params);
}

const routes = getRoutes();

export const navigate: RouteNavigate = {
	aboutPage: () => getNavigateAction(routes.aboutPage.name),
	counterPage: () => getNavigateAction(routes.counterPage.name),
	homePage: () => getNavigateAction(routes.homePage.name),
	starsPage: () => getNavigateAction(routes.starsPage.name)
};

--#

--% /rts/src/app/selectors/translationsSelector.ts
import {IStore} from "../redux/IStore";

export const translationsSelector = (state: Pick<IStore, "settings">) => state.settings?.translations;

--#

--% /rts/.storybook/webpack.config.js
module.exports = ({ config }) => {
	config.module.rules.push({
		test: /\.(ts|tsx)$/,
		use: [
			{
				loader: require.resolve('babel-loader'),
			},
			{
				loader: require.resolve('react-docgen-typescript-loader'),
			},
		],
	});
	config.resolve.extensions.push('.ts', '.tsx');
	return config;
};

--#

--% /rts/.storybook/presets.js
module.exports = ['@storybook/addon-docs/react/preset'];

--#

--% /rts/.storybook/config.js
import {configure} from '@storybook/react';
configure(require.context('../src', true, /\.stories\.tsx$/), module);

--#

--% /rts/config/main.js
/** General Configurations Like PORT, HOST names and etc... */

const config = {
	// This part goes to React-Helmet for Head of our HTML
	app: {
		head: {
			link: [
				{
					href: 'https://fonts.googleapis.com/css?family=Roboto',
					rel: 'stylesheet',
					type: 'text/css'
				}
			],
			meta: [
				{charset: 'utf-8'},
				{'http-equiv': 'x-ua-compatible', content: 'ie=edge'},
				{name: 'viewport', content: 'width=device-width, initial-scale=1'},
				{name: 'description', content: 'React Redux Typescript'},
			],
			title: 'Crazy Factory'
		}
	},
	env: process.env.NODE_ENV || 'development',
	host: process.env.HOST || 'localhost',
	port: process.env.PORT || __TEMPLATE_SERVER_PORT__,
	ssr: true,
	sentry: {
		dsn: '', // your sentry dsn here
		options: {}
	}
};

module.exports = config;

--#

--% /rts/config/main.local.js
/** General Configurations Like PORT, HOST names and etc... */

const config = {
	// This part goes to React-Helmet for Head of our HTML
	app: {
		head: {
			link: [
				{
					href: 'https://fonts.googleapis.com/css?family=Roboto',
					rel: 'stylesheet',
					type: 'text/css'
				}
			],
			meta: [
				{charset: 'utf-8'},
				{'http-equiv': 'x-ua-compatible', content: 'ie=edge'},
				{name: 'viewport', content: 'width=device-width, initial-scale=1'},
				{name: 'description', content: 'React Redux Typescript'},
			],
			title: 'Crazy Factory'
		}
	},
	env: process.env.NODE_ENV || 'development',
	host: process.env.HOST || 'localhost',
	port: process.env.PORT || __TEMPLATE_SERVER_PORT__,
	ssr: true,
	sentry: {
		dsn: '', // your sentry dsn here
		options: {}
	}
};

module.exports = config;

--#

--% /rts/config/index.js
const defaultConfig = require('./main');
const localConfig = require('./main.local');
module.exports.config = {
	...defaultConfig,
	...localConfig
};

--#

--% /rts/config/webpack/index.js
const utils = require('../utils');

utils.copySyncIfDoesntExist('./config/main.js', './config/main.local.js');
utils.createIfDoesntExist('./build');
utils.createIfDoesntExist('./build/public');

if (process.env.NODE_ENV === 'production')
{
	module.exports = require('./prod');
}
else
{
	module.exports = require('./dev');
}

--#

--% /rts/config/webpack/dev.js
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const path = require('path');
const webpack = require('webpack');
const ManifestPlugin = require('webpack-manifest-plugin');
const appConfig = require('../').config;
const utils = require('../utils');

const config = {
	mode: 'development',

	// Enable sourcemaps for debugging webpack's output.
	devtool: 'source-map',

	resolve: {
		extensions: ['.ts', '.tsx', '.js', '.jsx'],
		modules: [path.resolve(__dirname), 'node_modules', 'app', 'app/redux'],
	},

	entry: {
		app: [
			'react-hot-loader/patch',
			'webpack-hot-middleware/client?reload=true',
			'./src/client.tsx',
			'./src/vendor/main.ts'
		]
	},

	output: {
		path: path.resolve('./build/public'),
		publicPath: '/public/',
		filename: 'js/[name].js',
		pathinfo: true
	},

	module: {
		rules: [
			{
				test: /\.tsx?$/,
				loader: 'babel-loader',
				exclude: /node_modules/
			},
			{
				test: /\.eot(\?.*)?$/,
				loader: 'file-loader?name=fonts/[hash].[ext]'
			},
			{
				test: /\.(woff|woff2)(\?.*)?$/,
				loader: 'file-loader?name=fonts/[hash].[ext]'
			},
			{
				test: /\.ttf(\?.*)?$/,
				loader: 'url-loader?limit=10000&mimetype=application/octet-stream&name=fonts/[hash].[ext]'
			},
			{
				test: /\.svg(\?.*)?$/,
				loader: 'url-loader?limit=10000&mimetype=image/svg+xml&name=fonts/[hash].[ext]'
			},
			{
				test: /\.(jpe?g|png|gif)$/i,
				loader: 'url-loader',
				options: {
					esModule: false,
					limit: 10000
				}
			},
			{
				test: /\.css$/,
				use: [
					appConfig.ssr ?
						{
							loader: MiniCssExtractPlugin.loader,
							options: {
								hmr: process.env.NODE_ENV !== 'production',
							}
						} :
						'style-loader',
					'css-loader'
				]
			}
		]
	},

	plugins: [
		new webpack.LoaderOptionsPlugin({
			debug: true,
			options: {
				tslint: {
					failOnHint: true
				},
			}
		}),
		new ManifestPlugin({
			fileName: '../manifest.json'
		}),
		new webpack.DefinePlugin({
			'process.env': {
				BROWSER: JSON.stringify(true),
				NODE_ENV: JSON.stringify('development')
			}
		}),
		new webpack.HotModuleReplacementPlugin(),
		new MiniCssExtractPlugin({
			filename: 'css/[name].css'
		})
	],

	optimization: {
		noEmitOnErrors: true
	}
};

utils.copySync('./src/favicon.ico', './build/public/favicon.ico', true);
utils.copySync('./src/index.html', './build/index.html');

module.exports = config;

--#

--% /rts/config/webpack/prod.js
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const OptimizeCSSAssetsPlugin = require('optimize-css-assets-webpack-plugin');
const path = require('path');
const TerserWebpackPlugin = require('terser-webpack-plugin');
const webpack = require('webpack');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
const ManifestPlugin = require('webpack-manifest-plugin');
const appConfig = require('../').config;
const utils = require('../utils');

const config = {
	mode: 'production',

	bail: true,

	resolve: {
		extensions: ['.ts', '.tsx', '.js', '.jsx'],
		modules: [path.resolve(__dirname), 'node_modules', 'app', 'app/redux'],
	},

	entry: {
		app: [
			'./src/client.tsx',
			'./src/vendor/main.ts'
		]
	},

	output: {
		path: path.resolve('./build/public'),
		publicPath: '/public/',
		filename: 'js/[name].[chunkhash].js'
	},

	module: {
		rules: [
			{
				enforce: 'pre',
				test: /\.tsx?$/,
				loader: 'eslint-loader'
			},
			{
				test: /\.tsx?$/,
				loader: 'babel-loader',
				exclude: /node_modules/
			},
			{
				test: /\.eot(\?.*)?$/,
				loader: 'file-loader?name=fonts/[hash].[ext]'
			},
			{
				test: /\.(woff|woff2)(\?.*)?$/,
				loader: 'file-loader?name=fonts/[hash].[ext]'
			},
			{
				test: /\.ttf(\?.*)?$/,
				loader: 'url-loader?limit=10000&mimetype=application/octet-stream&name=fonts/[hash].[ext]'
			},
			{
				test: /\.svg(\?.*)?$/,
				loader: 'url-loader?limit=10000&mimetype=image/svg+xml&name=fonts/[hash].[ext]'
			},
			{
				test: /\.(jpe?g|png|gif)$/i,
				loader: 'url-loader',
				options: {
					esModule: false,
					limit: 10000
				}
			},
			{
				test: /\.css$/,
				use: [
					appConfig.ssr ?
						{
							loader: MiniCssExtractPlugin.loader,
							options: {
								hmr: process.env.NODE_ENV !== 'production',
							}
						} :
						'style-loader',
					'css-loader'
				]
			}
		]
	},

	plugins: [
		new webpack.LoaderOptionsPlugin({
			debug: true,
			options: {
				tslint: {
					failOnHint: true
				},
			}
		}),
		new ManifestPlugin({
			fileName: '../manifest.json'
		}),
		new webpack.DefinePlugin({
			'process.env': {
				BROWSER: JSON.stringify(true),
				NODE_ENV: JSON.stringify('production')
			}
		}),
		new MiniCssExtractPlugin({
			filename: 'css/[name].[chunkhash].css'
		}),
		// Uncomment this to analyze bundle
		// new BundleAnalyzerPlugin()
	],

	optimization: {
		minimizer: [new TerserWebpackPlugin({}), new OptimizeCSSAssetsPlugin({})],
		splitChunks: {
			chunks: 'all'
		}
	}
};

utils.copySync('./src/favicon.ico', './build/public/favicon.ico', true);

module.exports = config;

--#

--% /rts/config/webpack/server.js
const path = require('path');
const fs = require('fs');
const utils = require('../utils');

const nodeModules = {};
fs.readdirSync('node_modules')
	.filter(function (x) {
		return ['.bin'].indexOf(x) === -1;
	})
	.forEach(function (mod) {
		nodeModules[mod] = 'commonjs ' + mod;
	});

const config = {
	mode: process.env.NODE_ENV === 'production' ? 'production' : 'development',
	externals: nodeModules,
	target: 'node',

	resolve: {
		extensions: ['.ts', '.tsx', '.js', '.jsx'],
		modules: [path.resolve(__dirname), 'node_modules', 'app', 'app/redux'],
	},

	entry: './src/server.tsx',

	output: {
		path: path.resolve('./build/public'),
		filename: '../server.js',
		publicPath: '/public/',
		libraryTarget: 'commonjs2'
	},

	module: {
		rules: [
			{
				test: /\.tsx?$/,
				loader: 'babel-loader',
				exclude: /node_modules/
			},
			{
				test: /\.eot(\?.*)?$/,
				loader: 'file-loader?name=fonts/[hash].[ext]'
			},
			{
				test: /\.(woff|woff2)(\?.*)?$/,
				loader: 'file-loader?name=fonts/[hash].[ext]'
			},
			{
				test: /\.ttf(\?.*)?$/,
				loader: 'url-loader?limit=10000&mimetype=application/octet-stream&name=fonts/[hash].[ext]'
			},
			{
				test: /\.svg(\?.*)?$/,
				loader: 'url-loader?limit=10000&mimetype=image/svg+xml&name=fonts/[hash].[ext]'
			},
			{
				test: /\.(jpe?g|png|gif)$/i,
				loader: 'url-loader',
				options: {
					esModule: false,
					limit: 10000
				}
			},
			{
				test: /\.css$/,
				loader: 'null-loader'
			}
		]
	},

	plugins: [],

	node: {
		console: false,
		global: false,
		process: false,
		Buffer: false,
		__filename: false,
		__dirname: false
	}
};

utils.copySync('./src/favicon.ico', './build/public/favicon.ico', true);

module.exports = config;

--#

--% /rts/config/types/png.d.ts
declare module "*.png" {
	const value: any;
	export = value;
}

--#

--% /rts/config/types/dev.d.ts
/**
 * Type declerations for global development variables
 */

// tslint:disable:interface-name

interface Window {
	// A hack for the Redux DevTools Chrome extension.
	__REDUX_DEVTOOLS_EXTENSION_COMPOSE__?: any;
	__INITIAL_STATE__?: any;
}

--#

--% /rts/config/types/redux-router5.d.ts
import {State} from "router5";

// tslint:disable:interface-name
declare module "redux-router5" {
	interface RouterState {
		route: State | null;
		previousRoute: State | null;
		transitionRoute: State | null;
		transitionError: any | null;
	}
}

--#

--% /rts/config/utils/createIfDoesntExist.js
const fs = require('fs');

const createIfDoesntExist = (dest) => {
	if (!fs.existsSync(dest)) {
		fs.mkdirSync(dest);
	}
};

module.exports = createIfDoesntExist;

--#

--% /rts/config/utils/index.js
const copySync = require('./copySync');
const copySyncIfDoesntExist = require('./copySyncIfDoesntExist');
const createIfDoesntExist = require('./createIfDoesntExist');

module.exports = {
	copySync,
	copySyncIfDoesntExist,
	createIfDoesntExist
};

--#

--% /rts/config/utils/copySync.js
const fs = require('fs');

const copySync = (src, dest, overwrite) => {
	if (overwrite && fs.existsSync(dest)) {
		fs.unlinkSync(dest);
	}
	const data = fs.readFileSync(src);
	fs.writeFileSync(dest, data);
};

module.exports = copySync;

--#

--% /rts/config/utils/replaceWithProdScripts.js
const fs = require('fs');
const manifest = require('../../build/manifest');
const utils = require('../utils');

utils.copySync('./src/index.html', './build/index.html');

const scriptFileNames = [];
Object.keys(manifest).forEach((key) => {
	if (manifest[key].endsWith('.js')) {
		scriptFileNames.push(manifest[key]);
	}
});
const scripts = scriptFileNames.map((fileName) => `<script src="${fileName}"></script>`);
const indexHtml = fs.readFileSync('./build/index.html').toString();
const resultHtml = indexHtml.replace('<script src="/public/js/app.js"></script>', scripts.join('\n'));
fs.writeFileSync('./build/index.html', resultHtml);

--#

--% /rts/config/utils/copySyncIfDoesntExist.js
const fs = require('fs');
const copySync = require('./copySync');

const copySyncIfDoesntExist = (src, dest) => {
	if (fs.existsSync(dest)) {
		return;
	}
	copySync(src, dest);
};

module.exports = copySyncIfDoesntExist;

--#

--% /rts/translations/en.json
{
	"Hello": "Hello!",
	"About": "About",
	"About us": "About Us",
	"Change language": "Change Language",
	"Counter": "Counter",
	"Increment": "Increment",
	"Decrement": "Decrement",
	"Current language": "Current Language",
	"Stars": "Stars",
	"Home": "Home",
	"Fetching stars...": "Fetching Stars...",
	"Not found": "Not Found"
}

--#

--% /rts/translations/de.json
{
	"Hello": "Hallo!",
	"About": "Über",
	"About us": "Über uns",
	"Change language": "Sprache Ändern",
	"Counter": "Zähler",
	"Increment": "Zuwachs",
	"Decrement": "Dekrementieren",
	"Current language": "Aktuelle Sprache",
	"Stars": "Sterne",
	"Home": "Zuhause",
	"Fetching stars...": "Holte Sterne..",
	"Not found": "Nicht Gefunden"
}

--#

--% /rts/__mocks__/.fs.ts
// __mocks__/fs.js
"use strict";

export interface IStringifyable {
	toString: () => string;
}

export interface IFS {
	readFileSync: (filename: string) => IStringifyable;
	__setFileContents: (filename: string, content: string) => void;
	__clear: () => void;
}

const fs: IFS = (jest.genMockFromModule("fs") as IFS);
let files = {};
fs.readFileSync =  (filename) => {
	const match = Object.keys(files).filter((file: string) => {
		return filename.indexOf(file) !== -1;
	});
	return {
		toString: () => {
			return files[match[0]].content;
		}
	};
};

fs.__setFileContents = (filename, content) => {
	files[filename] = content;
};

fs.__clear = () => {
	files = {};
};

module.exports = fs;

--#

--% /rts/__mocks__/fileMock.js
module.exports = {};

--#

--% /rts/__mocks__/fs.js
// __mocks__/fs.js
"use strict";
var fs = jest.genMockFromModule("fs");
var files = {};
fs.readFileSync = function (filename) {
	let match = Object.keys(files).filter((file) => {
		return filename.indexOf(file) !== -1
	});
	return {
		toString: function () {
			return files[match[0]];
		}
	};
};

fs.__setFileContents = function (filename, content) {
	files[filename] = content;
};

fs.__clear = function() {
	files = {};
};
module.exports = fs;
--#

