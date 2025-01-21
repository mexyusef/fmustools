--% index/fmus
--#

--% /react-light/public/manifest.json
{
  "short_name": "FL",
  "name": "Fulgent Light",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#000000",
  "background_color": "#ffffff"
}
--#

--% /react-light/public/index.html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta
      name="viewport"
      content="width=device-width, initial-scale=1, shrink-to-fit=no"
    />
    <meta name="theme-color" content="#000000" />
    <!--
			manifest.json provides metadata used when your web app is added to the
			homescreen on Android. See https://developers.google.com/web/fundamentals/engage-and-retain/web-app-manifest/
			-->
    <link rel="manifest" href="%PUBLIC_URL%/manifest.json" />
    <link rel="shortcut icon" href="%PUBLIC_URL%/favicon.ico" />
    <link
      rel="apple-touch-icon"
      sizes="76x76"
      href="%PUBLIC_URL%/apple-icon.png"
    />

    <!--
			Notice the use of %PUBLIC_URL% in the tags above.
			It will be replaced with the URL of the `public` folder during the build.
			Only files inside the `public` folder can be referenced from the HTML.

			Unlike "/favicon.ico" or "favicon.ico", "%PUBLIC_URL%/favicon.ico" will
			work correctly both with client-side routing and a non-root public URL.
			Learn how to configure a non-root public URL by running `npm run build`.
			-->
    <title>Frontend - Light</title>
    <link
      href="https://fonts.googleapis.com/css?family=Montserrat:400,700,200"
      rel="stylesheet"
    />
  </head>
  <body>
    <noscript> You need to enable JavaScript to run this app. </noscript>
    <div id="root"></div>
    <!--
			This HTML file is a template.
			If you open it directly in the browser, you will see an empty page.

			You can add webfonts, meta tags, or analytics to this file.
			The build step will place the bundled scripts into the <body> tag.

			To begin the development, run `npm start` or `yarn start`.
			To create a production bundle, use `npm run build` or `yarn build`.
			-->
  </body>
</html>
--#

--% /react-light/public/apple-icon.png
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
--#

--% /react-light/public/favicon.ico
AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAABMLAAATCwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwBAQFNAQEBOQAAABEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAARAQEBOQEBAU0AAAAMAAAAAAAAAAAAAAA2AAAA7gAAAPIAAADJAAAAcQEBARUAAAAAAAAAAAEBARUAAABxAAAAyQAAAPIAAADuAAAANgAAAAAAAAAAAAAAVQAAAPwAAAD/AAAA/wAAAP0AAAC4AAAAVwAAAFcAAAC4AAAA/QAAAP8AAAD/AAAA/AAAAFUAAAAAAAAAAAAAAG8AAAD/AAAA/wAAAP8AAAD/AAAA/wAAAP4AAAD+AAAA/wAAAP8AAAD/AAAA/wAAAP8AAABvAAAAAAAAAAAAAAB5AAAA/wAAAP8AAAD/AAAA/wAAAPgAAADiAAAA4gAAAPgAAAD/AAAA/wAAAP8AAAD/AAAAeQAAAAAAAAAAAAAAWQAAAPwAAAD/AAAA/wAAAOMAAAByAAAAIAAAACAAAAByAAAA4wAAAP8AAAD/AAAA/AAAAFkAAAAAAAAAAAAAACYAAADKAAAAuQAAAHcAAAArAAAAAgAAAAAAAAAAAAAAAgAAACsAAAB3AAAAuQAAAMoAAAAmAAAAAAAAAAAAAAAEAAAAGgAAAAkAAAAAAwMDAAAAAAAAAAAAAAAAAAAAAAADAwMAAAAAAAAAAAkAAAAaAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA//8AAP//AAD//wAA//8AAIPBAACBgQAAgAEAAIABAACAAQAAgAEAAIGBAACP8QAA//8AAP//AAD//wAA//8AAA==
--#


--% /react-light/README.md
# [Light Bootstrap Dashboard React](https://demos.creative-tim.com/light-bootstrap-dashboard-react/#/?ref=lbdr-readme) [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&logo=twitter)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fcreativetimofficial.github.io%2Flight-bootstrap-dashboard-react&text=Light%20Bootstrap%20Dashboard%20React%20-%20Free%20Bootstrap%20Admin%20Template&original_referer=https%3A%2F%2Fdemos.creative-tim.com%2Flight-bootstrap-dashboard-react%2F&via=creativetim&hashtags=react%2Cbootstrap%2Creact-bootstrap%2Ccreativetim%2Ccreative-tim)

![version](https://img.shields.io/badge/version-2.0.0-blue.svg) ![license](https://img.shields.io/badge/license-MIT-blue.svg) [![GitHub issues open](https://img.shields.io/github/issues/creativetimofficial/light-bootstrap-dashboard-react.svg?maxAge=2592000)]() [![GitHub issues closed](https://img.shields.io/github/issues-closed-raw/creativetimofficial/light-bootstrap-dashboard-react.svg?maxAge=2592000)]()  [![Chat](https://img.shields.io/badge/chat-on%20discord-7289da.svg)](https://discord.gg/E4aHAQy)

![Product Gif](https://raw.githubusercontent.com/creativetimofficial/public-assets/master/light-bootstrap-dashboard-react/light-bootstrap-dashboard-react.gif)


**[Light Bootstrap Dashboard React](https://demos.creative-tim.com/light-bootstrap-dashboard-react/#/?ref=lbdr-readme)** is an admin dashboard template designed to be beautiful and simple. It is built on top of [React Bootstrap](https://5c507d49471426000887a6a7--react-bootstrap.netlify.com/), using [Light Bootstrap Dashboard](https://www.creative-tim.com/product/light-bootstrap?ref=lbdr-readme) and it is fully responsive. It comes with a big collections of elements that will offer you multiple possibilities to create the app that best fits your needs. It can be used to create admin panels, project management systems, web applications backend, CMS or CRM.

The product represents a big suite of front-end developer tools that can help you jump start your project. We have created it thinking about things you actually need in a dashboard. Light Bootstrap Dashboard React contains multiple handpicked and optimized plugins. Everything is designed to fit with one another. As you will be able to see, the dashboard you can access on Creative Tim is a customization of this product.

It comes with 6 filter colors for the sidebar (`black`, `azure`,`green`,`orange`,`red`,`purple`) and an option to have a background image.

## Table of Contents

* [Versions](#versions)
* [Demo](#demo)
* [Quick Start](#quick-start)
* [Documentation](#documentation)
* [File Structure](#file-structure)
* [Browser Support](#browser-support)
* [Resources](#resources)
* [Reporting Issues](#reporting-issues)
* [Technical Support or Questions](#technical-support-or-questions)
* [Licensing](#licensing)
* [Useful Links](#useful-links)


## Versions

[<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/html-logo.jpg" width="60" height="60" />](https://www.creative-tim.com/product/light-bootstrap-dashboard?ref=lbdr-readme)[<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/react-logo.jpg" width="60" height="60" />](https://www.creative-tim.com/product/light-bootstrap-dashboard-react?ref=lbdr-readme)[<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/vue-logo.jpg" width="60" height="60" />](https://www.creative-tim.com/product/vue-light-bootstrap-dashboard?ref=lbdr-readme)[<img src="https://raw.githubusercontent.com/creativetimofficial/public-assets/master/logos/angular-logo.jpg" width="60" height="60" />](https://www.creative-tim.com/product/light-bootstrap-dashboard-angular2?ref=lbdr-readme)


| HTML | React | Vue | Angular |
| --- | --- | --- | --- |
| [![Light Bootstrap Dashboard HTML](https://github.com/creativetimofficial/public-assets/blob/master/light-bootstrap-dashboard/light-bootstrap-dashboard.jpg?raw=true)](https://www.creative-tim.com/product/light-bootstrap-dashboard?ref=lbdr-readme) | [![Light Bootstrap Dashboard React](https://github.com/creativetimofficial/public-assets/blob/master/light-bootstrap-dashboard-react/light-bootstrap-dashboard-react.jpg?raw=true)](https://www.creative-tim.com/product/light-bootstrap-dashboard-react?ref=lbdr-readme) | [![Vue Light Bootstrap Dashboard](https://github.com/creativetimofficial/public-assets/blob/master/vue-light-bootstrap-dashboard/vue-light-bootstrap-dashboard.jpg?raw=true)](https://www.creative-tim.com/product/vue-light-bootstrap-dashboard?ref=lbdr-readme) | [![Light Bootstrap Dashboard Angular](https://github.com/creativetimofficial/public-assets/blob/master/light-bootstrap-dashboard-angular/light-bootstrap-dashboard-angular.jpg?raw=true)](https://www.creative-tim.com/product/light-bootstrap-dashboard-angular2?ref=lbdr-readme) |

## Demo

| Dashboard | User Profile | Tables | Maps |
| --- | --- | --- | --- | --- |
| [![Start page](https://raw.githubusercontent.com/creativetimofficial/public-assets/master/light-bootstrap-dashboard-react/dashboard-page.png)](https://demos.creative-tim.com/light-bootstrap-dashboard-react/#/admin/dashboard?ref=lbdr-readme) | [![User profile page](https://raw.githubusercontent.com/creativetimofficial/public-assets/master/light-bootstrap-dashboard-react/user-page.png)](https://demos.creative-tim.com/light-bootstrap-dashboard-react/#/admin/user-page?ref=lbdr-readme) | [![Tables page ](https://raw.githubusercontent.com/creativetimofficial/public-assets/master/light-bootstrap-dashboard-react/tables-page.png)](https://demos.creative-tim.com/light-bootstrap-dashboard-react/#/admin/table-list?ref=lbdr-readme) | [![Notifications Page](https://raw.githubusercontent.com/creativetimofficial/public-assets/master/light-bootstrap-dashboard-react/notifications-page.png)](https://demos.creative-tim.com/light-bootstrap-dashboard-react/#/admin/notifications?ref=lbdr-readme) |

[View More](https://demos.creative-tim.com/light-bootstrap-dashboard-react/#/admin/dashboard?ref=lbdr-readme).


## Quick start

Quick start options:

- Clone the repo: `git clone https://github.com/creativetimofficial/light-bootstrap-dashboard-react.git`.
- [Download from Github](https://github.com/creativetimofficial/light-bootstrap-dashboard-react/archive/master.zip).
- [Download from Creative Tim](https://www.creative-tim.com/product/light-bootstrap-dashboard-react?ref=lbdr-readme).


## Documentation
The documentation for the Light Bootstrap Dashboard React is hosted at our [website](https://demos.creative-tim.com/light-bootstrap-dashboard-react/#/documentation/?ref=lbdr-readme).


## File Structure

Within the download you'll find the following directories and files:

```
light-bootstrap-dashboard-react
.
├── CHANGELOG.md
├── ISSUE_TEMPLATE.md
├── LICENSE.md
├── README.md
├── gulpfile.js
├── jsconfig.json
├── package.json
├── Documentation
│   ├── css
│   │   ├── demo.css
│   │   ├── documentation.css
│   │   └── light-bootstrap-dashboard.css
│   ├── img
│   └── tutorial-components.html
├── public
│   ├── favicon.ico
│   ├── index.html
│   └── manifest.json
└── src
    ├── index.js
    ├── logo.svg
    ├── routes.js
    ├── assets
    │   ├── css
    │   │   ├── animate.min.css
    │   │   ├── demo.css
    │   │   ├── light-bootstrap-dashboard-react.css
    │   │   ├── light-bootstrap-dashboard-react.css.map
    │   │   └── light-bootstrap-dashboard-react.min.css
    │   ├── fonts
    │   │   ├── nucleo-icons.eot
    │   │   ├── nucleo-icons.svg
    │   │   ├── nucleo-icons.ttf
    │   │   ├── nucleo-icons.woff
    │   │   └── nucleo-icons.woff2
    │   ├── img
    │   │   └── faces
    │   └── scss
    │       ├── lbd
    │       │   ├── mixins
    │       │   └── plugins
    │       ├── lbdr
    │       │   ├── plugins
    │       │   └── react-differences.scss
    │       └── light-bootstrap-dashboard-react.scss
    ├── layouts
    │   └── Admin.js
    ├── components
    │   ├── FixedPlugin
    │   │   └── FixedPlugin.js
    │   ├── Footer
    │   │   └── Footer.js
    │   ├── Navbars
    │   │   └── AdminNavbar.js
    │   └── Sidebar
    │       └── Sidebar.js
    └── views
        ├── Dashboard.js
        ├── Icons.js
        ├── Maps.js
        ├── Notifications.js
        ├── TableList.js
        ├── Typography.js
        ├── Upgrade.js
        └── UserProfile.js
```

## Browser Support

At present, we officially aim to support the last two versions of the following browsers:

<img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/chrome.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/firefox.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/edge.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/safari.png" width="64" height="64"> <img src="https://s3.amazonaws.com/creativetim_bucket/github/browser/opera.png" width="64" height="64">


## Resources
- Demo: https://demos.creative-tim.com/light-bootstrap-dashboard-react/#/admin/dashboard?ref=lbdr-readme
- Download Page: https://www.creative-tim.com/product/light-bootstrap-dashboard-react?ref=lbdr-readme
- Documentation: https://demos.creative-tim.com/light-bootstrap-dashboard-react/#/documentation/tutorial?ref=lbdr-readme
- License Agreement: https://www.creative-tim.com/license?ref=lbdr-readme
- Support: https://www.creative-tim.com/contact-us?ref=lbdr-readme
- Issues: [Github Issues Page](https://github.com/creativetimofficial/light-bootstrap-dashboard-react/issues)

## Reporting Issues
We use GitHub Issues as the official bug tracker for the Light Bootstrap Dashboard React. Here are some advices for our users that want to report an issue:

1. Make sure that you are using the latest version of the Light Bootstrap Dashboard React. Check the CHANGELOG from your dashboard on our [website](https://www.creative-tim.com/?ref=lbdr-readme).
2. Providing us reproducible steps for the issue will shorten the time it takes for it to be fixed.
3. Some issues may be browser specific, so specifying in what browser you encountered the issue might help.

## Technical Support or Questions

If you have questions or need help integrating the product please [contact us](https://www.creative-tim.com/contact-us?ref=lbdr-readme) instead of opening an issue.

## Licensing

- Copyright 2018 Creative Tim (https://www.creative-tim.com?ref=lbdr-readme)
- Licensed under MIT (https://github.com/creativetimofficial/light-bootstrap-dashboard-react/blob/master/LICENSE.md)

## Useful Links

More products from Creative Tim: <https://www.creative-tim.com/products?ref=lbdr-readme>

Tutorials: <https://www.youtube.com/channel/UCVyTG4sCw-rOvB9oHkzZD1w>

Freebies: <https://www.creative-tim.com/products?ref=lbdr-readme>

Affiliate Program (earn money): <https://www.creative-tim.com/affiliates/new?ref=lbdr-readme>

Social Media:

Twitter: <https://twitter.com/CreativeTim>

Facebook: <https://www.facebook.com/CreativeTim>

Dribbble: <https://dribbble.com/creativetim>

Google+: <https://plus.google.com/+CreativetimPage>

Instagram: <https://instagram.com/creativetimofficial>
--#


--% /react-light/gulpfile.js
const gulp = require("gulp");
const gap = require("gulp-append-prepend");

gulp.task("licenses", async function () {
  // this is to add Creative Tim licenses in the production mode for the minified js
  gulp
    .src("build/static/js/*chunk.js", { base: "./" })
    .pipe(
      gap.prependText(`/*!

=========================================================
* Light Bootstrap Dashboard React - v2.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/light-bootstrap-dashboard-react
* Copyright 2020 Creative Tim (https://www.creative-tim.com)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/`)
    )
    .pipe(gulp.dest("./", { overwrite: true }));

  // this is to add Creative Tim licenses in the production mode for the minified html
  gulp
    .src("build/index.html", { base: "./" })
    .pipe(
      gap.prependText(`<!--

=========================================================
* Light Bootstrap Dashboard React - v2.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/light-bootstrap-dashboard-react
* Copyright 2020 Creative Tim (https://www.creative-tim.com)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

-->`)
    )
    .pipe(gulp.dest("./", { overwrite: true }));

  // this is to add Creative Tim licenses in the production mode for the minified css
  gulp
    .src("build/static/css/*chunk.css", { base: "./" })
    .pipe(
      gap.prependText(`/*!

=========================================================
* Light Bootstrap Dashboard React - v2.0.0
=========================================================

* Product Page: https://www.creative-tim.com/product/light-bootstrap-dashboard-react
* Copyright 2020 Creative Tim (https://www.creative-tim.com)

* Coded by Creative Tim

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/`)
    )
    .pipe(gulp.dest("./", { overwrite: true }));
  return;
});


--#
