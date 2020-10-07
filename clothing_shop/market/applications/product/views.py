from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    DeleteView,
    CreateView,
    ListView,
    UpdateView,


)
from applications.users.mixins import EmpleadoPermisoMixin
from .forms import FormProduct

# Create your views here.
from .models import (
    Product, 
    Marca, 
    Colors, 
    Category, 
    SubCategoria,
    Size,
    SizeNumber, 
)



class ProductCreateView(EmpleadoPermisoMixin, CreateView):
    template_name = "product/form_product.html"
    form_class = FormProduct
    success_url = reverse_lazy('panel_app:index')
   
    
    
class ProductDetailView(DetailView):
    template_name = "product/detail_product.html"
    model = Product




class ProductUpdateView(UpdateView):
    template_name = "product/update_product.html"
    model = Product
    fields = ('__all__')
    success_url = reverse_lazy('product_app:list-product')

    
 
        

class ProductDeleteView(EmpleadoPermisoMixin, DeleteView):
    template_name = "product/delete_product.html"
    model = Product
    success_url = reverse_lazy('product_app:list-product')


class ProductListView(ListView):
    template_name = "product/list_product.html"
    context_object_name = "productos"
    paginate_by= 2

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context["categorias"] = Category.objects.all()
        context["cantidad_productos"] = Category.objects.count_product_on_category()
        return context

    def get_queryset(self):
        kword = self.request.GET.get("kword", '')
        categoria = self.request.GET.get("categoria", '') 
        sub_categoria = self.request.GET.get("sub_categoria", '') 
        consulta = Product.objects.search_product(kword,categoria, sub_categoria)
        return consulta
  
    
