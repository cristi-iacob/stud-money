from django import forms
from django.contrib.auth.forms import UserCreationForm
from app.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    name = forms.CharField(max_length=100, required=True)
    birthdate = forms.CharField(max_length=100, required=True, help_text='dd/mm/yyyy')

    class Meta:
        model = User
        fields = ('username', 'name', 'birthdate', 'email', 'password1', 'password2', )