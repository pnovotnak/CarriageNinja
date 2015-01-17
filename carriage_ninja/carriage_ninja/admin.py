from django.contrib.auth.models import User
from django.contrib import admin

from .models import DriversLicense, Trip

admin.site.unregister(User)


class DriversLicenseInline(admin.StackedInline):
    model = DriversLicense
    extra = 0
    min_num = 1


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [
        DriversLicenseInline,
    ]

admin.register(Trip)