import uuid

from django.db import models

from accounts.models import User
from organization.models import Organization
from django.utils import timezone


class InventoryModel(models.Model):
    inventory_id = models.CharField(max_length=36, unique=True, primary_key=True, default=uuid.uuid4)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=500, default="")
    description = models.TextField(default="")
    unit = models.CharField(default="piece",max_length=50)
    created = models.DateTimeField(default=timezone.now)


class InventoryChangeModel(models.Model):
    inventory_change_id = models.CharField(max_length=36, unique=True, primary_key=True, default=uuid.uuid4)
    inventory = models.ForeignKey(InventoryModel, on_delete=models.DO_NOTHING, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created = models.DateTimeField(default=timezone.now)
    price_per_unit = models.FloatField(default=0.0)
    quantity = models.FloatField(default=0.0)
    deleted = models.BooleanField(default=False)
