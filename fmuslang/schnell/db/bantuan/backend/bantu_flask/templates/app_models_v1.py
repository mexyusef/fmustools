from flask import url_for
from datetime import datetime

from project.main.extensions import db, ma
from project.apps.common import PaginatedAPIMixin

# https://flask-marshmallow.readthedocs.io/en/latest/
class __TEMPLATE_TABLENAME_CASE__Schema(ma.Schema):
	class Meta:
		fields = (__COLUMN_LIST__)

class __TEMPLATE_TABLENAME_CASE__(PaginatedAPIMixin, db.Model):
  __tablename__ = '__TEMPLATE_TABLENAME_LOWER__s'
__TEMPLATE_COLUMNS__

  def __repr__(self):
    return f'<__TEMPLATE_TABLENAME_CASE__ {self.__TEMPLATE_CHOOSE_COLUMN_REPR__}>'

  def to_json(self):
    data = {
      'id': self.id,
__TEMPLATE_TOJSON__
    }
    return data

  def to_dict(self):
    data = {
      'id': self.id,
__TEMPLATE_TODICT__
      # '_links': {
      #   'self': url_for('api.get_order', id=self.id),
      #   'cart_items': url_for('api.get_cart_items', id=self.id)
      # }
    }
    return data

