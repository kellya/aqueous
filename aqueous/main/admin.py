from django.contrib import admin
from main.models import (
    Type,
    Manufacturer,
    Tank,
)


class TypeAdmin(admin.ModelAdmin):
    pass


class TankAdmin(admin.ModelAdmin):
    pass

class ManufacturerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tank, TankAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
