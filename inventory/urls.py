
from django.urls import path
from . import views

urlpatterns = [
    path('cab/model/view/',views.cab_models_view,name='cab_models_view'),
    path('cab/model/create/',views.cab_models_create,name='cab_models_create'),

    path('vendor/view',views.vendor_view,name='vendor_view'),
    path('vendor/create/',views.vendor_create,name='vendor_create'),

    path('cab/view', views.cab_view, name='cab_view'),
    path('cab/create/', views.cab_create, name='cab_create'),
    path('cab/update/<int:id>', views.cab_update, name='cab_update'),

    # path('route/view', views.cab_view, name='cab_view'),
    path('route/create/', views.route_create, name='route_create'),
    # path('route/update/<str:id>', views.cab_update, name='cab_update'),

]
