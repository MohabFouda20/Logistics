# Generated by Django 5.0.4 on 2024-05-13 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0006_alter_user_transferoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='transferOption',
            field=models.CharField(choices=[('smart wallet', 'smart wallet'), ('bank Transfer', 'bank Transfer')], max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='PickupRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('number_of_orders', models.IntegerField(blank=True, null=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.user')),
            ],
        ),
    ]
