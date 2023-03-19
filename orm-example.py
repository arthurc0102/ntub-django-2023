from first.models import Post


# 建立 Post 方法一

post = Post()
post.title = 'Title01'
post.content = 'Content01'
post.save()

# 建立 Post 方法一之一

post = Post(title='Title02', content='Content01')
post.save()

# 建立 Post 方法

Post.objects.create(title='Title003', content='Content003')

# 查詢 Post

Post.objects.get(id=9)
Post.objects.get(title='Title003')
Post.objects.get(id=9, title='Title003')
Post.objects.get(id=10, title='Title003')
Post.objects.get(title='1111')