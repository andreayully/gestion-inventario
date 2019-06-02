from django import forms
from django.forms import ModelForm
from recursos.models import Recurso


class RecursoForm(ModelForm):
    # email = forms.EmailInput(attrs={'id':"inputEmail"})
    class Meta:
        model=Recurso
        exclude=['codigo', 'fecha_asignacion']
        fields=['nombre', 'marca', 'categoria', 'persona_asignada',]

class RecursoUpdateForm(ModelForm):
    class Meta:
        model=Recurso
        fields=['nombre', 'marca', 'categoria', 'persona_asignada',]
