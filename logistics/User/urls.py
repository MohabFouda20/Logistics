from django.urls import path
from . import views

urlpatterns = [
    path('' ,views.UserListCreate.as_view()),
    path('<int:pk>/' ,views.UserRetrieve.as_view()),
    path('Update/<int:pk>/' ,views.UserUpdate.as_view()),
    path('Delete/<int:pk>/' ,views.Userdelete.as_view()),
    
    # pickup request urls
    # path('pickup/' ,views.PickupListCreate.as_view()),
    # path('pickup/edit/<int:pk>/' ,views.pickupEdit.as_view()),
    # path('pickup/delete/<int:pk>/' ,views.pickupDelete.as_view()),
    
]