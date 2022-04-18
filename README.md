Primeros pasos:
# Aquí pondremos las instrucciones para poder ejecutar nuestra aplicación
1) Crear el entorno virtual: virtualenv my_django_app
2) Entrar en el entorno virtual: source my_django_app/bin/activate
3) Cerrar el entorno virtual: deactivate
5) Crear un archivo con los requirements: pip freeze > requirements. txt
6) Correr la aplicación: python manage.py runserver
7) Creamos un archivo urls.py dentro de la aplicacion
8) migrar la base de datos: python manage.py makemigrations myApp
9) python manage.py migrate
10) Crear superusuario: python manage.py createsuperuser
