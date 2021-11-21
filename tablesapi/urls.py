from django.urls import path

from . import views
from .views import PicturesList
from django.conf.urls import (
  handler400, handler403, handler404, handler500)

urlpatterns = [
    path('', views.index, name='hello'),
    path('pics/', PicturesList.as_view(), name='pictures_url'),
]

