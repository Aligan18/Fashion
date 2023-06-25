from django_filters import rest_framework as filters

from comments.models import Comments
from orders.models import Orders


class OrdersFilter(filters.FilterSet):
    class Meta:
        model = Orders
        fields = ['user']
