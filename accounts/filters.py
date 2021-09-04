import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created',
                            lookup_expr='gte', label='Data do pedido maior que ou igual a')
    end_date = DateFilter(field_name='date_created', lookup_expr='lte',
                          label='Data do pedido menor que ou igual a')
    note = CharFilter(field_name='note',
                      lookup_expr='icontains', label='Observação')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']
