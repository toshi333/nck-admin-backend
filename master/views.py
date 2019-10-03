from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated


class TeamList(ListAPIView):
    """チームの階層構造を取得
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)

    queryset = models.Team.objects.filter(parentTeam__isnull=True)
    serializer_class = serializers.TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """チームマスタViewSet
    一覧、登録、更新、削除処理を一括で担当
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)

    # 全件検索
    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """顧客マスタViewSet
    一覧、登録、更新、削除処理を一括で担当
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)

    # 全件検索
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer

    def list(self, request):
        queryset = models.Customer.objects.all()
        serializer = serializers.CustomerListSerializer(queryset, many=True)
        return Response(serializer.data)
