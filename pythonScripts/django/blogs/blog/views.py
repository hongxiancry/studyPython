from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from comments.forms import CommentForm
from .models import Post,Category
import markdown

def home(request):
	post_list = Post.objects.all()
	return render(request,'blog/homepage.html',context={
		'hometitle':'homepagetitle!',
		'loginfo':'hello ,welcome to your blog!',
		'post_list':post_list
		})

def detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	post.body = markdown.markdown(post.body,extensions=[
		'markdown.extensions.extra',
		'markdown.extensions.codehilite',
		'markdown.extensions.toc',
		])
	commentForm = CommentForm()
	comment_list = post.comment_set.all()
	context = {
	'post':post,
	'commentForm':commentForm,
	'comment_list':comment_list
	}
	return render(request,'blog/detail.html',context=context)

def archives(request,year,month):
	post_list = Post.objects.filter(created_Time__year=year,
		created_Time__month=month)
	return render(request,'blog/homepage.html',context={'post_list':post_list})

def category(request,pk):
	cate = get_object_or_404(Category,pk=pk)
	post_list = Post.objects.filter(category=cate)
	return render(request,'blog/homepage.html',context={'post_list':post_list})
