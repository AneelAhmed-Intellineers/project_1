# Generated by Django 2.2.3 on 2019-08-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20190805_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrollment',
            field=models.CharField(max_length=50),
        ),
    ]
