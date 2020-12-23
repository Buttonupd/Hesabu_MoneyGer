from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.contrib.auth.models import AbstractBaseUser
from django.contrib import messages



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label="Email Address", required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

        def clean_email(self):
            email = self.cleaned_data.get("email")
            if User.objects.filter(email=email).exists():
                print("email exists")
            return self.cleaned_data


class ProductForm(forms.ModelForm):
    class Meta:
        model = Project
        fields =['product', 'product_item', 'quantity', 'price', 'added_month', 'posted_by']

class SalesForm(forms.ModelForm):
    class Meta:
        model = MadeSale
        exclude =['project','juror', 'profile']

class MilkCollectionForm(forms.ModelForm):
    class Meta:
        model = MilkCollection
        fields = ['day_of_the_week', 'evening_litres', 'morning_litres','price_per_litre']