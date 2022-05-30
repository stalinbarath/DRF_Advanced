from django.urls import path

from watchlist_app.api import views

urlpatterns = [
    path('list/', views.movies, name='movies'),
    path('<int:pk>', views.movie, name='movie')
]
