# Generated by Django 4.0.6 on 2022-07-23 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonetoken',
            name='token_id',
            field=models.CharField(auto_created='b9df9ff9-3d9d-459f-9eb4-28f23eb33a82', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(auto_created='674b2ff6-3404-4dbd-b3a7-8bdb8811a425', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
    ]
