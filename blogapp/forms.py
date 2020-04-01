from django import forms
from .models import Entry, Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'tagline', )


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('headline', 'blog', 'authors', 'content')