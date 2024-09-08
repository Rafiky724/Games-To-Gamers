
pip install django

pip freeze > requirements.txt

pip install -r requirements.txt

django-admin startproject Universidad 

django-admin startapp Academico

*Migracion Inicial Del Proyecto*
python manage.py migrate

*Migracion De La Tabla A La Base De Datos*
python manage.py makemigrations

*Super Usuario para que maneje todo, buena practica*
python manage.py createsuperuser  

python manage.py runserver

