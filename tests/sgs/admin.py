from __future__ import unicode_literals

from django.contrib import admin

from import_export.resources import ModelResource
from import_export.admin import ImportExportMixin, ImportMixin, ExportActionModelAdmin

#from .models import Book, Category, Author, Child

from .models import Shipment


#class ChildAdmin(ImportMixin, admin.ModelAdmin):
    #pass


class ShipmentResource(ModelResource):

    class Meta:
        model = Shipment

    def for_delete(self, row, instance):
        return self.fields['id'].clean(row) == ''


class ShipmentAdmin(ImportExportMixin, admin.ModelAdmin):
    #list_filter = ['categories', 'author']
    list_display = ['vessel', 'ata_eta_mom', 'bl_number', 'ocean_del_terms', 'bl_teu', 'bl_feu', 'cf_agent', 'qty_disch_loaded', 'ex_si_number_po_number', 'commodity', 'pack', 'recipient_country', 'project_type', 'sgs_amount' ]
    list_filter = [ 'ata_eta_mom', 'cf_agent', 'ocean_del_terms' ]
    resource_class = ShipmentResource


#class CategoryAdmin(ExportActionModelAdmin):
    #pass


#class AuthorAdmin(ImportMixin, admin.ModelAdmin):
    #pass

admin.site.register(Shipment, ShipmentAdmin)
#admin.site.register(Category, CategoryAdmin)
#admin.site.register(Author, AuthorAdmin)
#admin.site.register(Child, ChildAdmin)

admin.site.site_header = 'SGS Shipments'
