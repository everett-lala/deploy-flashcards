# Generated by Django 3.2 on 2021-05-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash_card_login_app', '0006_auto_20210523_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='add_count',
            field=models.IntegerField(blank=True, default=0, verbose_name='Correct Addition'),
        ),
        migrations.AlterField(
            model_name='user',
            name='capital_count',
            field=models.IntegerField(blank=True, default=0, verbose_name='Correct State capitals'),
        ),
        migrations.AlterField(
            model_name='user',
            name='div_count',
            field=models.IntegerField(blank=True, default=0, verbose_name='Correct Dvision'),
        ),
        migrations.AlterField(
            model_name='user',
            name='flag_count',
            field=models.IntegerField(blank=True, default=0, verbose_name='Correct State flags'),
        ),
        migrations.AlterField(
            model_name='user',
            name='multi_count',
            field=models.IntegerField(blank=True, default=0, verbose_name='Correct Multiplication'),
        ),
        migrations.AlterField(
            model_name='user',
            name='shape_count',
            field=models.IntegerField(blank=True, default=0, verbose_name='Correct State shapes'),
        ),
        migrations.AlterField(
            model_name='user',
            name='sub_count',
            field=models.IntegerField(blank=True, default=0, verbose_name='Correct Subtraction'),
        ),
    ]
