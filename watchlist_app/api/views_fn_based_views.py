from gzip import READ
from anyio import maybe_async
from django.http import request, JsonResponse
from watchlist_app.models import Movie

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.api import serializers

@api_view(['GET','POST'])
def movies(request):

    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = serializers.MovieSerializer(movies, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = serializers.MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def movie(request, pk):

    try:
        movie = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return Response({'error': 'Movie not found'}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = serializers.MovieSerializer(movie)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = serializers.MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)