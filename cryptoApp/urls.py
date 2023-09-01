# file handles routing in the application 

from django.urls import path
from . import views


urlpatterns = [
    path("home/",views.content),

    
]