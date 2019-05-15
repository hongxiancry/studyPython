#coding utf-8
from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
path(r'',views.home,name='home'),
path(r'^post/(?P<pk>\d+)/$',views.detail,name='detail'),
path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.archives,name='archives'),
path(r'^category/(?P<pk>\d+)/$',views.category,name='category'),
]
