from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from recursos.models import Recurso
from users.models import Persona
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from recursos.forms import RecursoForm, RecursoUpdateForm
from django.views.generic.base import TemplateView
import string
import random
import datetime

# Create your views here.

def id_generator(size, chars=string.ascii_uppercase + string.digits):
     return str(''.join(random.choice(chars) for _ in range(size)))

class RecursoCreateView(CreateView):
    model=Recurso
    form_class= RecursoForm
    template_name='recursos/recursos.html'
    success_url = reverse_lazy('recursos:list_recurso')

    def form_valid(self, form):
        recurso = form.save(commit=False)
        recurso.codigo = id_generator(4)
        form.save()
        return super(RecursoCreateView, self).form_valid(form)

class RecursoListView(ListView):
    model=Recurso
    paginate_by= 10
    template_name= 'recursos/recursos_list.html'
    context_object_name = 'recursos'

    def get_context_data(self, **kwargs):
        context = super(RecursoListView, self).get_context_data(**kwargs)
        recursos= Recurso.objects.all()
        context['recursos'] = recursos
        context['is_real']=True
        return context

class RecursoUpdateView(UpdateView):
    model=Recurso
    form_class=RecursoUpdateForm
    template_name='recursos/recursos.html'
    success_url = reverse_lazy('recursos:list_recurso')

    def get_object(self, queryset=None):
        obj = Recurso.objects.get(pk=self.kwargs['id'])
        return obj

    def form_valid(self, form):
        recurso = form.save(commit=False)
        recurso.fecha_asignacion = datetime.datetime.now()
        form.save()
        return super(RecursoUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context=super(RecursoUpdateView, self).get_context_data(**kwargs)
        context['recurso']=Recurso.objects.get(pk=self.kwargs['id'])
        context['is_update'] = True
        return context


def asg_recurso(request, recurso_id, persona_id):
    recurso = Recurso.objects.get(pk=recurso_id)
    persona = Persona.objects.get(pk=persona_id)
    recurso.persona_asignada = persona
    recurso.save()
    return redirect('users:persona_view', id=persona_id)

def delete_recurso(request, recurso_id, persona_id):
    persona = Persona.objects.get(pk=persona_id)
    recurso = Recurso.objects.get(pk=recurso_id)
    recurso.persona_asignada = None
    recurso.save()
    return redirect('users:persona_view', id=persona_id)


class RecursoAddView(TemplateView):
    template_name= 'recursos/recursos_list.html'

    def get_context_data(self, **kwargs):
        context =super(RecursoAddView, self).get_context_data(**kwargs)
        recursos= Recurso.objects.exclude(persona_asignada__pk=self.kwargs['id'])
        persona = Persona.objects.get(pk=self.kwargs['id'])
        context['recursos'] = recursos
        context['persona']=persona
        context['is_add']=True
        return context
