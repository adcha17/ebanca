#encoding: utf-8

from django import forms
from core.models import Client


class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = '__all__'


class SignInForm(forms.Form):

    num_card = forms.IntegerField(label='Número de tarjeta')
    num_pin = forms.IntegerField(label='PIN', widget=forms.PasswordInput, min_value=1000, max_value=9999)
