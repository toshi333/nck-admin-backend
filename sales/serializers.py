from drf_writable_nested import WritableNestedModelSerializer
from rest_framework import serializers

from users.serializers import UsernameSerializer
from . import models


class BaseFormSerializer(serializers.ModelSerializer):
    """共通伝票
    """
    # ユーザー名と顧客名を追加する
    user_name = serializers.StringRelatedField(source='user')
    customer_name = serializers.StringRelatedField(source='customer')

    class Meta:
        model = models.BaseForm
        fields = (
            'id',
            'form_type',
            'status',
            'project',
            'customer',
            'customer_name',
            'name',
            'price',
            'user',
            'user_name')


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
        fields = ('id', 'row_num', 'name', 'quantity',
                  'purchase_price', 'estimate_price', 'memo')


class EstimateTaskSerializer(serializers.ModelSerializer):
    """見積タスク
    """

    class Meta:
        model = models.EstimateTask
        fields = ('id', 'row_num', 'name',
                  'estimate_price', 'time', 'user', 'memo')


class EstimateSerializer(WritableNestedModelSerializer):
    """見積伝票処理用（全データ）
    """

    # 購入を追加
    purchases = EstimatePurchaseSerializer(
        many=True, required=False, allow_null=True)
    # タスクを追加
    tasks = EstimateTaskSerializer(many=True, required=False, allow_null=True)

    class Meta:
        model = models.Estimate
        fields = ('id', 'form_type', 'status', 'project', 'name', 'user', 'customer',
                  'price', 'description', 'purchases', 'tasks')


class EstimateListSerializer(serializers.ModelSerializer):
    """見積一覧用（簡易データ）
    """

    # ユーザー名と顧客名を追加する
    user_name = serializers.StringRelatedField(source='user')
    customer_name = serializers.StringRelatedField(source='customer')

    class Meta:
        model = models.Estimate
        fields = ('id', 'project', 'name', 'user', 'user_name',
                  'customer_name', 'customer', 'price')
