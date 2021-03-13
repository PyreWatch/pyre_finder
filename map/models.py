from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Fighter(models.Model):
    FIRE_CHOICES = (
        ('P', 'Fire is present'),
        ('N', 'Fire is not present')
    )

    OPERATION_CHOICES = (
        ('O', 'Agent is operational'),
        ('N', 'Agent is not operational')
    )
    
    latitude = models.DecimalField(max_digits=4, decimal_places=2, validators=[MaxValueValidator(90.00), MinValueValidator(-90.00)])
    longitude = models.DecimalField(max_digits=5, decimal_places=2, validators=[MaxValueValidator(180.00), MinValueValidator(-180.00)])
    fire_status = models.CharField(max_length=1, choices=FIRE_CHOICES, default='N')
    operation_status = models.CharField(max_length=1, choices=OPERATION_CHOICES,  default='O')

    def __str__(self):
        return 'Fighter agent @' + str(self.latitude) + ", " + str(self.longitude)