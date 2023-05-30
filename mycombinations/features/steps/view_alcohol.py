from behave import *

use_step_matcher("parse")

@when('I view the details for alcohol "{alcohol_name}"')
def step_impl(context, alcohol_name):
    from web.models import Alcohol
    alcohol = Alcohol.objects.get(name=alcohol_name)
    context.browser.visit(context.get_url(alcohol))

@then("I'm viewing alcohol details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])