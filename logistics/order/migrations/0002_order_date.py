# Generated by Django 5.0.4 on 2024-05-13 03:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.today, editable=False),
        ),
    ]
