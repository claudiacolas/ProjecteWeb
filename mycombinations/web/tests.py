from django.test import TestCase
from django.contrib.auth.models import User
from .models import *

class CombinationReviewTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        user3 = User.objects.create(username="user3")
        rumcola =  Combination.objects.create(name="RumCola", user= user1)
        CombinationReview.objects.create(rating=3, comment="Average...", Combination=rumcola, user=user1)
        CombinationReview.objects.create(rating=5, comment="Excellent!", Combination=rumcola, user=user2)
        CombinationReview.objects.create(rating=1, comment="Really bad!", Combination=rumcola, user=user3)
        Combination.objects.create(name="Unknown Combination")

    def test_average_3reviews(self):
        """The average review for a combination with 3 reviews is properly computed"""
        combination = Combination.objects.get(name="RumCola")
        self.assertEqual(combination.averageRating(), 3)

    def test_average_no_review(self):
        """The average review for a combination without reviews is 0"""
        combination = Combination.objects.get(name="Unknown Combination")
        self.assertEqual(combination.averageRating(), 0)