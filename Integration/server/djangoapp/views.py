from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Note
from .serializers import NotesSerializer
from rest_framework import status


# @api_view(['GET'])
# def getRoutes(request):
#     routes = [
#         {
#             'Endpoint': '/notes/',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns an array of notes'
#         },
#         {
#             'Endpoint': '/notes/id',
#             'method': 'GET',
#             'body': None,
#             'description': 'Returns a single note object'
#         },
#         {
#             'Endpoint': '/notes/create/',
#             'method': 'POST',
#             'body': {'body': ""},
#             'description': 'Creates new note with data sent in post request'
#         },
#         {
#             'Endpoint': '/notes/id/update/',
#             'method': 'PUT',
#             'body': {'body': ""},
#             'description': 'Creates an existing note with data sent in post request'
#         },
#         {
#             'Endpoint': '/notes/id/delete/',
#             'method': 'DELETE',
#             'body': None,
#             'description': 'Deletes and exiting note'
#         },
#     ]
#     #  return JsonResponse(routes,safe = False)
#     return Response(routes)

# @api_view(['GET'])



class getNotes(APIView):
    
    def get(self,request):
        notes = Note.objects.all() 
        print(notes,"888888")
        serializer = NotesSerializer(notes,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        
        obj = request.data
        print(obj)
        
        serializer =NotesSerializer(data= obj,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)
        
class getNote(APIView):
    def get(self,request,id):
        try:
            obj = Note.objects.get(id=id)
            
        except Note.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = NotesSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            print(id)
            print(request.data)
            obj = Note.objects.get(id=id)
            print("uuuuuuuuuuuuu",request.data.get('product_name'))
            
        except Note.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = NotesSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_205_RESET_CONTENT)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        try:
            obj = Note.objects.get(id=id)
            obj.delete()

            
        except Note.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        return Response({'msg':'deleted'},status=status.HTTP_204_NO_CONTENT)
    
    
