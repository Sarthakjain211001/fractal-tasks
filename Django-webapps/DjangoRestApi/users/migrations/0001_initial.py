# Generated by Django 5.1.3 on 2024-12-04 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(default='', max_length=70)),
                ('password', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
