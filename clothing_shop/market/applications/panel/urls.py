from django.urls import path

from . import views



app_name = "panel_app"

urlpatterns = [
    path(
        '', 
        views.HomePageView.as_view(),
        name='index',
    ),
    path(
        'panel/user', 
        views.HomePage.as_view(),
        name='panel-user',
    ),
]