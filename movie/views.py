from django.shortcuts import render
from django.views import View
import json
from .models import Actors,Movies
from django.http import JsonResponse

class MovieView(View):
    def get(self,request):
        results=[]
        movies=Movies.objects.all()
        for movie in movies:
            results.append({
                "제목":movie.title,
                "개봉일":movie.release_date,
                "상영시간":movie.running_time
            })

        return JsonResponse({"products" : results}, status=200)



#     def post(self,request):
#         input_data=json.loads(request.body)
#         movie=Movies.objects.create(
#             title=input_data["title"],
#             release_date=input_data["release_date"],
#             running_time=input_data["running_time"]
#         )
#         return JsonResponse({"message" : "SUCCESS"}, status=201)

# # Create your views here.

class ActorView(View):
    # def get(self, request):
    #     dsaf
    # def post(self, request):
    #     input_data=json.loads(request.body)
    #     actor=Actors.objects.create(
    #         first_name=input_data["first_name"],
    #         second_name=input_data["second_name"],
    #         date_of_birth=input_data["date_of_birth"]
    #     )
    #     return JsonResponse({"message" : "SUCCESS"}, status=201)

    def get(self,request):
        results=[]
        actors=Actors.objects.all()
        for actor in actors:
            results.append({
                "이름":actor.first_name,
                "이름":actor.last_name,
                "생일":actor.date_of_birth
            })
 
        return JsonResponse({"products" : results}, status=200)