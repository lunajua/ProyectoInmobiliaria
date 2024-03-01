from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from users.models import Avatar
class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username' , 'email' , 'password1', 'password2')
        help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    email = forms.EmailField(label="Ingresar E-mail:")
    password1 = forms.CharField(label='Contraseña:', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña:', widget=forms.PasswordInput) 

    class Meta:
        model = User
        fields = [ 'email', 'password1', 'password2'] 
        help_texts = {k:"" for k in fields}

class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']

    def init(self, args, kwargs):
        self.user = kwargs.pop('user', None)
        super(AvatarFormulario, self).init(args, kwargs)

    def save(self, commit=True):
        self.instance.user = self.user
        return super(AvatarFormulario, self).save(commit=commit)