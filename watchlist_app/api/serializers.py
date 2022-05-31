from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

    # Field level validation
    def validate_description(self,value):
        if not 'lokesh' in value.lower():
            raise serializers.ValidationError('Not a Lokesh Kanagaraj Film')
        return value
    
    def validate_name(self,value):
        if len(value) <= 1:
            raise serializers.ValidationError('Movie name is too short. Include year to increase length.')
        return value

    # Object level validation
    def validate(self,value):
        if value['name'] == value['description']:
            raise serializers.ValidationError('Description shouldn\'t be identical to Movie name.')
        return value