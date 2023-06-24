from modeltranslation.translator import TranslationOptions,register
from .models import (
    Country,
    Exclusive,
    About_company,
    News,
    Commit,
    Appeal,
    Contact,
)

@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('name', 'discription')

@register(Exclusive)
class ExclusiveTranslationOptions(TranslationOptions):
    fields = ('name', )

@register(About_company)
class About_companyTranslationOptions(TranslationOptions):
    fields = ('discription',)

@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'discription',)

@register(Commit)
class CommitTranslationOptions(TranslationOptions):
    fields = ('name', 'discription')

@register(Appeal)
class AppealTranslationOptions(TranslationOptions):
    fields = ('name', 'title')

@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('area','location')