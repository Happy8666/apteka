# Generated by Django 4.2.1 on 2023-06-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apteka', '0003_rename_address_customer_numberphone'),
    ]

    operations = [
        migrations.AddField(
            model_name='medication',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
