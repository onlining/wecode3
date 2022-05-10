from django.shortcuts import render
from django.views import View
import json
from .models import Actors,Movies,Actors_Movies
from django.http import JsonResponse

class MovieView(View):
    def get(self,request):
        results=[]
        movies=Movies.objects.all()
        for movie in movies:
            results.append({
                "제목":movie.title,
                "개봉일":movie.release_date,
                "배우목록":Actors_Movies.objects.get(movie_id=movie.id).actor.first_name+Actors_Movies.objects.get(movie_id=movie.id).actor.last_name
            })

        return JsonResponse({"products" : results}, status=200)



    def post(self,request):
        input_data=json.loads(request.body)
        movie=Movies.objects.create(
            title=input_data["title"],
            release_date=input_data["release_date"],
            running_time=input_data["running_time"]
        )
        return JsonResponse({"message" : "SUCCESS"}, status=201)

# # Create your views here.

class ActorView(View):
   
    def post(self, request):
        input_data=json.loads(request.body)
        actor=Actors.objects.create(
            first_name=input_data["first_name"],
            second_name=input_data["second_name"],
            date_of_birth=input_data["date_of_birth"]
        )
        return JsonResponse({"message" : "SUCCESS"}, status=201)

    def get(self,request):
        results=[]
        actors=Actors.objects.all()
        for actor in actors:
            results.append({
                "이름":actor.first_name,
                "이f":actor.last_name,
                "출연영화":Actors_Movies.objects.get(actor_id=actor.id).movie.title
            })

        return JsonResponse({"products" : results}, status=200)

# class Actors_MoviesView(View):
#     def get(self,request):
#         actors_movies=Actors_Movies.objects.all()
#         realactors=Actors.objects.all()
#         realmovies=Movies.objects.all()
#         for actor in realactors
#         for actor in actors:
#             results.append({
#                 actor.id
#             })
#         for actor in actors:
#             results.append({
#                 actor.id
#             })

#         return JsonResponse({"message" : "SUCCESS"}, status=201)