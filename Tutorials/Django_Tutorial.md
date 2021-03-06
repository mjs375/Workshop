# D J A N G O
- *Django is a Python Web framework.*

- **Install:** ```$ python3 -m pip install Django``` / ```$ pip3 install Django```
- **Create Project:** ```$ django-admin startproject PROJECT_NAME```
- **Run Server:** ```$ python3 manage.py runserver```
- **Create App:** ```$ python3 manage.py startapp APP_NAME```
  - **Install App:** *open ```settings.py```, add ```'myapp'``` to ```INSTALLED_APPS = [...]```*
- **Update DB:*** ```$ python3 manage.py makemigrations```, ```$ python3 manage.py migrate```

- **Create an Admin User**: ```$ python3 manage.py createsuperuser```
  - *1. Enter a username, email, password.*
  - *2. ```$ python3 manage.py runserver```: start up the server```
  - *3. Open the web browser and add ```/admin/``` to the local domain.*
    - ```django.contrib.auth``` must be on


### Files
- **```urls.py```:** **
```python
from django.urls import path
from . import views # import views from this directory/project

urlpatterns = [
path("", views.index, name="index"), 
  # from the URL pattern "" [aka index/homepage], go to index() in views.py
path()
]
```
