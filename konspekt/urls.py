from django.urls import path

from . import views

app_name = 'konspekt'
urlpatterns = [
    # Головна сторінка
    path('', views.index, name='index'),
]
