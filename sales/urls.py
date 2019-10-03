from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'sales'

router = DefaultRouter()

# 受注伝票ViewSetの登録
router.register(r'order', views.OrderViewSet)
# 見積伝票ViewSetの登録
router.register(r'estimate', views.EstimateViewSet)

urlpatterns = [
    path('', include(router.urls))
]