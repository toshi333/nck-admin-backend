from django.db import models
import uuid


class CommonInfoQuerySet(models.QuerySet):
    """標準利用クエリセット
    必要ならここに書く
    """


class CommonInfoManager(models.Manager.from_queryset(CommonInfoQuerySet)):
    """共通情報マネージャー
    必要ならここに書く
    """


class CommonInfo(models.Model):
    """全モデルの基礎モデル
    uuidを主キー
    マルチテナントのための企業コード
    作成、更新情報
    """

    # 主キーuuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    # 所属企業
    corporate = models.ForeignKey(
        'master.Corporate',
        db_index=True,
        blank=True,
        null=True,
        related_name='%(app_label)s_%(class)s_corporate',
        on_delete=models.SET_NULL
    )
    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)
    # 作成者
    created_by = models.ForeignKey(
        'users.User',
        blank=True,
        null=True,
        related_name='%(app_label)s_%(class)s_created_by',
        on_delete=models.SET_NULL)
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)
    # 更新者
    updated_by = models.ForeignKey(
        'users.User',
        blank=True,
        null=True,
        related_name='%(app_label)s_%(class)s_updated_by',
        on_delete=models.SET_NULL)

    objects = CommonInfoManager()

    class Meta:
        # 抽象基底クラス化
        # これでDBテーブルが生成されない
        abstract = True
