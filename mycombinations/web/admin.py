from django.contrib import admin

from web.models import Brand, Alcohol, Mix, Combination

# Register your models here.

admin.site.register(Brand)
admin.site.register(Alcohol)
admin.site.register(Mix)
admin.site.register(Combination)
