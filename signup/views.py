from django.shortcuts import render
from .models import Signup
# Create your views here.
import json
from django.views import View
from django.http import JsonResponse
import re
class SignupView(View):
    # def get(self,request):


    def post(self,request):
        input_data=json.loads(request.body)
        # email=(,input_data["email"])
        # password=(r)
        a=re.search('(\w|\W)+@{1}\w+\.(\w|\W)+', input_data["email"])
        b=re.search('^.*(?=^.{8,}$)(?=.*\d)(?=.*[a-z|A-Z|가-핳])(?=.*\W).*$',input_data["password"])
        
        print(b)
    
        if a==None and b==None:

            return JsonResponse({"message": "@과.이 포함된 이메일 형식이 필요합니다,8자리 이상, 문자, 숫자, 특수문자의 복합이어야 합니다"}, status=400)
        elif a==None:
            return JsonResponse({"message": "@과.이 포함된 이메일 형식이 필요합니다"}, status=400)
        elif b==None:
            
            return JsonResponse({"message":"8자리 이상, 문자, 숫자, 특수문자의 복합이어야 합니다"}, status=400)
        else:
            Signup.objects.create(
                email=input_data["email"],
                password=input_data["password"],
                name=input_data["name"],
                phonenumber=input_data["phonenumber"],
                personal=input_data["personal"]
            

            )
            return JsonResponse({"message" : "SUCCESS"}, status=201)

class LoginView(View):
    def post(self,request):
        input_data=json.loads(request.body)

        if input_data["email"] not in request.body or input_data["password"]not in request.body:
            return JsonResponse( {"message": "KEY_ERROR"}, status=400)
        
        # Signup.objects.get(email=input_data["email"]) == None:
        #     return JsonResponse({"message" : "SUCCESS"}, status=201)






        return JsonResponse({"message" : "SUCCESS"}, status=200)






        # 비밀번호는 8자리 이상, 문자, 숫자, 특수문자의 복합이어야 합니다. 
        # regex = re.compile(r'(?=.*[@])(?=.*[.]).*')


