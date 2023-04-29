from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=500)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(max_length=500)

    # FK 刪除的策略
    # models.CASCADE：連帶刪除 -> 刪除 Post 時一併刪除 Comment
    # models.PROTECT：保護 -> 刪除 Post 時，若有 Comemnt 存在阻止 Post 刪除
    # models.SET_DEFAULT：刪除 Post 時，將 Comment 中的 post 欄位設定成預設值
    # models.SET_NULL：刪除 Post 時，將 Comment 中的 post 欄位設定成 null    
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
