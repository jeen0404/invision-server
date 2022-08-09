# Generated by Django 4.0.6 on 2022-07-23 06:25

import accounts.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('organization', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhoneToken',
            fields=[
                ('token_id', models.CharField(auto_created='97cc8c01-f3af-4c38-8bfb-b0a209fc8691', max_length=36, primary_key=True, serialize=False, unique=True)),
                ('phone_number', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Phone no must be in the format of +99999999. 14 digit allowed', regex='^\\+?1?\\d{9,14}$')])),
                ('otp', models.CharField(editable=False, max_length=40)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('attempts', models.IntegerField(default=0)),
                ('used', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'OTP Token',
                'verbose_name_plural': 'OTP Tokens',
                'db_table': 'phone_token',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(auto_created='07adeb8a-bdf2-4dcc-ae47-80adadc15d69', max_length=36, primary_key=True, serialize=False, unique=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('phone_number', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Phone no must be in the format of +99999999. 14 digit allowed', regex='^\\+?1?\\d{9,14}$')])),
                ('deleted', models.BooleanField(default=False)),
                ('suspended', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('username', models.CharField(max_length=50, unique=True, validators=[django.core.validators.RegexValidator(message='only digits and numbers allowed.', regex='^[a-zA-Z0-9]+([._]?[a-zA-Z0-9]+)*$')])),
                ('name', models.CharField(default='', max_length=200)),
                ('title', models.CharField(default='', max_length=200)),
                ('profile_image', models.TextField(default='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('organization', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='organization', to='organization.organization')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
                'db_table': 'users',
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
    ]
