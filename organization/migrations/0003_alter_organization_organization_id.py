# Generated by Django 4.0.6 on 2022-07-23 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_alter_organization_organization_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='organization_id',
            field=models.CharField(default='31050acd-77fb-4dd6-8d19-5d4d6ae4811d', max_length=36, primary_key=True, serialize=False, unique=True),
        ),
    ]
