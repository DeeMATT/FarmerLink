# Generated by Django 3.1.2 on 2020-10-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ussdConnect', '0002_auto_20201028_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='phoneNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='users',
            name='userId',
            field=models.IntegerField(default=0),
        ),
    ]