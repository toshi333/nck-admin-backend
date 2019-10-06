"""SalesViewsets
"""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from . import models, serializers


class BaseFormListViewSet(viewsets.ReadOnlyModelViewSet):
    """共用伝票一覧用viewSet
    参照のみ
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.BaseFormSerializer

    def get_queryset(self):
        # ログインユーザー企業の情報のみを取得
        return models.BaseForm.objects.filter(
            corporate=self.request.user.corporate)


class OrderViewSet(viewsets.ModelViewSet):
    """受注伝票ViewSet
    一覧、登録、更新、削除処理を一括で担当
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        # ログインユーザー企業の情報のみを取得
        return models.Order.objects.filter(
            corporate=self.request.user.corporate)

    def perform_create(self, serializer):
        # 作成者と企業情報をログインユーザーで登録
        serializer.save(
            form_type='order',
            corporate=self.request.user.corporate,
            created_by=self.request.user)


class EstimateListViewSet(viewsets.ReadOnlyModelViewSet):
    """見積一覧用viewSet
    参照のみ
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.EstimateListSerializer

    def get_queryset(self):
        # ログインユーザー企業の情報のみを取得
        return models.Estimate.objects.filter(
            corporate=self.request.user.corporate)


class EstimateViewSet(viewsets.ModelViewSet):
    """見積伝票ViewSet
    一覧、登録、更新、削除処理を一括で担当
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.EstimateSerializer

    def get_queryset(self):
        # ログインユーザー企業の情報のみを取得
        return models.Estimate.objects.filter(
            corporate=self.request.user.corporate)

    def perform_create(self, serializer):
        # 作成者と企業情報をログインユーザーで登録
        serializer.save(
            form_type='estimate',
            corporate=self.request.user.corporate,
            created_by=self.request.user)
