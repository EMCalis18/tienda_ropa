from django.shortcuts import render
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from django.views.generic import (
    View,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    DetailView
)

from django.views.generic.edit import (
    FormView
)

from .forms import (
    UserRegisterForm, 
    LoginForm,
    UserUpdateForm,
    UpdatePasswordForm,
)
#
from .models import User
# 
# 

class UserRegisterView(FormView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:user-lista')

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            user_name=form.cleaned_data['user_name'],
            ocupation=form.cleaned_data['ocupation'],
            genero=form.cleaned_data['genero'],
            date_birth=form.cleaned_data['date_birth'],
        )
        # enviar el codigo al email del user
        return super(UserRegisterView, self).form_valid(form)


class ClientRegisterView(FormView):
    template_name = 'users/register-cliente.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        #
        User.objects.create_client(
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            user_name=form.cleaned_data['user_name'],
            genero=form.cleaned_data['genero'],
            date_birth=form.cleaned_data['date_birth'],
        )
        # enviar el codigo al email del user
        return super(ClientRegisterView, self).form_valid(form)


class LoginUser(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('panel_app:panel-user')

    def form_valid(self, form):
        user = authenticate(#autenticate siempre min estos dos campos
            #con el autenticate se verifica que exista este usuario
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
        )
        login(self.request, user)
        return super(LoginUser, self).form_valid(form)


class LogOutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'panel_app:index'                
            )
        )


class UserUpdateView(UpdateView):
    template_name = "users/update.html"
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('panel_app:panel-user')


class UpdatePassword(LoginRequiredMixin, FormView):
    template_name = 'users/update-password.html'
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('users_app:login')
    login_url = reverse_lazy('users_app:login')

    def form_valid(self, form):
        usuario = self.request.user#para obtener el usuario en una view
        user = authenticate(  
            email=usuario.email,
            password=form.cleaned_data['password_actual'],
        )
        if user:
            new_password = form.cleaned_data['new_password']
            print(new_password)
            usuario.set_password(new_password)
            usuario.save()
        logout(self.request)
        
        return super(UpdatePassword, self).form_valid(form)

