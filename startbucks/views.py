from django.shortcuts import render

# Create your views here.
import json
from django.views import View
from django.http import JsonResponse

from .models import Menu,Allergen,DrinkAllergies,DrinkCategories,DrinkImages,DrinkNutritions,Drinks

class MenuView(View):
    def post(self,request):
        input_data=json.loads(request.body)
        menu=Menu.objects.create(
            name=input_data["name"]
        )
        return JsonResponse({"message" : "SUCCESS"}, status=201)
    # def get(self,request):


class DrinkCategoriesView(View):
    def post(self,request):
        input_data=json.loads(request.body)
        DrinkCategories.objects.create(
            menu_id=Menu.objects.get(name=input_data["menu"]).id,
            name=input_data["name"]
        )
        return JsonResponse({"message" : "SUCCESS"}, status=201)
class DrinksView(View):
    def post(self,request):
        input_data=json.loads(request.body)

        drink = Drinks.objects.create(
            name=input_data["name"],
            category_id=DrinkCategories.objects.get(name=input_data["category"]).id,
            is_new=input_data["is_new"],
            description=input_data["description"]            
        )

        DrinkNutritions.objects.create(
            drink_id=drink.id,
            kcal=input_data["kcal"],
            sugar=input_data["sugar"],
            protein=input_data["protein"],
            sodium=input_data["sodium"],
            fat=input_data["fat"],
            caffeine=input_data["caffeine"]
        )

        return JsonResponse({"message" : "SUCCESS"}, status=201)

    def get(self, request):
        # 음료를 가져오는데 영양소도 다 가져오고 알러지도 가져오고, 원래 음료도 가져오고
        results=[]
        
        drinks=Drinks.objects.all()
        # allergies=.objects.all()
        nutrients=DrinkNutritions.objects.all()
        
        for drink in drinks:
            allergy=[]
            a=DrinkNutritions.objects.get(drink_id=drink.id)
            nutrient=[]
           
            [allergy.append(angry.name) for angry in drink.allergen_set.all()]
            
               
            nutrient.append({
                    # a.kcal,a.sugar,a.protein,a.fat,a.caffeine

                    "칼로리":a.kcal,
                    "설탕":a.sugar,
                    "단백질":a.protein,
                    "소디움": a.sodium,
                    "지방":a.fat,
                    "카페인":a.caffeine


                })
            results.append({
                "이름":drink.name,
                "묘사":drink.description,
                '신상여부':drink.is_new,
                '영양소': nutrient,
                '알러지': allergy

            })
        return JsonResponse({"message" : results}, status=201)

class AllergieView(View):
    def post(self, request):
        input_data=json.loads(request.body)
        allergy = Allergen.objects.create(
            name=input_data["name"]
        )
        return JsonResponse({"message" : "SUCCESS"}, status=201)

class DrinkAllergiesView(View):
    def post(self, request):
        input_data=json.loads(request.body)
        a= Allergen.objects.get(name=input_data["allergen"]).id
        b=drink=Drinks.objects.get(name=input_data["drink"]).id
        DrinkAllergies.objects.create(
        drink_id=b,
        allergen_id=a,
        extraprice=input_data["extraprice"],


        )
        return JsonResponse({"message" : "SUCCESS"}, status=201)
    

# Create your views here.
