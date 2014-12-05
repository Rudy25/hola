from django import forms
from usuarioperfil.models import Userprofile
from django.contrib.auth.models import User
from django.forms import ModelForm

class UserprofileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        fields = ('telefono', 'provincia', 'distrito', 'departamento', 'zona_horaria',)
class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
                    'password': forms.PasswordInput(),
                }
