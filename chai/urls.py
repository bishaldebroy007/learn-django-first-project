# from django.contrib import admin
from django.urls import path
from . import views  # I had to import this
#how it will be read:
# localhost:8000/chai
#localhost:8000/chai/order

# I just copied the url.py code from the main project url.py for the new app called chai
urlpatterns = [
    path('', views.all_chai, name='all_chai'),

]