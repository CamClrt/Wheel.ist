import django_tables2 as tables
from products.models import Product


class ProductHTMxTable(tables.Table):
    class Meta:
        model = Product
        template_name = "tables/bootstrap_htmx.html"
