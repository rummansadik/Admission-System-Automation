from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from login_system.models import Profile


class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField()
    hsc_roll = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'hsc_roll']


class TeacherRegisterForm(UserCreationForm):
    email = forms.EmailField()
    employee_id = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'employee_id']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class TeacherUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
