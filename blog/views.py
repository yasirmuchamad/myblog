from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def post_list(request):
    post = Post.published.all()
    return render(request, 'blog/post/list.html',{'post':'post'})

def post_detail(request, year, mounth, day, post):
    post = get_object_or_404(Post, slug=post,
                                    status='published', 
                                    publish__year=year,
                                    publish__mounth=mounth,
                                    publish__day=day)
    return render(request, 'blog/post/detail.html', {'post':post})