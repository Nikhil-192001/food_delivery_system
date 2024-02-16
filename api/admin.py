from django.contrib import admin
from .models import Organization,Item,Pricing
# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','type','description']

@admin.register(Pricing)
class PricingAdmin(admin.ModelAdmin):
    list_display = ['id','zone','base_distance_in_km','km_price','fix_price','organization_id','item_id']