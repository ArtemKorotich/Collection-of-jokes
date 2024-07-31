from django.shortcuts import render, get_object_or_404
from jokes.models import Content, Theme
from django.contrib.auth.decorators import login_required

def index(request):
    contents = Content.objects.all().order_by('-rating')[:10]
    return render(request, 'main/index.html', {'contents': contents})

def theme_list(request):
    themes = Theme.objects.all()
    return render(request, 'main/theme_list.html', {'themes': themes})

def theme_detail(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id)
    contents = Content.objects.filter(theme=theme).order_by('-rating')
    return render(request, 'main/theme_detail.html', {'theme': theme, 'contents': contents})

@login_required
def favorite_list(request):
    favorites = Content.objects.filter(favorite__user=request.user)
    return render(request, 'main/favorite_list.html', {'favorites': favorites})

def user_jokes_list(request):
    jokes = Content.objects.filter(content_type='joke').order_by('-id')
    return render(request, 'main/user_jokes_list.html', {'jokes': jokes})