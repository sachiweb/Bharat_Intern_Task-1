from unicodedata import category
from django.shortcuts import redirect, render
from .models import Post
# Create your views here.

def index(request):
    featured_post = Post.objects.all().filter(category=0)[:1]
    django_post = Post.objects.all().filter(fram=0)[:2]
    flask_post = Post.objects.all().filter(fram=1)[:2]

    context = {'featured_post':featured_post,'django_post':django_post,'flask_post':flask_post}
    return render(request, 'index.html', context)



def PostDetail(request,pk):
    post_detail = Post.objects.filter(pk=pk)
    context = {'post_detail':post_detail}
    return render(request, 'post_detail.html', context)

def add(request):
    if request.method == 'POST':
        title=request.POST['title']
        category=request.POST['category']
        fram=request.POST['fram']
        thumbnail=request.POST['thumbnail']
        body=request.POST['body']
        summary=request.POST['summary']

        post=Post(title=title,category=category,fram=fram,thumbnail=thumbnail,body=body,summary=summary)
        post.save()
        return redirect('home')
    # else:
    #     return redirect('add')
    return render(request, 'new_post.html')