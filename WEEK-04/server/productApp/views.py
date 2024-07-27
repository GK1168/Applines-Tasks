from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import ProductsList
from .serializer import ProductsListOneSerializer, ProductsListSerializer
from datetime import datetime,timedelta
import calendar
from etherpad_lite import EtherpadLiteClient

class ProductList(APIView):
    def get(self,request):
        obj = ProductsList.objects.all()
        serializer = ProductsListSerializer(obj,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)
    
    def post(self,request):
        
        obj = request.data
        
        serializer = ProductsListSerializer(data= obj,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)
        
        
       
class ProductInfo(APIView):
    def get(self,request,id):
        try:
            obj = ProductsList.objects.get(id=id)
            
        except ProductsList.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductsListSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    # def post(self,request,id):
    #     try:
    #         obj = ProductsList.objects.get(id=id)
            
    #     except ProductsList.DoesNotExist:
    #         msg ={'msg':'not found'}
    #         return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
    #     serializer = ProductsListSerializer(data=request.data)
    #     return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            print(id)
            print(request.data)
            obj = ProductsList.objects.get(id=id)
            print("uuuuuuuuuuuuu",request.data.get('product_name'))
            
        except ProductsList.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductsListSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_205_RESET_CONTENT)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    def patch(self,request,id):
        try:
            obj = ProductsList.objects.get(id=id)
            
        except ProductsList.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductsListSerializer(obj,data=request.data,partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data,status = status.HTTP_205_RESET_CONTENT)
        
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,id):
        try:
            obj = ProductsList.objects.get(id=id)
            obj.delete()

            
        except ProductsList.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        return Response({'msg':'deleted'},status=status.HTTP_204_NO_CONTENT)
        
    
    
class ProductQuery(APIView):
    
    def get(self,request,value):
        try:
            if(value == 'fav'):
                obj = ProductsList.objects.filter(favourites = 1)
            elif(value == 'arch'):
                obj = ProductsList.objects.filter(archive = 1)
            
            # print(obj)
        except ProductsList.DoesNotExist:
            msg = {'msg' : 'not found'}
            return Response(msg,status = status.HTTP_404_NOT_FOUND)
        
        serializer = ProductsListSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ProductFilter(APIView):
    def get(self,request,name,price):
        try:
            obj = ProductsList.objects.filter(product_name = name,price__gte = price)
            print(obj)
            
        except ProductsList.DoesNotExist:
            msg = {'msg' : 'not found'}
            return Response(msg,status = status.HTTP_404_NOT_FOUND)
        
        serializer = ProductsListSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class FetchProducts(APIView):
    def post(self,request):
        try:
            startdate = datetime.today()

            if(request.data['edate'] == 'thisweekdate'):
                enddate = startdate + timedelta(days = -(startdate.weekday() ))
                print(f"start date : {startdate} - enddate : {enddate}")
                obj = ProductsList.objects.filter(date_time__range=[enddate,startdate])
            elif(request.data['edate'] == 'lastweekdate'):
                startdate = startdate + timedelta(days = -(startdate.weekday()+1))
                enddate = startdate + timedelta(days = -(startdate.weekday() ))
                print(f"start date : {startdate} - enddate : {enddate}")
                obj = ProductsList.objects.filter(date_time__range=[enddate,startdate])
            elif(request.data['edate'] == 'lastmonthdate'):
                startdate = startdate.replace(day=1) + timedelta(days=-1)
                month_range = calendar.monthrange(startdate.year,startdate.month)[1]
                enddate = startdate + timedelta(days=-month_range+1)
                print(f"start date : {startdate} - enddate : {enddate} - monthrange : {month_range}")
                obj = ProductsList.objects.filter(date_time__range=[enddate,startdate])
            elif(request.data['edate'] == 'thismonthdate'):
                startdate = startdate.replace(day=1)
                month_range = calendar.monthrange(startdate.year,startdate.month)[1]
                enddate = startdate + timedelta(days=month_range-1)
                print(f"start date : {startdate} - enddate : {enddate} - monthrange : {month_range}")
                obj = ProductsList.objects.filter(date_time__range=[startdate,enddate])
            else:
                raise NameError(request.data['edate'])
        
            # print(obj)
            serializer = ProductsListSerializer(obj,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        
        except NameError as e:
            print(e)
            
class Etherpad_Access(APIView):
    
    
    def patch(self,request):
        try:
            obj = ProductsList.objects.get(id=request.data['product_id'])
            print(obj,obj.product_description)
            request.data['product_id'] = 'prod111'
            api_key = 'f754bce968a3dc705fb6dc58865deca5db15689e035a487fc9e53847c7048f67'
            print(api_key)
            connect = EtherpadLiteClient(base_params={'apikey':api_key})
            connect.createPad(padID = request.data['product_id'],text="This is the first pad....!")
            connect.setText(padID = request.data['product_id'],text =request.data['product_description'])
            obj.product_description = connect.getText(padID = request.data['product_id'])['text'].replace("\n","")
            # obj.save()
            d = {'product_description':obj.product_description}
            print(connect.getText(padID = request.data['product_id']))
            print(obj.product_description)
            print(obj)
            connect.deletePad(padID = request.data['product_id'])
            
        except ProductsList.DoesNotExist:
            msg ={'msg':'not found'}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = ProductsListSerializer(obj,data = d,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
        # print(request.api_key)
        
        
    def post(self,request):
        
        obj = request.data
        api_key = 'f754bce968a3dc705fb6dc58865deca5db15689e035a487fc9e53847c7048f67'
        print(obj,api_key)
        pad_id = obj['product_name']
        connect = EtherpadLiteClient(base_params={'apikey':api_key})
        connect.createPad(padID = pad_id, text= "Hii this is my first pad...")
        connect.setText(padID = pad_id,text=obj['product_description'])
        obj['product_description'] = connect.getText(padID = pad_id)['text']
        connect.deletePad(padID = pad_id)
        serializer = ProductsListSerializer(data = obj,many = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

       
        
        
        
    

        