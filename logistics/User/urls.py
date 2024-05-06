from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.UserListCreate.as_view()),
    path('<int:pk>/' ,views.UserRetrieve.as_view()),
    path('retrieve/<int:pk>/' ,views.UserUpdate.as_view()),
    path('retrieve/<int:pk>/' ,views.Userdelete.as_view()),
]