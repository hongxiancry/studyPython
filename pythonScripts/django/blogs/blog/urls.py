#coding utf-8
from django.urls import path
from . import views

app_name='blog'
urlpatterns = [
path(r'',views.HomeView.as_view(),name='home'),
path(r'^post/(?P<pk>\d+)/$',views.PostDetailView.as_view(),name='detail'),
path(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$',views.ArchivesView.as_view(),name='archives'),
path(r'^category/(?P<pk>\d+)/$',views.CategoryView.as_view(),name='category'),
path(r'^contact/$',views.contact,name='contact'),
path(r'^about/$',views.about,name='about'),
]
