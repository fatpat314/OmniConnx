from django import forms
from .models import Listing


class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta():
        model = Listing
        fields = ['title', 'author', 'content', 'sub_category']


# class Form(forms.Form):
#     first_name = forms.CharField(max_length=100)
