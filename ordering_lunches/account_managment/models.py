from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    telephone = models.PositiveIntegerField(max_length=12)

    def __str__(self):
        return self.name + " " + self.surname


class Product(models.Model):
    product_name = models.CharField(max_length=200)
    shop = models.CharField(max_length=30)
    price = models.PositiveIntegerField(max_length=12)

    def __str__(self):
        return str(self.product_name) + " " + str(self.shop) + " " + str(self.price) + " грн."


class UserTokken(models.Model):
    user_tokken=models.CharField(primary_key=True,max_length=30)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + " " + self.user_tokken + " "
