# Generated by Django 5.0.4 on 2024-05-15 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_order_net_income'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cod',
            new_name='cash_on_delivery',
        ),
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('pending', 'pending'), ('ready for pickup', 'ready for pickup'), ('delivered', 'delivered'), ('canceled', 'canceled')], default='ready for pickup', editable=False, max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]