from django.db import models
from tutoring_platform.models import Student

class Course(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Level(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        blank=False
    )
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']

class Lesson(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        blank=False
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Material(models.Model):
    title = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    display = models.BooleanField(default=False)
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        blank=False
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Practice(models.Model):
    title = models.CharField(max_length=100)
    lesson = models.ForeignKey(
        Lesson, 
        on_delete=models.CASCADE,
        blank=False
    )

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class Question(models.Model):
    instruction = models.CharField(max_length=5000)
    kind = models.CharField(max_length=50)
    time_limit = models.IntegerField()
    practice = models.ForeignKey(
        Practice,
        on_delete=models.CASCADE,
        blank=False
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

class PracticeSession(models.Model):
    session_date = models.DateTimeField()
    practice = models.ForeignKey(
            Practice,
            on_delete=models.CASCADE,
            blank=False
        )
    student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE, 
        blank=False
    )
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']

class PracticeResult(models.Model):
    execution_time = models.IntegerField()
    execution_result = models.BooleanField()
    practiceSession = models.ForeignKey(
        PracticeSession,
        on_delete=models.CASCADE,
        blank=False
    )
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']


class StudentLesson(models.Model):
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        blank=False
    )
    Student = models.ForeignKey(
        Student, 
        on_delete=models.CASCADE,
        blank=False
    )

    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']