--% index/fmus
gingonic_simple,d(/mk)
	%utama=__FILE__
	.gitignore,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/.gitignore)
	.travis.yml,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/.travis.yml)
	BACKEND_INSTRUCTIONS.md,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/BACKEND_INSTRUCTIONS.md)
	doc.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/doc.go)
	FRONTEND_INSTRUCTIONS.md,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/FRONTEND_INSTRUCTIONS.md)
	go.mod,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/go.mod)
	go.mod-generated_by_mod_init,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/go.mod-generated_by_mod_init)
	go.sum,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/go.sum)
	gorm.db,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/gorm.db)
	hello.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/hello.go)
	LICENSE,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/LICENSE)
	logo.png,f(b64=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/logo.png)
	MOBILE_INSTRUCTIONS.md,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/MOBILE_INSTRUCTIONS.md)
	readme.md,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/readme.md)
	articles,d(/mk)
		doc.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/articles/doc.go)
		models.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/articles/models.go)
		routers.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/articles/routers.go)
		serializers.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/articles/serializers.go)
		validators.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/articles/validators.go)
	common,d(/mk)
		database.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/common/database.go)
		unit_test.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/common/unit_test.go)
		utils.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/common/utils.go)
	scripts,d(/mk)
		coverage.sh,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/scripts/coverage.sh)
		gofmt.sh,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/scripts/gofmt.sh)
	users,d(/mk)
		doc.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/doc.go)
		middlewares.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/middlewares.go)
		models.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/models.go)
		routers.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/routers.go)
		serializers.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/serializers.go)
		unit_test.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/unit_test.go)
		validators.go,f(e=utama=/tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/validators.go)
--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/.gitignore
# See http://help.github.com/ignore-files/ for more about ignoring files.

# dependencies
/node_modules
/bower_components

# IDEs and editors
/.idea
.project
.classpath
*.launch
.settings/


#System Files
.DS_Store
Thumbs.db

vendor/*
!vendor/vendor.json

tmp/*
gorm.db
coverage.txt

bak.*

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/.travis.yml
language: go

go:
  - 1.7
  - 1.8.x
  - master

go_import_path: github.com/gothinkster/golang-gin-realworld-example-app

services:
  - sqlite3

install:
  - go get -u github.com/gothinkster/golang-gin-realworld-example-app
  - go get -u github.com/kardianos/govendor
  - govendor sync
script:
#  - go test -v ./...
  - bash ./scripts/gofmt.sh
  - bash ./scripts/coverage.sh

after_success:
  - bash <(curl -s https://codecov.io/bash)

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/BACKEND_INSTRUCTIONS.md
> *Note: Delete this file before publishing your app!*

# [Backend API spec](https://github.com/gothinkster/realworld/tree/master/api)

For your convenience, we have a [Postman collection](https://github.com/gothinkster/realworld/blob/master/api/Conduit.postman_collection.json) that you can use to test your API endpoints as you build your app.

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/doc.go
/*
Golang Gonic/Gin startup project fork form RealWorld https://realworld.io

You can find all the spec and front end demo in the Realworld project

This project will include objects and relationships' CRUD, you will know how to write a golang/gin app though small perfectly formed.
*/
package main

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/FRONTEND_INSTRUCTIONS.md
> *Note: Delete this file before publishing your app!*

### Using the hosted API

Simply point your [API requests](https://github.com/gothinkster/realworld/tree/master/api) to `https://conduit.productionready.io/api` and you're good to go!

### Routing Guidelines

- Home page (URL: /#/ )
    - List of tags
    - List of articles pulled from either Feed, Global, or by Tag
    - Pagination for list of articles
- Sign in/Sign up pages (URL: /#/login, /#/register )
    - Uses JWT (store the token in localStorage)
    - Authentication can be easily switched to session/cookie based
- Settings page (URL: /#/settings )
- Editor page to create/edit articles (URL: /#/editor, /#/editor/article-slug-here )
- Article page (URL: /#/article/article-slug-here )
    - Delete article button (only shown to article's author)
    - Render markdown from server client side
    - Comments section at bottom of page
    - Delete comment button (only shown to comment's author)
- Profile page (URL: /#/profile/:username, /#/profile/:username/favorites )
    - Show basic user info
    - List of articles populated from author's created articles or author's favorited articles

# Styles

Instead of having the Bootstrap theme included locally, we recommend loading the precompiled theme from our CDN (our [header template](#header) does this by default):

```html
<link rel="stylesheet" href="//demo.productionready.io/main.css">
```

Alternatively, if you want to make modifications to the theme, check out the [theme's repo](https://github.com/gothinkster/conduit-bootstrap-template).


# Templates

- [Layout](#layout)
  - [Header](#header)
  - [Footer](#footer)
- [Pages](#pages)
  - [Home](#home)
  - [Login/Register](#loginregister)
  - [Profile](#profile)
  - [Settings](#settings)
  - [Create/Edit Article](#createedit-article)
  - [Article](#article)
  

## Layout


### Header

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Conduit</title>
    <!-- Import Ionicon icons & Google Fonts our Bootstrap theme relies on -->
    <link href="//code.ionicframework.com/ionicons/2.0.1/css/ionicons.min.css" rel="stylesheet" type="text/css">
    <link href="//fonts.googleapis.com/css?family=Titillium+Web:700|Source+Serif+Pro:400,700|Merriweather+Sans:400,700|Source+Sans+Pro:400,300,600,700,300italic,400italic,600italic,700italic" rel="stylesheet" type="text/css">
    <!-- Import the custom Bootstrap 4 theme from our hosted CDN -->
    <link rel="stylesheet" href="//demo.productionready.io/main.css">
  </head>
  <body>

     <nav class="navbar navbar-light">
      <div class="container">
        <a class="navbar-brand" href="index.html">conduit</a>
        <ul class="nav navbar-nav pull-xs-right">
          <li class="nav-item">
            <!-- Add "active" class when you're on that page" -->
            <a class="nav-link active" href="">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="">
              <i class="ion-compose"></i>&nbsp;New Post
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="">
              <i class="ion-gear-a"></i>&nbsp;Settings
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="">Sign up</a>
          </li>
        </ul>
      </div>
    </nav>


```

### Footer
```html
    <footer>
      <div class="container">
        <a href="/" class="logo-font">conduit</a>
        <span class="attribution">
          An interactive learning project from <a href="https://thinkster.io">Thinkster</a>. Code &amp; design licensed under MIT.
        </span>
      </div>
    </footer>

  </body>
</html>
```

## Pages

### Home
```html
<div class="home-page">

  <div class="banner">
    <div class="container">
      <h1 class="logo-font">conduit</h1>
      <p>A place to share your knowledge.</p>
    </div>
  </div>

  <div class="container page">
    <div class="row">

      <div class="col-md-9">
        <div class="feed-toggle">
          <ul class="nav nav-pills outline-active">
            <li class="nav-item">
              <a class="nav-link disabled" href="">Your Feed</a>
            </li>
            <li class="nav-item">
              <a class="nav-link active" href="">Global Feed</a>
            </li>
          </ul>
        </div>

        <div class="article-preview">
          <div class="article-meta">
            <a href="profile.html"><img src="http://i.imgur.com/Qr71crq.jpg" /></a>
            <div class="info">
              <a href="" class="author">Eric Simons</a>
              <span class="date">January 20th</span>
            </div>
            <button class="btn btn-outline-primary btn-sm pull-xs-right">
              <i class="ion-heart"></i> 29
            </button>
          </div>
          <a href="" class="preview-link">
            <h1>How to build webapps that scale</h1>
            <p>This is the description for the post.</p>
            <span>Read more...</span>
          </a>
        </div>

        <div class="article-preview">
          <div class="article-meta">
            <a href="profile.html"><img src="http://i.imgur.com/N4VcUeJ.jpg" /></a>
            <div class="info">
              <a href="" class="author">Albert Pai</a>
              <span class="date">January 20th</span>
            </div>
            <button class="btn btn-outline-primary btn-sm pull-xs-right">
              <i class="ion-heart"></i> 32
            </button>
          </div>
          <a href="" class="preview-link">
            <h1>The song you won't ever stop singing. No matter how hard you try.</h1>
            <p>This is the description for the post.</p>
            <span>Read more...</span>
          </a>
        </div>

      </div>

      <div class="col-md-3">
        <div class="sidebar">
          <p>Popular Tags</p>

          <div class="tag-list">
            <a href="" class="tag-pill tag-default">programming</a>
            <a href="" class="tag-pill tag-default">javascript</a>
            <a href="" class="tag-pill tag-default">emberjs</a>
            <a href="" class="tag-pill tag-default">angularjs</a>
            <a href="" class="tag-pill tag-default">react</a>
            <a href="" class="tag-pill tag-default">mean</a>
            <a href="" class="tag-pill tag-default">node</a>
            <a href="" class="tag-pill tag-default">rails</a>
          </div>
        </div>
      </div>

    </div>
  </div>

</div>
```

### Login/Register

```html
<div class="auth-page">
  <div class="container page">
    <div class="row">

      <div class="col-md-6 offset-md-3 col-xs-12">
        <h1 class="text-xs-center">Sign up</h1>
        <p class="text-xs-center">
          <a href="">Have an account?</a>
        </p>

        <ul class="error-messages">
          <li>That email is already taken</li>
        </ul>

        <form>
          <fieldset class="form-group">
            <input class="form-control form-control-lg" type="text" placeholder="Your Name">
          </fieldset>
          <fieldset class="form-group">
            <input class="form-control form-control-lg" type="text" placeholder="Email">
          </fieldset>
          <fieldset class="form-group">
            <input class="form-control form-control-lg" type="password" placeholder="Password">
          </fieldset>
          <button class="btn btn-lg btn-primary pull-xs-right">
            Sign up
          </button>
        </form>
      </div>

    </div>
  </div>
</div>
```

### Profile

```html
<div class="profile-page">

  <div class="user-info">
    <div class="container">
      <div class="row">

        <div class="col-xs-12 col-md-10 offset-md-1">
          <img src="http://i.imgur.com/Qr71crq.jpg" class="user-img" />
          <h4>Eric Simons</h4>
          <p>
            Cofounder @GoThinkster, lived in Aol's HQ for a few months, kinda looks like Peeta from the Hunger Games
          </p>
          <button class="btn btn-sm btn-outline-secondary action-btn">
            <i class="ion-plus-round"></i>
            &nbsp;
            Follow Eric Simons 
          </button>
        </div>

      </div>
    </div>
  </div>

  <div class="container">
    <div class="row">

      <div class="col-xs-12 col-md-10 offset-md-1">
        <div class="articles-toggle">
          <ul class="nav nav-pills outline-active">
            <li class="nav-item">
              <a class="nav-link active" href="">My Articles</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="">Favorited Articles</a>
            </li>
          </ul>
        </div>

        <div class="article-preview">
          <div class="article-meta">
            <a href=""><img src="http://i.imgur.com/Qr71crq.jpg" /></a>
            <div class="info">
              <a href="" class="author">Eric Simons</a>
              <span class="date">January 20th</span>
            </div>
            <button class="btn btn-outline-primary btn-sm pull-xs-right">
              <i class="ion-heart"></i> 29
            </button>
          </div>
          <a href="" class="preview-link">
            <h1>How to build webapps that scale</h1>
            <p>This is the description for the post.</p>
            <span>Read more...</span>
          </a>
        </div>

        <div class="article-preview">
          <div class="article-meta">
            <a href=""><img src="http://i.imgur.com/N4VcUeJ.jpg" /></a>
            <div class="info">
              <a href="" class="author">Albert Pai</a>
              <span class="date">January 20th</span>
            </div>
            <button class="btn btn-outline-primary btn-sm pull-xs-right">
              <i class="ion-heart"></i> 32
            </button>
          </div>
          <a href="" class="preview-link">
            <h1>The song you won't ever stop singing. No matter how hard you try.</h1>
            <p>This is the description for the post.</p>
            <span>Read more...</span>
            <ul class="tag-list">
              <li class="tag-default tag-pill tag-outline">Music</li>
              <li class="tag-default tag-pill tag-outline">Song</li>
            </ul>
          </a>
        </div>


      </div>

    </div>
  </div>

</div>
```

### Settings

```html
<div class="settings-page">
  <div class="container page">
    <div class="row">

      <div class="col-md-6 offset-md-3 col-xs-12">
        <h1 class="text-xs-center">Your Settings</h1>

        <form>
          <fieldset>
              <fieldset class="form-group">
                <input class="form-control" type="text" placeholder="URL of profile picture">
              </fieldset>
              <fieldset class="form-group">
                <input class="form-control form-control-lg" type="text" placeholder="Your Name">
              </fieldset>
              <fieldset class="form-group">
                <textarea class="form-control form-control-lg" rows="8" placeholder="Short bio about you"></textarea>
              </fieldset>
              <fieldset class="form-group">
                <input class="form-control form-control-lg" type="text" placeholder="Email">
              </fieldset>
              <fieldset class="form-group">
                <input class="form-control form-control-lg" type="password" placeholder="Password">
              </fieldset>
              <button class="btn btn-lg btn-primary pull-xs-right">
                Update Settings
              </button>
          </fieldset>
        </form>
      </div>

    </div>
  </div>
</div>
```

### Create/Edit Article

```html
<div class="editor-page">
  <div class="container page">
    <div class="row">

      <div class="col-md-10 offset-md-1 col-xs-12">
        <form>
          <fieldset>
            <fieldset class="form-group">
                <input type="text" class="form-control form-control-lg" placeholder="Article Title">
            </fieldset>
            <fieldset class="form-group">
                <input type="text" class="form-control" placeholder="What's this article about?">
            </fieldset>
            <fieldset class="form-group">
                <textarea class="form-control" rows="8" placeholder="Write your article (in markdown)"></textarea>
            </fieldset>
            <fieldset class="form-group">
                <input type="text" class="form-control" placeholder="Enter tags"><div class="tag-list"></div>
            </fieldset>
            <button class="btn btn-lg pull-xs-right btn-primary" type="button">
                Publish Article
            </button>
          </fieldset>
        </form>
      </div>

    </div>
  </div>
</div>


```

### Article

```html
<div class="article-page">

  <div class="banner">
    <div class="container">

      <h1>How to build webapps that scale</h1>

      <div class="article-meta">
        <a href=""><img src="http://i.imgur.com/Qr71crq.jpg" /></a>
        <div class="info">
          <a href="" class="author">Eric Simons</a>
          <span class="date">January 20th</span>
        </div>
        <button class="btn btn-sm btn-outline-secondary">
          <i class="ion-plus-round"></i>
          &nbsp;
          Follow Eric Simons <span class="counter">(10)</span>
        </button>
        &nbsp;&nbsp;
        <button class="btn btn-sm btn-outline-primary">
          <i class="ion-heart"></i>
          &nbsp;
          Favorite Post <span class="counter">(29)</span>
        </button>
      </div>

    </div>
  </div>

  <div class="container page">

    <div class="row article-content">
      <div class="col-md-12">
        <p>
        Web development technologies have evolved at an incredible clip over the past few years.
        </p>
        <h2 id="introducing-ionic">Introducing RealWorld.</h2>
        <p>It's a great solution for learning how other frameworks work.</p>
      </div>
    </div>

    <hr />

    <div class="article-actions">
      <div class="article-meta">
        <a href="profile.html"><img src="http://i.imgur.com/Qr71crq.jpg" /></a>
        <div class="info">
          <a href="" class="author">Eric Simons</a>
          <span class="date">January 20th</span>
        </div>

        <button class="btn btn-sm btn-outline-secondary">
          <i class="ion-plus-round"></i>
          &nbsp;
          Follow Eric Simons <span class="counter">(10)</span>
        </button>
        &nbsp;
        <button class="btn btn-sm btn-outline-primary">
          <i class="ion-heart"></i>
          &nbsp;
          Favorite Post <span class="counter">(29)</span>
        </button>
      </div>
    </div>

    <div class="row">

      <div class="col-xs-12 col-md-8 offset-md-2">

        <form class="card comment-form">
          <div class="card-block">
            <textarea class="form-control" placeholder="Write a comment..." rows="3"></textarea>
          </div>
          <div class="card-footer">
            <img src="http://i.imgur.com/Qr71crq.jpg" class="comment-author-img" />
            <button class="btn btn-sm btn-primary">
             Post Comment
            </button>
          </div>
        </form>
        
        <div class="card">
          <div class="card-block">
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
          </div>
          <div class="card-footer">
            <a href="" class="comment-author">
              <img src="http://i.imgur.com/Qr71crq.jpg" class="comment-author-img" />
            </a>
            &nbsp;
            <a href="" class="comment-author">Jacob Schmidt</a>
            <span class="date-posted">Dec 29th</span>
          </div>
        </div>

        <div class="card">
          <div class="card-block">
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
          </div>
          <div class="card-footer">
            <a href="" class="comment-author">
              <img src="http://i.imgur.com/Qr71crq.jpg" class="comment-author-img" />
            </a>
            &nbsp;
            <a href="" class="comment-author">Jacob Schmidt</a>
            <span class="date-posted">Dec 29th</span>
            <span class="mod-options">
              <i class="ion-edit"></i>
              <i class="ion-trash-a"></i>
            </span>
          </div>
        </div>
        
      </div>

    </div>

  </div>

</div>
```

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/go.mod
module github.com/gothinkster/golang-gin-realworld-example-app

go 1.15

require (
	github.com/denisenkom/go-mssqldb v0.9.0 // indirect
	github.com/dgrijalva/jwt-go v3.2.0+incompatible
	github.com/erikstmartin/go-testdb v0.0.0-20160219214506-8d10e4a1bae5 // indirect
	github.com/gin-contrib/sse v0.1.0 // indirect
	github.com/gin-gonic/gin v1.1.5-0.20170716034208-93b3a0d7ec95
	github.com/go-sql-driver/mysql v1.5.0 // indirect
	github.com/golang/protobuf v1.5.1 // indirect
	github.com/gosimple/slug v1.9.0
	github.com/jinzhu/gorm v0.0.0-20170703134954-2a1463811ee1
	github.com/jinzhu/inflection v1.0.0 // indirect
	github.com/jinzhu/now v1.1.2 // indirect
	github.com/json-iterator/go v1.1.10 // indirect
	github.com/lib/pq v1.10.0 // indirect
	github.com/mattn/go-isatty v0.0.12 // indirect
	github.com/mattn/go-sqlite3 v1.14.6 // indirect
	github.com/stretchr/testify v1.7.0
	github.com/ugorji/go v1.2.4 // indirect
	golang.org/x/crypto v0.0.0-20210322153248-0c34fe9e7dc2
	gopkg.in/go-playground/assert.v1 v1.2.1 // indirect
	gopkg.in/go-playground/validator.v8 v8.18.2
	gopkg.in/yaml.v2 v2.4.0 // indirect
)

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/go.mod-generated_by_mod_init
module github.com/gothinkster/golang-gin-realworld-example-app

go 1.15

require (
	github.com/Pallinder/go-randomdata v0.0.0-20170410161340-8c3362a5e678
	github.com/davecgh/go-spew v1.1.1-0.20170711183451-adab96458c51
	github.com/dgrijalva/jwt-go v3.0.1-0.20170608005149-a539ee1a749a+incompatible
	github.com/gin-contrib/sse v0.0.0-20170109093832-22d885f9ecc7
	github.com/gin-gonic/contrib v0.0.0-20170529062310-d4fc5a96cc0d
	github.com/gin-gonic/gin v1.1.5-0.20170716034208-93b3a0d7ec95
	github.com/go-playground/locales v0.11.2-0.20170327191450-1e5f1161c641
	github.com/go-playground/universal-translator v0.16.1-0.20170327191703-71201497bace
	github.com/golang/protobuf v0.0.0-20170712042213-0a4f71a498b7
	github.com/gosimple/slug v1.1.0
	github.com/jinzhu/gorm v0.0.0-20170703134954-2a1463811ee1
	github.com/jinzhu/inflection v0.0.0-20170102125226-1c35d901db3d
	github.com/json-iterator/go v0.0.0-20170711230430-b9dc3ebda73c
	github.com/mattn/go-isatty v0.0.2
	github.com/mattn/go-sqlite3 v1.2.1-0.20170710140056-47fc4e5e9153
	github.com/pmezard/go-difflib v1.0.0
	github.com/rainycape/unidecode v0.0.0-20150907023854-cb7f23ec59be
	github.com/stretchr/objx v0.0.0-20150928122152-1a9d0bb9f541
	github.com/stretchr/testify v1.1.5-0.20170714215325-05e8a0eda380
	github.com/ugorji/go v0.0.0-20170620104852-5efa3251c7f7
	golang.org/x/net v0.0.0-20170711181219-f01ecb60fe38
	golang.org/x/sys v0.0.0-20170710161658-abf9c25f5445
	gopkg.in/gin-gonic/gin.v1 v1.1.5-0.20170702092826-d459835d2b07
	gopkg.in/go-playground/validator.v8 v8.18.1
	gopkg.in/stretchr/testify.v1 v1.1.4
	gopkg.in/yaml.v2 v2.0.0-20170712054546-1be3d31502d6
)

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/go.sum
github.com/davecgh/go-spew v1.1.0/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/denisenkom/go-mssqldb v0.9.0 h1:RSohk2RsiZqLZ0zCjtfn3S4Gp4exhpBWHyQ7D0yGjAk=
github.com/denisenkom/go-mssqldb v0.9.0/go.mod h1:xbL0rPBG9cCiLr28tMa8zpbdarY27NDyej4t/EjAShU=
github.com/dgrijalva/jwt-go v3.2.0+incompatible h1:7qlOGliEKZXTDg6OTjfoBKDXWrumCAMpl/TFQ4/5kLM=
github.com/dgrijalva/jwt-go v3.2.0+incompatible/go.mod h1:E3ru+11k8xSBh+hMPgOLZmtrrCbhqsmaPHjLKYnJCaQ=
github.com/erikstmartin/go-testdb v0.0.0-20160219214506-8d10e4a1bae5 h1:Yzb9+7DPaBjB8zlTR87/ElzFsnQfuHnVUVqpZZIcV5Y=
github.com/erikstmartin/go-testdb v0.0.0-20160219214506-8d10e4a1bae5/go.mod h1:a2zkGnVExMxdzMo3M0Hi/3sEU+cWnZpSni0O6/Yb/P0=
github.com/gin-contrib/sse v0.1.0 h1:Y/yl/+YNO8GZSjAhjMsSuLt29uWRFHdHYUb5lYOV9qE=
github.com/gin-contrib/sse v0.1.0/go.mod h1:RHrZQHXnP2xjPF+u1gW/2HnVO7nvIa9PG3Gm+fLHvGI=
github.com/gin-gonic/gin v1.1.5-0.20170716034208-93b3a0d7ec95 h1:sIbRUfQ2deJ7FBWMCYemeGy82ZiuGL/uSPnYpjcr8zw=
github.com/gin-gonic/gin v1.1.5-0.20170716034208-93b3a0d7ec95/go.mod h1:7cKuhb5qV2ggCFctp2fJQ+ErvciLZrIeoOSOm6mUr7Y=
github.com/go-sql-driver/mysql v1.5.0 h1:ozyZYNQW3x3HtqT1jira07DN2PArx2v7/mN66gGcHOs=
github.com/go-sql-driver/mysql v1.5.0/go.mod h1:DCzpHaOWr8IXmIStZouvnhqoel9Qv2LBy8hT2VhHyBg=
github.com/golang-sql/civil v0.0.0-20190719163853-cb61b32ac6fe h1:lXe2qZdvpiX5WZkZR4hgp4KJVfY3nMkvmwbVkpv1rVY=
github.com/golang-sql/civil v0.0.0-20190719163853-cb61b32ac6fe/go.mod h1:8vg3r2VgvsThLBIFL93Qb5yWzgyZWhEmBwUJWevAkK0=
github.com/golang/protobuf v1.5.0/go.mod h1:FsONVRAS9T7sI+LIUmWTfcYkHO4aIWwzhcaSAoJOfIk=
github.com/golang/protobuf v1.5.1 h1:jAbXjIeW2ZSW2AwFxlGTDoc2CjI2XujLkV3ArsZFCvc=
github.com/golang/protobuf v1.5.1/go.mod h1:DopwsBzvsk0Fs44TXzsVbJyPhcCPeIwnvohx4u74HPM=
github.com/google/go-cmp v0.5.5 h1:Khx7svrCpmxxtHBq5j2mp/xVjsi8hQMfNLvJFAlrGgU=
github.com/google/go-cmp v0.5.5/go.mod h1:v8dTdLbMG2kIc/vJvl+f65V22dbkXbowE6jgT/gNBxE=
github.com/google/gofuzz v1.0.0/go.mod h1:dBl0BpW6vV/+mYPU4Po3pmUjxk6FQPldtuIdl/M65Eg=
github.com/gosimple/slug v1.9.0 h1:r5vDcYrFz9BmfIAMC829un9hq7hKM4cHUrsv36LbEqs=
github.com/gosimple/slug v1.9.0/go.mod h1:AMZ+sOVe65uByN3kgEyf9WEBKBCSS+dJjMX9x4vDJbg=
github.com/jinzhu/gorm v0.0.0-20170703134954-2a1463811ee1 h1:sWeCm69jE8uwB/gHLNG65Szf24KebYqoWq1boLccYcQ=
github.com/jinzhu/gorm v0.0.0-20170703134954-2a1463811ee1/go.mod h1:Vla75njaFJ8clLU1W44h34PjIkijhjHIYnZxMqCdxqo=
github.com/jinzhu/inflection v1.0.0 h1:K317FqzuhWc8YvSVlFMCCUb36O/S9MCKRDI7QkRKD/E=
github.com/jinzhu/inflection v1.0.0/go.mod h1:h+uFLlag+Qp1Va5pdKtLDYj+kHp5pxUVkryuEj+Srlc=
github.com/jinzhu/now v1.1.2 h1:eVKgfIdy9b6zbWBMgFpfDPoAMifwSZagU9HmEU6zgiI=
github.com/jinzhu/now v1.1.2/go.mod h1:d3SSVoowX0Lcu0IBviAWJpolVfI5UJVZZ7cO71lE/z8=
github.com/json-iterator/go v1.1.10 h1:Kz6Cvnvv2wGdaG/V8yMvfkmNiXq9Ya2KUv4rouJJr68=
github.com/json-iterator/go v1.1.10/go.mod h1:KdQUCv79m/52Kvf8AW2vK1V8akMuk1QjK/uOdHXbAo4=
github.com/lib/pq v1.10.0 h1:Zx5DJFEYQXio93kgXnQ09fXNiUKsqv4OUEu2UtGcB1E=
github.com/lib/pq v1.10.0/go.mod h1:AlVN5x4E4T544tWzH6hKfbfQvm3HdbOxrmggDNAPY9o=
github.com/mattn/go-isatty v0.0.12 h1:wuysRhFDzyxgEmMf5xjvJ2M9dZoWAXNNr5LSBS7uHXY=
github.com/mattn/go-isatty v0.0.12/go.mod h1:cbi8OIDigv2wuxKPP5vlRcQ1OAZbq2CE4Kysco4FUpU=
github.com/mattn/go-sqlite3 v1.14.6 h1:dNPt6NO46WmLVt2DLNpwczCmdV5boIZ6g/tlDrlRUbg=
github.com/mattn/go-sqlite3 v1.14.6/go.mod h1:NyWgC/yNuGj7Q9rpYnZvas74GogHl5/Z4A/KQRfk6bU=
github.com/modern-go/concurrent v0.0.0-20180228061459-e0a39a4cb421 h1:ZqeYNhU3OHLH3mGKHDcjJRFFRrJa6eAM5H+CtDdOsPc=
github.com/modern-go/concurrent v0.0.0-20180228061459-e0a39a4cb421/go.mod h1:6dJC0mAP4ikYIbvyc7fijjWJddQyLn8Ig3JB5CqoB9Q=
github.com/modern-go/reflect2 v0.0.0-20180701023420-4b7aa43c6742 h1:Esafd1046DLDQ0W1YjYsBW+p8U2u7vzgW2SQVmlNazg=
github.com/modern-go/reflect2 v0.0.0-20180701023420-4b7aa43c6742/go.mod h1:bx2lNnkwVCuqBIxFjflWJWanXIb3RllmbCylyMrvgv0=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/rainycape/unidecode v0.0.0-20150907023854-cb7f23ec59be h1:ta7tUOvsPHVHGom5hKW5VXNc2xZIkfCKP8iaqOyYtUQ=
github.com/rainycape/unidecode v0.0.0-20150907023854-cb7f23ec59be/go.mod h1:MIDFMn7db1kT65GmV94GzpX9Qdi7N/pQlwb+AN8wh+Q=
github.com/stretchr/objx v0.1.0/go.mod h1:HFkY916IF+rwdDfMAkV7OtwuqBVzrE8GR6GFx+wExME=
github.com/stretchr/testify v1.3.0/go.mod h1:M5WIy9Dh21IEIfnGCwXGc5bZfKNJtfHm1UVUgZn+9EI=
github.com/stretchr/testify v1.7.0 h1:nwc3DEeHmmLAfoZucVR881uASk0Mfjw8xYJ99tb5CcY=
github.com/stretchr/testify v1.7.0/go.mod h1:6Fq8oRcR53rry900zMqJjRRixrwX3KX962/h/Wwjteg=
github.com/ugorji/go v1.2.4 h1:cTciPbZ/VSOzCLKclmssnfQ/jyoVyOcJ3aoJyUV1Urc=
github.com/ugorji/go v1.2.4/go.mod h1:EuaSCk8iZMdIspsu6HXH7X2UGKw1ezO4wCfGszGmmo4=
github.com/ugorji/go/codec v1.2.4 h1:C5VurWRRCKjuENsbM6GYVw8W++WVW9rSxoACKIvxzz8=
github.com/ugorji/go/codec v1.2.4/go.mod h1:bWBu1+kIRWcF8uMklKaJrR6fTWQOwAlrIzX22pHwryA=
golang.org/x/crypto v0.0.0-20190325154230-a5d413f7728c/go.mod h1:djNgcEr1/C05ACkg1iLfiJU5Ep61QUkGW8qpdssI0+w=
golang.org/x/crypto v0.0.0-20210322153248-0c34fe9e7dc2 h1:It14KIkyBFYkHkwZ7k45minvA9aorojkyjGk9KJ5B/w=
golang.org/x/crypto v0.0.0-20210322153248-0c34fe9e7dc2/go.mod h1:T9bdIzuCu7OtxOm1hfPfRQxPLYneinmdGuTeoZ9dtd4=
golang.org/x/net v0.0.0-20210226172049-e18ecbb05110 h1:qWPm9rbaAMKs8Bq/9LRpbMqxWRVUAQwMI9fVrssnTfw=
golang.org/x/net v0.0.0-20210226172049-e18ecbb05110/go.mod h1:m0MpNAwzfU5UDzcl9v0D8zg8gWTRqZa9RBIspLL5mdg=
golang.org/x/sys v0.0.0-20190215142949-d0b11bdaac8a/go.mod h1:STP8DvDyc/dI5b8T5hshtkjS+E42TnysNCUPdjciGhY=
golang.org/x/sys v0.0.0-20200116001909-b77594299b42/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/sys v0.0.0-20201119102817-f84b799fce68 h1:nxC68pudNYkKU6jWhgrqdreuFiOQWj1Fs7T3VrH4Pjw=
golang.org/x/sys v0.0.0-20201119102817-f84b799fce68/go.mod h1:h1NjWce9XRLGQEsW7wpKNCjG9DtNlClVuFLEZdDNbEs=
golang.org/x/term v0.0.0-20201126162022-7de9c90e9dd1/go.mod h1:bj7SfCRtBDWHUb9snDiAeCFNEtKQo2Wmx5Cou7ajbmo=
golang.org/x/text v0.3.3/go.mod h1:5Zoc/QRtKVWzQhOtBMvqHzDpF6irO9z98xDceosuGiQ=
golang.org/x/tools v0.0.0-20180917221912-90fa682c2a6e/go.mod h1:n7NCudcB/nEzxVGmLbDWY5pfWTLqBcC2KZ6jyYvM4mQ=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543 h1:E7g+9GITq07hpfrRu66IVDexMakfv52eLZ2CXBWiKr4=
golang.org/x/xerrors v0.0.0-20191204190536-9bdfabe68543/go.mod h1:I/5z698sn9Ka8TeJc9MKroUUfqBBauWjQqLJ2OPfmY0=
google.golang.org/protobuf v1.26.0-rc.1/go.mod h1:jlhhOSvTdKEhbULTjvd4ARK9grFBp09yW+WbY/TyQbw=
google.golang.org/protobuf v1.26.0 h1:bxAC2xTBsZGibn2RTntX0oH50xLsqy1OxA9tTL3p/lk=
google.golang.org/protobuf v1.26.0/go.mod h1:9q0QmTI4eRPtz6boOQmLYwt+qCgq0jsYwAQnmE0givc=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405 h1:yhCVgyC4o1eVCa2tZl7eS0r+SDo693bJlVdllGtEeKM=
gopkg.in/check.v1 v0.0.0-20161208181325-20d25e280405/go.mod h1:Co6ibVJAznAaIkqp8huTwlJQCZ016jof/cbN4VW5Yz0=
gopkg.in/go-playground/assert.v1 v1.2.1 h1:xoYuJVE7KT85PYWrN730RguIQO0ePzVRfFMXadIrXTM=
gopkg.in/go-playground/assert.v1 v1.2.1/go.mod h1:9RXL0bg/zibRAgZUYszZSwO/z8Y/a8bDuhia5mkpMnE=
gopkg.in/go-playground/validator.v8 v8.18.2 h1:lFB4DoMU6B626w8ny76MV7VX6W2VHct2GVOI3xgiMrQ=
gopkg.in/go-playground/validator.v8 v8.18.2/go.mod h1:RX2a/7Ha8BgOhfk7j780h4/u/RRjR0eouCJSH80/M2Y=
gopkg.in/yaml.v2 v2.4.0 h1:D8xgwECY7CYvx+Y2n4sBz93Jn9JRvxdiyyo8CTfuKaY=
gopkg.in/yaml.v2 v2.4.0/go.mod h1:RDklbk79AGWmwhnvt/jBztapEOGDOx6ZbXqjP6csGnQ=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c h1:dUUwHk2QECo/6vqA44rthZ8ie2QXMNeKRTHCNY2nXvo=
gopkg.in/yaml.v3 v3.0.0-20200313102051-9f266ea9e77c/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/gorm.db

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/hello.go
package main

import (
	"fmt"

	"github.com/gin-gonic/gin"

	"github.com/jinzhu/gorm"
	"github.com/gothinkster/golang-gin-realworld-example-app/articles"
	"github.com/gothinkster/golang-gin-realworld-example-app/common"
	"github.com/gothinkster/golang-gin-realworld-example-app/users"
)

func Migrate(db *gorm.DB) {
	users.AutoMigrate()
	db.AutoMigrate(&articles.ArticleModel{})
	db.AutoMigrate(&articles.TagModel{})
	db.AutoMigrate(&articles.FavoriteModel{})
	db.AutoMigrate(&articles.ArticleUserModel{})
	db.AutoMigrate(&articles.CommentModel{})
}

func main() {

	db := common.Init()
	Migrate(db)
	defer db.Close()

	r := gin.Default()

	v1 := r.Group("/api")
	users.UsersRegister(v1.Group("/users"))
	v1.Use(users.AuthMiddleware(false))
	articles.ArticlesAnonymousRegister(v1.Group("/articles"))
	articles.TagsAnonymousRegister(v1.Group("/tags"))

	v1.Use(users.AuthMiddleware(true))
	users.UserRegister(v1.Group("/user"))
	users.ProfileRegister(v1.Group("/profiles"))

	articles.ArticlesRegister(v1.Group("/articles"))

	testAuth := r.Group("/api/ping")

	testAuth.GET("/", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "pong",
		})
	})

	// test 1 to 1
	tx1 := db.Begin()
	userA := users.UserModel{
		Username: "AAAAAAAAAAAAAAAA",
		Email:    "aaaa@g.cn",
		Bio:      "hehddeda",
		Image:    nil,
	}
	tx1.Save(&userA)
	tx1.Commit()
	fmt.Println(userA)

	//db.Save(&ArticleUserModel{
	//    UserModelID:userA.ID,
	//})
	//var userAA ArticleUserModel
	//db.Where(&ArticleUserModel{
	//    UserModelID:userA.ID,
	//}).First(&userAA)
	//fmt.Println(userAA)

	r.Run() // listen and serve on 0.0.0.0:8080
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/LICENSE
MIT License

Copyright (c) 2017 wangzitian0

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/logo.png
iVBORw0KGgoAAAANSUhEUgAABoUAAAEBCAYAAAC+OawFAAAACXBIWXMAABcSAAAXEgFnn9JSAAA7AWlUWHRYTUw6Y29tLmFkb2JlLnhtcAAAAAAAPD94cGFja2V0IGJlZ2luPSLvu78iIGlkPSJXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQiPz4KPHg6eG1wbWV0YSB4bWxuczp4PSJhZG9iZTpuczptZXRhLyIgeDp4bXB0az0iQWRvYmUgWE1QIENvcmUgNS42LWMwMTQgNzkuMTU2Nzk3LCAyMDE0LzA4LzIwLTA5OjUzOjAyICAgICAgICAiPgogICA8cmRmOlJERiB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiPgogICAgICA8cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0iIgogICAgICAgICAgICB4bWxuczp4bXA9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyIKICAgICAgICAgICAgeG1sbnM6cGhvdG9zaG9wPSJodHRwOi8vbnMuYWRvYmUuY29tL3Bob3Rvc2hvcC8xLjAvIgogICAgICAgICAgICB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIKICAgICAgICAgICAgeG1sbnM6c3RFdnQ9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZUV2ZW50IyIKICAgICAgICAgICAgeG1sbnM6dGlmZj0iaHR0cDovL25zLmFkb2JlLmNvbS90aWZmLzEuMC8iCiAgICAgICAgICAgIHhtbG5zOmV4aWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20vZXhpZi8xLjAvIj4KICAgICAgICAgPHhtcDpDcmVhdG9yVG9vbD5BZG9iZSBQaG90b3Nob3AgQ0MgMjAxNCAoTWFjaW50b3NoKTwveG1wOkNyZWF0b3JUb29sPgogICAgICAgICA8eG1wOkNyZWF0ZURhdGU+MjAxNy0wNy0xMlQxNDozODowMSswODowMDwveG1wOkNyZWF0ZURhdGU+CiAgICAgICAgIDx4bXA6TW9kaWZ5RGF0ZT4yMDE3LTA3LTI4VDE4OjQzOjU5KzA4OjAwPC94bXA6TW9kaWZ5RGF0ZT4KICAgICAgICAgPHhtcDpNZXRhZGF0YURhdGU+MjAxNy0wNy0yOFQxODo0Mzo1OSswODowMDwveG1wOk1ldGFkYXRhRGF0ZT4KICAgICAgICAgPGRjOmZvcm1hdD5pbWFnZS9wbmc8L2RjOmZvcm1hdD4KICAgICAgICAgPHBob3Rvc2hvcDpDb2xvck1vZGU+MzwvcGhvdG9zaG9wOkNvbG9yTW9kZT4KICAgICAgICAgPHBob3Rvc2hvcDpEb2N1bWVudEFuY2VzdG9ycz4KICAgICAgICAgICAgPHJkZjpCYWc+CiAgICAgICAgICAgICAgIDxyZGY6bGk+QzVEMUExRUUxQjZDMDZGOTFEMzUwMjRBMDMzQURFNDY8L3JkZjpsaT4KICAgICAgICAgICAgICAgPHJkZjpsaT54bXAuZGlkOjNkZjg2NGUyLTM0MjctNDFiYi1iZjliLWM0ZDMzMmJhN2QyZjwvcmRmOmxpPgogICAgICAgICAgICA8L3JkZjpCYWc+CiAgICAgICAgIDwvcGhvdG9zaG9wOkRvY3VtZW50QW5jZXN0b3JzPgogICAgICAgICA8eG1wTU06SW5zdGFuY2VJRD54bXAuaWlkOjQxYjEyZmE3LWEyYTUtNDhmNC1hZDA3LWY5YWQ2MWZiMGUzMzwveG1wTU06SW5zdGFuY2VJRD4KICAgICAgICAgPHhtcE1NOkRvY3VtZW50SUQ+YWRvYmU6ZG9jaWQ6cGhvdG9zaG9wOjBkMzI5YzkwLWI0MTAtMTE3YS1hNmVhLTliZGVmMDcyZTY0OTwveG1wTU06RG9jdW1lbnRJRD4KICAgICAgICAgPHhtcE1NOk9yaWdpbmFsRG9jdW1lbnRJRD54bXAuZGlkOjg4YWZjZDEzLWYyNDUtNGY4Zi1hZjMzLTZlOGNjMWM0MjdmMjwveG1wTU06T3JpZ2luYWxEb2N1bWVudElEPgogICAgICAgICA8eG1wTU06SGlzdG9yeT4KICAgICAgICAgICAgPHJkZjpTZXE+CiAgICAgICAgICAgICAgIDxyZGY6bGkgcmRmOnBhcnNlVHlwZT0iUmVzb3VyY2UiPgogICAgICAgICAgICAgICAgICA8c3RFdnQ6YWN0aW9uPmNyZWF0ZWQ8L3N0RXZ0OmFjdGlvbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0Omluc3RhbmNlSUQ+eG1wLmlpZDo4OGFmY2QxMy1mMjQ1LTRmOGYtYWYzMy02ZThjYzFjNDI3ZjI8L3N0RXZ0Omluc3RhbmNlSUQ+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDp3aGVuPjIwMTctMDctMTJUMTQ6Mzg6MDErMDg6MDA8L3N0RXZ0OndoZW4+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpzb2Z0d2FyZUFnZW50PkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE0IChNYWNpbnRvc2gpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgICAgPHJkZjpsaSByZGY6cGFyc2VUeXBlPSJSZXNvdXJjZSI+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDphY3Rpb24+c2F2ZWQ8L3N0RXZ0OmFjdGlvbj4KICAgICAgICAgICAgICAgICAgPHN0RXZ0Omluc3RhbmNlSUQ+eG1wLmlpZDo0MWIxMmZhNy1hMmE1LTQ4ZjQtYWQwNy1mOWFkNjFmYjBlMzM8L3N0RXZ0Omluc3RhbmNlSUQ+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDp3aGVuPjIwMTctMDctMjhUMTg6NDM6NTkrMDg6MDA8L3N0RXZ0OndoZW4+CiAgICAgICAgICAgICAgICAgIDxzdEV2dDpzb2Z0d2FyZUFnZW50PkFkb2JlIFBob3Rvc2hvcCBDQyAyMDE0IChNYWNpbnRvc2gpPC9zdEV2dDpzb2Z0d2FyZUFnZW50PgogICAgICAgICAgICAgICAgICA8c3RFdnQ6Y2hhbmdlZD4vPC9zdEV2dDpjaGFuZ2VkPgogICAgICAgICAgICAgICA8L3JkZjpsaT4KICAgICAgICAgICAgPC9yZGY6U2VxPgogICAgICAgICA8L3htcE1NOkhpc3Rvcnk+CiAgICAgICAgIDx0aWZmOk9yaWVudGF0aW9uPjE8L3RpZmY6T3JpZW50YXRpb24+CiAgICAgICAgIDx0aWZmOlhSZXNvbHV0aW9uPjE1MDAwMDAvMTAwMDA8L3RpZmY6WFJlc29sdXRpb24+CiAgICAgICAgIDx0aWZmOllSZXNvbHV0aW9uPjE1MDAwMDAvMTAwMDA8L3RpZmY6WVJlc29sdXRpb24+CiAgICAgICAgIDx0aWZmOlJlc29sdXRpb25Vbml0PjI8L3RpZmY6UmVzb2x1dGlvblVuaXQ+CiAgICAgICAgIDxleGlmOkNvbG9yU3BhY2U+NjU1MzU8L2V4aWY6Q29sb3JTcGFjZT4KICAgICAgICAgPGV4aWY6UGl4ZWxYRGltZW5zaW9uPjE2Njk8L2V4aWY6UGl4ZWxYRGltZW5zaW9uPgogICAgICAgICA8ZXhpZjpQaXhlbFlEaW1lbnNpb24+MjU3PC9leGlmOlBpeGVsWURpbWVuc2lvbj4KICAgICAgPC9yZGY6RGVzY3JpcHRpb24+CiAgIDwvcmRmOlJERj4KPC94OnhtcG1ldGE+CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgCjw/eHBhY2tldCBlbmQ9InciPz6IXfKWAAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAMSrSURBVHja7N13nBvF+fjxz+yqXj/73Hs3HVNMN72DIaEGCN8kEJKQBvkmUTqks/y+KYQ0EkilJJCETgiBhN676TZgbOPerqvu/P6Y1Z1OJ93p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A/twg9AWPoONFVSwLIQ19G9BkzfdW0aR8+XNY8hrsTOKWPnL9WvVNMpYtqe+BollIRKLk2xvZ92C+WRS3QuBJlz3cSIiIiIiIiIiIiIiVUEthYYnA7QDSzcvWdydbG2BqGHo7t4KlZsC84QN7pM3T29LGNM3qE7PdE/c3knTP7zJ2+b8MtPviQKx8rfBFI5l8mJRylimryy3PnJjGYjW1tGyejUbFr3eDSwA2tB4QiIiIiIiIiIiIiJSRZQUGp4M0A282bzszea2desGqUKNKVQwlmVMxxQyxmCiEdYveJnmFUuXA0uBDlzLLxERERERERERERGRqqCk0PCkgsfy9s0bN25ctAATJB3GXKEGSgPG26FAS6GQWEXNN8Q8xcxnBikLi1XMPhbcH0skHifV0cHKF+aRSnS+BqzFdR2n8YREREREREREREREpGooKTR8aWCjtXbRmvkvkUp1g6mAarRFlhWz7ISKNXSwaE0NLatWsual57uBl3DjCanrOBERERERERERERGpKkoKDV8SNx7N/LUvP9/esXkTJppfjXndrvUrH2y6UFnYbHndrPV0nzZU2YB5wuarsFiD7iPh08HDRKIYE2H1y8+z+c1Fi4F/ofGERERERERERERERKQKKSk0fN1AFzC/aembGze8+grRaDRvlkLdyZki5usdJCdH3rQx/R9h5cG0HWqeAssNGSt/nrDy/OXKHSvkEa2pIdG6lTdnP2qzmcxLwHLceEJZvZVFREREREREREREpJooKTR8WVwrk+XZbOaVN2Y9bDOpVEh+ZzTjDA2RPLK2rzFSTysZY/qmc1rOmNx5IHSeAbEKzNcvVu822ALxQpbrXbZQLEYXq/fRt1wkFmPDgldZ8czcJuApoBmX1BMRERERERERERERqSpKCo1MAmg3mDnLnvpHZ/PyZUTjtUWNb1MyhvDckTGDlxWcp9j5hpinmPnMIGVhsYaMHb5MJBYjnUyy8NH76WprnQ/MBzpxrb1ERERERERERERERKqKkkIjkwweL3Y2N72x8NH7ideOcVKo0Jg8xZaFxerXcqeCYo1kOQORWJzNSxaz6JEHOoHHgQ24hJ7VW1hEREREREREREREqo2xtnqvjxszmi7emAHsCpyyzVv2Ov/km+9myvY7ku7qClqyWEbehVz+skPEyu1CLrfMmL4lC81TYLkB8fNjhdVd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VBk925elr0VTTzd3Pa2BepJEKfq3AMobpahk+9mTGNoZ2BHXndw7gN2DbVwMLMCNybQGN2ZThgnQSgiUFBIRERERERERERGR8lBSaPQiuBZDu+GSE0cAH2ior9u+M5FsAfs68BwuUdHTYqWF4rtNG/Vu5v2d2w2bySsLYws88p8f05cu+DeG6xZvO1xXebVBvXYFddwznlFmIr0vlRQSERERERERERERkXJQUqhEoXBj+Oyc85iK60atCTd20Gbc2DtdjE8iZbKK4JJBPV3hgWvB1EVf13cTipJCIiIiIiIiIiIiIlIOSgqVKFTwby0uGTQV14qlp9VKK9BJX7druupf4peS/q2dwsYvmjCUFBIRERERERERERGRclBSqLR6umSL0pekSAf/9iSERAalpJCIiIiIiIiIiIiIlIPRBWgREREREREREREREZHJL6IqEBERERERERERERERmfyUFBIREREREREREREREakCSgqJiIiIiIiIiIiIiIhUASWFREREREREREREREREqoCSQiIiIiIiIiIiIiIiIlVASSEREREREREREREREZEqoKSQiIiIiIiIiIiIiIhIFVBSSEREREREREREREREpAooKSQiIiIiIiIiIiIiIlIFlBQSERERERERERERERGpAkoKiYiIiIiIiIiIiIiIVAElhURERERERERERERERKqAkkIiIiIiIiIiIiIiIiJVQEkhERERERERERERERGRKqCkkIiIiIiIiIiIiIiISBVQUkhERERERERERERERKQKKCkkIiIiIiIiIiIiIiJSBZQUEhERERERERERERERqQJKComIiIiIiIiIiIiIiFQBJYVERERERERERERERESqgJJCIiIiIiIiIiIiIiIiVUBJIRERERERERERERERkSqgpJCIiIiIiIiIiIiIiEgVUFJIRERERERERERERESkCigpJCIiIiIiIiIiIiIiUgWUFBIREREREREREREREakCSgqJiIiIiIiIiIiIiIhUgf8/ACvz9hFL6XG/AAAAAElFTkSuQmCC
--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/MOBILE_INSTRUCTIONS.md
> *Note: Delete this file before publishing your app!*

# [Mobile Icons (iOS/Android)](https://github.com/gothinkster/realworld/tree/master/spec/mobile_icons)

### Using the hosted API

Simply point your [API requests](https://github.com/gothinkster/realworld/tree/master/api) to `https://conduit.productionready.io/api` and you're good to go!

### Styles/Templates

Unfortunately, there isn't a common way for us to reuse & share styles/templates for cross-platform mobile apps.

Instead, we recommend using the Medium.com [iOS](https://itunes.apple.com/us/app/medium/id828256236?mt=8) and [Android](https://play.google.com/store/apps/details?id=com.medium.reader&hl=en) apps as a "north star" regarding general UI functionality/layout, but try not to go too overboard otherwise it will unnecessarily complicate your codebase (in other words, [KISS](https://en.wikipedia.org/wiki/KISS_principle) :)

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/readme.md
# ![RealWorld Example App](logo.png)


[![Build Status](https://travis-ci.org/wangzitian0/golang-gin-realworld-example-app.svg?branch=master)](https://travis-ci.org/wangzitian0/golang-gin-realworld-example-app)
[![codecov](https://codecov.io/gh/wangzitian0/golang-gin-realworld-example-app/branch/master/graph/badge.svg)](https://codecov.io/gh/wangzitian0/golang-gin-realworld-example-app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/gothinkster/golang-gin-realworld-example-app/blob/master/LICENSE)
[![GoDoc](https://godoc.org/github.com/gothinkster/golang-gin-realworld-example-app?status.svg)](https://godoc.org/github.com/gothinkster/golang-gin-realworld-example-app)

> ### Golang/Gin codebase containing real world examples (CRUD, auth, advanced patterns, etc) that adheres to the [RealWorld](https://github.com/gothinkster/realworld) spec and API.


This codebase was created to demonstrate a fully fledged fullstack application built with **Golang/Gin** including CRUD operations, authentication, routing, pagination, and more.


# Directory structure
```
.
├── gorm.db
├── hello.go
├── common
│   ├── utils.go        //small tools function
│   └── database.go     //DB connect manager
├── users
|   ├── models.go       //data models define & DB operation
|   ├── serializers.go  //response computing & format
|   ├── routers.go      //business logic & router binding
|   ├── middlewares.go  //put the before & after logic of handle request
|   └── validators.go   //form/json checker
├── ...
...
```

# Getting started

## Install Golang

Make sure you have Go 1.13 or higher installed.

https://golang.org/doc/install

## Environment Config

Set-up the standard Go environment variables according to latest guidance (see https://golang.org/doc/install#install).


## Install Dependencies
From the project root, run:
```
go build ./...
go test ./...
go mod tidy
```

## Testing
From the project root, run:
```
go test ./...
```
or
```
go test ./... -cover
```
or
```
go test -v ./... -cover
```
depending on whether you want to see test coverage and how verbose the output you want.

## Todo
- More elegance config
- Test coverage (common & users 100%, article 0%)
- ProtoBuf support
- Code structure optimize (I think some place can use interface)
- Continuous integration (done)

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/articles/doc.go
/*
The article module containing the article CRUD operation and relationship CRUD.

model.go: definition of orm based data model

routers.go: router binding and core logic

serializers.go: definition the schema of return data

validators.go: definition the validator of form data
*/
package articles

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/articles/models.go
package articles

import (
	_ "fmt"
	"github.com/jinzhu/gorm"
	"github.com/gothinkster/golang-gin-realworld-example-app/common"
	"github.com/gothinkster/golang-gin-realworld-example-app/users"
	"strconv"
)

type ArticleModel struct {
	gorm.Model
	Slug        string `gorm:"unique_index"`
	Title       string
	Description string `gorm:"size:2048"`
	Body        string `gorm:"size:2048"`
	Author      ArticleUserModel
	AuthorID    uint
	Tags        []TagModel     `gorm:"many2many:article_tags;"`
	Comments    []CommentModel `gorm:"ForeignKey:ArticleID"`
}

type ArticleUserModel struct {
	gorm.Model
	UserModel      users.UserModel
	UserModelID    uint
	ArticleModels  []ArticleModel  `gorm:"ForeignKey:AuthorID"`
	FavoriteModels []FavoriteModel `gorm:"ForeignKey:FavoriteByID"`
}

type FavoriteModel struct {
	gorm.Model
	Favorite     ArticleModel
	FavoriteID   uint
	FavoriteBy   ArticleUserModel
	FavoriteByID uint
}

type TagModel struct {
	gorm.Model
	Tag           string         `gorm:"unique_index"`
	ArticleModels []ArticleModel `gorm:"many2many:article_tags;"`
}

type CommentModel struct {
	gorm.Model
	Article   ArticleModel
	ArticleID uint
	Author    ArticleUserModel
	AuthorID  uint
	Body      string `gorm:"size:2048"`
}

func GetArticleUserModel(userModel users.UserModel) ArticleUserModel {
	var articleUserModel ArticleUserModel
	if userModel.ID == 0 {
		return articleUserModel
	}
	db := common.GetDB()
	db.Where(&ArticleUserModel{
		UserModelID: userModel.ID,
	}).FirstOrCreate(&articleUserModel)
	articleUserModel.UserModel = userModel
	return articleUserModel
}

func (article ArticleModel) favoritesCount() uint {
	db := common.GetDB()
	var count uint
	db.Model(&FavoriteModel{}).Where(FavoriteModel{
		FavoriteID: article.ID,
	}).Count(&count)
	return count
}

func (article ArticleModel) isFavoriteBy(user ArticleUserModel) bool {
	db := common.GetDB()
	var favorite FavoriteModel
	db.Where(FavoriteModel{
		FavoriteID:   article.ID,
		FavoriteByID: user.ID,
	}).First(&favorite)
	return favorite.ID != 0
}

func (article ArticleModel) favoriteBy(user ArticleUserModel) error {
	db := common.GetDB()
	var favorite FavoriteModel
	err := db.FirstOrCreate(&favorite, &FavoriteModel{
		FavoriteID:   article.ID,
		FavoriteByID: user.ID,
	}).Error
	return err
}

func (article ArticleModel) unFavoriteBy(user ArticleUserModel) error {
	db := common.GetDB()
	err := db.Where(FavoriteModel{
		FavoriteID:   article.ID,
		FavoriteByID: user.ID,
	}).Delete(FavoriteModel{}).Error
	return err
}

func SaveOne(data interface{}) error {
	db := common.GetDB()
	err := db.Save(data).Error
	return err
}

func FindOneArticle(condition interface{}) (ArticleModel, error) {
	db := common.GetDB()
	var model ArticleModel
	tx := db.Begin()
	tx.Where(condition).First(&model)
	tx.Model(&model).Related(&model.Author, "Author")
	tx.Model(&model.Author).Related(&model.Author.UserModel)
	tx.Model(&model).Related(&model.Tags, "Tags")
	err := tx.Commit().Error
	return model, err
}

func (self *ArticleModel) getComments() error {
	db := common.GetDB()
	tx := db.Begin()
	tx.Model(self).Related(&self.Comments, "Comments")
	for i, _ := range self.Comments {
		tx.Model(&self.Comments[i]).Related(&self.Comments[i].Author, "Author")
		tx.Model(&self.Comments[i].Author).Related(&self.Comments[i].Author.UserModel)
	}
	err := tx.Commit().Error
	return err
}

func getAllTags() ([]TagModel, error) {
	db := common.GetDB()
	var models []TagModel
	err := db.Find(&models).Error
	return models, err
}

func FindManyArticle(tag, author, limit, offset, favorited string) ([]ArticleModel, int, error) {
	db := common.GetDB()
	var models []ArticleModel
	var count int

	offset_int, err := strconv.Atoi(offset)
	if err != nil {
		offset_int = 0
	}

	limit_int, err := strconv.Atoi(limit)
	if err != nil {
		limit_int = 20
	}

	tx := db.Begin()
	if tag != "" {
		var tagModel TagModel
		tx.Where(TagModel{Tag: tag}).First(&tagModel)
		if tagModel.ID != 0 {
			tx.Model(&tagModel).Offset(offset_int).Limit(limit_int).Related(&models, "ArticleModels")
			count = tx.Model(&tagModel).Association("ArticleModels").Count()
		}
	} else if author != "" {
		var userModel users.UserModel
		tx.Where(users.UserModel{Username: author}).First(&userModel)
		articleUserModel := GetArticleUserModel(userModel)

		if articleUserModel.ID != 0 {
			count = tx.Model(&articleUserModel).Association("ArticleModels").Count()
			tx.Model(&articleUserModel).Offset(offset_int).Limit(limit_int).Related(&models, "ArticleModels")
		}
	} else if favorited != "" {
		var userModel users.UserModel
		tx.Where(users.UserModel{Username: favorited}).First(&userModel)
		articleUserModel := GetArticleUserModel(userModel)
		if articleUserModel.ID != 0 {
			var favoriteModels []FavoriteModel
			tx.Where(FavoriteModel{
				FavoriteByID: articleUserModel.ID,
			}).Offset(offset_int).Limit(limit_int).Find(&favoriteModels)

			count = tx.Model(&articleUserModel).Association("FavoriteModels").Count()
			for _, favorite := range favoriteModels {
				var model ArticleModel
				tx.Model(&favorite).Related(&model, "Favorite")
				models = append(models, model)
			}
		}
	} else {
		db.Model(&models).Count(&count)
		db.Offset(offset_int).Limit(limit_int).Find(&models)
	}

	for i, _ := range models {
		tx.Model(&models[i]).Related(&models[i].Author, "Author")
		tx.Model(&models[i].Author).Related(&models[i].Author.UserModel)
		tx.Model(&models[i]).Related(&models[i].Tags, "Tags")
	}
	err = tx.Commit().Error
	return models, count, err
}

func (self *ArticleUserModel) GetArticleFeed(limit, offset string) ([]ArticleModel, int, error) {
	db := common.GetDB()
	var models []ArticleModel
	var count int

	offset_int, err := strconv.Atoi(offset)
	if err != nil {
		offset_int = 0
	}
	limit_int, err := strconv.Atoi(limit)
	if err != nil {
		limit_int = 20
	}

	tx := db.Begin()
	followings := self.UserModel.GetFollowings()
	var articleUserModels []uint
	for _, following := range followings {
		articleUserModel := GetArticleUserModel(following)
		articleUserModels = append(articleUserModels, articleUserModel.ID)
	}

	tx.Where("author_id in (?)", articleUserModels).Order("updated_at desc").Offset(offset_int).Limit(limit_int).Find(&models)

	for i, _ := range models {
		tx.Model(&models[i]).Related(&models[i].Author, "Author")
		tx.Model(&models[i].Author).Related(&models[i].Author.UserModel)
		tx.Model(&models[i]).Related(&models[i].Tags, "Tags")
	}
	err = tx.Commit().Error
	return models, count, err
}

func (model *ArticleModel) setTags(tags []string) error {
	db := common.GetDB()
	var tagList []TagModel
	for _, tag := range tags {
		var tagModel TagModel
		err := db.FirstOrCreate(&tagModel, TagModel{Tag: tag}).Error
		if err != nil {
			return err
		}
		tagList = append(tagList, tagModel)
	}
	model.Tags = tagList
	return nil
}

func (model *ArticleModel) Update(data interface{}) error {
	db := common.GetDB()
	err := db.Model(model).Update(data).Error
	return err
}

func DeleteArticleModel(condition interface{}) error {
	db := common.GetDB()
	err := db.Where(condition).Delete(ArticleModel{}).Error
	return err
}

func DeleteCommentModel(condition interface{}) error {
	db := common.GetDB()
	err := db.Where(condition).Delete(CommentModel{}).Error
	return err
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/articles/routers.go
package articles

import (
	"errors"
	"github.com/gothinkster/golang-gin-realworld-example-app/common"
	"github.com/gothinkster/golang-gin-realworld-example-app/users"
	"github.com/gin-gonic/gin"
	"net/http"
	"strconv"
)

func ArticlesRegister(router *gin.RouterGroup) {
	router.POST("/", ArticleCreate)
	router.PUT("/:slug", ArticleUpdate)
	router.DELETE("/:slug", ArticleDelete)
	router.POST("/:slug/favorite", ArticleFavorite)
	router.DELETE("/:slug/favorite", ArticleUnfavorite)
	router.POST("/:slug/comments", ArticleCommentCreate)
	router.DELETE("/:slug/comments/:id", ArticleCommentDelete)
}

func ArticlesAnonymousRegister(router *gin.RouterGroup) {
	router.GET("/", ArticleList)
	router.GET("/:slug", ArticleRetrieve)
	router.GET("/:slug/comments", ArticleCommentList)
}

func TagsAnonymousRegister(router *gin.RouterGroup) {
	router.GET("/", TagList)
}

func ArticleCreate(c *gin.Context) {
	articleModelValidator := NewArticleModelValidator()
	if err := articleModelValidator.Bind(c); err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewValidatorError(err))
		return
	}
	//fmt.Println(articleModelValidator.articleModel.Author.UserModel)

	if err := SaveOne(&articleModelValidator.articleModel); err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewError("database", err))
		return
	}
	serializer := ArticleSerializer{c, articleModelValidator.articleModel}
	c.JSON(http.StatusCreated, gin.H{"article": serializer.Response()})
}

func ArticleList(c *gin.Context) {
	//condition := ArticleModel{}
	tag := c.Query("tag")
	author := c.Query("author")
	favorited := c.Query("favorited")
	limit := c.Query("limit")
	offset := c.Query("offset")
	articleModels, modelCount, err := FindManyArticle(tag, author, limit, offset, favorited)
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("articles", errors.New("Invalid param")))
		return
	}
	serializer := ArticlesSerializer{c, articleModels}
	c.JSON(http.StatusOK, gin.H{"articles": serializer.Response(), "articlesCount": modelCount})
}

func ArticleFeed(c *gin.Context) {
	limit := c.Query("limit")
	offset := c.Query("offset")
	myUserModel := c.MustGet("my_user_model").(users.UserModel)
	if myUserModel.ID == 0 {
		c.AbortWithError(http.StatusUnauthorized, errors.New("{error : \"Require auth!\"}"))
		return
	}
	articleUserModel := GetArticleUserModel(myUserModel)
	articleModels, modelCount, err := articleUserModel.GetArticleFeed(limit, offset)
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("articles", errors.New("Invalid param")))
		return
	}
	serializer := ArticlesSerializer{c, articleModels}
	c.JSON(http.StatusOK, gin.H{"articles": serializer.Response(), "articlesCount": modelCount})
}

func ArticleRetrieve(c *gin.Context) {
	slug := c.Param("slug")
	if slug == "feed" {
		ArticleFeed(c)
		return
	}
	articleModel, err := FindOneArticle(&ArticleModel{Slug: slug})
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("articles", errors.New("Invalid slug")))
		return
	}
	serializer := ArticleSerializer{c, articleModel}
	c.JSON(http.StatusOK, gin.H{"article": serializer.Response()})
}

func ArticleUpdate(c *gin.Context) {
	slug := c.Param("slug")
	articleModel, err := FindOneArticle(&ArticleModel{Slug: slug})
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("articles", errors.New("Invalid slug")))
		return
	}
	articleModelValidator := NewArticleModelValidatorFillWith(articleModel)
	if err := articleModelValidator.Bind(c); err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewValidatorError(err))
		return
	}

	articleModelValidator.articleModel.ID = articleModel.ID
	if err := articleModel.Update(articleModelValidator.articleModel); err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewError("database", err))
		return
	}
	serializer := ArticleSerializer{c, articleModel}
	c.JSON(http.StatusOK, gin.H{"article": serializer.Response()})
}

func ArticleDelete(c *gin.Context) {
	slug := c.Param("slug")
	err := DeleteArticleModel(&ArticleModel{Slug: slug})
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("articles", errors.New("Invalid slug")))
		return
	}
	c.JSON(http.StatusOK, gin.H{"article": "Delete success"})
}

func ArticleFavorite(c *gin.Context) {
	slug := c.Param("slug")
	articleModel, err := FindOneArticle(&ArticleModel{Slug: slug})
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("articles", errors.New("Invalid slug")))
		return
	}
	myUserModel := c.MustGet("my_user_model").(users.UserModel)
	err = articleModel.favoriteBy(GetArticleUserModel(myUserModel))
	serializer := ArticleSerializer{c, articleModel}
	c.JSON(http.StatusOK, gin.H{"article": serializer.Response()})
}

func ArticleUnfavorite(c *gin.Context) {
	slug := c.Param("slug")
	articleModel, err := FindOneArticle(&ArticleModel{Slug: slug})
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("articles", errors.New("Invalid slug")))
		return
	}
	myUserModel := c.MustGet("my_user_model").(users.UserModel)
	err = articleModel.unFavoriteBy(GetArticleUserModel(myUserModel))
	serializer := ArticleSerializer{c, articleModel}
	c.JSON(http.StatusOK, gin.H{"article": serializer.Response()})
}

func ArticleCommentCreate(c *gin.Context) {
	slug := c.Param("slug")
	articleModel, err := FindOneArticle(&ArticleModel{Slug: slug})
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("comment", errors.New("Invalid slug")))
		return
	}
	commentModelValidator := NewCommentModelValidator()
	if err := commentModelValidator.Bind(c); err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewValidatorError(err))
		return
	}
	commentModelValidator.commentModel.Article = articleModel

	if err := SaveOne(&commentModelValidator.commentModel); err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewError("database", err))
		return
	}
	serializer := CommentSerializer{c, commentModelValidator.commentModel}
	c.JSON(http.StatusCreated, gin.H{"comment": serializer.Response()})
}

func ArticleCommentDelete(c *gin.Context) {
	id64, err := strconv.ParseUint(c.Param("id"), 10, 32)
	id := uint(id64)
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("comment", errors.New("Invalid id")))
		return
	}
	err = DeleteCommentModel([]uint{id})
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("comment", errors.New("Invalid id")))
		return
	}
	c.JSON(http.StatusOK, gin.H{"comment": "Delete success"})
}

func ArticleCommentList(c *gin.Context) {
	slug := c.Param("slug")
	articleModel, err := FindOneArticle(&ArticleModel{Slug: slug})
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("comments", errors.New("Invalid slug")))
		return
	}
	err = articleModel.getComments()
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("comments", errors.New("Database error")))
		return
	}
	serializer := CommentsSerializer{c, articleModel.Comments}
	c.JSON(http.StatusOK, gin.H{"comments": serializer.Response()})
}
func TagList(c *gin.Context) {
	tagModels, err := getAllTags()
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("articles", errors.New("Invalid param")))
		return
	}
	serializer := TagsSerializer{c, tagModels}
	c.JSON(http.StatusOK, gin.H{"tags": serializer.Response()})
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/articles/serializers.go
package articles

import (
	"github.com/gosimple/slug"
	"github.com/gothinkster/golang-gin-realworld-example-app/users"
	"github.com/gin-gonic/gin"
)

type TagSerializer struct {
	C *gin.Context
	TagModel
}

type TagsSerializer struct {
	C    *gin.Context
	Tags []TagModel
}

func (s *TagSerializer) Response() string {
	return s.TagModel.Tag
}

func (s *TagsSerializer) Response() []string {
	response := []string{}
	for _, tag := range s.Tags {
		serializer := TagSerializer{s.C, tag}
		response = append(response, serializer.Response())
	}
	return response
}

type ArticleUserSerializer struct {
	C *gin.Context
	ArticleUserModel
}

func (s *ArticleUserSerializer) Response() users.ProfileResponse {
	response := users.ProfileSerializer{s.C, s.ArticleUserModel.UserModel}
	return response.Response()
}

type ArticleSerializer struct {
	C *gin.Context
	ArticleModel
}

type ArticleResponse struct {
	ID             uint                  `json:"-"`
	Title          string                `json:"title"`
	Slug           string                `json:"slug"`
	Description    string                `json:"description"`
	Body           string                `json:"body"`
	CreatedAt      string                `json:"createdAt"`
	UpdatedAt      string                `json:"updatedAt"`
	Author         users.ProfileResponse `json:"author"`
	Tags           []string              `json:"tagList"`
	Favorite       bool                  `json:"favorited"`
	FavoritesCount uint                  `json:"favoritesCount"`
}

type ArticlesSerializer struct {
	C        *gin.Context
	Articles []ArticleModel
}

func (s *ArticleSerializer) Response() ArticleResponse {
	myUserModel := s.C.MustGet("my_user_model").(users.UserModel)
	authorSerializer := ArticleUserSerializer{s.C, s.Author}
	response := ArticleResponse{
		ID:          s.ID,
		Slug:        slug.Make(s.Title),
		Title:       s.Title,
		Description: s.Description,
		Body:        s.Body,
		CreatedAt:   s.CreatedAt.UTC().Format("2006-01-02T15:04:05.999Z"),
		//UpdatedAt:      s.UpdatedAt.UTC().Format(time.RFC3339Nano),
		UpdatedAt:      s.UpdatedAt.UTC().Format("2006-01-02T15:04:05.999Z"),
		Author:         authorSerializer.Response(),
		Favorite:       s.isFavoriteBy(GetArticleUserModel(myUserModel)),
		FavoritesCount: s.favoritesCount(),
	}
	response.Tags = make([]string, 0)
	for _, tag := range s.Tags {
		serializer := TagSerializer{s.C, tag}
		response.Tags = append(response.Tags, serializer.Response())
	}
	return response
}

func (s *ArticlesSerializer) Response() []ArticleResponse {
	response := []ArticleResponse{}
	for _, article := range s.Articles {
		serializer := ArticleSerializer{s.C, article}
		response = append(response, serializer.Response())
	}
	return response
}

type CommentSerializer struct {
	C *gin.Context
	CommentModel
}

type CommentsSerializer struct {
	C        *gin.Context
	Comments []CommentModel
}

type CommentResponse struct {
	ID        uint                  `json:"id"`
	Body      string                `json:"body"`
	CreatedAt string                `json:"createdAt"`
	UpdatedAt string                `json:"updatedAt"`
	Author    users.ProfileResponse `json:"author"`
}

func (s *CommentSerializer) Response() CommentResponse {
	authorSerializer := ArticleUserSerializer{s.C, s.Author}
	response := CommentResponse{
		ID:        s.ID,
		Body:      s.Body,
		CreatedAt: s.CreatedAt.UTC().Format("2006-01-02T15:04:05.999Z"),
		UpdatedAt: s.UpdatedAt.UTC().Format("2006-01-02T15:04:05.999Z"),
		Author:    authorSerializer.Response(),
	}
	return response
}

func (s *CommentsSerializer) Response() []CommentResponse {
	response := []CommentResponse{}
	for _, comment := range s.Comments {
		serializer := CommentSerializer{s.C, comment}
		response = append(response, serializer.Response())
	}
	return response
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/articles/validators.go
package articles

import (
	"github.com/gosimple/slug"
	"github.com/gothinkster/golang-gin-realworld-example-app/common"
	"github.com/gothinkster/golang-gin-realworld-example-app/users"
	"github.com/gin-gonic/gin"
)

type ArticleModelValidator struct {
	Article struct {
		Title       string   `form:"title" json:"title" binding:"exists,min=4"`
		Description string   `form:"description" json:"description" binding:"max=2048"`
		Body        string   `form:"body" json:"body" binding:"max=2048"`
		Tags        []string `form:"tagList" json:"tagList"`
	} `json:"article"`
	articleModel ArticleModel `json:"-"`
}

func NewArticleModelValidator() ArticleModelValidator {
	return ArticleModelValidator{}
}

func NewArticleModelValidatorFillWith(articleModel ArticleModel) ArticleModelValidator {
	articleModelValidator := NewArticleModelValidator()
	articleModelValidator.Article.Title = articleModel.Title
	articleModelValidator.Article.Description = articleModel.Description
	articleModelValidator.Article.Body = articleModel.Body
	for _, tagModel := range articleModel.Tags {
		articleModelValidator.Article.Tags = append(articleModelValidator.Article.Tags, tagModel.Tag)
	}
	return articleModelValidator
}

func (s *ArticleModelValidator) Bind(c *gin.Context) error {
	myUserModel := c.MustGet("my_user_model").(users.UserModel)

	err := common.Bind(c, s)
	if err != nil {
		return err
	}
	s.articleModel.Slug = slug.Make(s.Article.Title)
	s.articleModel.Title = s.Article.Title
	s.articleModel.Description = s.Article.Description
	s.articleModel.Body = s.Article.Body
	s.articleModel.Author = GetArticleUserModel(myUserModel)
	s.articleModel.setTags(s.Article.Tags)
	return nil
}

type CommentModelValidator struct {
	Comment struct {
		Body string `form:"body" json:"body" binding:"max=2048"`
	} `json:"comment"`
	commentModel CommentModel `json:"-"`
}

func NewCommentModelValidator() CommentModelValidator {
	return CommentModelValidator{}
}

func (s *CommentModelValidator) Bind(c *gin.Context) error {
	myUserModel := c.MustGet("my_user_model").(users.UserModel)

	err := common.Bind(c, s)
	if err != nil {
		return err
	}
	s.commentModel.Body = s.Comment.Body
	s.commentModel.Author = GetArticleUserModel(myUserModel)
	return nil
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/common/database.go
package common

import (
	"fmt"
	"github.com/jinzhu/gorm"
	_ "github.com/jinzhu/gorm/dialects/sqlite"
	"os"
)

type Database struct {
	*gorm.DB
}

var DB *gorm.DB

// Opening a database and save the reference to `Database` struct.
func Init() *gorm.DB {
	db, err := gorm.Open("sqlite3", "./../gorm.db")
	if err != nil {
		fmt.Println("db err: (Init) ", err)
	}
	db.DB().SetMaxIdleConns(10)
	//db.LogMode(true)
	DB = db
	return DB
}

// This function will create a temporarily database for running testing cases
func TestDBInit() *gorm.DB {
	test_db, err := gorm.Open("sqlite3", "./../gorm_test.db")
	if err != nil {
		fmt.Println("db err: (TestDBInit) ", err)
	}
	test_db.DB().SetMaxIdleConns(3)
	test_db.LogMode(true)
	DB = test_db
	return DB
}

// Delete the database after running testing cases.
func TestDBFree(test_db *gorm.DB) error {
	test_db.Close()
	err := os.Remove("./../gorm_test.db")
	return err
}

// Using this function to get a connection, you can create your connection pool here.
func GetDB() *gorm.DB {
	return DB
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/common/unit_test.go
package common

import (
	"bytes"
	"errors"
	"github.com/stretchr/testify/assert"
	"github.com/gin-gonic/gin"
	"net/http"
	"net/http/httptest"
	"os"
	"testing"
)

func TestConnectingDatabase(t *testing.T) {
	asserts := assert.New(t)
	db := Init()
	// Test create & close DB
	_, err := os.Stat("./../gorm.db")
	asserts.NoError(err, "Db should exist")
	asserts.NoError(db.DB().Ping(), "Db should be able to ping")

	// Test get a connecting from connection pools
	connection := GetDB()
	asserts.NoError(connection.DB().Ping(), "Db should be able to ping")
	db.Close()

	// Test DB exceptions
	os.Chmod("./../gorm.db", 0000)
	db = Init()
	asserts.Error(db.DB().Ping(), "Db should not be able to ping")
	db.Close()
	os.Chmod("./../gorm.db", 0644)
}

func TestConnectingTestDatabase(t *testing.T) {
	asserts := assert.New(t)
	// Test create & close DB
	db := TestDBInit()
	_, err := os.Stat("./../gorm_test.db")
	asserts.NoError(err, "Db should exist")
	asserts.NoError(db.DB().Ping(), "Db should be able to ping")
	db.Close()

	// Test testDB exceptions
	os.Chmod("./../gorm_test.db", 0000)
	db = TestDBInit()
	_, err = os.Stat("./../gorm_test.db")
	asserts.NoError(err, "Db should exist")
	asserts.Error(db.DB().Ping(), "Db should not be able to ping")
	os.Chmod("./../gorm_test.db", 0644)

	// Test close delete DB
	TestDBFree(db)
	_, err = os.Stat("./../gorm_test.db")

	asserts.Error(err, "Db should not exist")
}

func TestRandString(t *testing.T) {
	asserts := assert.New(t)

	var letters = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
	str := RandString(0)
	asserts.Equal(str, "", "length should be ''")

	str = RandString(10)
	asserts.Equal(len(str), 10, "length should be 10")
	for _, ch := range str {
		asserts.Contains(letters, ch, "char should be a-z|A-Z|0-9")
	}
}

func TestGenToken(t *testing.T) {
	asserts := assert.New(t)

	token := GenToken(2)

	asserts.IsType(token, string("token"), "token type should be string")
	asserts.Len(token, 115, "JWT's length should be 115")
}

func TestNewValidatorError(t *testing.T) {
	asserts := assert.New(t)

	type Login struct {
		Username string `form:"username" json:"username" binding:"exists,alphanum,min=4,max=255"`
		Password string `form:"password" json:"password" binding:"exists,min=8,max=255"`
	}

	var requestTests = []struct {
		bodyData       string
		expectedCode   int
		responseRegexg string
		msg            string
	}{
		{
			`{"username": "wangzitian0","password": "0123456789"}`,
			http.StatusOK,
			`{"status":"you are logged in"}`,
			"valid data and should return StatusCreated",
		},
		{
			`{"username": "wangzitian0","password": "01234567866"}`,
			http.StatusUnauthorized,
			`{"errors":{"user":"wrong username or password"}}`,
			"wrong login status should return StatusUnauthorized",
		},
		{
			`{"username": "wangzitian0","password": "0122"}`,
			http.StatusUnprocessableEntity,
			`{"errors":{"Password":"{min: 8}"}}`,
			"invalid password of too short and should return StatusUnprocessableEntity",
		},
		{
			`{"username": "_wangzitian0","password": "0123456789"}`,
			http.StatusUnprocessableEntity,
			`{"errors":{"Username":"{key: alphanum}"}}`,
			"invalid username of non alphanum and should return StatusUnprocessableEntity",
		},
	}

	r := gin.Default()

	r.POST("/login", func(c *gin.Context) {
		var json Login
		if err := Bind(c, &json); err == nil {
			if json.Username == "wangzitian0" && json.Password == "0123456789" {
				c.JSON(http.StatusOK, gin.H{"status": "you are logged in"})
			} else {
				c.JSON(http.StatusUnauthorized, NewError("user", errors.New("wrong username or password")))
			}
		} else {
			c.JSON(http.StatusUnprocessableEntity, NewValidatorError(err))
		}
	})

	for _, testData := range requestTests {
		bodyData := testData.bodyData
		req, err := http.NewRequest("POST", "/login", bytes.NewBufferString(bodyData))
		req.Header.Set("Content-Type", "application/json")
		asserts.NoError(err)

		w := httptest.NewRecorder()
		r.ServeHTTP(w, req)

		asserts.Equal(testData.expectedCode, w.Code, "Response Status - "+testData.msg)
		asserts.Regexp(testData.responseRegexg, w.Body.String(), "Response Content - "+testData.msg)
	}
}

func TestNewError(t *testing.T) {
	assert := assert.New(t)

	db := TestDBInit()
	type NotExist struct {
		heheda string
	}
	db.AutoMigrate(NotExist{})

	commenError := NewError("database", db.Find(NotExist{heheda: "heheda"}).Error)
	assert.IsType(commenError, commenError, "commenError should have right type")
	assert.Equal(map[string]interface{}(map[string]interface{}{"database": "no such table: not_exists"}),
		commenError.Errors, "commenError should have right error info")
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/common/utils.go
// Common tools and helper functions
package common

import (
	"fmt"
	"math/rand"
	"time"

	"github.com/dgrijalva/jwt-go"
	"gopkg.in/go-playground/validator.v8"

	"github.com/gin-gonic/gin/binding"
	"github.com/gin-gonic/gin"
)

var letters = []rune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")

// A helper function to generate random string
func RandString(n int) string {
	b := make([]rune, n)
	for i := range b {
		b[i] = letters[rand.Intn(len(letters))]
	}
	return string(b)
}

// Keep this two config private, it should not expose to open source
const NBSecretPassword = "A String Very Very Very Strong!!@##$!@#$"
const NBRandomPassword = "A String Very Very Very Niubilty!!@##$!@#4"

// A Util function to generate jwt_token which can be used in the request header
func GenToken(id uint) string {
	jwt_token := jwt.New(jwt.GetSigningMethod("HS256"))
	// Set some claims
	jwt_token.Claims = jwt.MapClaims{
		"id":  id,
		"exp": time.Now().Add(time.Hour * 24).Unix(),
	}
	// Sign and get the complete encoded token as a string
	token, _ := jwt_token.SignedString([]byte(NBSecretPassword))
	return token
}

// My own Error type that will help return my customized Error info
//  {"database": {"hello":"no such table", error: "not_exists"}}
type CommonError struct {
	Errors map[string]interface{} `json:"errors"`
}

// To handle the error returned by c.Bind in gin framework
// https://github.com/go-playground/validator/blob/v9/_examples/translations/main.go
func NewValidatorError(err error) CommonError {
	res := CommonError{}
	res.Errors = make(map[string]interface{})
	errs := err.(validator.ValidationErrors)
	for _, v := range errs {
		// can translate each error one at a time.
		//fmt.Println("gg",v.NameNamespace)
		if v.Param != "" {
			res.Errors[v.Field] = fmt.Sprintf("{%v: %v}", v.Tag, v.Param)
		} else {
			res.Errors[v.Field] = fmt.Sprintf("{key: %v}", v.Tag)
		}

	}
	return res
}

// Warp the error info in a object
func NewError(key string, err error) CommonError {
	res := CommonError{}
	res.Errors = make(map[string]interface{})
	res.Errors[key] = err.Error()
	return res
}

// Changed the c.MustBindWith() ->  c.ShouldBindWith().
// I don't want to auto return 400 when error happened.
// origin function is here: https://github.com/gin-gonic/gin/blob/master/context.go
func Bind(c *gin.Context, obj interface{}) error {
	b := binding.Default(c.Request.Method, c.ContentType())
	return c.ShouldBindWith(obj, b)
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/scripts/coverage.sh
#!/usr/bin/env bash

set -e

# http://stackoverflow.com/a/21142256/2055281

echo "mode: atomic" > coverage.txt

for d in $(find ./* -maxdepth 10 -type d); do
    if ls $d/*.go &> /dev/null; then
        go test  -coverprofile=profile.out -covermode=atomic $d
        if [ -f profile.out ]; then
            echo "$(pwd)"
            cat profile.out | grep -v "mode: " >> coverage.txt
            rm profile.out
        fi
    fi
done


--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/scripts/gofmt.sh
#!/bin/bash

gofmt=$(govendor fmt +l)
echo $gofmt

if [ ${#gofmt} != 0 ]; then
    echo "There is unformatted code, you should use `go fmt ./\.\.\.` to format it."
    exit 1
else
    echo "Codes are formatted."
    exit 0
fi

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/doc.go
/*
The user module containing the user CRU operation.

model.go: definition of orm based data model

routers.go: router binding and core logic

serializers.go: definition the schema of return data

validators.go: definition the validator of form data
*/
package users

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/middlewares.go
package users

import (
	"github.com/dgrijalva/jwt-go"
	"github.com/dgrijalva/jwt-go/request"
	"github.com/gothinkster/golang-gin-realworld-example-app/common"
	"github.com/gin-gonic/gin"
	"net/http"
	"strings"
)

// Strips 'TOKEN ' prefix from token string
func stripBearerPrefixFromTokenString(tok string) (string, error) {
	// Should be a bearer token
	if len(tok) > 5 && strings.ToUpper(tok[0:6]) == "TOKEN " {
		return tok[6:], nil
	}
	return tok, nil
}

// Extract  token from Authorization header
// Uses PostExtractionFilter to strip "TOKEN " prefix from header
var AuthorizationHeaderExtractor = &request.PostExtractionFilter{
	request.HeaderExtractor{"Authorization"},
	stripBearerPrefixFromTokenString,
}

// Extractor for OAuth2 access tokens.  Looks in 'Authorization'
// header then 'access_token' argument for a token.
var MyAuth2Extractor = &request.MultiExtractor{
	AuthorizationHeaderExtractor,
	request.ArgumentExtractor{"access_token"},
}

// A helper to write user_id and user_model to the context
func UpdateContextUserModel(c *gin.Context, my_user_id uint) {
	var myUserModel UserModel
	if my_user_id != 0 {
		db := common.GetDB()
		db.First(&myUserModel, my_user_id)
	}
	c.Set("my_user_id", my_user_id)
	c.Set("my_user_model", myUserModel)
}

// You can custom middlewares yourself as the doc: https://github.com/gin-gonic/gin#custom-middleware
//  r.Use(AuthMiddleware(true))
func AuthMiddleware(auto401 bool) gin.HandlerFunc {
	return func(c *gin.Context) {
		UpdateContextUserModel(c, 0)
		token, err := request.ParseFromRequest(c.Request, MyAuth2Extractor, func(token *jwt.Token) (interface{}, error) {
			b := ([]byte(common.NBSecretPassword))
			return b, nil
		})
		if err != nil {
			if auto401 {
				c.AbortWithError(http.StatusUnauthorized, err)
			}
			return
		}
		if claims, ok := token.Claims.(jwt.MapClaims); ok && token.Valid {
			my_user_id := uint(claims["id"].(float64))
			//fmt.Println(my_user_id,claims["id"])
			UpdateContextUserModel(c, my_user_id)
		}
	}
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/models.go
package users

import (
	"errors"
	"github.com/jinzhu/gorm"
	"github.com/gothinkster/golang-gin-realworld-example-app/common"
	"golang.org/x/crypto/bcrypt"
)

// Models should only be concerned with database schema, more strict checking should be put in validator.
//
// More detail you can find here: http://jinzhu.me/gorm/models.html#model-definition
//
// HINT: If you want to split null and "", you should use *string instead of string.
type UserModel struct {
	ID           uint    `gorm:"primary_key"`
	Username     string  `gorm:"column:username"`
	Email        string  `gorm:"column:email;unique_index"`
	Bio          string  `gorm:"column:bio;size:1024"`
	Image        *string `gorm:"column:image"`
	PasswordHash string  `gorm:"column:password;not null"`
}

// A hack way to save ManyToMany relationship,
// gorm will build the alias as FollowingBy <-> FollowingByID <-> "following_by_id".
//
// DB schema looks like: id, created_at, updated_at, deleted_at, following_id, followed_by_id.
//
// Retrieve them by:
// 	db.Where(FollowModel{ FollowingID:  v.ID, FollowedByID: u.ID, }).First(&follow)
// 	db.Where(FollowModel{ FollowedByID: u.ID, }).Find(&follows)
//
// More details about gorm.Model: http://jinzhu.me/gorm/models.html#conventions
type FollowModel struct {
	gorm.Model
	Following    UserModel
	FollowingID  uint
	FollowedBy   UserModel
	FollowedByID uint
}

// Migrate the schema of database if needed
func AutoMigrate() {
	db := common.GetDB()

	db.AutoMigrate(&UserModel{})
	db.AutoMigrate(&FollowModel{})
}

// What's bcrypt? https://en.wikipedia.org/wiki/Bcrypt
// Golang bcrypt doc: https://godoc.org/golang.org/x/crypto/bcrypt
// You can change the value in bcrypt.DefaultCost to adjust the security index.
// 	err := userModel.setPassword("password0")
func (u *UserModel) setPassword(password string) error {
	if len(password) == 0 {
		return errors.New("password should not be empty!")
	}
	bytePassword := []byte(password)
	// Make sure the second param `bcrypt generator cost` between [4, 32)
	passwordHash, _ := bcrypt.GenerateFromPassword(bytePassword, bcrypt.DefaultCost)
	u.PasswordHash = string(passwordHash)
	return nil
}

// Database will only save the hashed string, you should check it by util function.
// 	if err := serModel.checkPassword("password0"); err != nil { password error }
func (u *UserModel) checkPassword(password string) error {
	bytePassword := []byte(password)
	byteHashedPassword := []byte(u.PasswordHash)
	return bcrypt.CompareHashAndPassword(byteHashedPassword, bytePassword)
}

// You could input the conditions and it will return an UserModel in database with error info.
// 	userModel, err := FindOneUser(&UserModel{Username: "username0"})
func FindOneUser(condition interface{}) (UserModel, error) {
	db := common.GetDB()
	var model UserModel
	err := db.Where(condition).First(&model).Error
	return model, err
}

// You could input an UserModel which will be saved in database returning with error info
// 	if err := SaveOne(&userModel); err != nil { ... }
func SaveOne(data interface{}) error {
	db := common.GetDB()
	err := db.Save(data).Error
	return err
}

// You could update properties of an UserModel to database returning with error info.
//  err := db.Model(userModel).Update(UserModel{Username: "wangzitian0"}).Error
func (model *UserModel) Update(data interface{}) error {
	db := common.GetDB()
	err := db.Model(model).Update(data).Error
	return err
}

// You could add a following relationship as userModel1 following userModel2
// 	err = userModel1.following(userModel2)
func (u UserModel) following(v UserModel) error {
	db := common.GetDB()
	var follow FollowModel
	err := db.FirstOrCreate(&follow, &FollowModel{
		FollowingID:  v.ID,
		FollowedByID: u.ID,
	}).Error
	return err
}

// You could check whether  userModel1 following userModel2
// 	followingBool = myUserModel.isFollowing(self.UserModel)
func (u UserModel) isFollowing(v UserModel) bool {
	db := common.GetDB()
	var follow FollowModel
	db.Where(FollowModel{
		FollowingID:  v.ID,
		FollowedByID: u.ID,
	}).First(&follow)
	return follow.ID != 0
}

// You could delete a following relationship as userModel1 following userModel2
// 	err = userModel1.unFollowing(userModel2)
func (u UserModel) unFollowing(v UserModel) error {
	db := common.GetDB()
	err := db.Where(FollowModel{
		FollowingID:  v.ID,
		FollowedByID: u.ID,
	}).Delete(FollowModel{}).Error
	return err
}

// You could get a following list of userModel
// 	followings := userModel.GetFollowings()
func (u UserModel) GetFollowings() []UserModel {
	db := common.GetDB()
	tx := db.Begin()
	var follows []FollowModel
	var followings []UserModel
	tx.Where(FollowModel{
		FollowedByID: u.ID,
	}).Find(&follows)
	for _, follow := range follows {
		var userModel UserModel
		tx.Model(&follow).Related(&userModel, "Following")
		followings = append(followings, userModel)
	}
	tx.Commit()
	return followings
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/routers.go
package users

import (
	"errors"
	"github.com/gothinkster/golang-gin-realworld-example-app/common"
	"github.com/gin-gonic/gin"
	"net/http"
)

func UsersRegister(router *gin.RouterGroup) {
	router.POST("/", UsersRegistration)
	router.POST("/login", UsersLogin)
}

func UserRegister(router *gin.RouterGroup) {
	router.GET("/", UserRetrieve)
	router.PUT("/", UserUpdate)
}

func ProfileRegister(router *gin.RouterGroup) {
	router.GET("/:username", ProfileRetrieve)
	router.POST("/:username/follow", ProfileFollow)
	router.DELETE("/:username/follow", ProfileUnfollow)
}

func ProfileRetrieve(c *gin.Context) {
	username := c.Param("username")
	userModel, err := FindOneUser(&UserModel{Username: username})
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("profile", errors.New("Invalid username")))
		return
	}
	profileSerializer := ProfileSerializer{c, userModel}
	c.JSON(http.StatusOK, gin.H{"profile": profileSerializer.Response()})
}

func ProfileFollow(c *gin.Context) {
	username := c.Param("username")
	userModel, err := FindOneUser(&UserModel{Username: username})
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("profile", errors.New("Invalid username")))
		return
	}
	myUserModel := c.MustGet("my_user_model").(UserModel)
	err = myUserModel.following(userModel)
	if err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewError("database", err))
		return
	}
	serializer := ProfileSerializer{c, userModel}
	c.JSON(http.StatusOK, gin.H{"profile": serializer.Response()})
}

func ProfileUnfollow(c *gin.Context) {
	username := c.Param("username")
	userModel, err := FindOneUser(&UserModel{Username: username})
	if err != nil {
		c.JSON(http.StatusNotFound, common.NewError("profile", errors.New("Invalid username")))
		return
	}
	myUserModel := c.MustGet("my_user_model").(UserModel)

	err = myUserModel.unFollowing(userModel)
	if err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewError("database", err))
		return
	}
	serializer := ProfileSerializer{c, userModel}
	c.JSON(http.StatusOK, gin.H{"profile": serializer.Response()})
}

func UsersRegistration(c *gin.Context) {
	userModelValidator := NewUserModelValidator()
	if err := userModelValidator.Bind(c); err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewValidatorError(err))
		return
	}

	if err := SaveOne(&userModelValidator.userModel); err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewError("database", err))
		return
	}
	c.Set("my_user_model", userModelValidator.userModel)
	serializer := UserSerializer{c}
	c.JSON(http.StatusCreated, gin.H{"user": serializer.Response()})
}

func UsersLogin(c *gin.Context) {
	loginValidator := NewLoginValidator()
	if err := loginValidator.Bind(c); err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewValidatorError(err))
		return
	}
	userModel, err := FindOneUser(&UserModel{Email: loginValidator.userModel.Email})

	if err != nil {
		c.JSON(http.StatusForbidden, common.NewError("login", errors.New("Not Registered email or invalid password")))
		return
	}

	if userModel.checkPassword(loginValidator.User.Password) != nil {
		c.JSON(http.StatusForbidden, common.NewError("login", errors.New("Not Registered email or invalid password")))
		return
	}
	UpdateContextUserModel(c, userModel.ID)
	serializer := UserSerializer{c}
	c.JSON(http.StatusOK, gin.H{"user": serializer.Response()})
}

func UserRetrieve(c *gin.Context) {
	serializer := UserSerializer{c}
	c.JSON(http.StatusOK, gin.H{"user": serializer.Response()})
}

func UserUpdate(c *gin.Context) {
	myUserModel := c.MustGet("my_user_model").(UserModel)
	userModelValidator := NewUserModelValidatorFillWith(myUserModel)
	if err := userModelValidator.Bind(c); err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewValidatorError(err))
		return
	}

	userModelValidator.userModel.ID = myUserModel.ID
	if err := myUserModel.Update(userModelValidator.userModel); err != nil {
		c.JSON(http.StatusUnprocessableEntity, common.NewError("database", err))
		return
	}
	UpdateContextUserModel(c, myUserModel.ID)
	serializer := UserSerializer{c}
	c.JSON(http.StatusOK, gin.H{"user": serializer.Response()})
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/serializers.go
package users

import (
	"github.com/gin-gonic/gin"

	"github.com/gothinkster/golang-gin-realworld-example-app/common"
)

type ProfileSerializer struct {
	C *gin.Context
	UserModel
}

// Declare your response schema here
type ProfileResponse struct {
	ID        uint    `json:"-"`
	Username  string  `json:"username"`
	Bio       string  `json:"bio"`
	Image     *string `json:"image"`
	Following bool    `json:"following"`
}

// Put your response logic including wrap the userModel here.
func (self *ProfileSerializer) Response() ProfileResponse {
	myUserModel := self.C.MustGet("my_user_model").(UserModel)
	profile := ProfileResponse{
		ID:        self.ID,
		Username:  self.Username,
		Bio:       self.Bio,
		Image:     self.Image,
		Following: myUserModel.isFollowing(self.UserModel),
	}
	return profile
}

type UserSerializer struct {
	c *gin.Context
}

type UserResponse struct {
	Username string  `json:"username"`
	Email    string  `json:"email"`
	Bio      string  `json:"bio"`
	Image    *string `json:"image"`
	Token    string  `json:"token"`
}

func (self *UserSerializer) Response() UserResponse {
	myUserModel := self.c.MustGet("my_user_model").(UserModel)
	user := UserResponse{
		Username: myUserModel.Username,
		Email:    myUserModel.Email,
		Bio:      myUserModel.Bio,
		Image:    myUserModel.Image,
		Token:    common.GenToken(myUserModel.ID),
	}
	return user
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/unit_test.go
package users

import (
	"github.com/stretchr/testify/assert"
	"testing"

	"bytes"
	"fmt"
	"github.com/jinzhu/gorm"
	"github.com/gothinkster/golang-gin-realworld-example-app/common"
	"github.com/gin-gonic/gin"
	"net/http"
	"net/http/httptest"
	"os"
	_ "regexp"
)

var image_url = "https://golang.org/doc/gopher/frontpage.png"
var test_db *gorm.DB

func newUserModel() UserModel {
	return UserModel{
		ID:           2,
		Username:     "asd123!@#ASD",
		Email:        "wzt@g.cn",
		Bio:          "heheda",
		Image:        &image_url,
		PasswordHash: "",
	}
}

func userModelMocker(n int) []UserModel {
	var offset int
	test_db.Model(&UserModel{}).Count(&offset)
	var ret []UserModel
	for i := offset + 1; i <= offset+n; i++ {
		image := fmt.Sprintf("http://image/%v.jpg", i)
		userModel := UserModel{
			Username: fmt.Sprintf("user%v", i),
			Email:    fmt.Sprintf("user%v@linkedin.com", i),
			Bio:      fmt.Sprintf("bio%v", i),
			Image:    &image,
		}
		userModel.setPassword("password123")
		test_db.Create(&userModel)
		ret = append(ret, userModel)
	}
	return ret
}

func TestUserModel(t *testing.T) {
	asserts := assert.New(t)

	//Testing UserModel's password feature
	userModel := newUserModel()
	err := userModel.checkPassword("")
	asserts.Error(err, "empty password should return err")

	userModel = newUserModel()
	err = userModel.setPassword("")
	asserts.Error(err, "empty password can not be set null")

	userModel = newUserModel()
	err = userModel.setPassword("asd123!@#ASD")
	asserts.NoError(err, "password should be set successful")
	asserts.Len(userModel.PasswordHash, 60, "password hash length should be 60")

	err = userModel.checkPassword("sd123!@#ASD")
	asserts.Error(err, "password should be checked and not validated")

	err = userModel.checkPassword("asd123!@#ASD")
	asserts.NoError(err, "password should be checked and validated")

	//Testing the following relationship between users
	users := userModelMocker(3)
	a := users[0]
	b := users[1]
	c := users[2]
	asserts.Equal(0, len(a.GetFollowings()), "GetFollowings should be right before following")
	asserts.Equal(false, a.isFollowing(b), "isFollowing relationship should be right at init")
	a.following(b)
	asserts.Equal(1, len(a.GetFollowings()), "GetFollowings should be right after a following b")
	asserts.Equal(true, a.isFollowing(b), "isFollowing should be right after a following b")
	a.following(c)
	asserts.Equal(2, len(a.GetFollowings()), "GetFollowings be right after a following c")
	asserts.EqualValues(b, a.GetFollowings()[0], "GetFollowings should be right")
	asserts.EqualValues(c, a.GetFollowings()[1], "GetFollowings should be right")
	a.unFollowing(b)
	asserts.Equal(1, len(a.GetFollowings()), "GetFollowings should be right after a unFollowing b")
	asserts.EqualValues(c, a.GetFollowings()[0], "GetFollowings should be right after a unFollowing b")
	asserts.Equal(false, a.isFollowing(b), "isFollowing should be right after a unFollowing b")
}

//Reset test DB and create new one with mock data
func resetDBWithMock() {
	common.TestDBFree(test_db)
	test_db = common.TestDBInit()
	AutoMigrate()
	userModelMocker(3)
}

func HeaderTokenMock(req *http.Request, u uint) {
	req.Header.Set("Authorization", fmt.Sprintf("Token %v", common.GenToken(u)))
}

//You could write the init logic like reset database code here
var unauthRequestTests = []struct {
	init           func(*http.Request)
	url            string
	method         string
	bodyData       string
	expectedCode   int
	responseRegexg string
	msg            string
}{
	//Testing will run one by one, so you can combine it to a user story till another init().
	//And you can modified the header or body in the func(req *http.Request) {}

	//---------------------   Testing for user register   ---------------------
	{
		func(req *http.Request) {
			resetDBWithMock()
		},
		"/users/",
		"POST",
		`{"user":{"username": "wangzitian0","email": "wzt@gg.cn","password": "jakejxke"}}`,
		http.StatusCreated,
		`{"user":{"username":"wangzitian0","email":"wzt@gg.cn","bio":"","image":null,"token":"([a-zA-Z0-9-_.]{115})"}}`,
		"valid data and should return StatusCreated",
	},
	{
		func(req *http.Request) {},
		"/users/",
		"POST",
		`{"user":{"username": "wangzitian0","email": "wzt@gg.cn","password": "jakejxke"}}`,
		http.StatusUnprocessableEntity,
		`{"errors":{"database":"UNIQUE constraint failed: user_models.email"}}`,
		"duplicated data and should return StatusUnprocessableEntity",
	},
	{
		func(req *http.Request) {},
		"/users/",
		"POST",
		`{"user":{"username": "u","email": "wzt@gg.cn","password": "jakejxke"}}`,
		http.StatusUnprocessableEntity,
		`{"errors":{"Username":"{min: 4}"}}`,
		"too short username should return error",
	},
	{
		func(req *http.Request) {},
		"/users/",
		"POST",
		`{"user":{"username": "wangzitian0","email": "wzt@gg.cn","password": "j"}}`,
		http.StatusUnprocessableEntity,
		`{"errors":{"Password":"{min: 8}"}}`,
		"too short password should return error",
	},
	{
		func(req *http.Request) {},
		"/users/",
		"POST",
		`{"user":{"username": "wangzitian0","email": "wztgg.cn","password": "jakejxke"}}`,
		http.StatusUnprocessableEntity,
		`{"errors":{"Email":"{key: email}"}}`,
		"email invalid should return error",
	},

	//---------------------   Testing for user login   ---------------------
	{
		func(req *http.Request) {
			resetDBWithMock()
		},
		"/users/login",
		"POST",
		`{"user":{"email": "user1@linkedin.com","password": "password123"}}`,
		http.StatusOK,
		`{"user":{"username":"user1","email":"user1@linkedin.com","bio":"bio1","image":"http://image/1.jpg","token":"([a-zA-Z0-9-_.]{115})"}}`,
		"right info login should return user",
	},
	{
		func(req *http.Request) {},
		"/users/login",
		"POST",
		`{"user":{"email": "user112312312@linkedin.com","password": "password123"}}`,
		http.StatusForbidden,
		`{"errors":{"login":"Not Registered email or invalid password"}}`,
		"email not exist should return error info",
	},
	{
		func(req *http.Request) {},
		"/users/login",
		"POST",
		`{"user":{"email": "user1@linkedin.com","password": "password126"}}`,
		http.StatusForbidden,
		`{"errors":{"login":"Not Registered email or invalid password"}}`,
		"password error should return error info",
	},
	{
		func(req *http.Request) {},
		"/users/login",
		"POST",
		`{"user":{"email": "user1@linkedin.com","password": "passw"}}`,
		http.StatusUnprocessableEntity,
		`{"errors":{"Password":"{min: 8}"}}`,
		"password too short should return error info",
	},
	{
		func(req *http.Request) {},
		"/users/login",
		"POST",
		`{"user":{"email": "user1@linkedin.com","password": "passw"}}`,
		http.StatusUnprocessableEntity,
		`{"errors":{"Password":"{min: 8}"}}`,
		"password too short should return error info",
	},

	//---------------------   Testing for self info get & auth module  ---------------------
	{
		func(req *http.Request) {
			resetDBWithMock()
		},
		"/user/",
		"GET",
		``,
		http.StatusUnauthorized,
		``,
		"request should return 401 without token",
	},
	{
		func(req *http.Request) {
			req.Header.Set("Authorization", fmt.Sprintf("Tokee %v", common.GenToken(1)))
		},
		"/user/",
		"GET",
		``,
		http.StatusUnauthorized,
		``,
		"wrong token should return 401",
	},
	{
		func(req *http.Request) {
			HeaderTokenMock(req, 1)
		},
		"/user/",
		"GET",
		``,
		http.StatusOK,
		`{"user":{"username":"user1","email":"user1@linkedin.com","bio":"bio1","image":"http://image/1.jpg","token":"([a-zA-Z0-9-_.]{115})"}}`,
		"request should return current user with token",
	},

	//---------------------   Testing for users' profile get   ---------------------
	{
		func(req *http.Request) {
			resetDBWithMock()
			HeaderTokenMock(req, 1)
		},
		"/profiles/user1",
		"GET",
		``,
		http.StatusOK,
		`{"profile":{"username":"user1","bio":"bio1","image":"http://image/1.jpg","following":false}}`,
		"request should return self profile",
	},
	{
		func(req *http.Request) {
			HeaderTokenMock(req, 2)
		},
		"/profiles/user1",
		"GET",
		``,
		http.StatusOK,
		`{"profile":{"username":"user1","bio":"bio1","image":"http://image/1.jpg","following":false}}`,
		"request should return correct other's profile",
	},

	//---------------------   Testing for users' profile update   ---------------------
	{
		func(req *http.Request) {
			resetDBWithMock()
			HeaderTokenMock(req, 1)
		},
		"/profiles/user123",
		"GET",
		``,
		http.StatusNotFound,
		``,
		"user should not exist profile before changed",
	},
	{
		func(req *http.Request) {
			HeaderTokenMock(req, 1)
		},
		"/user/",
		"PUT",
		`{"user":{"username":"user123","password": "password126","email":"user123@linkedin.com","bio":"bio123","image":"http://hehe/123.jpg"}}`,
		http.StatusOK,
		`{"user":{"username":"user123","email":"user123@linkedin.com","bio":"bio123","image":"http://hehe/123.jpg","token":"([a-zA-Z0-9-_.]{115})"}}`,
		"current user profile should be changed",
	},
	{
		func(req *http.Request) {
			HeaderTokenMock(req, 1)
		},
		"/profiles/user123",
		"GET",
		``,
		http.StatusOK,
		`{"profile":{"username":"user123","bio":"bio123","image":"http://hehe/123.jpg","following":false}}`,
		"request should return self profile after changed",
	},
	{
		func(req *http.Request) {},
		"/users/login",
		"POST",
		`{"user":{"email": "user123@linkedin.com","password": "password126"}}`,
		http.StatusOK,
		`{"user":{"username":"user123","email":"user123@linkedin.com","bio":"bio123","image":"http://hehe/123.jpg","token":"([a-zA-Z0-9-_.]{115})"}}`,
		"user should login using new password after changed",
	},
	{
		func(req *http.Request) {
			HeaderTokenMock(req, 2)
		},
		"/user/",
		"PUT",
		`{"user":{"password": "pas"}}`,
		http.StatusUnprocessableEntity,
		`{"errors":{"Password":"{min: 8}"}}`,
		"current user profile should not be changed with error user info",
	},

	//---------------------   Testing for db errors   ---------------------
	{
		func(req *http.Request) {
			resetDBWithMock()
			HeaderTokenMock(req, 4)
		},
		"/user/",
		"PUT",
		`{"password": "password321"}}`,
		http.StatusUnprocessableEntity,
		`{"errors":{"Email":"{key: email}","Username":"{key: alphanum}"}}`,
		"test database pk error for user update",
	},
	{
		func(req *http.Request) {
			HeaderTokenMock(req, 0)
		},
		"/user/",
		"PUT",
		`{"user":{"username": "wangzitian0","email": "wzt@gg.cn","password": "jakejxke"}}`,
		http.StatusUnprocessableEntity,
		`{"errors":{"database":"UNIQUE constraint failed: user_models.email"}}`,
		"cheat validator and test database connecting error for user update",
	},
	{
		func(req *http.Request) {
			common.TestDBFree(test_db)
			test_db = common.TestDBInit()

			test_db.AutoMigrate(&UserModel{})
			userModelMocker(3)
			HeaderTokenMock(req, 2)
		},
		"/profiles/user1/follow",
		"POST",
		``,
		http.StatusUnprocessableEntity,
		`{"errors":{"database":"no such table: follow_models"}}`,
		"test database error for following",
	},
	{
		func(req *http.Request) {
			HeaderTokenMock(req, 2)
		},
		"/profiles/user1/follow",
		"DELETE",
		``,
		http.StatusUnprocessableEntity,
		`{"errors":{"database":"no such table: follow_models"}}`,
		"test database error for canceling following",
	},
	{
		func(req *http.Request) {
			resetDBWithMock()
			HeaderTokenMock(req, 2)
		},
		"/profiles/user666/follow",
		"POST",
		``,
		http.StatusNotFound,
		`{"errors":{"profile":"Invalid username"}}`,
		"following wrong user name should return errors",
	},
	{
		func(req *http.Request) {
			HeaderTokenMock(req, 2)
		},
		"/profiles/user666/follow",
		"DELETE",
		``,
		http.StatusNotFound,
		`{"errors":{"profile":"Invalid username"}}`,
		"cancel following wrong user name should return errors",
	},

	//---------------------   Testing for user following   ---------------------
	{
		func(req *http.Request) {
			resetDBWithMock()
			HeaderTokenMock(req, 2)
		},
		"/profiles/user1/follow",
		"POST",
		``,
		http.StatusOK,
		`{"profile":{"username":"user1","bio":"bio1","image":"http://image/1.jpg","following":true}}`,
		"user follow another should work",
	},
	{
		func(req *http.Request) {
			HeaderTokenMock(req, 2)
		},
		"/profiles/user1",
		"GET",
		``,
		http.StatusOK,
		`{"profile":{"username":"user1","bio":"bio1","image":"http://image/1.jpg","following":true}}`,
		"user follow another should make sure database changed",
	},
	{
		func(req *http.Request) {
			HeaderTokenMock(req, 2)
		},
		"/profiles/user1/follow",
		"DELETE",
		``,
		http.StatusOK,
		`{"profile":{"username":"user1","bio":"bio1","image":"http://image/1.jpg","following":false}}`,
		"user cancel follow another should work",
	},
	{
		func(req *http.Request) {
			HeaderTokenMock(req, 2)
		},
		"/profiles/user1",
		"GET",
		``,
		http.StatusOK,
		`{"profile":{"username":"user1","bio":"bio1","image":"http://image/1.jpg","following":false}}`,
		"user cancel follow another should make sure database changed",
	},
}

func TestWithoutAuth(t *testing.T) {
	asserts := assert.New(t)
	//You could write the reset database code here if you want to create a database for this block
	//resetDB()

	r := gin.New()
	UsersRegister(r.Group("/users"))
	r.Use(AuthMiddleware(true))
	UserRegister(r.Group("/user"))
	ProfileRegister(r.Group("/profiles"))
	for _, testData := range unauthRequestTests {
		bodyData := testData.bodyData
		req, err := http.NewRequest(testData.method, testData.url, bytes.NewBufferString(bodyData))
		req.Header.Set("Content-Type", "application/json")
		asserts.NoError(err)

		testData.init(req)

		w := httptest.NewRecorder()
		r.ServeHTTP(w, req)

		asserts.Equal(testData.expectedCode, w.Code, "Response Status - "+testData.msg)
		asserts.Regexp(testData.responseRegexg, w.Body.String(), "Response Content - "+testData.msg)
	}
}

//This is a hack way to add test database for each case, as whole test will just share one database.
//You can read TestWithoutAuth's comment to know how to not share database each case.
func TestMain(m *testing.M) {
	test_db = common.TestDBInit()
	AutoMigrate()
	exitVal := m.Run()
	common.TestDBFree(test_db)
	os.Exit(exitVal)
}

--#

--% /tmp/hapus/jakartaee/golang-gin-realworld-example-app/users/validators.go
package users

import (
	"github.com/gothinkster/golang-gin-realworld-example-app/common"
	"github.com/gin-gonic/gin"
)

// *ModelValidator containing two parts:
// - Validator: write the form/json checking rule according to the doc https://github.com/go-playground/validator
// - DataModel: fill with data from Validator after invoking common.Bind(c, self)
// Then, you can just call model.save() after the data is ready in DataModel.
type UserModelValidator struct {
	User struct {
		Username string `form:"username" json:"username" binding:"exists,alphanum,min=4,max=255"`
		Email    string `form:"email" json:"email" binding:"exists,email"`
		Password string `form:"password" json:"password" binding:"exists,min=8,max=255"`
		Bio      string `form:"bio" json:"bio" binding:"max=1024"`
		Image    string `form:"image" json:"image" binding:"omitempty,url"`
	} `json:"user"`
	userModel UserModel `json:"-"`
}

// There are some difference when you create or update a model, you need to fill the DataModel before
// update so that you can use your origin data to cheat the validator.
// BTW, you can put your general binding logic here such as setting password.
func (self *UserModelValidator) Bind(c *gin.Context) error {
	err := common.Bind(c, self)
	if err != nil {
		return err
	}
	self.userModel.Username = self.User.Username
	self.userModel.Email = self.User.Email
	self.userModel.Bio = self.User.Bio

	if self.User.Password != common.NBRandomPassword {
		self.userModel.setPassword(self.User.Password)
	}
	if self.User.Image != "" {
		self.userModel.Image = &self.User.Image
	}
	return nil
}

// You can put the default value of a Validator here
func NewUserModelValidator() UserModelValidator {
	userModelValidator := UserModelValidator{}
	//userModelValidator.User.Email ="w@g.cn"
	return userModelValidator
}

func NewUserModelValidatorFillWith(userModel UserModel) UserModelValidator {
	userModelValidator := NewUserModelValidator()
	userModelValidator.User.Username = userModel.Username
	userModelValidator.User.Email = userModel.Email
	userModelValidator.User.Bio = userModel.Bio
	userModelValidator.User.Password = common.NBRandomPassword

	if userModel.Image != nil {
		userModelValidator.User.Image = *userModel.Image
	}
	return userModelValidator
}

type LoginValidator struct {
	User struct {
		Email    string `form:"email" json:"email" binding:"exists,email"`
		Password string `form:"password"json:"password" binding:"exists,min=8,max=255"`
	} `json:"user"`
	userModel UserModel `json:"-"`
}

func (self *LoginValidator) Bind(c *gin.Context) error {
	err := common.Bind(c, self)
	if err != nil {
		return err
	}

	self.userModel.Email = self.User.Email
	return nil
}

// You can put the default value of a Validator here
func NewLoginValidator() LoginValidator {
	loginValidator := LoginValidator{}
	return loginValidator
}

--#

