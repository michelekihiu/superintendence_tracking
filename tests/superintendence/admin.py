from __future__ import unicode_literals

from django.contrib import admin

from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin

from .models import Shipment


class ShipmentResource(ModelResource):

    class Meta:
        model = Shipment


    def for_delete(self, row, instance):
        return self.fields['id'].clean(row) == ''


class ShipmentAdmin(ImportExportMixin, admin.ModelAdmin):
    def set_container_charges_inspection_stripping(modelAdmin, request, queryset):
        for shipment in queryset:
            if shipment.bl_teu > 0:
                shipment.sgs_amount = shipment.bl_teu * 38
            elif shipment.bl_feu > 0:
                shipment.sgs_amount = shipment.fl_feu * 38
            shipment.save()

    def set_container_charges_inspection(modelAdmin, request, queryset):
        for shipment in queryset:
            if shipment.bl_teu > 0:
                shipment.sgs_amount = shipment.bl_teu * 16
            elif shipment.bl_feu > 0:
                shipment.sgs_amount = shipment.fl_feu * 16
            shipment.save()

    list_display = ['vessel', 'ata_eta_mom', 'bl_number', 'ocean_del_terms', 'bl_teu', 'bl_feu', 'cf_agent', 'tonnage', 'ex_si_number_po_number', 'commodity', 'pack', 'recipient_country', 'project_type', 'sgs_amount', 'po_number', 'ses_number' ]
    list_filter = [ 'ata_eta_mom', 'cf_agent', 'ocean_del_terms' ]
    search_fields = ['vessel']
    list_per_page = 5
    resource_class = ShipmentResource
    actions = [set_container_charges_inspection_stripping, set_container_charges_inspection,]

    set_container_charges_inspection_stripping.short_description = 'Container charges - inspection + stripping'
    set_container_charges_inspection.short_description = 'Container charges - inspection'


admin.site.register(Shipment, ShipmentAdmin)

admin.site.site_header = 'Superintendents Tracking'
