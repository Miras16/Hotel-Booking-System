# Generated by Django 3.1.2 on 2020-11-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20201107_0516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, default=None),
        ),
    ]
