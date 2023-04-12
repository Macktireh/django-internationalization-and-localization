from modeltranslation.translator import register, TranslationOptions

from apps.course.models import News


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text')
