import random

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View

from .forms import FoodShopForm
from .models import FoodKind, FoodShop


def top(request):
    shops = FoodShop.objects.all()
    context = {"shops": shops}
    return render(request, "gohanbot/top.html", context)


class FoodShopCreateView(LoginRequiredMixin, View):
    form_class = FoodShopForm
    template_name = "gohanbot/shop_register.html"
    food_kind = FoodKind.objects.all()

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {"form": form, "food_kinds": self.food_kind},
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            food_shop = form.save(commit=False)
            food_shop.created_by = request.user
            food_shop.save()
            messages.add_message(request, messages.SUCCESS, "おみせのとうろくにせいこうしたよ！")
            return redirect("/", self.template_name)
        messages.add_message(request, messages.ERROR, "おみせのとうろくにしっぱいしちゃった")
        return render(
            request,
            self.template_name,
            {"form": form, "food_kinds": self.food_kind},
        )


def lottery(request):
    template_name = "gohanbot/lottery.html"
    shops = FoodShop.objects.all()
    if len(shops) == 0:
        messages.add_message(request, messages.ERROR, 'お店が登録されていないよ。')
        return redirect('/', template_name)
    amount_shops = len(shops)
    random_number = random.randint(1, amount_shops)
    shop = FoodShop.objects.get(pk=random_number)
    context = {"shop": shop}
    return render(request, template_name, context)
