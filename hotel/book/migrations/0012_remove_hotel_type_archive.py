# Generated by Django 4.0.3 on 2022-05-09 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_category_transaction_room_id_user_user_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='type',
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tracking_id', models.CharField(default='000', max_length=64)),
                ('first_name', models.CharField(default=None, max_length=64)),
                ('last_name', models.CharField(default=None, max_length=64)),
                ('email', models.CharField(default=None, max_length=64)),
                ('phone', models.CharField(default=None, max_length=64)),
                ('room', models.IntegerField(default=1)),
                ('adult', models.IntegerField(default=1)),
                ('child', models.IntegerField(default=0)),
                ('checkin_date', models.CharField(default=None, max_length=64)),
                ('checkout_date', models.CharField(default=None, max_length=64)),
                ('booking_date', models.DateTimeField(auto_now_add=True)),
                ('price', models.CharField(default=None, max_length=64)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='archive', to='book.hotel')),
                ('user', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='archive', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
