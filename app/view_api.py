from django.http import response
from django.http.response import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import profile
import uuid



class login_api(APIView):
    def post(self,request):
        response={}
        response['status']=500
        response['message']='something went wrong'
        try:
            check_user=User.objects.filter(username=request.data.get('email')).first()
            if check_user is None:
                response['message']='User not found'
            
            Profile=profile.objects.filter(user=check_user).first()
            if not Profile.is_varified:
                response['message']='Profile is not varified'
                return JsonResponse(response)  
            
            
            user=authenticate(username=request.data.get('email'),password=request.data.get('password'))
            if user is not None:
                login(request,user)
                response['status']=200
                response['message']='Login susscessfull'
        
        except Exception as e:
            print(e)
        
        return JsonResponse(response)
    

class register_api(APIView):
    def post(self,request):
        response={}
        response['status']=500
        response['message']='Something went wrong'
        
        try:
            data=request.data
            if User.objects.filter(username=data.get('username')).exists():
                response['message']='Username already exits'
                return JsonResponse(response)
            
            if User.objects.filter(email=data.get('email')).exists():
                response['message']='Eamil already exits'
                return JsonResponse(response)
            
            user=User.objects.create(username=data.get('username'),email=data.get('email'))
            user.set_password(data.get('password'))  
            user.save()

            token=str(uuid.uuid4())
            Profile=profile.objects.create(user=user,token=token)
            Profile.save()
            response['message']='User created'         
            response['status']=200

        except Exception as e:
            print(e)
        return JsonResponse(response)


      