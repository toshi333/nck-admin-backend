# Generated by Django 2.2.5 on 2019-10-08 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_auto_20191008_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimatepurchase',
            name='memo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='estimatepurchase',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='estimatetask',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
