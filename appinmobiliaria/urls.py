from django.urls import path 
from appinmobiliaria import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('pagina_no_encontrada/', views.pagina_no_encontrada),
    path('contact/', views.contact),   
]
    
    
