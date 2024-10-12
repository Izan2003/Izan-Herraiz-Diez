from django.db import models

# Create your models here.
# Modelo Destination
class Destination(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        unique=True,
        blank=False
    )
    description = models.TextField(
        max_length=2000,
        null=False,
        blank=False
    )

    def __str__(self):
        return self.name
# Modelo Cruise
class Cruise(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False
    )
    description = models.TextField(
        max_length=2000,
        blank=False
    )

    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, null=True)

    duration = models.IntegerField(default=10, null=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00,null=True)

    departure_date = models.DateField(
        blank=False,
        null=True,
        default = "2024-01-01"
    )

    def __str__(self):
        return self.name

