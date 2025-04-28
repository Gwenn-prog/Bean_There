from rest_framework import serializers
from .models import Cafe


class CafeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cafe
        fields = '__all__'   


favorites_count = serializers.SerializerMethodField()

def get_favorites_count(self, obj):
    return obj.favorite_set.count()


is_favorited = serializers.SerializerMethodField()

def get_is_favorited(self, obj):
    request = self.context.get('request')
    if request and request.user.is_authenticated:
        return obj.favorite_set.filter(user=request.user).exists()
    return False