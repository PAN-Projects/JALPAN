# Generated by Django 4.1.3 on 2023-01-14 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_delete_orders'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='food_catagory',
            new_name='food_category',
        ),
    ]
