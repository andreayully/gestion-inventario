from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from users.models import Persona
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from users.forms import PersonaForm

# Create your views here.
class PersonaCreateView(CreateView):
    model=Persona
    form_class=PersonaForm
    template_name='users/persona.html'
    success_url = reverse_lazy('users:list_persona')

    def form_valid(self, form):
        persona =form.save(commit=False)
        persona.username=persona.email
        form.save()
        return super(PersonaCreateView, self).form_valid(form)


class PersonaListView(ListView):
    model=Persona
    template_name= 'users/personas_list.html'

    def get_context_data(self, **kwargs):
        context = super(PersonaListView, self).get_context_data(**kwargs)
        context['personas'] = Persona.objects.all()
        return context


class PersonaView(TemplateView):
    template_name = 'users/persona_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PersonaView, self).get_context_data(*args, **kwargs)
        persona = Persona.objects.get(pk=self.kwargs['id'])
        articulos = persona.recurso_set.all()
        context['persona'] = persona
        context['articulos'] = articulos
        #context['add_recurso'] = True
        return context
