# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-10 01:08
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=16, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_account', models.CharField(blank=True, max_length=14, null=True, unique=True)),
                ('associated_currency', models.CharField(choices=[('S', 'SOLES'), ('D', 'DOLARES'), ('E', 'EUROS')], max_length=1)),
                ('current_balance', models.DecimalField(decimal_places=4, default=0, max_digits=7)),
                ('maintenance_cost', models.DecimalField(decimal_places=4, default=0, max_digits=7)),
                ('cancellation_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastname', models.CharField(max_length=50)),
                ('mothers_lastname', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1)),
                ('birthdate', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('district', models.CharField(blank=True, max_length=100, null=True)),
                ('membership_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('document_type', models.CharField(choices=[('DNI', 'DNI')], default='DNI', max_length=3)),
                ('document_number', models.CharField(max_length=8, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]{8,8}$', 'DNI require 8 digitos.', 'Invalid number')])),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_card', models.IntegerField(blank=True, null=True, unique=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('num_cvv', models.IntegerField(blank=True, null=True)),
                ('validity_status', models.BooleanField(default=True)),
                ('blocking_status', models.BooleanField(default=False)),
                ('num_pin', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CreditCard'),
        ),
        migrations.AddField(
            model_name='account',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Client'),
        ),
        migrations.AddField(
            model_name='user',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Client'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]