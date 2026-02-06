from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django_recaptcha.fields import ReCaptchaField

from django.utils.translation import gettext_lazy as _

class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField()
    username = forms.CharField(label=_("Username"))
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    captcha = ReCaptchaField()
    email = forms.EmailField(required=True, label=_("Email"))
    phone = forms.CharField(required=False, label=_("Phone"))
    address = forms.CharField(required=False, label=_("Address"))

    field_order = ['username', 'email', 'phone', 'address', 'password1', 'password2', 'captcha']

    class Meta:
        model = User
        fields = ("username", "email",)
        labels = {
            'username': _('User Name'),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("This email is already registered"))
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Save extra profile data
            if hasattr(user, 'profile'):
                user.profile.phone = self.cleaned_data.get('phone', '')
                user.profile.address = self.cleaned_data.get('address', '')
                user.profile.save()
        return user

class CouponApplyForm(forms.Form):
    code = forms.CharField(label='Coupon', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Coupon Code'}))

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'email': _('Email'),
        }

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'address']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'phone': _('Phone'),
            'address': _('Address'),
        }
