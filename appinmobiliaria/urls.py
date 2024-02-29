from django.urls import path 
from appinmobiliaria import views
from appinmobiliaria.views import ContactoView, AgregaPropiedad, ver_propiedad, PropiedadListView, PropiedadSearchView

app_name = 'appinmobiliaria'

urlpatterns = [
    path('', PropiedadSearchView.as_view(), name="index"),
    path('about/', views.about, name="views"),
    path('carga/', views.AgregaPropiedad.as_view(), name="carga"),
    path('contact/', views.ContactoView.as_view(), name="contact"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('property-agent/', views.property_agent, name="agente"),
    path('property-list/', PropiedadListView.as_view(), name="lista"), 
    path('property-type/', views.property_type, name="tipo"),   
    path('ver-propiedad/<int:propiedad_id>', views.ver_propiedad, name="ver-propiedad")
]
    
    
