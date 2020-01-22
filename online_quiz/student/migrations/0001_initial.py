# Generated by Django 3.0.2 on 2020-01-22 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=40, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
