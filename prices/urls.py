from django.urls import path
from . import views

urlpatterns = [
    path('outstation_price/',views.cab_models_create,name='cab_models_create'),
]
