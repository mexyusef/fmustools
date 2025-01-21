from flask_wtf import FlaskForm
from wtforms import PasswordField, TextField
from wtforms.validators import DataRequired, Email, InputRequired

class __TEMPLATE_TABLENAME_CASE__Form(FlaskForm):
__TEMPLATE_COLUMN_LIST
	# username = TextField('Username', id='username_login', validators=[DataRequired()])
	# password = PasswordField('Password', id='pwd_login', validators=[DataRequired()])
	# email    = TextField('Email', id='email_create', validators=[DataRequired(), Email()])
