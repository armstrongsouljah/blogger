from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import EntryForm, BlogForm


class CreateBlogView(LoginRequiredMixin, CreateView):
    template_name = 'new_blog.html'
    form_class = BlogForm
    success_url = '/'

    def form_valid(self, form):
        if not form.is_valid():
            return super().form_invalid(form)
        form.save()
        return super().form_valid(form)
