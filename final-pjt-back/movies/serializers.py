
from .models import Movie
from rest_framework import serializers
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title', 'poster_path', 'overview', 'release_date','pk')