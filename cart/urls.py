from django.urls import path
from . import views

urlpatterns=[
    path('cartDetails',views.cart_details,name='cartDetails'),
    path('addd/<int:product_id>/',views.add_cart,name='addcart'),
    path('delete/<int:product_id>',views.del_cart,name='delcart'),
    path('remove/<int:product_id>',views.remv_cart,name='remvcart')
]