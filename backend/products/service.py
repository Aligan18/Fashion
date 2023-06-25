from django_filters import rest_framework as filters, ChoiceFilter


from comments.models import Comments
from products.models import TYPE_CHOICES, GENDER_CHOICES, Products


class ProductsFilter(filters.FilterSet):
    type = ChoiceFilter(choices=TYPE_CHOICES)
    gender = ChoiceFilter(choices=GENDER_CHOICES)
    price = filters.RangeFilter()
    visible = filters.BooleanFilter()

    class Meta:
        model = Products
        fields = ['visible', 'price', 'type', 'gender']
