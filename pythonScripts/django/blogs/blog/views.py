from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse
from comments.forms import CommentForm
from .models import Post,Category,Tag
import markdown
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

#class 视图替换之前的写法
def home(request):
	post_list = Post.objects.all()
	#分页
	paginator = Paginator(post_list,3)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)

	return render(request,'blog/homepage.html',context={
		'hometitle':'homepagetitle!',
		'loginfo':'hello ,welcome to your blog!',
		'post_list':posts
		})
#改为ListView
class HomeView(ListView):
	model = Post
	template_name = 'blog/homepage.html'
	context_object_name = 'post_list'
	paginate_by = 2

	def get_context_data(self,**kwargs):
		context = super(HomeView,self).get_context_data(**kwargs)
		context.update({
			'hometitle':'homepagetitle!',
			'loginfo':'hello ,welcome to your blog!',
			})
		return context

#改为DetailView
class PostDetailView(DetailView):
	model = Post
	template_name = 'blog/detail.html'
	context_object_name = 'post'

	#计算阅读量
	def get(self,request,*args,**kwargs):
		#先调用父类get_object 方法的原因是为了获得self.object,然后调用增加阅读计数的函数
		response = super(PostDetailView,self).get(request,*args,**kwargs)
		self.object.increase_views()
		return response
	#渲染postbody,这对应着 detail 视图函数中根据文章的 id（也就是 pk）获取文章，然后对文章的 post.body 进行 Markdown 渲染的代码部分。
	def get_object(self,queryset=None):
		post = super(PostDetailView,self).get_object(queryset=None)
		post.body = markdown.markdown(post.body,extensions=[
			'markdown.extensions.extra',
			'markdown.extensions.codehilite',
			'markdown.extensions.toc',
			])
		return post
	# 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
	# 还要把评论表单、post 下的评论列表传递给模板。
	def get_context_data(self,**kwargs):
		context = super(PostDetailView,self).get_context_data(**kwargs)
		commentForm = CommentForm()
		comment_list = self.object.comment_set.all()
		context.update({
			'commentForm':commentForm,
			'comment_list':comment_list
			})
		return context

#改写为class类
class ArchivesView(ListView):
	model = Post
	template_name= 'blog/homepage.html'
	context_object_name = 'post_list'

	paginate_by = 2

	def get_queryset(self):
		year = self.kwargs.get('year')
		month = self.kwargs.get('month')
		return super(ArchivesView,self).get_queryset().filter(created_Time__year=year,created_Time__month=month)

#改写为Listview的子类
class CategoryView(ListView):
	model = Post
	template_name='blog/homepage.html'
	context_object_name = 'post_list'
	paginate_by = 2

	def get_queryset(self):
		cate = get_object_or_404(Category,pk=self.kwargs.get('pk'))
		return super(CategoryView,self).get_queryset().filter(category=cate)

def contact(request):
	return render(request,'contact.html',context={
		})

def about(request):
	return render(request,'about.html',context={})

#获取tag
class TagView(ListView):
	model = Post
	template_name = 'blog/homepage.html'
	context_object_name = 'post_list'

	paginate_by=2

	def get_queryset(self):
		tag = get_object_or_404(Tag,pk=self.kwargs.get('pk'))
		return super(TagView,self).get_queryset().filter(tags=tag)
#搜索功能实现
def search(request):
	keywords = request.GET.get('search')
	error_message=''
	if not keywords:
		error_message='请输入关键词'
		return render(request,'blog/homepage.html',context={'error_message':error_message})
	else:
		post_list = Post.objects.filter(title__icontains=keywords)
		return render(request,'blog/homepage.html',context={'error_message':error_message,'post_list':post_list})






