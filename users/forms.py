from django import forms
from django.forms import ModelForm
from users.models import Persona

class PersonaForm(ModelForm):
    email = forms.EmailInput(attrs={'id':"inputEmail"})
    class Meta:
        model=Persona
        exclude=['username', 'password', 'is_active', 'last_login', 'groups', 'user_permissions', 'is_staff', 'date_joined', 'is_superuser', 'fecha_registro']
        fields=['first_name', 'last_name', 'identificacion', 'email']
