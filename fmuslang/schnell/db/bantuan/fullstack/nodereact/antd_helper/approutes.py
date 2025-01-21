
# Routes.js,f(e=utama=/np/react-antd/components/Route/Routes.js)
# --% /np/react-antd/components/Route/Routes.js

app_route_item = """
  { 
    name: '__TEMPLATE_Modelname', 
    path: '/__TEMPLATE_modelname', 
    icon: 'group', 
    exact: true, 
    component: __TEMPLATE_Modelname, 
    roles: [], 
  },
"""

app_routes = """
import Dashboard from 'modules/Dashboard/Dashboard';

__TEMPLATE_APP_ROUTE_IMPORT_ITEMS

export default [

  { 
    name: 'Dashboard', 
    path: '/dashboard', 
    icon: 'group', 
    exact: true, 
    component: Dashboard, 
    roles: [], 
  },

__TEMPLATE_APP_ROUTE_ITEMS

];
"""
