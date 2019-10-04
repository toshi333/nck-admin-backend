from django.db import models
import uuid


class Corporate(models.Model):
    """企業マスタ
    """

    # 主キーuuid
    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    # 企業名
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Team(models.Model):
    """チームマスタ
    """

    # 主キーuuid
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    parentTeam = models.ForeignKey(
        'self', blank=True, null=True, related_name='subteams', on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    manager = models.ForeignKey('users.User', blank=True, null=True,
                                related_name='management_teams', on_delete=models.SET_NULL)
    description = models.CharField(blank=True, max_length=200)

    # 所属企業
    corporate = models.ForeignKey(
        'master.Corporate',
        db_index=True,
        blank=True,
        null=True,
        related_name='corporate_teams',
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name


class Customer(models.Model):
    """顧客マスタ
    """

    # 主キーuuid
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=200)
    user = models.ForeignKey('users.User', blank=True, null=True,
                             related_name='user_customers', on_delete=models.SET_NULL)
    # 所属企業
    corporate = models.ForeignKey(
        'master.Corporate',
        db_index=True,
        blank=True,
        null=True,
        related_name='corporate_customers',
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name
