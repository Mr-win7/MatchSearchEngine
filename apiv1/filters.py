from drf_haystack.filters import HaystackFilter
from hanziconv import HanziConv

class SimplifiedHaystackFilter(HaystackFilter):
    def process_filters(self, filters, queryset, view):
        print filters
        return filters
