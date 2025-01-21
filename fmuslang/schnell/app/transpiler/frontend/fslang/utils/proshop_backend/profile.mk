--% index/fmus
.,d
	__init__.py,f(e=__FILE__=__init__.py)
	exceptions.py,f(e=__FILE__=admin.py)
	models.py,f(e=__FILE__=models.py)
	renderers.py,f(e=__FILE__=renderers.py)
	serializers.py,f(e=__FILE__=serializers.py)
	urls.py,f(e=__FILE__=urls.py)
	views.py,f(e=__FILE__=views.py)
--#

--% __init__.py
--#

--% exceptions.py
from rest_framework.exceptions import APIException

class ProfileDoesNotExist(APIException):
  status_code = 400
  default_detail = 'The requested profile does not exist.'
--#

--% models.py
from django.db import models
from main.helpers import TimestampedModel

class Profile(TimestampedModel):
  user = models.OneToOneField(
    'user.User', on_delete=models.CASCADE
  )
  bio = models.TextField(blank=True)
  image = models.URLField(blank=True)
  follows = models.ManyToManyField(
    'self',
    related_name='followed_by',
    symmetrical=False
  )
  # favorites = models.ManyToManyField(
  #   'article.Article',
  #   related_name='favorited_by'
  # )
  def __str__(self):
    return self.user.username

  def follow(self, profile):
    self.follows.add(profile)

  def unfollow(self, profile):
    self.follows.remove(profile)

  def is_following(self, profile):
    return self.follows.filter(pk=profile.pk).exists()

  def is_followed_by(self, profile):
    return self.followed_by.filter(pk=profile.pk).exists()

  def favorite(self, article):
    self.favorites.add(article)

  # def unfavorite(self, article):
  #   self.favorites.remove(article)

  # def has_favorited(self, article):
  #   return self.favorites.filter(pk=article.pk).exists()
--#

--% renderers.py
from main.helpers import CustomJSONRenderer

class ProfileJSONRenderer(CustomJSONRenderer):
  object_label = 'profile'
  pagination_object_label = 'profiles'
  pagination_count_label = 'profilesCount'
--#

--% serializers.py
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
  username = serializers.CharField(source='user.username')
  bio = serializers.CharField(allow_blank=True, required=False)
  image = serializers.SerializerMethodField()
  following = serializers.SerializerMethodField()

  class Meta:
    model = Profile
    fields = ('username', 'bio', 'image', 'following',)
    read_only_fields = ('username',)

  def get_image(self, obj):
    if obj.image:
      return obj.image

    return 'http://clipart-library.com/images/8TzngraXc.jpg'

  def get_following(self, instance):
    request = self.context.get('request', None)
    if request is None:
      return False

    if not request.user.is_authenticated():
      return False

    follower = request.user.profile
    followee = instance

    return follower.is_following(followee)
--#

--% urls.py
from django.urls import path, re_path
from .views import ProfileRetrieveAPIView, ProfileFollowAPIView

urlpatterns = [
  re_path(r'^profiles/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
  re_path(r'^profiles/(?P<username>\w+)/follow/?$', ProfileFollowAPIView.as_view()),
]
--#

--% views.py
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .renderers import ProfileJSONRenderer
from .serializers import ProfileSerializer

class ProfileRetrieveAPIView(RetrieveAPIView):
  permission_classes = (AllowAny,)
  queryset = Profile.objects.select_related('user')
  renderer_classes = (ProfileJSONRenderer,)
  serializer_class = ProfileSerializer

  def retrieve(self, request, username, *args, **kwargs):
    try:
      profile = self.queryset.get(user__username=username)
    except Profile.DoesNotExist:
      raise NotFound('A profile with this username does not exist.')

    serializer = self.serializer_class(profile, context = {
      'request': request
    })

    return Response(serializer.data, status=status.HTTP_200_OK)

class ProfileFollowAPIView(APIView):
  permission_classes = (IsAuthenticated,)
  renderer_classes = (ProfileJSONRenderer,)
  serializer_class = ProfileSerializer

  def delete(self, request, username=None):
    follower = self.request.user.profile
    try:
      followee = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
      raise NotFound('A profile with this username was not found.')

    follower.unfollow(followee)
    serializer = self.serializer_class(followee, context={
      'request': request
    })
    return Response(serializer.data, status=status.HTTP_200_OK)

  def post(self, request, username=None):
    follower = self.request.user.profile
    try:
      followee = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
      raise NotFound('A profile with this username was not found.')

    if follower.pk is followee.pk:
      raise serializers.ValidationError('You can not follow yourself.')

    follower.follow(followee)

    serializer = self.serializer_class(followee, context={
      'request': request
    })

    return Response(serializer.data, status=status.HTTP_201_CREATED)
--#
