from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('schools', SchoolViewSet)
router.register('classrooms', ClassroomViewSet)
router.register('teachers', TeacherViewSet)
router.register('students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
