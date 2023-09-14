from django.db import models
from django.utils import timezone


# Create your models here.
   
    
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField()
    
    # sale_start = models.DateTimeField(blank=True, null=True, default=None)
    # sale_end = models.DateTimeField(blank=True, null=True, default=None)
    # photo = models.ImageField(blank=True, null=True, default=None, upload_to='products')

    # def is_on_sale(self):
    #     now = timezone.now()
    #     if self.sale_start:
    #         if self.sale_end:
    #             return self.sale_start <= now <= self.sale_end
    #         return self.sale_start <= now
    #     return False

    # def get_rounded_price(self):
    #     return round(self.price, 2)

    # def current_price(self):
    #     if self.is_on_sale():
    #         discounted_price = self.price * (1 - self.DISCOUNT_RATE)
    #         return round(discounted_price, 2)
    #     return self.get_rounded_price()

    def __repr__(self):
        return '<Product object ({}) "{}">'.format(self.id, self.name)