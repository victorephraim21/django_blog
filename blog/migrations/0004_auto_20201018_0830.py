# Generated by Django 3.1.1 on 2020-10-18 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20201015_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='location',
            field=models.TextField(default='Dar es Salaam', max_length=50),
        ),
    ]