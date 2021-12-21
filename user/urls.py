from django.urls import path
from .views import RegisterView, ChangePasswordView, UpdateProfileView, LogoutAllView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name="auth_register"),
    path('change_password/<int:pk>/', ChangePasswordView.as_view(), name='auth_change_password'),
    path('change_profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_password'),
    path('logout/', LogoutAllView.as_view(), name='auth_logout'),
    path('logout_all', LogoutAllView.as_view(), name='auth_logout_all'),
]
