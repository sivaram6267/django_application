# Generated by Django 4.1 on 2024-07-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0002_bngjobs_punejobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hydjobs',
            name='company',
            field=models.CharField(max_length=64),
        ),
    ]