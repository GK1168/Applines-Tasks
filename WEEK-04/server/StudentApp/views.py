from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import StudentDetails,ExamDetails
from .Serializer import StudentDetailsSerializer,ExamDetailsSerializer

class StudentDetail(APIView):
    def get(self,request):
        obj = StudentDetails.objects.all()
        serializer = StudentDetailsSerializer(obj,many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    def post(self,request):
        
        obj = request.data
        
        serializer = StudentDetailsSerializer(data= obj,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)
        
        
class StudentInfo(APIView):
    def get(self,request,id):
        try:
            obj = StudentDetails.objects.get(id = id)
            
        except StudentDetails.DoesNotExist:
            msg = {'msg' : 'not found'}
            return Response(msg,status = status.HTTP_404_NOT_FOUND)
        
        serializer = StudentDetailsSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    def put(self,request,id):
        try:
            obj = StudentDetails.objects.get(id = id)
            
        except StudentDetails.DoesNotExist:
            msg = {'msg' : 'not found'}
            return Response(msg,status = status.HTTP_404_NOT_FOUND)
        
        serializer = StudentDetailsSerializer(obj,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_205_RESET_CONTENT)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        
    def patch(self,request,id):
        try:
            obj = StudentDetails.objects.get(id = id)
            
        except StudentDetails.DoesNotExist:
            msg = {'msg' : 'not found'}
            return Response(msg,status = status.HTTP_404_NOT_FOUND)
        
        serializer = StudentDetailsSerializer(obj,data = request.data,partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_205_RESET_CONTENT)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
        
    def delete(self,request,id):
        try:
            obj = StudentDetails.objects.get(id = id)
            obj.delete()
            
        except StudentDetails.DoesNotExist:
            msg = {'msg' : 'not found'}
            return Response(msg, status = status.HTTP_404_NOT_FOUND)
        
        return Response({'msg':'deleted'},status = status.HTTP_204_NO_CONTENT)
    
    
class StudentQuery(APIView):
    def get(self,request,student_course):
        
        try:
            
            # student_course = request.data['course']
            obj = StudentDetails.objects.filter(course = student_course)
            
        except StudentDetails.DoesNotExist:
            msg = {'msg' : 'not found'}
            return Response(msg,status = status.HTTP_404_NOT_FOUND)
        
        serializer = StudentDetailsSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
            
class ExamDetail(APIView):
    
    def get(self,request):
        try:
            obj = ExamDetails.objects.filter(percentage__gte = 50)
        
        except ExamDetails.DoesNotExist:
            msg = {'msg' : 'not found'}
            return Response(msg,status = status.HTTP_404_NOT_FOUND)
        
        serializer = ExamDetailsSerializer(obj,many = True)
        return Response(data = serializer.data,status = status.HTTP_200_OK)
    
    def post(self,request):
        a = ExamDetails()
        
        print(a.max_score,"maxscoreeeee")
        A_Score = request.data['actual_score']
        
        a.actual_score = A_Score
        a.student_id = StudentDetails.objects.get(student_id=request.data.get('student_id'))
        a.subject = request.data['subject']
        a.percentage = int((a.actual_score/a.max_score)*100)
        if(a.percentage < 50):
            a.grade = 0 
        a.save()
        
        return Response("success",status = status.HTTP_201_CREATED)
        
        # obj = {}
        # obj['student_id'] = request.data['student_id']
        # obj['subject'] = request.data['subject']
        # obj['exam_date'] = request.data['exam_date']
        # obj['actual_score'] = request.data['actual_score']
        # obj['percentage'] = int((request.data['actual_score']/request.data['max_score'])*100)
        # if(obj['percentage'] < 50):
        #     obj['grade'] = 0
        # print(obj)
        # serializer = ExamDetailsSerializer(obj,many=True)
        # if(serializer.is_valid()):
        #     serializer.save()
        #     return Response(serializer.data,status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)
        
        
        
    
             
