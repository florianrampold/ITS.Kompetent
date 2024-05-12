from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import UserProfile
from django.utils.translation import gettext_lazy as _

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Kampagnen-Manager-Status'

class CustomUserAdmin(UserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    inlines = (UserProfileInline,)
    list_display = ('username', 'is_superuser', 'is_staff', 'get_is_campagne_manager')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    def get_is_campagne_manager(self, obj):
        return obj.profile.is_campagne_manager

    get_is_campagne_manager.short_description = _('Kampagnen-Manager-Status')
    get_is_campagne_manager.boolean = True

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
