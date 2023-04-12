from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from modeltranslation.admin import TabbedExternalJqueryTranslationAdmin
from parler.admin import TranslatableAdmin

from apps.course.models import Course, News


@admin.register(Course)
class CourseAdmin(TranslatableAdmin):

    list_display = ('title', 'description', 'date', 'price')

    fieldsets = (
        (_("fields to be translated"), {
            'fields': ('title', 'description',),
        }),
        (_("fields not to be translated"), {
            'fields': ('date', 'price', 'thumbnail',),
        }),
    )



@admin.register(News)
class NewsAdmin(TabbedExternalJqueryTranslationAdmin):

    list_display = ('title', 'text')
