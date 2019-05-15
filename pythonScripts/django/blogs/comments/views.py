from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .models import Comment
from .forms import CommentForm

# Create your views here.
def post_comment(request,post_pk):
	post = get_object_or_404(Post,pk=post_pk)

	if request.method=='POST':
		#用户提交的数据存在 request.POST 中，这是一个类字典对象
		#利用表单数据构成comentForm的内容
		commentForm = CommentForm(request.POST)

		#判断表单是否合法：
		if commentForm.is_valid():
			#commit=False 表示仅仅利用form实例，不保存到数据库
			comment = commentForm.save(commit=False)
			comment.post = post
			#保存实例到数据库
			comment.save()
			#redirect 接受一个对象，并且重定向url到该对象的get_absolute_url方法所指向的地址
			return redirect(post)
		else:
			#返回页面三个内容 评论内容列表，文章对象，form表单
			comment_list = post.comment_set.all()
			context = {'post':post,
			'comment_list':comment_list,
			'commentForm':commentForm}
			return render(request,'blog/detail.html',context=context)
	return  redirect(post)




