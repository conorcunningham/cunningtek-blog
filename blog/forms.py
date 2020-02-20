from django import forms
from .models import Post


class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', ]
