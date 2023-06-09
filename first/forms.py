from django import forms

from first.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        # fields = ('title', 'content')


class PostDeleteConfirmForm(forms.Form):
    check = forms.BooleanField(
        required=True,
        label="你確定要刪除這篇文章嗎？真的會消失喔！！！",
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # fields = "__all__"
        exclude = ("post",)


class CommentDeleteConfirmForm(forms.Form):
    check = forms.BooleanField(
        required=True,
        label="你確定要刪除這篇留言嗎？真的會消失喔！！！",
    )
