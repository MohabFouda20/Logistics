# Generated by Django 5.0.4 on 2024-05-13 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_alter_user_transferoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='transferOption',
            field=models.CharField(choices=[('smart wallet', 'smart wallet'), ('bank Transfer', 'bank Transfer')], max_length=100, null=True),
        ),
    ]
