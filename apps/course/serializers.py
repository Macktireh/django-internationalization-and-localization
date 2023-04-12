from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField

from apps.course.models import Course, News


class CourseTranslatableSerializer(TranslatableModelSerializer):
    
    translations = TranslatedFieldsField(shared_model=Course)

    class Meta:
        model = Course
        fields = ('id', 'translations', 'price', 'thumbnail', 'date',)


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'date', 'price', 'thumbnail',)


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'text', 'date', 'thumbnail',)
