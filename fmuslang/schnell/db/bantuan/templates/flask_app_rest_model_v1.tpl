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
