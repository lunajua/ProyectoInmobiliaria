from django.urls import path 
from appinmobiliaria import views
from appinmobiliaria.views import ContactoView, AgregaPropiedad, ver_propiedad, PropiedadListView, PropiedadSearchView, VerPropiedades, PropiedadUpdateView, EditaPropiedades, EliminarPropiedad
from users.views import UserAvatarView

app_name = 'appinmobiliaria'

urlpatterns = [
    path('', PropiedadSearchView.as_view(), name="index"),
    path('about/', views.about, name="views"),
    path('carga/', views.AgregaPropiedad.as_view(), name="carga"),
    path('contact/', views.ContactoView.as_view(), name="contact"),
    path('property-list/', PropiedadListView.as_view(), name="lista"),    
    path('ver-propiedad/<int:propiedad_id>', views.ver_propiedad, name="ver-propiedad"),
    path('ver-propiedades/', VerPropiedades.as_view(), name="ver-propiedades"),
    path('avatar/<int:user_id>', UserAvatarView.as_view(),name="user_avatar"),
    path('modifica_propiedad/<int:pk>', PropiedadUpdateView.as_view(), name="modificar_propiedad"),
    path('editar_propiedades/', EditaPropiedades.as_view(), name="editar_propiedades"),
    path('propiedad/<int:pk>/delete', EliminarPropiedad.as_view(), name="eliminar-propiedad")
]

