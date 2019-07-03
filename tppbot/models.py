from django.db import models

# Create your models here.
class User(models.Model):
    uuid = models.CharField(max_length=50)
    create_date = models.DateTimeField('date join')

class Store(models.Model):
    storeid = models.CharField(max_length=10)
    storename = models.CharField(max_length=50)
    create_date = models.DateTimeField('date create')
    last_modify_date = models.DateTimeField('date modify')