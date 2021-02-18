from django.urls import path 

from . import views

urlpatterns = [
    path('', views.index),
    path('guess', views.check_guess),
    path('game', views.game)
]