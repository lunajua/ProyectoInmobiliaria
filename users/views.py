from django.shortcuts import render
from django.views import generic
from users.forms import UserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.

from django.views import generic
from users.forms import UserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy



class CreacionDeCuenta(generic.CreateView):
    form_class = UserForm
    success_url = 'pre_entrega/index.html'
    template_name='pre_entrega/index.html'


class Login(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('pre_entrega:index')
    

class logout(LogoutView):
    next_page = 'pre_entrega:index'