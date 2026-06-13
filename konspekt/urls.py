from django.urls import path

from . import views

app_name = 'konspekt'
urlpatterns = [
    # Головна сторінка
    path('', views.index, name='index'),
    # Сторінка зі списком усіх тем
    path('topics/', views.topics, name='topics'),
    # Сторінка з інформацією за окремою темою
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Сторінка для додавання нової теми
    path('new_topic/', views.new_topic, name='new_topic'),
    # Сторінка для довання нової нотатки
    path('new_note/<int:topic_id>/', views.new_note, name='new_note'),
    # Сторінка для редагування нотатки
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
]
