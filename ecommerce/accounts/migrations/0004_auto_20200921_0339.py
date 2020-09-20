# Generated by Django 3.0 on 2020-09-20 21:39

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_order_billing_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='countries',
        ),
        migrations.AddField(
            model_name='billingaddress',
            name='country',
            field=django_countries.fields.CountryField(default='Bangladesh', max_length=2),
            preserve_default=False,
        ),
    ]