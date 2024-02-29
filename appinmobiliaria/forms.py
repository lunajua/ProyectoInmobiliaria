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

class PropiedadSearchForm(forms.Form):
    VENTA_O_ALQUILER_CHOICES = [        
        [1, "Venta"],
        [2, "Alquiler"],
    ]
    
    venta_o_alquiler = forms.ChoiceField(choices=VENTA_O_ALQUILER_CHOICES)
    