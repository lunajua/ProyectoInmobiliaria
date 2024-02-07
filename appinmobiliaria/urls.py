from django.urls import path 
from appinmobiliaria import views


urlpatterns = [
    path('', views.index, name="Index"),
    path('about/', views.about, name="Views"),
    path('pagina_no_encontrada/', views.pagina_no_encontrada, name="No_encontrado"),
    path('contact/', views.contact, name="Contact"),
    path('testimonial/', views.testimonial, name="Testimonial"),
    # path('property-agent/', views.property_agent, name="Agente"),
    # path('property-list/', views.property_list, name="Lista"), 
    # path('property-type/', views.property_type, name="Tipo"),   
]
    
    
