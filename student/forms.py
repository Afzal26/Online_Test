
from django.contrib.auth.models import User
from django import forms
from . import models


class StudentUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
        widgets = {
            'password': forms.PasswordInput()
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = ['address', 'mobile']
