# Generated by Django 2.0.6 on 2018-06-11 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0003_auto_20180611_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id_client',
            field=models.CharField(max_length=200, primary_key=True, serialize=False),
        ),
    ]
