# Generated by Django 3.2 on 2021-05-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash_card_app', '0004_auto_20210521_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='date_of_entry',
            field=models.DateField(blank=True, null=True, verbose_name='Entry Date'),
        ),
    ]