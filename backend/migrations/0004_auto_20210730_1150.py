# Generated by Django 3.2.4 on 2021-07-30 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_rename_pre_user_presupport_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aftersupport',
            old_name='after_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='implement',
            old_name='imp_user',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='ser_user',
            new_name='user',
        ),
    ]
