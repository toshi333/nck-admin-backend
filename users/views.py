from rest_framework import viewsets
from django_filters import rest_framework as filters
from users.models import User
from users.serializers import UserSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class UserListFilter(filters.FilterSet):
    """社員一覧で使う検索条件の定義
    """

    # フィルタの定義（ここで定めた項目で検索条件が指定出来るようになる）
    code = filters.CharFilter(field_name="code", lookup_expr='contains')
    last_name = filters.CharFilter(
        field_name="last_name", lookup_expr='contains')
    team = filters.CharFilter(field_name="team", lookup_expr='exact')

    class Meta:
        model = User
        fields = ['code', 'team']


class UserViewSet(viewsets.ModelViewSet):
    """ユーザー情報ViewSet
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    filter_class = UserListFilter
    ordering_fields = ['code']
    ordering = ['code']


class UserProfileViewSet(viewsets.ModelViewSet):
    """プロフィール更新ViewSet
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
