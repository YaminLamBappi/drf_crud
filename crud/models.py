from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.CharField(max_length=255)
    phone = models.IntegerField()
    address = models.CharField(max_length=255)
    
    def __str__(self) :
        return f"{self.name,}, {self.phone}, {self.address}"