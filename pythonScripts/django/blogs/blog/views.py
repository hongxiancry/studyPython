from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Post


def home(request):
	post_list = Post.objects.all().order_by('-created_Time')
	return render(request,'blog/homepage.html',context={
		'hometitle':'homepagetitle!',
		'loginfo':'hello ,welcome to your blog!',
		'post_list':post_list
		})

def detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'blog/detail.html',context={'post':post})
