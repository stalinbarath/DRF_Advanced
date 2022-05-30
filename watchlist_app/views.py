# from django.shortcuts import render

# from django.http import request, JsonResponse
# from .models import Movie
# # Create your views here.
# def movies(request):
#     movies = Movie.objects.all()
#     response_dict = {
#         'movies': list(movies.values())
#     }
#     return JsonResponse(response_dict)

# def movie(request, pk):
#     movie = Movie.objects.get(pk=pk)
#     response_dict = {
#         'title': movie.name,
#         'description': movie.description
#     }
#     return JsonResponse(response_dict)