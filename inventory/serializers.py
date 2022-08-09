from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from accounts.models import User
from accounts.serializers import ProfileSerializer
from inventory.models import InventoryModel
from organization.models import Organization
from organization.serializers import OrganizationSerializer


class InventoryModelSerializer(ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(allow_null=True, source="organization.organization_id",
                                                      queryset=Organization.objects.all())
    user = serializers.PrimaryKeyRelatedField(allow_null=True, source="user.user_id", queryset=User.objects.all())

    class Meta:
        model = InventoryModel
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)

        inventory_model = InventoryModel(organization=validated_data['organization']['organization_id'],
                                         user=validated_data['user']['user_id'],
                                         name=validated_data['name'], description=validated_data['description'])
        inventory_model.save()
        return inventory_model
