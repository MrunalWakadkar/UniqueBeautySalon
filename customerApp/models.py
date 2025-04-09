

# Create your models here.
from django.db import models

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('Hair Care', 'Hair Care'),
        ('Skin Care', 'Skin Care'),
        ('Makeup', 'Makeup'),
        ('Nail Care', 'Nail Care'),
        ('Spa', 'Spa & Massage'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.CharField(max_length=50)
    image = models.ImageField(upload_to='services/', blank=True, null=True)

    def __str__(self):
        return self.name
