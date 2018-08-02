from django import forms
from django.contrib.auth.forms import UserCreationForm
from authenticator.models import *


class SigningUping (UserCreationForm):
    email = forms.EmailField(max_length=250, help_text='Required. Please put a valid email address.')

    class Meta:
        model = AuthUser
        fields = ('email', 'password1', 'password2',)