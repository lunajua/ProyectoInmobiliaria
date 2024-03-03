from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Image , Propiedad
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, ListView
from django.urls import reverse_lazy
from .forms import ContactoFormulario, CargaPropiedad, ImageForm, PropiedadSearchForm
from django.contrib import messages
from users.models import Avatar
from django.contrib.auth.mixins import LoginRequiredMixin

 

def about(request):
    return render(request, 'appinmobiliaria/about.html')

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
        propiedad = form.save()
        form_image = ImageForm(self.request.POST, self.request.FILES)
        if form_image.is_valid():
            for img in self.request.FILES.getlist('image'):
                Image.objects.create(propiedad=propiedad, image=img)
            messages.success(self.request, 'Propiedad y imágenes cargadas correctamente')
            return redirect(self.success_url)
        else:

            messages.error(self.request, 'Error al cargar las imágenes')
            return self.render_to_response(self.get_context_data(form=form, image_form=form_image))
    
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['image_form'] = ImageForm(self.request.POST, self.request.FILES)
        else:
            context['image_form'] = ImageForm()
        return context
    

def ver_propiedad(request, propiedad_id):
    property_instance = Propiedad.objects.get(pk=propiedad_id)

    images = property_instance.images.all()

    return render(request, 'appinmobiliaria/propiedad.html', {'property': property_instance, 'images': images})


class VerPropiedades(ListView):
    model = Propiedad
    template_name = 'appinmobiliaria/property-list.html'
    context_object_name = "propiedades"


class PropiedadListView(ListView):
    model = Propiedad
    template_name = 'appinmobiliaria/propiedad_search.html'
    context_object_name = "propiedades"

    def get_queryset(self):
        venta_o_alquiler = self.request.GET.get('venta_o_alquiler', None)

        queryset = Propiedad.objects.none()
        if venta_o_alquiler is not None and venta_o_alquiler != 'Seleccione Venta o Alquiler':
            try:
                venta_o_alquiler_int = int(venta_o_alquiler)
                queryset = Propiedad.objects.filter(venta_o_alquiler=venta_o_alquiler_int)
            except ValueError:
                pass
        return queryset


class PropiedadSearchView(FormView):
    template_name = 'appinmobiliaria/index.html'
    form_class = PropiedadSearchForm

    def form_valid(self, form):
        
        venta_o_alquiler = form.cleaned_data.get('venta_o_alquiler')


        redirect_url = f'/?tipo=venta_o_alquiler={venta_o_alquiler}'

        return redirect(redirect_url)

class PropiedadUpdateView(LoginRequiredMixin,UpdateView):
    model = Propiedad
    form_class = CargaPropiedad
    template_name = 'appinmobiliaria/modifica_propiedad.html'
    success_url = reverse_lazy ('appinmobiliaria:ver-propiedades')

class EditaPropiedades(LoginRequiredMixin,ListView):
    model = Propiedad
    template_name = 'appinmobiliaria/editar_propiedades.html'
    context_object_name = "propiedades"


class EliminarPropiedad(LoginRequiredMixin,DeleteView):
    model = Propiedad
    template_name = "appinmobiliaria/borrar_propiedad.html"
    success_url = reverse_lazy('appinmobiliaria:ver-propiedades')