from django.db import models
import uuid


class Order(models.Model):
    """受注
    """

    # 主キーuuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    # プロジェクト
    project = models.ForeignKey('works.Project', related_name='project_orders', on_delete=models.PROTECT)
    # 受注名
    name = models.CharField(max_length=50)
    # 担当者
    user = models.ForeignKey('users.User', related_name='user_orders', on_delete=models.PROTECT)
    # 顧客名
    customer = models.ForeignKey('master.Customer', related_name='customer_orders', on_delete=models.PROTECT)
    # 受注日
    date = models.DateField()
    # 受注金額
    price = models.IntegerField(default=0)
    # 納期
    delivery_date = models.DateField()
    # 説明
    description = models.CharField(max_length=200)
    # 売上フラグ
    sales_flg = models.BooleanField(default=False)
    # 売上日
    sales_date = models.DateField(blank=True, null=True)
    # 売上金額
    sales_price = models.IntegerField(default=0)

    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    """購入
    """

    # 主キーuuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    # プロジェクトid
    project = models.ForeignKey('works.Project', related_name='project_purchases', on_delete=models.PROTECT)
    # 件名
    name = models.CharField(max_length=50)
    # 担当者
    user = models.ForeignKey('users.User', related_name='user_purchases', on_delete=models.PROTECT)
    # 顧客名
    customer = models.ForeignKey('master.Customer', related_name='customer_purchases', on_delete=models.PROTECT)
    # 作成日
    date = models.DateField()
    # 説明
    description = models.CharField(max_length=200)

    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PurchaseList(models.Model):
    """購入品リスト
    """

    # 主キーuuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    # 購入id
    purchase = models.ForeignKey('sales.Purchase', on_delete=models.CASCADE)
    # 品名
    name = models.CharField(max_length=50)
    # 数量
    quantity = models.IntegerField(default=0)
    # 単価
    price = models.IntegerField(default=0)
    # 金額
    amount = models.IntegerField(default=0)
    # 説明
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Estimate(models.Model):
    """見積
    """

    # 主キーuuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    # プロジェクトid
    project = models.ForeignKey('works.Project', related_name='project_estimates', on_delete=models.PROTECT)
    # 件名
    name = models.CharField(max_length=50)
    # 担当者
    user = models.ForeignKey('users.User', related_name='user_estimates', on_delete=models.PROTECT)
    # 顧客名
    customer = models.ForeignKey('master.Customer', related_name='customer_estimates', on_delete=models.PROTECT)
    # 見積日
    date = models.DateField()
    # 見積金額
    price = models.IntegerField(default=0)
    # 説明
    description = models.CharField(max_length=200)

    # 作成日時
    created_at = models.DateTimeField(auto_now_add=True)
    # 更新日時
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class EstimatePurchase(models.Model):
    """見積購入リスト
    """

    # 主キーuuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    # 見積id
    estimate = models.ForeignKey('sales.Estimate', related_name='purchases', on_delete=models.CASCADE)
    # 品名
    name = models.CharField(max_length=50)
    # 数量
    quantity = models.IntegerField(default=0)
    # 単価
    price = models.IntegerField(default=0)
    # 金額
    amount = models.IntegerField(default=0)
    # 説明
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class EstimateTask(models.Model):
    """見積タスクリスト
    """

    # 主キーuuid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    # 見積id
    estimate = models.ForeignKey('sales.Estimate', related_name='tasks', on_delete=models.CASCADE)
    # 品名
    name = models.CharField(max_length=50)
    # 工数
    time = models.IntegerField(default=0)
    # 担当者
    user = models.ForeignKey('users.User', blank=True, null=True, related_name='user_estimatetasks', on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
