from django.contrib import admin
from .models import StudentDetails,ExamDetails

class StudentDetailsAdmin(admin.ModelAdmin):
    pass

admin.site.register(StudentDetails,StudentDetailsAdmin)

class ExamDetailsAdmin(admin.ModelAdmin):
    pass

admin.site.register(ExamDetails,ExamDetailsAdmin)