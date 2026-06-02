from django.contrib import admin

from .models import ParkingSpot


@admin.register(ParkingSpot)
class ParkingSpotAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'number',
        'zone',
        'address',
        'spot_type',
        'status',
        'updated_at',
    )
    list_filter = (
        'status',
        'spot_type',
        'zone',
    )
    search_fields = (
        'number',
        'zone',
        'address',
    )
    readonly_fields = (
        'updated_at',
    )