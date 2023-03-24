from rest_framework import serializers
from api.models import Invoice,InvoiceDetail

class InvoiceSerializer(serializers.HyperlinkedModelSerializer):


    class Meta:
        model=Invoice
        fields=['id','Date','InvoiceNo','CustomerName']

class InvoiceDetailSerializer(serializers.HyperlinkedModelSerializer):
    #NESTED SERIALIZER
    sungby = InvoiceSerializer(many=True,read_only=True)

    class Meta:
        model=InvoiceDetail
        fields=['id','invoice','description','quantity','unit_price','price','sungby']
