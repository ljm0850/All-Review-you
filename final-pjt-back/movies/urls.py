from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('setmovie/', views.setmovie),
    path('getmovie/', views.getmovie),
    path('best/', views.best),
]
