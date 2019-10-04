from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated


class CorporateViewSet(viewsets.ModelViewSet):
    """企業情報を取得
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CorporateSerializer

    def get_queryset(self):
        # ログインユーザー企業の情報のみを取得
        return models.Corporate.objects.filter(corporate=self.request.user.corporate)


class TeamList(ListAPIView):
    """チームの階層構造を取得
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TeamSerializer

    def get_queryset(self):
        # ログインユーザー企業の情報のみを取得
        return models.Team.objects.filter(corporate=self.request.user.corporate).filter(corporate=self.request.user.corporate)


class TeamViewSet(viewsets.ModelViewSet):
    """チームマスタViewSet
    一覧、登録、更新、削除処理を一括で担当
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.TeamSerializer

    def get_queryset(self):
        # ログインユーザー企業の情報のみを取得
        return models.Team.objects.filter(corporate=self.request.user.corporate)


class CustomerViewSet(viewsets.ModelViewSet):
    """顧客マスタViewSet
    一覧、登録、更新、削除処理を一括で担当
    """

    # ログイン時のみアクセス可
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.CustomerSerializer

    def get_queryset(self):
        # ログインユーザー企業の情報のみを取得
        return models.Customer.objects.filter(corporate=self.request.user.corporate)
