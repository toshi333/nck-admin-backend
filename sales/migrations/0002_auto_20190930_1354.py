# Generated by Django 2.2.5 on 2019-09-30 04:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sales', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('works', '0001_initial'),
        ('master', '0002_auto_20190930_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_purchases', to='works.Project'),
        ),
        migrations.AddField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_purchases', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer_orders', to='master.Customer'),
        ),
        migrations.AddField(
            model_name='order',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_orders', to='works.Project'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='estimatetask',
            name='estimate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='sales.Estimate'),
        ),
        migrations.AddField(
            model_name='estimatetask',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_estimatetasks', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='estimatepurchase',
            name='estimate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='sales.Estimate'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='customer_estimates', to='master.Customer'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_estimates', to='works.Project'),
        ),
        migrations.AddField(
            model_name='estimate',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_estimates', to=settings.AUTH_USER_MODEL),
        ),
    ]