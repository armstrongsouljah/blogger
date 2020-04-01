from django.urls import path
from .views import (
    CreateBlogView
)
app_name = 'blogapp'

urlpatterns = [
  path('new', CreateBlogView.as_view(), name='new')
]