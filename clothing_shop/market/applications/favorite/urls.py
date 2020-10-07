from django.urls import path

from . import views

app_name = "favorites_app"

urlpatterns = [
    path(
        'add-favoritos/<pk>/', 
        views.AddFavorites.as_view(),
        name='add-favorites',
    ),
    path(
        'remove-favoritos/<pk>/', 
        views.RemoveFavorite.as_view(),
        name='remove-favorito',
    ),
]