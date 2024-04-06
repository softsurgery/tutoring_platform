from rest_framework import serializers
from .models import Course, Level, Lesson, Material, Practice, Question, PracticeSession, PracticeResult, StudentLesson

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'

class PracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practice
        fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'

class PracticeSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeSession
        fields = '__all__'

class PracticeResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeResult
        fields = '__all__'

class StudentLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentLesson
        fields = '__all__'
