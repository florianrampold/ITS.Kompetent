from django.contrib import admin
from django.utils.translation import gettext_lazy as _

class CampagneManagerStateFilter(admin.SimpleListFilter):
    title = _('Kampagnen-Manager-Status') 
    parameter_name = 'is_campagne_manager'  

    def lookups(self, request, model_admin):
        """
        Returns a list of tuples. The first element in each tuple is the coded value
        for the option that will appear in the URL query. The second element is the
        human-readable name for the option that will appear in the right sidebar.
        """
        return (
            ('yes', _('Ja')),
            ('no', _('Nein')),
        )

    def queryset(self, request, queryset):
        """
        Returns the filtered queryset based on the value provided in the query string
        and retrievable via `self.value()`.
        """
        if self.value() == 'yes':
            return queryset.filter(profile__is_campagne_manager=True)
        if self.value() == 'no':
            return queryset.filter(profile__is_campagne_manager=False)
