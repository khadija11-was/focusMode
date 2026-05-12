from django.urls import path
from . import views

urlpatterns = [
    path('', views.pomodoro_list),
    path('add/', views.add_pomodoro),
]