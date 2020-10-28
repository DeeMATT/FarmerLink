# Generated by Django 3.1.2 on 2020-10-28 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ussdConnect', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='phoneNumber',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='users',
            name='userId',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='CropOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.TextField()),
                ('crop', models.TextField()),
                ('QuantityInNumber', models.TextField(null=True)),
                ('entryId', models.TextField()),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ussdConnect.users')),
            ],
        ),
        migrations.CreateModel(
            name='CropAvailability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.TextField()),
                ('crop', models.TextField()),
                ('location', models.TextField()),
                ('unitOfMeasure', models.TextField()),
                ('QuantityInNumber', models.TextField(null=True)),
                ('entryId', models.TextField()),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ussdConnect.users')),
            ],
        ),
    ]
