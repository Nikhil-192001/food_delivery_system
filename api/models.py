from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Item(models.Model):
    TYPE_CHOICES = [
        ('perishable', 'Perishable'),
        ('non-perishable', 'Non-Perishable')
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.type

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=100)
    base_distance_in_km = models.FloatField(default=5)
    km_price = models.FloatField()
    fix_price = models.FloatField()

    def __str__(self):
        return f"{self.organization} - {self.item} - {self.zone}"