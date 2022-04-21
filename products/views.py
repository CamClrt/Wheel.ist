import django_tables2 as tables
from tables import SimpleTable
from models import Product

class TableView(tables.SingleTableView):
    table_class = SimpleTable
    queryset = Product.objects.all()
    template_name = "base.html"
