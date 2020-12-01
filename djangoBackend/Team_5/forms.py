from django import forms
from django.contrib.auth.models import User
import django.contrib.auth.models as models
from django.forms import ModelForm
from .models import CustomUser, Listing
import uuid
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


class ListingForm(ModelForm):

    class Meta:
        model = Listing
        fields = ('user', 'title', 'address1', 'address2', 'description', 'zipcode', 'category',
                  'bedrooms', 'bathrooms', 'price', 'photo_main', 'photo_1', 'photo_2',
                  'state', 'city', 'year', 'photo_3', 'photo_4', 'photo_5', 'photo_6', 'listing_type')

    def save(self, commit=True):
        
        listing = super(ListingForm, self).save(commit=False)
        listing.user = self.cleaned_data['user']
        listing.title = self.cleaned_data["title"]
        listing.address1 = self.cleaned_data['address1']
        listing.address2 = self.cleaned_data['address2']
        listing.zipcode = self.cleaned_data['zipcode']
        listing.category = self.cleaned_data['category']
        listing.bedrooms = self.cleaned_data['bedrooms']
        listing.bathrooms = self.cleaned_data['bathrooms']
        listing.price = self.cleaned_data['price']
        listing.year = self.cleaned_data['year']
        listing.city = self.cleaned_data['city']
        listing.state = self.cleaned_data['state']
        listing.listing_type = self.cleaned_data['listing_type']
        if commit:
            listing.save()

        return listing

