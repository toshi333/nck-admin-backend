from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'sales'

router = DefaultRouter()

# 受注伝票ViewSetの登録
router.register(r'baseform-list', views.BaseFormListViewSet, basename='BaseForm')
# 受注伝票ViewSetの登録
router.register(r'order', views.OrderViewSet, basename='Order')
# 見積伝票ViewSetの登録
router.register(r'estimate', views.EstimateViewSet, basename='Estimate')
# 見積一覧ViewSetの登録
router.register(r'estimate-list', views.EstimateListViewSet, basename='Estimate')

urlpatterns = [
    path('', include(router.urls))
]
