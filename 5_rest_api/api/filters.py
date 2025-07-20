import django_filters
from .models import School, Classroom, Teacher, Student


class SchoolFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = School
        fields = ['name']


class ClassroomFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(field_name='school__id')

    class Meta:
        model = Classroom
        fields = ['school']


class TeacherFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(method='filter_school')
    classroom = django_filters.NumberFilter(field_name='classrooms__id')
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter()

    class Meta:
        model = Teacher
        fields = ['first_name', 'last_name', 'gender']

    def filter_school(self, queryset, name, value):
        return queryset.filter(classrooms__school__id=value).distinct()


class StudentFilter(django_filters.FilterSet):
    school = django_filters.NumberFilter(field_name='classroom__school__id')
    classroom = django_filters.NumberFilter(field_name='classroom__id')
    first_name = django_filters.CharFilter(lookup_expr='icontains')
    last_name = django_filters.CharFilter(lookup_expr='icontains')
    gender = django_filters.CharFilter()

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'gender', 'classroom', 'school']
