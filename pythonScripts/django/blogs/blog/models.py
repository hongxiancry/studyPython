#coding utf-8
__author__='chairuiya'

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags


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
	#增加浏览文章数量记录字段
	views = models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse('blog:detail',kwargs={'pk':self.pk})
	#设置文章默认排序方式
	class Meta:
		ordering = ['-created_Time']
	#文章每被浏览一次views加1
	def increase_views(self):
		self.views +=1
		self.save(update_fields=['views']) 
	#自动提取摘要
	def save(self,*args,**kwargs):
		if not self.excerpt:
			mkd = markdown.Markdown(extensions=['markdown.extensions.extra','markdown.extensions.codehilite'])
			  # strip_tags 去掉 HTML 文本的全部 HTML 标
			self.excerpt = strip_tags(mkd.convert(self.body))[0:50]

		super(Post,self).save(*args,**kwargs)




