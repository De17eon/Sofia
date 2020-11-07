# Generated by Django 3.1.3 on 2020-11-06 08:01

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('authsystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('name_company', models.CharField(max_length=255, verbose_name='Название компании')),
                ('FIO_CEO', models.CharField(max_length=255, verbose_name='ФИО Директора')),
                ('Phone_CEO', models.CharField(max_length=12, verbose_name='Телефон Директора')),
                ('Email_CEO', models.CharField(max_length=100, verbose_name='Почта Директора')),
                ('FIO_Contact', models.CharField(max_length=255, verbose_name='ФИО Конатктного лица')),
                ('Phone_Contact', models.CharField(max_length=12, verbose_name='Телефон Конактного лица')),
                ('Email_Contact', models.CharField(max_length=12, verbose_name='Почта Конатктного лица')),
                ('description', models.TextField(verbose_name='О компании')),
                ('img_logo', models.ImageField(blank=True, upload_to='', verbose_name='Логотип компании')),
                ('place', models.CharField(max_length=300, verbose_name='Адрес компании')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]