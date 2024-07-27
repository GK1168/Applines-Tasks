from django.db import models

class ProductsList(models.Model):
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.FloatField()
    date_time = models.DateField(auto_now=True)
    favourites = models.BooleanField(default=False)
    archive = models.BooleanField(default=True)
    product_description = models.TextField(max_length=500)
    
    def __str__(self):
        return f"id: {self.product_id} +--+ name: {self.product_name} +--+ price: {self.price} +--+ quantity: {self.quantity} +--+ date and time : {self.date_time} +--+ favourites : {self.favourites} +--+ Archived :{self.archive} +--+ Description : {self.product_description}"
    
# class FavouritesList(models.Model):
#     favourites = models.ManyToManyField(ProductsList)
    
#     def __str__(self):
#         return f"favourites : {self.favourites}"