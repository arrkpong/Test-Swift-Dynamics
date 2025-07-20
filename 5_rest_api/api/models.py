from django.db import models


class School(models.Model):
    name = models.CharField("ชื่อโรงเรียน", max_length=255)
    short_name = models.CharField("ตัวย่อชื่อโรงเรียน", max_length=100)
    address = models.TextField("ที่อยู่")

    class Meta:
        verbose_name = "โรงเรียน"
        verbose_name_plural = "โรงเรียน"

    def __str__(self):
        return self.name


class Classroom(models.Model):
    year = models.PositiveIntegerField("ชั้นปี")
    section = models.CharField("ทับ", max_length=10)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classrooms', verbose_name="โรงเรียน")

    class Meta:
        verbose_name = "ห้องเรียน"
        verbose_name_plural = "ห้องเรียน"

    def __str__(self):
        return f"{self.year}/{self.section}"


class Teacher(models.Model):
    GENDER_CHOICES = [('M', 'ชาย'), ('F', 'หญิง')]

    first_name = models.CharField("ชื่อ", max_length=100)
    last_name = models.CharField("นามสกุล", max_length=100)
    gender = models.CharField("เพศ", max_length=1, choices=GENDER_CHOICES)
    classrooms = models.ManyToManyField(Classroom, related_name='teachers', verbose_name="ห้องเรียนที่สอน")

    class Meta:
        verbose_name = "ครู"
        verbose_name_plural = "ครู"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Student(models.Model):
    GENDER_CHOICES = [('M', 'ชาย'), ('F', 'หญิง')]

    first_name = models.CharField("ชื่อ", max_length=100)
    last_name = models.CharField("นามสกุล", max_length=100)
    gender = models.CharField("เพศ", max_length=1, choices=GENDER_CHOICES)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students', verbose_name="ห้องเรียน")

    class Meta:
        verbose_name = "นักเรียน"
        verbose_name_plural = "นักเรียน"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
