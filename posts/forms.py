from django import forms
from . models import Post
class PostForm(forms.ModelForm):
    """docstring for PostForm """

    class Meta:
        """docstring for Meta"""
        model = Post
        fields = [
            "title",
            "content",
            "wait",
            "color",
            "image",
            "type"
        ]