from django.urls import path

from .views import MenuView,DrinkCategoriesView,DrinksView,AllergieView,DrinkAllergiesView
# DrinksView

urlpatterns=[
    path("menu",MenuView.as_view()),
    path("drinkcategories",DrinkCategoriesView.as_view()),
    path("drink",DrinksView.as_view()),
    path("allergy",AllergieView.as_view()),
    path("allergydrink",DrinkAllergiesView.as_view()),
    
    
] 