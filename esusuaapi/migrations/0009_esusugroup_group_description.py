# Generated by Django 2.0.2 on 2019-07-20 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esusuaapi', '0008_esusugroup'),
    ]

    operations = [
        migrations.AddField(
            model_name='esusugroup',
            name='group_description',
            field=models.CharField(default='', max_length=300),
        ),
    ]
