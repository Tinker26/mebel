# Generated by Django 3.1.1 on 2021-12-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('icons', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]