from django.urls import path, re_path

from . import views

urlpatterns = [
  path('__TABLENAME_PLURAL_LOWER__/create/', views.create__TABLENAME_CASE__, name="__TABLENAME_LOWER__-create"),
  path('__TABLENAME_PLURAL_LOWER__/list/', views.get__TABLENAME_CASE__s, name="__TABLENAME_LOWER__-list"),

  path('__TABLENAME_PLURAL_LOWER__/update/<str:pk>/', views.update__TABLENAME_CASE__, name="__TABLENAME_LOWER__-update"),
  path('__TABLENAME_PLURAL_LOWER__/delete/<str:pk>/', views.delete__TABLENAME_CASE__, name="__TABLENAME_LOWER__-delete"),

  # extra urls

  # detail terakhir
  # path('__TABLENAME_PLURAL_LOWER__/detail/<str:pk>/', views.get__TABLENAME_CASE__, name="__TABLENAME_LOWER__-detail"),
  path('__TABLENAME_PLURAL_LOWER__/<str:pk>/', views.get__TABLENAME_CASE__, name="__TABLENAME_LOWER__-detail"),
]