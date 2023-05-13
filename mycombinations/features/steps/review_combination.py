from behave import *

use_step_matcher("parse")

@given('Exists review at combination "{combination_name}" by "{username}"')
def step_impl(context, combination_name, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from mycombinations.web.models import Combination
    combination = Combination.objects.get(name=combination_name)
    from mycombinations.web.models import CombinationReview
    for row in context.table:
        review = CombinationReview(combination=combination, user=user)
        for heading in row.headings:
            setattr(review, heading, row[heading])
        review.save()

@when('I register a review at combination "{combination_name}"')
def step_impl(context, combination_name):
    from mycombinations.web.models import Combination
    combination = Combination.objects.get(name=combination_name)
    for row in context.table:
        context.browser.visit(context.get_url(combination))
        form = context.browser.find_by_tag('form').first
        context.browser.choose('rating', row['rating'])
        context.browser.fill('comment', row['comment'])
        form.find_by_value('Review').first.click()

@then('There are {count:n} reviews')
def step_impl(context, count):
    from mycombinations.web.models import CombinationReview
    assert count == CombinationReview.objects.count()