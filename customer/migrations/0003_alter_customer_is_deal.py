# Generated by Django 3.2.4 on 2021-07-12 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20210628_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='is_deal',
            field=models.SmallIntegerField(blank=True, choices=[(1, '成交'), (0, '未成交')], default=0, null=True, verbose_name='是否成交'),
        ),
    ]