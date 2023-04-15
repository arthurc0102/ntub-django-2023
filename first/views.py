from django.shortcuts import render, get_object_or_404, redirect

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
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('post_list')

    return render(request, 'post_create.html', {'form': form})


def post_update(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post_detail', post_id)

    return render(request, 'post_update.html', {'form': form})


def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post_list')