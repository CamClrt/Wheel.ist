from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from products.models import Product
from products.tables import ProductHTMxTable
from products.filters import ProductFilter


class ProductHTMxTableView(SingleTableMixin, FilterView):
    table_class = ProductHTMxTable
    queryset = Product.objects.all()
    filterset_class = ProductFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "product_table_partial.html"
        else:
            template_name = "product_table_htmx.html"

        return template_name
