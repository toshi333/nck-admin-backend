# Generated by Django 2.2.5 on 2019-10-04 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20191004_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='corporate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corporate_members', to='master.Corporate'),
        ),
    ]
