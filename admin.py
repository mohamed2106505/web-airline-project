from django.contrib import admin
from .models import restaurant


class RestaurantAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name']}),
        (None,               {'fields': ['address']}),
        (None,               {'fields': ['latitude']}),
        (None,               {'fields': ['longitude']})
    ]
    list_display = ('name', 'address', 'latitude', 'longitude')
admin.site.register(Restaurant, RestaurantAdmin)
# Register your models here.
