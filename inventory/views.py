from django.shortcuts import render

# Create your views here.
from rest_framework import permissions, generics
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from inventory.models import InventoryModel
from inventory.serializers import InventoryModelSerializer
from organization.models import Organization


class Inventory(generics.ListAPIView):
    """ for handling user_post request """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = InventoryModelSerializer

    def get_queryset(self):
        post_id = self.request.user.organization_id
        return InventoryModel.objects.filter(organization=post_id)
