from django.conf.urls import url, include
from recursos.views import *

urlpatterns = [
     url(r'^$', RecursoCreateView.as_view(), name='create_recurso'),
     url(r'lista/', RecursoListView.as_view(), name='list_recurso'),
     url(r'asignar/(?P<id>\d+)/$', RecursoAddView.as_view(), name='add_recurso'),
     url(r'asignar/(?P<recurso_id>\d+)/(?P<persona_id>[0-9]+)$', asg_recurso, name='asg_recurso'),
     url(r'delete/(?P<recurso_id>\d+)/(?P<persona_id>[0-9]+)$', delete_recurso, name='delete_recurso'),
     url(r'editar/(?P<id>\d+)/$', RecursoUpdateView.as_view(), name='update_recurso'),
]
