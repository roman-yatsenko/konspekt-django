from django.shortcuts import render

def index(request):
    """Головна сторінка застосунку"""
    return render(request, 'konspekt/index.html')
