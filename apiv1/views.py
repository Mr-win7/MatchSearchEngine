# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from apiv1.models import *
from apiv1.serializers import *
from drf_haystack.viewsets import HaystackViewSet

# Create your views here.

class DocumentViewSet(HaystackViewSet):
    index_models = [Document]
    serializer_class = DocumentSearchSerializer
