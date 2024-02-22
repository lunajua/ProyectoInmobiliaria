from django.urls import path 
from appinmobiliaria import views
from appinmobiliaria.views import ContactoView

app_name = 'appinmobiliaria'

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="views"),
    path('pagina_no_encontrada/', views.pagina_no_encontrada, name="no-encontrado"),
    path('contact/', views.ContactoView.as_view(), name="contact"),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('property-agent/', views.property_agent, name="agente"),
    path('property-list/', views.property_list, name="lista"), 
    path('property-type/', views.property_type, name="tipo"),   
]
    
    
