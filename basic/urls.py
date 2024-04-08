from django.urls import path
from . import views

urlpatterns = [
    
    # URLs for Tutor model
    path('tutors/', views.TutorListCreateAPIView.as_view(), name='tutor-list-create'),
    path('tutors/<int:pk>/', views.TutorRetrieveUpdateDestroyAPIView.as_view(), name='tutor-detail'),
    
    # URLs for Student model
    path('students/', views.StudentListCreateAPIView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', views.StudentRetrieveUpdateDestroyAPIView.as_view(), name='student-detail'),

    # URLs for Course model
    path('course/', views.CourseListCreateAPIView.as_view(), name='course_list_create'),
    path('course/<int:pk>/', views.CourseRetrieveUpdateDestroyAPIView.as_view(), name='course_detail'),

    # URLs for Level model
    path('level/', views.LevelListCreateAPIView.as_view(), name='level_list_create'),
    path('level/<int:pk>/', views.LevelRetrieveUpdateDestroyAPIView.as_view(), name='level_detail'),

    # URLs for Lesson model
    path('lesson/', views.LessonListCreateAPIView.as_view(), name='lesson_list_create'),
    path('lesson/<int:pk>/', views.LessonRetrieveUpdateDestroyAPIView.as_view(), name='lesson_detail'),

    # URLs for Material model
    path('material/', views.MaterialListCreateAPIView.as_view(), name='material_list_create'),
    path('material/<int:pk>/', views.MaterialRetrieveUpdateDestroyAPIView.as_view(), name='material_detail'),

    # URLs for Practice model
    path('practice/', views.PracticeListCreateAPIView.as_view(), name='practice_list_create'),
    path('practice/<int:pk>/', views.PracticeRetrieveUpdateDestroyAPIView.as_view(), name='practice_detail'),

    # URLs for Question model
    path('question/', views.QuestionListCreateAPIView.as_view(), name='question_list_create'),
    path('question/<int:pk>/', views.QuestionRetrieveUpdateDestroyAPIView.as_view(), name='question_detail'),

    # URLs for PracticeSession model
    path('practice-session/', views.PracticeSessionListCreateAPIView.as_view(), name='practice_session_list_create'),
    path('practice-session/<int:pk>/', views.PracticeSessionRetrieveUpdateDestroyAPIView.as_view(), name='practice_session_detail'),

    # URLs for PracticeResult model
    path('practice-result/', views.PracticeResultListCreateAPIView.as_view(), name='practice_result_list_create'),
    path('practice-result/<int:pk>/', views.PracticeResultRetrieveUpdateDestroyAPIView.as_view(), name='practice_result_detail'),

    # URLs for StudentLesson model
    path('student-lesson/', views.StudentLessonListCreateAPIView.as_view(), name='student_lesson_list_create'),
    path('student-lesson/<int:pk>/', views.StudentLessonRetrieveUpdateDestroyAPIView.as_view(), name='student_lesson_detail'),
]
