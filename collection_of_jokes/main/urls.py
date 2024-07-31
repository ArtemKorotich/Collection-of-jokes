from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('themes/', views.theme_list, name='theme_list'),
    path('themes/<int:theme_id>/', views.theme_detail, name='theme_detail'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('jokes/', views.user_jokes_list, name='user_jokes_list'),  # Новый маршрут для списка анекдотов
]