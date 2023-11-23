from generic.views import *
from django.urls import path
app_name='generic'
urlpatterns=[
    path('vegetables/',vegetables,name='vegetables'),
]