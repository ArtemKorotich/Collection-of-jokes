from django.urls import path
from . import views

app_name = 'jokes'

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('add/', views.add_content, name='add_content'),  # Страница для добавления контента
    path('<int:joke_id>/', views.detail, name='detail'),  # Детальная страница анекдота
]