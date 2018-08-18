# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, filters
from apiv1.models import *
from apiv1.serializers import *
from drf_haystack.viewsets import HaystackViewSet

from apiv1.filters import SimplifiedHaystackFilter
from apiv1.pagination import DocumentPageNumberPagination

# Create your views here.

class DocumentViewSet(HaystackViewSet):
    index_models = [Document]
    serializer_class = MainDocumentSearchSerializer
    pagination_class = DocumentPageNumberPagination
    filter_backends = [SimplifiedHaystackFilter, filters.OrderingFilter, ]
    ordering_fields = ['time',]

