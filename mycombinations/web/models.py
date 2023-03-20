from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=200)

class Alcohol(models.Model):
    name = models.CharField(max_length=200)
    marca = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
class Mix(models.Model):
    name = models.CharField(max_length=200)
    marca = models.ForeignKey(Brand, on_delete=models.CASCADE)

class Combination(models.Model):
    name = models.CharField(max_length=200)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE)
    barreja = models.ForeignKey(Mix, on_delete=models.CASCADE)
