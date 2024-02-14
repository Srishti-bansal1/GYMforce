from django.shortcuts import render

# Create your views here.
from GYMapp.models import EMmodel

from rest_framework import viewsets ,status
from rest_framework.response import Response
from rest_framework.decorators import action ,api_view
from rest_framework_simplejwt.tokens import RefreshToken
from GYMapp.serializers import  EMSerializer, LoginSerializer ,TokenSerializer
#from GYMapp.serializers import CustomTokenObtainPairSerializer
#from rest_framework_simplejwt.views import TokenObtainPairView
import jwt
from django.conf import settings


class EMViewSet(viewsets.ModelViewSet):
    queryset = EMmodel.objects.all()
    serializer_class = EMSerializer

    @action(detail=False, methods=["GET"],url_path='show')
    def getCustom(self, request):
        queryset = EMmodel.objects.all()
        serializer = EMSerializer(queryset,many=True) 
        return Response(serializer.data)
    
    @action(detail=True, methods=["GET"],url_path='one_display') 
    def retriveCustom(self, request,pk=None):
        queryset = EMmodel.objects.get(pk=pk)
        serializer = EMSerializer(queryset) 
        return Response(serializer.data)
    
    @action(detail=False, methods=["POST"],url_path='create')
    def created(self, request):
        dataReceived = request.data 
        serializer = EMSerializer(data = request.data)

        if EMmodel.objects.filter(**dataReceived).exists():
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        if serializer.is_valid():
            serializer.save()
            serializer_data = serializer.data
            return Response(serializer_data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
    @action(detail=True , methods=['PUT'],url_path='modify')
    def modify(self,request,pk=None):
        EDMS = EMmodel.objects.get(pk=pk)
        serializer = EMSerializer(instance = EDMS,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
    @action(detail=True , methods=['DELETE'],url_path='delete')
    def remove(self,request,pk=None):
        EDMS = EMmodel.objects.get(pk=pk)  
        EDMS.delete()
        return Response({'message':'data is delete'})
    
    @action(detail=False , methods=['DELETE'],url_path='delete_all')
    def remove_all(self,request):
        EMmodel.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class LogViewSet(viewsets.ModelViewSet):  
    @action(detail=False, methods=["GET"],url_path='get_user')
    def getCustom(self, request):
        Username = request.GET.get('username')
        Password = request.GET.get('password')
                
        queryset = EMmodel.objects.get(username=Username)
        serializer = LoginSerializer(queryset)
        
        _password= serializer.data.get('password')
        
        if _password == Password:
            _refresh = RefreshToken()
            #_refresh.payload = {"a": "b"}
            token = _refresh.for_user(queryset)
            return Response({"refresh": str(token), "access": str(token.access_token)}) 
        return Response(status=status.HTTP_401_UNAUTHORIZED)
   
   
class customToken(viewsets.ModelViewSet):
    @action(detail=False, methods=["GET"],url_path='cust_token')
    def Custom_token(self, request):
        Username = request.GET.get('username')
        Password = request.GET.get('password')
                
        queryset = EMmodel.objects.get(username=Username)
        serializer = LoginSerializer(queryset)
        
        _password= serializer.data.get('password')
        
        serializer_data = TokenSerializer(queryset)
    
        
        if _password == Password:
            token = jwt.encode(serializer_data.data,settings.JWT_SECRET_KEY, algorithm="HS256")
            return Response({"access": token})
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])   
def SignUp(request):
    return render(request,'signup.html', {'signUp': SignUp})


@api_view(['GET'])   
def Login(request):
    return render(request,'login.html', {'login': Login})

'''class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()
    @action(detail=False, methods=["GET"],url_path='get_token')
    def getCustom(self, request):
        return True
    
    def get_extra_actions():
        return []'''  #commented code explore after some time