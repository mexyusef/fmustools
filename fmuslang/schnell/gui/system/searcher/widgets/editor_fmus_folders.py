from schnell.app.dirutils import joinhere
from schnell.app.fileutils import file_content

# FILE_API = joinhere(__file__, 'folders/django.txt')

best_practice_folders = {
######################## django
    "/dj": {
    'desc': 'django',
    'content': file_content(joinhere(__file__, 'folders/django.txt'))
    },
######################## flask
    "/fl": {
    'desc': 'flask',
    'content': file_content(joinhere(__file__, 'folders/flask.txt'))},

######################## fastapi
    "/fa": {
    'desc': 'fastapi',
    'content': file_content(joinhere(__file__, 'folders/fastapi.txt'))},

######################## springboot
    "/sb": {
    'desc': 'list of localhost urls',
    'content': file_content(joinhere(__file__, 'folders/springboot.txt'))},
######################## quarkus
    "/qk": {
    'desc': 'quarkus',
    'content': """.,d
    src,d
        main,d
            java,d
                comexample,d
                    app,d
                        model,d
                            User.java,f(t=)
                            Product.java,f(t=)
                        service,d
                            UserService.java,f(t=)
                            ProductService.java,f(t=)
                        resource,d
                            UserResource.java,f(t=)
                            ProductResource.java,f(t=)
                        Application.java,f(t=)
        resources,d
            application.properties,f(t=)
            logback.xml,f(t=)
      test,d
        java,d
            comexample,d
                app,d
                    resource,d
                        UserResourceTest.java,f(t=)
                        ProductResourceTest.java,f(t=)
"""},
######################## jakartaee
    "/jee": {
    'desc': 'jakarta ee',
    'content': file_content(joinhere(__file__, 'folders/jakarta-ee.txt'))},
######################## micronaut
    "/mn": {
    'desc': 'micronaut',
    'content': """.,d
    src,d
        main,d
            java,d
                comexamplekerjaan,d
                    config,d
                        ApplicationConfiguration.java,f(t=)
                    controllers,d
                        HomeController.java,f(t=)
                        UserController.java,f(t=)
                    dao,d
                        UserRepository.java,f(t=)
                    dto,d
                        UserDto.java,f(t=)
                    entities,d
                        User.java,f(t=)
                    exceptions,d
                        CustomException.java,f(t=)
                    filters,d
                        AuthFilter.java,f(t=)
                    services,d
                        UserService.java,f(t=)
            resources,d
                application.yml,f(t=)
                logback.xml,f(t=)
"""},
######################## dropwizard
    "/dw": {
    'desc': 'dropwizard',
    'content': """.,d
    config,d
        development.yaml,f(t=)
        production.yaml,f(t=)
    src,d
        main,d
            java,d
                comexample,d
                    api,d
                        resources,d
                            ExampleResource.java,f(t=)
                    config,d
                        AppConfiguration.java,f(t=)
                    core,d
                        Example.java,f(t=)
                    db,d
                        migrations,d
                            V1__initial.sql,f(t=)
                        dao,d
                            ExampleDAO.java,f(t=)
                            ExampleDAOImpl.java,f(t=)
                    health,d
                        ExampleHealthCheck.java,f(t=)
                    Application.java,f(t=)
    test,d
        java,d
            comexample,d
                api,d
                    resources,d
                        ExampleResourceTest.java,f(t=)
                db,d
                    dao,d
                        ExampleDAOTest.java,f(t=)
                health,d
                    ExampleHealthCheckTest.java,f(t=)
                ApplicationTest.java,f(t=)
"""},
######################## vertx
    "/vt": {
    'desc': 'vertx',
    'content': """.,d
    src,d
        main,d
            java,d
            comexample,d
                    MyApp.java,f(t=)
                    handlers,d
                        HttpHandler.java,f(t=)
                        WebSocketHandler.java,f(t=)
                    models,d
                        User.java,f(t=)
                    services,d
                        UserService.java,f(t=)
                        AuthService.java,f(t=)
            resources,d
                application.properties,f(t=)
                log4j2.xml,f(t=)
"""},
######################## play-scala
    "/plays": {
    'desc': 'play scala',
    'content': """.,d
    app,d
        controllers,d
            HomeController.scala,f(t=)
            UserController.scala,f(t=)
        models,d
            User.scala,f(t=)
        services,d
            UserService.scala,f(t=)
    conf,d
        application.conf,f(t=)
        routes,f(t=)
    public,d
        css,d
            main.css,f(t=)
        js,d
            main.js,f(t=)
        images,d
            #logo.png,f(t=)
    views,d
        index.scala.html,f(t=)
        login.scala.html,f(t=)
        layout,d
            main.scala.html,f(t=)
"""},
######################## kotr
    "/ktr": {
    'desc': 'kotr',
    'content': """.d
    src,d
        main,d
            kotlin,d
                comexample,d
                    config,d
                        ApplicationConfig.kt,f(t=)
                    controllers,d
                        UserController.kt,f(t=)
                    models,d
                        User.kt,f(t=)
                        #...
                    repositories,d
                        UserRepository.kt,f(t=)
                        #...
                    services,d
                        UserService.kt,f(t=)
                        #...
                    utils,d
                        ResponseWrapper.kt,f(t=)
                        #...
                    Application.kt,f(t=)

            resources,d
                application.yml,f(t=)
                #...
        test,d
            kotlin,d
                comexample,d
                    controllers,d
                        UserControllerTest.kt,f(t=)
                    repositories,d
                        UserRepositoryTest.kt,f(t=)
                    services,d
                        UserServiceTest.kt,f(t=)
                    utils,d
                        ResponseWrapperTest.kt,f(t=)
            resources,d
"""},
######################## react
    "/react": {
    'desc': 'react',
    'content': file_content(joinhere(__file__, 'folders/react.txt'))},
######################## vue
    "/vue": {
    'desc': 'vue',
    'content': file_content(joinhere(__file__, 'folders/vue.txt'))},
######################## angular
    "/ang": {
    'desc': 'angular',
    'content': """.,d
    src,d
        app,d
            modules,d
                user-profile,d
                    user-profile.module.ts,f(t=)
                    user-profile-routing.module.ts,f(t=)
                    user-profile.component.ts,f(t=)
                    user-profile.component.html,f(t=)
                    user-profile.component.scss,f(t=)
                dashboard,d
                    dashboard.module.ts,f(t=)
                    dashboard-routing.module.ts,f(t=)
                    dashboard.component.ts,f(t=)
                    dashboard.component.html,f(t=)
                    dashboard.component.scss,f(t=)
            services,d
                user.service.ts,f(t=)
                auth.service.ts,f(t=)
            components,d
                atoms,d
                molecules,d
                organisms,d
            guards,d
                auth.guard.ts,f(t=)
            routes,d
                app-routing.module.ts,f(t=)
            assets,d
                images,d
                fonts,d
            utils,d
                date-utils.ts,f(t=)
"""},
######################## nodejs
    "/nd": {
    'desc': 'nodejs',
    'content': file_content(joinhere(__file__, 'folders/node.txt'))
},
######################## nextjs
    "/nx": {
    'desc': 'nextjs',
    'content': file_content(joinhere(__file__, 'folders/next.txt'))
},
######################## nestjs
    "/ns": {
    'desc': 'nestjs',
    'content': file_content(joinhere(__file__, 'folders/nest.txt'))
},
######################## android kotlin
    "/andro": {
    'desc': 'android',
    'content': file_content(joinhere(__file__, 'folders/android.txt'))},
######################## flutter
    "/flu": {
    'desc': 'flutter',
    'content': file_content(joinhere(__file__, 'folders/flutter.txt'))},
######################## react native
    "/rn": {
    'desc': 'react-native',
    'content': file_content(joinhere(__file__, 'folders/react-native.txt'))},
}
