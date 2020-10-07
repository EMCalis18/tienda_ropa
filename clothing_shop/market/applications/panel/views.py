from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

from applications.favorite.models import Favorites
from applications.product.models import Product
from applications.users.models import User
from applications.users.forms import UserUpdateForm, UpdatePasswordForm
# Create your views here.
from django.views.generic import (
    TemplateView,
)



class HomePageView(TemplateView):
    template_name = "panel/index.html"

    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        #new products in list home
        context['productos'] = Product.objects.list_product_new()
        context['productos_oferta'] = Product.objects.offer_list()
        return context



class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "panel/panel-client.html"
    login_url = reverse_lazy('users_app:login')
    
    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(HomePage, self).get_context_data(**kwargs)
        #new products in list home
        context['favorites'] = Favorites.objects.favoritos_user(user)
        return context

    
"""def post(self, request, *args, **kwargs):
        user = self.request.user
        form = UserUpdateForm()

        if form.is_valid():
            form.save()
            return redirect(reverse('users_app:login'))
        else:
            context = self.get_context_data()
            context['usuario'] = User.objects.favoritos_user(user, editable=True)
            return render(request, self.template_name, context)

        return self.get(request)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        store_id = self.kwargs['store']
        store = get_object_or_404(Store, pk=store_id)

        data = {
            'name': store.name,
            'description': store.description,
            'address': store.address,
            'geo_loc': store.geo_loc,
            'opened': store.opened
        }

        context['editing'] = True
        context['data_form'] = StoreForm(initial=data, on_edit=True)
        context['store'] = store
        return context
    """
    #login_url para q cuando intente entrar al panel,los redireciones ahi