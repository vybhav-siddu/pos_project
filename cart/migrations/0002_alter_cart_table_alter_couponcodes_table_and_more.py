# Generated by Django 4.2.3 on 2023-08-15 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='cart',
        ),
        migrations.AlterModelTable(
            name='couponcodes',
            table='coupon_codes',
        ),
        migrations.AlterModelTable(
            name='couponoutletlink',
            table='coupon_outlet_link',
        ),
        migrations.AlterModelTable(
            name='customercuponusage',
            table='customer_coupon_usage',
        ),
        migrations.AlterModelTable(
            name='influencercouponcodes',
            table='influencer_coupon_codes',
        ),
    ]
