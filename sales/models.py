from django.db import models
from common.models import CommonInfo


class BaseForm(CommonInfo):
    """伝票情報共通モデル
    """

    FORM_STATUS = ((1, '下書き'), (2, '申請中'), (3, '差戻し'), (4, '決裁済'), (9, '中止'))

    # 伝票種類
    form_type = models.CharField(max_length=10, blank=True)
    # プロジェクト
    project = models.ForeignKey(
        'works.Project',
        blank=True,
        null=True,
        related_name='project_orders',
        on_delete=models.PROTECT)
    # 顧客名
    customer = models.ForeignKey(
        'master.Customer',
        related_name='customer_orders',
        on_delete=models.PROTECT)
    # 件名
    name = models.CharField(max_length=50)
    # 担当者
    user = models.ForeignKey(
        'users.User', related_name='user_orders', on_delete=models.PROTECT)
    # 合計金額
    price = models.IntegerField(default=0)
    # 説明
    description = models.CharField(blank=True, null=True, max_length=200)
    # 状態
    status = models.IntegerField(choices=FORM_STATUS, default=1)

    def __str__(self):
        return self.name


class Order(BaseForm):
    """受注
    """

    # 納期
    delivery_date = models.DateField()
    # 売上フラグ
    sales_flg = models.BooleanField(default=False)
    # 売上日
    sales_date = models.DateField(blank=True, null=True)
    # 売上金額
    sales_price = models.IntegerField(default=0)


class Purchase(BaseForm):
    """購入伝票
    """

    PURCHASE_CATEGORY = ((1, '設備'), (2, '研究開発'), (3, 'その他'),)

    # 分類
    category = models.IntegerField(choices=PURCHASE_CATEGORY, default=1)


class PurchaseList(CommonInfo):
    """購入品リスト
    """

    # 購入伝票
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


class Estimate(BaseForm):
    """見積伝票
    """

    PURCHASE_CATEGORY = ((1, '一括'), (2, '派遣'), (3, '継続保守'),
                         (4, '購入代行'), (5, 'その他'))

    # 分類
    category = models.IntegerField(choices=PURCHASE_CATEGORY, default=1)
    # 提出予定日
    submit_schedule = models.DateField(blank=True, null=True)
    # 原価
    cost = models.IntegerField(blank=True, default=0)


class EstimatePurchase(CommonInfo):
    """見積購入リスト
    """

    # 見積id
    estimate = models.ForeignKey(
        'sales.Estimate',
        related_name='purchases',
        on_delete=models.CASCADE)
    # 行番
    row_num = models.IntegerField(blank=True)
    # 品名
    name = models.CharField(max_length=50, blank=True, null=True)
    # 数量
    quantity = models.IntegerField(default=0)
    # 仕入単価
    purchase_price = models.IntegerField(default=0)
    # 見積単価
    estimate_price = models.IntegerField(default=0)
    # メモ
    memo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['estimate', 'row_num']

    def __str__(self):
        return self.name


class EstimateTask(CommonInfo):
    """見積タスクリスト
    """

    # 見積id
    estimate = models.ForeignKey(
        'sales.Estimate', related_name='tasks', on_delete=models.CASCADE)
    # 行番
    row_num = models.IntegerField(blank=True)
    # 件名
    name = models.CharField(max_length=50, blank=True, null=True)
    # 見積単価
    estimate_price = models.IntegerField(default=0)
    # 工数
    time = models.IntegerField(default=0)
    # 担当者
    user = models.ForeignKey(
        'users.User',
        blank=True,
        null=True,
        related_name='user_estimatetasks',
        on_delete=models.SET_NULL)
    # メモ
    memo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['estimate', 'row_num']

    def __str__(self):
        return self.name
