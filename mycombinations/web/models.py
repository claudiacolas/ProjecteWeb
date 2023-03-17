from django.db import models

# Create your models here.

class Marca(models.Model):
    name = models.CharField(max_length=200)

class Alcohol(models.Model):
    name = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    
class Barreja(models.Model):
    name = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

class Combinacio(models.Model):
    name = models.CharField(max_length=200)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE)
    barreja = models.ForeignKey(Barreja, on_delete=models.CASCADE)
