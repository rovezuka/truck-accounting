from django.urls import path
from . import views

urlpatterns = [
    path('', views.truck_list, name='truck_list'),
]