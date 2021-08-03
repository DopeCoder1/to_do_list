from django.urls import path
from .views import *
urlpatterns = [
    path('', home_list, name="list"),
    path('update_task/<str:pk>/', UpdateList, name="update_task"),
    path('delete/<str:pk>/', DeleteList, name="delete"),
]