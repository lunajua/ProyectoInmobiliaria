from django.urls import path 
from appinmobiliaria import views


urlpatterns = [
    path('', views.index),
    path('about/', views.about),   
]
    
    
