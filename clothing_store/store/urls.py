from django.urls import path
from . import views  # Импортируем представления из файла views.py

urlpatterns = [
    path('', views.preferences, name='preferences'),  # Главная страница приложения
]