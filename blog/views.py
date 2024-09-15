from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.forms import PostForm
from blog.models import Post

def hello_world(request):
    return HttpResponse("Hello, Blog!")

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})