from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cablist/<source>/<destination>', views.cablist, name='cablist'),
]
