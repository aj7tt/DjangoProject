from django.db import models

# Import the necessary module
from django.db import models

# Define the Product model
class Product(models.Model): 
    name = models.CharField(max_length=120)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name+ " price is = "+ self.price