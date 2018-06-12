# Generated by Django 2.0.6 on 2018-06-11 16:19

import clients.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id_client', models.CharField(default=clients.models.create_id, editable=False, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('deviceId', models.CharField(max_length=500)),
            ],
        ),
    ]