from django.urls import path

from . import views

app_name ="profolio"

urlpatterns =[
    path('',views.index, name="index")
]