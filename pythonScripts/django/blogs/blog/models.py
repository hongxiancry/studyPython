#coding utf-8
__author__='chairuiya'

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
#blog category
class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
#tags
class Tag(models.Model):
	name = models.CharField(max_length=500)
	def __str__(self):
		return self.name
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
	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})
	#设置文章默认排序方式
	class Meta:
		ordering = ['-created_Time']



