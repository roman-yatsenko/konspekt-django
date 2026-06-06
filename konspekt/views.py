from django.shortcuts import render

from .models import Topic

def index(request):
    """Головна сторінка застосунку"""
    return render(request, 'konspekt/index.html')

def topics(request):
    """Ввиоде список тем"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'konspekt/topics.html', context)

def topic(request, topic_id):
    """Виводе одну тему і всі її нотатки"""
    topic = Topic.objects.get(id=topic_id)
    notes = topic.note_set.order_by('-date_added')
    context = {'topic': topic, 'notes': notes}
    return render(request, 'konspekt/topic.html', context)
