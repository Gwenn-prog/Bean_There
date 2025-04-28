from rest_framework import serializers
from favorite.models import Favorite
from cafe.serializers import CafeSerializer  # Assuming you have a CafeSerializer

class FavoriteSerializer(serializers.ModelSerializer):
    cafe = CafeSerializer(read_only=True)  # Nested cafe details
    
    class Meta:
        model = Favorite
        fields = ['id', 'cafe', 'created_at']
        read_only_fields = ['id', 'created_at']

class CreateFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['cafe']  # Only need cafe ID when creating