
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class BaseSignUpForm(UserCreationForm):
    USER_TYPES = [
                    ('buyer', 'Buyer'),
                    ('seller', 'Seller'),
                    ('lawyer', 'Lawyer'),
                ]
    user_type = forms.ChoiceField(choices=USER_TYPES, widget=forms.HiddenInput())

class Meta(UserCreationForm.Meta):
    model = User
    fields = ('username', 'email', 'password1', 'password2', 'user_type')

class BuyerSignUpForm(BaseSignUpForm):
    phone_number = forms.CharField(max_length=15)
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_type'].initial = 'buyer'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'buyer'
        if commit:
            user.save()
        return user

class SellerSignUpForm(BaseSignUpForm):
    phone_number = forms.CharField(max_length=15)
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    address = forms.CharField(max_length=255, required=False)
    company_name = forms.CharField(max_length=100, required=False)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_type'].initial = 'seller'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'seller'
        if commit:
            user.save()
        return user

class LawyerSignUpForm(BaseSignUpForm):
    phone_number = forms.CharField(max_length=15)
    country = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    bar_association_id = forms.CharField(max_length=50)
    license_number = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_type'].initial = 'lawyer'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'lawyer'
        if commit:
            user.save()
        return user
