from behave import *

use_step_matcher("parse")

@when('I view the details for brand "{brand_name}"')
def step_impl(context, brand_name):
    from web.models import Brand
    brand = Brand.objects.get(name=brand_name)
    context.browser.visit(context.get_url(brand))

@then("I'm viewing brand details including")
def step_impl(context):
    for heading in context.table.headings:
        context.browser.is_text_present(context.table[0][heading])