from django.shortcuts import render
from django.views import generic
from users.forms import UserForm
from users.forms import UserEditForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required


# Create your views here.



class CreacionDeCuenta(generic.CreateView):
    form_class = UserForm
    success_url = reverse_lazy('appinmobiliaria:index')
    template_name='users/register.html'


class Login(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('appinmobiliaria:index')
    

class logout(LogoutView):
    next_page = 'appinmobiliaria:index'

@login_required
def editarPerfil(request):

      usuario = request.user
     
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST) 
            
            if miFormulario.is_valid():  

                 informacion = miFormulario.cleaned_data
                 usuario.email = informacion['email']
                 
                 usuario.set_password(informacion['password1'])  # tuve que usar este método porque no guardaba la contraseña, además especifica que django valida los dos pass antes de guardarlos automáticamente.
                 usuario.save()
                 
                 return render(request, "appinmobiliaria/index.html") 
            
      else: 
            datos = {
                 'first name': usuario.first_name,
                 'email': usuario.email
            }

            miFormulario= UserEditForm(initial=datos) 

 
      return render(request, "users/editar_usuario.html", {"miFormulario":miFormulario, "usuario":usuario})