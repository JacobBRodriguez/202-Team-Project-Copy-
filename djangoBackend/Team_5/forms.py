from django import forms
from django.contrib.auth.models import User
import django.contrib.auth.models as models
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name',
                  'last_name', 'email',
                  'password1', 'password2',
                  'groups', 'is_active',
                  )

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password1']
        user.set_password(user.password)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user_type = self.cleaned_data['groups']
        user.is_active = self.cleaned_data['is_active']
        user.is_active = True

        if commit:
            user.save()

        return user


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name',
                  'last_name', 'email',
                  'password1', 'password2',
                  'user_type', 'is_active',
                  )

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.password = self.cleaned_data['password1']
        user.set_password(user.password)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.user_type = self.cleaned_data['user_type']
        user.is_active = True

        if commit:
            user.save()

        return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

