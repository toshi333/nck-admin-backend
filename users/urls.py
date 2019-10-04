from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'users'

user_router = DefaultRouter()

# ユーザーマスタ用
user_router.register(r'user', views.UserViewSet, basename='User')
# ログイン者のプロフィール用
user_router.register(r'profile', views.UserProfileViewSet, basename="User")

urlpatterns = [
    path('', include(user_router.urls)),
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('google/', views.GoogleLogin.as_view(), name='google_login'),
]
