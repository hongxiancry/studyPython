from django.contrib import admin

# Register your models here.
from .models import Post,Tag,Category

class Postuser(admin.ModelAdmin):
	list_display = ['id','title','created_Time','modified_time','user','category']

admin.site.register(Post,Postuser)
admin.site.register(Tag)
admin.site.register(Category)
