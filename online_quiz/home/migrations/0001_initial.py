# Generated by Django 3.0.2 on 2020-01-18 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=25)),
                ('user_type', models.CharField(max_length=20)),
                ('user_email', models.EmailField(max_length=70)),
                ('user_points', models.IntegerField()),
            ],
        ),
    ]
