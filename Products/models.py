from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50) 
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)
    email = models.EmailField(max_length=254)
    date = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=100,default='null')
    
    def __str__ (self):
        return f"{self.last_name} {self.first_name}"
    
# class Products(models.Model):
#     name = models.CharField(max_length=50)
#     category_id = models.ForeignKey(on_delete=models.CASCADE) 
#     price = models.IntegerField()
#     quantity = models.BigIntegerField()
#     description = models.TextField()

# class Category (models.Model):
#     name = models.CharField(max_length=50)

# class Client (models.Model):1
#     name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254)
#     phone_number = models.CharField(max_length=50)
#     addres = models.CharField(max_length=50)

# class Orders (models.model):
#     customer_id = models.BigIntegerField()
#     total_price = models.BigIntegerField()
#     status = models.CharField(max_length=50)
#     created_at = models.TimeField(auto_now=True)

# class Order_item (models.Model):
#     order_id = models.BigAutoField()
#     product_id = models.BigAutoField()
#     quantity = models.BigAutoField()
#     price = models.BigAutoField()

# class Stock_movement (models.Model):
#     product_id = models.BigAutoField()
#     change_type = models.CharField(max_length=50)
#     quantity_change = models.BigAutoField()
#     date = models.DateField(auto_now=True)

    