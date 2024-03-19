from django.urls import path
from .views import select_station,shortest_path
urlpatterns=[
    path('',select_station,name='select_station'),
    path('shortest_path/',shortest_path,name='shortest_path')
]