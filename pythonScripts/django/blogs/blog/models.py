#coding utf-8
__author__='chairuiya'

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#blog category
class Category(models.Model):
	name = models.CharField(max_length=100)
#tags
class Tag(models.Model):
	name = models.CharField(max_length=500)
#post
class Post(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	created_Time = models.DateTimeField()
	modified_time = models.DateTimeField()
#文章摘要
	excerpt =models.CharField(max_length=200,blank=True)

	tags = models.ManyToManyField(Tag,blank=True)
	category = models.ForeignKey(Category,on_delete=models.SET)
	user = models.ForeignKey(User,on_delete=models.SET)



