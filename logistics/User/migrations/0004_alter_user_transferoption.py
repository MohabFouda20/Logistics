# Generated by Django 5.0.4 on 2024-05-13 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0003_alter_user_transferoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='transferOption',
            field=models.CharField(choices=[('bank Transfer', 'bank Transfer'), ('smart wallet', 'smart wallet')], max_length=100, null=True),
        ),
    ]
