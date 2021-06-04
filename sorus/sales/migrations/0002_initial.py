# Generated by Django 3.2 on 2021-06-02 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('offers', '0002_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sales', '0001_initial'),
        ('status', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='buyer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sale',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='offers.product'),
        ),
        migrations.AddField(
            model_name='sale',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='buymethod',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='status.state'),
        ),
    ]
