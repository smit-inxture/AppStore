# Generated by Django 4.2.2 on 2023-06-28 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('play_store', '0003_alter_appdetails_developerid_alter_appdetails_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appdetails',
            name='installs',
            field=models.CharField(max_length=100),
        ),
    ]
