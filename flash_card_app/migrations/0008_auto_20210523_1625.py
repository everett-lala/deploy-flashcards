# Generated by Django 3.2 on 2021-05-23 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flash_card_app', '0007_auto_20210523_1619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='add_count',
        ),
        migrations.RemoveField(
            model_name='state',
            name='capital_count',
        ),
        migrations.RemoveField(
            model_name='state',
            name='div_count',
        ),
        migrations.RemoveField(
            model_name='state',
            name='flag_count',
        ),
        migrations.RemoveField(
            model_name='state',
            name='multi_count',
        ),
        migrations.RemoveField(
            model_name='state',
            name='shape_count',
        ),
        migrations.RemoveField(
            model_name='state',
            name='sub_count',
        ),
    ]
