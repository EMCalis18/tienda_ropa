from django.urls import path

from . import views

app_name = "users_app"

urlpatterns = [
    path(
        'register/client', 
        views.ClientRegisterView.as_view(),
        name='register-cliente',
    ),
    path(
        'login/client', 
        views.LoginUser.as_view(),
        name='login',
    ),
    path(
        'logout/client', 
        views.LogOutView.as_view(),
        name='log-out',
    ),
    path(
        'update/client/<pk>/', 
        views.UserUpdateView.as_view(),
        name='update-client',
    ),
    path(
        'users/update-password/<pk>/', 
        views.UpdatePassword.as_view(),
        name='user-update_password',
    ),
    
]