from django.db import models

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