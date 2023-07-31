from django.urls import path
from app2.views import *

urlpatterns =[
    path('family1/',family1,name='family1'),
    path('nature/',nature,name='nature'),
]