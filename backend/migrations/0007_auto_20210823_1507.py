# Generated by Django 3.2.4 on 2021-08-23 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20210820_1657'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
            ],
            options={
                'db_table': 'files',
                'ordering': ['-id'],
            },
        ),
        migrations.AlterField(
            model_name='aftersupport',
            name='file',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='implement',
            name='file',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='presupport',
            name='file',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='文件'),
        ),
        migrations.AlterField(
            model_name='service',
            name='file',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='文件'),
        ),
    ]
