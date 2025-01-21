--% index/fm.us
__TEMPLATE_PROJECT_DIR__,d(/mk)
	%utama=__FILE__
	%__TEMPLATE_SERVER_PORT__=9503

	__TEMPLATE_MTS_DIR__,d(/mk)

		# __TEMPLATE_WEBPACK_NAME__.js,f(e=utama=/webpack.js)
		.editorconfig,f(e=utama=/redcrypt/.editorconfig)
		# package.json,f(e=utama=/redcrypt/package.json)
		.env,f(e=utama=/redcrypt/.env.default)
		.gitignore,f(e=utama=/redcrypt/.gitignore)
		tsconfig.json,f(e=utama=/redcrypt/tsconfig.json)
		.sonarcloud.properties,f(e=utama=/redcrypt/.sonarcloud.properties)
		README.md,f(e=utama=/redcrypt/README.md)
		usef.md,f(e=utama=/redcrypt/usef.md)
		jest.config.js,f(e=utama=/redcrypt/jest.config.js)
		yarn.add.sh,f(e=utama=/yarn.add.sh)
		# run.sh,f(e=utama=/run.sh)
		$*chmod a+x *.sh
		# sementara tanpa webpack
		$*ln -s ../node_modules .
		public,d(/mk)
			index.html,f(e=utama=/redcrypt/public/index.html)
			favicon.ico,f(b64=utama=/redcrypt/public/favicon.ico)
		src,d(/mk)
			App.tsx,f(e=utama=/redcrypt/src/App.tsx)
			index.tsx,f(e=utama=/redcrypt/src/index.tsx)
			theme,d(/mk)
				index.ts,f(e=utama=/redcrypt/src/theme/index.ts)
				core,d(/mk)
					index.ts,f(e=utama=/redcrypt/src/theme/core/index.ts)
					font.ts,f(e=utama=/redcrypt/src/theme/core/font.ts)
			store,d(/mk)
				index.ts,f(e=utama=/redcrypt/src/store/index.ts)
				sagas.ts,f(e=utama=/redcrypt/src/store/sagas.ts)
				loading,d(/mk)
					storeKeys.ts,f(e=utama=/redcrypt/src/store/loading/storeKeys.ts)
					reducer.ts,f(e=utama=/redcrypt/src/store/loading/reducer.ts)
					index.ts,f(e=utama=/redcrypt/src/store/loading/index.ts)
					types.ts,f(e=utama=/redcrypt/src/store/loading/types.ts)
					__tests__,d(/mk)
						reducer.test.ts,f(e=utama=/redcrypt/src/store/loading/__tests__/reducer.test.ts)
				user,d(/mk)
					reducer.ts,f(e=utama=/redcrypt/src/store/user/reducer.ts)
					index.ts,f(e=utama=/redcrypt/src/store/user/index.ts)
					types.ts,f(e=utama=/redcrypt/src/store/user/types.ts)
					actions.ts,f(e=utama=/redcrypt/src/store/user/actions.ts)
					__tests__,d(/mk)
						reducer.test.ts,f(e=utama=/redcrypt/src/store/user/__tests__/reducer.test.ts)
			pages,d(/mk)
				Dashboard,d(/mk)
					Dashboard.container.ts,f(e=utama=/redcrypt/src/pages/Dashboard/Dashboard.container.ts)
					Dashboard.test.tsx,f(e=utama=/redcrypt/src/pages/Dashboard/Dashboard.test.tsx)
					index.ts,f(e=utama=/redcrypt/src/pages/Dashboard/index.ts)
					types.ts,f(e=utama=/redcrypt/src/pages/Dashboard/types.ts)
					Dashboard.tsx,f(e=utama=/redcrypt/src/pages/Dashboard/Dashboard.tsx)
					__snapshots__,d(/mk)
						Dashboard.test.tsx.snap,f(e=utama=/redcrypt/src/pages/Dashboard/__snapshots__/Dashboard.test.tsx.snap)
			components,d(/mk)
				index.ts,f(e=utama=/redcrypt/src/components/index.ts)
				layout,d(/mk)
					index.ts,f(e=utama=/redcrypt/src/components/layout/index.ts)
					ErrorBoundary,d(/mk)
						ErrorBoundary.test.tsx,f(e=utama=/redcrypt/src/components/layout/ErrorBoundary/ErrorBoundary.test.tsx)
						index.ts,f(e=utama=/redcrypt/src/components/layout/ErrorBoundary/index.ts)
						ErrorBoundary.tsx,f(e=utama=/redcrypt/src/components/layout/ErrorBoundary/ErrorBoundary.tsx)
					PageContent,d(/mk)
						PageContent.styled.tsx,f(e=utama=/redcrypt/src/components/layout/PageContent/PageContent.styled.tsx)
						PageContent.test.tsx,f(e=utama=/redcrypt/src/components/layout/PageContent/PageContent.test.tsx)
						PageContent.tsx,f(e=utama=/redcrypt/src/components/layout/PageContent/PageContent.tsx)
						index.ts,f(e=utama=/redcrypt/src/components/layout/PageContent/index.ts)
						types.ts,f(e=utama=/redcrypt/src/components/layout/PageContent/types.ts)
						__snapshots__,d(/mk)
							PageContent.test.tsx.snap,f(e=utama=/redcrypt/src/components/layout/PageContent/__snapshots__/PageContent.test.tsx.snap)
					Header,d(/mk)
						Header.tsx,f(e=utama=/redcrypt/src/components/layout/Header/Header.tsx)
						Header.test.tsx,f(e=utama=/redcrypt/src/components/layout/Header/Header.test.tsx)
						index.ts,f(e=utama=/redcrypt/src/components/layout/Header/index.ts)
						Header.styled.tsx,f(e=utama=/redcrypt/src/components/layout/Header/Header.styled.tsx)
						__snapshots__,d(/mk)
							Header.test.tsx.snap,f(e=utama=/redcrypt/src/components/layout/Header/__snapshots__/Header.test.tsx.snap)
					PageLayout,d(/mk)
						PageLayout.tsx,f(e=utama=/redcrypt/src/components/layout/PageLayout/PageLayout.tsx)
						PageLayout.styled.tsx,f(e=utama=/redcrypt/src/components/layout/PageLayout/PageLayout.styled.tsx)
						index.ts,f(e=utama=/redcrypt/src/components/layout/PageLayout/index.ts)
						PageLayout.test.tsx,f(e=utama=/redcrypt/src/components/layout/PageLayout/PageLayout.test.tsx)
					SideNav,d(/mk)
						SideNav.tsx,f(e=utama=/redcrypt/src/components/layout/SideNav/SideNav.tsx)
						SideNav.test.tsx,f(e=utama=/redcrypt/src/components/layout/SideNav/SideNav.test.tsx)
						index.ts,f(e=utama=/redcrypt/src/components/layout/SideNav/index.ts)
			routes,d(/mk)
				index.ts,f(e=utama=/redcrypt/src/routes/index.ts)
				Routes.tsx,f(e=utama=/redcrypt/src/routes/Routes.tsx)
				Routes.test.tsx,f(e=utama=/redcrypt/src/routes/Routes.test.tsx)
			utils,d(/mk)
				test-utils.tsx,f(e=utama=/redcrypt/src/utils/test-utils.tsx)
				index.ts,f(e=utama=/redcrypt/src/utils/index.ts)
				fetch.ts,f(e=utama=/redcrypt/src/utils/fetch.ts)
		.github,d(/mk)
			workflows,d(/mk)
				build.yml,f(e=utama=/redcrypt/.github/workflows/build.yml)
		.vscode,d(/mk)
			settings.json,f(e=utama=/redcrypt/.vscode/settings.json)
			rfc.code-snippets,f(e=utama=/redcrypt/.vscode/rfc.code-snippets)
			ead.code-snippets,f(e=utama=/redcrypt/.vscode/ead.code-snippets)
			extensions.json,f(e=utama=/redcrypt/.vscode/extensions.json)
		types,d(/mk)
			styled-components.d.ts,f(e=utama=/redcrypt/types/styled-components.d.ts)
			process.d.ts,f(e=utama=/redcrypt/types/process.d.ts)

		$*qterminal 2>/dev/null &
--#

--% /yarn.add.sh
yarn add @medly-components/core @medly-components/forms @medly-components/layout @medly-components/loaders @medly-components/theme axios react react-dom react-redux react-router-dom redux redux-saga styled-components

yarn add --dev @medly/babel-config-react @medly/eslint-config-react @medly/jest-config-react @medly/prettier-config @medly/stylelint-config @medly/typescript-config-react @medly/webpack-config @testing-library/react @types/react @types/react-dom @types/react-redux @types/react-router-dom @types/redux-mock-store @types/styled-components axios-mock-adapter husky lint-staged npm-run-all redux-devtools-extension redux-mock-store rimraf
--#

--% /run.sh
# ./node_modules/.bin/webpack serve --mode development --config __TEMPLATE_WEBPACK_NAME__
./node_modules/.bin/webpack serve --mode development --config node_modules/@medly/webpack-config
--#

--% /redcrypt/usef.md
masukkan ke package.json:
"babel": {
	"extends": "@medly/babel-config-react"
},
"eslintConfig": {
	"parser": "@typescript-eslint/parser",
	"extends": "@medly/react"
},
"stylelint": {
	"extends": "@medly/stylelint-config"
},
--#

--% /redcrypt/.editorconfig
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
max_line_length = 140
quote_type = single
spaces_around_brackets = true
spaces_around_operators = true
trim_trailing_whitespace = true


# identation
indent_style = space
indent_size = 4
--#

--% /redcrypt/package.json
{
	"name": "react-redux-typescript-boilerplate",
	"version": "1.0.0",
	"description": "React Redux Typescript boilerplate",
	"scripts": {
		"clean": "rimraf dist coverage",
		"lint:css": "stylelint 'src/**/*.tsx'",
		"lint:ts": "eslint 'src/**/*.{ts,tsx}'",
		"lint": "run-p lint:ts lint:css",
		"lint:fix": "run-p 'lint:ts --fix' 'lint:css --fix'",
		"test:update": "run-p test:types 'test:jest -- -u'",
		"test:watch": "run-p 'test:types -- -w' 'test:jest -- --watch'",
		"test:jest": "jest",
		"test:types": "tsc",
		"test": "run-p test:types test:jest",
		"watch": "webpack serve --mode development --config node_modules/@medly/webpack-config",
		"dist": "webpack --mode production --progress --config node_modules/@medly/webpack-config",
		"dist:analyze": "npm run dist -- --analyze"
	},
	"author": "Mukul Bansal",
	"license": "ISC",
	"husky": {
		"hooks": {
			"pre-commit": "lint-staged"
		}
	},
	"lint-staged": {
		"src/**/*.{ts,tsx}": [
			"eslint 'src/**/*.tsx' --fix",
			"stylelint 'src/**/*.tsx' --fix"
		]
	},
	"babel": {
		"extends": "@medly/babel-config-react"
	},
	"eslintConfig": {
		"parser": "@typescript-eslint/parser",
		"extends": "@medly/react"
	},
	"stylelint": {
		"extends": "@medly/stylelint-config"
	},
	"prettier": "@medly/prettier-config",
	"dependencies": {
		"@medly-components/core": "^1.54.0",
		"@medly-components/forms": "^1.22.2",
		"@medly-components/layout": "^1.22.2",
		"@medly-components/loaders": "^1.1.1",
		"@medly-components/theme": "^1.30.9",
		"axios": "^0.21.1",
		"react": "^17.0.2",
		"react-dom": "^17.0.2",
		"react-redux": "^7.2.4",
		"react-router-dom": "^5.2.0",
		"redux": "^4.1.0",
		"redux-saga": "^1.1.3",
		"styled-components": "^5.3.0"
	},
	"devDependencies": {
		"@medly/babel-config-react": "^0.1.4",
		"@medly/eslint-config-react": "^0.1.6",
		"@medly/jest-config-react": "^0.1.0",
		"@medly/prettier-config": "^0.1.1",
		"@medly/stylelint-config": "^0.1.2",
		"@medly/typescript-config-react": "^0.0.2",
		"@medly/webpack-config": "0.1.7",
		"@testing-library/react": "^11.2.7",
		"@types/react": "^17.0.11",
		"@types/react-dom": "^17.0.7",
		"@types/react-redux": "^7.1.16",
		"@types/react-router-dom": "^5.1.7",
		"@types/redux-mock-store": "^1.0.2",
		"@types/styled-components": "^5.1.10",
		"axios-mock-adapter": "^1.19.0",
		"husky": "4.3.8",
		"lint-staged": "^11.0.0",
		"npm-run-all": "^4.1.5",
		"redux-devtools-extension": "^2.13.9",
		"redux-mock-store": "^1.5.4",
		"rimraf": "^3.0.2"
	}
}

--#

--% /redcrypt/.env.default
API_URL=http://www.fake.com/api/0/
--#

--% /redcrypt/.gitignore
node_modules/
dist/
coverage/
.idea

--#

--% /redcrypt/tsconfig.json
{
	"extends": "@medly/typescript-config-react",
	"compilerOptions": {
		"baseUrl": "src",
		 "paths": {
			"@components": ["components"],
			"@components/*": ["components/*"],
			"@theme": ["theme"],
			"@theme/*": ["theme/*"],
			"@utils": ["utils"],
			"@utils/*": ["utils/*"],
			"@test-utils": ["utils/test-utils"],
			"@styled": ["utils/styled"],
			"@store": ["store"],
			"@store/*": ["store/*"],
			"@routes": ["routes"],
			"@routes/*": ["routes/*"],
			"@pages": ["pages"],
			"@pages/*": ["pages/*"]
		}
	},
	"include": ["src", "types"],
	"exclude": ["node_modules", "dist", "coverage"]
}

--#

--% /redcrypt/.sonarcloud.properties
sonar.sources=src
sonar.exclusions=**/*.test.*

--#

--% /redcrypt/README.md
# React Redux with Typescript Boilerplate

This boilerplate will help you to quick start your project.

"scripts": {
	"clean": "rimraf dist coverage",
	"lint:css": "stylelint 'src/**/*.tsx'",
	"lint:ts": "eslint 'src/**/*.{ts,tsx}'",
	"lint": "run-p lint:ts lint:css",
	"lint:fix": "run-p 'lint:ts --fix' 'lint:css --fix'",
	"test:update": "run-p test:types 'test:jest -- -u'",
	"test:watch": "run-p 'test:types -- -w' 'test:jest -- --watch'",
	"test:jest": "jest",
	"test:types": "tsc",
	"test": "run-p test:types test:jest",
	"watch": "webpack serve --mode development --config node_modules/@medly/webpack-config",
	"dist": "webpack --mode production --progress --config node_modules/@medly/webpack-config",
	"dist:analyze": "npm run dist -- --analyze"
},

## Getting Started

1. Just download this repo and change the project name **OR** click on `use this template` button to create the new repo.
2. Init the commitizen before committing anything in your new project. `npx commitizen init cz-conventional-changelog --yarn --dev --exact --force`

## Built With

🔥 [react](https://github.com/facebook/react)

🐠 [react-hooks](https://reactjs.org/docs/hooks-intro.html)

🚢 [redux](https://redux.js.org/)

⛑ [typescript](https://www.typescriptlang.org/)

🚀 [redux-saga](https://redux-saga.js.org/)

💥 [babel](https://babeljs.io/)

💅 [styled-components](https://www.styled-components.com)

🐐 [react-testing-library](https://github.com/kentcdodds/react-testing-library)

## npm scripts

-   `yarn lint` to run both css & ts lint
-   `yarn test` to run tests and type check
-   `yarn dist` to build your project
-   `yarn clean` to remove the dist and coverage folder
-   `yarn watch` to run your project locally
-   `yarn type-check` to run tsc to check types
-   `yarn bundle:analyze` to analyze the bundle size
-   `yarn lint:css` to run the css lint
-   `yarn lint:ts` to run the ts lint
-   `yarn test:update` to upgrate snapshots
-   `yarn test:watch` to watch tests
-   `yarn test:jest` to run test only
-   `yarn docker-watch` to be executed as the startup command for the Docker development container (no need to manually run)
-   `yarn image-build` to build the Docker development container
-   `yarn image-remove` to remove the Docker development container
-   `yarn docker-dev` to run the Docker development container with hot reloading
-   `yarn docker-stop` to stop the running Docker development container
-   `yarn docker-update-deps` to remove and rebuild the container image with updated dependencies
-   `yarn docker-exec` to open an interactive ash shell inside the container

## Table of Contents

1. [Create project directory](#-create-project-directory)
2. [Create npm package](#-create-npm-package)
3. [Create git repository](#-create-git-repository)
4. [Add react libraries](#-add-react-libraries)
5. [Add Eslint](#-add-eslint)
6. [Add Prettier](#-add-prettier)
7. [Add editorconfig file](#-add-editorconfig-file)
8. [Add Typescript](#-add-typescript)
9. [Add Vscode config files](#-add-vscode-config-files)
10. [Add Babel](#-add-babel)
11. [Add index.html](#-add-index.html)
12. [Add Webpack](#-add-webpack)
13. [Add React-hot-loader](#-add-react-hot-loader)
14. [Add Webpack plugins](#-add-webpack-plugins)
15. [Add stylelint](#-add-styleint)
16. [Add Jest](#-add-jest)
17. [Add commitizen & commitlint](#-add-commitizen-&-commitlint)
18. [Add Redux](#-add-redux)
19. [Add SVG Loader](#-add-svg-loader)

#### 1. Create project directory

	`mkdir my-project && cd my-project`

#### 2. Create npm package

	`npm init`

#### 3. Create git repository

	`git init`

#### 4. Add react libraries

	`yarn add react react-dom`

#### 5. Add Eslint

-   add eslint `yarn add -D eslint`

Explaining the important bits:

-   `parser: '@typescript-eslint/parser'` tells ESLint to use the parser package you installed ([`@typescript-eslint/parser`](../../../packages/parser)).
	-   This allows ESLint to understand TypeScript syntax.
	-   This is required, or else ESLint will throw errors as it tries to parse TypeScript code as if it were regular JavaScript.
-   `plugins: ['@typescript-eslint']` tells ESLint to load the plugin package you installed ([`@typescript-eslint/eslint-plugin`](../../../packages/eslint-plugin)).
	-   This allows you to use the rules within your codebase.
-   `extends: [ ... ]` tells ESLint that your config extends the given configurations.
	-   `eslint:recommended` is ESLint's inbuilt "recommended" config - it turns on a small, sensible set of rules which lint for well-known best-practices.
	-   `plugin:@typescript-eslint/eslint-recommended` is a configuration we provide which disables a few of the recommended rules from the previous set that we know are already covered by TypeScript's typechecker.
	-   `plugin:@typescript-eslint/recommended` is our "recommended" config - it's just like `eslint:recommended`, except it only turns on rules from our TypeScript-specific plugin.

Plugins

There are many plugins, each covering a different slice of the JS development world. Below are just a few examples, but there are [many, many more](https://www.npmjs.com/search?q=eslint-plugin).

-   Jest testing: [`eslint-plugin-jest`](https://www.npmjs.com/package/eslint-plugin-jest)
-   React best practices: [`eslint-plugin-react`](https://www.npmjs.com/package/eslint-plugin-react) and [`eslint-plugin-react-hooks`](https://www.npmjs.com/package/eslint-plugin-react-hooks)

So finally install `yarn add -D @typescript-eslint/eslint-plugin @typescript-eslint/parser eslint-plugin-jest eslint-plugin-react eslint-plugin-react-hooks`

-   eslint file would be like below:

```json
{
	"root": true,
	"env": {
		"es6": true,
		"browser": true,
		"jest/globals": true
	},
	"settings": {
		"react": {
			"version": "detect"
		}
	},
	"parserOptions": {
		"ecmaVersion": 11,
		"jsx": true,
		"project": "./tsconfig.json"
	},
	"parser": "@typescript-eslint/parser",
	"plugins": ["@typescript-eslint", "jest", "react-hooks", "prettier"],
	"extends": [
		"eslint:recommended",
		"plugin:@typescript-eslint/eslint-recommended",
		"plugin:@typescript-eslint/recommended",
		"plugin:jest/recommended",
		"plugin:react/recommended",
		"prettier/@typescript-eslint"
	],
	"rules": {
		"arrow-parens": ["error", "as-needed"],
		"react-hooks/rules-of-hooks": "error",
		"react-hooks/exhaustive-deps": "warn",
		"react/jsx-no-bind": "warn",
		"react/prop-types": "off",
		"@typescript-eslint/ban-ts-ignore": "off",
		"@typescript-eslint/explicit-function-return-type": "off"
	}
}
```

-   Add .eslintignore file

```
node_modules
dist
coverage
```

-   Add lint script in package.json

```json
{
	"script": {
		"lint": "run-p -c lint:*",
		"lint:ts": "eslint 'src/**/*.{ts,tsx}'"
	}
}
```

#### 6. Add Prettier

	`yarn add -D prettier eslint-config-prettier eslint-plugin-prettier`

add plugin in the esconfig file

```json
{
	// ...
	"plugins": ["@typescript-eslint", "jest", "react-hooks", "prettier"],
	"extends": [
		//...
		"prettier/@typescript-eslint"
	]
	//..
}
```

Add .preetierrc

```json
{
	"bracketSpacing": true,
	"printWidth": 140,
	"semi": true,
	"trailingComma": "none",
	"singleQuote": true,
	"tabWidth": 4,
	"arrowParens": "avoid"
}
```

#### 7. Add editorconfig file

.editorconfig

```
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
max_line_length = 140
quote_type = single
spaces_around_brackets = true
spaces_around_operators = true
trim_trailing_whitespace = true


# identation
indent_style = space
indent_size = 4
```

#### 8. Add Typescript

`yarn add -W typescript`

-   Add tsconfig.json

```json
{
	"compilerOptions": {
		"allowJs": true,
		"baseUrl": "src",
		"esModuleInterop": true,
		"isolatedModules": true,
		"forceConsistentCasingInFileNames": true,
		"jsx": "react",
		"lib": ["es2017", "es2015", "dom", "es2018.promise"],
		"module": "esnext",
		"moduleResolution": "node",
		"noEmit": true,
		"resolveJsonModule": true,
		"rootDir": "../",
		"skipLibCheck": true,
		"strict": true,
		"strictFunctionTypes": false,
		"strictNullChecks": false,
		"target": "esnext",
		"types": ["jest", "testing-library__jest-dom"],
		"paths": {
			"@components": ["components"],
			"@components/*": ["components/*"],
			"@theme": ["theme"],
			"@theme/*": ["theme/*"],
			"@utils": ["utils"],
			"@utils/*": ["utils/*"],
			"@test-utils": ["utils/test-utils"],
			"@styled": ["utils/styled"],
			"@store": ["store"],
			"@store/*": ["store/*"]
		}
	},
	"include": ["src"],
	"exclude": ["node_modules", ".commitlintrc"]
}
```

#### 9. Add Vscode config files

-   Add settings.json file

```json
{
	"editor.codeActionsOnSave": {
		"source.fixAll.eslint": true,
		"source.organizeImports": true,
		"source.fixAll.stylelint": true
	},
	"eslint.validate": ["html", "javascript", "javascriptreact", "typescript", "typescriptreact"],
	"cSpell.words": ["Medly"]
}
```

-   Add extensions.json file

```json
{
	"recommendations": [
		"eamodio.gitlens",
		"stylelint.vscode-stylelint",
		"dbaeumer.vscode-eslint",
		"esbenp.prettier-vscode",
		"jpoissonnier.vscode-styled-components",
		"streetsidesoftware.code-spell-checker"
	]
}
```

#### 10. Add Babel

	`yarn add -D babel-loader @babel/core @babel/preset-env @babel/preset-react @babel/preset-typescript`

Create babel.config.js file

```javascript
module.exports = function (api) {
	const presets = ['@babel/preset-env', '@babel/react', '@babel/typescript'],
		plugins = [];

	return { presets, plugins };
};
```

#### 11. Add index.html

#### **`public/index.html`**

```html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Boilerplate</title>
	</head>
	<body>
		<div id="root" />
	</body>
	<noscript>Your browser does not support JavaScript!</noscript>
</html>
```

#### 12. Add Webpack

	`yarn add -D webpack webpack-cli webpack-dev-server html-webpack-plugin`

Create webpack.config.js file

```javascript
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

const SRC = path.resolve(__dirname, './src/index');

module.exports = {
	entry: SRC,
	output: {
		path: path.join(__dirname, '/dist'),
		filename: 'bundle.js',
		publicPath: '/'
	},
	resolve: {
		extensions: ['.ts', '.tsx', '.js']
	},
	module: {
		rules: [
			{
				test: /\.(ts|js)x?$/,
				exclude: /node_modules/,
				use: {
					loader: 'babel-loader'
				}
			}
		]
	},
	devServer: {
		historyApiFallback: true
	},
	plugins: [
		new HtmlWebpackPlugin({
			template: './public/index.html'
		})
	]
};
```

Add script in package.json `"start": "webpack-dev-server --mode development --hot"`

#### 13. Add React-hot-loader

This will hot reload the app, keeping the components state.

-   install: `yarn add -D react-hot-loader @hot-loader/react-dom`
-   add plugin in babel.config.json

	```javascript
	//...
	if (api.env() === 'development') {
		plugins.push('react-hot-loader/babel');
	}
	//...
	```

-   add alias in webpack

	```javascript
	resolve: {
		alias: {
			'react-dom': '@hot-loader/react-dom',
		}
	}
	```

-   wrap your app in hot();
	`export default hot(App)`

#### 14. Add Webpack plugins

Few useful webpack plugins

`yarn add -D circular-dependency-plugin clean-webpack-plugin compression-webpack-plugin copy-webpack-plugin fork-ts-checker-webpack-plugin tsconfig-paths-webpack-plugin webpack-bundle-analyzer webpack-merge`

webpack.common.js

```javascript
const path = require('path');
const webpack = require('webpack');
const CopyPlugin = require('copy-webpack-plugin');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const TsconfigPathsPlugin = require('tsconfig-paths-webpack-plugin');
const CircularDependencyPlugin = require('circular-dependency-plugin');
const ForkTsCheckerWebpackPlugin = require('fork-ts-checker-webpack-plugin');
const CompressionPlugin = require('compression-webpack-plugin');

const SRC = path.resolve(__dirname, '../../src');
const DIST = path.resolve(__dirname, '../../dist');
const ENTRY = path.resolve(__dirname, '../../src/index');
const STATIC = path.resolve(__dirname, '../../public/static');
const INDEX_HTML = path.resolve(__dirname, '../../public/index.html');

module.exports = {
	entry: [ENTRY],
	performance: {
		maxAssetSize: 500000,
		maxEntrypointSize: 500000
	},
	resolve: {
		extensions: ['.js', '.ts', '.tsx', '.json'],
		symlinks: false,
		plugins: [new TsconfigPathsPlugin()]
	},
	module: {
		rules: [
			{
				test: /\.tsx?$/,
				include: SRC,
				exclude: [/node_modules/, /\.spec.tsx?$/, /\.test.tsx?$/, /__snapshots__/, /__tests__/],
				use: [
					{
						loader: 'thread-loader',
						options: {
							workers: 2,
							workerParallelJobs: 50
						}
					},
					'babel-loader'
				]
			}
		]
	},
	plugins: [
		new CleanWebpackPlugin(),
		new HtmlWebpackPlugin({
			template: INDEX_HTML,
			minify: {
				collapseWhitespace: true,
				removeComments: true
			}
		}),
		new CopyPlugin([{ from: STATIC, to: DIST }]),
		new ForkTsCheckerWebpackPlugin(),
		new CircularDependencyPlugin({
			exclude: /node_modules/,
			failOnError: true
		}),
		new webpack.HashedModuleIdsPlugin(),
		new CompressionPlugin()
	]
};
```

webpack.dev.js

```javascript
const path = require('path');
const merge = require('webpack-merge');
const common = require('./webpack.common.js');
const DIST = path.resolve(__dirname, '../../dist');

module.exports = merge(common, {
	mode: 'development',
	output: {
		path: DIST,
		filename: '[name].[hash].js',
		chunkFilename: '[name].[hash].js',
		publicPath: '/'
	},
	resolve: {
		alias: {
			'react-dom': '@hot-loader/react-dom'
		}
	},
	devServer: {
		hot: true,
		inline: true,
		overlay: true,
		historyApiFallback: true,
		disableHostCheck: true,
		stats: { children: false }
	}
});
```

webpack.prod.js

```javascript
const path = require('path');
const common = require('./webpack.common.js');
const merge = require('webpack-merge');
const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;
const DIST = path.resolve(__dirname, '../../dist');

const config = {
	mode: 'production',
	output: {
		path: DIST,
		filename: '[name].[contenthash].js',
		chunkFilename: '[name].[contenthash].js',
		publicPath: '/'
	},
	optimization: {
		moduleIds: 'hashed',
		runtimeChunk: 'single',
		splitChunks: {
			chunks: 'all',
			maxInitialRequests: 10,
			cacheGroups: {
				vendor: {
					test: /[\\/]node_modules[\\/]/,
					name(module) {
						const packageName = module.context.match(/[\\/]node_modules[\\/](.*?)([\\/]|$)/)[1];
						return `vendor~${packageName.replace('@', '')}`;
					}
				}
			}
		}
	}
};

if (process.env.BUNDLE_ANALYZE) config.plugins = [new BundleAnalyzerPlugin()];

module.exports = merge(common, config);
```

#### 15. Add stylelint

`yarn add -D stylelint stylelint-config-prettier stylelint-config-standard stylelint-config-styled-components stylelint-custom-processor-loader stylelint-prettier babel-plugin-styled-components`

-   add **`.stylelintrc`** file

```json
{
	"syntax": "scss",
	"plugins": ["stylelint-prettier"],
	"extends": ["stylelint-config-standard", "stylelint-config-styled-components", "stylelint-prettier/recommended"],
	"rules": {
		"prettier/prettier": true,
		"value-keyword-case": null,
		"declaration-empty-line-before": "never",
		"unit-no-unknown": [
			true,
			{
				"ignoreUnits": ["`"]
			}
		],
		"function-name-case": null
	}
}
```

-   add plugin in babel.config.js

```javascript
//...
plugins = [
	[
		'babel-plugin-styled-components',
		{
			pure: true,
			displayName: true,
			minify: true,
			transpileTemplateLiterals: true
		}
	]
];
//...
```

-   add loader for ts and tsx file

```javascript
[
	{
		loader: 'thread-loader',
		options: {
			workers: 2,
			workerParallelJobs: 50
		}
	},
	'babel-loader',
	'stylelint-custom-processor-loader'
];
```

-   add script in package.json file for linting

```json
{
	"lint": "run-p -c lint:**",
	"lint:css": "stylelint 'src/**/*.tsx'",
	"lint:ts": "eslint 'src/**/*.{ts,tsx}'"
}
```

#### 16. Add Jest

`yarn add -D jest @testing-library/react @testing-library/jest-dom jest-styled-components`

-   Add **_config/jest.config.js_**

```javascript
module.exports = {
	collectCoverage: true,
	coverageThreshold: {
		global: {
			branches: 100,
			functions: 100,
			lines: 100,
			statements: 100
		}
	},
	collectCoverageFrom: [
		'<rootDir>/src/**/*.(ts|tsx)',
		'!<rootDir>/**/index.(ts|tsx)',
		'!<rootDir>/src/App.tsx',
		'!<rootDir>/src/theme/**',
		'!<rootDir>/src/icons/**',
		'!<rootDir>/src/store/sagas.ts',
		'!<rootDir>/src/utils/styled.ts',
		'!<rootDir>/node_modules/**',
		'!<rootDir>/src/**/types.(ts|tsx)',
		'!<rootDir>/src/**/types/**',
		'!<rootDir>/src/utils/fetch.ts',
		'!<rootDir>/src/utils/test-utils.tsx'
	],
	coverageDirectory: '<rootDir>/coverage/',
	moduleFileExtensions: ['.mjs', 'ts', 'tsx', 'js', 'jsx', 'svg'],
	roots: ['<rootDir>/src/'],
	rootDir: '../../',
	setupFilesAfterEnv: ['<rootDir>/config/jest/setupAfterEnv.js'],
	testEnvironment: 'jsdom',
	testMatch: ['**/*.(spec|test).(ts|tsx)'],
	verbose: true,
	moduleNameMapper: {
		'\\.(css|less)$': '<rootDir>/config/jest/__mocks__/styleMock.js',
		'^@styled': '<rootDir>/src/utils/styled',
		'^@store(.*)$': '<rootDir>/src/store$1',
		'^@test-utils': '<rootDir>/src/utils/test-utils',
		'^@components(.*)$': '<rootDir>/src/components$1',
		'^@theme(.*)$': '<rootDir>/src/theme$1',
		'^@utils(.*)$': '<rootDir>/src/utils$1'
	}
};
```

-   Add localStorage file

```javascript
const storageMock = () => {
	const storage = {};

	return {
		setItem: (key, value) => {
			storage[key] = value || '';
		},

		getItem: key => {
			return key in storage ? storage[key] : null;
		},

		removeItem: key => {
			delete storage[key];
		}
	};
};

window.localStorage = storageMock();
```

-   Add setupAfterEnv file

```javascript
import '@testing-library/jest-dom/extend-expect';
import 'jest-styled-components';
```

-   Add style mock file for loading css of all the libraries

```javascript
module.exports = {};
```

-   Add jest-dom types in tsconfig file

```json
{
	"types": ["jest", "testing-library__jest-dom"]
}
```

#### 17. Add commitizen & commitlint

`yarn add -W husky commitizen @commitlint/cli @commitlint/config-conventional cz-conventional-changelog`

-   Add .commitlintrc file

```javascript
{
	"extends": [
		"@commitlint/config-conventional"
	]
}
```

-   Add configs in package.json

```json
{
	"config": {
		"commitizen": {
			"path": "./node_modules/cz-conventional-changelog"
		}
	},
	"husky": {
		"hooks": {
			"prepare-commit-msg": "exec < /dev/tty && git cz --hook || true",
			"commit-msg": "commitlint -E HUSKY_GIT_PARAMS"
		}
	}
}
```

#### 18. Add Redux

`yarn add redux react-redux redux-saga`

-   add other dev dependencies
	`yarn add -D @types/react-redux @babel/plugin-transform-runtime redux-devtools-extension redux-mock-store`

-   configure store

```javascript
import { applyMiddleware, combineReducers, createStore } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import reduxSaga from 'redux-saga';
import { rootSaga } from './sagas';
import { initialState as userInitialState, user } from './user';

export const initialState = {
		user: userInitialState
	},
	sagaMiddleware = reduxSaga(),
	rootReducer = combineReducers({
		user
	}),
	store = createStore(rootReducer, {}, composeWithDevTools(applyMiddleware(sagaMiddleware)));

sagaMiddleware.run(rootSaga);

export type AppState = ReturnType<typeof rootReducer>;
```

-   provide this store to app

```javascript
import { store } from '@store';
import { ThemeProvider } from 'styled-components';
import { defaultTheme } from '@theme';
import React from 'react';
import * as ReactDOM from 'react-dom';
import { Provider } from 'react-redux';
import App from './App';

ReactDOM.render(
	<Provider store={store}>
		<ThemeProvider theme={defaultTheme}>
			<>
				<App />
			</>
		</ThemeProvider>
	</Provider>,
	document.getElementById('root')
);
```

#### 18. Add SVG Loader

-   Add these packages `yarn add -D @svgr/webpack babel-plugin-inline-react-svg`

-   Add `inline-react-svg` in babel config plugins.

-   Add Svg loader in webpack config

```json
{
	"test": /\.svg$/,
	"use": [
		{
			"loader": "@svgr/webpack",
			"options": {
				"icon": true
			}
		}
	]
}
```

-   Add svg in extensions in jest config `moduleFileExtensions: ['.mjs', 'ts', 'tsx', 'js', 'jsx', 'svg'],`

--#

--% /redcrypt/jest.config.js
const { configure } = require('@medly/jest-config-react');

module.exports = configure({
	rootDir: './',
	collectCoverageFrom: ['!<rootDir>/src/utils/fetch.ts']
});

--#

--% /redcrypt/public/index.html
<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<title>Boilerplate</title>
	</head>
	<body>
		<div id="root"></div>
	</body>
	<noscript>Your browser does not support JavaScript!</noscript>
</html>

--#

--% /redcrypt/public/favicon.ico
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
--#

--% /redcrypt/src/App.tsx
import { ErrorBoundary, Header, PageLayout, SideNav } from '@components';
import { CssBaseline, ToastContainer } from '@medly-components/core';
import Routes from '@routes';
import { store } from '@store';
import { defaultTheme } from '@theme';
import React from 'react';
import { Provider } from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';
import { ThemeProvider } from 'styled-components';

const App: React.SFC = () => (
	<Provider store={store}>
		<ThemeProvider theme={defaultTheme}>
			<>
				<CssBaseline />
				<Router>
					<ErrorBoundary>
						<PageLayout>
							<ToastContainer position="top-end" />
							<SideNav />
							<Header />
							<Routes />
						</PageLayout>
					</ErrorBoundary>
				</Router>
			</>
		</ThemeProvider>
	</Provider>
);

export default App;

--#

--% /redcrypt/src/index.tsx
import React from 'react';
import * as ReactDOM from 'react-dom';
import App from './App';

ReactDOM.render(<App />, document.getElementById('root'));

--#

--% /redcrypt/src/theme/index.ts
import { defaultTheme as medlyDefaultTheme, Theme as MedlyTheme } from '@medly-components/theme';
import { coreDefaultTheme } from './core';

export const defaultTheme = {
	...medlyDefaultTheme,
	...coreDefaultTheme
};

export type Theme = MedlyTheme;

--#

--% /redcrypt/src/theme/core/index.ts
import font from './font';

export const coreDefaultTheme = {
	font
};

--#

--% /redcrypt/src/theme/core/font.ts
import { defaultTheme, FontTheme } from '@medly-components/theme';

const font: FontTheme = {
	...defaultTheme.font,
	defaults: {
		...defaultTheme.font.defaults,
		color: defaultTheme.colors.black
	}
};

export default font;

--#

--% /redcrypt/src/store/index.ts
import { TypedUseSelectorHook, useSelector } from 'react-redux';
import { applyMiddleware, combineReducers, createStore } from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import reduxSaga from 'redux-saga';
import { rootSaga } from './sagas';
import { initialState as userInitialState, user } from './user';
import { initialState as loadingInitialState, loading } from './loading';

export const initialState = {
		user: userInitialState,
		loading: loadingInitialState
	},
	sagaMiddleware = reduxSaga(),
	rootReducer = combineReducers({
		user,
		loading
	}),
	store = createStore(rootReducer, {}, composeWithDevTools(applyMiddleware(sagaMiddleware)));

sagaMiddleware.run(rootSaga);

export type AppState = ReturnType<typeof rootReducer>;

export const useTypedSelector: TypedUseSelectorHook<AppState> = useSelector;

--#

--% /redcrypt/src/store/sagas.ts
import { all } from 'redux-saga/effects';

export function* rootSaga(): Generator {
	yield all([]);
}

--#

--% /redcrypt/src/store/loading/storeKeys.ts
const storeKeys = ['dashboard'];

export default storeKeys;

--#

--% /redcrypt/src/store/loading/reducer.ts
import { Reducer } from 'redux';
import storeKeys from './storeKeys';
import { LoadingState } from './types';

export const initialState = storeKeys.reduce(
	(acc, curr) => ({
		...acc,
		[curr]: {
			isLoading: false
		}
	}),
	{} as LoadingState
);

/* eslint-disable @typescript-eslint/no-explicit-any */
export const loading: Reducer<LoadingState, any> = (state = initialState, action) => {
	const apiCallMatch = /@@(.*)\/FETCH/.exec(action.type),
		storeKey = apiCallMatch && apiCallMatch[1];

	switch (true) {
		case /.*FETCH_\w*REQUEST/.test(action.type):
			return {
				...state,
				[storeKey]: {
					isLoading: true
				}
			};

		case /.*FETCH_SUCCESS/.test(action.type):
		case /.*FETCH_FAILURE/.test(action.type):
			return {
				...state,
				[storeKey]: {
					isLoading: false
				}
			};

		default:
			return state;
	}
};

--#

--% /redcrypt/src/store/loading/index.ts
export * from './reducer';
export * from './types';

--#

--% /redcrypt/src/store/loading/types.ts
import storeKeys from './storeKeys';

export type StoreKeys = typeof storeKeys[number];

export interface LoadingField {
	readonly isLoading?: boolean;
}

export type LoadingState = {
	[k in StoreKeys]: LoadingField;
};

--#

--% /redcrypt/src/store/loading/__tests__/reducer.test.ts
import { loading, initialState } from '../reducer';

jest.mock('@medly-components/core');

describe('Loading reducer', () => {
	it('should start loading on any FETCH_*_REQUEST action', () => {
		const fetchAction = {
			type: '@@testData/FETCH_TEST_REQUEST'
		};
		expect(loading(initialState, fetchAction)).toEqual({
			...initialState,
			testData: {
				isLoading: true
			}
		});
	});

	test.each(['FETCH_SUCCESS', 'FETCH_FAILURE'])('should done loading on any given action', action => {
		const fetchAction = {
			type: `@@testData/${action}`
		};
		expect(loading(initialState, fetchAction)).toEqual({ ...initialState, testData: { isLoading: false } });
	});
});

--#

--% /redcrypt/src/store/user/reducer.ts
import { Reducer } from 'redux';
import { UserActions, UserActionTypes, UserState } from './types';

export const initialState: UserState = {
	userName: '',
	email: '',
	phoneNumber: '',
	groups: []
};

export const user: Reducer<UserState, UserActions> = (state = initialState, { type, ...payload }) => {
	switch (type) {
		case UserActionTypes.ADD_USER:
			return {
				...state,
				...payload
			};
		case UserActionTypes.REMOVE_USER:
			return {
				...initialState
			};
		default:
			return state;
	}
};

--#

--% /redcrypt/src/store/user/index.ts
export * from './types';
export * from './actions';
export * from './reducer';

--#

--% /redcrypt/src/store/user/types.ts
import { Action } from 'redux';

export enum UserActionTypes {
	ADD_USER = '@@user/ADD_USER',
	REMOVE_USER = '@@user/REMOVE_USER'
}

export type UserRoles = 'admin' | '2k+';

export interface UserState {
	userName: string;
	email: string;
	phoneNumber: string;
	groups: UserRoles[];
}

export interface AddUserAction extends Action {
	userName: string;
	email: string;
	phoneNumber: string;
	groups: UserRoles[];
	type: typeof UserActionTypes.ADD_USER;
}

export interface RemoveUserAction extends Action {
	type: typeof UserActionTypes.REMOVE_USER;
}

export type UserActions = AddUserAction | RemoveUserAction;

--#

--% /redcrypt/src/store/user/actions.ts
import { AddUserAction, RemoveUserAction, UserActionTypes, UserRoles } from './types';

export const addUser = (userName: string, email: string, phoneNumber: string, groups: UserRoles[]): AddUserAction => ({
	userName,
	email,
	phoneNumber,
	groups,
	type: UserActionTypes.ADD_USER
});

export const removeUser = (): RemoveUserAction => ({
	type: UserActionTypes.REMOVE_USER
});

--#

--% /redcrypt/src/store/user/__tests__/reducer.test.ts
import { addUser, removeUser } from '../actions';
import { initialState, user } from '../reducer';
import { UserState } from '../types';

describe('User reducer', () => {
	it('should return initial on first load', () => {
		expect(user(undefined, { type: undefined })).toEqual(initialState);
	});

	it('should handle ADD_USER action', () => {
		const expected = {
			email: 'dummy@dummy.com',
			phoneNumber: '+913434398394834',
			userName: 'Demo username',
			groups: ['admin', '2k+']
		};
		expect(user(initialState, addUser('Demo username', 'dummy@dummy.com', '+913434398394834', ['admin', '2k+']))).toEqual(expected);
	});

	it('should handle REMOVE_USER action', () => {
		const userSate: UserState = {
			userName: 'Demo username',
			email: 'dummy@dummy.com',
			phoneNumber: '+919082375498',
			groups: ['admin', '2k+']
		};
		expect(user(userSate, removeUser())).toEqual(initialState);
	});
});

--#

--% /redcrypt/src/pages/Dashboard/Dashboard.container.ts
import { AppState } from '@store';
import { connect } from 'react-redux';
import { Dashboard } from './Dashboard';
import { StateProps } from './types';

const mapStateToProps = ({ loading }: AppState): StateProps => ({
	isLoading: loading.dashboard.isLoading
});

export default connect<StateProps, unknown>(mapStateToProps, {})(Dashboard);

--#

--% /redcrypt/src/pages/Dashboard/Dashboard.test.tsx
import { renderWithRouter } from '@test-utils';
import React from 'react';
import reduxMockStore from 'redux-mock-store';
import { Provider } from 'react-redux';
import { initialState } from '@store';
import Dashboard from './Dashboard.container';

describe('Dashboard', () => {
	const mockStore = reduxMockStore(),
		renderDashboard = (store: ReturnType<typeof mockStore>) =>
			renderWithRouter(
				<Provider store={store}>
					<Dashboard />
				</Provider>
			);

	it('should render properly', () => {
		const store = mockStore({ ...initialState, loading: { dashboard: { isLoading: false } } });
		const { container } = renderDashboard(store);
		expect(container).toMatchSnapshot();
	});

	it('should show loading if isLoading Prop is true', () => {
		const store = mockStore({ ...initialState, loading: { dashboard: { isLoading: true } } });
		const { container } = renderDashboard(store);
		expect(container).toMatchSnapshot();
	});
});

--#

--% /redcrypt/src/pages/Dashboard/index.ts
import Dashboard from './Dashboard.container';

export default Dashboard;

--#

--% /redcrypt/src/pages/Dashboard/types.ts
export type StateProps = {
	isLoading: boolean;
};

export type Props = StateProps;

--#

--% /redcrypt/src/pages/Dashboard/Dashboard.tsx
import { PageContent } from '@components/layout';
import { Text } from '@medly-components/core';
import React from 'react';
import { Props } from './types';

export const Dashboard: React.FunctionComponent<Props> = ({ isLoading }) => (
	<PageContent isLoading={isLoading}>
		<Text textWeight="Strong" textVariant="body1">
			Dashboard Content
		</Text>
	</PageContent>
);

--#

--% /redcrypt/src/pages/Dashboard/__snapshots__/Dashboard.test.tsx.snap
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`Dashboard should render properly 1`] = `
.c2 {
	margin: 0;
	color: inherit;
	font-size: 1.6rem;
	font-weight: 700;
	-webkit-letter-spacing: 0rem;
	-moz-letter-spacing: 0rem;
	-ms-letter-spacing: 0rem;
	letter-spacing: 0rem;
	line-height: 2.6rem;
	text-align: initial;
}

.c0 {
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	-webkit-flex-direction: column;
	-ms-flex-direction: column;
	flex-direction: column;
	padding: 2rem;
	position: fixed;
	z-index: 1001;
	top: 0;
	right: 0;
}

.c0 > * + * {
	margin-top: 2rem;
}

.c1 {
	background-color: #eff2f4;
	overflow: auto;
	padding-top: 32px;
}

@media (max-width:1279px) {
	.c1 {
	padding-left: 24px;
	padding-right: 24px;
	}
}

@media (min-width:1280px) {
	.c1 {
	padding-left: calc(24px + (((100vw - 1280px) / 160) * 16));
	padding-right: calc(24px + (((100vw - 1280px) / 160) * 16));
	}
}

@media (min-width:1440px) {
	.c1 {
	padding-left: 40px;
	padding-right: 40px;
	}
}

<div>
	<div
	class="c0"
	/>
	<main
	class="c1"
	>
	<strong
		class="c2"
	>
		Dashboard Content
	</strong>
	</main>
</div>
`;

exports[`Dashboard should show loading if isLoading Prop is true 1`] = `
.c4 {
	margin: 0;
	color: inherit;
	font-size: 1.6rem;
	font-weight: 700;
	-webkit-letter-spacing: 0rem;
	-moz-letter-spacing: 0rem;
	-ms-letter-spacing: 0rem;
	letter-spacing: 0rem;
	line-height: 2.6rem;
	text-align: initial;
}

.c0 {
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	-webkit-flex-direction: column;
	-ms-flex-direction: column;
	flex-direction: column;
	padding: 2rem;
	position: fixed;
	z-index: 1001;
	top: 0;
	right: 0;
}

.c0 > * + * {
	margin-top: 2rem;
}

.c3 {
	font-size: 56px;
}

.c3 * {
	fill: #126AFA;
}

.c1 {
	background-color: #eff2f4;
	overflow: auto;
	padding-top: 32px;
}

.c2 {
	position: fixed;
	top: 0;
	bottom: 0;
	right: 0;
	left: 0;
	background-color: rgba(255,255,255,0.7);
	z-index: 1;
}

@media (max-width:1279px) {
	.c1 {
	padding-left: 24px;
	padding-right: 24px;
	}
}

@media (min-width:1280px) {
	.c1 {
	padding-left: calc(24px + (((100vw - 1280px) / 160) * 16));
	padding-right: calc(24px + (((100vw - 1280px) / 160) * 16));
	}
}

@media (min-width:1440px) {
	.c1 {
	padding-left: 40px;
	padding-right: 40px;
	}
}

<div>
	<div
	class="c0"
	/>
	<main
	class="c1"
	>
	<div
		class="c2"
	>
		<svg
		class="c3"
		height="1em"
		viewBox="0 0 100 100"
		width="1em"
		xmlns="http://www.w3.org/2000/svg"
		>
		<path
			d="M82 35.7C74.1 18 53.4 10.1 35.7 18S10.1 46.6 18 64.3l7.6-3.4c-6-13.5 0-29.3 13.5-35.3s29.3 0 35.3 13.5l7.6-3.4z"
		>
			<animatetransform
			attributeName="transform"
			attributeType="XML"
			dur="2s"
			from="0 50 50"
			repeatCount="indefinite"
			to="360 50 50"
			type="rotate"
			/>
		</path>
		</svg>
	</div>
	<strong
		class="c4"
	>
		Dashboard Content
	</strong>
	</main>
</div>
`;

--#

--% /redcrypt/src/components/index.ts
export * from './layout';

--#

--% /redcrypt/src/components/layout/index.ts
export { default as ErrorBoundary } from './ErrorBoundary';
export { default as Header } from './Header';
export { default as PageContent } from './PageContent';
export { default as PageLayout } from './PageLayout';
export { default as SideNav } from './SideNav';

--#

--% /redcrypt/src/components/layout/ErrorBoundary/ErrorBoundary.test.tsx
import { renderWithStoreAndRouter } from '@test-utils';
import React from 'react';
import PageContent from '../PageContent';
import ErrorBoundary from './ErrorBoundary';

describe('ErrorBoundary component', () => {
	beforeEach(() => {
		jest.spyOn(console, 'error');
		// @ts-ignore
		console.error.mockImplementation(() => {
			return null;
		});
	});

	afterEach(() => {
		// @ts-ignore
		console.error.mockRestore();
	});
	it('should render properly', () => {
		const dummy = jest
			.fn()
			.mockReturnValueOnce(() => {
				throw new Error('Something went wrong');
			})
			.mockReturnValue(() => 'Success');

		const ErrorComponent = () => <div>{dummy()()}</div>;
		const { container } = renderWithStoreAndRouter(
			<ErrorBoundary>
				<PageContent>
					<ErrorComponent />
				</PageContent>
			</ErrorBoundary>
		);
		expect(container).toHaveTextContent('Success');
	});
});

--#

--% /redcrypt/src/components/layout/ErrorBoundary/index.ts
import ErrorBoundary from './ErrorBoundary';

export default ErrorBoundary;

--#

--% /redcrypt/src/components/layout/ErrorBoundary/ErrorBoundary.tsx
import React from 'react';
import { RouteComponentProps, withRouter } from 'react-router-dom';

class ErrorBoundary extends React.PureComponent<RouteComponentProps> {
	public componentDidCatch() {
		this.props.history.push(this.props.location.pathname);
	}

	public render() {
		return <>{this.props.children}</>;
	}
}

export default withRouter(ErrorBoundary);

--#

--% /redcrypt/src/components/layout/PageContent/PageContent.styled.tsx
import styled from 'styled-components';

export const PageContent = styled('main')`
	background-color: #eff2f4;
	overflow: auto;
	padding-top: 32px;

	@media (max-width: 1279px) {
		padding-left: 24px;
		padding-right: 24px;
	}

	@media (min-width: 1280px) {
		padding-left: calc(24px + (((100vw - 1280px) / 160) * 16));
		padding-right: calc(24px + (((100vw - 1280px) / 160) * 16));
	}

	@media (min-width: 1440px) {
		padding-left: 40px;
		padding-right: 40px;
	}
`;

export const Loader = styled('div')`
	position: fixed;
	top: 0;
	bottom: 0;
	right: 0;
	left: 0;
	background-color: rgba(255, 255, 255, 0.7);
	z-index: 1;
`;

--#

--% /redcrypt/src/components/layout/PageContent/PageContent.test.tsx
import { render } from '@test-utils';
import React from 'react';
import { PageContent } from './PageContent';

describe('PageContent component', () => {
	it('should render properly', () => {
		const { container } = render(<PageContent>Demo PageContent</PageContent>);
		expect(container).toMatchSnapshot();
	});
	it('should render with loader properly', () => {
		const { container } = render(<PageContent isLoading={true}>Demo PageContent</PageContent>);
		expect(container).toMatchSnapshot();
	});
});

--#

--% /redcrypt/src/components/layout/PageContent/PageContent.tsx
import { WithStyle } from '@medly-components/utils';
import { CircleLoader } from '@medly-components/loaders';
import React from 'react';
import * as Styled from './PageContent.styled';
import { Props } from './types';

export const PageContent: React.SFC<Props> & WithStyle = props => {
	return (
		<Styled.PageContent {...props}>
			{props.isLoading && (
				<Styled.Loader>
					<CircleLoader />
				</Styled.Loader>
			)}
			{props.children}
		</Styled.PageContent>
	);
};

PageContent.displayName = 'PageContent';
PageContent.Style = Styled.PageContent;

--#

--% /redcrypt/src/components/layout/PageContent/index.ts
export { PageContent as default } from './PageContent';

--#

--% /redcrypt/src/components/layout/PageContent/types.ts
export interface Props {
	isLoading?: boolean;
}

--#

--% /redcrypt/src/components/layout/PageContent/__snapshots__/PageContent.test.tsx.snap
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`PageContent component should render properly 1`] = `
.c0 {
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	-webkit-flex-direction: column;
	-ms-flex-direction: column;
	flex-direction: column;
	padding: 2rem;
	position: fixed;
	z-index: 1001;
	top: 0;
	right: 0;
}

.c0 > * + * {
	margin-top: 2rem;
}

.c1 {
	background-color: #eff2f4;
	overflow: auto;
	padding-top: 32px;
}

@media (max-width:1279px) {
	.c1 {
	padding-left: 24px;
	padding-right: 24px;
	}
}

@media (min-width:1280px) {
	.c1 {
	padding-left: calc(24px + (((100vw - 1280px) / 160) * 16));
	padding-right: calc(24px + (((100vw - 1280px) / 160) * 16));
	}
}

@media (min-width:1440px) {
	.c1 {
	padding-left: 40px;
	padding-right: 40px;
	}
}

<div>
	<div
	class="c0"
	/>
	<main
	class="c1"
	>
	Demo PageContent
	</main>
</div>
`;

exports[`PageContent component should render with loader properly 1`] = `
.c0 {
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	-webkit-flex-direction: column;
	-ms-flex-direction: column;
	flex-direction: column;
	padding: 2rem;
	position: fixed;
	z-index: 1001;
	top: 0;
	right: 0;
}

.c0 > * + * {
	margin-top: 2rem;
}

.c3 {
	font-size: 56px;
}

.c3 * {
	fill: #126AFA;
}

.c1 {
	background-color: #eff2f4;
	overflow: auto;
	padding-top: 32px;
}

.c2 {
	position: fixed;
	top: 0;
	bottom: 0;
	right: 0;
	left: 0;
	background-color: rgba(255,255,255,0.7);
	z-index: 1;
}

@media (max-width:1279px) {
	.c1 {
	padding-left: 24px;
	padding-right: 24px;
	}
}

@media (min-width:1280px) {
	.c1 {
	padding-left: calc(24px + (((100vw - 1280px) / 160) * 16));
	padding-right: calc(24px + (((100vw - 1280px) / 160) * 16));
	}
}

@media (min-width:1440px) {
	.c1 {
	padding-left: 40px;
	padding-right: 40px;
	}
}

<div>
	<div
	class="c0"
	/>
	<main
	class="c1"
	>
	<div
		class="c2"
	>
		<svg
		class="c3"
		height="1em"
		viewBox="0 0 100 100"
		width="1em"
		xmlns="http://www.w3.org/2000/svg"
		>
		<path
			d="M82 35.7C74.1 18 53.4 10.1 35.7 18S10.1 46.6 18 64.3l7.6-3.4c-6-13.5 0-29.3 13.5-35.3s29.3 0 35.3 13.5l7.6-3.4z"
		>
			<animatetransform
			attributeName="transform"
			attributeType="XML"
			dur="2s"
			from="0 50 50"
			repeatCount="indefinite"
			to="360 50 50"
			type="rotate"
			/>
		</path>
		</svg>
	</div>
	Demo PageContent
	</main>
</div>
`;

--#

--% /redcrypt/src/components/layout/Header/Header.tsx
import { Avatar, Text } from '@medly-components/core';
import { WithStyle } from '@medly-components/utils';
import React from 'react';
import * as Styled from './Header.styled';

export const Header: React.SFC & WithStyle = () => {
	return (
		<Styled.Header>
			<Styled.LeftSide>
				<Text textWeight="Strong" textVariant="h4">
					Boilerplate
				</Text>
			</Styled.LeftSide>
			<Styled.RightSide>
				<Avatar size="M">JD</Avatar>
			</Styled.RightSide>
		</Styled.Header>
	);
};

Header.displayName = 'Header';
Header.Style = Styled.Header;

export default Header;

--#

--% /redcrypt/src/components/layout/Header/Header.test.tsx
import { render } from '@test-utils';
import React from 'react';
import Header from './Header';

describe('Header', () => {
	it('should render properly', () => {
		const { container } = render(<Header />);
		expect(container).toMatchSnapshot();
	});
});

--#

--% /redcrypt/src/components/layout/Header/index.ts
export { Header as default } from './Header';

--#

--% /redcrypt/src/components/layout/Header/Header.styled.tsx
import styled from 'styled-components';

export const Header = styled('header')`
	min-height: 72px;
	background-color: white;
	padding: 0 2%;
	box-shadow: 0 2px 8 rgba(176, 188, 200, 0.2);
	display: flex;
	align-items: center;
	justify-content: space-between;
`;

export const LeftSide = styled('div')`
	display: flex;
	align-items: center;
	& > * {
		margin-right: ${({ theme }) => theme.spacing.S2};
	}
`;

export const RightSide = styled('div')`
	display: flex;
	align-items: center;
	& > * {
		margin-left: ${({ theme }) => theme.spacing.S2};
	}
`;

--#

--% /redcrypt/src/components/layout/Header/__snapshots__/Header.test.tsx.snap
// Jest Snapshot v1, https://goo.gl/fbAQLP

exports[`Header should render properly 1`] = `
.c4 {
	margin: 0;
	color: inherit;
	font-size: 1.8rem;
	font-weight: 700;
	-webkit-letter-spacing: -0.02rem;
	-moz-letter-spacing: -0.02rem;
	-ms-letter-spacing: -0.02rem;
	letter-spacing: -0.02rem;
	line-height: 2.4rem;
	text-align: initial;
}

.c7 {
	margin: 0;
	color: inherit;
	font-size: 1.4rem;
	font-weight: 700;
	-webkit-letter-spacing: 0rem;
	-moz-letter-spacing: 0rem;
	-ms-letter-spacing: 0rem;
	letter-spacing: 0rem;
	line-height: 2.2rem;
	text-align: initial;
	text-transform: uppercase;
}

.c6 {
	display: inline-block;
	text-align: center;
	min-width: -webkit-max-content;
	min-width: -moz-max-content;
	min-width: max-content;
	width: 4rem;
	height: 4rem;
	border-radius: 50%;
	overflow: hidden;
	cursor: inherit;
	color: #126AFA;
	background: #E7F0FF;
	-webkit-user-select: none;
	-moz-user-select: none;
	-ms-user-select: none;
	user-select: none;
}

.c6 .c3 {
	line-height: 4rem;
	font-size: 1.6rem;
	font-weight: 400;
	font-family: Open Sans;
}

.c6 img {
	width: 4rem;
	height: 4rem;
	object-fit: cover;
	border: 0.1rem solid #dfe4e9;
	box-sizing: border-box;
	border-radius: 50%;
}

.c0 {
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	-webkit-flex-direction: column;
	-ms-flex-direction: column;
	flex-direction: column;
	padding: 2rem;
	position: fixed;
	z-index: 1001;
	top: 0;
	right: 0;
}

.c0 > * + * {
	margin-top: 2rem;
}

.c1 {
	min-height: 72px;
	background-color: white;
	padding: 0 2%;
	box-shadow: 0 2px 8 rgba(176,188,200,0.2);
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	-webkit-align-items: center;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
	-webkit-box-pack: justify;
	-webkit-justify-content: space-between;
	-ms-flex-pack: justify;
	justify-content: space-between;
}

.c2 {
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	-webkit-align-items: center;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
}

.c2 > * {
	margin-right: 0.8rem;
}

.c5 {
	display: -webkit-box;
	display: -webkit-flex;
	display: -ms-flexbox;
	display: flex;
	-webkit-align-items: center;
	-webkit-box-align: center;
	-ms-flex-align: center;
	align-items: center;
}

.c5 > * {
	margin-left: 0.8rem;
}

<div>
	<div
	class="c0"
	/>
	<header
	class="c1"
	>
	<div
		class="c2"
	>
		<h4
		class="c3 c4"
		>
		Boilerplate
		</h4>
	</div>
	<div
		class="c5"
	>
		<div
		class="c6"
		>
		<strong
			class="c3 c7"
		>
			JD
		</strong>
		</div>
	</div>
	</header>
</div>
`;

--#

--% /redcrypt/src/components/layout/PageLayout/PageLayout.tsx
import React, { HTMLProps } from 'react';
import { PageLayoutStyled } from './PageLayout.styled';

const PageLayout: React.FC<HTMLProps<HTMLDivElement>> = React.memo(({ children }) => {
	return <PageLayoutStyled>{children}</PageLayoutStyled>;
});

PageLayout.displayName = 'PageLayout';

export default PageLayout;

--#

--% /redcrypt/src/components/layout/PageLayout/PageLayout.styled.tsx
import styled from 'styled-components';

export const PageLayoutStyled = styled('div')`
	display: grid;
	height: 100%;
	width: 100%;
	grid-template-areas:
		'aside header'
		'aside  main';
	grid-template-rows: max-content auto;
	grid-template-columns: auto 1fr;

	& > aside {
		grid-area: aside;
	}

	& > header {
		grid-area: header;
	}

	& > main {
		grid-area: main;
		transition: width 200ms;
	}
`;

--#

--% /redcrypt/src/components/layout/PageLayout/index.ts
import PageLayout from './PageLayout';

export default PageLayout;

--#

--% /redcrypt/src/components/layout/PageLayout/PageLayout.test.tsx
import { render } from '@test-utils';
import React from 'react';
import Header from '../Header';
import PageContent from '../PageContent';
import PageLayout from './PageLayout';

describe('PageLayout component', () => {
	it('should render properly', () => {
		const { container } = render(
			<PageLayout>
				<Header />
				<PageContent>
					<div>Success</div>
				</PageContent>
			</PageLayout>
		);
		expect(container).toHaveTextContent('Success');
	});
});

--#

--% /redcrypt/src/components/layout/SideNav/SideNav.tsx
import { Text } from '@medly-components/core';
import { DashboardIcon } from '@medly-components/icons';
import { MedlySidenavHeader, SideNav as MedlySideNav } from '@medly-components/layout';
import { WithStyle } from '@medly-components/utils';
import React, { useCallback } from 'react';
import { useHistory, useLocation } from 'react-router-dom';

export const SideNav: React.SFC & WithStyle = React.memo(() => {
	const { pathname } = useLocation(),
		history = useHistory(),
		handlePathChange = useCallback((page: string) => history.push(page), [history]);
	return (
		<MedlySideNav onChange={handlePathChange} active={pathname} defaultActive="/">
			<MedlySidenavHeader />
			<MedlySideNav.List>
				<MedlySideNav.Nav path="/">
					<DashboardIcon />
					<Text>Dashboard</Text>
				</MedlySideNav.Nav>

				<MedlySideNav.Nav path="/2">
					<DashboardIcon />
					<Text>Kedua</Text>
				</MedlySideNav.Nav>

				<MedlySideNav.Nav path="/3">
					<DashboardIcon />
					<Text>Ketiga</Text>
				</MedlySideNav.Nav>
			</MedlySideNav.List>
		</MedlySideNav>
	);
});
SideNav.displayName = 'AppSideNav';
SideNav.Style = MedlySideNav.Style;

--#

--% /redcrypt/src/components/layout/SideNav/SideNav.test.tsx
import { cleanup, fireEvent, renderWithRouter } from '@test-utils';
import React from 'react';
import { SideNav } from './SideNav';

const mockHistoryPush = jest.fn();

jest.mock('react-router-dom', () => ({
	...(jest.requireActual('react-router-dom') as any),
	useHistory: () => ({
		push: mockHistoryPush
	})
}));

describe('SideNav', () => {
	afterEach(cleanup);

	it('should call history.push on click on dashboard', async () => {
		const { getByText } = renderWithRouter(<SideNav />);
		fireEvent.click(getByText('Dashboard'));
		expect(mockHistoryPush).toHaveBeenCalledWith('/');
	});
});

--#

--% /redcrypt/src/components/layout/SideNav/index.ts
export { SideNav as default } from './SideNav';

--#

--% /redcrypt/src/routes/index.ts
export { Routes as default } from './Routes';

--#

--% /redcrypt/src/routes/Routes.tsx
import React, { lazy, Suspense } from 'react';
import { Route, Switch } from 'react-router-dom';

const Dashboard = lazy(() => import(
	/* webpackChunkName: "Dashboard" */ 
	/* webpackPrefetch: true */ 
	'@pages/Dashboard')
);

const Kedua = () => (<h1>kedua</h1>)
const Ketiga = () => (<h1>Ketiga</h1>)

export const Routes: React.SFC = () => (
	<Suspense fallback={<span>Loading ...</span>}>
		<Switch>
			<Route exact path="/" component={Dashboard} />
			<Route exact path="/2" component={Kedua} />
			<Route exact path="/3" component={Ketiga} />
		</Switch>
	</Suspense>
);

--#

--% /redcrypt/src/routes/Routes.test.tsx
import { cleanup, renderWithStore } from '@test-utils';
import React from 'react';
import { MemoryRouter } from 'react-router-dom';
import { Routes } from './Routes';

describe('Routes', () => {
	afterEach(cleanup);

	it('should render dashboard page properly', async () => {
		const { findByText } = renderWithStore(
			<MemoryRouter initialEntries={[{ pathname: `/` }]}>
				<Routes />
			</MemoryRouter>
		);
		const dashboard = await findByText('Dashboard Content', {}, { timeout: 5000 });
		expect(dashboard).toBeInTheDocument();
	});
});

--#

--% /redcrypt/src/utils/test-utils.tsx
import { ToastContainer } from '@medly-components/core';
import { initialState } from '@store';
import { rootSaga } from '@store/sagas';
import { render, RenderOptions, RenderResult } from '@testing-library/react';
import { defaultTheme } from '@theme';
import axios from 'axios';
import MockAdapter from 'axios-mock-adapter';
import React from 'react';
import { Provider } from 'react-redux';
import { MemoryRouter } from 'react-router-dom';
import reduxMockStore from 'redux-mock-store';
import reduxSaga from 'redux-saga';
import { ThemeProvider } from 'styled-components';

export const mockAxios = new MockAdapter(axios);

const sagaMiddleware = reduxSaga();

const mockStore = reduxMockStore([sagaMiddleware]),
	store = mockStore({
		...initialState,
		user: { ...initialState.user, groups: ['admin'] }
	});
sagaMiddleware.run(rootSaga);

const WithThemeProvider: React.FunctionComponent = props => (
	<ThemeProvider theme={defaultTheme}>
		<>
			<ToastContainer position="top-end" />
			{props.children}
		</>
	</ThemeProvider>
);

const WithStore: React.FunctionComponent = props => (
	<Provider store={store}>
		<WithThemeProvider>{props.children}</WithThemeProvider>
	</Provider>
);

const WithRouter: React.FunctionComponent = props => (
	<MemoryRouter>
		<WithThemeProvider>{props.children}</WithThemeProvider>
	</MemoryRouter>
);

const WithStoreAndRouter: React.FunctionComponent = props => (
	<Provider store={store}>
		<MemoryRouter>
			<WithThemeProvider>{props.children}</WithThemeProvider>
		</MemoryRouter>
	</Provider>
);

const customRender = (ui: React.ReactElement, options?: RenderOptions): RenderResult =>
	render(ui, { wrapper: WithThemeProvider, ...options });

export const renderWithStore = (ui: React.ReactElement, options?: RenderOptions): RenderResult =>
	render(ui, { wrapper: WithStore, ...options });

export const renderWithRouter = (ui: React.ReactElement, options?: RenderOptions): RenderResult =>
	render(ui, { wrapper: WithRouter, ...options });

export const renderWithStoreAndRouter = (ui: React.ReactElement, options?: RenderOptions): RenderResult =>
	render(ui, { wrapper: WithStoreAndRouter, ...options });

// re-export everything
export * from '@testing-library/react';
// override render method
export { customRender as render, store };

--#

--% /redcrypt/src/utils/index.ts
export * from './fetch';

--#

--% /redcrypt/src/utils/fetch.ts
/* eslint-disable @typescript-eslint/no-explicit-any */
import axios, { AxiosRequestConfig, AxiosResponse } from 'axios';

export interface AxiosReturn {
	response?: AxiosResponse<any>;
	error?: AxiosResponse<any>;
}

export async function fetch(config: AxiosRequestConfig): Promise<AxiosReturn> {
	try {
		const request = {
			...config,
			headers: {
				...(config.headers ? config.headers : {})
			}
		};
		const response = await axios(request);
		return { response: { ...(response || { config, status: 500, data: '', headers: '', statusText: '' }) } };
	} catch (error) {
		return { error: { ...(error.response || { status: 500, data: error, variant: 'error' }) } };
	}
}

--#

--% /redcrypt/.github/workflows/build.yml
name: Build

on: [push, label, release, pull_request]

jobs:
	build:
		runs-on: ubuntu-latest
		steps:
			- name: Checkout repo
				uses: actions/checkout@v2

			- name: Setup Node.js
				uses: actions/setup-node@v1
				with:
					node-version: '12.x'

			- name: Install dependencies
				run: yarn

			- name: Clean
				run: yarn clean

			- name: Linting
				run: yarn lint

			- name: Run tests
				run: yarn test

			- name: Create bundle
				run: yarn dist

			- name: Upload test coverage
				uses: actions/upload-artifact@v2
				with:
					name: coverage
					path: coverage

			- name: Upload dist
				uses: actions/upload-artifact@v2
				with:
					name: dist
					path: dist

--#

--% /redcrypt/.vscode/settings.json
{
	"editor.formatOnSave": true,
	"editor.codeActionsOnSave": {
		"source.fixAll.eslint": true,
		"source.organizeImports": true,
		"source.fixAll.stylelint": true
	},
	"eslint.validate": ["html", "javascript", "javascriptreact", "typescript", "typescriptreact"],
	"cSpell.words": ["Medly"]
}

--#

--% /redcrypt/.vscode/rfc.code-snippets
{
	"Medly: React functional component": {
		"scope": "javascript,javascriptreact,typescript,typescriptreact",
		"prefix": ["react", "rfc"],
		"body": [
			"import React from 'react'; \n \nexport const ${1:Component}: React.FC = React.memo(() => {\n    return <${2}></>;\n});\n\n${1}.displayName = '${1}';"
		],
		"description": "Create new react functional component"
	}
}

--#

--% /redcrypt/.vscode/ead.code-snippets
{
	"Medly: Export as default": {
		"scope": "javascript,javascriptreact,typescript,typescriptreact",
		"prefix": ["export", "ead"],
		"body": ["export { ${1:Component} as default } from './${1}'"],
		"description": "export non default function as default in index.ts"
	}
}

--#

--% /redcrypt/.vscode/extensions.json
{
	"recommendations": [
		"eamodio.gitlens",
		"stylelint.vscode-stylelint",
		"dbaeumer.vscode-eslint",
		"esbenp.prettier-vscode",
		"jpoissonnier.vscode-styled-components",
		"streetsidesoftware.code-spell-checker"
	]
}

--#

--% /redcrypt/types/styled-components.d.ts
import { Theme } from '@medly-components/theme';
import 'styled-components';

declare module 'styled-components' {
	export type DefaultTheme = Theme;
}

--#

--% /redcrypt/types/process.d.ts
declare const process: {
	env: {
		// Example:
		// API_URL: string;
	};
};

--#
