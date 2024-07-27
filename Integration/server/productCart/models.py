from django.db import models

class productDetails(models.Model):
    product_name = models.CharField(max_length=100)
    product_qty = models.IntegerField(default = 0)
    product_price = models.IntegerField()
    total_price = models.IntegerField()
    
    
    def __str__ (self):
        return f"id : {self.id} - product_name : {self.product_name} - product_qty : {self.product_qty} - product_price : {self.product_price} : total_price : {self.total_price}"
