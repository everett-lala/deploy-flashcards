# Generated by Django 3.2 on 2021-05-21 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash_card_app', '0002_rename_states_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='state',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='state',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='state',
            name='capital',
            field=models.CharField(max_length=255, verbose_name="State's capital"),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Name of State'),
        ),
    ]