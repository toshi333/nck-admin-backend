# Generated by Django 2.2.5 on 2019-10-04 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0003_corporate'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='corporate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corporate_customers', to='master.Corporate'),
        ),
        migrations.AddField(
            model_name='team',
            name='corporate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='corporate_teams', to='master.Corporate'),
        ),
    ]
