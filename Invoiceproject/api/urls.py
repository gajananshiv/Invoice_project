from django.contrib import admin
from django.urls import path,include
from api.views import InvoiceViewSet,InvoiceDetailViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'invoice',InvoiceViewSet)
router.register(r'invoicedetail',InvoiceDetailViewSet)

urlpatterns=[
    path('',include(router.urls))
]