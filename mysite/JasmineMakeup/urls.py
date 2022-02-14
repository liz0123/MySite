from django.urls import path

from . import views

app_name = "JasmineMakeup"

urlpatterns = [
    path('', views.index, name='index'),
]