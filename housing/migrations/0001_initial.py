# Generated by Django 4.0.5 on 2022-09-27 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]