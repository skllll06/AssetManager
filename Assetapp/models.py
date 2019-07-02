from django.db import models

# Create your models here.
class Assetlist(models.Model):
    assetname=models.CharField(max_length=50)
    controlno=models.CharField(max_length=50)
    modelno=models.CharField(max_length=50)
    boughtdate=models.DateField()
    stockplace=models.CharField(max_length=50)
    
    def __str__(self):
        return self.controlno
    