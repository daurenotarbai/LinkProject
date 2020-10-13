from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(CategoryLink)
class CategoryLinkTranslationOptions(TranslationOptions):
    fields = ('category_name',)


@register(LinkModel)
class LinkModelTranslationOptions(TranslationOptions):
    fields = ('link_title',)





