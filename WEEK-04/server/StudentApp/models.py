from django.db import models

# Create your models here.from django.db import models

class StudentDetails(models.Model):
    student_id = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    course = models.CharField(max_length=10)

    
    def __str__(self):
        return f"id: {self.student_id} +--+ first name: {self.first_name} +--+ last_name: {self.last_name} +--+ email: {self.email} +--+ course: {self.course}"
    

class ExamDetails(models.Model):
    student_id=models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
    subject = models.CharField(max_length=15)
    exam_date = models.DateField(auto_now=True)
    max_score = models.IntegerField(default=93)
    actual_score = models.IntegerField(blank=False,null=False)
    percentage = models.IntegerField()
    grade = models.BooleanField(default=True)
    
    
    def __str__(self):
        return f"id: {self.student_id} +--+ subject: {self.subject} +--+ exam_date: {self.exam_date} +--+ max_score: {self.max_score} +--+ actual_score: {self.actual_score} +--+ percentage: {self.percentage} +--+ grade : {self.grade}"
    