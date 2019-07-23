# Generated by Django 2.0.2 on 2019-07-19 14:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('esusuaapi', '0002_auto_20190719_1442'),
    ]

    operations = [
        migrations.CreateModel(
            name='EsusuMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='esusugroup',
            name='group_name',
        ),
    ]
