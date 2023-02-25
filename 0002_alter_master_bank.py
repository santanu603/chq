# Generated by Django 4.1.5 on 2023-01-24 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chq_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='bank',
            field=models.CharField(choices=[('SBI', 'State Bank of India'), ('Bandhan Bank', 'Bandhan Bank'), ('HDFC Bank', 'HDFC Bank'), ('IDBI Bank', 'IDBI Bank'), ('Axis Bank', 'Axis Bank'), ('Union Bank of India', 'Union Bank of India'), ('Kotak Mahindra Bank', 'Kotak Mahindra Bank'), ('Indian Bank', 'Indian Bank'), ('Punjab National bank', 'Punjab National bank'), ('Bank of Baroda', 'Bank of Baroda'), ('Indian Overseas Bank', 'Indian Overseas Bank'), ('Central Bank of India', 'Central Bank of India'), ('Canara Bank', 'Canara Bank'), ('UCO Bank', 'UCO Bank')], max_length=50),
        ),
    ]
