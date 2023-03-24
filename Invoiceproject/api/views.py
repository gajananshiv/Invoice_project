from django.shortcuts import render
from rest_framework import viewsets
from api.models import Invoice,InvoiceDetail
from api.serializers import InvoiceSerializer,InvoiceDetailSerializer

# Create your views here.
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class =InvoiceSerializer

class InvoiceDetailViewSet(viewsets.ModelViewSet):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailSerializer
