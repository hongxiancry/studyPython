#coding utf-8
from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
path(r'',views.home,name='home'),
path(r'^post/(?P<pk>\d+)/$',views.detail,name='detail'),
]
