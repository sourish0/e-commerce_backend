from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.

class Brand(models.Model):
    name =models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = TreeForeignKey('Category', on_delete=models.PROTECT)
    # price = models.IntegerField()
    description = models.TextField()
    is_digital = models.BooleanField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    class MPTTMeta:
        order_insertion_by = ['name']
    def __str__(self):
        return self.name