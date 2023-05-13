from behave import *

use_step_matcher("parse")

@when('I view the details for combination "{combination_name}"')
def step_impl(context,combination_name):
    from mycombinations.web.models import Combination
    combination = Combination.objects.get(name=combination_name)
    context.browser.visit(context.get_url(combination))

@then("I'm viewing combination details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])