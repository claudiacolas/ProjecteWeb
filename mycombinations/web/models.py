from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name

class Alcohol(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name+" of the brand "+self.brand.name
    
class Mix(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name

class Combination(models.Model):
    name = models.CharField(max_length=200)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE)
    mix = models.ForeignKey(Mix, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.name+"="+self.alcohol+"with"+self.mix
