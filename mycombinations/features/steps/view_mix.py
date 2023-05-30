from behave import *

use_step_matcher("parse")

@when('I view the details for mix "{mix_name}"')
def step_impl(context, mix_name):
    from web.models import Mix
    mix = Mix.objects.get(name=mix_name)
    context.browser.visit(context.get_url(mix))

@then("I'm viewing mix details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])