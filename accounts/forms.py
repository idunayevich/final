from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(label='Email')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(UserChangeForm):
    password = None  # ocultar campo password
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'avatar', 'bio', 'birth_date')