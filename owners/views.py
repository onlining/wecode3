from django.shortcuts import render
from .models import Owners,Dogs
import json
from django.views import View
from django.http import JsonResponse

        

        
class OwnerView(View):
    def get(self,request):
        results=[]
        owners=Owners.objects.all()
        for owner in owners:
            results.append({
                "이름":owner.name,
                "이메일":owner.email,
                "나이":owner.age
            })

        return JsonResponse({"products" : results}, status=200)



    def post(self, request):
        input_data=json.loads(request.body)
        owner=Owners.objects.create(
            name=input_data["name"],
            email=input_data["email"],
            age=input_data["age"]
        )
        return JsonResponse({"message" : "SUCCESS"}, status=201)


class DogsView(View):
    def get(self,request):
        results=[]
        dogs=Dogs.objects.all()
        owners=Owners.objects.all()
       

        # Owners.objects.get(onwers.id==dogs.owner_id)
        # owners=Owners.objects.all()
        # owners= Owners.objects.get(dogs.owner==owners.id)
        for owner in owners:
            for dog in dogs:
                if dog.owner_id==owner.id:
                    results.append({
                        "이름":dog.name,
                        "나이":dog.age,
                        "주인":owner.name
                
                })
            # select name from onwers where owners.id=dogs.owner_id
            
        return JsonResponse({"products" : results}, status=200)

    def post(self, request):
        input_data=json.loads(request.body)
        owner=Owners.objects.get(id=input_data["owner"])
        dogs=Dogs(
            name=input_data["name"],
            age=input_data["age"],
            owner=owner
        )
        dogs.save()

        return JsonResponse({"message" : "SUCCESS"}, status=201)

        

class OwnerandDogView(View):
    def get(self, request):
        results=[]
        dogs=Dogs.objects.all()
        owners=Owners.objects.all()
       

        # Owners.objects.get(onwers.id==dogs.owner_id)
        # owners=Owners.objects.all()
        # owners= Owners.objects.get(dogs.owner==owners.id)
        for owner in owners:
            for dog in dogs:
                if dog.owner_id==owner.id:
                    results.append({
                        "주인":owner.name,
                        "이메일":owner.email,
                        "주인나이":owner.age,
                        "강아지이름":dog.name,
                        "강아지나이":dog.age,
                
                })
            # select name from onwers where owners.id=dogs.owner_id
            
        return JsonResponse({"products" : results}, status=200)

        


# Create your views here.
