# Generated by Django 4.2.1 on 2023-06-12 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apteka', '0002_remove_customer_email_remove_medication_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='address',
            new_name='numberPhone',
        ),
    ]
