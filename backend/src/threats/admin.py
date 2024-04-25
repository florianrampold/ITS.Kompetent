from django.contrib import admin

from .models import ThreatArea
from .models import ThreatVector
from .models import ThreatEvent
from .models import ThreatSituation
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ThreatEventResource(resources.ModelResource):
    """
    Resource class to import threat events into Threat Event model.

    """
    class Meta:
        model = ThreatEvent

class ThreatEventAdmin(ImportExportModelAdmin):
    """
    Admin class for ThreatEvent model.

    Attributes:
        list_display: The table columns displayed in the list view.
    """
    resource_class = ThreatEventResource
    list_display = ("id", "event_name", "event_description")


class ThreatAreaAdmin(admin.ModelAdmin):
    """
    Admin class for ThreatArea model.

    Attributes:
        list_display: The table columns displayed in the list view.
    """
    list_display = ("area_name", "area_description") # display these table columns in the list view



class ThreatVectorAdmin(admin.ModelAdmin):
    """
    Admin class for ThreatVector model.

    Attributes:
        list_display: The table columns displayed in the list view.
    """
    list_display = ("threat_area", "threat_event")

class ThreatSituationAdmin(admin.ModelAdmin):
    """
    Admin class for ThreatSituation model.

    Attributes:
        list_display: The table columns displayed in the list view.
    """
    list_display = ("threat_situation_identificator", "threat_description", "threat_vector", "job_profile")
    list_filter = ['job_profile__job_name', 'threat_vector']
    search_fields = ("job_profile__job_name",)


# Register your models here.

admin.site.register(ThreatArea, ThreatAreaAdmin)
admin.site.register(ThreatVector, ThreatVectorAdmin)
admin.site.register(ThreatEvent, ThreatEventAdmin)
admin.site.register(ThreatSituation, ThreatSituationAdmin)


