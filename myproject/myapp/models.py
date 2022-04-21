from django.db import models

# Create your models here.
class Customer(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=5)
    email = models.EmailField()

    def __str__(self):
        return "%s"%(self.fullname)