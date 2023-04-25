from functools import reduce

from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")

@given('Exists mix registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from mycombinations.models import Mix
    for row in context.table:
        mix = Mix(user=user)
        for heading in row.headings:
            setattr(mix, heading, row[heading])
        mix.save()

@when('I register mix')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('mycombinations:mix_create'))
        if context.browser.url == context.get_url('mycombinations:mix_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('There are {count:n} mixs')
def step_impl(context, count):
    from mycombinations.models import Mix
    assert count == Mix.objects.count()

@then('I\'m viewing the details page for mix by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from mycombinations.models import Mix
    mix = Mix.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(mix)

@when('I edit the mix with name "{name}"')
def step_impl(context, name):
    from mycombinations.models import Mix
    mix = Mix.objects.get(name=name)
    context.browser.visit(context.get_url('mycombinations:mix_edit', mix.pk))
    if context.browser.url == context.get_url('mycombinations:mix_edit', mix.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()