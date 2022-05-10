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
        # 이메일에는 @와 .이 필수로 포함되어야 합니다
        # @를 기준으로 앞에 적어도 무엇인가 하나는 있어야 하고 @를 기준으로 뒤쪽에도 적어도 1개가 있어야 하고
        #.이 있고 그 다음에 무엇인가 1개 이상 있어야 한다.
        #극단적인 이메일 a@a.a이렇게 
        #@은 무조건 1개가 있어야 한다.
        # email=(r'(\w|\W)*@{1}\w+.{1}\w*\W*',input_data["email"])



        # 비밀번호는 8자리 이상, 문자, 숫자, 특수문자의 복합이어야 합니다. 
        # regex = re.compile(r'(?=.*[@])(?=.*[.]).*')

        try:

            return JsonResponse({"message" : "SUCCESS"}, status=201)
        except:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)



