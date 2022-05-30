from django.urls import path

from watchlist_app.api import views
urlpatterns = [
    path('list/', views.MovieList.as_view(), name='movies'),
    path('<int:pk>', views.MovieDetails.as_view(), name='movie')
]

# For function-based views:
# from watchlist_app.api import views
# urlpatterns = [
#     path('list/', views.movies, name='movies'),
#     path('<int:pk>', views.movie, name='movie')
# ]
