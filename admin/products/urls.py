from django.urls import path

from .views import ProductViewSet, UserAPIView, LoginView, ProfileView

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='products-view'),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='products-individual-view'),
    path('user', UserAPIView.as_view(), name='user-api-view'),
    path('login', LoginView.as_view(), name='login-view'),
    path('profile', ProfileView.as_view(), name='profile-view'),
]
