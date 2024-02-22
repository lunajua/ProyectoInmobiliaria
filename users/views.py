from django.shortcuts import render

# Create your views here.
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