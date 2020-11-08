from django.urls import path
from .views import (
    products_detailed_view,
    product_create_view,
    product_update_view,
    product_view,
    product_delete_view,
    api_products_detailed_view
)

app_name = 'products'

urlpatterns = [
    path('api_list/', api_products_detailed_view),
    path('', products_detailed_view),
    path('create/', product_create_view),
    path('<int:prod_id>/', product_view, name='product-detail'),
    path('<int:prod_id>/delete/', product_delete_view),
    path('<int:prod_id>/update/', product_update_view),
]