from django.db import models


def calculate_vendor_performance(vendor):
    completed_orders = vendor.purchaseorder_set.filter(status='completed')
    total_orders = vendor.purchaseorder_set.all()

    if total_orders.count() == 0:
        vendor.fulfillment_rate = 0
    else:
        vendor.fulfillment_rate = (completed_orders.count() / total_orders.count()) * 100

    if completed_orders.filter(quality_rating__isnull=False).exists():
        vendor.quality_rating_avg = completed_orders.filter(quality_rating__isnull=False).aggregate(avg_rating=models.Avg('quality_rating'))['avg_rating']
    else:
        vendor.quality_rating_avg = 0

    if completed_orders.filter(acknowledgment_date__isnull=False).exists():
        avg_response_time = completed_orders.filter(acknowledgment_date__isnull=False).aggregate(avg_time=models.Avg(models.F('acknowledgment_date') - models.F('issue_date')))['avg_time']
        vendor.average_response_time = avg_response_time.total_seconds() / 3600 # Convert to hours
    else:
        vendor.average_response_time = 0

    if completed_orders.filter(delivery_date__lte=models.F('delivery_date')).exists():
        vendor.on_time_delivery_rate = (completed_orders.filter(delivery_date__lte=models.F('delivery_date')).count() / completed_orders.count()) * 100
    else:
        vendor.on_time_delivery_rate = 0

    vendor.save()