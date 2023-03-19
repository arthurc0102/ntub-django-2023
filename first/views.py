from django.shortcuts import render, get_object_or_404

from first.models import Post
from first.forms import PostForm


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})


def post_create(request):
    form = PostForm()
    return render(request, 'post_create.html', {'form': form})