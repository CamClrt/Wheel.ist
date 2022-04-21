# from django.db import models
#
# """
#     # Brand
#     0.1 marque, plusieurs produits
#
#     # Options
#     0.n options, plusieurs produits
#
#     # Catégories
#     1.n catégories, plusieurs produits
#
#     # Produit
#     Model/ref
#     Power(W)
#     Battery (Wh)
#     Battery (Ah)
#     Size
#     Max Speed (Km/h)
#     Range (Km)
#     Charge time (H)
#     Weight (Kg)
#     Max weight (Kg)
#     Year
#
#     Voir aussi :
#     # https://django-model-utils.readthedocs.io/en/4.1.1/index.html#
#     # https://django-extensions.readthedocs.io/en/latest/index.html
# """
#
#
# class Status(models.IntegerChoices):
#     ACTIVE = 1, "Active"
#     INACTIVE = 2, "Inactive"
#     ARCHIVED = 3, "Archived"
#
#
# class Brand(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#
# class Option(models.Model):
#     name = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=255)
#     reference = models.CharField(max_length=255)
#     sku = models.CharField(max_length=255)
#     status = models.PositiveSmallIntegerField(choices=Status.choices)
#     collapsible = models.BooleanField()
#     weight = models.PositiveSmallIntegerField()
#     speed_max = models.PositiveSmallIntegerField()
#     autonomy_max = models.PositiveSmallIntegerField()
#
#     """
#     color = models.CharField(max_length=255)
#     brand = models.ForeignKey(Brand, on_delete=models.SET_NULL)
#     category = models.ForeignKey(Category, on_delete=models.SET_NULL)
#     options = models.ManyToManyField(Option, on_delete=models.CASCADE, verbose_name="list of options")
#     TODO: revoir CASCADE où SET_NULL
#     """
#
#     """year = models.DateField()
#     power = models.DecimalField(max_digits=5, decimal_places=2)
#     battery_wh = models.DecimalField(max_digits=5, decimal_places=2)
#     battery_ah = models.DecimalField(max_digits=5, decimal_places=2)
#     size = models.PositiveSmallIntegerField()
#     max_speed = models.PositiveSmallIntegerField()
#     range = models.PositiveSmallIntegerField()
#     charge_time = models.PositiveSmallIntegerField()
#     weight = models.PositiveSmallIntegerField()
#     max_weight = models.PositiveSmallIntegerField()"""
#
#     def __str__(self):
#         return self.name

from django.db import models


class Product(models.Model):
    class Status(models.IntegerChoices):
        ACTIVE = 1, "Active"
        INACTIVE = 2, "Inactive"
        ARCHIVED = 3, "Archived"

    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.PositiveSmallIntegerField(choices=Status.choices)

    def __str__(self):
        return self.name
