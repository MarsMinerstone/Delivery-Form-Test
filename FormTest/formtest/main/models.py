from django.db import models


class Product(models.Model):
    prod_name = models.CharField(unique=True, max_length=20)
    p_image = models.ImageField(verbose_name='Image', upload_to="media/", null=True, blank=True)
    cat = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.prod_name


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Delivery(models.Model):
    delivery_name = models.ForeignKey('Product', on_delete=models.CASCADE)
    delivery_date = models.DateField()
    delivery_address = models.CharField(max_length=40)

    def __str__(self):
        return self.delivery_name
