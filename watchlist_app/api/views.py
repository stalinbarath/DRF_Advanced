from gzip import READ
from anyio import maybe_async
from django.http import request, JsonResponse
from watchlist_app.models import Movie

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
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET','PUT','DELETE'])
def movie(request, pk):

    if request.method == 'GET':
        movie = Movie.objects.get(pk=pk)
        serializer = serializers.MovieSerializer(movie)
        return Response(serializer.data)

    if request.method == 'PUT':
        movie = Movie.objects.get(pk=pk)
        serializer = serializers.MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        movie = Movie.objects.get(pk=pk)
        movie.delete()
        return Response(status=200)