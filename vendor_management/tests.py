from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import Vendor, PurchaseOrder

class VendorPerformanceTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='test@example.com',
            address='123 Test St',
            vendor_code='TEST001',
            on_time_delivery_rate=90,
            quality_rating_avg=4.5,
            average_response_time=2,
            fulfillment_rate=95
        )

    def test_vendor_performance_endpoint(self):
        url = reverse('vendor-performance', kwargs={'pk': self.vendor.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['on_time_delivery_rate'], self.vendor.on_time_delivery_rate)
        self.assertEqual(response.data['quality_rating_avg'], self.vendor.quality_rating_avg)
        self.assertEqual(response.data['average_response_time'], self.vendor.average_response_time)
        self.assertEqual(response.data['fulfillment_rate'], self.vendor.fulfillment_rate)

class AcknowledgePurchaseOrderTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.purchase_order = PurchaseOrder.objects.create(
            po_number='PO001',
            vendor=Vendor.objects.create(
                name='Test Vendor',
                contact_details='test@example.com',
                address='123 Test St',
                vendor_code='TEST001',
                on_time_delivery_rate=90,
                quality_rating_avg=4.5,
                average_response_time=2,
                fulfillment_rate=95
            ),
            delivery_date='2024-05-05T12:00:00Z',
            items=[{'name': 'Item 1', 'quantity': 5}],
            quantity=5,
            status='pending'
        )

    def test_acknowledge_purchase_order_endpoint(self):
        url = reverse('acknowledge-purchase-order', kwargs={'pk': self.purchase_order.pk})
        response = self.client.put(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.purchase_order.refresh_from_db()
        self.assertIsNotNone(self.purchase_order.acknowledgment_date)
