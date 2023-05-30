from functools import reduce

from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")

@given('Exists combination registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from web.models import Combination
    for row in context.table:
        combination = Combination(user=user)
        for heading in row.headings:
            setattr(combination, heading, row[heading])
        combination.save()

@when('I register combination')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('web:combination_create'))
        if context.browser.url == context.get_url('web:combination_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('There are {count:n} combinations')
def step_impl(context, count):
    from web.models import Combination
    assert count == Combination.objects.count()

@then('I\'m viewing the details page for combination by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from web.models import Combination
    combination = Combination.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(combination)

@when('I edit the combination with name "{name}"')
def step_impl(context, name):
    from web.models import Combination
    combination = Combination.objects.get(name=name)
    context.browser.visit(context.get_url('web:combination_edit', combination.pk))
    if context.browser.url == context.get_url('web:combination_edit', combination.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()