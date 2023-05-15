from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    
    class Type(models.IntegerChoices):
        NONE = 0
        ALCOHOL = 1
        MIX = 2
    
    type = models.IntegerField(choices=Type.choices, default=0)
    
    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('web:brand_detail', kwargs={'pk': self.pk})


class Alcohol(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    
    def __str__(self) -> str:
        return self.name+" of the brand "+self.brand.name

    def get_absolute_url(self):
        return reverse('mycombinations:alcohol_detail', kwargs={'pkr': self.Alcohol.pk, 'pk': self.pk})
    
class Mix(models.Model):
    name = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    
    def __str__(self) -> str:
        return self.name+" of the brand "+self.brand.name

    def get_absolute_url(self):
        return reverse('mycombinations:mix_detail', kwargs={'pkr': self.Mix.pk, 'pk': self.pk})

class Combination(models.Model):
    name = models.CharField(max_length=200)
    alcohol = models.ForeignKey(Alcohol, on_delete=models.CASCADE)
    mix = models.ForeignKey(Mix, on_delete=models.CASCADE)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    image=models.ImageField(upload_to="mycombinations", blank=True, null=True)
    
    def __unicode__(self):
        return u"%s" % self.name

    def __str__(self) -> str:
        return self.name+" with " +self.alcohol.brand.name+" and "+self.mix.brand.name

    def get_absolute_url(self):
        return reverse('mycombinations:combination_detail', kwargs={'pk': self.pk})

    def averageRating(self):
        reviewCount = self.combinationsreview_set.count()
        if not reviewCount:
            return 0
        else:
            ratingSum = sum([float(review.rating) for review in self.combinationreview_set.all()])
            return ratingSum / reviewCount

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class CombinationReview(Review):
    combination = models.ForeignKey(Combination, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("combination", "user")
