from django.urls import path
from users.views import CreacionDeCuenta, Login, logout, agregar_avatar
from users import views

app_name = 'users'

urlpatterns = [path('register/',CreacionDeCuenta.as_view(),name="register"),
               path('login/',Login.as_view(), name="login"),
               path('logout/',logout.as_view(), name="logout"),
               path('editarusuario/', views.editarPerfil , name="editarusuario"),
               path('agregar_avatar/', agregar_avatar, name="agregar-avatar"),
               ]