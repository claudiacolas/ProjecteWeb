from functools import reduce

from behave import *
import operator
from django.db.models import Q

use_step_matcher("parse")

@given('Exists brand registered by "{username}"')
def step_impl(context, username):
    from django.contrib.auth.models import User
    user = User.objects.get(username=username)
    from mycombinations.web.models import Brand
    for row in context.table:
        brand = Brand(user=user)
        for heading in row.headings:
            setattr(brand, heading, row[heading])
        brand.save()

@when('I register brand')
def step_impl(context):
    for row in context.table:
        context.browser.visit(context.get_url('web:brand_create'))
        if context.browser.url == context.get_url('web:brand_create'):
            form = context.browser.find_by_tag('form').first
            for heading in row.headings:
                context.browser.fill(heading, row[heading])
            form.find_by_value('Submit').first.click()

@then('There are {count:n} brands')
def step_impl(context, count):
    from web.models import Brand
    assert count == Brand.objects.count()

@then('I\'m viewing the details page for brand by "{username}"')
def step_impl(context, username):
    q_list = [Q((attribute, context.table.rows[0][attribute])) for attribute in context.table.headings]
    from django.contrib.auth.models import User
    q_list.append(Q(('user', User.objects.get(username=username))))
    from web.models import Brand
    brand = Brand.objects.filter(reduce(operator.and_, q_list)).get()
    assert context.browser.url == context.get_url(brand)

@when('I edit the brand with name "{name}"')
def step_impl(context, name):
    from mycombinations.web.models import Brand
    brand = Brand.objects.get(name=name)
    context.browser.visit(context.get_url('web:brand_edit', brand.pk))
    if context.browser.url == context.get_url('web:brand_edit', brand.pk)\
            and context.browser.find_by_tag('form'):
        form = context.browser.find_by_tag('form').first
        for heading in context.table.headings:
            context.browser.fill(heading, context.table[0][heading])
        form.find_by_value('Submit').first.click()