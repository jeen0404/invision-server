# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models


# Create your models here.


class Organization(models.Model):
    organization_id = models.CharField(max_length=36, unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=500, unique=True)
    logo_url = models.TextField(default='')
    description = models.TextField(default='')
    address = models.TextField(default='')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return "{} - {}".format(self.name, self.description)
