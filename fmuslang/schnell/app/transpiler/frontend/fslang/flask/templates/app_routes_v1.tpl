from flask import Blueprint
from flask_restful import Api

from .resource import __TEMPLATE_TABLENAME_CASE__Detail, __TEMPLATE_TABLENAME_CASE__List

blueprint = Blueprint(
  '__TEMPLATE_TABLENAME_LOWER___blueprint', 
  __name__, 
  url_prefix='__TEMPLATE_URL_PREFIX',
  template_folder='templates',
	static_folder='static'
)
api = Api(blueprint)

api.add_resource(__TEMPLATE_TABLENAME_CASE__Detail, '/__TEMPLATE_TABLENAME_LOWER__s/<int:__TEMPLATE_TABLENAME_LOWER___id>')
api.add_resource(__TEMPLATE_TABLENAME_CASE__List, '/__TEMPLATE_TABLENAME_LOWER__s')
