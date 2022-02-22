import random

from django.shortcuts import render, redirect
from django.views import View

from .forms import FoodShopForm
from .models import FoodShop, FoodKind


# Create your views here.
def top(request):
    shops = FoodShop.objects.all()
    context = {"shops": shops}
    return render(request, 'gohanbot/top.html', context)


# @method_decorator(decorator=login_required)
class FoodShopCreateView(View):
    form_class = FoodShopForm
    template_name = 'gohanbot/shop_register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            food_shop = form.save(commit=False)
            food_shop.created_by = request.user
            food_kind = FoodKind.objects.get(pk=2)
            food_shop.food_kind = food_kind
            food_shop.save()
            return redirect('/', self.template_name)
        return render(request, self.template_name, {'form', form})


def lottery(request):
    shops = FoodShop.objects.all()
    amount_shops = len(shops)
    random_number = random.randint(1, amount_shops)
    shop = FoodShop.objects.get(pk=random_number)
    context = {'shop': shop}
    return render(request, 'gohanbot/lottery.html', context)
