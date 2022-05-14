from django.urls import path

from .views import OwnerView,DogsView,OwnerandDogView

urlpatterns=[
    path("owners",OwnerView.as_view()),
    path("dogs",DogsView.as_view()),
    path("ownersdogs",OwnerandDogView.as_view())
]