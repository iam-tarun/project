import django_filters
from .models import Itemlist


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Itemlist
        fields = ['item']
