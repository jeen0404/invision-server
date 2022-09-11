from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from accounts.models import User
from inventory.models import InventoryModel, InventoryUnit
from inventory.serializers import InventoryListModelSerializer, InventoryUnitSerializer, InventoryModelSerializer
from organization.models import Organization


class InventorysView(generics.ListAPIView):
    """ for handling user_post request """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InventoryListModelSerializer

    def get_queryset(self):
        organization_id = self.request.user.organization
        print(organization_id)
        return InventoryModel.objects.filter(organization=organization_id)


class InventoryUnitsView(generics.ListAPIView):
    """ for handling user_post request """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InventoryUnitSerializer

    def get_queryset(self):
        return InventoryUnit.objects.all()


class InventoryView(CreateAPIView):
    """ for handling user_post request """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InventoryModelSerializer

    def post(self, request, **kwargs):
        user: User = request.user
        organization: Organization = request.user.organization
        print(request.data);
        if 'name' in request.data and 'description' and request.data and 'unit_id' and request.data and 'code' and request.data and 'min' in request.data and 'max' in request.data:
            try:
                inventory_model = InventoryModel(created_by=user,
                                                 organization=organization,
                                                 name=request.data['name'],
                                                 description=request.data['description'],
                                                 code=request.data['code'],
                                                 min=request.data['min'],
                                                 max=request.data['max'],
                                                 unit=InventoryUnit.objects.get(inventory_unit_id=request.data['unit'])
                                                 )
                inventory_model.save()
                return Response(status=200)
            except Exception as e:
                return Response(status=429,data={'reason':"Inventory already exist with given material code."})
        else:
            return Response({"error": "request params in invalid"})
