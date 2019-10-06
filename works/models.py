from django.db import models
from common.models import CommonInfo


class Project(CommonInfo):
    """プロジェクト（案件）
    """

    CATEGORYS = (('社外', '社外'), ('社内', '社内'))

    # プロジェクトコード（作番）
    code = models.CharField(max_length=10)
    # 件名
    name = models.CharField(max_length=200)
    # 分類
    category = models.CharField(max_length=10, choices=CATEGORYS)
    # 顧客
    customer = models.ForeignKey(
        'master.Customer',
        related_name='customer_projects',
        on_delete=models.PROTECT)
    # 所属
    team = models.ForeignKey(
        'master.Team',
        related_name='team_projects',
        on_delete=models.SET_DEFAULT,
        default='不明')
    # 説明
    description = models.CharField(max_length=200, blank=True, null=True)
    estimate_price = models.IntegerField()
    estimate_date = models.DateField()
    closed_flg = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Task(CommonInfo):
    """作業タスク
    """

    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Result(CommonInfo):
    """作業実績
    """

    task = models.ForeignKey(
        'works.Task',
        related_name='task_work_results',
        on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(
        'users.User',
        related_name='user_work_results',
        on_delete=models.PROTECT)
    date = models.DateField()
    hours = models.IntegerField()

    def __str__(self):
        return self.name
