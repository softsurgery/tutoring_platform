from rest_framework import generics
from .models import *
from .serializers import *

class TutorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class TutorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Views for Course model
class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Views for Level model
class LevelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

class LevelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer

# Views for Lesson model
class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

# Views for Material model
class MaterialListCreateAPIView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

# Views for Practice model
class PracticeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer

class PracticeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer

# Views for Question model
class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Views for PracticeSession model
class PracticeSessionListCreateAPIView(generics.ListCreateAPIView):
    queryset = PracticeSession.objects.all()
    serializer_class = PracticeSessionSerializer

class PracticeSessionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PracticeSession.objects.all()
    serializer_class = PracticeSessionSerializer

# Views for PracticeResult model
class PracticeResultListCreateAPIView(generics.ListCreateAPIView):
    queryset = PracticeResult.objects.all()
    serializer_class = PracticeResultSerializer

class PracticeResultRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PracticeResult.objects.all()
    serializer_class = PracticeResultSerializer

# Views for StudentLesson model
class StudentLessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = StudentLesson.objects.all()
    serializer_class = StudentLessonSerializer

class StudentLessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentLesson.objects.all()
    serializer_class = StudentLessonSerializer
