from django.http import request

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist_app.api import serializers
from watchlist_app.models import Movie

class MovieList(APIView):

    def get(self,request):
        movies = Movie.objects.all()
        serializer = serializers.MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = serializers.MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetails(APIView):

    def get(self,request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.MovieSerializer(movie)
        return Response(serializer.data)

    def put(self,request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

    def delete(self,request,pk):
        try:
            movie = Movie.objects.get(pk=pk)
        except Movie.DoesNotExist:
            return Response({'error': 'Movie not found'}, status=status.HTTP_400_BAD_REQUEST)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)