from django.urls import path
from gohanbot import views

urlpatterns = [
    path('lottery', views.lottery, name='lottery')
]