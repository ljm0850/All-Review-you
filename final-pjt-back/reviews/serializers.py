from asyncore import read
from .models import Review,Comment
from rest_framework import serializers
from accounts.serializers import FollowSerializer
from movies.serializers import MovieSerializer

class ReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'

class nameReviewSerializer(serializers.ModelSerializer):
    user = FollowSerializer(read_only=True)
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        

class UpdateReviewSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user',)

class ReviewListSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class UpdateCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('review','user')