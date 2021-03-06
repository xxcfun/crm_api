# Generated by Django 3.2.4 on 2021-06-28 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0002_auto_20210628_1444'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_valid', models.BooleanField(default=True, verbose_name='是否有效')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('theme', models.CharField(max_length=256, verbose_name='拜访主题')),
                ('status', models.SmallIntegerField(choices=[(1, '线上'), (2, '线下')], default=1, verbose_name='客户拜访方式')),
                ('main', models.TextField(blank=True, max_length=1000, null=True, verbose_name='主要事宜')),
                ('next', models.TextField(blank=True, max_length=1000, null=True, verbose_name='后期规划')),
                ('remarks', models.TextField(blank=True, max_length=1000, null=True, verbose_name='拜访备注')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='record', to='customer.customer', verbose_name='客户')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='创建人')),
            ],
            options={
                'verbose_name': '客户拜访记录',
                'verbose_name_plural': '客户拜访记录',
                'db_table': 'record',
                'ordering': ['-created_at'],
            },
        ),
    ]
