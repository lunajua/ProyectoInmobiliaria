from django import forms
from .models import Contacto, Propiedad , Image

class ContactoFormulario(forms.ModelForm):
    
    class Meta:
        model = Contacto
        fields = "__all__"

class CargaPropiedad(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = "__all__"


class ImageForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple':True}))

    class Meta:
        model = Image
        fields = ['image']