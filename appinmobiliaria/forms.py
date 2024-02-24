from django import forms
from .models import Contacto, Propiedad

class ContactoFormulario(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = "__all__"

class CargaPropiedad(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = "__all__"

