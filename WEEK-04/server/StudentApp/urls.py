from django.urls import path


from .views import StudentDetail,StudentInfo,StudentQuery,ExamDetail

urlpatterns = [
    path('student-details/', StudentDetail.as_view() ),
    path('student-info/<int:id>', StudentInfo.as_view()),
    path('student-query/<str:student_course>', StudentQuery.as_view()),
    path('exam-details/',ExamDetail.as_view())
]