from django.db import models
from common.models import CommonInfo


class Corporate(CommonInfo):
    """企業マスタ
    """

    # 企業名
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class AutoNum(CommonInfo):
    """伝票連番マスタ
    """
    # 伝票分類
    from_type = models.CharField(max_length=20)
    # 現在No
    num = models.IntegerField(default=0)


class Team(CommonInfo):
    """チームマスタ
    """

    parentTeam = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='subteams',
        on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    manager = models.ForeignKey(
        'users.User',
        blank=True,
        null=True,
        related_name='management_teams',
        on_delete=models.SET_NULL)
    description = models.CharField(blank=True, max_length=200)

    def __str__(self):
        return self.name


class Customer(CommonInfo):
    """顧客マスタ
    """

    name = models.CharField(max_length=200)
    user = models.ForeignKey(
        'users.User',
        blank=True,
        null=True,
        related_name='user_customers',
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
