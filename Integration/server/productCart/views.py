from django.shortcuts import render
# from django.http import JsonResponse
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import productDetails
from .serializers import ProductDetailsSerializer
from rest_framework import status
from django.db.models import Q


class getProdDetails(APIView):
    
    def get(self,request):
        obj = productDetails.objects.all()
        serializer = ProductDetailsSerializer(obj,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        obj = productDetails()
        print(obj,request.data)
        obj.product_name = request.data['product_name']
        obj.product_qty = request.data['product_qty']
        obj.product_price = request.data['product_price']
        obj.total_price = obj.product_qty*obj.product_price
        obj.save()
        print(obj)
        return Response("success",status = status.HTTP_201_CREATED)
        
class getProdDet(APIView):
    def get(self,request,id):
        try:
            obj = productDetails.objects.get(id=id)
            
        except productDetails.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductDetailsSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            obj = productDetails.objects.get(id=id)
            print(obj,request.data)
            updatedProduct ={}
            updatedProduct['product_name'] = request.data['product_name']
            updatedProduct['product_qty'] = request.data['product_qty']
            updatedProduct['product_price'] = request.data['product_price']
            
            
            updatedProduct['total_price'] = (request.data['product_qty'])*(request.data['product_price'])
            
            # data.save()
            print(updatedProduct,"obhh565")
            # data = data.hi
            serializer = ProductDetailsSerializer(obj,data=updatedProduct)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status = status.HTTP_205_RESET_CONTENT)
            else:
                return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
            
        except productDetails.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        
        
    def delete(self,request,id):
        try:
            obj = productDetails.objects.get(id=id)
            obj.delete()

            
        except productDetails.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        return Response({'msg':'deleted'},status=status.HTTP_204_NO_CONTENT)
    
class SearchProducts(APIView):
    def get(self,request,name):
        obj = productDetails.objects.filter(Q(product_name__icontains = name))
        serializer = ProductDetailsSerializer(obj,many = True)
        return Response(serializer.data)
    
    
class ChangeQuantity(APIView):
    def get(self,request):
        obj = productDetails.objects.all()
        serializer = ProductDetailsSerializer(obj,many=True)
        return Response(serializer.data)
    
    
    def put(self,request,id,operand):
        try:
            obj = productDetails.objects.get(id=id)
            print(obj,request.data)
            updatedProduct ={}
            updatedProduct['product_name'] = request.data['product_name']
            
            if(operand == 'inc'):
                updatedProduct['product_qty'] = request.data['product_qty'] + 1
            elif(operand == 'dec'):
                if(request.data['product_qty'] <= 0):
                    updatedProduct['product_qty'] = 0
                else:
                    updatedProduct['product_qty'] = request.data['product_qty'] -  1
            
            else:
                updatedProduct['product_qty'] = request.data['product_qty']
            
            updatedProduct['product_price'] = request.data['product_price']
            
            
            updatedProduct['total_price'] = (updatedProduct['product_qty'])*(request.data['product_price'])
            
            # data.save()
            print(updatedProduct,"obhh565")
            # data = data.hi
            serializer = ProductDetailsSerializer(obj,data=updatedProduct)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status = status.HTTP_205_RESET_CONTENT)
            else:
                return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
            
        except productDetails.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
class ChangeContent(APIView):
    def get(self,request):
        obj = productDetails.objects.all()
        serializer = ProductDetailsSerializer(obj,many=True)
        return Response(serializer.data)
    
    def put(self,request,id):
        try:
            obj = productDetails.objects.get(id = id)
            edit_content = {}
            edit_content['product_price'] = obj.product_price
            edit_content['product_qty'] = obj.product_qty
            edit_content['total_price'] = obj.total_price
            edit_content['product_name'] = request.data['product_name']
        except productDetails.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductDetailsSerializer(obj,data = edit_content)
            
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_205_RESET_CONTENT)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        try:
            obj = productDetails.objects.get(id=id)
            obj.delete()

            
        except productDetails.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        return Response({'msg':'deleted'},status=status.HTTP_204_NO_CONTENT)
            
            
