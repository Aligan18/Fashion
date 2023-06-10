"""
URL configuration for testBackend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another UR
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from address.views import AddressAPICreate, AddressAPIRetrieveUpdateDelete
from custom_users.views import ActivateUser
from orders.views import OrderInfoAPICreate, OrderInfoAPIRetrieve, OrdersAPIListAll, OrdersAPIRetrieve, OrdersAPICreate
from products.views import BasketsAPICreate, BasketsAPIRetrieve, ProductsAPIListAll, \
    ProductsAPICreate, ProductsAPIDelete, ProductInfoAPIRetrieve, ProductInfoAPIUpdate, ProductInfoAPICreate, \
    ProductsAPIUpdate, ProductsAPIRetrieve
from comments.views import CommentsAPICreate, CommentsAPIDelete, CommentsAPIListAll

from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'products', ProductsAPICreate, ProductsAPIListAll)


class ProductsAPIVisibleList:
    pass


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('accounts/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),

    path('api/v1/address/create', AddressAPICreate.as_view()),
    path('api/v1/address/<int:pk>/', AddressAPIRetrieveUpdateDelete.as_view()),

    path('api/v1/baskets/create', BasketsAPICreate.as_view()),
    path('api/v1/baskets/retrieve/<int:pk>/', BasketsAPIRetrieve.as_view()),

    path('api/v1/comments/create', CommentsAPICreate.as_view()),
    path('api/v1/comments/list_all', CommentsAPIListAll.as_view()),
    path('api/v1/comments/delete/<int:pk>/', CommentsAPIDelete.as_view()),
    # Get All Comments by product ID

    path('api/v1/orders/create', OrdersAPICreate.as_view()),
    path('api/v1/orders/retrieve/<int:pk>/', OrdersAPIRetrieve.as_view()),
    path('api/v1/orders/list_all', OrdersAPIListAll.as_view()),
    # Order by user ID

    path('api/v1/order/info/retrieve/<int:pk>/', OrderInfoAPIRetrieve.as_view()),
    path('api/v1/order/info/create', OrderInfoAPICreate.as_view()),

    # path('api/v1/products/visible_list<int:pk>/', ProductsAPIVisibleList.as_view()),
    path('api/v1/products/create', ProductsAPICreate.as_view()),
    # path('api/v1/products/visible_list_by_category', ProductsAPIVisibleListByCategory.as_view()),
    path('api/v1/products/list_all', ProductsAPIListAll.as_view()),
    path('api/v1/products/delete/<int:pk>/', ProductsAPIDelete.as_view()),
    path('api/v1/products/retrieve/<int:pk>/', ProductsAPIRetrieve.as_view()),
    path('api/v1/products/update/<int:pk>/', ProductsAPIUpdate.as_view()),

    path('api/v1/products/info/retrieve/<int:pk>/', ProductInfoAPIRetrieve.as_view()),
    path('api/v1/products/info/update/<int:pk>/', ProductInfoAPIUpdate.as_view()),
    path('api/v1/products/info/create', ProductInfoAPICreate.as_view()),
]


