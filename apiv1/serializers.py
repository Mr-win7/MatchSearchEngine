from rest_framework import serializers
from drf_haystack.serializers import HaystackSerializer, HighlighterMixin, HaystackSerializerMixin

from apiv1.models import *
from apiv1.search_indexes import *

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class DocumentSearchSerializer(HaystackSerializerMixin, DocumentSerializer):
    class Meta(DocumentSerializer.Meta):
        index_classes = [DocumentIndex]

'''
class MainDocumentSearchSerializer(HighlighterMixin, HaystackSerializer):
    highlighter_css_class = 'highlighted-class'
    highlighter_html_tag = 'em'
    class Meta:
        serializers = {
            DocumentIndex: DocumentSearchSerializer,
        }
'''

class MainDocumentSearchSerializer(HighlighterMixin, HaystackSerializer):
    highlighter_css_class = 'highlighted-class'
    highlighter_html_tag = 'em'
    class Meta:
        index_classes = [DocumentIndex]
        fields = ['text', 'time', 'department', 'content', 'title']

