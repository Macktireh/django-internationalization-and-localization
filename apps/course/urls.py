from django.urls import path

from apps.course.views import ListCourse, CourseTranslatableViewSet, CourseViewSet, NewsViewSet

urlpatterns = [
    path('', ListCourse.as_view()),
    path('api/all/', CourseTranslatableViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('api/', CourseViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
    path('news/', NewsViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update', 'delete': 'destroy'})),
]
