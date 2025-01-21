from app.dirutils import (
  ayah, 
  joiner, 
  here,
)
from app.fileutils import append_file
from app.utils import (
  env_get, env_int,
)
# from db.bantuan.common import (
#   __CURDIR__,
#   get_env,
# )

disini = here(__file__)
from db.bantuan.config import output_folder
# filepath_output = joiner(disini, 'node-pg-antd-output.mk')
filepath_output = joiner(output_folder, 'node-pg-antd-output.mk')
# templatedir = joiner(__CURDIR__, 'templates')
# nodejs_sequelize_template = joiner(templatedir, 'node_pg_antd.mk')
node_pg_antd_template = joiner(disini, 'node-pg-antd.mk')


QuoteChar = '$$$'
ReplaceQuoteChar = '"'
EmptyReplaceQuoteChar = ''

sequelize_type_mapper = {
  'array_of':     'ARRAY(__SUBTYPE__)',
	'bigint':       'BIGINT',
	'boolean':      'BOOLEAN',
	'date':         'DATE',
  'decimal':      'DECIMAL',
	'double':       'DOUBLE',
	'enum':         'ENUM',
	'float':        'FLOAT',
  'image':        'STRING',
	'integer':      'INTEGER',
	'number':       'DECIMAL',
	'string':       'STRING',
	'text':       	'TEXT',
	# 'timestamp':    ReplaceQuoteChar + 'TIMESTAMP' + ReplaceQuoteChar,
  'timestamp':    '__DQTIMESTAMP__DQ',
  # 'timestamp':    'TIMESTAMP',
	'uuid':       	'UUID',
	'uuid1':       	'UUIDV1',
	'uuid4':       	'UUIDV4',
	'varchar':      'STRING',

  # 'django_foreign_key':			  '{ type: mongoose.Schema.ObjectId, ref: ModelRujukan, required: true, }',
  'django_foreign_key':			  '{ type: STRING, allowNull: false, references: __DQModelRujukan__DQ, }',
  'django_many_to_many':		  '[{ type: String }]',	
  'django_one_to_one':			  '[{ type: String }]',

  'auto':         '{ type: Number, required: true, }',
	'slug':         'STRING',

	# 'email':                  'models.EmailField',	
	# 'django_one_to_many':			'models.OneToManyField',
}


nodejs_mongoose_model_template = """
import mongoose from 'mongoose';

const fieldsMap = {
__FIELDS__
}

const optionsMap = { 
__TABtimestamps: true 
}

const __TABLENAMELOWER__Schema = new mongoose.Schema(
__TABfieldsMap,
__TABoptionsMap,
);

export default mongoose.model("__TABLENAME__", __TABLENAMELOWER__Schema);
"""

nodejs_sequelize_model_template = """
import { default as dbConnect } from 'D';
import {
  ARRAY,
	BIGINT, 
	BOOLEAN, 
	DATE,
  DECIMAL,
	DOUBLE, 
	ENUM, 
	FLOAT, 
	INTEGER, 
	STRING, 
	TEXT, 
	UUID, 
	UUIDV1, 
	UUIDV4,
} from 'sequelize';

const tableName = '__TABLENAME_LOWER_PLURAL__';

const fieldsMap = __FIELDS__;

const optionsMap = {
__TABfreezeTableName: true,
__TABschema: process.env.DB_SCHEMA,
__TABtimestamps: false,
};

const __TABLENAME__ = dbConnect.define(
__TABtableName,
__TABfieldsMap,
__TABoptionsMap,
);

/*
if (parseInt(process.env.DB_SYNC)===1) {
	console.log(`\n\nDO SYNC'ing database...`);
	dbConnect.sync({force: true});
} else {
	console.log(`\n\nnot synching database...`);
}
*/

export default __TABLENAME__;
"""

__TEMPLATE_APP_CONTENT_MK_ENTRY = """
			__TEMPLATE_APP$$GANTI_DENGAN_INDEX$$,d(/mk)
        %__TEMPLATE_Modelname=$$GANTI_DENGAN_MODEL_TITLE$$
				%__TEMPLATE_MODELNAME=$$GANTI_DENGAN_MODEL_UPPER$$
				%__TEMPLATE_modelname=$$GANTI_DENGAN_MODEL_LOWER$$
        %__TEMPLATE_MODELNAMES=$$GANTI_DENGAN_MODEL_UPPER_PLURAL$$
				%__TEMPLATE_modelnames=$$GANTI_DENGAN_MODEL_LOWER_PLURAL$$
				models,d(/mk)
					mongo.js,f(e=utama=webpack-express/src/apps/$$GANTI_DENGAN_MODEL_LOWER$$/models/mongo.js)
					postgres.js,f(e=utama=webpack-express/src/apps/$$GANTI_DENGAN_MODEL_LOWER$$/models/postgres.js)
					index.js,f(e=utama=webpack-express/src/apps/$$GANTI_DENGAN_MODEL_LOWER$$/models/index.js)
"""

__TEMPLATE_APP_CONTENT_APPMODELS = """
import User from './user/models';
// import Task from './task/models';
__TEMPLATE_IMPORT_MODELS__

import ExtenderUser from './user/extender.js';
// import ExtenderAdmin from './admin/extender.js';
__TEMPLATE_IMPORT_EXTENDERS__

// khusus mongo
// dummy utk aktivasi mongo connect = Log
// import dbConnect from 'D';
// export const LogModel = dbConnect.model("Log", new dbConnect.Schema({ content: String, },));

const AppModels = {
  base: {
    // 'task': Task, 
__TEMPLATE_MAPPING_BASE__
    'user': User,
  },

  extenders: [
__TEMPLATE_ENTRY_EXTENDER__
    ExtenderUser,    
  ]
};

export default AppModels;
"""

"""
				task,d(/mk)
					extender.js,f(e=utama=/np/node-postgres/src/apps/task/extender.js)
					models,d(/mk)
						mongo.js,f(e=utama=/np/node-postgres/src/apps/task/models/mongo.js)
						postgres.js,f(e=utama=/np/node-postgres/src/apps/task/models/postgres.js)
						index.js,f(e=utama=/np/node-postgres/src/apps/task/models/index.js)
"""

node_sequelize_app_mk_template = """
__TAB(4)$$GANTI_DENGAN_MODEL_LOWER$$,d(/mk)
__TAB(5)%__TEMPLATE_MODELNAME=$$GANTI_DENGAN_MODEL_UPPER$$
__TAB(5)%__TEMPLATE_Modelname=$$GANTI_DENGAN_MODEL_TITLE$$
__TAB(5)%__TEMPLATE_modelname=$$GANTI_DENGAN_MODEL_LOWER$$
__TAB(5)%__TEMPLATE_MODELNAMES=$$GANTI_DENGAN_MODEL_UPPER_PLURAL$$
__TAB(5)%__TEMPLATE_modelnames=$$GANTI_DENGAN_MODEL_LOWER_PLURAL$$
__TAB(5)extender.js,f(e=utama=/np/node-postgres/src/apps/$$GANTI_DENGAN_MODEL_LOWER$$/extender.js)
__TAB(5)models,d(/mk)
__TAB(6)mongo.js,f(e=utama=/np/node-postgres/src/apps/$$GANTI_DENGAN_MODEL_LOWER$$/models/mongo.js)
__TAB(6)postgres.js,f(e=utama=/np/node-postgres/src/apps/$$GANTI_DENGAN_MODEL_LOWER$$/models/postgres.js)
__TAB(6)index.js,f(e=utama=/np/node-postgres/src/apps/$$GANTI_DENGAN_MODEL_LOWER$$/models/index.js)
"""

"""
				Task,d(/mk)
					UpdateForm.js,f(e=utama=/np/react-antd/components/modules/Task/UpdateForm.js)
					FormProvider.js,f(e=utama=/np/react-antd/components/modules/Task/FormProvider.js)
					FormWrapper.js,f(e=utama=/np/react-antd/components/modules/Task/FormWrapper.js)
					Modal.js,f(e=utama=/np/react-antd/components/modules/Task/Modal.js)
					Task.js,f(e=utama=/np/react-antd/components/modules/Task/Task.js)
					CreateForm.js,f(e=utama=/np/react-antd/components/modules/Task/CreateForm.js)
					List.js,f(e=utama=/np/react-antd/components/modules/Task/List.js)
"""

react_antd_app_mk_template = """
__TAB(4)$$GANTI_DENGAN_MODEL_TITLE$$,d(/mk)
__TAB(5)%__TEMPLATE_MODELNAME=$$GANTI_DENGAN_MODEL_UPPER$$
__TAB(5)%__TEMPLATE_Modelname=$$GANTI_DENGAN_MODEL_TITLE$$
__TAB(5)%__TEMPLATE_modelname=$$GANTI_DENGAN_MODEL_LOWER$$
__TAB(5)%__TEMPLATE_MODELNAMES=$$GANTI_DENGAN_MODEL_UPPER_PLURAL$$
__TAB(5)%__TEMPLATE_modelnames=$$GANTI_DENGAN_MODEL_LOWER_PLURAL$$
__TAB(5)CreateForm.js,f(e=utama=/np/react-antd/components/modules/$$GANTI_DENGAN_MODEL_TITLE$$/CreateForm.js)
__TAB(5)FormProvider.js,f(e=utama=/np/react-antd/components/modules/$$GANTI_DENGAN_MODEL_TITLE$$/FormProvider.js)
__TAB(5)FormWrapper.js,f(e=utama=/np/react-antd/components/modules/$$GANTI_DENGAN_MODEL_TITLE$$/FormWrapper.js)
__TAB(5)List.js,f(e=utama=/np/react-antd/components/modules/$$GANTI_DENGAN_MODEL_TITLE$$/List.js)
__TAB(5)Modal.js,f(e=utama=/np/react-antd/components/modules/$$GANTI_DENGAN_MODEL_TITLE$$/Modal.js)
__TAB(5)UpdateForm.js,f(e=utama=/np/react-antd/components/modules/$$GANTI_DENGAN_MODEL_TITLE$$/UpdateForm.js)
__TAB(5)$$GANTI_DENGAN_MODEL_TITLE$$.js,f(e=utama=/np/react-antd/components/modules/$$GANTI_DENGAN_MODEL_TITLE$$/$$GANTI_DENGAN_MODEL_TITLE$$.js)
"""

"""
--% /np/react-antd/assets/task.json
{
  "headers": [
    "",
    "id",
    "title",
    "description",    
    "period_type",

    "delete"
  ],
  "widths": {
    "show": 50,
    "id": 30,
    "hapus": 30,
    "normal": 150
  }
}
--#

/np/react-antd/assets/menu.json
  {
    "label": "Task",
    "children": [
      { "label": "Create", "link": "task" },
      { "label": "Read", "link": "task" },
      { "label": "Update", "link": "task" },
      { "label": "Delete", "link": "task" }
    ]
  },
"""

react_antd_app_json_template = """
__TAB(3)$$GANTI_DENGAN_MODEL_LOWER$$.json,f(e=utama=/np/react-antd/assets/$$GANTI_DENGAN_MODEL_LOWER$$.json)
"""

"""
/np/react-antd/components/Route/Routes.js
import Task from 'modules/Task/Task';
  { 
    name: 'Task', 
    path: '/task', 
    icon: 'group', 
    exact: true, 
    component: Task, 
    roles: [], 
  },
"""

react_antd_app_route_template = """
  { 
    name: '__TABLENAME__',
    path: '/__TABLENAME_LOWER__',
    icon: 'group', 
    exact: true,
    component: __TABLENAME__,
    roles: [],
  },
"""

react_antd_app_asset_json = """
{
  "headers": [
    "",
    "id",

__TEMPLATE_APP_ASSET_JSON

    "delete"
  ],
  "widths": {
    "show": 50,
    "id": 30,
    "hapus": 30,
    "normal": 150
  }
}

"""


def append_entry(filepath_output, header, body):
	"""
	/apps/{tablename}/models.py
	"""
	start='--%'
	end='--#'
	# header = f'/apps/{tablename}/models.py'
	entry_model = f'\n{start} {header}\n' + body + f'\n{end}\n'
	append_file(filepath_output, entry_model)
	return entry_model
