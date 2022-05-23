from django.db import models
# from django.db.models import UniqueConstraint
from django.contrib.auth import get_user_model
from shop.models import Item, Group, Collection

User = get_user_model()

# class Order(models.Model):
#     item = models.ForeignKey(
#         Item,
#         null=True,
#         related_name='item',
#         on_delete=models.SET_NULL,
#         verbose_name='item in ordering'
#     )
#     holder = models.ForeignKey(
#         User,
#         related_name='item',
#         on_delete=models.CASCADE,
#         verbose_name='item in ordering'

#     )
        

class User(models.Model):
    first_name = models.CharField(
        max_length=150,
        help_text='input name',
        verbose_name='title of group',
    )
    second_name = models.CharField(
        max_length=150
    )
    middle_name = models.CharField(
        max_length=150
    )
    country = models.CharField(
        max_length=150
    )
    region = models.CharField(
        max_length=150
    )
    city = models.CharField(
        max_length=150
    )
    street = models.CharField(
        max_length=150
    )
    house = models.CharField(
        max_length=150
    )
    flat = models.CharField(
        max_length=150
    )
    orders = models.CharField(
        max_length=150
    )
    

class Cart(models.Model):
    itemcart = models.ForeignKey(
        Item,
        null=True,
        related_name='item',
        on_delete=models.SET_NULL,
        verbose_name='item in ordering'
    )
    holder = models.ForeignKey(
        User,
        related_name='item',
        on_delete=models.CASCADE,
        verbose_name='item in ordering'

    )