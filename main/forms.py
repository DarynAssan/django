from django import forms
from .models import Commentary, Tapsyrys


class Con(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ("name", "email", "text")


class Tapy(forms.ModelForm):
    class Meta:
        model = Tapsyrys
        fields = ("name", "number", "adres")