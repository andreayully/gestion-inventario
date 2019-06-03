import factory
import factory.django
from recursos.models import Categoria

def generar_categorias():
    lista = ['Herramientas', 'Aseo', 'Elementos de Seguridad', 'Articulos Diversos']
    for nombre in lista:
        #nombre = CategoriaFactory.create()
        categoria = Categoria(nombre=nombre)
        categoria.save()
        print(nombre)



#from recursos.cat_factory import generar_categorias
#generar_categorias()
