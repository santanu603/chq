# Generated by Django 4.1.4 on 2023-02-05 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chq_app', '0004_remove_master_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
