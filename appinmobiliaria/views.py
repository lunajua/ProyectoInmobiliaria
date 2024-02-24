from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy
from .forms import ContactoFormulario, CargaPropiedad
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    return render(request, 'appinmobiliaria/index.html') 

def about(request):
    return render(request, 'appinmobiliaria/about.html')

def pagina_no_encontrada(request):
    return render(request, 'appinmobiliaria/404.html')

def testimonial(request):
    return render(request, 'appinmobiliaria/testimonial.html')

def property_agent(request):
    return render(request, 'appinmobiliaria/property-agent.html')

def property_list(request):
    return render(request, 'appinmobiliaria/property-list.html')

def property_type(request):
    return render(request, 'appinmobiliaria/property-type.html')

class ContactoView(FormView):
    template_name = 'appinmobiliaria/contact.html'
    form_class = ContactoFormulario
    success_url = reverse_lazy('contact')  # Asume que 'contact' es el nombre de la URL de esta vista

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class AgregaPropiedad(LoginRequiredMixin,CreateView):    
    login_url = 'users/login'
    template_name = 'appinmobiliaria/carga_propiedad.html'
    form_class = CargaPropiedad
    success_url = reverse_lazy('appinmobiliaria:carga')
    
    def form_valid(self, form):        
        response = super().form_valid(form)
        messages.success(self.request, 'Propiedad cargada correctamente')
        return response
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
