from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'master'

router = DefaultRouter()

# 企業マスタ
router.register(r'corporate', views.CorporateViewSet, basename="Corporate")
# チームマスタ
router.register(r'team', views.TeamViewSet, basename="Team")
# 顧客マスタ
router.register(r'customer', views.CustomerViewSet, basename="Customer")

urlpatterns = [
    path('', include(router.urls))
]
