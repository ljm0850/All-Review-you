from reviews.models import Review
from .models import User
from rest_framework import serializers

class FollowSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)

class YouUserSerializer(serializers.ModelSerializer):
    followers = serializers.IntegerField(source='followers.count', read_only=True)
    class Meta:
        model = User
        fields = ('username', 'rank_point', 'followings','followers')

class YouReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class MeUserSerializer(serializers.ModelSerializer):
    followers = serializers.IntegerField(source='followers.count', read_only=True)
    followings = FollowSerializer(read_only=True, many=True)
    class Meta:
        model = User
        fields = ('followers', 'username', 'first_name', 'last_name',
                    'email', 'rank_point', 'followings', 'is_superuser')

class MeReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'rank_point', 'followers')