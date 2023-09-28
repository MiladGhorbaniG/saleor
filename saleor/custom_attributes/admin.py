from django.contrib import admin
from .models import CustomAttribute

class CustomAttributeAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "input_type", "entity_type", "unit"]
    search_fields = ["name", "slug"]
    prepopulated_fields = {"slug": ["name"]}

admin.site.register(CustomAttribute, CustomAttributeAdmin)