from django.shortcuts import render
from django.views import generic
from users.forms import UserForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.



class CreacionDeCuenta(generic.CreateView):
    form_class = UserForm
    success_url = reverse_lazy('users:index')
    template_name='users/register.html'


class Login(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('appinmobiliaria:index')
    

class logout(LogoutView):
    next_page = 'appinmobiliaria:index'