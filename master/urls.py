from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'master'

router = DefaultRouter()

# チームマスタ
router.register(r'team', views.TeamViewSet)
# 顧客マスタ
router.register(r'customer', views.CustomerViewSet)

urlpatterns = [
    path('', include(router.urls))
]