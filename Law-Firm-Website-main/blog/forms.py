from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    A class to display comment form
    """
    class Meta:
        model = Comment
        fields = ('body',)
