# Generated by Django 3.1.1 on 2020-09-29 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20200929_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='status',
            field=models.CharField(max_length=15),
        ),
    ]
