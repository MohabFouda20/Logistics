# Generated by Django 5.0.4 on 2024-05-13 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_alter_order_net_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='net_income',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
