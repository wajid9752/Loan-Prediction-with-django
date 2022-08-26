from django.urls import path 
from .views import *
urlpatterns = [

        path('' , home , name="home"),
        path('prediction' , prediction_view , name="prediction")
]
