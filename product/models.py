
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, null= True)
    slug = models.SlugField(max_length=50 , unique= True , null= True)



      
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null= True ,  on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=200, blank = True)
    image = models.ImageField(upload_to ='product/%Y/%m/%d/', null = True)
    price = models.DecimalField(max_digits=10, decimal_places=2,  default=0.0) 

    def __str__(self):
     return self.name
    



class Product2(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null= True , blank= True, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=200, blank = True)
    image = models.ImageField(upload_to ='product/%Y/%m/%d/', null = True)


    def __str__(self):
     return self.name
    



class Product3(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null= True , blank= True, on_delete=models.DO_NOTHING)
    description = models.TextField(max_length=200, blank = True)
    image = models.ImageField(upload_to ='product/%Y/%m/%d/', null = True)


    def __str__(self):
     return self.name
    



class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart of {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)