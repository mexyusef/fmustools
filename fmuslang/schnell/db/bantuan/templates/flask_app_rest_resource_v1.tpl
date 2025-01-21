import json
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from flask import request, jsonify, make_response
from project.apps.user.model import User
from project.main.db.sqlite.index import db_session

# class UserResource(Resource):
# 	parser = RequestParser()
# 	parser.add_argument('email', type=str, location='json', help="Email must be filled", required=True)
# 	parser.add_argument('name', type=str, location='json', help="Name must be filled", required=True)
# 	parser.add_argument("password", type=str, location="json", help="Password must be filled", required=True)
# 	parser.add_argument("address", type=str, location="json")

# 	def get(self, **kwargs):
# 		users = User.query.all()
# 		return jsonify({
# 			'users': [str(u) for u in users]
# 		})

# 	def post(self, **kwargs):
# 		args = self.parser.parse_args()
# 		print('post args:', args)
# 		if not 'email' in args:
# 			return {
# 				"message": "Harus ada email",
# 			}, 400
# 		if not 'name' in args:
# 			return {
# 				"message": "Harus ada name",
# 			}, 400
# 		if not 'password' in args:
# 			return {
# 				"message": "Harus ada password",
# 			}, 400

# 		params = (args['name'], args['email'], args['password'])
# 		if 'address' in args and args['address'] is not None:
# 			params .extend(args['address'])

# 		user = User(*params)
# 		db_session.add(user)
# 		db_session.commit()
# 		return {
# 			"message": "User {} telah berhasil dibuat".format(args['email']),
# 			"data": str(user)
# 		}, 201

from flask import jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
# from marshmallow_sqlalchemy import ModelSchema
from project.main.extensions import ma, db
from project.apps.common import paginate

from .model import User

# https://stackoverflow.com/questions/57984649/marshmallow-object-has-no-attribute-modelschema
class UserSchema(ma.SQLAlchemySchema):

	password = ma.String(load_only=True, required=True)

	class Meta:
		model = User
		# load_instance = True
		# sqla_session = db.session


class UserDetail(Resource):
	"""
	detail, update, delete
	"""
	# method_decorators = [jwt_required()]

	def get(self, user_id):
		schema = UserSchema()
		user = User.query.get_or_404(user_id)
		return {"user": schema.dump(user).data}

	def put(self, user_id):
		schema = UserSchema(partial=True)
		user = User.query.get_or_404(user_id)
		user, errors = schema.load(request.json, instance=user)
		if errors:
			return errors, 422

		return {"msg": "user updated", "user": schema.dump(user).data}

	def delete(self, user_id):
		user = User.query.get_or_404(user_id)
		db.session.delete(user)
		db.session.commit()

		return {"msg": "user deleted"}


class UserList(Resource):
	"""
	list, create
	"""
	# method_decorators = [jwt_required()]

	def get(self):
		schema = UserSchema(many=True)
		# query = User.query
		# data = list(query)
		data = User.query.all()
		# return paginate(query, schema)
		result = {
			'data'		: [item.to_json() for item in data],
			'total'		: len(data),
		}
		return result

	def post(self):
		schema = UserSchema()
		user, errors = schema.load(request.json)
		if errors:
			return errors, 422

		db.session.add(user)
		db.session.commit()

		return {"msg": "user created", "user": schema.dump(user).data}, 201
