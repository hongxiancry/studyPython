from ..models import Post,Category,Tag
from django import template
from django.db.models import Count

register = template.Library()

@register.simple_tag
def get_recent_posts(num=4):
	return Post.objects.all().order_by('-created_Time')[:num]

@register.simple_tag
def get_archives():
	return Post.objects.dates('created_Time','month',order='DESC')

@register.simple_tag
def get_Categories():
	return Category.objects.annotate(post_nums=Count('post')).filter(post_nums__gt=0)

@register.simple_tag
def get_tags():
	return Tag.objects.annotate(num_posts = Count('post')).filter(num_posts__gt=0)