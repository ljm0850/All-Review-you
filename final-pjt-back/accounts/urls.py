from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile),
    path('follow/', views.follow),
    path('ranking/', views.ranking),
    
]
