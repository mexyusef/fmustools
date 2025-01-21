---
title: Vue.js Tutorial
date: 2018/09/25
description: Vue.js Tutorial
tag: vue, javascript
author: Yusef
---

This is an example of creating a Vue application containing several simple pages utilizing the Bulma CSS framework.

# Installing Vue

First we install vue-cli globally, so that we can use the "vue" command to create a project.
```
npm i -g vue-cli

vue init webpack myvueapp
cd myvueapp
```
Access the page in http://localhost:8080/


# Components

The generated structure would be like this:
```
build/
config/
src/
    assets/
    components/
        Home.vue
    router/
        index.js
    App.vue
    main.js
static/
    index.html
        <div id="app></div>
```

The content of main.js:
```
import Vue from 'vue'
import App from './App'
import router from './router'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
    el: "#app",
    router,
    template: '<App/>',
    components: { App }
})
```

App.vue will contain html, scripts, and styles:
```
<template>
    <div id="app">
        <img src="./assets/logo.png">
        <router-view></router-view>
    </div>
</template>

<script>
export default {
    name: 'app'
}
</script>

<style>
#app {
    font-family: 'Avenir', Helvetica, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e58;
    margin-top: 60px;
}
</style>
```

Here is the content of router.js:
```
import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'Hello',
            component: Hello
        }
    ]
})
```

# Using Bulma

There are several CSS framework out there, we can use Bulma for instance. The documentation can be found in `https://bulmua.io/documentation/`.

```
npm i -D node-sass sass-loader style-loader
npm i -S bulma
```

Afterward, add the following line to App.vue in the `<style>` section:
```
@import '../node_modules/bulma/bulma.sass'
```
We can tell the difference from different font style, etc.

Let us create another file `style.sass` within the `src` directory.

```
$primary: #1EC9AC !default

$tablet: 769px !default
$desktop: 1000px !default
$widescreen: 1192px !default
$fullhd: 1384px !default

=mobile
    @media screen and (max-width: $tablet - 1px)
        @content

=tablet
    @media screen and (max-width: $tablet), print
        @content

=tablet-only
    @media screen and (max-width: $tablet) and (max-width: $desktop - 1px)
        @content

=desktop
    @media screen and (max-width: $desktop)
        @content

=desktop-only
    @media screen and (max-width: $desktop) and (max-width: $widescreen - 1px)
        @content
```

Then add reference to the new style within App.vue in the `<style>` section:
```
@import 'style'
```

Since we use sass, change the style tag in Home.vue from `<style scoped>` to `<style lang="sass" scoped>` and we can import the new style file `style.sass` directly `@import '../style'`.

# Navigation

We can copy and paste the following code from `https://bulma.io/documentation/components/navbar/` to use in our `App.vue` file.

```
<nav class="navbar" role="navigation" aria-label="main navigation">
  <div class="navbar-brand">
    <a class="navbar-item" href="https://bulma.io">
      <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
    </a>

    <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
      <span aria-hidden="true"></span>
    </a>
  </div>

  <div id="navbarBasicExample" class="navbar-menu">
    <div class="navbar-start">
      <a class="navbar-item">
        Home
      </a>

      <a class="navbar-item">
        Documentation
      </a>

      <div class="navbar-item has-dropdown is-hoverable">
        <a class="navbar-link">
          More
        </a>

        <div class="navbar-dropdown">
          <a class="navbar-item">
            About
          </a>
          <a class="navbar-item">
            Jobs
          </a>
          <a class="navbar-item">
            Contact
          </a>
          <hr class="navbar-divider">
          <a class="navbar-item">
            Report an issue
          </a>
        </div>
      </div>
    </div>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="buttons">
          <a class="button is-primary">
            <strong>Sign up</strong>
          </a>
          <a class="button is-light">
            Log in
          </a>
        </div>
      </div>
    </div>
  </div>
</nav>
```

# Creating Footer and Hero

We can either create a separate component for Footer (real world scenario) or just insert it directly within App.vue for the purpose of a tutorial. If we choose the later, just create a footer tag after the `<router-view></router-view>` in the HTML template section.
```
<footer class="footer is-primary">
    <div class="container">
        <div class="columns">
            <div class="column">
                <p>Footer text</p>
            </div>
            <div class="column has-text-right">
                <p>Footer text on the right</p>
            </div>
        </div>
    </div>
</footer>
```
Style the template accordingly:
```
footer
    background-color: $Primary $important!
    color: #fff
    .icon
        color: #fff
        marign-left: 20px
```

The code for the Hero section can be copied from `https://bulma.io/documentation/layout/hero/` and put into our `components/Home.vue` file.

Interpolation between data in the html section and properties in the script section would be below.

html template:
```
<h1 class="title">{{ heading }}</h1>
```

script:
```
export deefault {
    name: 'home',
    data () {
        return {
            heading: 'Sample title for our hero',
            subheading: '...because this not a serious real-world app development'
        }
    }
}
```

# Finishing up
We can also add some dynamic data fetched from an external API.
For example, to get sampe of blog posts, we can fetch from `http://jsonplaceholder.typicode.com/posts`

and modify the page accordingly:

The HTML section:
```
<div class="columns" v-if="blogposts && blogposts.length">
    <div class="column is-one-third" v-for="blogpost of blogposts">
        ...
        <p class="title">{{ blogpost.title }}</p>
        <p class="title">{{ blogpost.body }}</p>
```

The script section:
```
import axios from 'axios';

export default {
    name: 'blog',
    data: () => ({
        blogposts: [],
        errors: []
    })
    created() {
        axios.get('http://jsonplaceholder.typicode.com/posts')
            .then(response => {
                this.blogposts = response.data.slice(0,10);
            })
            .catch(e => {
                this.errors.push(e)
            })
    }
}
```

The style section:
```
.columns
    flex-wrap: wrap
```

