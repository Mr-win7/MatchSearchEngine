from haystack import indexes
from apiv1.models import *

class DocumentIndex(indexes.ModelSearchIndex, indexes.Indexable):
    class Meta:
        model = Document
