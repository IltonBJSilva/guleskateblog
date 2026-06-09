from django.contrib import admin
from .models import Mod


@admin.register(Mod)
class ModAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "minecraft_version",
        "created_at",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }