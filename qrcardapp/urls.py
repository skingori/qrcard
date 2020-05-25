from django.conf.urls import url
from django.urls import path, re_path
from . import views
from django.http import Http404

app_name = 'garbage_app'

urlpatterns = [
  path('', views.Homepage.as_view(), name='home'),
  path('signup/', views.SignUp.as_view(), name='signup')
]
