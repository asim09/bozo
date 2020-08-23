from django.urls import path
from . import views

urlpatterns = [
    path('outstation_price/', views.outstation_price, name='outstation_price'),
]
