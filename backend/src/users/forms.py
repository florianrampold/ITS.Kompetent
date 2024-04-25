from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from .models import UserProfile


class CustomUserCreationForm(forms.ModelForm):
    """
    Form class for creating a custom user.

    Attributes:
        is_campagne_manager: Boolean field indicating whether the user is a campagne manager or not.
        email: Email field for the user's email address.
    """

    is_campagne_manager = forms.BooleanField(required=False, initial=False)
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    
    class Meta(UserCreationForm.Meta):
        """
        Meta class for the form.

        Attributes:
            model: The user model associated with the form.
            labels: Custom labels for form fields.
            fields: Fields to be included in the form.
        """

        model = User
        labels = {
            'username': 'Benutzername',
            'email': 'Email-Adresse'
        }
        fields = UserCreationForm.Meta.fields

    def save(self, commit=True):
        """
        Saves the user and its associated profile.

        Args:
            commit: Boolean indicating whether to save the user to the database.

        Returns:
            The saved user object.
        """
        user = super().save(commit=False)
        if commit:
            user.save()
            UserProfile.objects.get_or_create(
                user=user,
                defaults={'is_campagne_manager': self.cleaned_data['is_campagne_manager']},
            )
        return user

    def clean_email(self):
        """
        Validates the uniqueness of the email field.

        Raises:
            ValidationError: If the email is already associated with another account.
        """
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Dieser E-Mail-Adresse ist schon einem Account zugeordnet.')
        return email

class CustomUserChangeForm(UserChangeForm):
    """
    Form class for changing a custom user.

    Attributes:
        model: The user model associated with the form.
        fields: All fields from the associated model.
    """

    class Meta(UserChangeForm.Meta):
        """
        Meta class for the form.

        Attributes:
            model: The user model associated with the form.
            fields: All fields from the associated model.
        """

        model = User
        fields = '__all__'

    def clean_email(self):
        """
        Validates the uniqueness of the email field.

        Raises:
            ValidationError: If the email is already associated with another account.
        """
        email = self.cleaned_data.get('email')
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
                raise ValidationError('Dieser E-Mail-Adresse ist schon einem Account zugeordnet.')
        return email