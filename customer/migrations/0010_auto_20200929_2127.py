# Generated by Django 3.1.1 on 2020-09-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20200929_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='zipCode',
            field=models.CharField(max_length=4),
        ),
    ]