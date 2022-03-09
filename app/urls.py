from django.urls import path
from .views import dashboard, UserListView, UserCreate , UserUpdate, UserDelete

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('user/', UserListView.as_view(), name='user-list'),
    path('user/add/', UserCreate.as_view(), name='user-add'),
    path('user/<int:pk>/', UserUpdate.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', UserDelete.as_view(), name='user-delete'),
]