from django.shortcuts import render, get_object_or_404, redirect
from .models import Content
from .forms import ContentForm
def index(request):
    jokes = Content.objects.filter(content_type='joke')
    context = {'jokes': jokes}
    return render(request, 'jokes/index.html', context)

def detail(request, joke_id):
    joke = get_object_or_404(Content, pk=joke_id)
    return render(request, 'jokes/detail.html', {'joke': joke})

def add_content(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('content_list')  # Используем redirect
    else:
        form = ContentForm()
    return render(request, 'add_content.html', {'form': form})

def content_list(request):
    contents = Content.objects.all()
    return render(request, 'content_list.html', {'contents': contents})