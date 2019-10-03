from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField
from . import models


class TeamTreeSerializer(serializers.ModelSerializer):
    """チームツリー取得用
    django-rest-framework-recursive
    ライブラリを使って、再帰リレーションを取得
    https://github.com/beda-software/drf-writable-nested
    """
    subteams = RecursiveField(many=True)

    class Meta:
        model = models.Team
        fields = ('id', 'parentTeam', 'name',
                  'manager', 'description', 'subteams')


class TeamSerializer(serializers.ModelSerializer):
    """チーム名コンボボックス取得用
    """

    class Meta:
        model = models.Team
        fields = ('id', 'parentTeam', 'name', 'manager', 'description')


class CustomerSerializer(serializers.ModelSerializer):
    """顧客全情報用
    """

    class Meta:
        model = models.Customer
        fields = ('id', 'name', 'user')


class CustomerListSerializer(serializers.ModelSerializer):
    """顧客名取得用
    """

    class Meta:
        model = models.Customer
        fields = ('id', 'name')
