from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from users.models import Avatar
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from users.forms import UserForm, AvatarFormulario, UserEditForm


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


class VerAvatar():
     model = Avatar



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



@login_required
def agregar_avatar(request):
    
    if request.method == 'POST':
        
        mi_form = AvatarFormulario(request.POST, request.FILES) 
            
        if mi_form.is_valid():
            user = User.objects.get(username=request.user)
            print(f"\n\n{mi_form.cleaned_data['imagen']}\n")

            try:
                avatar = Avatar.objects.get(user=user)
            except Avatar.DoesNotExist:
                avatar= Avatar(user=user, imagen= mi_form.cleaned_data['imagen'])
            else:
                 avatar.imagen = mi_form.cleaned_data['imagen']
           
            avatar.save
                             
            return render(request, "appinmobiliaria/index.html") 
            
    else:
        mi_form = AvatarFormulario()

    context_data = {"mi_form": mi_form}
    return render(request, "users/agregar_avatar.html", context_data)





class UserAvatarView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id', None)
        if user_id:
            avatar = get_object_or_404(Avatar, user_id=user_id)
            if avatar.imagen:
                return HttpResponse(avatar.imagen)
            else:
                return HttpResponse("No se encontró un avatar para el usuario", status=404)
        else:
            return HttpResponse("ID de usuario no proporcionado", status=400)