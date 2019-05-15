from ..models import Post,Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=4):
	return Post.objects.all().order_by('-created_Time')[:num]

@register.simple_tag
def get_archives():
	return Post.objects.dates('created_Time','month',order='DESC')

@register.simple_tag
def get_Categories():
	return Category.objects.all()
