from django.views.generic import ListView

from rest_framework import viewsets

from apps.course.models import Course, News
from apps.course.serializers import CourseSerializer, CourseTranslatableSerializer, NewsSerializer


class ListCourse(ListView):
    model = Course
    template_name = 'index.html'
    context_object_name = 'courses'


class CourseTranslatableViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseTranslatableSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
