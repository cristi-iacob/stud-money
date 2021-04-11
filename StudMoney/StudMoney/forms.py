from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from app.models import User, LocationEnum, Task


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    name = forms.CharField(max_length=100, required=True)
    birthdate = forms.CharField(max_length=100, required=True, help_text='dd/mm/yyyy')

    class Meta:
        model = User
        fields = ('username', 'name', 'birthdate', 'email', 'password1', 'password2', )


class AddTaskForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True)
    starttime = forms.DateTimeField(help_text="yyyy/MM/dd hh:mm:ss", required=True)
    location = models.CharField(max_length=2, choices=LocationEnum)
    description = forms.CharField(max_length=400, required=True)
    reward = forms.FloatField(required=True)

    class Meta:
        model = Task
        fields = ('name', 'starttime', 'location', 'description', 'reward')
