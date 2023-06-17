
from django.urls import path, include

from address.views import AddressAPICreate, AddressAPIRetrieveUpdateDelete
from custom_users.views import ActivateUser
from orders.views import OrderInfoAPICreate, OrderInfoAPIRetrieve, OrdersAPIListAll, OrdersAPIRetrieve, OrdersAPICreate, \
    OrdersAPIByUserId, OrdersAPIRetrieveUpdateDestroy, OrderInfoAPIRetrieveUpdateDestroy
from products.views import BasketsAPIRetrieve, \
    ProductsAPICreate, ProductInfoAPIRetrieve, ProductsAPIRetrieve, BasketsAPIRetrieveUpdate, VisibleProductsAPIList, \
    ProductsAPIList, ProductsAPIUpdateDelete, ProductInfoAPIUpdateDelete, ProductInfoAPICreate
from comments.views import CommentsAPICreate, CommentsAPIDelete, CommentsAPIListAll


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('accounts/activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),

    path('api/v1/address/create', AddressAPICreate.as_view()),
    path('api/v1/address/<int:pk>/', AddressAPIRetrieveUpdateDelete.as_view()),

    path('api/v1/baskets/update/<int:pk>/', BasketsAPIRetrieveUpdate.as_view()),  # id = clients
    path('api/v1/baskets/list/<int:pk>/', BasketsAPIRetrieve.as_view()),  # id = clients

    path('api/v1/comments/create', CommentsAPICreate.as_view()),
    path('api/v1/comments/list_all', CommentsAPIListAll.as_view()),  # Get All Comments by product ID
    path('api/v1/comments/delete/<int:pk>/', CommentsAPIDelete.as_view()),


    path('api/v1/orders/create', OrdersAPICreate.as_view()),
    path('api/v1/orders/retrieve/<int:pk>/', OrdersAPIRetrieve.as_view()),
    path('api/v1/orders/rud/<int:pk>/', OrdersAPIRetrieveUpdateDestroy.as_view()),
    path('api/v1/orders/list_all', OrdersAPIListAll.as_view()),
    path('api/v1/orders/list_client',  OrdersAPIByUserId.as_view()), # требует /?user=<id>

    path('api/v1/order-info/retrieve/<int:pk>/', OrderInfoAPIRetrieve.as_view()),
    path('api/v1/order-info/create', OrderInfoAPICreate.as_view()),
    path('api/v1/order-info/rud/<int:pk>/', OrderInfoAPIRetrieveUpdateDestroy.as_view()),

    path('api/v1/products/visible_list<int:pk>/', VisibleProductsAPIList.as_view()),
    path('api/v1/products/create', ProductsAPICreate.as_view()),
    path('api/v1/products/list_all', ProductsAPIList.as_view()),
    path('api/v1/products/retrieve/<int:pk>/', ProductsAPIRetrieve.as_view()),
    path('api/v1/products/rud/<int:pk>/', ProductsAPIUpdateDelete.as_view()),

    path('api/v1/products-info/create', ProductInfoAPICreate.as_view()),
    path('api/v1/products-info/retrieve/<int:pk>/', ProductInfoAPIRetrieve.as_view()),
    path('api/v1/products-info/rud/<int:pk>/', ProductInfoAPIUpdateDelete.as_view()),

]
