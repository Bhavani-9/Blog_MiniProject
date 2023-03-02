from django.shortcuts import render,redirect
from .models import Post,Category
# Create your views here.

def blog(request):
    posts=Post.objects.all()

    context={
        'posts':posts,
    }
    return render(request,'blog/blog.html',context)


def post(request,title):
    print(title)
    try:
        post=Post.objects.get(title=title)
    except Post.DoesNotExist:
        post=None
    # post=Post.objects.all()
    print(20*'--',post)
    context={
        'post':post,
    }
    return render(request,'blog/post.html',context)



