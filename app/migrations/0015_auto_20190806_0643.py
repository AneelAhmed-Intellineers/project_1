# Generated by Django 2.2.3 on 2019-08-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20190806_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enrollment',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
