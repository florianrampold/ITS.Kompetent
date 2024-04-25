from django.contrib import admin
from .models import Training
from .models import Language
from .models import TargetAudience
from .models import DeliveryMethod
from .models import TrainingGroup
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class TrainingResource(resources.ModelResource):
    """
    Resource class for Training model.

    Attributes:
        model: The model associated with the resource.
    """

    class Meta:
        model = Training

class TrainingAdmin(ImportExportModelAdmin):
    """
    Admin class for Training model.

    Attributes:
        resource_class: The resource class associated with the admin class.
    """

    resource_class = TrainingResource

class LanguageAdmin(admin.ModelAdmin):
    """
    Admin class for Language model.

    Attributes:
        list_display: The table columns displayed in the list view.
        search_fields: The fields included in the search functionality.
    """

    list_display = ("language",)
    search_fields = ("language",)

class TrainingGroupAdmin(admin.ModelAdmin):
    """
    Admin class for TrainingGroup model.

    Attributes:
        list_display: The table columns displayed in the list view.
        search_fields: The fields included in the search functionality.
    """

    list_display = ("identifier",)
    search_fields = ("identifier",)

class TargetAudienceAdmin(admin.ModelAdmin):
    """
    Admin class for TargetAudience model.

    Attributes:
        list_display: The table columns displayed in the list view.
        search_fields: The fields included in the search functionality.
    """

    list_display = ("audience_name",)
    search_fields = ("audience_name",)

class DeliveryMethodAdmin(admin.ModelAdmin):
    """
    Admin class for DeliveryMethod model.

    Attributes:
        list_display: The table columns displayed in the list view.
        search_fields: The fields included in the search functionality.
    """

    list_display = ("delivery_method",)
    search_fields = ("delivery_method",)


admin.site.register(Training, TrainingAdmin)
admin.site.register(TrainingGroup, TrainingGroupAdmin)
admin.site.register(TargetAudience, TargetAudienceAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(DeliveryMethod, DeliveryMethodAdmin)

