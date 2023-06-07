# Generated by Django 4.2.1 on 2023-06-06 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apteka', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='description',
        ),
        migrations.RemoveField(
            model_name='medication',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_date',
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='Supply',
        ),
    ]