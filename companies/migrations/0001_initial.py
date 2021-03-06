# Generated by Django 2.0.6 on 2018-06-09 00:16

import companies.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kinds_companies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id_company', models.CharField(default=companies.models.create_id, editable=False, max_length=100, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('image', models.CharField(max_length=200)),
                ('lat', models.CharField(max_length=200, null=True)),
                ('lon', models.CharField(max_length=200, null=True)),
                ('service_hour', models.CharField(max_length=200, null=True)),
                ('type_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kinds_companies.Kind_Company')),
            ],
        ),
    ]
