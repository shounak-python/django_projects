from django.db import models

# Create your models here.
# category, state, region, iso

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class State(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Region(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Iso(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name


class Site(models.Model):
    name=models.CharField(max_length=100,null=True)
    description=models.CharField(max_length=500,null=True)
    justification=models.CharField(max_length=500,null=True)
    year=models.PositiveIntegerField(null=True)
    longitude=models.FloatField(null=True)
    latitude=models.FloatField(null=True)
    area_hectares=models.FloatField(null=True)
    category=models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    region=models.ForeignKey("Region", on_delete=models.CASCADE, null=True)
    iso=models.ForeignKey("Iso", on_delete=models.CASCADE, null=True)
    state=models.ForeignKey("State", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name
