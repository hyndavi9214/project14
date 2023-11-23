from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('fruits/',fruits,name='fruits'),
    path('flowers/',flowers,name='flowers'),
]