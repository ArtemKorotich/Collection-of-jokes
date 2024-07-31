from django.shortcuts import render, get_object_or_404
from .models import Content

def index(request):
    jokes = Content.objects.filter(content_type='joke')
    context = {'jokes': jokes}
    return render(request, 'jokes/index.html', context)

def detail(request, joke_id):
    joke = get_object_or_404(Content, pk=joke_id)
    return render(request, 'jokes/detail.html', {'joke': joke})