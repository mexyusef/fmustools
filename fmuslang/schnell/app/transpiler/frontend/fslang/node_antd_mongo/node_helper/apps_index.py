

# index.js,f(e=utama=/np/node-postgres/src/apps/index.js/hasil_creation)
# --% /np/node-postgres/src/apps/index.js

template_models_index = """
import __TEMPLATE_Modelname from './mongo';
// import __TEMPLATE_Modelname from './postgres';

export default __TEMPLATE_Modelname;
"""

template_dummy_extender = """
// import Category from './models';
// import Product from '../product/models';

// const ExtenderObj = {
//   find_by_category: async(req, res) => {
//     res.json({ category, products, });
//   },
// }

const ExtensionRouter = Router => Router
  // http://localhost:9101/find_by_category/misc
  // .get("/find_by_category/:slug", ExtenderObj.find_by_category)

  // .post("/create-or-update-user", ExtenderObj.createOrUpdateUser)
  // .post("/current-user", ExtenderObj.currentUser)
  // .post("/current-admin", ExtenderObj.currentUser)
  // .post("/api/users/login", AuthProvider.login)
  // .post("/api/users/register", AuthProvider.register)
  // .post("/api/users/update_password", AuthProvider.updatePassword)
  ;
export default ExtensionRouter;
"""

# __TEMPLATE_Modelname
# __TEMPLATE_modelname
template_apps_index = """
__TEMPLATE_BASE_IMPORT_PARTS
__TEMPLATE_EXTENDER_IMPORT_PARTS

// khusus mongo
// dummy utk aktivasi mongo connect = Log
// import dbConnect from 'D';
// export const LogModel = dbConnect.model("Log", new dbConnect.Schema({ content: String, },));

const AppModels = {
  base: {
__TEMPLATE_BASE_PARTS    
  },
  extenders: [    
__TEMPLATE_EXTENDER_PARTS
  ]
};

export default AppModels;
"""
