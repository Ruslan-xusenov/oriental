from django.contrib import admin
from .models import Country, Institution, ContactMessage, News


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ("name","country","created_at")
    list_filter = ("country",)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name","email","created_at")

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title", "content")
    list_filter = ("created_at",)