Making a virtual environment:

~ python3 -m venv .venv   [Here, .venv is the folder name]

Another way, and the way we are going to follow:

https://pypi.org/project/uv/


To deactivate the venv:
~deactivate

To install Django/Flask:
~uv pip install Django/Flask

To start building the project folder and 
~ django-admin startproject <fileName>
~ cd <fileName>

To run:
~ python manage.py runserver

In case I need to specify the port number while running the server:
~ python manage.py runserver <PORT NUMBER>
