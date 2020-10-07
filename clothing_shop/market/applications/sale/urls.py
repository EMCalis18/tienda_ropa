from django.urls import path

from . import views

app_name = "sale_app"

urlpatterns = [
    path(
        'venta/index/', 
        views.AddCarView.as_view(),
        name='sale-index',
    ),
    path(
        'carshop/update/less/<pk>/', 
        views.CarShopUpdateLessView.as_view(),
        name='carshop-update-less',
    ),
    path(
        'carshop/update/more/<pk>/', 
        views.CarShopUpdateMoreView.as_view(),
        name='carshop-update-more',
    ),
    path(
        'carshop/delete/<pk>/', 
        views.CarShopDeleteView.as_view(),
        name='carshop-delete',
    ),
    path(
        'carshop/delete-all/', 
        views.CarShopDeleteAll.as_view(),
        name='carshop-delete_all',
    ),
    path(
        'venta/simple/', 
        views.ProcesoVentaSimpleView.as_view(),
        name='venta-simple',
    ),
    path(
        'venta/voucher/', 
        views.ProcesoVentaVoucherView.as_view(),
        name='venta-voucher',
    ),
    path(
        'venta/voucher-pdf/<pk>/', 
        views.VentaVoucherPdf.as_view(),
        name='venta-voucher_pdf',
    ),
    path(
        'venta/ultimas-ventas/', 
        views.SaleListView.as_view(),
        name='venta-list',
    ),
    path(
        'venta/delete/<pk>/', 
        views.SaleDeleteView.as_view(),
        name='venta-delete',
    ),
]