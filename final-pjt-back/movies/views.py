
from django.shortcuts import get_list_or_404
import requests
import random

from .models import Movie
from accounts.models import User
from reviews.models import Review
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import MovieSerializer
from rest_framework import status

@api_view(['POST'])
def setmovie(request):
    if request.user.is_superuser :
        page = request.data.get("page")

        SET_PARAM = {'api_key' : 'ea7d9cdc4bf52e1cef1da35e207d3eee', 'language' : 'ko', 'region' : 'KR', "page" : page}
        temp = requests.get('https://api.themoviedb.org/3/movie/popular', params = SET_PARAM)
        mov = temp.json()

        for mdata in mov["results"]:
            data = {"title": mdata["title"], "overview": mdata["overview"], "poster_path": mdata["poster_path"], "release_date": mdata["release_date"]}
            serializer = MovieSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
        return Response(status.HTTP_201_CREATED)
    return Response(status.HTTP_401_UNAUTHORIZED)
    

@api_view(['GET'])
def getmovie(request):
    movies = get_list_or_404(Movie)
    selectedmovies = random.sample(movies, 10)
    serializer = MovieSerializer(selectedmovies, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def best(request):
    top = User.objects.order_by("-rank_point")[0]
    reviews = top.review_set.order_by("-point")
    mlist = []
    for review in reviews:
        movie = review.movie
        if not movie in mlist:
            mlist.append(movie)
    mlist = mlist[0:10]
    serializer = MovieSerializer(mlist, many=True)
    return Response(serializer.data)


