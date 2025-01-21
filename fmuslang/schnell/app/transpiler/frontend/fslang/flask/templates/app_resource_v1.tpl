import json
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from flask import jsonify, make_response, request
from project.apps.__TEMPLATE_TABLENAME_LOWER__.models import __TEMPLATE_TABLENAME_CASE__, __TEMPLATE_TABLENAME_CASE__Schema
from project.main.db.sqlite.index import db_session
from project.main.extensions import db

class __TEMPLATE_TABLENAME_CASE__Detail(Resource):
	"""
	detail, update, delete
	"""

	def get(self, __TEMPLATE_TABLENAME_LOWER___id):
		# schema = __TEMPLATE_TABLENAME_CASE__Schema()
		# __TEMPLATE_TABLENAME_LOWER__ = __TEMPLATE_TABLENAME_CASE__.query.get_or_404(__TEMPLATE_TABLENAME_LOWER___id)
		# return {"__TEMPLATE_TABLENAME_LOWER__": schema.dump(__TEMPLATE_TABLENAME_LOWER__).data}
		__TEMPLATE_TABLENAME_LOWER__ = __TEMPLATE_TABLENAME_CASE__.query.filter_by(id=__TEMPLATE_TABLENAME_LOWER___id).first()
		return __TEMPLATE_TABLENAME_LOWER__

	def put(self, __TEMPLATE_TABLENAME_LOWER___id):
		schema = __TEMPLATE_TABLENAME_CASE__Schema(partial=True)
		__TEMPLATE_TABLENAME_LOWER__ = __TEMPLATE_TABLENAME_CASE__.query.get_or_404(__TEMPLATE_TABLENAME_LOWER___id)
		__TEMPLATE_TABLENAME_LOWER__, errors = schema.load(request.json, instance=__TEMPLATE_TABLENAME_LOWER__)
		if errors:
			return errors, 422

		return {"msg": "__TEMPLATE_TABLENAME_LOWER__ updated", "__TEMPLATE_TABLENAME_LOWER__": schema.dump(__TEMPLATE_TABLENAME_LOWER__).data}

	def delete(self, __TEMPLATE_TABLENAME_LOWER___id):
		__TEMPLATE_TABLENAME_LOWER__ = __TEMPLATE_TABLENAME_CASE__.query.get_or_404(__TEMPLATE_TABLENAME_LOWER___id)
		db.session.delete(__TEMPLATE_TABLENAME_LOWER__)
		db.session.commit()

		return {"msg": "__TEMPLATE_TABLENAME_LOWER__ deleted"}


class __TEMPLATE_TABLENAME_CASE__List(Resource):
	"""
	list, create
	"""

	def get(self):
		schema = __TEMPLATE_TABLENAME_CASE__Schema(many=True)
		data = __TEMPLATE_TABLENAME_CASE__.query.all()
		# result = {
		# 	'data'		: [item.to_json() for item in data],
		# 	'total'		: len(data),
		# }
		# return result
		return schema.dump(data)

	def post(self):
		schema = __TEMPLATE_TABLENAME_CASE__Schema()
		__TEMPLATE_TABLENAME_LOWER__, errors = schema.load(request.json)
		if errors:
			return errors, 422

		db.session.add(__TEMPLATE_TABLENAME_LOWER__)
		db.session.commit()

		return {"msg": "__TEMPLATE_TABLENAME_LOWER__ created", "__TEMPLATE_TABLENAME_LOWER__": schema.dump(__TEMPLATE_TABLENAME_LOWER__).data}, 201
