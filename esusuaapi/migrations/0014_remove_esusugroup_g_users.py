# Generated by Django 2.0.2 on 2019-07-20 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('esusuaapi', '0013_auto_20190720_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='esusugroup',
            name='g_users',
        ),
    ]
