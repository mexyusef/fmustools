--% program/fm.us
__REPLACE_WITH_PROJECT_DIR_OR_INPUT__,d(/mk)
	%utama=__FILE__
	#%tambahan=/home/usef/danger/ulib/schnell/db/bantuan/backend/bantu_flask/resource.mk
	%tambahan=/home/usef/work/ulibs/schnell/db/bantuan/backend/bantu_flask/resource.mk
	%__TEMPLATE_SERVER_PORT__=9000
	%__TEMPLATE_URL_PREFIX=/api
__TEMPLATE_DB_INIT
__TEMPLATE_APP_INIT
	manage.py,f(e=utama=/myflask2/manage.py)
	__init__.py,f(e=utama=/myflask2/__init__.py)
	work.fmus,f(e=utama=/myflask2/work.fmus)
	.env,f(e=utama=/myflask2/.env)
	config.py,f(e=utama=/myflask2/config.py)  
	server.py,f(e=utama=/myflask2/server.py)
	run.sh,f(e=utama=/myflask2/run.sh)
	manual.sh,f(e=utama=/myflask2/manual.sh)
	populate.sh,f(e=utama=/myflask2/populate.sh)
	$*chmod a+x *.sh
	project,d(/mk)
		__init__.py,f(e=utama=/myflask2/project/__init__.py)
		apps,d(/mk)
			__init__.py,f(e=utama=/myflask2/project/apps/__init__.py)
			common.py,f(e=utama=/myflask2/project/apps/common.py)
			user,d(/mk)
				model.py,f(e=utama=/myflask2/project/apps/user/model.py)
				__init__.py,f(e=utama=/myflask2/project/apps/user/__init__.py)
				util.py,f(e=utama=/myflask2/project/apps/user/util.py)
				forms.py,f(e=utama=/myflask2/project/apps/user/forms.py)
				resource.py,f(e=utama=/myflask2/project/apps/user/resource.py)
				static,d(/mk)
				templates,d(/mk)
					index.html,f(e=utama=/myflask2/project/apps/user/templates/index.html)
					layouts,d(/mk)
						base.html,f(e=utama=/myflask2/project/apps/user/templates/layouts/base.html)
						base-fullscreen.html,f(e=utama=/myflask2/project/apps/user/templates/layouts/base-fullscreen.html)
					includes,d(/mk)
						settings-box.html,f(e=utama=/myflask2/project/apps/user/templates/includes/settings-box.html)
						sidebar.html,f(e=utama=/myflask2/project/apps/user/templates/includes/sidebar.html)
						navigation.html,f(e=utama=/myflask2/project/apps/user/templates/includes/navigation.html)
						footer.html,f(e=utama=/myflask2/project/apps/user/templates/includes/footer.html)
						scripts.html,f(e=utama=/myflask2/project/apps/user/templates/includes/scripts.html)
					accounts,d(/mk)
						register.html,f(e=utama=/myflask2/project/apps/user/templates/accounts/register.html)
						login.html,f(e=utama=/myflask2/project/apps/user/templates/accounts/login.html)
			home,d(/mk)
				__init__.py,f(e=utama=/myflask2/project/apps/home/__init__.py)
				static,d(/mk)
					assets,d(/mk)
						img,d(/mk)
						css,d(/mk)
							volt.min.css,f(e=tambahan=/myflask2/project/apps/home/static/assets/css/volt.min.css)
						js,d(/mk)
							volt.js,f(e=utama=/myflask2/project/apps/home/static/assets/js/volt.js)
				templates,d(/mk)
					index.html,f(e=utama=/myflask2/project/apps/home/templates/index.html)
					page-500.html,f(e=utama=/myflask2/project/apps/home/templates/page-500.html)
					page-404.html,f(e=utama=/myflask2/project/apps/home/templates/page-404.html)
					page-403.html,f(e=utama=/myflask2/project/apps/home/templates/page-403.html)
__TEMPLATE_SERVER_APP_CONTENT
		main,d(/mk)
			wsgi.py,f(e=utama=/myflask2/project/main/wsgi.py)
			__init__.py,f(e=utama=/myflask2/project/main/__init__.py)
			index.py,f(e=utama=/myflask2/project/main/index.py)
			extensions.py,f(e=utama=/myflask2/project/main/extensions.py)
			router.py,f(e=utama=/myflask2/project/main/router.py)
			loader.py,f(e=utama=/myflask2/project/main/loader.py)
			resource.py,f(e=utama=/myflask2/project/main/resource.py)
			db,d(/mk)
				sqlite,d(/mk)
					index.py,f(e=utama=/myflask2/project/main/db/sqlite/index.py)

	# $*qterminal 2>/dev/null &
--#

--% /myflask2/manage.py
import click
from flask.cli import FlaskGroup
from project.main import create_app


def create_flask_app(info):
	return create_app(do_migrate=True)


@click.group(cls=FlaskGroup, create_app=create_flask_app)
def cli():
	"""
	Main entry point
	"""

@cli.command("init")
def init():
	"""
	migration etc
	"""
	from project.main.extensions import db
	from project.apps.user.model import User
	click.echo("create database")
	db.create_all()
	click.echo("done")

	click.echo("create user")
	user = User(
		username='usef',
		email='usef@gmail.com',
		password='rahasia',
		active=True
	)
	db.session.add(user)
	click.echo("create user")

	db.session.commit()
	click.echo("user admin and initial data created")


# ini gak bisa python manage.py do_migrate
@cli.command("do_migrate")
def do_migrate_fn():
	print('press any key to start migrating...', end='')
	input(' ')
	click.echo('ready to go!')
	init()


if __name__ == "__main__":
	cli()

--#

--% /myflask2/__init__.py

--#

--% /myflask2/work.fmus

**.,d
	config.py,f(t=)
	server.py,f(t=)
	run.sh,f(t=)
	project,d(/mk)
		apps,d(/mk)
			user,d(/mk)
		main,d(/mk)
			db,d(/mk)
				sqlite,d(/mk)
			loader.py,f(t=)
			index.py,f(t=)
			resource.py,f(t=)
			router.py,f(t=)

**.,d
	run.bat,f(t=)

term
gen

*~localhost:8083/api/user p json {email=usef@gmail.com,password=rahasia}

*~localhost:8083/api
*~localhost:8083/api/
*~localhost:8083/api/user
*~localhost:8083/api/user/

*~localhost:8083
Alive
--#

--% /myflask2/.env
DBUSER=__TEMPLATE_DBUSER
DBPASS=__TEMPLATE_DBPASS
DBNAME=__TEMPLATE_DBNAME
DBHOST=__TEMPLATE_DBHOST
DBPORT=__TEMPLATE_DBPORT
DBSQLITE=/tmp/__TEMPLATE_DBNAME.db
DATABASE=postgres
DEBUG=1
MODE=development
SECRET_KEY=the world is your oyster
--#

--% /myflask2/config.py
import os
from dotenv import load_dotenv
CURRENT_FILE = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(CURRENT_FILE, '.env'))

DEBUG = bool(int(os.environ.get('DEBUG')))
ENV = os.environ.get('MODE')
SECRET_KEY = os.environ.get('SECRET_KEY')

SQLITE = f"sqlite:///{os.environ.get('DBSQLITE')}"
POSTGRES = f"postgresql://{os.environ.get('DBUSER')}:{os.environ.get('DBPASS')}@{os.environ.get('DBHOST')}:{os.environ.get('DBPORT')}/{os.environ.get('DBNAME')}"
SQLALCHEMY_DATABASE_URI = SQLITE
if os.environ.get('DATABASE') == 'postgres':
	SQLALCHEMY_DATABASE_URI = POSTGRES
SQLALCHEMY_TRACK_MODIFICATIONS = False

APP_RESOURCES_KEY = "resources"
PROJ_FOLDER = "project"
APPS_FOLDER = "apps"
APPS_DIR = os.path.join(PROJ_FOLDER, APPS_FOLDER)
APPS_PREFIX = f"{PROJ_FOLDER}.{APPS_FOLDER}." # import project.apps.user
ABS_PATH = CURRENT_FILE

JWT_BLACKLIST_ENABLED = True
JWT_BLACKLIST_TOKEN_CHECKS = ['access', 'refresh']
--#

--% /myflask2/server.py
# import os, sys
# sys.path.insert(0, os.path.dirname(__file__))

from project.main import FlaskApp
app = FlaskApp(__name__, static_folder='./static')

# app.add_url_rule('/lampiran/<filename>', 'uploaded_file', build_only=True)
# from werkzeug.middleware.shared_data import SharedDataMiddleware
# app.wsgi_app = SharedDataMiddleware(app.wsgi_app, { '/lampiran': app.config['UPLOAD_FOLDER'] } )

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=__TEMPLATE_SERVER_PORT__)

--#

--% /myflask2/run.sh
# python /home/usef/common/working/_incub/oprek/newflask2/server.py
gunicorn --worker-class eventlet -b 0.0.0.0:__TEMPLATE_SERVER_PORT__ --no-sendfile --access-logfile - "project.main:create_app()"
--#

--% /myflask2/manual.sh
python $(pwd)/server.py
--#

--% /myflask2/populate.sh
python manage.py init

--#

--% /myflask2/project/__init__.py

--#

--% /myflask2/project/apps/__init__.py
# all apps
--#

--% /myflask2/project/apps/common.py
from flask import url_for, request
import binascii, hashlib, os
from project.main.extensions import pwd_context


DEFAULT_PAGE_SIZE = 50
DEFAULT_PAGE_NUMBER = 1


def paginate(query, schema):
	page = request.args.get('page', DEFAULT_PAGE_NUMBER)
	per_page = request.args.get('page_size', DEFAULT_PAGE_SIZE)
	page_obj = query.paginate(page=page, per_page=per_page)

	next = url_for(
		request.endpoint,
		page=page_obj.next_num if page_obj.has_next else page_obj.page,
		per_page=per_page,
		**request.view_args
	)
	prev = url_for(
		request.endpoint,
		page=page_obj.prev_num if page_obj.has_prev else page_obj.page,
		per_page=per_page,
		**request.view_args
	)

	return {
		'total': page_obj.total,
		'pages': page_obj.pages,
		'next': next,
		'prev': prev,
		# 'results': schema.dump(page_obj.items).data
		'results': schema.dump(page_obj.items)
	}


class PaginatedAPIMixin(object):
	@staticmethod
	def to_collection_dict(query, page, per_page, endpoint, **kwargs):
		resources = query.paginate(page, per_page, False)
		data = {
			'items': [item.to_dict() for item in resources.items],
			'_meta': {
				'page': page,
				'per_page': per_page,
				'total_pages': resources.pages,
				'total_items': resources.total
			},
			'_links': {
				'self': url_for(endpoint, page=page, per_page=per_page, **kwargs),
				'next': url_for(endpoint, page=page + 1, per_page=per_page, **kwargs) if resources.has_next else None,
				'prev': url_for(endpoint, page=page - 1, per_page=per_page, **kwargs) if resources.has_prev else None
			}
		}
		return data


def hash_pass( password ):
	"""Hash a password for storing."""
	return pwd_context.hash(password)


def hash_pass2( password ):
	"""Hash a password for storing."""
	salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
	pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
	pwdhash = binascii.hexlify(pwdhash)
	return (salt + pwdhash) # return bytes


def hashing1(stored_password):
	salt = stored_password[:64]
	stored_password = stored_password[64:]

	pwdhash = hashlib.pbkdf2_hmac('sha512', 
		provided_password.encode('utf-8'), 
		salt.encode('ascii'), 
		100000)

	pwdhash = binascii.hexlify(pwdhash).decode('ascii')
	return pwdhash


def hashing2(supplied_password, stored_password):	
	return pwd_context.verify(supplied_password, stored_password)


def verify_pass(provided_password, stored_password):
	"""Verify a stored password against one provided by user"""
	print(f'flask/apps/user/util/verify_pass #1 = terima = [{provided_password}] db = [{stored_password}], jenis = {type(stored_password)}')
	if not isinstance(stored_password, str):
		stored_password = stored_password.decode('ascii')

	# pwdhash = hashing1(stored_password)
	# print(f'flask/apps/user/util/verify_pass #2 = hitung = [{pwdhash}] db = [{stored_password}], jenis = {type(stored_password)}')
	# return pwdhash == stored_password

	return hashing2(provided_password, stored_password)

--#

--% /myflask2/project/apps/user/model.py
# from sqlalchemy import Column, Integer, String
# from project.main.db.sqlite.index import Base

# class User(Base):
# 	__tablename__ = 'users'

# 	id = Column(Integer, primary_key=True)
# 	name = Column(String(50), unique=True)
# 	email = Column(String(120), unique=True)
# 	password = Column(String(120))
# 	address = Column(String(200))

# 	def __init__(self, name=None, email=None, password=None, address=None):
# 		self.name = name
# 		self.email = email
# 		self.password = password
# 		self.address = address

# 	def __repr__(self):
# 		return '<User %r (%s)>' % (self.name, self.email)
from flask_login import UserMixin
from project.main.extensions import db, login_manager, pwd_context


class User(db.Model, UserMixin):
	"""
	"""
	id 				= db.Column(db.Integer, primary_key=True)
	username 	= db.Column(db.String(80), unique=True, nullable=False)
	email 		= db.Column(db.String(80), unique=True, nullable=False)
	password 	= db.Column(db.String(255), nullable=False)
	active 		= db.Column(db.Boolean, default=True)


	def __init__(self, **kwargs):
		super(User, self).__init__(**kwargs)
		self.password = pwd_context.hash(self.password)

	def __repr__(self):
		return "<User %s>" % self.username

	def to_json(self):
		return {
			'id': self.id,
			'username': self.username,
			'email': self.email,
			'active': self.active
		}


@login_manager.user_loader
def user_loader(id):
	return User.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
	username = request.form.get('username')
	user = User.query.filter_by(username=username).first()
	return user if user else None

--#

--% /myflask2/project/apps/user/__init__.py
# from .resource import UserResource
# resources = (
# 	dict(
# 		rule = "/",
# 		resource_class = UserResource
# 	),
# )

from flask import Blueprint
from flask_restful import Api

from .resource import UserDetail, UserList

blueprint = Blueprint(
	'user_blueprint', 
	__name__, 
	url_prefix='/api',
	template_folder='templates',
	static_folder='static'
)
api = Api(blueprint)

api.add_resource(UserDetail, '/users/<int:user_id>')
api.add_resource(UserList, '/users')


from flask import (
	render_template, 
	redirect, 
	url_for, 
	request, 
	jsonify
)
from flask_login import (
	current_user,
	login_required,
	login_user,
	logout_user
)
from jinja2 import TemplateNotFound
from .forms import LoginForm, CreateAccountForm
from .model import User
from .util import verify_pass


@blueprint.route('/')
def route_default():
	return redirect(url_for('user_blueprint.login'))


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
	login_form = LoginForm(request.form)
	if 'login' in request.form:
		
		# read form data
		username = request.form['username']
		password = request.form['password']

		# Locate user
		user = User.query.filter_by(username=username).first()
		print(f'login => user adlh: {user}, pass adlh: {password}')
		verifikasi = verify_pass( password, user.password)
		print(f'login initial => verifikasi adlh: {verifikasi}')
		if user and verifikasi:
			login_user(user)
			print(f'login ok => verifikasi adlh: {verifikasi}')
			return redirect(url_for('user_blueprint.route_default'))

		# Something (user or pass) is not ok
		return render_template( 'accounts/login.html', msg='Wrong user or password', form=login_form)

	if not current_user.is_authenticated:
		return render_template( 'accounts/login.html', form=login_form)

	return redirect(url_for('home_blueprint.index'))


@blueprint.route('/register', methods=['GET', 'POST'])
def register():

	login_form = LoginForm(request.form)
	create_account_form = CreateAccountForm(request.form)

	if 'register' in request.form:

		username  = request.form['username']
		email     = request.form['email'   ]

		# Check usename exists
		user = User.query.filter_by(username=username).first()
		if user:
			return render_template( 'accounts/register.html', 
				msg='Username already registered',
				success=False,
				form=create_account_form)

		# Check email exists
		user = User.query.filter_by(email=email).first()
		if user:
			return render_template( 'accounts/register.html', 
				msg='Email already registered', 
				success=False,
				form=create_account_form)

		# else we can create the user
		user = User(**request.form)
		db.session.add(user)
		db.session.commit()

		return render_template( 'accounts/register.html', 
			msg='User created please <a href="/login">login</a>', 
			success=True,
			form=create_account_form)

	else:
		return render_template( 'accounts/register.html', form=create_account_form)


@blueprint.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('user_blueprint.login'))


# @login_manager.unauthorized_handler
def unauthorized_handler():
	return render_template('page-403.html'), 403


@blueprint.errorhandler(403)
def access_forbidden(error):
	return render_template('page-403.html'), 403


@blueprint.errorhandler(404)
def not_found_error(error):
	return render_template('page-404.html'), 404


@blueprint.errorhandler(500)
def internal_error(error):
	return render_template('page-500.html'), 500

--#

--% /myflask2/project/apps/user/util.py
import binascii, hashlib, os
from project.main.extensions import pwd_context


def hash_pass( password ):
	"""Hash a password for storing."""
	return pwd_context.hash(password)


def hash_pass2( password ):
	"""Hash a password for storing."""
	salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
	pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
	pwdhash = binascii.hexlify(pwdhash)
	return (salt + pwdhash) # return bytes


def hashing1(stored_password):
	salt = stored_password[:64]
	stored_password = stored_password[64:]

	pwdhash = hashlib.pbkdf2_hmac('sha512', 
		provided_password.encode('utf-8'), 
		salt.encode('ascii'), 
		100000)

	pwdhash = binascii.hexlify(pwdhash).decode('ascii')
	return pwdhash

def hashing2(supplied_password, stored_password):	
	return pwd_context.verify(supplied_password, stored_password)


def verify_pass(provided_password, stored_password):
	"""Verify a stored password against one provided by user"""
	print(f'flask/apps/user/util/verify_pass #1 = terima = [{provided_password}] db = [{stored_password}], jenis = {type(stored_password)}')
	if not isinstance(stored_password, str):
		stored_password = stored_password.decode('ascii')

	return hashing2(provided_password, stored_password)
	
--#

--% /myflask2/project/apps/user/forms.py

from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import InputRequired, Email, DataRequired

## login and registration

class LoginForm(FlaskForm):
	username = TextField    ('Username', id='username_login'   , validators=[DataRequired()])
	password = PasswordField('Password', id='pwd_login'        , validators=[DataRequired()])

class CreateAccountForm(FlaskForm):
	username = TextField('Username'     , id='username_create' , validators=[DataRequired()])
	email    = TextField('Email'        , id='email_create'    , validators=[DataRequired(), Email()])
	password = PasswordField('Password' , id='pwd_create'      , validators=[DataRequired()])

--#

--% /myflask2/project/apps/user/resource.py
import json
from flask_restful import Resource
from flask_restful.reqparse import RequestParser
from flask import request, jsonify, make_response
from project.apps.user.model import User
from project.main.db.sqlite.index import db_session

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

--#

--% /myflask2/project/apps/user/templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>User Blueprint</title>
</head>
<body>
	User Blueprint - Index
</body>
</html>

--#

--% /myflask2/project/apps/user/templates/layouts/base.html
<!DOCTYPE html>
<html lang="en">

<head> 
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<!-- Primary Meta Tags -->

<title>
	Flask Volt Dashboard - {% block title %}{% endblock %} | AppSeed
</title>

<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="title" content="Volt - Free Bootstrap 5 Dashboard">
<meta name="author" content="Themesberg">
<meta name="description" content="Volt Pro is a Premium Bootstrap 5 Admin Dashboard featuring over 800 components, 10+ plugins and 20 example pages using Vanilla JS.">
<meta name="keywords" content="bootstrap 5, bootstrap, bootstrap 5 admin dashboard, bootstrap 5 dashboard, bootstrap 5 charts, bootstrap 5 calendar, bootstrap 5 datepicker, bootstrap 5 tables, bootstrap 5 datatable, vanilla js datatable, themesberg, themesberg dashboard, themesberg admin dashboard" />
<link rel="canonical" href="https://appseed.us/admin-dashboards/flask-dashboard-volt">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://demo.themesberg.com/volt-pro">
<meta property="og:title" content="Volt - Free Bootstrap 5 Dashboard">
<meta property="og:description" content="Volt Pro is a Premium Bootstrap 5 Admin Dashboard featuring over 800 components, 10+ plugins and 20 example pages using Vanilla JS.">
<meta property="og:image" content="https://themesberg.s3.us-east-2.amazonaws.com/public/products/volt-pro-bootstrap-5-dashboard/volt-pro-preview.jpg">

<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="https://demo.themesberg.com/volt-pro">
<meta property="twitter:title" content="Volt - Free Bootstrap 5 Dashboard">
<meta property="twitter:description" content="Volt Pro is a Premium Bootstrap 5 Admin Dashboard featuring over 800 components, 10+ plugins and 20 example pages using Vanilla JS.">
<meta property="twitter:image" content="https://themesberg.s3.us-east-2.amazonaws.com/public/products/volt-pro-bootstrap-5-dashboard/volt-pro-preview.jpg">

<!-- Favicon -->
<link rel="apple-touch-icon" sizes="120x120" href="/static/assets/img/favicon/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/static/assets/img/favicon/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/static/assets/img/favicon/favicon-16x16.png">
<link rel="manifest" href="/static/assets/img/favicon/site.webmanifest">
<link rel="mask-icon" href="/static/assets/img/favicon/safari-pinned-tab.svg" color="#ffffff">
<meta name="msapplication-TileColor" content="#ffffff">
<meta name="theme-color" content="#ffffff">

<!-- Fontawesome -->
<link type="text/css" href="/static/assets/vendor/@fortawesome/fontawesome-free/css/all.min.css" rel="stylesheet">

<!-- Sweet Alert -->
<link type="text/css" href="/static/assets/vendor/sweetalert2/dist/sweetalert2.min.css" rel="stylesheet">

<!-- Notyf -->
<link type="text/css" href="/static/assets/vendor/notyf/notyf.min.css" rel="stylesheet">

<!-- Volt CSS -->
<link type="text/css" href="/static/assets/css/volt.css" rel="stylesheet">

</head>
<body>

	<nav class="navbar navbar-dark navbar-theme-primary px-4 col-12 d-md-none">
		<a class="navbar-brand me-lg-5" href="/">
			<img class="navbar-brand-dark" src="/static/assets/img/brand/light.svg" alt="Volt logo" /> <img class="navbar-brand-light" src="/static/assets/img/brand/dark.svg" alt="Volt logo" />
		</a>
		<div class="d-flex align-items-center">
			<button class="navbar-toggler d-md-none collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation">
			<span class="navbar-toggler-icon"></span>
			</button>
		</div>
	</nav>

	{% include 'includes/sidebar.html' %} 
	
	<main class="content">

	{% include 'includes/navigation.html' %}

	{% block content %}{% endblock content %}

	{% include 'includes/settings-box.html' %}

	{% include 'includes/footer.html' %}

	</main>

	{% include 'includes/scripts.html' %}

</body>
</html>


--#

--% /myflask2/project/apps/user/templates/layouts/base-fullscreen.html

<!DOCTYPE html>
<html lang="en">

<head> 
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<!-- Primary Meta Tags -->

<title>
	Flask Volt Dashboard - {% block title %}{% endblock %} | AppSeed
</title>

<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta name="title" content="Volt Free Bootstrap Dashboard - Sign up page">
<meta name="author" content="Themesberg">
<meta name="description" content="Volt Pro is a Premium Bootstrap 5 Admin Dashboard featuring over 800 components, 10+ plugins and 20 example pages using Vanilla JS.">
<meta name="keywords" content="bootstrap 5, bootstrap, bootstrap 5 admin dashboard, bootstrap 5 dashboard, bootstrap 5 charts, bootstrap 5 calendar, bootstrap 5 datepicker, bootstrap 5 tables, bootstrap 5 datatable, vanilla js datatable, themesberg, themesberg dashboard, themesberg admin dashboard" />
<link rel="canonical" href="https://appseed.us/admin-dashboards/flask-dashboard-volt">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://demo.themesberg.com/volt-pro">
<meta property="og:title" content="Volt Free Bootstrap Dashboard - Sign up page">
<meta property="og:description" content="Volt Pro is a Premium Bootstrap 5 Admin Dashboard featuring over 800 components, 10+ plugins and 20 example pages using Vanilla JS.">
<meta property="og:image" content="https://themesberg.s3.us-east-2.amazonaws.com/public/products/volt-pro-bootstrap-5-dashboard/volt-pro-preview.jpg">

<!-- Twitter -->
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:url" content="https://demo.themesberg.com/volt-pro">
<meta property="twitter:title" content="Volt Free Bootstrap Dashboard - Sign up page">
<meta property="twitter:description" content="Volt Pro is a Premium Bootstrap 5 Admin Dashboard featuring over 800 components, 10+ plugins and 20 example pages using Vanilla JS.">
<meta property="twitter:image" content="https://themesberg.s3.us-east-2.amazonaws.com/public/products/volt-pro-bootstrap-5-dashboard/volt-pro-preview.jpg">

<!-- Favicon -->
<link rel="apple-touch-icon" sizes="120x120" href="/static/assets/img/favicon/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="/static/assets/img/favicon/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/static/assets/img/favicon/favicon-16x16.png">
<link rel="manifest" href="/static/assets/img/favicon/site.webmanifest">
<link rel="mask-icon" href="/static/assets/img/favicon/safari-pinned-tab.svg" color="#ffffff">
<meta name="msapplication-TileColor" content="#ffffff">
<meta name="theme-color" content="#ffffff">

<!-- Fontawesome -->
<link type="text/css" href="/static/assets/vendor/@fortawesome/fontawesome-free/css/all.min.css" rel="stylesheet">

<!-- Sweet Alert -->
<link type="text/css" href="/static/assets/vendor/sweetalert2/dist/sweetalert2.min.css" rel="stylesheet">

<!-- Notyf -->
<link type="text/css" href="/static/assets/vendor/notyf/notyf.min.css" rel="stylesheet">

<!-- Volt CSS -->
<link type="text/css" href="/static/assets/css/volt.css" rel="stylesheet">

</head>
<body>

	{% block content %}{% endblock content %}

	{% include 'includes/scripts.html' %}

</body>
</html>


--#

--% /myflask2/project/apps/user/templates/includes/settings-box.html

<div class="theme-settings card pt-2 collapse" id="theme-settings">
	<div class="card-body pt-4">
		<button type="button" class="btn-close theme-settings-close" aria-label="Close" data-bs-toggle="collapse"
			href="#theme-settings" role="button" aria-expanded="false" aria-controls="theme-settings"></button>
		<div class="d-flex justify-content-between align-items-center mb-3">
			<p class="m-0 mb-1 me-4 fs-7">Open source <span role="img" aria-label="gratitude">💛</span></p>
			<a class="github-button" href="https://github.com/app-generator/flask-dashboard-volt"
				data-color-scheme="no-preference: dark; light: light; dark: light;" data-icon="octicon-star"
				data-size="large" data-show-count="true"
				aria-label="Star themesberg/volt-bootstrap-5-dashboard on GitHub">Star</a>
		</div>
		<a href="https://appseed.us/admin-dashboards/flask-dashboard-volt" target="_blank"
			class="btn btn-primary mb-3 w-100">Download <i class="fas fa-download ms-2"></i></a>
		<p class="fs-7 text-gray-700 text-center">Available in the following technologies:</p>
		<div class="d-flex justify-content-center">
			<a class="me-3" href="https://themesberg.com/product/admin-dashboard/volt-bootstrap-5-dashboard"
				target="_blank">
				<img src="/static/assets/img/technologies/bootstrap-5-logo.svg" class="image image-xs">
			</a>
			<a href="https://demo.themesberg.com/volt-react-dashboard/#/" target="_blank">
				<img src="/static/assets/img/technologies/react-logo.svg" class="image image-xs">
			</a>
			<a href="https://appseed.us/admin-dashboards/flask-dashboard-volt" target="_blank">
				<img src="/static/assets/img/technologies/flask-logo.svg" class="image image-xs">
			</a>
			<a href="https://appseed.us/admin-dashboards/django-dashboard-volt" target="_blank">
				<img src="/static/assets/img/technologies/django-logo.svg" class="image image-xs">
			</a>                        
		</div>
	</div>
</div>

<div class="card theme-settings theme-settings-expand" id="theme-settings-expand">
	<div class="card-body p-3 py-2">
		<span class="fw-bold h6">
			<i class="fas fa-cogs me-1 fs-7"></i> Settings
		</span>
	</div>
</div>


--#

--% /myflask2/project/apps/user/templates/includes/sidebar.html
<nav id="sidebarMenu" class="sidebar d-md-block bg-dark text-white collapse" data-simplebar>
	<div class="sidebar-inner px-4 pt-3">
		<div class="user-card d-flex d-md-none align-items-center justify-content-between justify-content-md-center pb-4">
		<div class="d-flex align-items-center">
			<div class="user-avatar lg-avatar me-4">
			<img src="/static/assets/img/team/profile-picture-3.jpg" class="card-img-top rounded-circle border-white"
				alt="Bonnie Green">
			</div>
			<div class="d-block">
			<h2 class="h6">
				{{ current_user.username }}
			</h2>
			<a href="{{ url_for('base_blueprint.logout') }}" class="btn btn-secondary text-dark btn-xs"><span
				class="me-2"><span class="fas fa-sign-out-alt"></span></span>Sign Out</a>
			</div>
		</div>
		<div class="collapse-close d-md-none">
			<a href="#sidebarMenu" class="fas fa-times" data-bs-toggle="collapse" data-bs-target="#sidebarMenu"
			aria-controls="sidebarMenu" aria-expanded="true" aria-label="Toggle navigation"></a>
		</div>
		</div>
		<ul class="nav flex-column pt-3 pt-md-0">
		<li class="nav-item">
			<a href="/" class="nav-link d-flex align-items-center">
			<span class="sidebar-icon">
				<img src="/static/assets/img/brand/light.svg" height="20" width="20" alt="Volt Logo">
			</span>
			<span class="mt-1 ms-1 sidebar-text">Volt Overview</span>
			</a>
		</li>
		<li class="nav-item {% if 'dashboard' in segment %} active {% endif %}">
			<a href="/dashboard.html" class="nav-link">
			<span class="sidebar-icon"><span class="fas fa-chart-pie"></span></span>
			<span class="sidebar-text">Dashboard</span>
			</a>
		</li>
		<li class="nav-item {% if 'transactions' in segment %} active {% endif %}">
			<a href="/transactions.html" class="nav-link">
			<span class="sidebar-icon"><span class="fas fa-hand-holding-usd"></span></span>
			<span class="sidebar-text">Transactions</span>
			</a>
		</li>
		<li class="nav-item {% if 'settings' in segment %} active {% endif %}">
			<a href="/settings.html" class="nav-link">
			<span class="sidebar-icon"><span class="fas fa-cog"></span></span>
			<span class="sidebar-text">Settings</span>
			</a>
		</li>
		<li class="nav-item {% if 'bootstrap-tables' in segment %} active {% endif %}">
			<span
			class="nav-link  collapsed  d-flex justify-content-between align-items-center"
			data-bs-toggle="collapse" data-bs-target="#submenu-app">
			<span>
				<span class="sidebar-icon"><span class="fas fa-table"></span></span>
				<span class="sidebar-text">Tables</span>
			</span>
			<span class="link-arrow"><span class="fas fa-chevron-right"></span></span>
			</span>
			<div class="multi-level collapse "
			role="list" id="submenu-app" aria-expanded="false">
			<ul class="flex-column nav">
				<li class="nav-item ">
				<a class="nav-link" href="/bootstrap-tables.html">
					<span class="sidebar-text">Bootstrap Tables</span>
				</a>
				</li>
			</ul>
			</div>
		</li>
		<li class="nav-item">
			<span
			class="nav-link  collapsed  d-flex justify-content-between align-items-center"
			data-bs-toggle="collapse" data-bs-target="#submenu-pages">
			<span>
				<span class="sidebar-icon"><span class="far fa-file-alt"></span></span>
				<span class="sidebar-text">Page examples</span>
			</span>
			<span class="link-arrow"><span class="fas fa-chevron-right"></span></span>
			</span>
			<div class="multi-level collapse " role="list"
			id="submenu-pages" aria-expanded="false">
			<ul class="flex-column nav">
				<li class="nav-item">
				<a class="nav-link" href="/sign-in.html">
					<span class="sidebar-text">Sign In</span>
				</a>
				</li>
				<li class="nav-item">
				<a class="nav-link" href="/sign-up.html">
					<span class="sidebar-text">Sign Up</span>
				</a>
				</li>
				<li class="nav-item">
				<a class="nav-link" href="/forgot-password.html">
					<span class="sidebar-text">Forgot password</span>
				</a>
				</li>
				<li class="nav-item">
				<a class="nav-link" href="/reset-password.html">
					<span class="sidebar-text">Reset password</span>
				</a>
				</li>
				<li class="nav-item">
				<a class="nav-link" href="/lock.html">
					<span class="sidebar-text">Lock</span>
				</a>
				</li>
				<li class="nav-item">
				<a class="nav-link" href="/page-404.html">
					<span class="sidebar-text">404 Not Found</span>
				</a>
				</li>
				<li class="nav-item">
				<a class="nav-link" href="/page-500.html">
					<span class="sidebar-text">500 Not Found</span>
				</a>
				</li>
			</ul>
			</div>
		</li>
		<li class="nav-item {% if 'ui-' in segment %} active {% endif %}">
			<span
			class="nav-link  collapsed  d-flex justify-content-between align-items-center"
			data-bs-toggle="collapse" data-bs-target="#submenu-components">
			<span>
				<span class="sidebar-icon"><span class="fas fa-box-open"></span></span>
				<span class="sidebar-text">Components</span>
			</span>
			<span class="link-arrow"><span class="fas fa-chevron-right"></span></span>
			</span>
			<div class="multi-level collapse " role="list"
			id="submenu-components" aria-expanded="false">
			<ul class="flex-column nav">
				<li class="nav-item ">
				<a class="nav-link" href="/ui-buttons.html">
					<span class="sidebar-text">Buttons</span>
				</a>
				</li>
				<li class="nav-item ">
				<a class="nav-link" href="/ui-notifications.html">
					<span class="sidebar-text">Notifications</span>
				</a>
				</li>
				<li class="nav-item ">
				<a class="nav-link" href="/ui-forms.html">
					<span class="sidebar-text">Forms</span>
				</a>
				</li>
				<li class="nav-item ">
				<a class="nav-link" href="/ui-modals.html">
					<span class="sidebar-text">Modals</span>
				</a>
				</li>
				<li class="nav-item ">
				<a class="nav-link" href="/ui-typography.html">
					<span class="sidebar-text">Typography</span>
				</a>
				</li>
			</ul>
			</div>
		</li>
		<li role="separator" class="dropdown-divider mt-4 mb-3 border-black"></li>
		<li class="nav-item">
			<a href="https://appseed.us/admin-dashboards/flask-dashboard-volt" 
			 target="_blank"
			class="nav-link d-flex align-items-center">
			<span class="sidebar-icon"><span class="fas fa-info-circle"></span></span>
			<span class="sidebar-text">Product Page</span>
			</a>
		</li>
		<li class="nav-item">
			<a href="https://appseed.us/" 
			 target="_blank"
			class="nav-link d-flex align-items-center">
			<span class="sidebar-icon"><span class="fas fa-envelope"></span></span>
			<span class="sidebar-text">Support</span>
			</a>
		</li>
		<li class="nav-item">
			<a target="_blank" 
			 href="https://appseed.us/admin-dashboards/flask-dashboard-volt-pro"
			class="btn btn-secondary d-flex align-items-center justify-content-center btn-upgrade-pro">
			<span class="sidebar-icon"><span class="fas fa-rocket me-2"></span></span> 
				<span>Upgrade to Pro</span>
			</a>
		</li>
		</ul>
	</div>
	</nav>
	

--#

--% /myflask2/project/apps/user/templates/includes/navigation.html
	<nav class="navbar navbar-top navbar-expand navbar-dashboard navbar-dark ps-0 pe-2 pb-0">
		<div class="container-fluid px-0">
			<div class="d-flex justify-content-between w-100" id="navbarSupportedContent">
			<div class="d-flex align-items-center">
				<!-- Search form -->
				<form class="navbar-search form-inline" id="navbar-search-main">
				<div class="input-group input-group-merge search-bar">
					<span class="input-group-text" id="topbar-addon"><span class="fas fa-search"></span></span>
					<input type="text" class="form-control" id="topbarInputIconLeft" placeholder="Search" aria-label="Search" aria-describedby="topbar-addon">
				</div>
				</form>
			</div>
			<!-- Navbar links -->
			<ul class="navbar-nav align-items-center">
				<li class="nav-item dropdown">
				<a class="nav-link text-dark me-lg-3 icon-notifications dropdown-toggle" data-unread-notifications="true" href="#" role="button" data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
					<span class="icon icon-sm">
					<span class="fas fa-bell bell-shake"></span>
					<span class="icon-badge rounded-circle unread-notifications"></span>
					</span>
				</a>
				<div class="dropdown-menu dashboard-dropdown dropdown-menu-lg dropdown-menu-center mt-2 py-0">
					<div class="list-group list-group-flush">
					<a href="#" class="text-center text-primary fw-bold border-bottom border-light py-3">Notifications</a>
					<a href="#" class="list-group-item list-group-item-action border-bottom border-light">
						<div class="row align-items-center">
							<div class="col-auto">
							<!-- Avatar -->
							<img alt="Image placeholder" src="/static/assets/img/team/profile-picture-1.jpg" class="user-avatar lg-avatar rounded-circle">
							</div>
							<div class="col ps-0 ms-2">
							<div class="d-flex justify-content-between align-items-center">
								<div>
									<h4 class="h6 mb-0 text-small">Jose Leos</h4>
								</div>
								<div class="text-end">
									<small class="text-danger">a few moments ago</small>
								</div>
							</div>
							<p class="font-small mt-1 mb-0">Added you to an event "Project stand-up" tomorrow at 12:30 AM.</p>
							</div>
						</div>
					</a>
					<a href="#" class="list-group-item list-group-item-action border-bottom border-light">
						<div class="row align-items-center">
							<div class="col-auto">
							<!-- Avatar -->
							<img alt="Image placeholder" src="/static/assets/img/team/profile-picture-2.jpg" class="user-avatar lg-avatar rounded-circle">
							</div>
							<div class="col ps-0 ms-2">
							<div class="d-flex justify-content-between align-items-center">
								<div>
									<h4 class="h6 mb-0 text-small">Neil Sims</h4>
								</div>
								<div class="text-end">
									<small class="text-danger">2 hrs ago</small>
								</div>
							</div>
							<p class="font-small mt-1 mb-0">You've been assigned a task for "Awesome new project".</p>
							</div>
						</div>
					</a>
					<a href="#" class="list-group-item list-group-item-action border-bottom border-light">
						<div class="row align-items-center">
							<div class="col-auto">
							<!-- Avatar -->
							<img alt="Image placeholder" src="/static/assets/img/team/profile-picture-3.jpg" class="user-avatar lg-avatar rounded-circle">
							</div>
							<div class="col ps-0 m-2">
							<div class="d-flex justify-content-between align-items-center">
								<div>
									<h4 class="h6 mb-0 text-small">Roberta Casas</h4>
								</div>
								<div class="text-end">
									<small>5 hrs ago</small>
								</div>
							</div>
							<p class="font-small mt-1 mb-0">Tagged you in a document called "First quarter financial plans",</p>
							</div>
						</div>
					</a>
					<a href="#" class="list-group-item list-group-item-action border-bottom border-light">
						<div class="row align-items-center">
							<div class="col-auto">
							<!-- Avatar -->
							<img alt="Image placeholder" src="/static/assets/img/team/profile-picture-4.jpg" class="user-avatar lg-avatar rounded-circle">
							</div>
							<div class="col ps-0 ms-2">
							<div class="d-flex justify-content-between align-items-center">
								<div>
									<h4 class="h6 mb-0 text-small">Joseph Garth</h4>
								</div>
								<div class="text-end">
									<small>1 d ago</small>
								</div>
							</div>
							<p class="font-small mt-1 mb-0">New message: "Hey, what's up? All set for the presentation?"</p>
							</div>
						</div>
					</a>
					<a href="#" class="list-group-item list-group-item-action border-bottom border-light">
						<div class="row align-items-center">
							<div class="col-auto">
							<!-- Avatar -->
							<img alt="Image placeholder" src="/static/assets/img/team/profile-picture-5.jpg" class="user-avatar lg-avatar rounded-circle">
							</div>
							<div class="col ps-0 ms-2">
							<div class="d-flex justify-content-between align-items-center">
								<div>
									<h4 class="h6 mb-0 text-small">Bonnie Green</h4>
								</div>
								<div class="text-end">
									<small>2 hrs ago</small>
								</div>
							</div>
							<p class="font-small mt-1 mb-0">New message: "We need to improve the UI/UX for the landing page."</p>
							</div>
						</div>
					</a>
					<a href="#" class="dropdown-item text-center text-primary fw-bold rounded-bottom py-3">View all</a>
					</div>
				</div>
				</li>
				<li class="nav-item dropdown">
				<a class="nav-link dropdown-toggle pt-1 px-0" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
					<div class="media d-flex align-items-center">
					<img class="user-avatar md-avatar rounded-circle" alt="Image placeholder" src="/static/assets/img/team/profile-picture-3.jpg">
					<div class="media-body ms-2 text-dark align-items-center d-none d-lg-block">
						<span class="mb-0 font-small fw-bold">
						Current User: <strong>{{ current_user.username }}</strong>
						</span>
					</div>
					</div>
				</a>
				<div class="dropdown-menu dashboard-dropdown dropdown-menu-end mt-2 py-0">
					<a class="dropdown-item rounded-top fw-bold" href="/settings.html">
						<span class="far fa-user-circle"></span>My Profile</a>
					<a class="dropdown-item fw-bold" href="/settings.html"><span class="fas fa-cog"></span>Settings</a>
					<div role="separator" class="dropdown-divider my-0"></div>
					<a class="dropdown-item rounded-bottom fw-bold" href="{{ url_for('base_blueprint.logout') }}">
						<span class="fas fa-sign-out-alt text-danger"></span>Logout</a>
				</div>
				</li>
			</ul>
			</div>
		</div>
	</nav>
	

--#

--% /myflask2/project/apps/user/templates/includes/footer.html
<footer class="footer section py-5">
		<div class="row">
			<div class="col-12 col-lg-6 mb-4 mb-lg-0">
				<p class="mb-0 text-center text-xl-left">
					&copy; <a class="text-primary fw-normal" href="https://themesberg.com" target="_blank">Themesberg</a>
				- Coded by <a href="https://appseed.us" target="_blank">AppSeed</a>. 
				</p>
			</div>

			<div class="col-12 col-lg-6">
				<!-- List -->
				<ul class="list-inline list-group-flush list-group-borderless text-center text-xl-right mb-0">
					<li class="list-inline-item px-0 px-sm-2">
						<a target="_blank" 
							 href="https://appseed.us/admin-dashboards/flask-dashboard-volt">Flask Volt Dashboard</a>
					</li>
				</ul>
			</div>
		</div>
	</footer>
	

--#

--% /myflask2/project/apps/user/templates/includes/scripts.html

<!-- Core -->
<script src="/static/assets/vendor/@popperjs/core/dist/umd/popper.min.js"></script>
<script src="/static/assets/vendor/bootstrap/dist/js/bootstrap.min.js"></script>

<!-- Vendor JS -->
<script src="/static/assets/vendor/onscreen/dist/on-screen.umd.min.js"></script>

<!-- Slider -->
<script src="/static/assets/vendor/nouislider/distribute/nouislider.min.js"></script>

<!-- Smooth scroll -->
<script src="/static/assets/vendor/smooth-scroll/dist/smooth-scroll.polyfills.min.js"></script>

<!-- Charts -->
<script src="/static/assets/vendor/chartist/dist/chartist.min.js"></script>
<script src="/static/assets/vendor/chartist-plugin-tooltips/dist/chartist-plugin-tooltip.min.js"></script>

<!-- Datepicker -->
<script src="/static/assets/vendor/vanillajs-datepicker/dist/js/datepicker.min.js"></script>

<!-- Sweet Alerts 2 -->
<script src="/static/assets/vendor/sweetalert2/dist/sweetalert2.all.min.js"></script>

<!-- Moment JS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/moment.js/2.27.0/moment.min.js"></script>

<!-- Vanilla JS Datepicker -->
<script src="/static/assets/vendor/vanillajs-datepicker/dist/js/datepicker.min.js"></script>

<!-- Notyf -->
<script src="/static/assets/vendor/notyf/notyf.min.js"></script>

<!-- Simplebar -->
<script src="/static/assets/vendor/simplebar/dist/simplebar.min.js"></script>

<!-- Github buttons -->
<script async defer src="https://buttons.github.io/buttons.js"></script>

<!-- Volt JS -->
<script src="/static/assets/js/volt.js"></script>


--#

--% /myflask2/project/apps/user/templates/accounts/register.html
{% extends "layouts/base-fullscreen.html" %}

{% block title %} Sign Up {% endblock %} 

<!-- Specific Page CSS goes HERE  -->
{% block stylesheets %}{% endblock stylesheets %}

{% block content %}

	<main>
		<section class="d-flex align-items-center my-5 mt-lg-6 mb-lg-5">
			<div class="container">
				<div class="row justify-content-center form-bg-image" data-background-lg="/static/assets/img/illustrations/signin.svg">
					<div class="col-12 d-flex align-items-center justify-content-center">
						<div class="mb-4 mb-lg-0 bg-white shadow-soft border rounded border-light p-4 p-lg-5 w-100 fmxw-500">
							<div class="text-center text-md-center mb-4 mt-md-0">
								<h1 class="mb-0 h3">
									<a target="_blank"
										 href="https://appseed.us/admin-dashboards/flask-dashboard-volt">Flask Volt</a> - Sign UP
								</h1>
								<br />
								<p>
									{% if msg %}
										{{ msg | safe }}
									{% else %}
										Add your credentials
									{% endif %}                                     
								</p> 
							</div>

							<form method="post" action="">
							
								{{ form.hidden_tag() }}

								<!-- Form -->
								<div class="form-group mb-4">
									<label for="email">Username</label>
									<div class="input-group">
										<span class="input-group-text" id="basic-addon3"><span class="fas fa-user-shield"></span></span>
										{{ form.username(placeholder="Username", class="form-control") }}
									</div>  
								</div>

								<!-- Form -->
								<div class="form-group mb-4">
									<label for="email">Your Email</label>
									<div class="input-group">
										<span class="input-group-text" id="basic-addon3"><span class="fas fa-envelope"></span></span>
										{{ form.email(placeholder="Email", class="input form-control", type="email") }}
									</div>  
								</div>
								<!-- End of Form -->

								<!-- End of Form -->
								<div class="form-group">

									<!-- Form -->
									<div class="form-group mb-4">
										<label for="password">Your Password</label>
										<div class="input-group">
											<span class="input-group-text" id="basic-addon4"><span class="fas fa-unlock-alt"></span></span>
											{{ form.password(placeholder="Password", class="form-control", type="password") }}
										</div>  
									</div>
									<!-- End of Form -->

									<div class="d-flex justify-content-between align-items-top mb-4">
										<div class="form-check">
											<input class="form-check-input" type="checkbox" value="" id="remember">
											<label class="form-check-label mb-0" for="remember">
												Agree Terms
											</label>
										</div>
										<div class="form-check">
											<a href="{{ url_for('user_blueprint.login') }}" class="small text-right">Login</a>
										</div>
									</div>                                  
								</div>
								<div class="d-grid">
									<button type="submit" name="register" class="btn btn-dark">Sign UP</button>
								</div>
							</form>

							<div class="d-flex justify-content-center align-items-center mt-4">
								<span class="font-weight-normal">
									&copy; <a  href="http://fulgent.de" target="_blank">Fulgent</a> 
									- developed by <a target="_blank" href="http://fulgent.de">Usef</a>
								</span>
							</div>

						</div>
					</div>
				</div>
			</div>
		</section>
	</main>

{% endblock content %}

<!-- Specific Page JS goes HERE  -->
{% block javascripts %}{% endblock javascripts %}


--#

--% /myflask2/project/apps/user/templates/accounts/login.html
{% extends "layouts/base-fullscreen.html" %}

{% block title %} Sign In {% endblock %} 

<!-- Specific Page CSS goes HERE  -->
{% block stylesheets %}{% endblock stylesheets %}

{% block content %}

	<main>
		<!-- Section -->
		<section class="d-flex align-items-center my-5 mt-lg-6 mb-lg-5">
			<div class="container">
				<div class="row justify-content-center form-bg-image" data-background-lg="/static/assets/img/illustrations/signin.svg">
					<div class="col-12 d-flex align-items-center justify-content-center">
						<div class="bg-white shadow-soft border rounded border-light p-4 p-lg-5 w-100 fmxw-500">
							<div class="text-center text-md-center mb-4 mt-md-0">
								<h1 class="mb-0 h3">
									<a target="_blank"
										 href="https://appseed.us/admin-dashboards/flask-dashboard-volt">Flask Volt</a> - Sign UP
								</h1>
								<br />
								<p>
									{% if msg %}
										{{ msg | safe }}
									{% else %}
										Add your credentials
									{% endif %}                                     
								</p>                                 
							</div>

							<form method="post" action="" class="mt-4">
								
								{{ form.hidden_tag() }}

								<!-- Form -->
								<div class="form-group mb-4">
									<label for="email">Username</label>
									<div class="input-group">
										<span class="input-group-text" id="basic-addon1"><span class="fas fa-user-circle"></span></span>
										{{ form.username(placeholder="Username", class="form-control") }}
									</div>  
								</div>
								<!-- End of Form -->
								<div class="form-group">
									<!-- Form -->
									<div class="form-group mb-4">
										<label for="password">Your Password</label>
										<div class="input-group">
											<span class="input-group-text" id="basic-addon2"><span class="fas fa-unlock-alt"></span></span>
											{{ form.password(placeholder="Password", class="form-control", type="password") }}
										</div>  
									</div>
									<!-- End of Form -->
									<div class="d-flex justify-content-between align-items-top mb-4">
										<div class="form-check">
											<input class="form-check-input" type="checkbox" value="" id="remember">
											<label class="form-check-label mb-0" for="remember">
												Remember me
											</label>
										</div>
										<div class="form-check">
											<a href="{{ url_for('user_blueprint.register') }}" class="small text-right">Register</a>
										</div>
									</div>
								</div>
								<div class="d-grid">
									<button type="submit" name="login" class="btn btn-dark">Sign in</button>
								</div>
							</form>

							<div class="d-flex justify-content-center align-items-center mt-4">
								<span class="font-weight-normal">
									&copy; <a  href="http://fulgent.de" target="_blank">Fulgent</a> 
									- developed by <a target="_blank" href="http://fulgent.de">Usef</a>
								</span>
							</div>

						</div>
					</div>
				</div>
			</div>
		</section>
	</main>

{% endblock content %}

<!-- Specific Page JS goes HERE  -->
{% block javascripts %}{% endblock javascripts %}


--#

--% /myflask2/project/apps/home/__init__.py
from flask import Blueprint
from flask_restful import Api

# from .resource import UserDetail, UserList

blueprint = Blueprint(
	'home_blueprint', 
	__name__, 
	url_prefix='',
	# url_prefix='',
	template_folder='templates',
	static_folder='static'
)

# api = Api(blueprint)
# api.add_resource(UserDetail, '/users/<int:user_id>')
# api.add_resource(UserList, '/users')

from flask import render_template, redirect, url_for, request
# from flask_login import login_required, current_user
from jinja2 import TemplateNotFound

@blueprint.route('/index')
# @login_required
def index():
	return render_template('index.html', segment='index')

@blueprint.route('/<template>')
# @login_required
def route_template(template):
	try:
		if not template.endswith( '.html' ):
			template += '.html'
		# Detect the current page
		segment = get_segment( request )
		# Serve the file (if exists) from app/templates/FILE.html
		return render_template( template, segment=segment )

	except TemplateNotFound:
		return render_template('page-404.html'), 404
	
	except:
		return render_template('page-500.html'), 500

# Helper - Extract current page name from request 
def get_segment( request ):
	try:
		segment = request.path.split('/')[-1]
		if segment == '':
			segment = 'index'

		return segment
	except:
		return None

--#

--% /myflask2/project/apps/home/static/assets/js/volt.js
/*

=========================================================
* Volt Pro - Premium Bootstrap 5 Dashboard
=========================================================

* Product Page: https://themesberg.com/product/admin-dashboard/volt-premium-bootstrap-5-dashboard
* Copyright 2020 Themesberg (https://www.themesberg.com)

* Designed and coded by https://themesberg.com

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. Please contact us to request a removal. Contact us if you want to remove it.

*/

"use strict";
const d = document;
d.addEventListener("DOMContentLoaded", function(event) {

		const swalWithBootstrapButtons = Swal.mixin({
				customClass: {
						confirmButton: 'btn btn-primary me-3',
						cancelButton: 'btn btn-gray'
				},
				buttonsStyling: false
		});

		var themeSettingsEl = document.getElementById('theme-settings');
		var themeSettingsExpandEl = document.getElementById('theme-settings-expand');

		if(themeSettingsEl) {

				var themeSettingsCollapse = new bootstrap.Collapse(themeSettingsEl, {
						show: true,
						toggle: false
				});

				if (window.localStorage.getItem('settings_expanded') === 'true') {
						themeSettingsCollapse.show();
						themeSettingsExpandEl.classList.remove('show');
				} else {
						themeSettingsCollapse.hide();
						themeSettingsExpandEl.classList.add('show');
				}
				
				themeSettingsEl.addEventListener('hidden.bs.collapse', function () {
						themeSettingsExpandEl.classList.add('show');
						window.localStorage.setItem('settings_expanded', false);
				});

				themeSettingsExpandEl.addEventListener('click', function () {
						themeSettingsExpandEl.classList.remove('show');
						window.localStorage.setItem('settings_expanded', true);
						setTimeout(function() {
								themeSettingsCollapse.show();
						}, 300);
				});
		}

		// options
		const breakpoints = {
				sm: 540,
				md: 720,
				lg: 960,
				xl: 1140
		};

		var sidebar = document.getElementById('sidebarMenu')
		if(sidebar && d.body.clientWidth < breakpoints.lg) {
				sidebar.addEventListener('shown.bs.collapse', function () {
						document.querySelector('body').style.position = 'fixed';
				});
				sidebar.addEventListener('hidden.bs.collapse', function () {
						document.querySelector('body').style.position = 'relative';
				});
		}

		var iconNotifications = d.querySelector('.icon-notifications');
		if(iconNotifications) {
				var unreadNotifications = d.querySelector('.unread-notifications');
				var bellShake = d.querySelector('.bell-shake');
		
				if (iconNotifications.getAttribute('data-unread-notifications') === 'true') {
						unreadNotifications.style.display = 'block';
				} else {
						unreadNotifications.style.display = 'none';
				}
		
				// bell shake
				var shakingInterval = setInterval(function() {
						if (iconNotifications.getAttribute('data-unread-notifications') === 'true') {
								if (bellShake.classList.contains('shaking')) {
										bellShake.classList.remove('shaking');
								} else {
										bellShake.classList.add('shaking');
								}
						}
				}, 5000);
		
				iconNotifications.addEventListener('show.bs.dropdown', function () {
						bellShake.setAttribute('data-unread-notifications', false);
						clearInterval(shakingInterval);
						bellShake.classList.remove('shaking');
						unreadNotifications.style.display = 'none';
				});
		}

		[].slice.call(d.querySelectorAll('[data-background]')).map(function(el) {
				el.style.background = 'url(' + el.getAttribute('data-background') + ')';
		});

		[].slice.call(d.querySelectorAll('[data-background-lg]')).map(function(el) {
				if(document.body.clientWidth > breakpoints.lg) {
						el.style.background = 'url(' + el.getAttribute('data-background-lg') + ')';
				}
		});

		[].slice.call(d.querySelectorAll('[data-background-color]')).map(function(el) {
				el.style.background = 'url(' + el.getAttribute('data-background-color') + ')';
		});

		[].slice.call(d.querySelectorAll('[data-color]')).map(function(el) {
				el.style.color = 'url(' + el.getAttribute('data-color') + ')';
		});

		//Tooltips
		var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
		var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
		return new bootstrap.Tooltip(tooltipTriggerEl)
		})


		// Popovers
		var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
		var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
			return new bootstrap.Popover(popoverTriggerEl)
		})
		

		// Datepicker
		var datepickers = [].slice.call(d.querySelectorAll('[data-datepicker]'))
		var datepickersList = datepickers.map(function (el) {
				return new Datepicker(el, {
						buttonClass: 'btn'
					});
		})

		if(d.querySelector('.input-slider-container')) {
				[].slice.call(d.querySelectorAll('.input-slider-container')).map(function(el) {
						var slider = el.querySelector(':scope .input-slider');
						var sliderId = slider.getAttribute('id');
						var minValue = slider.getAttribute('data-range-value-min');
						var maxValue = slider.getAttribute('data-range-value-max');

						var sliderValue = el.querySelector(':scope .range-slider-value');
						var sliderValueId = sliderValue.getAttribute('id');
						var startValue = sliderValue.getAttribute('data-range-value-low');

						var c = d.getElementById(sliderId),
								id = d.getElementById(sliderValueId);

						noUiSlider.create(c, {
								start: [parseInt(startValue)],
								connect: [true, false],
								//step: 1000,
								range: {
										'min': [parseInt(minValue)],
										'max': [parseInt(maxValue)]
								}
						});
				});
		}

		if (d.getElementById('input-slider-range')) {
				var c = d.getElementById("input-slider-range"),
						low = d.getElementById("input-slider-range-value-low"),
						e = d.getElementById("input-slider-range-value-high"),
						f = [d, e];

				noUiSlider.create(c, {
						start: [parseInt(low.getAttribute('data-range-value-low')), parseInt(e.getAttribute('data-range-value-high'))],
						connect: !0,
						tooltips: true,
						range: {
								min: parseInt(c.getAttribute('data-range-value-min')),
								max: parseInt(c.getAttribute('data-range-value-max'))
						}
				}), c.noUiSlider.on("update", function (a, b) {
						f[b].textContent = a[b]
				});
		}

		//Chartist

		if(d.querySelector('.ct-chart-sales-value')) {
				//Chart 5
					new Chartist.Line('.ct-chart-sales-value', {
						labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
						series: [
								[0, 10, 30, 40, 80, 60, 100]
						]
					}, {
						low: 0,
						showArea: true,
						fullWidth: true,
						plugins: [
							Chartist.plugins.tooltip()
						],
						axisX: {
								// On the x-axis start means top and end means bottom
								position: 'end',
								showGrid: true
						},
						axisY: {
								// On the y-axis start means left and end means right
								showGrid: false,
								showLabel: false,
								labelInterpolationFnc: function(value) {
										return '$' + (value / 1) + 'k';
								}
						}
				});
		}

		if(d.querySelector('.ct-chart-ranking')) {
				var chart = new Chartist.Bar('.ct-chart-ranking', {
						labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
						series: [
							[1, 5, 2, 5, 4, 3],
							[2, 3, 4, 8, 1, 2],
						]
					}, {
						low: 0,
						showArea: true,
						plugins: [
							Chartist.plugins.tooltip()
						],
						axisX: {
								// On the x-axis start means top and end means bottom
								position: 'end'
						},
						axisY: {
								// On the y-axis start means left and end means right
								showGrid: false,
								showLabel: false,
								offset: 0
						}
						});
					
					chart.on('draw', function(data) {
						if(data.type === 'line' || data.type === 'area') {
							data.element.animate({
								d: {
									begin: 2000 * data.index,
									dur: 2000,
									from: data.path.clone().scale(1, 0).translate(0, data.chartRect.height()).stringify(),
									to: data.path.clone().stringify(),
									easing: Chartist.Svg.Easing.easeOutQuint
								}
							});
						}
				});
		}

		if(d.querySelector('.ct-chart-traffic-share')) {
				var data = {
						series: [70, 20, 10]
					};
					
					var sum = function(a, b) { return a + b };
					
					new Chartist.Pie('.ct-chart-traffic-share', data, {
						labelInterpolationFnc: function(value) {
							return Math.round(value / data.series.reduce(sum) * 100) + '%';
						},            
						low: 0,
						high: 8,
						donut: true,
						donutWidth: 20,
						donutSolid: true,
						fullWidth: false,
						showLabel: false,
						plugins: [
							Chartist.plugins.tooltip()
						],
				});         
		}

		if (d.getElementById('loadOnClick')) {
				d.getElementById('loadOnClick').addEventListener('click', function () {
						var button = this;
						var loadContent = d.getElementById('extraContent');
						var allLoaded = d.getElementById('allLoadedText');
		
						button.classList.add('btn-loading');
						button.setAttribute('disabled', 'true');
		
						setTimeout(function () {
								loadContent.style.display = 'block';
								button.style.display = 'none';
								allLoaded.style.display = 'block';
						}, 1500);
				});
		}

		var scroll = new SmoothScroll('a[href*="#"]', {
				speed: 500,
				speedAsDuration: true
		});

		if(d.querySelector('.current-year')){
				d.querySelector('.current-year').textContent = new Date().getFullYear();
		}

		// Glide JS

		if (d.querySelector('.glide')) {
				new Glide('.glide', {
						type: 'carousel',
						startAt: 0,
						perView: 3
					}).mount();
		}

		if (d.querySelector('.glide-testimonials')) {
				new Glide('.glide-testimonials', {
						type: 'carousel',
						startAt: 0,
						perView: 1,
						autoplay: 2000
					}).mount();
		}

		if (d.querySelector('.glide-clients')) {
				new Glide('.glide-clients', {
						type: 'carousel',
						startAt: 0,
						perView: 5,
						autoplay: 2000
					}).mount();
		}

		if (d.querySelector('.glide-news-widget')) {
				new Glide('.glide-news-widget', {
						type: 'carousel',
						startAt: 0,
						perView: 1,
						autoplay: 2000
					}).mount();
		}

		if (d.querySelector('.glide-autoplay')) {
				new Glide('.glide-autoplay', {
						type: 'carousel',
						startAt: 0,
						perView: 3,
						autoplay: 2000
					}).mount();
		}

		// Pricing countup
		var billingSwitchEl = d.getElementById('billingSwitch');
		if(billingSwitchEl) {
				const countUpStandard = new countUp.CountUp('priceStandard', 99, { startVal: 199 });
				const countUpPremium = new countUp.CountUp('pricePremium', 199, { startVal: 299 });
				
				billingSwitchEl.addEventListener('change', function() {
						if(billingSwitch.checked) {
								countUpStandard.start();
								countUpPremium.start();
						} else {
								countUpStandard.reset();
								countUpPremium.reset();
						}
				});
		}

});
--#

--% /myflask2/project/apps/home/templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Home Blueprint</title>
</head>
<body>
	Home Blueprint - Index
</body>
</html>

--#

--% /myflask2/project/apps/home/templates/page-500.html
{% extends "layouts/base-fullscreen.html" %}

{% block title %} Error 500 {% endblock %} 

<!-- Specific Page CSS goes HERE  -->
{% block stylesheets %}{% endblock stylesheets %}

{% block content %}

	<main>
		<section class="vh-100 d-flex align-items-center justify-content-center">
			<div class="container">
				<div class="row align-items-center ">
					<div class="col-12 col-lg-5 order-2 order-lg-1 text-center text-lg-left">
						<h1 class="mt-5">Something has gone <span class="text-primary">seriously</span> wrong</h1>
						<p class="lead my-4">It's always time for a coffee break. We should be back by the time you finish your coffee.</p>
						<a class="btn btn-dark animate-hover" href="/dashboard.html">
							<i class="fas fa-chevron-left me-3 ps-2 animate-left-3"></i>Go back home</a>
					</div>
					<div class="col-12 col-lg-7 order-1 order-lg-2 text-center d-flex align-items-center justify-content-center">
						<img class="img-fluid w-75" src="/static/assets/img/illustrations/500.svg" alt="500 Server Error">
					</div>
				</div>
			</div>
		</section>
	</main>

{% endblock content %}

<!-- Specific Page JS goes HERE  -->
{% block javascripts %}{% endblock javascripts %}


--#

--% /myflask2/project/apps/home/templates/page-404.html
{% extends "layouts/base-fullscreen.html" %}

{% block title %} Error 404 {% endblock %} 

<!-- Specific Page CSS goes HERE  -->
{% block stylesheets %}{% endblock stylesheets %}

{% block content %}

	<main>
		<section class="vh-100 d-flex align-items-center justify-content-center">
			<div class="container">
				<div class="row">
					<div class="col-12 text-center d-flex align-items-center justify-content-center">
						<div>
							<img class="img-fluid w-75" src="/static/assets/img/illustrations/404.svg" alt="404 not found">
							<h1 class="mt-5">Page not <span class="fw-bolder text-primary">found</span></h1>
							<p class="lead my-4">Oops! Looks like you followed a bad link. If you think this is a
								problem with us, please tell us.</p>
							<a class="btn btn-dark animate-hover" href="/dashboard.html">
								<i class="fas fa-chevron-left me-3 ps-2 animate-left-3"></i>Go back home</a>
						</div>
					</div>
				</div>
			</div>
		</section>
	</main>

{% endblock content %}

<!-- Specific Page JS goes HERE  -->
{% block javascripts %}{% endblock javascripts %}


--#

--% /myflask2/project/apps/home/templates/page-403.html
{% extends "layouts/base-fullscreen.html" %}

{% block title %} Error 403 {% endblock %} 

<!-- Specific Page CSS goes HERE  -->
{% block stylesheets %}{% endblock stylesheets %}

{% block content %}

	<main>
		<section class="vh-100 d-flex align-items-center justify-content-center">
			<div class="container">
				<div class="row">
					<div class="col-12 text-center d-flex align-items-center justify-content-center">
						<div>
							<img class="img-fluid w-75" src="/static/assets/img/illustrations/404.svg" alt="404 not found">
							<h1 class="mt-5">
								Access <span class="fw-bolder text-primary">denied</span>
							</h1>
							<p class="lead my-4">
								Please contact support or authenticate
							</p>
							<a class="btn btn-dark animate-hover" href="/sign-in.html">
								 <i class="fas fa-chevron-left me-3 ps-2 animate-left-3"></i>LOGIN</a>
						</div>
					</div>
				</div>
			</div>
		</section>
	</main>

{% endblock content %}

<!-- Specific Page JS goes HERE  -->
{% block javascripts %}{% endblock javascripts %}


--#

--% /myflask2/project/main/wsgi.py
import os
from project.main import create_app

app = create_app()

--#

--% /myflask2/project/main/__init__.py
from project.main.index import Application as FlaskApp

def create_app(do_migrate=False):
	app = FlaskApp(do_migrate=do_migrate)
	return app

--#

--% /myflask2/project/main/index.py
import json, os, sys
from flask import Flask
from flask_cors import CORS
from project.main.resource import ResourceHandler
from .router import (
	register_resources,
	main_route,
	final_route,
)

class Application(Flask):

	def __init__(self, import_name=__package__, do_migrate=False, *args, **kwargs):
		super(Application, self).__init__(import_name, *args, **kwargs)
		self.config.from_object("config") # /config.py
		self.logger.info("Initializing Application...")
		CORS(self)

		if do_migrate:			
			self.do_migrate = do_migrate

		self.init_mainroutes() # server:port/
		# self.resource_handler = ResourceHandler(self)
		# self.init_modules(self.config["APPS_DIR"])
		self.init_extensions()
		self.init_blueprints()
		# self.init_db()
		# self.init_permissions()
		# self.init_admin()
		# self.init_utils()
		self.logger.debug("App initialized...")
		final_route(self)

	def run(self, *args, **kwargs):
		self.logger.info("App is running...")
		super(Application, self).run(*args, **kwargs)

	def init_mainroutes(self):
		main_route(self)

	def init_extensions(self):
		from .extensions import db, jwt, login_manager, migrate
		db.init_app(self)
		jwt.init_app(self)
		login_manager.init_app(self)
		if hasattr(self, 'do_migrate') and self.do_migrate:
			print('*'*40, 'START: migrating')
			migrate.init_app(self, db)
			print('*'*40, 'END: migrating')

	def init_blueprints(self):
__TEMPLATE2_BLUEPRINTS_IMPORTS
		# from project.apps import user
		# from project.apps import home
__TEMPLATE2_BLUEPRINTS_REGISTER
		# self.register_blueprint(user.blueprint)
		# self.register_blueprint(home.blueprint)

	def init_db(self):
		# semua model harus terimport sebelum init_db
		from project.main.db.sqlite.index import init_db
		init_db(self)

	def init_permissions(self):
		pass

	def init_admin(self):
		pass

	def init_utils(self):
		pass

--#

--% /myflask2/project/main/extensions.py
from flask_sqlalchemy import SQLAlchemy
from passlib.context import CryptContext
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate


db              = SQLAlchemy()
jwt             = JWTManager()
login_manager   = LoginManager()
ma              = Marshmallow()
migrate         = Migrate()
pwd_context     = CryptContext(schemes=['pbkdf2_sha256'], deprecated='auto')

--#

--% /myflask2/project/main/router.py
def register_resources(app, api, resources, prefix=None):
	app.logger.info(f"register_resources api={api}, resources={resources}, prefix={prefix}.")
	for resource in resources:
		if resource is not None:
			rule = resource['rule']
			disable_prefix = False
			if 'disable_prefix' in resource:
				disable_prefix = resource['disable_prefix']
			if prefix is not None and not disable_prefix:
				rule = "{}{}".format(prefix, rule,)
			print(f"\t Blueprint: Adding {resource['resource_class']} with rule {rule}")
			api.add_resource(resource['resource_class'], rule)


def main_route(app):
	@app.route('/')
	def index():
		return "Alive"


def final_route(app):
	"""
	um.ir
	"""
	for rule in app.url_map.iter_rules():
		print(rule)

	import os
	print('ABS_PATH =', app.config['ABS_PATH'])
	print('cwd = ', os.getcwd())

--#

--% /myflask2/project/main/loader.py
import imp
import importlib
import os, sys
# import project
# import project.apps
# import project.apps.user

def find_dotted_module(name, path=None):
	'''
	Example: find_dotted_module('mypackage.myfile')
	Background: imp.find_module() does not handle hierarchical module names (names containing dots).
	Important: No code of the module gets executed. The module does not get loaded (on purpose)
	ImportError gets raised if the module can't be found.
	Use case:
	Test discovery without loading 
	(otherwise coverage does not see the lines which are executed at import time)
	'''
	file = None
	descr = None
	for x in name.split('.'):
		if path is not None:
			path=[path]
		file, path, descr = imp.find_module(x, path)
	return file, path, descr

def import_modules(app, folderpath, name=None):
	folder_as_module = app.config['APPS_PREFIX'] + folderpath
	print("folder", folderpath, "as module", folder_as_module)

	try:
		# https://stackoverflow.com/questions/37970448/cant-find-module-that-exists
		# https://stackoverflow.com/questions/5795562/version-of-imp-find-module-that-works-on-dotted-modules
		# fp, pathname, description = imp.find_module(folder_as_module)
		# fp, pathname, description = imp.find_module(folderpath)
		fp, pathname, description = find_dotted_module(folder_as_module)
		name = os.path.split(folderpath)[-1].replace(".", "_")
		imported = imp.load_module(name, fp, pathname, description)
		# imported_modules.append(imported)
		return imported

	except ImportError as err:
		print('         => ImportError:', err)
		print('-'*40, 'globals():')
		print('='*40)
		print(dir(sys.modules[__name__]))
		print('*'*40)
		print('ABS_PATH =', app.config['ABS_PATH'])
		sys.path.append(app.config['ABS_PATH'])
		return None

--#

--% /myflask2/project/main/resource.py
from flask_restful import Api
from werkzeug.datastructures import Headers

class ResourceHandler(Api):

	def handle_error(self, e):
		error_name = type(e).__name__
		error_list = list(
			error for error in exceptions.__dict__.keys() if not error.startswith("__")
		)
		response = {
			"code": 500,
			"status": "SERVER_ERROR",
			"message": "Internal Server Error",
			"extras": None,
		}
		if error_name in error_list:
			response = e.to_dict()
		elif error_name in werkzeug_errors.keys():
			response['code'] = werkzeug_errors[error_name]['code']
			response['status'] = error_name
			response['message'] = werkzeug_errors[error_name]['message']
			if 'data' in e.__dict__.keys():
				if 'message' in e.data:
					response['extras'] = e.data['message']
		elif error_name in errors.keys():
			response['code'] = self.errors[error_name]['code']
			response['status'] = self.errors[error_name]['status']
			response['message'] = self.errors[error_name]['message']
			if 'extras' in self.errors[error_name]:
				response['extras'] = self.errors[error_name]['extras']
		else:
			return super(Api, self).handle_error(e)
				
		return self.make_response(
			response,
			response['code'],
			Headers()
		)

--#

--% /myflask2/project/main/db/sqlite/index.py
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
make_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db_session = scoped_session(make_session)
Base = declarative_base()
Base.query = db_session.query_property()

def init_db(app):
	# import all modules here that might define models so that
	# they will be registered properly on the metadata.  Otherwise
	# you will have to import them first before calling init_db()
	# import .models
	Base.metadata.create_all(bind=engine)

--#
