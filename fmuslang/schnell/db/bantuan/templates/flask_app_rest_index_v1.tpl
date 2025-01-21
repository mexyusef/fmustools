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
