from django.urls import path
from app1.views import *

urlpatterns =[
    path('family/',family,name='family'),
    path('hobbies/',hobbies,name='hobbies'),

]