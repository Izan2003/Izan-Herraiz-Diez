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
    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name='cruises',
        null=True  # Permitir nulos
    )
    def __str__(self):
        return self.name



   