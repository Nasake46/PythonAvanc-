from django.contrib import admin
from wilfridapp.models import Website
from wilfridapp.models import CheckWebsite

# admin.site.register(Website)
# admin.site.register(CheckWebsite)

@admin.register(Website)
class WebsiteAdmin(admin.ModelAdmin):
    list_display = ("host", "is_up", "last_check")
    list_filter = ("host", "is_up", "last_check")
    search_fields = ("host", "is_up", "last_check")


@admin.register(CheckWebsite)
class CheckAdmin(admin.ModelAdmin):
    list_display = ("website", "date", "is_up", "message")
    list_filter = ("website", "date", "is_up", "message")
    search_fields = ("website", "date", "is_up", "message")
