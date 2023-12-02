from rest_framework import viewsets, permissions,status
from django.core.exceptions import ValidationError
from api.models import Vendor,PurchaseOrder,HistoricalPerformance
from rest_framework.decorators import action
from rest_framework.response import Response
from api.serializers import VendorSerializer,PurchaseOrderSerializer,HistoricalPerformanceSerializer
from django.db import models




class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    permission_classes=[permissions.AllowAny]
    
    
    
    
    @action(detail=True, methods=['get'])
    def performance(self, request, pk=None):
        vendor = self.get_object()
        print("Data to be saved:", vendor.__dict__)
        serializer = HistoricalPerformanceSerializer(vendor.historicalperformance_set.all(), many=True)
        return Response(serializer.data)
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except ValidationError as e:
            errors_dict = dict(e)
            error_messages = self.get_error_messages(errors_dict)
            return Response({"error": error_messages}, status=status.HTTP_400_BAD_REQUEST)

    
    
class PurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    permission_classes=[permissions.AllowAny]
    @action(detail=True, methods=['post'])
    def acknowledge(self, request, pk=None):
        purchase_order = self.get_object()
        purchase_order.acknowledgment_date = models.DateTimeField.now()
        purchase_order.save()
        purchase_order.vendor.historicalperformance_set.update_vendor_performance(purchase_order.vendor)
        return Response({"detail": "Acknowledgment recorded successfully."}, status=status.HTTP_200_OK)

class HistoricalPerformanceViewSet(viewsets.ModelViewSet):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer
    permission_classes=[permissions.AllowAny]