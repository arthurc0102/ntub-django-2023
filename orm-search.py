from first.models import Post


Post.objects.filter(title='Title01')

Post.objects.filter(title__contains='Title')

Post.objects.filter(title__icontains='title')