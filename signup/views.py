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
        signups=Signup.objects.all()

        if input_data["email"] not in request.body or input_data["password"] not in request.body:
            return JsonResponse( {"message": "KEY_ERROR"}, status=400)
        
        # Signup.objects.get(email=input_data["email"]) == None:
        #     return JsonResponse({"message" : "SUCCESS"}, status=201)
        # 계정이나 패스워드 키가 전달되지 않았을 경우, {"message": "KEY_ERROR"}, status code 400 을 반환합니다.
        # try:
        #     for signup in signups:
        #         if input_data["email"] not in signup.email:
        #             return JsonResponse( {"message": "해당하는 이메일이 존재하지 않습니다."}, status=400)
        #         elif input_data["email"] in signup and :
        #             return 
                    
        #     return JsonResponse( {"message": "SUCCESS"}, status=201)
        # except NameError:
        #     return JsonResponse({"message":"계정이나 패스워드가 전달되지 않았습니다. "},status=400)
        # 계정을 잘 못 입력한 경우 {"message": "INVALID_USER"}, status code 401을 반환합니다. - 해당하는 값이 존재하지 않는다
        # 비밀번호를 잘 못 입력한 경우 {"message": "INVALID_USER"}, status code 401을 반환합니다.- 해당하는 비밀번호가 존재하지 않는다.
        # 로그인이 성공하면 {"message": "SUCCESS"}, status code 200을 반환합니다. 이메일도 맞고 비밀번호도 맞다






        # return JsonResponse({"message" : "SUCCESS"}, status=200)





