from rest_framework import serializers
from .models import School, Classroom, Teacher, Student


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'


class SchoolDetailSerializer(serializers.ModelSerializer):
    classroom_count = serializers.IntegerField(source='classrooms.count', read_only=True)
    teacher_count = serializers.SerializerMethodField()
    student_count = serializers.SerializerMethodField()

    class Meta:
        model = School
        fields = ['id', 'name', 'short_name', 'address', 'classroom_count', 'teacher_count', 'student_count']

    def get_teacher_count(self, obj):
        return Teacher.objects.filter(classrooms__school=obj).distinct().count()

    def get_student_count(self, obj):
        return Student.objects.filter(classroom__school=obj).count()


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = '__all__'


class ClassroomDetailSerializer(serializers.ModelSerializer):
    teachers = serializers.StringRelatedField(many=True)
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = Classroom
        fields = ['id', 'year', 'section', 'school', 'teachers', 'students']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherDetailSerializer(serializers.ModelSerializer):
    classrooms = serializers.StringRelatedField(many=True)

    class Meta:
        model = Teacher
        fields = ['id', 'first_name', 'last_name', 'gender', 'classrooms']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class StudentDetailSerializer(serializers.ModelSerializer):
    classroom = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'gender', 'classroom']
