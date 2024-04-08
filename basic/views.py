from rest_framework import generics,permissions
from .models import *
from .serializers import *

class TutorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = [permissions.IsAdminUser] 

class TutorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    permission_classes = [permissions.IsAdminUser] 

class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser] 

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser] 

# Views for Course model
class CourseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser] 

class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAdminUser] 

# Views for Level model
class LevelListCreateAPIView(generics.ListCreateAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAdminUser] 

class LevelRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer
    permission_classes = [permissions.IsAdminUser] 

# Views for Lesson model
class LessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAdminUser] 

class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAdminUser] 

# Views for Material model
class MaterialListCreateAPIView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAdminUser] 

class MaterialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    permission_classes = [permissions.IsAdminUser] 

# Views for Practice model
class PracticeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    permission_classes = [permissions.IsAdminUser] 

class PracticeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Practice.objects.all()
    serializer_class = PracticeSerializer
    permission_classes = [permissions.IsAdminUser] 

# Views for Question model
class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser] 

class QuestionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAdminUser] 

# Views for PracticeSession model
class PracticeSessionListCreateAPIView(generics.ListCreateAPIView):
    queryset = PracticeSession.objects.all()
    serializer_class = PracticeSessionSerializer
    permission_classes = [permissions.IsAdminUser] 

class PracticeSessionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PracticeSession.objects.all()
    serializer_class = PracticeSessionSerializer
    permission_classes = [permissions.IsAdminUser] 

# Views for PracticeResult model
class PracticeResultListCreateAPIView(generics.ListCreateAPIView):
    queryset = PracticeResult.objects.all()
    serializer_class = PracticeResultSerializer
    permission_classes = [permissions.IsAdminUser] 

class PracticeResultRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PracticeResult.objects.all()
    serializer_class = PracticeResultSerializer
    permission_classes = [permissions.IsAdminUser] 

# Views for StudentLesson model
class StudentLessonListCreateAPIView(generics.ListCreateAPIView):
    queryset = StudentLesson.objects.all()
    serializer_class = StudentLessonSerializer
    permission_classes = [permissions.IsAdminUser] 

class StudentLessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentLesson.objects.all()
    serializer_class = StudentLessonSerializer
    permission_classes = [permissions.IsAdminUser] 
