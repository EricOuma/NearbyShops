from django.contrib import admin
# Since the Shop model includes a GeoDjango field, you need to use the special OSMGeoAdmin
from django.contrib.gis.admin import OSMGeoAdmin

from shops.models import Shop


"""decorated class is a representation of the Shop model in the admin interface and allows customizing different aspects such as the Shop fields that you want to display. In your case, it’s the name and location."""
@admin.register(Shop)
class ShopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')