from django.db import models
from django.db.models import CharField
from django.utils import timezone

# Create your models here.

class CODE(models.Model):
    name = models.CharField(max_length=50, null=True)
    super = models.ForeignKey('self', null=True, blank=True, on_delete = models.CASCADE)
    create_date = models.DateTimeField(default=timezone.now)
    expired_date = models.DateTimeField(null=True)
    last_modify_date = models.DateTimeField(null=True)




class User(models.Model):
    uuid = models.CharField(max_length=50,default=True)
    create_date = models.DateTimeField(default=timezone.now)
    expired_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.uuid


class Store(models.Model):
    store_name = models.CharField(max_length=200,null=True)
    create_date = models.DateTimeField(default=timezone.now)
    expired_date = models.DateTimeField(null=True)
    last_modify_date = models.DateTimeField(null=True)
    category = models.ForeignKey(CODE, on_delete=models.CASCADE)


class ITEM(models.Model):
    store_id = models.ForeignKey(Store, on_delete = models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=200)
    stars = models.PositiveIntegerField(default=0)
    create_date = models.DateTimeField(default=timezone.now)
    expired_date = models.DateTimeField(null=True)
    last_modify_date = models.DateTimeField(null=True)


class USER_HISTORY(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    distance = models.CharField(max_length=10,null=True)
    category = models.CharField(max_length=10,null=True)
    number = models.IntegerField(null=True)
    create_date = models.DateTimeField(default=timezone.now)


class place(models.Model):
    address_name = models.CharField(max_length=100, blank=True, null=True, verbose_name='주소')
    category_group_code = models.CharField(max_length=10,default='0')
    distance = models.DecimalField(default=0, max_digits=10, decimal_places=4)
    map_id = models.CharField(max_length=20,default='0')
    phone = models.CharField(max_length=20, blank=True, null=True)
    place_name: CharField = models.CharField(max_length=30,null=True)
    place_url = models.TextField(null=True)
    road_address_name = models.TextField(null=True)
    lat = models.DecimalField(default=0, max_digits=18, decimal_places=15,null=True)
    lng = models.DecimalField(default=0, max_digits=18, decimal_places=15,null=True)

    def __str__(self):
        return self.place_name

    def getUrl(self):
        return self.place_url

