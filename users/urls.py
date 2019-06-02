from django.conf.urls import url, include
from users.views import PersonaCreateView, PersonaView, PersonaListView


urlpatterns = [
     url(r'^$', PersonaCreateView.as_view(), name='create_persona'),
     url(r'^lista/', PersonaListView.as_view(), name='list_persona'),
     url(r'^ver/(?P<id>\d+)/$', PersonaView.as_view(), name='persona_view'),
]
