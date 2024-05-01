from django.urls import path
from . import views

urlpatterns = [
    path('api/vendors', views.VendorListCreate.as_view()),
    path('api/vendors/<int:pk>', views.VendorRetrieveUpdateDestroy.as_view()),
    path('api/vendors/<int:pk>/performance', views.VendorPerformance.as_view(), name='vendor-performance'),
    path('api/purchase_orders', views.PurchaseOrderListCreate.as_view()),
    path('api/purchase_orders/<int:pk>', views.PurchaseOrderRetrieveUpdateDestroy.as_view()),
    path('api/purchase_orders/<int:pk>/acknowledge', views.AcknowledgePurchaseOrder.as_view(),name='acknowledge-purchase-order'),
]
