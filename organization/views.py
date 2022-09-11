# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from organization.serializers import OrganizationSerializer


# Create your views here.
class OrganizationView(CreateAPIView):
    """ for handling user_post request """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrganizationSerializer

    def get(self, request, **kwargs):
        organization = self.request.user.organization
        return Response(status=200,data=OrganizationSerializer(organization).data)

    def update(self,request, **kwargs):
        pass

    def delete(self,request, **kwargs):
        pass

    def put(self,request, **kwargs):
        pass

    def head(self,request, **kwargs):
        pass

