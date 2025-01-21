--% lamadev, react-admin-dashboard
simple one page dashboard, dg background warna oldies...

pnpm i
pnpm build
pnpm start
--#

--% react-purity-ui
.
├── api
- auth.js
let base = "users";
class AuthApi {
    static Login = (data) => {
        return axios.post(`${base}/login`, data);
    };
}
alamat = api/users/login

--#

--% react-soft-ui
.
├── api
- auth.js
let base = "users";
class AuthApi {
    static Login = (data) => {
        return axios.post(`${base}/login`, data);
    };
}
alamat = api/users/login

├── assets
│   ├── images
│   └── theme
│       ├── base
│       ├── components
│       └── functions
├── auth-context
├── components
...
├── config
├── context
├── examples
│   ├── Breadcrumbs
│   ├── Cards
...
│   ├── Charts
...
│   ├── Configurator
│   ├── Footer
│   ├── Icons
│   ├── LayoutContainers
│   │   ├── DashboardLayout
│   │   └── PageLayout
│   ├── Navbars
│   │   ├── DashboardNavbar
│   │   └── DefaultNavbar
│   ├── NotificationItem
│   ├── ProfilesList
│   ├── Sidenav
│   │   └── styles
│   ├── Table
│   └── Timeline
│       ├── TimelineItem
│       ├── TimelineList
│       └── context
└── layouts
    ├── authentication
    │   ├── components
    │   ├── sign-in
import AuthApi from "../../../api/auth";
let response = await AuthApi.Login({
    email,
    password,
});
if (response.data && response.data.success === false) {
    return setError(response.data.msg);
}
return setProfile(response);
    │   ├── sign-out
    │   └── sign-up
    ├── billing
    ├── dashboard
    ├── profile
    ├── rtl
    ├── tables
    └── virtual-reality

84 directories
--#
