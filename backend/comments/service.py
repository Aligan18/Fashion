from django_filters import rest_framework as filters

from comments.models import Comments


class CommentsFilter(filters.FilterSet):
    class Meta:
        model = Comments
        fields = ['product']
