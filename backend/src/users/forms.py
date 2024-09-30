
from .models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    """
    Creation Form for custom users.

    Attributes:
        is_campagne_manager: A booealn field that determines if the new user is a campagne manager.
    """
    is_campagne_manager = forms.BooleanField(required=False, initial=False)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "is_campagne_manager") 

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.update_or_create(
                user=user,
                defaults={'is_campagne_manager': self.cleaned_data['is_campagne_manager']}
            )
        return user


class CustomUserChangeForm(UserChangeForm):
    """
    Change Form for custom users.

    Attributes:
        is_campagne_manager: A booealn field that determines if the new user is a campagne manager.
    """
    is_campagne_manager = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = '__all__'

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.update_or_create(
                user=user,
                defaults={'is_campagne_manager': self.cleaned_data['is_campagne_manager']}
            )
        return user
