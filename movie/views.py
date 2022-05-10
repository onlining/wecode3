from django.shortcuts import render
from django.views import View
import json
from .models import Actors,Movies,Actors_Movies
from django.http import JsonResponse
from collections import defaultdict
class MovieView(View):
    def get(self,request):
        results=[]
        movies=Movies.objects.all()
        actors=Actors.objects.all()
        sss=Actors_Movies.objects.all()
      
        # c=defaultdict(list)
        

       
      

            
            # else:
            #     a.append(Actors_Movies.objects.get(movie_id=movie.id).actor.first_name+Actors_Movies.objects.get(movie_id=movie.id).actor.last_name)
            #     return a
        
        for movie in movies:
            
            
            a=[]
            for actor in actors:
                
                if Actors_Movies.objects.filter(movie_id=movie.id) != None:
                    
                    b=Actors_Movies.objects.filter(movie_id=movie.id).values()
                    
                    for i in b:
                        if i['actor_id']==actor.id:
                            a.append(actor.last_name)
                    
                            
                            
                                 
            results.append({
                "제목":movie.title,
                "개봉일":movie.release_date,
                        
                        "배우목록":a
                        })

                    # if Actors_Movies.objects.filter(movie_id=movie.id).actor_id==actor.id:
               
          

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
            last_name=input_data["second_name"],
            date_of_birth=input_data["date_of_birth"]
        )
        return JsonResponse({"message" : "SUCCESS"}, status=201)

    def get(self,request):
        results=[]
        actors=Actors.objects.all()
        movies=Movies.objects.all()



       
        for actor in actors:
            
            b=[]
            for movie in movies:
                if Actors_Movies.objects.filter(actor_id=actor.id) != None:
                    c=Actors_Movies.objects.filter(actor_id=actor.id).values()
                    for i in c:
                        if i['movie_id']==movie.id:
                            b.append(movie.title)
            results.append({
                "이름":actor.first_name,
                "이f":actor.last_name,
                "출연영화":b
            })

        return JsonResponse({"products" : results}, status=200)

class ActorsMoviesView(View):
    def post(self,request):
        input_data=json.loads(request.body)
        # a=input_data["first_name"]+input_data["second_name"]
        realactors=Actors.objects.get(last_name=input_data["second_name"]).id
        realmovies=Movies.objects.get(title=input_data["movie"]).id
        Actors_Movies.objects.create(
            actor_id=realactors,
            movie_id=realmovies

        )
        



        return JsonResponse({"message" : "SUCCESS"}, status=201)