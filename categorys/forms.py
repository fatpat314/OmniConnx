from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    # text = forms.CharField(label='Your name', max_length=100)

    class Meta:
        model = Comment
        fields = ('author', 'text',)
