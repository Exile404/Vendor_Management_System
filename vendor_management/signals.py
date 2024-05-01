from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import PurchaseOrder
from .performance import calculate_vendor_performance
from django.db import models

@receiver(post_save, sender=PurchaseOrder)
@receiver(post_delete, sender=PurchaseOrder)
def update_vendor_performance(sender, instance, **kwargs):
    calculate_vendor_performance(instance.vendor)

# vendor_management/apps.py
from django.apps import AppConfig

class VendorManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendor_management'

    def ready(self):
        import vendor_management.signals
