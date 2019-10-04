# Generated by Django 2.2.5 on 2019-10-04 05:35

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20191004_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='corporate',
            field=models.ForeignKey(blank=True, default=uuid.uuid4, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='corporate_members', to='master.Corporate'),
        ),
    ]