

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

class Package(models.Model):
    name=models.CharField(max_length=100)
    price=models.FloatField(max_length=20)
    item1=models.CharField(max_length=100)
    item2=models.CharField(max_length=100)
    item3=models.CharField(max_length=100)
    item4=models.CharField(max_length=100)
    item5=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Booking(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} - {self.package.name}"