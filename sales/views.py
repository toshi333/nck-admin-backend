from rest_framework import viewsets
from rest_framework.response import Response
from . import models, serializers
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    """受注伝票ViewSet
    一覧、登録、更新、削除処理を一括で担当
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)

    # 全件検索
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer


class EstimateViewSet(viewsets.ModelViewSet):
    """見積伝票ViewSet
    一覧、登録、更新、削除処理を一括で担当
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)

    # 全件検索
    queryset = models.Estimate.objects.all()
    serializer_class = serializers.EstimateSerializer

    def list(self, request):
        queryset = models.Estimate.objects.all()
        serializer = serializers.EstimateListSerializer(queryset, many=True)
        return Response(serializer.data)


class EstimatePurchaseViewSet(viewsets.ModelViewSet):
    """見積伝票ViewSet
    一覧、登録、更新、削除処理を一括で担当
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)

    # 全件検索
    queryset = models.EstimatePurchase.objects.all()
    serializer_class = serializers.EstimatePurchaseSerializer


class EstimateTaskViewSet(viewsets.ModelViewSet):
    """見積伝票ViewSet
    一覧、登録、更新、削除処理を一括で担当
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)

    # 全件検索
    queryset = models.EstimateTask.objects.all()
    serializer_class = serializers.EstimateTaskSerializer
