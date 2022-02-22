from django.urls import path
from apps.gohanbot import views

urlpatterns = [
    path('lottery', views.lottery, name='lottery'),
    path('register', views.FoodShopCreateView.as_view(), name='shop_register')
]
