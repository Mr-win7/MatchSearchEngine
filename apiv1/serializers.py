from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer, HighlighterMixin

from apiv1.models import *
from apiv1.search_indexes import *

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class DocumentSearchSerializer(HighlighterMixin, HaystackSerializer):
    highlighter_css_class = "highlighted-class"
    highlighter_html_tag = "em"
    class Meta:
        index_classes = [DocumentIndex]
        fields = ['id', 'title', 'department', 'url', 'time']

