from django.urls import path
from apps.gohanbot import views

urlpatterns = [
    path('lottery', views.lottery, name='lottery')
]