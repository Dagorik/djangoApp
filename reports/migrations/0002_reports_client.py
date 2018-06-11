# Generated by Django 2.0.6 on 2018-06-11 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20180611_1622'),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='client',
            field=models.ForeignKey(default='as', on_delete=django.db.models.deletion.CASCADE, to='clients.Client'),
            preserve_default=False,
        ),
    ]
