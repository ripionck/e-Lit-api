from django.urls import path, include
from .views import DepositView, PlaceOrderView, TransactionReport, CartView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('cart', CartView, basename='cart-api')

urlpatterns = [
    path('', include(router.urls)),
    path('deposit/', DepositView.as_view(), name='deposit-api'),
    path('place-order/', PlaceOrderView.as_view(), name='place-order-api'),
    path('transaction-report/', TransactionReport.as_view(),
         name='transaction-report-api'),
]
