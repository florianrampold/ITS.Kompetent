from django.contrib import admin
from polymorphic.admin import (
   PolymorphicChildModelAdmin,
   PolymorphicParentModelAdmin,
)
from .models import *

class ImpulseAdmin(PolymorphicParentModelAdmin):
    base_model = Impulse
    child_models = (ImageImpulse, EmailImpulse, ChatImpulse)

class EmailImpulseAdmin(PolymorphicChildModelAdmin):
    """
    Admin class for EmailImpulse model.

    Attributes:
        base_model: The base model associated with the admin class.
        list_display: The table columns displayed in the list view.
    """

    base_model = EmailImpulse
    list_display = ("__str__", "impulse_text",)

class ImageImpulseAdmin(PolymorphicChildModelAdmin):
    """
    Admin class for ImageImpulse model.

    Attributes:
        base_model: The base model associated with the admin class.
        list_display: The table columns displayed in the list view.
    """

    base_model = ImageImpulse
    list_display = ("__str__", "impulse_text",)

class ChatImpulseAdmin(PolymorphicChildModelAdmin):
    """
    Admin class for ChatImpulse model.

    Attributes:
        base_model: The base model associated with the admin class.
        list_display: The table columns displayed in the list view.
    """

    base_model = ChatImpulse
    list_display = ("__str__", "impulse_text",)

class ImpulseItemAdmin(PolymorphicParentModelAdmin):
    """
    Admin class for Impulse model.

    Attributes:
        base_model: The base model associated with the admin class.
        child_models: The child models associated with the admin class.
    """

    base_model = Impulse
    child_models = (EmailImpulse, ImageImpulse, ChatImpulse)

class ImageItemAdmin(admin.ModelAdmin):
    """
    Admin class for ImageItem model.

    Attributes:
        list_display: The table columns displayed in the list view.
    """

    list_display = ("threat_situation", "impulse_number", "image_description")
    search_fields = ("threat_situation__threat_situation_identificator",)

class EmailItemAdmin(admin.ModelAdmin):
    """
    Admin class for EmailItem model.

    Attributes:
        list_display: The table columns displayed in the list view.
    """

    list_display = ("threat_situation", "impulse_number")
    search_fields = ("threat_situation__threat_situation_identificator",)

class ChatInterfaceAdmin(admin.ModelAdmin):
    """
    Admin class for ChatInterface model.

    Attributes:
        list_display: The table columns displayed in the list view.
    """

    list_display = ("threat_situation", "impulse_number")
    search_fields = ("threat_situation__threat_situation_identificator",)

class ChoiceItemAdmin(admin.ModelAdmin):
    """
    Admin class for ChoiceItem model.

    Attributes:
        list_display: The table columns displayed in the list view.
        search_fields: The fields included in the search functionality.
    """

    list_display = ("question", "option", "answer_rating")
    search_fields = ("question__threat_situation__threat_situation_identificator", "option",)

class QuestionItemAdmin(admin.ModelAdmin):
    """
    Admin class for QuestionItem model.

    Attributes:
        list_display: The table columns displayed in the list view.
        search_fields: The fields included in the search functionality.
    """

    list_display = ("__str__", "competence_dimension", "question", "type")
    search_fields = ("threat_situation__threat_situation_identificator", "question",)

class CompetenceDimensionAdmin(admin.ModelAdmin):
    """
    Admin class for CompetenceDimension model.

    Attributes:
        list_display: The table columns displayed in the list view.
    """

    list_display = ("dimension_name", "dimension_description")

class CompetenceTestItemAdmin(admin.ModelAdmin):
    """
    Admin class for CompetenceTestItem model.

    Attributes:
        list_display: The table columns displayed in the list view.
    """

    list_display = ('__str__', "threat_situation", "impulse_item", "competence_dimension")
    search_fields = ("threat_situation__threat_situation_identificator",)


admin.site.register(QuestionItem, QuestionItemAdmin)
admin.site.register(ChoiceItem, ChoiceItemAdmin)
admin.site.register(CompetenceDimension, CompetenceDimensionAdmin)
admin.site.register(CompetenceTestItem, CompetenceTestItemAdmin)
admin.site.register(ImageImpulse, ImageImpulseAdmin)
admin.site.register(CompetenceTest)
admin.site.register(EmailImpulse, EmailImpulseAdmin)
admin.site.register(ChatImpulse, ChatImpulseAdmin)
admin.site.register(EmailItem, EmailItemAdmin)
admin.site.register(ImageItem, ImageItemAdmin)
admin.site.register(ChatInterface, ChatInterfaceAdmin)





