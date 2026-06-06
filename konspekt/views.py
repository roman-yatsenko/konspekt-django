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
