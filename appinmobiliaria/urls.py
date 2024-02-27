from django.urls import path 
from appinmobiliaria import views
from appinmobiliaria.views import ContactoView, AgregaPropiedad, ver_propiedad

app_name = 'appinmobiliaria'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="views"),
    path('carga/', views.AgregaPropiedad.as_view(), name="carga"),
    path('contact/', views.ContactoView.as_view(), name="contact"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('property-agent/', views.property_agent, name="agente"),
    path('property-list/', views.property_list, name="lista"), 
    path('property-type/', views.property_type, name="tipo"),   
    path('ver-propiedad/<int:propiedad_id>', views.ver_propiedad, name="ver-propiedad")
]
    
    
