from rest_framework import serializers
from users.serializers import UsernameSerializer
from master.serializers import CustomerListSerializer
from drf_writable_nested import WritableNestedModelSerializer
from . import models

class OrderSerializer(serializers.ModelSerializer):
    """受注伝票
    """

    class Meta:
        model = models.Order
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')


class EstimatePurchaseSerializer(serializers.ModelSerializer):
    """見積購入
    """

    class Meta:
        model = models.EstimatePurchase
        fields = ('id', 'name', 'quantity', 'price', 'amount', 'description')


class EstimateTaskSerializer(WritableNestedModelSerializer):
    """見積タスク
    """

    # ユーザー名
    user = UsernameSerializer()

    class Meta:
        model = models.EstimateTask
        fields = ('id', 'name', 'time', 'user')


class EstimateSerializer(WritableNestedModelSerializer):
    """見積伝票処理用（全データ）
    """

    # ユーザー名
    user = UsernameSerializer()
    # 顧客名
    customer = CustomerListSerializer()
    # 購入を追加
    purchases = EstimatePurchaseSerializer(many=True, allow_null=True)
    # タスクを追加
    tasks = EstimateTaskSerializer(many=True, allow_null=True)

    class Meta:
        model = models.Estimate
        fields = ('id', 'project', 'name', 'user', 'customer', 'date', 'price', 'description', 'purchases', 'tasks')


class EstimateTableSerializer(WritableNestedModelSerializer):
    """見積一覧用（簡易データ）
    """

    # 担当者と顧客はidではなく名称を表示する
    user = serializers.CharField(read_only=True)
    customer = serializers.CharField(read_only=True)

    class Meta:
        model = models.Estimate
        fields = ('id', 'project', 'name', 'user', 'customer', 'date', 'price')