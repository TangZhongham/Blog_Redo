from django import forms

from .models import UserPost


class UserPostForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ['title', 'body', 'author']