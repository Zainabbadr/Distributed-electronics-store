# Generated by Django 5.0.4 on 2024-05-03 18:59

import django.core.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Electronics_App', '0021_update_remaining_quantity_alter_cart_cart_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='Cart_id',
            field=models.UUIDField(default=uuid.UUID('ff31f964-2c78-4cc1-a9da-0b5b2041e3cb'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='update',
            name='remaining_quantity',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
