import random

from django.shortcuts import render
from gohanbot.models import FoodShop


# Create your views here.
def top(request):
    shops = FoodShop.objects.all()
    context = {"shops": shops}
    return render(request, 'gohanbot/top.html', context)


def lottery(request):
    shops = FoodShop.objects.all()
    amount_shops = len(shops)
    random_number = random.randint(1, amount_shops)
    shop = FoodShop.objects.get(pk=random_number)
    context = {'shop': shop}
    return render(request, 'gohanbot/lottery.html', context)
