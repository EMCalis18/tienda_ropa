from django.shortcuts import render

from .models import Favorites
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from applications.product.models import Product

# Create your views here.
from django.views.generic import (
    ListView,
    View,
    DeleteView
)


class RemoveFavorite(DeleteView):
    model = Favorites
    success_url = reverse_lazy('panel_app:panel-user')

class AddFavorites(LoginRequiredMixin ,View):
    login_url = reverse_lazy('users_app:login')
    def post(self, request, *args, **kwargs):
        usuario = self.request.user#para recuperar el user
        product = Product.objects.get(id=self.kwargs['pk'])#recuperar el pk

        #add el favorito        
        favorito, created =Favorites.objects.get_or_create(
            user=usuario,
            product=product,
        )
        #if created == False:
                  
        return HttpResponseRedirect(
            reverse(
            'panel_app:panel-user'
            )
        )
        




    

        

        
