from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from .filters import CampagneManagerStateFilter
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.test.client import RequestFactory
from django.contrib.sites.shortcuts import get_current_site
from django.db import transaction
import random
import string
from .models import UserProfile
from django.utils.translation import gettext_lazy as _

class UserProfileInline(admin.StackedInline):
    """
    Inline class for UserProfile model in the admin interface.

    Attributes:
        model: The model associated with the inline.
        can_delete: Boolean indicating whether the inline can be deleted or not.
        verbose_name_plural: Plural name displayed in the admin interface.
    """

    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Kampagnen-Manager-Status'

class CustomUserAdmin(UserAdmin):
    """
    Admin class for CustomUser model.

    Attributes:
        form: The form class associated with the admin class.
        add_form: The add form class associated with the admin class.
        inlines: The inline classes associated with the admin class.
        list_filter: The filters displayed in the list view.
        add_fieldsets: The fieldsets displayed when adding a new user.
        list_display: The fields displayed in the list view.
    """

    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    inlines = (UserProfileInline, )  
    list_filter = UserAdmin.list_filter + (CampagneManagerStateFilter,)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email'),  
        }),(_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                        'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display =  ('username', 'email', 'is_superuser', 'is_staff', 'get_is_campagne_manager',)

    def get_is_campagne_manager(self, obj):
        """
        Method to get the campagne manager status of the user.

        Args:
            obj: The CustomUser object.

        Returns:
            Boolean indicating whether the user is a campagne manager or not.
        """
        return obj.profile.is_campagne_manager

    get_is_campagne_manager.short_description = _('Kampagnen-Manager-Status')
    get_is_campagne_manager.boolean = True

    
    def generate_random_password(self, length=10):
        """
        Generates a random password of a given length.

        Args:
            length: The length of the password.

        Returns:
            A randomly generated password.
        """
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(length))

    def save_model(self, request, obj, form, change):
        """
        Saves the user model.

        Args:
            request: The request object.
            obj: The CustomUser object.
            form: The form associated with the object.
            change: Boolean indicating whether the object is being changed or not.
        """
        if not change:  # Means a new user is being created
            initial_password = self.generate_random_password(10)
            obj.set_password(initial_password)
            obj.is_active = True
            obj.save()

            # Now, trigger the password reset flow
            transaction.on_commit(lambda: self.send_password_reset_email(request, obj.email))
            
        else:
            super().save_model(request, obj, form, change)

   
    def send_password_reset_email(self, request, email):
        """
        Sends a password reset email to the user.

        Args:
        request: The request object.
        email: The email address of the user.
        """
        # Ensure the correct site is used based on the request
        current_site = get_current_site(request)
        protocol = 'https' if request.is_secure() else 'http'

        # Create a mock request if the original request lacks context
        if not hasattr(request, 'site'):
            factory = RequestFactory()
            mock_request = factory.get('/', HTTP_HOST=current_site.domain)
            mock_request.site = current_site
            mock_request.user = getattr(request, 'user', None)
            mock_request.is_secure = lambda: protocol == 'https'
        else:
            mock_request = request

        # Initialize the form with the provided email
        form = PasswordResetForm({'email': email})
        if form.is_valid():
            try:
                # Pass the mocked request with appropriate context
                form.save(
                    request=mock_request,
                    use_https=mock_request.is_secure(),
                    from_email='its.kompetent@uni-goettingen.de',
                    email_template_name='passwords/password_initial_creation_email.html',
                    html_email_template_name='passwords/password_initial_creation_email.html'
                )
                print("Password reset email sent.")
            except Exception as e:
                print(f"Error sending password reset email: {e}")
        else:
            print("Email not sent; form not valid.")



admin.site.unregister(User)
admin.site.register(UserProfile)
admin.site.register(User, CustomUserAdmin)
