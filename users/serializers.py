from rest_framework import serializers
from rest_auth.models import TokenModel
from users.models import User


class UserProfileSerializer(serializers.ModelSerializer):
    """プロフィール更新用
    """

    class Meta:
        model = User
        fields = ('id', 'code', 'email', 'team', 'username', 'first_name',
                  'last_name', 'is_staff', 'is_active', 'last_login', 'avatar', 'corporate')


class UserSerializer(serializers.ModelSerializer):
    """ユーザー一覧更新用
    """

    team_name = serializers.StringRelatedField(source='team')

    class Meta:
        model = User
        fields = ('id', 'code', 'email', 'team', 'team_name', 'username',
                  'first_name', 'last_name', 'is_staff', 'is_active', 'corporate')


class UsernameSerializer(serializers.ModelSerializer):
    """ユーザーオートコンプリート名称のみ取得用
    """

    class Meta:
        model = User
        fields = ('id', 'username')


class LoginUserSerializer(serializers.ModelSerializer):
    """ログイン成功後のResponse情報用
    """

    user = UserProfileSerializer()

    class Meta:
        model = TokenModel
        fields = ('key', 'user')
