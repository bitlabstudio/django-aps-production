"""Admin classes for the aps_production app."""
from django.contrib import admin

from . import models


class ErrorAdmin(admin.ModelAdmin):
    """Custom admin for the ``Error`` model."""
    list_display = ('order_run', 'error_bin', 'quantity', 'comment')


class ErrorBinAdmin(admin.ModelAdmin):
    """Custom admin for the ``ErrorBin`` model."""
    list_display = ('technology', 'error_code')


class OrderAdmin(admin.ModelAdmin):
    """Custom admin for the ``Order`` model."""
    list_display = ('order_number', 'company', 'date_created',
                    'customer_po_number', 'customer_po_date')


class OrderLineAdmin(admin.ModelAdmin):
    """Custom admin for the ``OrderLine`` model."""
    list_display = ('order', 'line_no', 'product', 'quantity_ordered',
                    'date_requested')


class OrderRunAdmin(admin.ModelAdmin):
    """Custom admin for the ```` model."""
    list_display = ('order_line', 'run_number', 'parent', 'ipn',
                    'quantity_started', 'quantity_dest_out', 'quantity_out',
                    'is_open', 'comment')
    list_filter = ['is_open']


class ShipmentAdmin(admin.ModelAdmin):
    """Custom admin for the ``Shipment`` model."""
    list_display = ('order_run', 'quantity', 'date_shipped')


admin.site.register(models.Error, ErrorAdmin)
admin.site.register(models.ErrorBin, ErrorBinAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderLine, OrderLineAdmin)
admin.site.register(models.OrderRun, OrderRunAdmin)
admin.site.register(models.Shipment, ShipmentAdmin)
