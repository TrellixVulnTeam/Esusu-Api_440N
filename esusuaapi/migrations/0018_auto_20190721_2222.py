# Generated by Django 2.0.2 on 2019-07-21 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('esusuaapi', '0017_auto_20190720_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esusugroup',
            name='g_users',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
