import django_filters
from django_filters import rest_framework as filters
from .models import Pictures


class PictureFilter(django_filters.FilterSet):
    ln = filters.CharFilter(lookup_expr='contains', field_name='authorLastName')
    fn = filters.CharFilter(lookup_expr='contains', field_name='authorFirstName')
    un = filters.CharFilter(lookup_expr='contains', field_name='authorUserName')
    album = filters.CharFilter(lookup_expr='contains', field_name='album')
    title = filters.CharFilter(lookup_expr='contains', field_name='title')

    o = django_filters.OrderingFilter(
        fields=['authorFirstName', 'authorLastName', 'authorUserName', 'album', 'title']
    )

    class Meta:
        model = Pictures
        # fields = ['authorFirstName', 'authorLastName', 'album', 'title']
        fields = []
