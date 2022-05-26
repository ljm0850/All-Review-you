from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
from reviews.models import Review
from .models import User
from .serializers import RankSerializer, YouUserSerializer,YouReviewsSerializer, MeReviewsSerializer, MeUserSerializer, FollowSerializer
from rest_framework import status

@api_view(['GET'])
def profile(request):
    if request.user.is_authenticated:
        you = request.GET.get("you")
        me = request.user.username
        user = get_object_or_404(User, username=you)
        user_id = user.pk
        reviews = Review.objects.filter(user=user_id)
        follow_list = User.objects.filter(followings=user_id)
        followserializer = FollowSerializer(follow_list, many=True)
        if you == me:
            userserializer = MeUserSerializer(user)
            reviewserializer = MeReviewsSerializer(reviews, many=True)
        else:
            userserializer = YouUserSerializer(user)
            reviewserializer = YouReviewsSerializer(reviews, many=True)
        print('@@@@@@@@@@')
        print(userserializer.data)
        context = {
            'data' : userserializer.data, 
            'reviews': reviewserializer.data,
            'followlist' : followserializer.data
        }
        return Response(context)
    return Response(status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def follow(request):
    username = request.data.get('username')    
    if request.user.is_authenticated:
        user = get_object_or_404(get_user_model(), username=username)
        if (request.user != username):
            if user.followers.filter(username=request.user).exists():
                user.followers.remove(request.user)
                return Response(status.HTTP_200_OK)
            else:
                user.followers.add(request.user)
                return Response(status.HTTP_200_OK) 
        return Response(status.HTTP_405_METHOD_NOT_ALLOWED)
    return Response(status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def ranking(request):
    users = get_list_or_404(User.objects.order_by("-rank_point")[:10])
    rankserializer = RankSerializer(users, many=True)
    return Response(rankserializer.data)
