from django.urls import path
from .views import ActorView,MovieView,ActorsMoviesView
urlpatterns=[
    path("movie",MovieView.as_view()),
    path("actor",ActorView.as_view()),
    path("actor_movie",ActorsMoviesView.as_view())
]
