from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import School, Classroom, Teacher, Student
from .serializers import *
from .filters import *


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SchoolFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return SchoolDetailSerializer
        return SchoolSerializer


class ClassroomViewSet(viewsets.ModelViewSet):
    queryset = Classroom.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = ClassroomFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ClassroomDetailSerializer
        return ClassroomSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TeacherFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TeacherDetailSerializer
        return TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = StudentFilter

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StudentDetailSerializer
        return StudentSerializer
