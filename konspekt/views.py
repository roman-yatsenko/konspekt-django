from django.shortcuts import render, redirect
from flet import context

from .forms import TopicForm, NoteForm
from .models import Topic, Note

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

def new_topic(request):
    """Додає нову тему"""
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('konspekt:topics')

    context = {'form': form}
    return render(request, 'konspekt/new_topic.html', context)

def new_note(request, topic_id):
    """Додає новий допис до певної теми"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = NoteForm()
    else:
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.topic = topic
            new_note.save()
            return redirect('konspekt:topic', topic_id=topic_id)

    context = {
        'topic': topic,
        'form': form
    }
    return render(request, 'konspekt/new_note.html', context)

def edit_note(request, note_id):
    """Редагує існуючу нотатку"""
    note = Note.objects.get(id=note_id)
    topic = note.topic

    if request.method != 'POST':
        form = NoteForm(instance=note)
    else:
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('konspekt:topic', topic_id=topic.id)

    context = {
        'note': note,
        'topic': topic,
        'form': form
    }
    return render(request, 'konspekt/edit_note.html', context)
