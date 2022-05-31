from wsgiref.validate import validator
from rest_framework import serializers
from watchlist_app.models import Movie

def check_movie_length(value):
    if len(value) <= 1:
        raise serializers.ValidationError('Movie name is too short. Include year to increase length.')
    return value

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[check_movie_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    # Field level validation
    def validate_description(self,value):
        if not 'lokesh' in value.lower():
            raise serializers.ValidationError('Not a Lokesh Kanagaraj Film')
        return value

    # Object level validation
    def validate(self,value):
        if value['name'] == value['description']:
            raise serializers.ValidationError('Description shouldn\'t be identical to Movie name.')
        return value