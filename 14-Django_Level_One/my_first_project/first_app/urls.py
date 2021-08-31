from django.urls import re_path
from first_app import views


urlpatterns = [
    re_path('^$', views.index, name='index')
]
