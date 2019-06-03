## Gestion de inventario
Aplicación Web utilizando Django como framework Web que permite gestionar el inventario de una bodega
1.  Perimite registrar persona en el sistema
2. Permitir registrar un recurso en el sistema (ej: categoria, código, nombre, marca, serie)
3. Permitir asignar recursos a una persona.
4. Permitir trasladar uno o varios recursos de una persona a otra.
5. Consultar los recursos asignados a una persona.

### Probar de manera local
  * Pre-requisitos Python 3.+ y Virtualenv

1. Crear ambiente virtual **virtualenv inventario_env** y activar el ambiente **source inventario_env/bin/activate**
2. Clonar el proyecto **git clone https://github.com/andreayully/gestion-inventario.git**
3. **cd gestion-inventario/**

    - Instalar requerimientos **pip install -R requirements.txt**
4. Realizar migraciones
    - ``` python manage.py makemigrations ```
    - ``` python manage.py migrate ```

5. Runserver ``` python manage.py runserver ``` [http://127.0.0.1:8000](http://127.0.0.1:8000)

6. Crear "Categorias desde el admin de Django" o crear categorias predeterminada del cat_category.py
  - Desde la Shell de Django ``` python manage.py shell```
  - Copiar y pegar
  1. ```from recursos.cat_factory import generar_categorias ```
  2. ``` generar_categorias() ```

### Características
- Django 1.11
- Base de datos noSql - SQLite
- Plantilla Bootstrap [https://startbootstrap.com/](https://startbootstrap.com/themes/sb-admin-2/)
