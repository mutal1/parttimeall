# Generated by Django 3.2.16 on 2022-12-07 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_box', models.TextField()),
                ('content_box', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('start', models.TextField()),
                ('end', models.TextField()),
                ('area', models.TextField()),
                ('gender', models.CharField(max_length=5)),
                ('start_money', models.IntegerField()),
                ('end_money', models.IntegerField()),
                ('image', models.TextField(default='#')),
            ],
            options={
                'db_table': 'Hottimes',
            },
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Todo_list', models.TextField()),
                ('month_year', models.TextField()),
                ('day', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'Todotext',
            },
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_box', models.TextField()),
                ('content_box', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('start', models.TextField()),
                ('end', models.TextField()),
                ('area', models.TextField()),
                ('gender', models.CharField(max_length=3)),
                ('money', models.IntegerField()),
            ],
            options={
                'db_table': 'Upload',
            },
        ),
    ]
