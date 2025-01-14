# Generated by Django 5.1.1 on 2024-10-01 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_profile_subscription_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='currency_choice',
            field=models.CharField(blank=True, choices=[('USD', 'usa_Dollar'), ('NGN', 'Nigerian Nira'), ('UGX', 'Uganda shillings'), ('KES', 'Kenyan Shillings'), ('XAF', 'Central African CFA Franc'), ('XOF', 'West African CFA Franc'), ('GBP', 'British Pound Sterling'), ('EUR', 'Euro'), ('ETB', 'Ethiopian Birr'), ('ZMW', 'Zambian Kwacha'), ('RWF', 'Rwandan Franc'), ('GHS', 'Ghanaian Cedi'), ('ZAR', 'South African Rand'), ('TZS', 'Tanzanian Shillings')], max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Subscription',
        ),
    ]
