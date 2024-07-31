from django.urls import path
from . import views

app_name = 'jokes'

urlpatterns = [
    path('', views.index, name='index'),  # Пример маршрута для главной страницы приложения jokes
    path('<int:joke_id>/', views.detail, name='detail'),  # Пример маршрута для детальной страницы анекдота
]