#coding utf-8
from django.urls import path
from . import views

app_name='comments'
urlpatterns = [
path(r'^comment/(?P<post_pk>\d+)/$',views.post_comment,name='post_comment'),
]