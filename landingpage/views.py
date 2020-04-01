from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    CreateView
)
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm
)


class HomePageView(TemplateView):
    template_name = 'homepage.html'


class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"

class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = '/'

class DashBoardView(TemplateView):
    template_name = 'dashboard.html'
