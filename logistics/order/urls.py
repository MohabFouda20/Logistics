from django.urls import path
from .views import orderListCreate, OrderRetrieve, OrderUpdate, OrderDelete


urlpatterns = [
    path('', orderListCreate.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderRetrieve.as_view(), name='order-retrieve'),
    path('<int:pk>/update/', OrderUpdate.as_view(), name='order-update'),
    path('<int:pk>/delete/', OrderDelete.as_view(), name='order-delete'),
]
