from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
class UserProfile(models.Model):
    """
    Represents a model to store the user profile whic extends the native user model. This model is used to assign campagne manager state to users.

    Attributes:
        user (OneToOneField): The user assigned to the user profile
        is_campagne_manager (BooleanField): A boolean (yes or no) that determines whether the user can log in into the campagne management portal
       

    Returns:
        (str): The username for the admin interface
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name="Benutzername")
    is_campagne_manager = models.BooleanField(default=False, verbose_name="Kampagnen Manager Status")
    must_change_password = models.BooleanField(default=True, verbose_name="Passwort ändern erforderlich")


    class Meta:
        verbose_name = _('Kampagnen-Berechtigung') 
        verbose_name_plural = _('Kampagnen-Berechtigungen') 

    def __str__(self):
        return self.user.username



