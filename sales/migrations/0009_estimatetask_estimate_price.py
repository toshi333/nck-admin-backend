# Generated by Django 2.2.5 on 2019-10-08 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0008_auto_20191008_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimatetask',
            name='estimate_price',
            field=models.IntegerField(default=0),
        ),
    ]
