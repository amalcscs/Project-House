# Generated by Django 4.0.2 on 2022-06-20 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionanswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform_name', models.CharField(default='', max_length=200)),
                ('q1', models.CharField(max_length=300)),
                ('a1', models.CharField(max_length=300)),
            ],
        ),
    ]
