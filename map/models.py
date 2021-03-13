from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Fighter(models.Model):
    FIRE_CHOICES = (
        ('P', "Fire is Present"),
        ('N', "Fire is not Present")
    )
    
    latitude = models.DecimalField(max_digits=4, decimal_places=2, validators=[MaxValueValidator(90.00), MinValueValidator(-90.00)])
    longitude = models.DecimalField(max_digits=5, decimal_places=2, validators=[MaxValueValidator(180.00), MinValueValidator(-180.00)])
    status = models.CharField(max_length=1, choices = FIRE_CHOICES)