from db.bantuan.common import (	
	tab,
)
from ..common import (
  append_entry,
	filepath_output,
)
from .apps_index import (
  template_apps_index,
  template_dummy_extender,
  template_models_index,
)


def gen_apps_models_index(configuration):
  tables = configuration['table_nodes']
  for index, tbl in enumerate(tables,1):
    content = template_models_index.replace('__TEMPLATE_Modelname', tbl.model)
    header = f'/np/node-postgres/src/apps/{tbl.model.lower()}/models/index.js'
    entrify = append_entry(filepath_output,	header, content)

def gen_apps_dummy_extender(configuration):
  tables = configuration['table_nodes']
  for index, tbl in enumerate(tables,1):
    content = template_dummy_extender
    header = f'/np/node-postgres/src/apps/{tbl.model.lower()}/extender.js'
    entrify = append_entry(filepath_output,	header, content)


def gen_apps_index_main(configuration):
  tables = configuration['table_nodes']

  base_import_parts = []
  extender_import_parts = []
  base_map_parts = []
  extender_map_parts = []

  for index, tbl in enumerate(tables,1):
    model_low = tbl.model.lower()
    model_cap = tbl.model

    # import Review from './review/models';
    entry1 = f"import {model_cap} from './{model_low}/models';"
    # import ExtenderReview from './review/extender.js';
    entry2 = f"import Extender{model_cap} from './{model_low}/extender.js';"
    # 'review': Review,
    entry3 = f"'{model_low}': {model_cap},"
    # ExtenderReview,
    entry4 = f"Extender{model_cap},"

    base_import_parts.append(entry1)
    extender_import_parts.append(entry2)
    base_map_parts.append(tab(2)+entry3)
    extender_map_parts.append(tab(2)+entry4)

  # content = form_model.replace('__TEMPLATE_modelname', tbl.model.lower())
  changer1 = '\n'.join(base_import_parts)
  changer2 = '\n'.join(extender_import_parts)
  changer3 = '\n'.join(base_map_parts)
  changer4 = '\n'.join(extender_map_parts)
  content = template_apps_index.replace('__TEMPLATE_BASE_IMPORT_PARTS', changer1)
  content = content.replace('__TEMPLATE_EXTENDER_IMPORT_PARTS', changer2)
  content = content.replace('__TEMPLATE_BASE_PARTS', changer3)
  content = content.replace('__TEMPLATE_EXTENDER_PARTS', changer4)

  header = f'/np/node-postgres/src/apps/index.js/hasil_creation'
  entrify = append_entry(filepath_output,	header, content)


def gen_apps_index(configuration):
  gen_apps_index_main(configuration)
  gen_apps_dummy_extender(configuration)
  gen_apps_models_index(configuration)
