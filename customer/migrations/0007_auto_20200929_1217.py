# Generated by Django 3.1.1 on 2020-09-29 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20200923_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profilePic',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
