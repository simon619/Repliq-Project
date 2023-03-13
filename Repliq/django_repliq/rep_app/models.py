from django.db import models

# Create your models here.
class Company(models.Model):
    com_name = models.CharField(max_length=50)
    com_id = models.IntegerField(primary_key=True)
    dev_status = models.CharField(max_length=15)
    user_id_f =  models.ForeignKey("User", on_delete=models.CASCADE)


class User(models.Model):
    user_name = models.CharField(max_length=50)
    user_id = models.IntegerField(primary_key=True)
    device_id_f = models.ForeignKey("Device", on_delete=models.CASCADE)

class Device(models.Model):
    device_name = models.CharField(max_length=50)
    device_id = models.IntegerField(primary_key=True)
