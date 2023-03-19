from django.contrib import admin

from first.models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title', 'content')