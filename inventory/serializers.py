from django.db.models import Sum
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from accounts.models import User
from inventory.models import InventoryModel, InventoryChangeModel, InventoryUnit
from organization.models import Organization


class InventoryListModelSerializer(ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(allow_null=True, source="organization.name",
                                                      queryset=Organization.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(allow_null=True, source="created_by.name",
                                                    queryset=User.objects.all())
    unit = serializers.PrimaryKeyRelatedField(allow_null=True, source="unit.name", queryset=User.objects.all())

    quantity = serializers.SerializerMethodField('get_quantity')

    def get_quantity(self, inventory_model):
        sum_up = InventoryChangeModel.objects.filter(inventory=inventory_model).aggregate(Sum('quantity'))[
            'quantity__sum']
        if sum_up:
            return sum_up
        else:
            return 0.0

    class Meta:
        model = InventoryModel
        fields = ['inventory_id', 'organization', 'name', 'description', 'unit', 'code', 'created_by', 'quantity','min','max']


class InventoryModelSerializer(ModelSerializer):
    class Meta:
        model = InventoryModel
        fields = ['code', 'name', 'description', 'unit', 'max', 'min']


class InventoryUnitSerializer(ModelSerializer):
    class Meta:
        model = InventoryUnit
        fields = ['inventory_unit_id', 'name', 'description']
