--% index/fmus
.,d(/mk)
	$* ln -s  /mnt/c/node_modules/_iso-node-rjs/node_modules .
	%utama=__FILE__
	.browserslistrc,f(e=utama=C:/tmp/wd4/project1/.browserslistrc)
	.gitignore,f(e=utama=C:/tmp/wd4/project1/.gitignore)
	env.config.js,f(e=utama=C:/tmp/wd4/project1/env.config.js)
	package.json,f(e=utama=C:/tmp/wd4/project1/package.json)
	README.md,f(e=utama=C:/tmp/wd4/project1/README.md)
	tsconfig.json,f(e=utama=C:/tmp/wd4/project1/tsconfig.json)
	webpack.config.development.js,f(e=utama=C:/tmp/wd4/project1/webpack.config.development.js)
	webpack.config.production.js,f(e=utama=C:/tmp/wd4/project1/webpack.config.production.js)
	src,d(/mk)
		App.ts,f(e=utama=C:/tmp/wd4/project1/src/App.ts)
		index.html,f(e=utama=C:/tmp/wd4/project1/src/index.html)
		Main.tsx,f(e=utama=C:/tmp/wd4/project1/src/Main.tsx)
		assets,d(/mk)
			fonts,d(/mk)
				.gitkeep,f(e=utama=C:/tmp/wd4/project1/src/assets/fonts/.gitkeep)
			images,d(/mk)
				.gitkeep,f(e=utama=C:/tmp/wd4/project1/src/assets/images/.gitkeep)
			stylesheets,d(/mk)
				.gitkeep,f(e=utama=C:/tmp/wd4/project1/src/assets/stylesheets/.gitkeep)
				app.scss,f(e=utama=C:/tmp/wd4/project1/src/assets/stylesheets/app.scss)
			vendor,d(/mk)
				.gitkeep,f(e=utama=C:/tmp/wd4/project1/src/assets/vendor/.gitkeep)
		components,d(/mk)
			Hello.tsx,f(e=utama=C:/tmp/wd4/project1/src/components/Hello.tsx)
--#

--% C:/tmp/wd4/project1/.browserslistrc
# Browsers that we support
# Configure how you require
# https://github.com/browserslist/browserslist

last 2 versions
> 1%
IE 11

--#

--% C:/tmp/wd4/project1/.gitignore
node_modules
dist

--#

--% C:/tmp/wd4/project1/env.config.js
const path = require('path');

const outputConfig = {
    destPath: "./dist"
};

// Entry points
// https://webpack.js.org/concepts/entry-points/ 
const entryConfig = [
    "./src/App.ts",
    "./src/assets/stylesheets/app.scss",
];


// Copy files from src to dist
// https://webpack.js.org/plugins/copy-webpack-plugin/
const copyPluginPatterns = {
    patterns: [
        { from: "./src/assets/images", to: "images" },
        { from: "./src/assets/fonts", to: "fonts" },
        { from: "./src/assets/vendor", to: "js" },
    ]
};


// Dev server setup
// https://webpack.js.org/configuration/dev-server/
const devServer = {
    static: {
        directory: path.join(__dirname, outputConfig.destPath),
    },
    // https: true,
    // port: "__TEMPLATE_CLIENT_PORT",
    // host: "0.0.0.0",
    // disableHostCheck: true
};


// SCSS compile
const scssConfig = {
    destFileName: "css/app.min.css"
};


// Production terser config options
// https://webpack.js.org/plugins/terser-webpack-plugin/#terseroptions
const terserPluginConfig = {
    extractComments: false,
    terserOptions: {
        compress: {
            drop_console: true,
        },
    }
};

module.exports.copyPluginPatterns = copyPluginPatterns;
module.exports.entryConfig = entryConfig;
module.exports.scssConfig = scssConfig;
module.exports.devServer = devServer;
module.exports.terserPluginConfig = terserPluginConfig;
module.exports.outputConfig = outputConfig;

--#

--% C:/tmp/wd4/project1/package.json
{
  "name": "project1",
  "version": "1.0.0",
  "main": "index.js",
  "license": "MIT",
  "scripts": {
    "dev": "webpack serve --mode development --progress --hot --config ./webpack.config.development.js",
    "build": "webpack --mode production --config ./webpack.config.production.js"
  },
  "dependencies": {
    "@babel/cli": "^7.17.0",
    "@babel/core": "^7.17.2",
    "@babel/plugin-proposal-class-properties": "^7.16.7",
    "@babel/plugin-proposal-export-default-from": "^7.16.7",
    "@babel/plugin-proposal-export-namespace-from": "^7.16.7",
    "@babel/plugin-proposal-object-rest-spread": "^7.16.7",
    "@babel/plugin-proposal-throw-expressions": "^7.16.7",
    "@babel/plugin-syntax-dynamic-import": "^7.8.3",
    "@babel/plugin-transform-runtime": "^7.17.0",
    "@babel/preset-env": "^7.16.11",
    "@babel/preset-react": "^7.16.7",
    "@babel/preset-typescript": "^7.16.7",
    "@babel/register": "^7.17.0",
    "@pmmmwh/react-refresh-webpack-plugin": "^0.5.4",
    "@svgr/webpack": "^6.2.1",
    "@teamsupercell/typings-for-css-modules-loader": "^2.5.1",
    "@types/classnames": "^2.3.1",
    "@types/jest": "^27.4.0",
    "@types/node": "^17.0.17",
    "@types/react": "^17.0.39",
    "@types/react-dom": "^17.0.11",
    "@typescript-eslint/eslint-plugin": "^5.11.0",
    "@typescript-eslint/parser": "^5.11.0",
    "autoprefixer": "^10.4.2",
    "babel-eslint": "^10.1.0",
    "babel-loader": "^8.2.3",
    "classnames": "^2.3.1",
    "clean-webpack-plugin": "^4.0.0",
    "copy-webpack-plugin": "^10.2.4",
    "core-js": "^3.21.0",
    "cross-env": "^7.0.3",
    "css-loader": "^6.6.0",
    "css-minimizer-webpack-plugin": "^3.4.1",
    "cssnano": "^5.0.17",
    "eslint": "^8.9.0",
    "eslint-config-airbnb-base": "^15.0.0",
    "eslint-config-airbnb-typescript": "^16.1.0",
    "eslint-config-prettier": "^8.3.0",
    "eslint-import-resolver-alias": "^1.1.2",
    "eslint-import-resolver-webpack": "^0.13.2",
    "eslint-plugin-import": "^2.25.4",
    "eslint-plugin-jsx-a11y": "^6.5.1",
    "eslint-plugin-prettier": "^4.0.0",
    "eslint-plugin-react": "^7.28.0",
    "eslint-plugin-react-hooks": "^4.3.0",
    "eslint-webpack-plugin": "^3.1.1",
    "express": "^4.17.2",
    "file-loader": "^6.2.0",
    "fork-ts-checker-webpack-plugin": "^7.2.1",
    "html-loader": "^3.1.0",
    "html-webpack-plugin": "^5.5.0",
    "image-webpack-loader": "^8.1.0",
    "import-sort-style-module-and-prefix": "^0.1.3",
    "jest": "^27.5.1",
    "less": "^4.1.2",
    "less-loader": "^10.2.0",
    "mini-css-extract-plugin": "^2.5.3",
    "node-sass": "^7.0.1",
    "normalize.css": "^8.0.1",
    "path": "^0.12.7",
    "postcss": "^8.4.6",
    "postcss-loader": "^6.2.1",
    "postcss-preset-env": "^7.3.2",
    "prettier": "^2.5.1",
    "prettier-plugin-import-sort": "^0.0.7",
    "pretty-quick": "^3.1.3",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-hot-loader": "^4.13.0",
    "react-refresh": "^0.11.0",
    "regenerator-runtime": "^0.13.9",
    "resolve-url-loader": "^5.0.0",
    "rimraf": "^3.0.2",
    "sass": "^1.49.7",
    "sass-loader": "^12.4.0",
    "sass-resources-loader": "^2.2.4",
    "simple-git-hooks": "^2.7.0",
    "style-loader": "^3.3.1",
    "svg-url-loader": "^7.1.1",
    "terser-webpack-plugin": "^5.3.1",
    "ts-loader": "^9.2.6",
    "typescript": "^4.5.5",
    "url-loader": "^4.1.1",
    "webpack": "^5.68.0",
    "webpack-bundle-analyzer": "^4.5.0",
    "webpack-cli": "^4.9.2",
    "webpack-dev-server": "^4.7.4",
    "webpack-merge": "^5.8.0"
  }
}


--#

--% C:/tmp/wd4/project1/README.md
![logo](https://user-images.githubusercontent.com/6104940/107880275-b04f2b80-6ed5-11eb-9852-de05425070cc.png)

# React TypeScript Webpack Starter

A starter project for using React, TypeScript, SCSS and Webpack.

## Features
- Webpack 5 + HMR
- TypeScript + React
- SCSS + Autoprefixing 

## 🚀 Getting Started

Get up and running with these simple steps:

1. Clone the project
2. Run `npm install`
3. Run `npm run dev`


## Class & Functional stubs
In the `master` branch you can find the class based starter. In the branch `functional` you can find the functional based starter.


## Configuration
Optional configuration for the project can be done in the following files below.

Open [env.config.js](/env.config.js) and you will see the default configuration for the project.


| Config      | Description |
| ----------- | ----------- |
| `.browerslistrc`      | Open [.browserslist](/.browserslist) to configure Browser support for TypeScript + SCSS compiliation. [Read more here about Browerslist](https://github.com/browserslist/browserslist). Defaults are set for last 2 versions, > 1% and IE 11.   |
| `outputConfig.destPath` | The folder in which you want your app to compile to. By default this is `dist`.               |
| `entryConfig` | Webpack Entry points, by default this will look for the TypeScript + SCSS entry point files.  More info on [Entry points here](https://webpack.js.org/concepts/entry-points/ )               |
| `copyPluginPatterns.patterns` | Configure folders you want copied over when compiling your app. Useful to copy over entire folder structures of images or fonts. |
| `devServer` | Configure the Webpack development server. Enable `https`, specify a particular `port`, or `host`. [More information on these options here](https://webpack.js.org/configuration/dev-server/)
| `scssConfig.destFileName` | Specify the output for your css. E.g `css/app.css`
| `terserPluginConfig` | Full [Terser config can be found here](https://webpack.js.org/plugins/terser-webpack-plugin/#terseroptions).


## Images, Fonts and output 

Here's an example of the default generated output to our `dist` folder.
```
- index.html
-- js
-- css
-- fonts
---- some-font-file.woff
-- images
---- path-to-example-image.jpg
```

- By default, fonts and images are copied to the `dist` folder.
- To include a reference to an image or font, it should be relative to where your css would output.

For example: 

`stylesheets/some-folder/some-file-somewhere.scss`
```css
.example {
    background-image: url("../images/path-to-image-example.jpg");
}

@font-face {
    font-family: "Example-font";
    src: url("../fonts/some-font-file.woff");
}
``` 

Would output to the folder `css/app.css` 

```
- index.html
-- js
-- css
---- app.css
-- fonts
---- some-font-file.woff
-- images
---- path-to-example-image.jpg
```


## Development

```shell
npm install
npm run dev
```

## Production
Note: This will compile to a `dist` folder.
```shell
npm run build
```




### Build tools

* [React](https://reactjs.org/) - JavaScript library for building user interfaces.
* [TypeScript](https://www.typescriptlang.org) - TypeScript is a superset of JavaScript that compiles to clean JavaScript.
* [Webpack 5](https://webpack.js.org/) - App bundler for JavaScript.
* [SCSS](https://sass-lang.com/) - Preprocessor for SCSS to CSS.


### 📝License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

--#

--% C:/tmp/wd4/project1/tsconfig.json
{
  "compilerOptions": {
    /* Visit https://aka.ms/tsconfig.json to read more about this file */
    /* Basic Options */
    // "incremental": true,                   /* Enable incremental compilation */
    "target": "es6", /* Specify ECMAScript target version: 'ES3' (default), 'ES5', 'ES2015', 'ES2016', 'ES2017', 'ES2018', 'ES2019', 'ES2020', or 'ESNEXT'. */
    "module": "es2015", /* Specify module code generation: 'none', 'commonjs', 'amd', 'system', 'umd', 'es2015', 'es2020', or 'ESNext'. */
    // "lib": [],                             /* Specify library files to be included in the compilation. */
    // "allowJs": true,                       /* Allow javascript files to be compiled. */
    // "checkJs": true,                       /* Report errors in .js files. */
    "jsx": "react", /* Specify JSX code generation: 'preserve', 'react-native', or 'react'. */
    // "declaration": true,                   /* Generates corresponding '.d.ts' file. */
    // "declarationMap": true,                /* Generates a sourcemap for each corresponding '.d.ts' file. */
    // "sourceMap": true,                     /* Generates corresponding '.map' file. */
    // "outFile": "./",                       /* Concatenate and emit output to single file. */
    // "outDir": "./",                        /* Redirect output structure to the directory. */
    // "rootDir": "./",                       /* Specify the root directory of input files. Use to control the output directory structure with --outDir. */
    // "composite": true,                     /* Enable project compilation */
    // "tsBuildInfoFile": "./",               /* Specify file to store incremental compilation information */
    // "removeComments": true,                /* Do not emit comments to output. */
    // "noEmit": true,                        /* Do not emit outputs. */
    // "importHelpers": true,                 /* Import emit helpers from 'tslib'. */
    // "downlevelIteration": true,            /* Provide full support for iterables in 'for-of', spread, and destructuring when targeting 'ES5' or 'ES3'. */
    // "isolatedModules": true,               /* Transpile each file as a separate module (similar to 'ts.transpileModule'). */
    /* Strict Type-Checking Options */
    "strict": true, /* Enable all strict type-checking options. */
    // "noImplicitAny": true,                 /* Raise error on expressions and declarations with an implied 'any' type. */
    // "strictNullChecks": true,              /* Enable strict null checks. */
    // "strictFunctionTypes": true,           /* Enable strict checking of function types. */
    // "strictBindCallApply": true,           /* Enable strict 'bind', 'call', and 'apply' methods on functions. */
    // "strictPropertyInitialization": true,  /* Enable strict checking of property initialization in classes. */
    // "noImplicitThis": true,                /* Raise error on 'this' expressions with an implied 'any' type. */
    // "alwaysStrict": true,                  /* Parse in strict mode and emit "use strict" for each source file. */
    /* Additional Checks */
    // "noUnusedLocals": true,                /* Report errors on unused locals. */
    // "noUnusedParameters": true,            /* Report errors on unused parameters. */
    // "noImplicitReturns": true,             /* Report error when not all code paths in function return a value. */
    // "noFallthroughCasesInSwitch": true,    /* Report errors for fallthrough cases in switch statement. */
    // "noUncheckedIndexedAccess": true,      /* Include 'undefined' in index signature results */
    /* Module Resolution Options */
    // "moduleResolution": "node",            /* Specify module resolution strategy: 'node' (Node.js) or 'classic' (TypeScript pre-1.6). */
    // "baseUrl": "./",                       /* Base directory to resolve non-absolute module names. */
    // "paths": {},                           /* A series of entries which re-map imports to lookup locations relative to the 'baseUrl'. */
    // "rootDirs": [],                        /* List of root folders whose combined content represents the structure of the project at runtime. */
    // "typeRoots": [],                       /* List of folders to include type definitions from. */
    // "types": [],                           /* Type declaration files to be included in compilation. */
    // "allowSyntheticDefaultImports": true,  /* Allow default imports from modules with no default export. This does not affect code emit, just typechecking. */
    "esModuleInterop": true, /* Enables emit interoperability between CommonJS and ES Modules via creation of namespace objects for all imports. Implies 'allowSyntheticDefaultImports'. */
    // "preserveSymlinks": true,              /* Do not resolve the real path of symlinks. */
    // "allowUmdGlobalAccess": true,          /* Allow accessing UMD globals from modules. */
    /* Source Map Options */
    // "sourceRoot": "",                      /* Specify the location where debugger should locate TypeScript files instead of source locations. */
    // "mapRoot": "",                         /* Specify the location where debugger should locate map files instead of generated locations. */
    // "inlineSourceMap": true,               /* Emit a single file with source maps instead of having a separate file. */
    // "inlineSources": true,                 /* Emit the source alongside the sourcemaps within a single file; requires '--inlineSourceMap' or '--sourceMap' to be set. */
    /* Experimental Options */
    // "experimentalDecorators": true,        /* Enables experimental support for ES7 decorators. */
    // "emitDecoratorMetadata": true,         /* Enables experimental support for emitting type metadata for decorators. */
    /* Advanced Options */
    "skipLibCheck": true, /* Skip type checking of declaration files. */
    "forceConsistentCasingInFileNames": true /* Disallow inconsistently-cased references to the same file. */
  }
}

--#

--% C:/tmp/wd4/project1/webpack.config.development.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyPlugin = require('copy-webpack-plugin');
const { outputConfig, copyPluginPatterns, entryConfig, devServer } = require("./env.config");

module.exports = (env, options) => 
{
    return {
        mode: options.mode,
        entry: entryConfig,
        devServer,
        // Dev only
        // Target must be set to web for hmr to work with .browserlist
        // https://github.com/webpack/webpack-dev-server/issues/2758#issuecomment-710086019
        target: "web",
        module: {
            rules: [
                {
                    test: /\.tsx?$/,
                    use: "ts-loader",
                    exclude: /node_modules/,
                },
                {
                    test: /\.scss$/,
                    use: [
                        // We're in dev and want HMR, SCSS is handled in JS
                        // In production, we want our css as files
                        "style-loader",
                        "css-loader",
                        {
                            loader: "postcss-loader",
                            options: {
                                postcssOptions: {
                                    plugins: [
                                        ["postcss-preset-env"],
                                    ],
                                },
                            },
                        },
                        "sass-loader"
                    ],
                },
                {
                    test: /\.(?:ico|gif|png|jpg|jpeg|svg)$/i,
                    type: "javascript/auto",
                    loader: "file-loader",
                    options: {
                        publicPath: "../",
                        name: "[path][name].[ext]",
                        context: path.resolve(__dirname, "src/assets"),
                        emitFile: false,
                    },
                },
                {
                    test: /\.(woff(2)?|eot|ttf|otf|svg|)$/,
                    type: "javascript/auto",
                    exclude: /images/,
                    loader: "file-loader",
                    options: {
                        publicPath: "../",
                        context: path.resolve(__dirname, "src/assets"),
                        name: "[path][name].[ext]",
                        emitFile: false,
                    },
                },
            ],
        },
        resolve: { extensions: [".tsx", ".ts", ".js"] },
        output: {
            filename: "js/[name].bundle.js",
            path: path.resolve(__dirname, outputConfig.destPath),
            publicPath: "",
        },
        plugins: [
            new HtmlWebpackPlugin({
                template: "./src/index.html",
                inject: true,
                minify: false
            }),
            new CopyPlugin(copyPluginPatterns),
        ]
    };
};

--#

--% C:/tmp/wd4/project1/webpack.config.production.js
const path = require("path");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const CopyPlugin = require("copy-webpack-plugin");
const TerserPlugin = require("terser-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const { outputConfig, copyPluginPatterns, scssConfig, entryConfig, terserPluginConfig } = require("./env.config");

module.exports = (env, options) => 
{
    return {
        mode: options.mode,
        entry: entryConfig,
        module: {
            rules: [
                {
                    test: /\.tsx?$/,
                    use: "ts-loader",
                    exclude: /node_modules/,
                },
                {
                    test: /\.scss$/,
                    use: [
                        MiniCssExtractPlugin.loader,
                        "css-loader",
                        {
                            loader: "postcss-loader",
                            options: {
                                postcssOptions: {
                                    plugins: [
                                        ["postcss-preset-env"],
                                    ],
                                },
                            },
                        },
                        "sass-loader"
                    ],
                },
                {
                    test: /\.(?:ico|gif|png|jpg|jpeg|svg)$/i,
                    type: "javascript/auto",
                    loader: "file-loader",
                    options: {
                        publicPath: "../",
                        name: "[path][name].[ext]",
                        context: path.resolve(__dirname, "src/assets"),
                        emitFile: false,
                    },
                },
                {
                    test: /\.(woff(2)?|eot|ttf|otf|svg|)$/,
                    type: "javascript/auto",
                    exclude: /images/,
                    loader: "file-loader",
                    options: {
                        publicPath: "../",
                        context: path.resolve(__dirname, "src/assets"),
                        name: "[path][name].[ext]",
                        emitFile: false,
                    },
                },
            ],
        },
        resolve: { extensions: [".tsx", ".ts", ".js"] },
        output: {
            filename: "js/[name].bundle.js",
            path: path.resolve(__dirname, outputConfig.destPath),
            publicPath: "",
        },
        optimization: {
            minimizer: [
                new TerserPlugin(terserPluginConfig)
            ],
            splitChunks: {
                chunks: "all",
            },
        },
        plugins: [
            new CleanWebpackPlugin(),
            new CopyPlugin(copyPluginPatterns),
            new MiniCssExtractPlugin({ filename: scssConfig.destFileName }),
            new HtmlWebpackPlugin({
                template: "./src/index.html",
                inject: true,
                minify: false
            }),
        ]
    };
};

--#

--% C:/tmp/wd4/project1/src/App.ts
import { createElement } from "react";
import ReactDOM from "react-dom";
import { Main } from "./Main";

export class App
{
    constructor()
    {
        this.render();
    }

    public static addTwoNumbers(num1: number, num2: number): number
    {
        return num1 + num2;
    }

    private render(): void
    {
        ReactDOM.render(createElement(Main, { app: this }), document.getElementById("app") || document.createElement("div"));
    }
}

new App();

--#

--% C:/tmp/wd4/project1/src/index.html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>App</title>
</head>

<body>
    <div id="app"></div>
</body>

</html>

--#

--% C:/tmp/wd4/project1/src/Main.tsx
import React, { Component } from "react";
import { App } from "./App";
import { Hello } from "./components/Hello";

export interface MainProps
{
    app: App;
}

export class Main extends Component<MainProps, {}>
{
    constructor(props: MainProps)
    {
        super(props);
    }

    public render(): JSX.Element
    {
        return (
            <>
                <Hello message="React TypeScript Webpack Starter">
                    <div className="features">
                        <div>Webpack 5 + HMR</div>
                        <div>TypeScript + React</div>
                        <div>SCSS + Autoprefixing</div>
                    </div>
                </Hello>
            </>
        );
    }
}

--#

--% C:/tmp/wd4/project1/src/assets/fonts/.gitkeep


--#

--% C:/tmp/wd4/project1/src/assets/images/.gitkeep


--#

--% C:/tmp/wd4/project1/src/assets/stylesheets/.gitkeep


--#

--% C:/tmp/wd4/project1/src/assets/stylesheets/app.scss
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap');

:root
{
    --color-example: #fff;
}

html,body 
{
    font-family: "Roboto", sans-serif;
    display: flex;
    flex-grow: 1;
    width: 100%;
    height: 100%;
    min-height: 100vh;
    font-size: 16px;
    text-align: center;
    color: var(--color-example);
    margin: 0;
}

#app 
{
    background-color: #4158D0;
    background-image: linear-gradient(43deg, #4158D0 0%, #C850C0 46%, #FFCC70 100%);
    color: var(--color-example);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-grow: 1;
    font-size: 2rem;
}


.features 
{
    font-size: 1.7rem;

    & div 
    {
        padding: 0.5rem;
    }
}

--#

--% C:/tmp/wd4/project1/src/assets/vendor/.gitkeep


--#

--% C:/tmp/wd4/project1/src/components/Hello.tsx
import React, { Component } from "react";

export interface HelloProps
{
    message: string;
}
export class Hello extends Component<HelloProps, {}>
{
    public render(): JSX.Element
    {
        return (
            <div className="hello">
                <h1>{this.props.message}</h1>
                <div>
                    {this.props.children}
                </div>
            </div>
        );
    }
}
--#
