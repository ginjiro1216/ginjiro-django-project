from django import forms

from .models import FoodShop


class FoodShopForm(forms.ModelForm):
    class Meta:
        model = FoodShop
        fields = ("shop", "food_kind", "description")
