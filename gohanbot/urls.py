from django.urls import path
from gohanbot import views

urlpatterns = [
    path('', views.top,  name='shop_list'),
    path('lottery', views.lottery, name='lottery')
]