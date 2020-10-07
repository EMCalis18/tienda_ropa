from django.urls import path

from . import views

app_name = "product_app"

urlpatterns = [
    path(
        'create/producto/', 
        views.ProductCreateView.as_view(),
        name='create-product',
    ),
    path(
        'detail/producto/<pk>/', 
        views.ProductDetailView.as_view(),
        name='detail-product',
    ),
    path(
        'delete/producto/<pk>/', 
        views.ProductDeleteView.as_view(),
        name='delete-product',
    ),
    path(
        'list/producto/', 
        views.ProductListView.as_view(),
        name='list-product',
    ),
    path(
        'update/producto/<pk>/', 
        views.ProductUpdateView.as_view(),
        name='update-product',
    ),

   
]