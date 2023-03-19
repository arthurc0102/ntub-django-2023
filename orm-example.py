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

# 查詢過濾 Post
# 會傳傳多筆資料，如果需要第一筆可以用 [0] 或是 .first() 取得

Post.objects.filter(id=9)  
Post.objects.filter(title='Title003')
Post.objects.filter(id=9, title='Title003')
Post.objects.filter(id=10, title='Title003')
Post.objects.filter(title='1111')

Post.objects.filter(title='1111').first()
Post.objects.filter(title='1111').last()
Post.objects.filter(title='1111')[0]
Post.objects.filter(title='1111')[0:2]

# 全部的 Post

Post.objects.all()
Post.objects.order_by('title')
Post.objects.order_by('-title')
Post.objects.order_by('?')

Post.objects.filter(title='1111').order_by('id')

# 修改 Post

post = Post.objects.get(id=9)
print(post.title)
post.title = 'Title003 - 修改過'
post.save()

posts = Post.objects.filter(title='1111')
posts.update(title='2222')

# 刪除 Post

post = Post.objects.get(id=9)
post.delete()

posts = Post.objects.filter(title='2222')
posts.delete()