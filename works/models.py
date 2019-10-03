from django.db import models
import uuid


class Project(models.Model):
    """プロジェクト（案件）
    """

    CATEGORYS = ((1, '社外'), (2, '社内'))

    # 主キーuuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=10, choices=CATEGORYS)
    customer = models.ForeignKey('master.Customer', related_name='customer_projects', on_delete=models.PROTECT)
    team = models.ForeignKey('master.Team', related_name='team_projects', on_delete=models.SET_DEFAULT, default='不明')
    description = models.CharField(max_length=200, blank=True, null=True)
    estimate_price = models.IntegerField()
    estimate_date = models.DateField()
    closed_flg = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    """作業タスク
    """

    # 主キーuuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    name = models.CharField(max_length=50, blank=True, null=True)
    def __str__(self):
        return self.name


class Result(models.Model):
    """作業実績
    """

    # 主キーuuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    task = models.ForeignKey('works.Task', related_name='task_work_results', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('users.User', related_name='user_work_results', on_delete=models.PROTECT)
    date = models.DateField()
    hours = models.IntegerField()

    def __str__(self):
        return self.name