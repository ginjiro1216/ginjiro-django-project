from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        help_text="とうこうしゃのおなまえにつかわれるよ",
        label="とうこうしゃ",
    )
    password1 = forms.CharField(
        help_text="ぱすわーどをにゅうりょくしてね", label="ぱすわーど", widget=forms.PasswordInput
    )

    password2 = forms.CharField(
        help_text="ぱすわーどがまちがっていないかかくにんしてね",
        label="ぱすわーど(かくにん)",
        widget=forms.PasswordInput,
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")
