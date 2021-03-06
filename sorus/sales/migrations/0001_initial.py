# Generated by Django 3.2 on 2021-06-07 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BuyMethod',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('quantity', models.IntegerField()),
                ('price', models.FloatField()),
                ('buy_date', models.DateTimeField(auto_now_add=True)),
                ('reference', models.CharField(max_length=36)),
                ('buy_method', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='sales.buymethod')),
            ],
        ),
    ]
