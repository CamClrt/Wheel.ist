import django_tables2 as tables
from products.models import Product


class SimpleTable(tables.Table):
    class Meta:
        model = Product
