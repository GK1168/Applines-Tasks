from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from py_etherpad import EtherpadLiteClient
from etherpad_lite import EtherpadLiteClient
from .serializer import EtharpadClassSerializer




class Etherpad_Access(APIView):
    
    def get(self,request):
        # print(request.api_key)
        api_key = 'f754bce968a3dc705fb6dc58865deca5db15689e035a487fc9e53847c7048f67'
        print(api_key)
        connect = EtherpadLiteClient(base_params={'apikey':api_key})
        connect.createPad(padID = 'check222',text="This is the first pad....!")
        data = connect.setText(padID = 'check222',text ='hii this is gopal')
        
        
        # serializer = EtharpadClassSerializer(connect,many=False)
        return Response('success',status = status.HTTP_200_OK)
    
    # api = require('etherpad-lite-client')
    # etherpad = api.connect({
    
    #     host: 'localhost',
    #     port: '9001'
            
    #     }
    # )
    # mypad = EtherpadLiteClient('EtherpadFTW','http://beta.etherpad.org/api')
    # mypad.setText('testpad','Newe Text from the python wrapper..!')


