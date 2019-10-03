from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

app_name = 'works'

router = DefaultRouter()

# ProjectViewSetの登録
router.register(r'project', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]