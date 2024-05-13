# Generated by Django 5.0.4 on 2024-05-12 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0002_alter_user_phone_alter_user_pickupaddress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('government', models.CharField(choices=[('Cairo', 'Cairo'), ('Alexandria', 'Alexandria'), ('Giza', 'Giza'), ('Sharqia', 'Sharqia'), ('Qalyubia', 'Qalyubia'), ('Ismailia', 'Ismailia'), ('Suez', 'Suez'), ('Dakahlia', 'Dakahlia'), ('Beheira', 'Beheira'), ('Aswan', 'Aswan'), ('Asyut', 'Asyut'), ('Beni Suef', 'Beni Suef'), ('Faiyum', 'Faiyum'), ('Gharbia', 'Gharbia'), ('Luxor', 'Luxor'), ('Matrouh', 'Matrouh'), ('Minya', 'Minya'), ('Monufia', 'Monufia'), ('New Valley', 'New Valley'), ('North Sinai', 'North Sinai'), ('Port Said', 'Port Said'), ('Qena', 'Qena'), ('Red Sea', 'Red Sea'), ('Sohag', 'Sohag'), ('South Sinai', 'South Sinai'), ('Kafr El Sheikh', 'Kafr El Sheikh'), ('Damietta', 'Damietta')], max_length=100)),
                ('address', models.CharField(max_length=300)),
                ('shipment_content', models.CharField(max_length=100)),
                ('shipment_weight', models.SmallIntegerField(default=1)),
                ('cod', models.IntegerField(default=0)),
                ('fees', models.IntegerField(default=0, editable=False)),
                ('shipper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
        ),
    ]
