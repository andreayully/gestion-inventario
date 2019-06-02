import factory
import factory.django
from recursos.models import Recurso

class CategoriaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Recurso
    nombre = factory.Faker('nombre')
