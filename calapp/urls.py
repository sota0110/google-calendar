from django.urls import path
from . import views

app_name = 'calapp'
urlpatterns = [
    path('', views.index, name='index')
]