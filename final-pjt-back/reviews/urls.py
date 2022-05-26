from django.urls import path
from . import views


app_name = 'reviews'

urlpatterns = [
    path('create/', views.create),
    path('detail/', views.detail),
    path('like/', views.like),
    path('index/', views.index),
    path('comment/', views.create_comment),
    path('comment/detail/', views.comment_detail),
]
