from first.models import Post


# 建立 Post 方法一

post = Post()
post.title = 'Title01'
post.content = 'Content01'
post.save()

# 建立 Post 方法一之一

post = Post(title='Title02', content='Content01')
post.save()