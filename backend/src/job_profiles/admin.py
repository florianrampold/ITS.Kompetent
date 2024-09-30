from django.contrib import admin

from .models import JobProfile


class JobProfileAdmin(admin.ModelAdmin):
    """
    Admin class for JobProfile model.

    Attributes:
        list_display: The table columns displayed in the list view.
    """
    list_display = ("id", "job_name", "job_description")


admin.site.register(JobProfile, JobProfileAdmin)
