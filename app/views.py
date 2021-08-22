from django.shortcuts import render
from django.views.generic import View
from .models import Article
# Create your views here.

class IndexView(View):
    def get(self,request,*args,**kwargs):
        # ここにデータ取得するコードを書く
        return render(request,'index.html')


class BlogListView(View):
    def get(self,request,*args,**kwargs):
        blogs_data =Article.objects.order_by('-id')
        return render(request,'blog.html',{
            'blogs_data':blogs_data
        })

class BlogDetailView(View):
    def get(self,request,*args,**kwargs):
        blog_data =Article.objects.get(id=self.kwargs['pk'])
        return render(request,'blog_detail.html',{
            'blog_data':blog_data
        })