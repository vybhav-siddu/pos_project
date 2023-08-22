# Generated by Django 4.2.3 on 2023-08-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveSubscriptions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('subscription_id', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Cancelled', 'Cancelled')], default='Inactive', max_length=20)),
                ('created_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('renewed_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cancelled_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('expiry_on', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_id', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=20)),
                ('transaction_hash', models.CharField(max_length=255)),
                ('created_on', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.CharField(max_length=255)),
                ('features', models.JSONField()),
            ],
        ),
    ]
