from django.contrib import admin
from django.urls import path, include


api_urlpatterns = [
    path('auth/', include('users.urls')),
    path('master/', include('master.urls')),
    path('sales/', include('sales.urls')),
    path('works/', include('works.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
]

# 開発環境でメディアファイルにアクセスする
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)