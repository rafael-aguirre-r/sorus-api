# Generated by Django 3.2 on 2021-06-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
