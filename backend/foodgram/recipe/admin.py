from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class Admin(admin.ModelAdmin):
    pass