from first.models import Post


Post.objects.filter(title='Title01')

Post.objects.filter(title__contains='Title')

Post.objects.filter(title__icontains='title')

# 文件：https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups

Post.objects.exclude(title__icontains='title')