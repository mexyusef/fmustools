--% index/fmus
.,d
	__init__.py,f(e=__FILE__=__init__.py)
	admin.py,f(e=__FILE__=admin.py)
	models.py,f(e=__FILE__=models.py)
	renderers.py,f(e=__FILE__=renderers.py)
	serializers.py,f(e=__FILE__=serializers.py)
	signals.py,f(e=__FILE__=signals.py)
	urls.py,f(e=__FILE__=urls.py)
	views.py,f(e=__FILE__=views.py)
--#

--% __init__.py
from django.apps import AppConfig

class UserAppConfig(AppConfig):
  name = 'apps.user'
  label = 'user'
  verbose_name = 'User'

  def ready(self):
    import apps.user.signals

default_app_config = 'apps.user.UserAppConfig'
--#

--% admin.py
from django.contrib import admin
from .models import User

admin.site.register(User)
--#

--% models.py
import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser, 
	BaseUserManager, 
	PermissionsMixin,
)
from main.helpers import TimestampedModel


class UserManager(BaseUserManager):
	def create_user(self, username, email, password=None):
		if username is None:
			raise TypeError('Users must have a username.')

		if email is None:
			raise TypeError('Users must have an email address.')

		user = self.model(username=username, email=self.normalize_email(email))
		user.set_password(password)
		user.save()

		return user

	def create_superuser(self, username, email, password):
		if password is None:
			raise TypeError('Superusers must have a password.')

		user = self.create_user(username, email, password)
		user.is_superuser = True
		user.is_staff = True
		user.save()
		return user

class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):
	username = models.CharField(db_index=True, max_length=255, unique=True)
	name = models.CharField(max_length=255, null=True)
	first_name = models.CharField(max_length=255, null=True)
	last_name = models.CharField(max_length=255, null=True)
	email = models.EmailField(db_index=True, unique=True)
	phone = models.CharField(db_index=True, max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	isAdmin         = models.BooleanField(null=False, default=False)
	password        = models.CharField(null=False, max_length=255)
	ROLES = (    
		('admin', 'Admin'),
		('user', 'User'),
		('guest', 'Guest'),
	)
	roles = models.CharField(max_length=50, choices=ROLES, default='user')

	USERNAME_FIELD = 'username'
	# ERRORS:
	# user.User: (auth.E002) The field named as the 'USERNAME_FIELD' for a custom user model must not be included in 'REQUIRED_FIELDS'.
	# HINT: The 'USERNAME_FIELD' is currently set to 'username', you should remove 'username' from the 'REQUIRED_FIELDS'.
	REQUIRED_FIELDS = []
	# # USERNAME_FIELD = 'email'
	# REQUIRED_FIELDS = ['username']

	objects = UserManager()

	class Meta:
		# db_table = 'users'
		db_table = 'auth_user'
		ordering = ['-username']

	def __str__(self):
		return f"{self.username}, {self.email}"

	@property
	def token(self):
		return self._generate_jwt_token()

	def get_full_name(self):
		return self.username

	def get_short_name(self):
		return self.username

	def _generate_jwt_token(self):
		dt = datetime.now() + timedelta(days=60)
		token = jwt.encode({
			'id': self.pk,
			'exp': int(dt.strftime('%s'))
		}, settings.SECRET_KEY, algorithm='HS256')
		if isinstance(token, bytes):
			return token.decode('utf-8')
		return token
--#

--% renderers.py
from main.helpers import CustomJSONRenderer

class UserJSONRenderer(CustomJSONRenderer):

  charset = 'utf-8'
  object_label = 'user'
  pagination_object_label = 'users'
  pagination_count_label = 'usersCount'

  def render(self, data, media_type=None, renderer_context=None):
    print('user json render utk data:', data)
    token = data.get('token', None)
    if token is not None and isinstance(token, bytes):
      data['token'] = token.decode('utf-8')

    return super(UserJSONRenderer, self).render(data)
--#

--% serializers.py
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User

class UserSerializer(serializers.ModelSerializer):
  """Handles serialization and deserialization of User objects."""
  password = serializers.CharField(
    max_length=128,
    min_length=8,
    write_only=True
  )
  # profile = ProfileSerializer(write_only=True)
  bio = serializers.CharField(source='profile.bio', read_only=True)
  image = serializers.CharField(source='profile.image', read_only=True)

  # tambahan START
  isAdmin = serializers.SerializerMethodField(read_only=True)
  def get_isAdmin(self, obj):
    return obj.is_staff

  name = serializers.SerializerMethodField(read_only=True)
  def get_name(self, obj):
    name = obj.first_name
    if hasattr(obj, 'last_name') and obj.last_name:
      name += (' ' if name else '') + obj.last_name
    if name == '':
      name = obj.email
    return name

  _id = serializers.SerializerMethodField(read_only=True)
  def get__id(self, obj):
    return obj.id
  # tambahan END


  class Meta:
    model = User
    fields = (
      'email', 'username', 'password', 'token', 'profile', 'bio', 'image',
      '_id', 'name', 'isAdmin',
    )
    read_only_fields = ('token',)

  def update(self, instance, validated_data):
    password = validated_data.pop('password', None)
    profile_data = validated_data.pop('profile', {})
    for (key, value) in validated_data.items():
      setattr(instance, key, value)

    if password is not None:
      instance.set_password(password)

    instance.save()

    for (key, value) in profile_data.items():
      setattr(instance.profile, key, value)

    instance.profile.save()
    return instance


class UserSerializerWithToken(UserSerializer):
  token = serializers.SerializerMethodField(read_only=True)

  class Meta:
    model = User
    # fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']
    # AssertionError: ("Creating a ModelSerializer without either the 'fields' attribute or the 'exclude' attribute has been deprecated since 3.3.0, and is now disallowed. Add an explicit fields = '__all__' to the UserSerializerWithToken serializer.",)
    # fields = '__all__'

    fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token', 'bio', 'image', 'phone', 'roles', 'first_name', 'last_name']

  def get_token(self, obj):
    token = RefreshToken.for_user(obj)
    print(f"""
			UserSerializerWithToken / get_token
			type = {type(token)}
			token = {token}    
			refresh_token = str(token) = {str(token)}
			access_token = str(token.access_token) = {str(token.access_token)}
    """)
    return str(token.access_token)
--#

--% signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver

# from apps.profile.models import Profile
from .models import User


# @receiver(post_save, sender=User)
# def create_related_profile(sender, instance, created, *args, **kwargs):
#   if instance and created:
#     instance.profile = Profile.objects.create(user=instance)
--#

--% urls.py
from django.urls import path
from . import views

urlpatterns = [
	path('users/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
	path('users/register/', views.registerUser, name='register'),

	path('users/profile/', views.getUserProfile, name="users-profile"),
	path('users/profile/update/', views.updateUserProfile, name="user-profile-update"),

	path('users/', views.getUsers, name="user-list"),
	path('users/<str:pk>/', views.getUserById, name='user-detail'),
	path('users/update/<str:pk>/', views.updateUser, name='user-update'),
	path('users/delete/<str:pk>/', views.deleteUser, name='user-delete'),
]
--#

--% views.py
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.contrib.auth.models import User
from .serializers import UserSerializer, UserSerializerWithToken

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.hashers import make_password
from rest_framework import status


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    data = super().validate(attrs)

    serializer = UserSerializerWithToken(self.user).data

    print(f"""
      MyTokenObtainPairSerializer
      ketemu serializer:
      {serializer}
    """)
    for k, v in serializer.items():
      data[k] = v

    return data


class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer


@api_view(['POST'])
def registerUser(request):
  data = request.data
  try:
    user = User.objects.create(
      first_name=data['name'],
      username=data['email'],
      email=data['email'],
      password=make_password(data['password'])
    )

    serializer = UserSerializerWithToken(user, many=False)
    return Response(serializer.data)
  except:
    message = {'detail': 'User with this email already exists'}
    return Response(message, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
  user = request.user
  serializer = UserSerializerWithToken(user, many=False)

  data = request.data
  user.first_name = data['name']
  user.username = data['email']
  user.email = data['email']

  if data['password'] != '':
    user.password = make_password(data['password'])

  user.save()

  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
  user = request.user
  serializer = UserSerializer(user, many=False)
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
  users = User.objects.all()
  serializer = UserSerializer(users, many=True)
  return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUserById(request, pk):
  user = User.objects.get(id=pk)
  serializer = UserSerializer(user, many=False)
  return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request, pk):
  user = User.objects.get(id=pk)
  data = request.data
  user.first_name = data['name']
  user.username = data['email']
  user.email = data['email']
  user.is_staff = data['isAdmin']
  user.save()
  serializer = UserSerializer(user, many=False)

  return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteUser(request, pk):
  userForDeletion = User.objects.get(id=pk)
  userForDeletion.delete()
  return Response('User was deleted')
--#
