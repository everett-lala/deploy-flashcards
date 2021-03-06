# Generated by Django 3.2 on 2021-05-29 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash_card_app', '0010_auto_20210526_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=10, verbose_name='Word')),
            ],
        ),
        migrations.CreateModel(
            name='WordEight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=10, verbose_name='Word')),
            ],
        ),
        migrations.CreateModel(
            name='WordFive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=10, verbose_name='Word')),
            ],
        ),
        migrations.CreateModel(
            name='WordSeven',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=10, verbose_name='Word')),
            ],
        ),
        migrations.CreateModel(
            name='WordSix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=10, verbose_name='Word')),
            ],
        ),
    ]
