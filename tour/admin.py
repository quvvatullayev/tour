from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
    Country,
    Exclusive,
    About_company,
    News,
    Commit,
    Appeal,
    Contact,
    
)

admin.site.register(Country)
admin.site.register(Exclusive)
admin.site.register(About_company)
admin.site.register(News)
admin.site.register(Commit)
admin.site.register(Appeal)
admin.site.register(Contact)
