# Generated by Django 3.1.3 on 2020-11-07 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vacancy', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('html_text', models.TextField(verbose_name='Текст для пользователя с картинками')),
                ('stage', models.IntegerField(default=1, verbose_name='Номер стадии')),
                ('vacancy_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vacancy.vacancy', verbose_name='Какая вакансия')),
            ],
            options={
                'verbose_name': 'Текст',
                'verbose_name_plural': 'Тексты',
            },
        ),
    ]
