# Generated by Django 4.1 on 2024-07-01 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BngJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('eligibility', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PuneJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('company', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('eligibility', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.BigIntegerField()),
            ],
        ),
    ]
