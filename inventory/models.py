import uuid

from django.db import models

from accounts.models import User
from organization.models import Organization
from django.utils import timezone


class InventoryUnit(models.Model):
    inventory_unit_id = models.CharField(max_length=36, unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=500, default="")
    description = models.TextField(default="")
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.description)


class InventoryModel(models.Model):
    inventory_id = models.CharField(max_length=36, unique=True, primary_key=True, default=uuid.uuid4)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=500, default="")
    code = models.CharField(max_length=500, default="", unique=True)
    description = models.TextField(default="")
    unit = models.ForeignKey(InventoryUnit, on_delete=models.DO_NOTHING, null=True)
    max = models.CharField(max_length=500, default="")
    min =  models.CharField(max_length=500, default="")
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} - {} - {}".format(self.name, self.organization, self.unit)


class InventoryChangeModel(models.Model):
    inventory_change_id = models.CharField(max_length=36, unique=True, primary_key=True, default=uuid.uuid4)
    inventory = models.ForeignKey(InventoryModel, on_delete=models.DO_NOTHING, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING, null=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    created = models.DateTimeField(default=timezone.now)
    price_per_unit = models.FloatField(default=0.0)
    quantity = models.FloatField(default=0.0)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.inventory, self.created_by, self.organization, self.quantity)
