# Generated by Django 2.2.3 on 2019-07-29 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190729_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrollment',
            field=models.CharField(max_length=10),
        ),
    ]