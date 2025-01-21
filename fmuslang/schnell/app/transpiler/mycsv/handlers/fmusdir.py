import re
from schnell.app.stringutils import tabify_content_tab, tabify_content_space, tabify_contentlist_tab, tabify_contentlist_space


def create_node_ts(tables, RootNode):
    template = """  node-ts,d
        app,d
            config,d
                config.ts,f(t=)
                env.ts,f(t=)
            controllers,d
                authController.ts,f(t=)
            middleware,d
                authMiddleware.ts,f(t=)
                errorMiddleware.ts,f(t=)
            models,d
                user.ts,f(t=)
            routes,d
                auth.ts,f(t=)
            services,d
                auth.ts,f(t=)
            utils,d
                logger.ts,f(t=)
                validator.ts,f(t=)
            app.ts,f(t=)
            tsconfig.json,f(t=)
"""
    kembali = template
    return kembali


def create_node_js(tables, RootNode):
    template = """  node-js,d
        app,d
            config,d
                config.js,f(t=)
                env.ts,f(t=)
            controllers,d
                authController.js,f(t=)
            middleware,d
                auth.js,f(t=)
                error.js,f(t=)
            models,d
                user.js,f(t=)
            routes,d
                auth.js,f(t=)
            services,d
                auth.js,f(t=)
            utils,d
                logger.js,f(t=)
                validator.js,f(t=)
            app.js,f(t=)
            tsconfig.json,f(t=)
"""
    kembali = template
    return kembali


def create_angular(tables, RootNode):
    model_template = """__TABLENAME_LOWER__,d
    components,d
        __TABLENAME_LOWER__-list,d
            __TABLENAME_LOWER__-list.component.ts,f(t=)
            __TABLENAME_LOWER__-list.component.html,f(t=)
            __TABLENAME_LOWER__-list.component.scss,f(t=)
        __TABLENAME_LOWER__-form,d
            __TABLENAME_LOWER__-form.component.ts,f(t=)
            __TABLENAME_LOWER__-form.component.html,f(t=)
            __TABLENAME_LOWER__-form.component.scss,f(t=)
    pages,d
        __TABLENAME_LOWER__-page,d
            __TABLENAME_LOWER__-page.component.ts,f(t=)
            __TABLENAME_LOWER__-page.component.html,f(t=)
            __TABLENAME_LOWER__-page.component.scss,f(t=)
    __TABLENAME_LOWER__-routing.module.ts,f(t=)
    __TABLENAME_LOWER__.module.ts,f(t=)
"""
    template = """  angular,d
        app,d
            core,d
                constants,d
                    app.constants.ts,f(t=)
                    api-endpoints.constants.ts,f(t=)
                models,d
                    user.ts,f(t=)
                services,d
                    api.service.ts,f(t=)
                core.module.ts,f(t=)
            shared,d
                components,d
                    header,d
                        header.component.ts,f(t=)
                        header.component.html,f(t=)
                        header.component.scss,f(t=)
                    footer,d
                        footer.component.ts,f(t=)
                        footer.component.html,f(t=)
                        footer.component.scss,f(t=)
                directives,d
                    highlight.directives.ts,f(t=)
                pipes,d
                    capitalize.pipe.ts,f(t=)
                    date-format.pipe.ts,f(t=)
                shared.module.ts,f(t=)
            app-routing.module.ts,f(t=)
            app.component.ts,f(t=)
            app.component.html,f(t=)
            app.component.scss,f(t=)
            app.module.ts,f(t=)
            index.html,f(t=)
            main.ts,f(t=)
            styles.scss,f(t=)
            environment,d
                environment.prod.ts,f(t=)
                environment.ts,f(t=)
            tsconfig.json,f(t=)
"""
    kembali = template
    return kembali


def create_vue(tables, RootNode):
    template = """  vue,d
        assets,d
            images,d
            styles,d
                base,d
                components,d
                utilities,d
            fonts,d
        components,d
            common,d
            views,d
        router,d
        store,d
            modules,d
            index.js,f(t=)
        utils,d
        views,d
            home,d
            __TABLENAME_LOWER_PLURAL__,d
                components,d
                views,d
            error,d
        App.vue,f(t=)
        main.js,f(t=)
"""
    kembali = template
    return kembali


def create_next_fe(tables, RootNode):
    template = """  next-fe,d
        assets,d
            images,d
            styles,d
                base,d
                components,d
                utilities,d
            fonts,d
        components,d
            common,d
            views,d
        router,d
        store,d
            modules,d
            index.js,f(t=)
        utils,d
        views,d
            home,d
            __TABLENAME_LOWER_PLURAL__,d
                components,d
                views,d
            error,d
        package.json,f(F=__CONTENT_START__)
{
  "name": "twitter-clone",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@next-auth/prisma-adapter": "^1.0.5",
    "@prisma/client": "^4.11.0",
    "@types/lodash": "^4.14.191",
    "@types/node": "18.14.2",
    "@types/react": "18.0.28",
    "@types/react-dom": "18.0.11",
    "axios": "^1.3.4",
    "bcrypt": "^5.1.0",
    "date-fns": "^2.29.3",
    "eslint": "8.35.0",
    "eslint-config-next": "13.2.1",
    "lodash": "^4.17.21",
    "next": "13.2.1",
    "next-auth": "^4.20.1",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "react-dropzone": "^14.2.3",
    "react-hot-toast": "^2.4.0",
    "react-icons": "^4.7.1",
    "react-spinners": "^0.13.8",
    "react-toastify": "^9.1.1",
    "swr": "^2.0.4",
    "typescript": "4.9.5",
    "zustand": "^4.3.5"
  },
  "devDependencies": {
    "@types/bcrypt": "^5.0.0",
    "autoprefixer": "^10.4.13",
    "postcss": "^8.4.21",
    "tailwindcss": "^3.2.7"
  }
}
__CONTENT_END__
        .eslintrc.json,f(F=__CONTENT_START__)
{
  "extends": "next/core-web-vitals"
}
__CONTENT_END__
        .env,f(F=__CONTENT_START__)
DATABASE_URL=
NEXTAUTH_JWT_SECRET=
NEXTAUTH_SECRET=
__CONTENT_END__
        .gitignore,f(t=)
        next-env.d.ts,f(F=__CONTENT_START__)
/// <reference types="next" />
/// <reference types="next/image-types/global" />

// NOTE: This file should not be edited
// see https://nextjs.org/docs/basic-features/typescript for more information.
__CONTENT_END__
        next.config.js,f(F=__CONTENT_START__)
const nextConfig = {
  reactStrictMode: true,
}

module.exports = nextConfig
__CONTENT_END__
        postcss.config.js,f(F=__CONTENT_START__)
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
__CONTENT_END__
        tailwind.config.js,f(F=__CONTENT_START__)
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx}",
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
__CONTENT_END__
        tsconfig.json,f(F=__CONTENT_START__)
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
__CONTENT_END__
"""
    kembali = template
    return kembali


def create_react(tables, RootNode):
    template = """
"""
    kembali = template
    return kembali


providers = [
    create_node_ts,
    create_node_js,
    create_angular,
    create_vue,
    create_next_fe,
    # jumat malam sabtu, 28/4/2023 ini mari habiskan java...
]

# cara coba dg ctrl+k
# /ketik)python C:\Users\usef\work\sidoarjo\schnell\app\transpiler\mycsv\main.py | fmus/{@Todo}title,s

def fmusdir(tables, RootNode):
    """
    target
    fmusoutput,d
        backend-node-js,d
        backend-node-ts,d
        backend-django,d
        backend-fastapi,d
        backend-flask,d
        backend-react,d
        backend-vue,d
        backend-angular,d
    """
    header = ".,d"
    kembali = header
    for provider in providers:
        kembali += '\n\n'
        kembali += provider(tables, RootNode)

    # kembali = header + tabify_content_tab(kembali)
    # kembali = re.sub(r'(?m)^\s+__CONTENT_END__\s*$', '__CONTENT_END__'.lstrip(), kembali)
    return kembali
