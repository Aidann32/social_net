from django import forms
from .models import Post,Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content','image')

class CommentModelForm(forms.ModelForm):
    body=forms.CharField(label='',widget=forms.TextInput(attrs={
                        'placeholder':'Добавьте комментарий...'
                        }))
    class Meta:
        model=Comment
        fields=('body',)