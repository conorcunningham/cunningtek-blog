from django import forms
from .models import Post
from martor.fields import MartorFormField


class NewPostForm(forms.ModelForm):
    # content = MartorFormField(max_length=35000,
    #                           help_text='Maximum length is 35000 characters')

    class Meta:
        model = Post
        fields = ['title', 'content']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', ]
