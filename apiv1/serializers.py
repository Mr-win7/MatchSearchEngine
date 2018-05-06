from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer

from apiv1.models import *
from apiv1.search_indexes import *

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        index_classes = [DocumentIndex]




